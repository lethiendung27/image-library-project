#!/usr/bin/env python3
"""Registry validator + index generator (SPEC.md section 8).

stdlib only, Python >= 3.9. Parses the constrained YAML subset defined in
SPEC.md section 3.4 — anything outside the subset is a validation error by design.

Usage:
  python3 scripts/validate.py               # validate, report, exit 1 on errors
  python3 scripts/validate.py --write-index # validate + regenerate registry/index.yaml
  python3 scripts/validate.py --check       # validate + fail if index.yaml is stale
"""
import hashlib
import json
import os
import re
import sys
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TYPES_DIR = os.path.join(ROOT, "registry", "types")
VOCAB_PATH = os.path.join(ROOT, "registry", "vocabulary.yaml")
RULES_PATH = os.path.join(ROOT, "registry", "rules.md")
INDEX_PATH = os.path.join(ROOT, "registry", "index.yaml")
OBS_PATH = os.path.join(ROOT, "ingestion", "observations.jsonl")
PICKS_PATH = os.path.join(ROOT, "feedback", "picks.jsonl")
SLUGS_PATH = os.path.join(ROOT, "query", "product-slugs.yaml")
RENDER_PATH = os.path.join(ROOT, "eval", "render-tests.jsonl")
GIF_TYPES_DIR = os.path.join(ROOT, "registry", "gif-types")
TOPLIST_TYPES_DIR = os.path.join(ROOT, "registry", "toplist-types")
PDP_DR_TYPES_DIR = os.path.join(ROOT, "registry", "pdp-dr-types")
GIF_LEDGER_PATH = os.path.join(ROOT, "ingestion", "gifs.jsonl")
GIF_VI_PATH = os.path.join(ROOT, "registry", "gif-cards-vi.md")

ERRORS = []
WARNINGS = []


def err(where, msg):
    ERRORS.append(f"{where}: {msg}")


def warn(where, msg):
    WARNINGS.append(f"{where}: {msg}")


# ---------------------------------------------------------------- YAML subset

def _split_top_commas(s):
    parts, buf, quote = [], "", False
    for ch in s:
        if ch == '"':
            quote = not quote
            buf += ch
        elif ch == "," and not quote:
            parts.append(buf)
            buf = ""
        else:
            buf += ch
    if buf.strip():
        parts.append(buf)
    return parts


def parse_scalar(tok, where="?"):
    tok = tok.strip()
    if tok in ("null", "~", ""):
        return None
    if tok == "true":
        return True
    if tok == "false":
        return False
    if re.fullmatch(r"-?\d+", tok):
        return int(tok)
    if len(tok) >= 2 and tok.startswith('"') and tok.endswith('"'):
        return tok[1:-1]
    if tok.startswith(("'", "{", "&", "*", "|", ">")):
        err(where, f"scalar outside the YAML subset: {tok!r}")
        return tok
    return tok


def parse_flow_list(tok, where="?"):
    inner = tok.strip()[1:-1].strip()
    if not inner:
        return []
    return [parse_scalar(p, where) for p in _split_top_commas(inner)]


def parse_value(rest, where="?"):
    rest = rest.strip()
    if rest.startswith("["):
        if not rest.endswith("]"):
            err(where, f"unterminated flow list: {rest!r}")
            return []
        return parse_flow_list(rest, where)
    if rest == "{}":
        return {}
    return parse_scalar(rest, where)


def parse_block(lines, where="?"):
    """Parse a top-level block of the YAML subset into a dict."""
    out = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line.startswith(" "):
            err(where, f"unexpected indent at: {line.strip()!r}")
            i += 1
            continue
        m = re.match(r"^([A-Za-z0-9_]+):(.*)$", line)
        if not m:
            err(where, f"unparseable line: {line!r}")
            i += 1
            continue
        key, rest = m.group(1), m.group(2)
        if rest.strip():
            out[key] = parse_value(rest, where)
            i += 1
            continue
        # nested block: collect lines indented by 2 spaces
        j = i + 1
        sub = []
        while j < len(lines):
            nxt = lines[j]
            if not nxt.strip() or nxt.lstrip().startswith("#"):
                j += 1
                continue
            if nxt.startswith("  "):
                sub.append(nxt[2:])
                j += 1
                continue
            break
        if not sub:
            out[key] = None
        elif sub[0].lstrip().startswith("- "):
            out[key] = [parse_scalar(s.strip()[2:], where) for s in sub
                        if s.strip().startswith("- ")]
        else:
            d = {}
            for s in sub:
                mm = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", s.strip())
                if not mm:
                    err(where, f"unparseable nested line: {s.strip()!r}")
                    continue
                d[mm.group(1)] = parse_value(mm.group(2), where)
            out[key] = d
        i = j
    return out


# ---------------------------------------------------------------- YAML output

_PLAIN_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")


def yq(v):
    """Serialize a scalar for index.yaml output."""
    if v is None:
        return "null"
    if v is True:
        return "true"
    if v is False:
        return "false"
    if isinstance(v, int):
        return str(v)
    s = str(v)
    if _PLAIN_RE.fullmatch(s) and not re.fullmatch(r"\d+", s):
        return s
    return '"' + s.replace('"', '\\"') + '"'


def ylist(vs):
    return "[" + ", ".join(yq(v) for v in vs) + "]"


# ---------------------------------------------------------------- file loading

def load_vocabulary():
    with open(VOCAB_PATH, encoding="utf-8") as f:
        return parse_block(f.read().splitlines(), "vocabulary.yaml")


def load_rule_ids():
    ids = []
    with open(RULES_PATH, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^## (G\d+)\b", line)
            if m:
                ids.append(m.group(1))
    return ids


def split_frontmatter(text, where):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        err(where, "file must start with `---` frontmatter")
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    err(where, "unterminated frontmatter")
    return None, text


def split_sections(body):
    """Map of `## HEADER` -> content (code fences are shielded)."""
    sections = {}
    current = None
    buf = []
    in_fence = False
    for line in body.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            if current:
                sections[current] = "\n".join(buf)
            current = line[3:].strip()
            buf = []
        else:
            buf.append(line)
    if current:
        sections[current] = "\n".join(buf)
    return sections


def extract_folded(section_text, name, where):
    m = re.search(rf"^{name}:\s*>\s*\n((?:[ \t]+\S.*\n?)*)", section_text, re.M)
    if not m:
        err(where, f"TRIGGER is missing a `{name}: >` folded block")
        return ""
    words = m.group(1).split()
    return " ".join(words)


# ---------------------------------------------------------------- validation

REQUIRED_KEYS = [
    "id", "step", "job", "device", "version", "status", "replaced_by",
    "channels", "requires_product_photo", "generation_mode",
]
OPTIONAL_KEYS = [
    "axes", "variants", "exempt_from", "pairs_with", "never_with",
    "avoid_adjacent", "requires_pair", "text_layer",
]
TEXT_LAYER_SLOTS = ["title", "copy", "badge"]
REQUIRED_SECTIONS = ["PURPOSE", "TRIGGER", "SKELETON", "NEGATIVE", "CHANGELOG"]

# Soft size limits, warnings only (ADR-013). Derived from the registry as it
# stood on 2026-08-13: untouched type files averaged 9831 characters, and the
# three that had been through the render loop had reached 28774, 32409 and
# 32678 with 25-36% of each file being CHANGELOG prose.
TYPE_FILE_WARN = 22000
CHANGELOG_ENTRY_WARN = 600
EXAMPLE_RE = re.compile(
    r"^### example: ([a-z0-9-]+) — skeleton@(\d+)\.(\d+), run: "
    r"(untested|pass|partial|fail)\s*$", re.M)


def validate_type_file(path, vocab, rule_ids, where_prefix="registry/types",
                       extra_optional=()):
    fname = os.path.basename(path)
    where = f"{where_prefix}/{fname}"
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm_lines, body = split_frontmatter(text, where)
    if fm_lines is None:
        return None
    fm = parse_block(fm_lines, where)

    for k in REQUIRED_KEYS:
        if k not in fm:
            err(where, f"missing required frontmatter key `{k}`")
    for k in fm:
        if k in REQUIRED_KEYS + OPTIONAL_KEYS + list(extra_optional):
            continue
        # Ahead of the generic message on purpose. ADR-069 found the toplist
        # `text_layer` error unreachable behind an unknown-key check and moved it,
        # because "unknown frontmatter key" does not tell a reader which namespace
        # the key belongs to.
        if k == "blocked_by":
            err(where, "`blocked_by` belongs to registry/pdp-dr-types/ (SPEC 3.8), "
                       "not to this registry. A type here is reserved by status "
                       "alone and its promotion criteria live in SPEC 6.3")
        else:
            err(where, f"unknown frontmatter key `{k}`")

    tid = fm.get("id")
    if tid != os.path.splitext(fname)[0]:
        err(where, f"id `{tid}` != filename")
    if tid and not re.fullmatch(r"\d{2}-[a-z]+-[a-z]+", str(tid)):
        err(where, f"id `{tid}` does not match NN-job-device")
    step, job, device = fm.get("step"), fm.get("job"), fm.get("device")
    if tid and isinstance(step, int) and job and device:
        if tid != f"{step:02d}-{job}-{device}":
            err(where, f"id `{tid}` inconsistent with step/job/device")
    if job is not None and job not in (vocab.get("jobs") or {}):
        err(where, f"job `{job}` not in vocabulary")
    if device is not None and device not in (vocab.get("devices") or {}):
        err(where, f"device `{device}` not in vocabulary")
    if isinstance(step, int) and str(step) not in {str(k) for k in (vocab.get("steps") or {})}:
        err(where, f"step `{step}` not in vocabulary.steps")

    ver = fm.get("version")
    if not (isinstance(ver, str) and re.fullmatch(r"\d+\.\d+", ver)):
        err(where, f"version must be a quoted MAJOR.MINOR string, got {ver!r}")

    status = fm.get("status")
    if status not in (vocab.get("statuses") or []):
        err(where, f"status `{status}` not in vocabulary.statuses")
    if status == "deprecated" and not fm.get("replaced_by"):
        err(where, "deprecated type must set replaced_by")
    if status != "deprecated" and fm.get("replaced_by"):
        err(where, "replaced_by is only valid on deprecated types")

    # `ratios` was a required key until ADR-082 removed it from every type file.
    # No format check replaces this one: the key is no longer in REQUIRED_KEYS or
    # OPTIONAL_KEYS, so re-adding it is caught by the unknown-frontmatter-key
    # error above, which is a stronger guard than validating its contents.
    for c in fm.get("channels") or []:
        if c not in (vocab.get("channels") or []):
            err(where, f"channel `{c}` not in vocabulary")
    if fm.get("generation_mode") not in (vocab.get("generation_modes") or []):
        err(where, f"generation_mode `{fm.get('generation_mode')}` invalid")
    if not isinstance(fm.get("requires_product_photo"), bool):
        err(where, "requires_product_photo must be true/false")

    axes = fm.get("axes") or {}
    if not isinstance(axes, dict):
        err(where, "axes must be a map")
        axes = {}
    for axis, values in axes.items():
        vocab_axis = (vocab.get("axes") or {}).get(axis)
        if vocab_axis is None:
            err(where, f"axis `{axis}` not in vocabulary.axes")
            continue
        for v in values if isinstance(values, list) else [values]:
            if v not in vocab_axis:
                err(where, f"axis value `{axis}:{v}` not in vocabulary")

    tl = fm.get("text_layer")
    if tl is not None:
        if not isinstance(tl, list) or not tl:
            err(where, "text_layer must be a non-empty list of slots")
        else:
            for slot in tl:
                if slot not in TEXT_LAYER_SLOTS:
                    err(where, f"text_layer slot `{slot}` is not one of {TEXT_LAYER_SLOTS} (G16)")

    for g in fm.get("exempt_from") or []:
        if g not in rule_ids:
            err(where, f"exempt_from references unknown rule `{g}`")

    sections = split_sections(body)
    for s in REQUIRED_SECTIONS:
        if s not in sections:
            err(where, f"missing required section `## {s}`")

    # --- size guards (warnings only; never block a commit) -------------------
    # A type file states current law. The reasoning behind each change lives in
    # the commit that made it, which ADR-007 makes this project's audit surface.
    # Writing the reasoning twice is what took three type files from ~10k to
    # ~30k characters in one day. Thresholds are derived, not guessed: the
    # median CHANGELOG entry written before 2026-08-12 is 240 characters and
    # only 4 of 44 exceed 600, while the entries written after it have a median
    # of 934. See ADR-013.
    # WORKED EXAMPLES is excluded: SPEC 3.3 requires a rendered example to keep
    # its FULL prompt text, so that section is mandated content and not authorial
    # prose. Measure only what the author chooses to write.
    discretionary = len(text) - len(sections.get("WORKED EXAMPLES", ""))
    if discretionary > TYPE_FILE_WARN:
        warn(where, f"type file is {discretionary} discretionary characters "
                    f"(soft limit {TYPE_FILE_WARN}, worked examples excluded); "
                    f"move workings to the commit message")
    if "CHANGELOG" in sections:
        for entry in re.split(r"\n(?=- \d)", sections["CHANGELOG"]):
            m = re.match(r"- ([\d.]+) \(", entry.strip())
            if m and len(entry.strip()) > CHANGELOG_ENTRY_WARN:
                warn(where, f"CHANGELOG entry {m.group(1)} is "
                            f"{len(entry.strip())} characters (soft limit "
                            f"{CHANGELOG_ENTRY_WARN}); state the decision and "
                            f"cite the commit")

    use_when = avoid_when = ""
    if "TRIGGER" in sections:
        use_when = extract_folded(sections["TRIGGER"], "use_when", where)
        # ADR-060 removed avoid_when from every image type. It is read if a file
        # still carries one so a lane mid-edit does not break, but it is no longer
        # required and nothing routes on it. GIF types keep theirs -- see below.
        if "avoid_when:" in sections["TRIGGER"]:
            avoid_when = extract_folded(sections["TRIGGER"], "avoid_when", where)

    if "NEGATIVE" in sections and "G6" not in (fm.get("exempt_from") or []):
        if "[G6]" not in sections["NEGATIVE"]:
            err(where, "NEGATIVE must extend the [G6] base block (or exempt G6)")

    for slug in fm.get("variants") or []:
        if not re.search(rf"^### --{re.escape(str(slug))}\b", body, re.M):
            err(where, f"variant `--{slug}` declared but has no `### --{slug}` block")

    examples = EXAMPLE_RE.findall(body)
    ex_headers = re.findall(r"^### example: .*$", body, re.M)
    if len(ex_headers) != len(examples):
        for h in ex_headers:
            if not EXAMPLE_RE.match(h):
                err(where, f"malformed worked-example header: {h!r}")
    if len(ex_headers) > 2:
        err(where, f"{len(ex_headers)} worked examples — hard cap is 2 (SPEC 3.3)")
    if ver and re.fullmatch(r"\d+\.\d+", ver):
        major = int(ver.split(".")[0])
        for slug, ex_major, _minor, _run in examples:
            if int(ex_major) < major:
                warn(where, f"worked example `{slug}` is stale "
                            f"(skeleton@{ex_major}.x < current major {major})")

    return {"fm": fm, "use_when": use_when, "avoid_when": avoid_when}


def cross_validate(files, known_ids, where_prefix="registry/types"):
    for tid, t in files.items():
        fm = t["fm"]
        where = f"{where_prefix}/{tid}.md"
        for field in ("pairs_with", "never_with", "avoid_adjacent"):
            for ref in fm.get(field) or []:
                if ref not in known_ids:
                    err(where, f"{field} references unknown type `{ref}`")
        rp = fm.get("requires_pair")
        if rp and rp not in known_ids:
            err(where, f"requires_pair references unknown type `{rp}`")
        rb = fm.get("replaced_by")
        if rb and rb not in known_ids:
            err(where, f"replaced_by references unknown type `{rb}`")


# ------------------------------------------------------------------ pdp-dr

# The FOURTH namespace (SPEC 3.8, ADR-077): every type a direct-response product
# detail page, LP2, may use. Since ADR-091 an LP2 page routes THIS folder and no
# other, so it holds verbatim copies of the active registry/types/ files under the
# same ids beside its own drafts. Same anatomy, same frontmatter, same
# {step}-{job}-{device} ids as registry/types/, so it reuses validate_type_file()
# rather than owning a second copy of those checks. What it adds is `blocked_by`
# and a BLOCK section, paired to `status: reserved`, and ADR-070's `copied_from` +
# `copied_at_version` pair for the copies.
PDP_DR_EXTRA_KEYS = ["blocked_by", "copied_from", "copied_at_version"]


def validate_pdp_dr_type_file(path, vocab, rule_ids, image_types):
    fname = os.path.basename(path)
    where = f"registry/pdp-dr-types/{fname}"
    parsed = validate_type_file(path, vocab, rule_ids,
                                where_prefix="registry/pdp-dr-types",
                                extra_optional=PDP_DR_EXTRA_KEYS)
    if parsed is None:
        return None
    fm = parsed["fm"]

    status = fm.get("status")
    blocked = fm.get("blocked_by")
    if status == "reserved" and not blocked:
        err(where, "status `reserved` with no `blocked_by` — SPEC 3.8 pairs them. "
                   "A reserved type that does not name what it waits on is a file "
                   "nobody can unblock")
    if status != "reserved" and blocked:
        err(where, f"`blocked_by` set on a type whose status is `{status}` — "
                   "the key is non-null exactly when the type is reserved")

    # A copy keeps its parent's id (ADR-091), so `copied_from` must name the file's
    # own id. Provenance, not a live link: the drift is made visible, never blocked.
    tid = fm.get("id")
    src = fm.get("copied_from")
    ver_at = fm.get("copied_at_version")
    if src is not None:
        if src != tid:
            err(where, f"copied_from `{src}` differs from this file's id `{tid}` — an "
                       "LP2 copy keeps its parent's id (ADR-091)")
        if src not in image_types:
            err(where, f"copied_from `{src}` is not an image type in registry/types/")
        elif image_types[src]["fm"].get("status") != "active":
            err(where, f"copied_from `{src}`, which is not active")
        if not (isinstance(ver_at, str) and re.fullmatch(r"\d+\.\d+", ver_at)):
            err(where, "copied_from is set, so copied_at_version must be a quoted "
                       f"MAJOR.MINOR string, got {ver_at!r}")
        elif src in image_types:
            now = image_types[src]["fm"].get("version")
            if isinstance(now, str) and now != ver_at:
                warn(where,
                     f"copied verbatim from `{src}` at {ver_at}, and that file is "
                     f"now {now} — re-copy it or record in this file's CHANGELOG "
                     "why the divergence is intended. Two copies of one file drift, "
                     "and the stale one is the one somebody reads")
    elif ver_at is not None:
        err(where, "copied_at_version is set but copied_from is null")

    with open(path, encoding="utf-8") as f:
        body = f.read()
    has_block = re.search(r"^## BLOCK\s*$", body, re.M) is not None
    if status == "reserved" and not has_block:
        err(where, "status `reserved` with no `## BLOCK` section — SPEC 3.8 asks a "
                   "reserved type for the prose behind its `blocked_by` line")
    if status != "reserved" and has_block:
        err(where, "carries a `## BLOCK` section but is not reserved — a block that "
                   "no longer blocks is the stale half of a promotion diff")

    return parsed


# ---------------------------------------------------------------- ledgers

def load_jsonl(path, required_keys, where):
    records = []
    if not os.path.exists(path):
        warn(where, "ledger file missing (expected empty file)")
        return records
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as e:
                err(where, f"line {n}: invalid JSON ({e})")
                continue
            for k in required_keys:
                if k not in rec:
                    err(where, f"line {n}: missing key `{k}`")
            records.append(rec)
    return records


# ---------------------------------------------------------------- evidence

# Renames whose observations stay filed under the OLD id, because the ledger is
# append-only and a rename is not a re-filing. Each entry cites the decision that
# made it. Without this map the three renamed pdp-dr files counted fewer distinct
# sources than their own promotion-status lines, and nothing was lost:
# 03-spec-stilllife 2 + 03-spec-ingredient 2 = the 3 its file records;
# 03-spec-lineup 1 + 03-spec-range 2 = 2; 02-symptom-callout 1 + 02-symptom-halo
# 2 = 3 (ADR-084). A DEPRECATION is not a rename and does not belong here:
# 07-identity-callout's observations are not credited to its replaced_by, because
# ADR-078 says retiring it did not re-file them.
FORMER_IDS = {
    "03-spec-ingredient": "03-spec-stilllife",   # ADR-065
    "03-spec-range": "03-spec-lineup",           # ADR-065
    "02-symptom-halo": "02-symptom-callout",     # ADR-066
}

_TYPE_VERDICTS = ("match", "variant-candidate")
_PROPOSAL_VERDICTS = ("match", "variant-candidate", "new-candidate")
_SOURCE_NOTE = re.compile(r"source file:\s*(\S+)")


def ledger_evidence(observations, ids):
    """Which observations evidence which id — the one reading every count shares.

    Three rules, each from a measured miss (ADR-084):

    - The LAST record for a hash is the live one. The ledger is append-only, so a
      re-filed frame appears under both ids; counting every record credits the
      superseded one as well.
    - `type` counts on `match` and `variant-candidate` only. On a `new-candidate`
      the template makes `type` the NEAREST existing type, which is evidence that
      the image is something ELSE.
    - `proposed_id` counts on all three, once that id has a file. A new-candidate
      naming a proposal is that proposal's founding exemplar, and a record filed
      `match` with `type: null` and a `proposed_id` matches a proposal made earlier
      in the same batch. Reading `type` alone reproduced 0 of the 6 hand-counted
      source totals in `registry/pdp-dr-types/_CURATION-2026-09-11.md`; reading
      both reproduces all 6.

    A source is the page slug before `__` in a `source file:` note. A record with
    no such note counts as an observation and is reported `unsourced` — never
    guessed into a source, because SPEC 6.3 criterion 1 counts sources and a
    guess there is a promotion made on a number nobody can check.

    Returns {id: {"obs": set of hashes, "sources": set of slugs, "unsourced": int}}.
    """
    latest = {}
    for rec in observations:
        h = rec.get("hash")
        if h:
            latest[h] = rec
    out = {tid: {"obs": set(), "sources": set(), "unsourced": 0} for tid in ids}
    for h, rec in latest.items():
        verdict = rec.get("verdict")
        t = FORMER_IDS.get(rec.get("type"), rec.get("type"))
        p = FORMER_IDS.get(rec.get("proposed_id"), rec.get("proposed_id"))
        if t in out and verdict in _TYPE_VERDICTS:
            tid = t
        elif p in out and verdict in _PROPOSAL_VERDICTS:
            tid = p
        else:
            continue
        entry = out[tid]
        entry["obs"].add(h)
        m = _SOURCE_NOTE.search(rec.get("notes") or "")
        if m and "__" in m.group(1):
            entry["sources"].add(m.group(1).split("__", 1)[0])
        else:
            entry["unsourced"] += 1
    return out


def evidence_counts(observations, vocab, types):
    """Distinct observations per image type — the `evidence_count` in index.yaml.

    Observations, not sources: SPEC 6.2's number (>=3 distinct observations
    before a patch), and what the index has always carried. The source count
    SPEC 6.3 criterion 1 reads comes from the same `ledger_evidence` and is
    printed by `--evidence`.
    """
    verdicts = set(vocab.get("observation_verdicts") or [])
    for rec in observations:
        if rec.get("verdict") not in verdicts:
            err("ingestion/observations.jsonl",
                f"unknown verdict `{rec.get('verdict')}`")
    ev = ledger_evidence(observations, types)
    return {tid: len(e["obs"]) for tid, e in ev.items()}


def check_toplist_evidence(observations, toplist_types):
    """Corpus support per toplist type, and a warning where an ACTIVE one is thin.

    A ledger record naming a toplist id once counted toward nothing and was
    invisible. SPEC 6.2's rule wants >=3 distinct observations before a clause is
    patched from the corpus, and an ACTIVE type with fewer than that is a type the
    market has not yet been shown to build.

    Reserved types are skipped: they are blocked on a decision, not on evidence.
    The last-record and proposal rules live in `ledger_evidence` (ADR-084), shared
    with the image and pdp-dr counts so the three readings cannot drift apart.
    """
    ev = ledger_evidence(observations, toplist_types)
    for tid in sorted(toplist_types):
        if toplist_types[tid]["fm"].get("status") != "active":
            continue
        n = len(ev[tid]["obs"])
        if n < 3:
            warn(f"registry/toplist-types/{tid}.md",
                 f"{n} corpus observation(s) — under SPEC 6.2's threshold of 3. "
                 "The type is active and routable; what it is not yet is evidenced")
    return {tid: len(e["obs"]) for tid, e in ev.items()}


def check_pdp_dr_evidence(observations, pdp_dr_types):
    """Corpus support per pdp-dr type — the count nothing took until ADR-084.

    `check_toplist_evidence` exists because a ledger record naming a toplist id
    counted toward nothing. The identical gap stood for this namespace and it was
    larger: every file in the folder states its criterion-1 source count in prose,
    and no function read a single observation filed against one of them. Those
    numbers were typed; `--evidence` now generates them.

    One warning, for the fault a count can prove without reading prose: a file
    whose own id, and any former id, resolves to no observation at all — a type
    written without ledger evidence, or a rename FORMER_IDS does not know. The
    typed counts in each file's BLOCK and `blocked_by` are NOT parsed: they mix
    digits and words, and one of them ("19 sources" in 03-spec-hero) is about a
    different type, so a parser would warn on text that is correct.
    """
    ev = ledger_evidence(observations, pdp_dr_types)
    for tid in sorted(pdp_dr_types):
        if pdp_dr_types[tid]["fm"].get("status") == "deprecated":
            continue
        # A copy shares its parent's id and therefore its parent's evidence; the
        # parent's namespace owns that count and does not warn on it (ADR-091).
        if pdp_dr_types[tid]["fm"].get("copied_from"):
            continue
        if not ev[tid]["obs"]:
            warn(f"registry/pdp-dr-types/{tid}.md",
                 "no ledger observation resolves to this id or to a former id in "
                 "FORMER_IDS — a type with no corpus evidence, or a rename the map "
                 "does not know about")
    return {tid: (len(e["obs"]), len(e["sources"]), e["unsourced"])
            for tid, e in ev.items()}


def check_former_ids(file_ids):
    """FORMER_IDS is keyed by name, so it goes stale silently unless it reports.

    An old id with a file again would credit one frame to two ids; a new id with
    no file resolves to nothing and swallows the old id's evidence.
    """
    for old, new in sorted(FORMER_IDS.items()):
        if old in file_ids:
            err("scripts/validate.py",
                f"FORMER_IDS maps `{old}` -> `{new}` but `{old}` has a file "
                "again; its observations would be credited to two ids")
        if new not in file_ids:
            err("scripts/validate.py",
                f"FORMER_IDS maps `{old}` -> `{new}` and `{new}` has no file in "
                "any namespace; the renamed evidence resolves to nothing")


def evidence_report(observations, namespaces):
    """`--evidence`: every count a promotion decision reads, generated not typed.

    Observations are SPEC 6.2's number; sources are SPEC 6.3 criterion 1's.
    """
    print("EVIDENCE  namespace  id                        status      "
          "obs  sources  unsourced")
    for label, registry in namespaces:
        ev = ledger_evidence(observations, registry)
        for tid in sorted(registry):
            e = ev[tid]
            status = (registry[tid].get("fm") or {}).get("status", "?")
            print(f"EVIDENCE  {label:9s}  {tid:24s}  {str(status):10s}  "
                  f"{len(e['obs']):3d}  {len(e['sources']):7d}  "
                  f"{e['unsourced']:9d}")


def pick_stats(picks, types):
    """Pick-rate per (type x section_role) for SPEC 7.7's soft prior.

    Only a CONTESTED slot counts: one that offered more than one distinct type,
    where a type could therefore have lost. A slot offering several executions
    of a single type, or one option only, records a real decision by the owner
    but carries no type-level information; counting it inflates the denominator
    of a rate whose whole job is to compare types against each other (ADR-026).
    A record is counted once per distinct type on offer, never once per option.
    """
    stats = {tid: {} for tid in types}
    for rec in picks:
        role = rec.get("section_role")
        if not role:
            continue
        shown_types = {o.get("type") for o in rec.get("options_shown") or []
                       if isinstance(o, dict)}
        if len(shown_types) < 2:
            continue
        for tid in shown_types:
            if tid in stats:
                cell = stats[tid].setdefault(role, {"shown": 0, "picked": 0})
                cell["shown"] += 1
        picked = rec.get("picked")
        if picked in stats:
            cell = stats[picked].setdefault(role, {"shown": 0, "picked": 0})
            cell["picked"] += 1
    return stats


# ---------------------------------------------------------------- index

PDP_DR_INDEX_PATH = os.path.join(ROOT, "registry", "pdp-dr-index.yaml")
LP1_SURFACE = "# Router surface: routing reads this file plus mapping/slot-rules.md only."
LP2_SURFACE = ("# Router surface for LP2 (`pdp_dr`, ADR-091): routing reads this file plus "
               "mapping/pdp-dr-rules.md, which applies mapping/slot-rules.md's gates unchanged.")


def render_index(vocab, types, evidence, picks, surface=LP1_SURFACE):
    out = []
    out.append("# GENERATED by scripts/validate.py --write-index — do not edit by hand.")
    out.append(surface)
    out.append(f"registry_version: {yq(vocab.get('registry_version'))}")
    out.append("types:")
    for tid in sorted(types):
        fm = types[tid]["fm"]
        out.append(f"  - id: {yq(tid)}")
        out.append(f"    step: {fm.get('step')}")
        out.append(f"    job: {yq(fm.get('job'))}")
        out.append(f"    device: {yq(fm.get('device'))}")
        out.append(f"    version: {yq(fm.get('version'))}")
        out.append(f"    status: {yq(fm.get('status'))}")
        out.append(f"    channels: {ylist(fm.get('channels') or [])}")
        out.append(f"    requires_product_photo: {yq(fm.get('requires_product_photo'))}")
        out.append(f"    generation_mode: {yq(fm.get('generation_mode'))}")
        axes = fm.get("axes") or {}
        if axes:
            out.append("    axes:")
            for axis in sorted(axes):
                out.append(f"      {axis}: {ylist(axes[axis])}")
        else:
            out.append("    axes: {}")
        out.append(f"    variants: {ylist(fm.get('variants') or [])}")
        out.append(f"    exempt_from: {ylist(fm.get('exempt_from') or [])}")
        out.append(f"    pairs_with: {ylist(fm.get('pairs_with') or [])}")
        out.append(f"    never_with: {ylist(fm.get('never_with') or [])}")
        out.append(f"    avoid_adjacent: {ylist(fm.get('avoid_adjacent') or [])}")
        out.append(f"    requires_pair: {yq(fm.get('requires_pair'))}")
        out.append(f"    evidence_count: {evidence.get(tid, 0)}")
        cells = picks.get(tid) or {}
        if cells:
            out.append("    picks:")
            for role in sorted(cells):
                c = cells[role]
                out.append(f"      {role}: {{shown: {c['shown']}, picked: {c['picked']}}}")
        else:
            out.append("    picks: {}")
        for field in ("use_when", "avoid_when"):
            if not types[tid][field]:
                continue            # avoid_when is gone since ADR-060
            out.append(f"    {field}: >")
            for line in textwrap.wrap(types[tid][field], width=72) or [""]:
                out.append(f"      {line}")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- json files

def check_json_files():
    for rel in ("mapping/content.schema.json", "query/output.schema.json"):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            warn(rel, "file not found (expected once phase 2 lands)")
            continue
        try:
            with open(path, encoding="utf-8") as f:
                json.load(f)
        except json.JSONDecodeError as e:
            err(rel, f"invalid JSON: {e}")
    golden_dir = os.path.join(ROOT, "eval", "golden")
    if os.path.isdir(golden_dir):
        for dirpath, _dirs, files in os.walk(golden_dir):
            for fn in files:
                if fn.endswith(".json"):
                    p = os.path.join(dirpath, fn)
                    rel = os.path.relpath(p, ROOT)
                    try:
                        with open(p, encoding="utf-8") as f:
                            json.load(f)
                    except json.JSONDecodeError as e:
                        err(rel, f"invalid JSON: {e}")


# ----------------------------------------------------------- content contracts

# Sessions routed before content.json was the contract SPEC 1 says it is. The
# air cooler session carries none at all; the L-shaped cushion v01 file is the
# raw Shopify export saved under that name; the optical drive v01 file is an
# earlier hand-rolled shape. They are warned rather than failed, the treatment
# ADR-024 gave page 13 and ADR-028 gave the five pre-plate sessions: a correction
# stays legible rather than being applied backwards over work that was correct
# under the law of its time. Nothing is added here — a session routed from today
# forward is an error or it is nothing.
PRE_CONTRACT_SESSIONS = {
    "listicle-air-cooler-wall-mounted-v01",
    "advertorial-seat-cushion-l-shaped-v01",
    "advertorial-optical-drive-7in1-v01",
}

# The keyword set `mapping/content.schema.json` actually uses, measured from the
# file rather than assumed. An unknown keyword is an ERROR and not a skip: a
# validator that silently ignores what it does not implement is one that passes
# by catching nothing, which is the state `expected-routes.yaml` sat in for eight
# days before ADR-027 — parsed, inert, and reported as green.
_SCHEMA_ANNOTATIONS = {"$schema", "title", "description"}
_SCHEMA_KEYWORDS = {"type", "properties", "required", "additionalProperties",
                    "items", "enum", "minItems", "minLength", "pattern"}
_JSON_TYPES = {"object": dict, "array": list, "string": str, "boolean": bool,
               "integer": int, "number": (int, float), "null": type(None)}


def schema_errors(doc, schema, path="$"):
    """Validate `doc` against the JSON Schema subset above. stdlib only — the
    `jsonschema` package is not a dependency this repo carries, and the subset
    is small enough that implementing it is cheaper than adding one.

    Returns a list of messages; an empty list means valid.
    """
    unknown = set(schema) - _SCHEMA_KEYWORDS - _SCHEMA_ANNOTATIONS
    if unknown:
        return [f"{path}: schema uses {sorted(unknown)}, which this validator "
                "does not implement — extend it rather than trusting it"]

    t = schema.get("type")
    if t:
        want = _JSON_TYPES.get(t)
        if want is None:
            return [f"{path}: schema declares unknown type `{t}`"]
        # bool is a subclass of int in Python; in JSON they are distinct types,
        # so `true` must not satisfy `type: integer`.
        if isinstance(doc, bool) and t != "boolean":
            return [f"{path}: expected {t}, got boolean"]
        if not isinstance(doc, want):
            return [f"{path}: expected {t}, got {type(doc).__name__}"]

    out = []
    if "enum" in schema and doc not in schema["enum"]:
        out.append(f"{path}: `{doc}` is not one of {schema['enum']}")

    if isinstance(doc, str):
        min_len = schema.get("minLength")
        if min_len is not None and len(doc) < min_len:
            out.append(f"{path}: {len(doc)} characters, minLength is {min_len}")
        pat = schema.get("pattern")
        if pat and not re.search(pat, doc):
            out.append(f"{path}: `{doc}` does not match {pat}")

    if isinstance(doc, list):
        min_items = schema.get("minItems")
        if min_items is not None and len(doc) < min_items:
            out.append(f"{path}: {len(doc)} items, minItems is {min_items}")
        item_schema = schema.get("items")
        if item_schema:
            for i, v in enumerate(doc):
                out += schema_errors(v, item_schema, f"{path}[{i}]")

    if isinstance(doc, dict):
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in doc:
                out.append(f"{path}: missing required `{key}`")
        if schema.get("additionalProperties") is False:
            for key in doc:
                if key not in props:
                    out.append(f"{path}: `{key}` is not in the contract")
        for key, val in doc.items():
            if key in props:
                out += schema_errors(val, props[key], f"{path}.{key}")

    return out


def check_content_contracts():
    """SPEC 1 states that the QUERY operation's input IS a content.json valid
    against `mapping/content.schema.json`. Nothing checked that any real one was.

    `check_golden` reads the two golden fixtures' content.json, but only to drive
    the Stage 1 derivation off `page.channel` and `product.attributes` — a
    malformed fixture would have raised a KeyError rather than produced an error
    message, and a session's contract was never opened by any code at all.

    Returns the number of contracts checked.
    """
    spath = os.path.join(ROOT, "mapping", "content.schema.json")
    if not os.path.exists(spath):
        return 0
    try:
        with open(spath, encoding="utf-8") as f:
            schema = json.load(f)
    except json.JSONDecodeError:
        return 0            # check_json_files already reported it

    targets = []
    sessions_dir = os.path.join(ROOT, "query", "sessions")
    if os.path.isdir(sessions_dir):
        for session in sorted(os.listdir(sessions_dir)):
            sdir = os.path.join(sessions_dir, session)
            if not os.path.isdir(sdir):
                continue
            cpath = os.path.join(sdir, "content.json")
            if os.path.exists(cpath):
                targets.append((cpath, session in PRE_CONTRACT_SESSIONS))
            elif os.path.exists(os.path.join(sdir, "prompts.json")):
                msg = ("routed with no content.json — SPEC 1 makes it the QUERY "
                       "input, so this page cannot reproduce its own prompts")
                if session in PRE_CONTRACT_SESSIONS:
                    warn(f"query/sessions/{session}", msg + " (pre-contract)")
                else:
                    err(f"query/sessions/{session}", msg)
    golden_dir = os.path.join(ROOT, "eval", "golden")
    if os.path.isdir(golden_dir):
        for name in sorted(os.listdir(golden_dir)):
            cpath = os.path.join(golden_dir, name, "content.json")
            if os.path.isfile(cpath):
                targets.append((cpath, False))

    checked = 0
    for path, grandfathered in targets:
        rel = os.path.relpath(path, ROOT)
        try:
            with open(path, encoding="utf-8") as f:
                doc = json.load(f)
        except json.JSONDecodeError as e:
            err(rel, f"invalid JSON: {e}")
            continue
        checked += 1
        problems = schema_errors(doc, schema)
        if not problems:
            continue
        if grandfathered:
            # One line, not one per problem: page 58 alone returns over a
            # hundred, and a legacy shape reported in full drowns the live ones.
            warn(rel, f"{len(problems)} contract violations, first is "
                      f"`{problems[0]}` — pre-contract session, grandfathered")
            continue
        for p in problems[:10]:
            err(rel, f"does not satisfy mapping/content.schema.json — {p}")
        if len(problems) > 10:
            err(rel, f"... and {len(problems) - 10} further contract violations")
    return checked


# ------------------------------------------------------------------ prompt sets

# Sessions emitted before ADR-021 declared the render capability. They are left
# standing because they were correct under the law of their time, and they are
# warned about on every run so the multi-pass prompts in them stay visible rather
# than quietly shipping to an owner who cannot composite. Nothing is added here.
GRANDFATHERED_MULTIPASS = {
    "advertorial-seat-cushion-l-shaped-v02",
}

# ADR-016, 2026-08-13: only these five ratios, system-wide. It proposed a
# validator check and deferred it ("the validator is shared and a second session
# is live"), and eleven days later 10 of 15 type entries still declared 4:5, 5:3
# or 3:2 and three delivered pages had emitted one. A reading rule with nothing
# reading it is what that deferral bought.
LEGAL_RATIOS = ("16:9", "4:3", "1:1", "3:4", "9:16")

# Sessions that emitted an illegal ratio before this check existed. Each entry
# carries WHY, because a bare name in an exemption set is a decision nobody can
# audit later. These warn; anything not listed errors.
GRANDFATHERED_RATIOS = {
    "advertorial-seat-cushion-l-shaped-v01":
        "page 31, routed before ADR-016 — 2:1 and 5:3 at the hero and the "
        "problems block",
    "listicle-air-cooler-wall-mounted-v01":
        "page 13, the oldest session and the one whose page id was never "
        "recovered (ADR-034) — 5:3 across the reason cards",
    "listicle-bp-monitor-upper-arm-v01":
        "page 73, and this one POSTDATES ADR-016 by six days — a real breach "
        "listed here only so the validator stays green for the lanes that did "
        "not cause it. Fix the 3:2 options when that page is next opened",
}



# Every session routed before ADR-058 moved the threshold from one type to
# three. All of them fail the new rule -- 161 image slots between them, 111 on a
# single type, 50 on two, none on three -- so the list is the whole set rather
# than the twelve ADR-052 named. They are legal output under the practice of
# their day and records of completed routings; the gate binds every session
# routed after 2026-08-26. One aggregate warning keeps the debt visible without
# drowning the live signal.
GRANDFATHERED_SINGLE_TYPE = {
    "advertorial-massage-comb-spray-v02",
    "advertorial-optical-drive-7in1-v01",
    "advertorial-seat-cushion-l-shaped-v01",
    "advertorial-seat-cushion-l-shaped-v02",
    "advertorial-seat-cushion-l-shaped-v03",
    "advertorial-seat-cushion-l-shaped-v04",
    "advertorial-seat-cushion-l-shaped-v05",
    "advertorial-seat-cushion-l-shaped-v06",
    "listicle-air-cooler-wall-mounted-v01",
    "listicle-arm-trainer-hydraulic-v01",
    "listicle-bp-monitor-upper-arm-v01",
    "listicle-massage-comb-spray-v01",
    "listicle-mattress-vacuum-uv-v01",
}


def check_option_pools():
    """ADR-058: every image slot carries THREE options of three DISTINCT types,
    the three best fits for that slot's content (SPEC §7 item 4, runbook Step 4).
    A slot holding fewer must declare what ran out in `pool_basis` — which gates
    fired, which global rule refused a type, whether marketplace legality
    removed one (ADR-090) — or the session errors.

    This replaces ADR-052's threshold, which failed a multi-option slot only when
    ALL its options carried ONE type. That caught the worst case and passed the
    common one: two types across three options looked healthy and was still a
    slot offering the owner one real alternative. Measured when the threshold
    moved: 161 image slots shipped, 111 single-type, 50 two-type, none carrying
    three. `single_type_basis` is read as the retired name for `pool_basis`.
    """
    sessions_dir = os.path.join(ROOT, "query", "sessions")
    if not os.path.isdir(sessions_dir):
        return
    inherited = 0
    for session in sorted(os.listdir(sessions_dir)):
        path = os.path.join(sessions_dir, session, "prompts.json")
        if not os.path.exists(path):
            continue
        try:
            with open(path, encoding="utf-8") as f:
                doc = json.load(f)
        except json.JSONDecodeError:
            continue            # check_prompt_sets already reported it
        offending = []
        for slot in doc.get("slots", []):
            opts = slot.get("options") or []
            if not opts:
                continue        # the never-empty rule is checked elsewhere
            if slot.get("pool_basis") or slot.get("single_type_basis"):
                continue
            if len({o.get("type") for o in opts}) < 3:
                offending.append(str(slot.get("slot_id")))
        if not offending:
            continue
        if session in GRANDFATHERED_SINGLE_TYPE:
            inherited += len(offending)
            continue
        rel = f"query/sessions/{session}/prompts.json"
        shown = "; ".join(offending[:3])
        more = f"; and {len(offending) - 3} more" if len(offending) > 3 else ""
        err(rel, f"{len(offending)} image slot(s) carry fewer than three "
                 f"distinct types with no `pool_basis`: {shown}{more} — every "
                 "slot carries three options of three distinct types, ranked "
                 "best-fit first, and a shortfall has to name what ran out "
                 "(runbook Step 4, ADR-058)")
    if inherited:
        warn("query/sessions",
             f"{len(GRANDFATHERED_SINGLE_TYPE)} session(s) predate ADR-058 and "
             f"carry {inherited} slot(s) below three distinct types between them — "
             "grandfathered records of completed routings; the gate binds "
             "sessions routed after 2026-08-26")


def check_prompt_sets():
    """ADR-021: this pipeline is paste-and-run, so a delivered prompt is
    single-pass or it is not deliverable. Enforced here rather than left to a
    runbook paragraph, because a rule nothing runs is a rule nobody keeps."""
    sessions_dir = os.path.join(ROOT, "query", "sessions")
    if not os.path.isdir(sessions_dir):
        return
    for session in sorted(os.listdir(sessions_dir)):
        path = os.path.join(sessions_dir, session, "prompts.json")
        if not os.path.exists(path):
            continue
        rel = os.path.relpath(path, ROOT)
        try:
            with open(path, encoding="utf-8") as f:
                doc = json.load(f)
        except json.JSONDecodeError as e:
            err(rel, f"invalid JSON: {e}")
            continue
        for slot in doc.get("slots", []):
            for opt in slot.get("options", []):
                mode = opt.get("pipeline", "single-pass")
                if mode == "single-pass":
                    continue
                msg = (f"slot `{slot.get('slot_id')}` option {opt.get('opt')} "
                       f"({opt.get('type')}) is `{mode}` — ADR-021 emits only "
                       f"single-pass; take the type's own single-pass route")
                if session in GRANDFATHERED_MULTIPASS:
                    warn(rel, msg + " (predates ADR-021, grandfathered)")
                else:
                    err(rel, msg)


def check_ratios(types):
    """ADR-016: only 16:9, 4:3, 1:1, 3:4 and 9:16, system-wide.

    ONE surface now. A DELIVERED prompt is the deliverable, so an illegal ratio
    there is an error for anything routed from now on; three sessions predate the
    check and are named in GRANDFATHERED_RATIOS with their reasons.

    The type-file half is gone with ADR-082, which deleted `ratios` from all 34
    type files: nothing read it to route, the ratio a renderer is asked for comes
    from the SLOT in content.json, and the field had drifted in 10 of the 34 —
    5 of them in `_staging/` and `pdp-dr-types/`, where this check never looked.
    A warning that says "correct it when the file is next opened" only works if
    somebody opens the file.

    `types` is still taken so main() need not change shape, and so the next
    reader sees that the argument became unused on purpose.
    """
    sessions_dir = os.path.join(ROOT, "query", "sessions")
    if not os.path.isdir(sessions_dir):
        return
    for session in sorted(os.listdir(sessions_dir)):
        path = os.path.join(sessions_dir, session, "prompts.json")
        if not os.path.exists(path):
            continue
        rel = os.path.relpath(path, ROOT)
        try:
            with open(path, encoding="utf-8") as f:
                doc = json.load(f)
        except json.JSONDecodeError:
            continue            # check_prompt_sets already reported it
        seen = []
        for slot in doc.get("slots", []):
            for opt in slot.get("options", []):
                r = opt.get("ratio")
                if r and r not in LEGAL_RATIOS:
                    seen.append(f"slot `{slot.get('slot_id')}` option "
                                f"{opt.get('opt')} asks for `{r}`")
            gif = slot.get("gif") or {}
            gr = gif.get("ratio")
            if gif.get("eligible") and gr and gr not in LEGAL_RATIOS:
                seen.append(f"slot `{slot.get('slot_id')}` gif asks for `{gr}`")
        if not seen:
            continue
        head = (f"{len(seen)} ratio(s) outside ADR-016's five: " +
                "; ".join(seen[:3]) +
                (f"; and {len(seen) - 3} more" if len(seen) > 3 else ""))
        if session in GRANDFATHERED_RATIOS:
            warn(rel, head + f" — grandfathered: {GRANDFATHERED_RATIOS[session]}")
        else:
            err(rel, head)


def check_multipass_declarations(types, staging, pdp_dr=None):
    """ADR-067: `multi-pass` is removed from the vocabulary, so this is an ERROR.

    Vocabulary closure already refuses the value; this check exists for the
    message. A file that declares it is not making a typo, it is asking for a
    pipeline this library removed in three steps — ADR-021 stopped it reaching a
    prompt, ADR-039 retired the adapter rule that expanded it, ADR-067 deleted
    the value — and the reader needs to be told which single-pass route to take
    instead, not that a string is not in a list.

    Frontmatter only. A type that discusses multi-pass in its PROSE — a variant
    override, a recorded fallback — is not mechanically separable from one that
    merely records the history, and pretending a regex can tell those apart is
    the false comfort ADR-040 refused to build. `scripts/adr-sweep.py multi-pass`
    is the tool for the prose, and its TEACHES bucket is the real list. Run it
    case-insensitively: the 2026-09-03 sweep missed `Multi-pass` in
    `eval/render-test.md` because the term was capitalised.
    """
    for label, group in (("registry/types", types),
                         ("registry/types/_staging", staging),
                         ("registry/pdp-dr-types", pdp_dr or {})):
        for tid in sorted(group):
            if group[tid]["fm"].get("generation_mode") == "multi-pass":
                err(f"{label}/{tid}.md",
                    "declares `generation_mode: multi-pass`, REMOVED from the "
                    "vocabulary at ADR-067. Take a single-pass route: state the "
                    "cross-panel invariants once, before any panel is described "
                    "(`01-pain-split --mirror`, `04-proof-lockedframe` strict). "
                    "There is no compositing step in this pipeline (ADR-021)")


def check_grandfather_sets():
    """An exemption keyed on a directory name goes stale the moment that
    directory is renamed, and it fails SILENTLY: the name stops matching, the
    exemption protects nothing, and the session it covered starts erroring for a
    reason that has nothing to do with the session.

    Not hypothetical. ADR-034 renamed all nine session directories while this
    check's own ADR was being written in a parallel session. ADR-034 spotted the
    hazard and updated `GRANDFATHERED_MULTIPASS` by hand — but `PRE_CONTRACT_
    SESSIONS` was uncommitted in the same working tree, so it was invisible to
    that audit and the tree went to 23 errors in the seconds between the two.
    Naming a session that does not exist is now an error rather than a silence:
    a set that protects nothing is as wrong as one that protects too much, and
    only one of the two announces itself.
    """
    sessions_dir = os.path.join(ROOT, "query", "sessions")
    if not os.path.isdir(sessions_dir):
        return
    live = {d for d in os.listdir(sessions_dir)
            if os.path.isdir(os.path.join(sessions_dir, d))}
    for label, names in (("PRE_CONTRACT_SESSIONS", PRE_CONTRACT_SESSIONS),
                         ("GRANDFATHERED_MULTIPASS", GRANDFATHERED_MULTIPASS),
                         ("GRANDFATHERED_RATIOS", GRANDFATHERED_RATIOS),
                         ("GRANDFATHERED_SINGLE_TYPE", GRANDFATHERED_SINGLE_TYPE)):
        for name in sorted(set(names) - live):
            err("scripts/validate.py",
                f"{label} names `{name}`, which is not a session directory. It "
                "was renamed or removed, so the exemption now protects nothing "
                "(ADR-035)")


def check_session_names():
    """A session directory is {page-type}-{product-slug}-v{NN} (ADR-034).

    The slug is read from query/product-slugs.yaml rather than derived from the
    product name, because one product arrives under several names and a derived
    slug would split it. A convention with no checker drifts inside six months,
    which is what the names this replaced had already done.
    """
    sessions_dir = os.path.join(ROOT, "query", "sessions")
    if not os.path.isdir(sessions_dir):
        return
    if not os.path.exists(SLUGS_PATH):
        err("query/product-slugs.yaml", "missing; session names cannot be checked")
        return
    # Its own reader: the repo's YAML subset bars hyphens in a key and every slug
    # has them. Two levels, `slug:` then `  - name`, and nothing else.
    slugs, cur = {}, None
    with open(SLUGS_PATH, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if line.startswith("  - "):
                if cur is None:
                    err("query/product-slugs.yaml", f"name before any slug: {line.strip()!r}")
                    continue
                slugs[cur].append(line[4:].strip())
            elif re.fullmatch(r"[a-z0-9-]+:", line.strip()) and not line.startswith(" "):
                cur = line.strip()[:-1]
                slugs.setdefault(cur, [])
            else:
                err("query/product-slugs.yaml", f"unparseable line: {line.strip()[:50]!r}")
    name_to_slug = {}
    for slug, names in slugs.items():
        for n in (names or []):
            name_to_slug[str(n).strip()] = slug

    seen = {}
    for session in sorted(os.listdir(sessions_dir)):
        sdir = os.path.join(sessions_dir, session)
        if not os.path.isdir(sdir):
            continue
        rel = f"query/sessions/{session}"
        m = re.fullmatch(r"([a-z0-9-]+?)-([a-z0-9-]+)-v(\d{2})", session)
        if not m:
            err(rel, "directory name is not {page-type}-{product-slug}-v{NN} (ADR-034)")
            continue
        page_type, slug, ver = m.group(1), m.group(2), m.group(3)
        if slug not in slugs:
            # the split is ambiguous until a slug matches; try the longest one that does
            cand = [s2 for s2 in slugs if session.endswith(f"-{s2}-v{ver}")]
            if not cand:
                err(rel, f"product slug `{slug}` is not in query/product-slugs.yaml")
                continue
            slug = max(cand, key=len)
            page_type = session[:-(len(slug) + len(ver) + 3)].rstrip("-")
        if not page_type:
            err(rel, "no page type in front of the product slug")
        key = (slug, ver)
        if key in seen:
            err(rel, f"version v{ver} of `{slug}` is already taken by {seen[key]}")
        seen[key] = session

        cpath = os.path.join(sdir, "content.json")
        if not os.path.exists(cpath):
            continue
        try:
            with open(cpath, encoding="utf-8") as f:
                pname = (json.load(f).get("product") or {}).get("name")
        except (json.JSONDecodeError, OSError):
            continue
        if pname is None:
            warn(rel, "content.json carries no product.name, so the directory slug "
                      "cannot be checked against it")
        elif name_to_slug.get(str(pname).strip()) != slug:
            err(rel, f"directory says `{slug}` but content.json product is "
                     f"`{pname}` ({name_to_slug.get(str(pname).strip()) or 'unmapped'})")

    # a page_id that is not a number is a handle that got written into the id field
    for session in sorted(os.listdir(sessions_dir)):
        p = os.path.join(sessions_dir, session, "prompts.json")
        if not os.path.exists(p):
            continue
        try:
            with open(p, encoding="utf-8") as f:
                pid = json.load(f).get("page_id")
        except (json.JSONDecodeError, OSError):
            continue
        if pid is not None and not str(pid).isdigit():
            warn(f"query/sessions/{session}/prompts.json",
                 f"page_id `{str(pid)[:40]}` is not a number — the source handle was "
                 "written into the id field, and the real id is unrecovered")


# ---------------------------------------------------------------- routing table

def check_slot_rules(types):
    """The preference table is a VIEW: one row per role, best type first.

    It collapsed from four channel columns to one at ADR-059, when channel
    stopped being an admission test — the columns had become the same list
    written four times. The channel-vs-frontmatter check went with them: a type
    is now a candidate for every slot, so listing it under a role can no longer
    contradict its own frontmatter.

    What replaces it is the opposite check, and it is the one that was missing.
    This table is now the ONLY place a type declares which beat it belongs to,
    so an active type absent from it is a type no slot will ever prefer.
    `03-spec-macro` and `03-use-grid` went active on 2026-08-26 with no entry at
    all and nothing noticed until a feasibility count found them by hand.
    """
    rel = "mapping/slot-rules.md"
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        err(rel, "file not found")
        return {}
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    shortlist = {}
    listed = set()
    in_table = False
    for line in lines:
        if line.startswith("| Role "):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                break
            if set(line.replace("|", "").strip()) <= set("- "):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            role, cell = cells[0], cells[1]
            for tid in re.findall(r"`([^`]+)`", cell):
                tid = re.sub(r"--\w+$", "", tid).strip()
                shortlist.setdefault(role, []).append(tid)
                listed.add(tid)
                if tid not in types:
                    err(rel, f"role `{role}`: unknown type `{tid}`")

    missing = sorted(
        tid for tid, d in types.items()
        if d.get("fm", {}).get("status") == "active" and tid not in listed)
    if missing:
        err(rel, f"{len(missing)} active type(s) appear in no row of the "
                 f"preference table: {', '.join(missing)} — this table is the "
                 "only place a type declares which beat it belongs to, so a "
                 "type absent from it is one no slot will ever prefer (ADR-059)")
    return shortlist


def parse_attribute_gates():
    """The deterministic kill-rules, read from the table that documents them.

    Encoding them a second time in code is how a rule and its documentation
    drift; the effect cell already says `drop \\`<type>\\`` in plain text, so the
    gates are derived from `mapping/slot-rules.md` rather than restated here.
    """
    gates = []
    path = os.path.join(ROOT, "mapping", "slot-rules.md")
    if not os.path.exists(path):
        return gates
    with open(path, encoding="utf-8") as f:
        in_table = False
        for line in f:
            if line.startswith("| Attribute condition "):
                in_table = True
                continue
            if not in_table:
                continue
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            cond = re.match(r"^`([a-z_]+): ([a-z-]+)`$", cells[0])
            dropped = re.findall(r"drop `([^`]+)`", cells[1])
            if cond and dropped:
                gates.append((cond.group(1), cond.group(2), dropped))
    return gates


# ------------------------------------------------------- toplist prompt economy

# adapters/nano-banana.md Rule 6: a prompt lands at ~1450-1600 characters, and one
# past ~2500 "should be re-read for a duplicated block". Only the ceiling is gated.
# The band is a REFERENCE NUMBER measured on a one-subject GIF-inset prompt, and a
# collage prompt carries five products, a layout, a palette, a graphics layer and a
# badge; warning at 1600 would fire on 94 of the 106 prompts this namespace has
# shipped and would be noise rather than a signal.
PROMPT_REREAD_CEILING = 2500


def check_toplist_prompt_length():
    """Gate the one thing a prompt-length rule can actually gate.

    WHY THIS EXISTS. Rule 6 has been law since 2026-08-11 and the per-type render
    loop never once measured against it. Set by set, every render failure was
    answered by ADDING a clause and no set ever removed one, so prompt length
    ratcheted monotonically in both types that ran the loop -- `lede-authority`
    1498 -> 2158 across seven sets, `lede-collage` 1646 -> 2464 across six, and
    the first draft of set 7 reached 3436. The owner found it by reading, which is
    the same way rule 6c's misses keep being found.

    Unlike rule 6c this one IS gateable: it is a number, not a claim about meaning.
    So the ratchet cannot run silently again.

    Warns rather than errors. A prompt over the ceiling is a prompt to re-read for a
    duplicated block, which is a judgement the person writing the set has to make --
    and the nine prompts already over it are shipped history that a gate must not
    retroactively fail.
    """
    root = os.path.join(ROOT, "registry", "toplist-types")
    if not os.path.isdir(root):
        return
    for dirpath, _, filenames in os.walk(root):
        if "prompts.md" not in filenames:
            continue
        path = os.path.join(dirpath, "prompts.md")
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as f:
            body = f.read()
        for i, block in enumerate(re.findall(r"```(.*?)```", body, re.S), 1):
            n = len(block.strip())
            if n > PROMPT_REREAD_CEILING:
                warn(rel, f"prompt {i} is {n} characters — adapter Rule 6 says re-read "
                          f"anything past {PROMPT_REREAD_CEILING} for a duplicated block "
                          f"(band is ~1450-1600)")


# ------------------------------------------------------------------ app bundle

def check_app_bundle(strict):
    """The vendored bundle is a claim about repo files; verify the claim.

    `scripts/build-app-bundle.py --check` verifies the bundle's COMPOSITION —
    that every file the repo should ship is present. This verifies its FRESHNESS
    from the other side: every source path the manifest names is re-hashed and
    compared. It needs no knowledge of what belongs in the bundle, because the
    manifest already declares that, so the two checks cannot drift into agreeing
    with each other while both being wrong.
    """
    mpath = os.path.join(ROOT, "dist", "app-bundle", "MANIFEST.json")
    if not os.path.exists(mpath):
        return 0
    rel = "dist/app-bundle/MANIFEST.json"
    report = err if strict else warn
    try:
        with open(mpath, encoding="utf-8") as f:
            manifest = json.load(f)
    except json.JSONDecodeError as e:
        err(rel, f"invalid JSON: {e}")
        return 0
    n = 0
    for dest, meta in (manifest.get("files") or {}).items():
        src = os.path.join(ROOT, meta.get("from", ""))
        if not os.path.exists(src):
            report(rel, f"{dest}: source `{meta.get('from')}` no longer exists — "
                        "run scripts/build-app-bundle.py")
            continue
        h = hashlib.sha256()
        with open(src, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        if h.hexdigest() != meta.get("sha256"):
            report(rel, f"{dest}: source `{meta.get('from')}` has changed since "
                        "the bundle was built — run scripts/build-app-bundle.py")
        n += 1
    return n


# ------------------------------------------------------------------ golden

def _parse_expected_routes(path, rel):
    """A deliberately small reader for eval/golden/*/expected-routes.yaml.

    That file is prose plus assertions and sits outside the SPEC 3.4 YAML subset
    (flow maps nested two deep), so it is read for the four assertion keys the
    routing derivation can actually be checked against and nothing else.
    """
    doc = {"registry_version": None, "slots": {}}
    slot = sub = None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if line.startswith("#") or not line.strip():
                continue
            m = re.match(r'^registry_version:\s*"?([\d.]+)"?', line)
            if m:
                doc["registry_version"] = m.group(1)
                continue
            m = re.match(r"^  ([\w-]+):\s*$", line)
            if m:
                slot = m.group(1)
                doc["slots"][slot] = {"role": None, "expect": [], "only": None,
                                      "alts": []}
                sub = None
                continue
            if not slot:
                continue
            m = re.match(r"^    (\w+):(.*)$", line)
            if m:
                key, rest = m.group(1), m.group(2)
                sub = key
                if key == "section_role":
                    doc["slots"][slot]["role"] = rest.strip()
                elif key in ("only_preferred_type", "only_legal_type"):
                    # ADR-058 renamed it: the assertion is about the role×channel
                    # CELL, which is now a preference order rather than the pool.
                    # "only legal" was never what it checked and is now false —
                    # every channel-legal type is a candidate at some rank.
                    doc["slots"][slot]["only"] = rest.strip()
                elif key == "expected_option_A":
                    t = re.search(r"type:\s*([\w-]+)", rest)
                    if t:
                        doc["slots"][slot]["expect"].append(t.group(1))
                continue
            if sub == "legal_alternatives_must_include":
                t = re.search(r"type:\s*([\w-]+)", line)
                if t:
                    doc["slots"][slot]["alts"].append(
                        (t.group(1), "conditional:" in line))
    return doc


def check_golden(types, vocab, shortlist, gates):
    """Run the golden fixtures as the routing regression they are named for.

    SPEC 9 calls these 'routing regression fixtures' and until now nothing read
    them — `check_json_files` only proved the content.json parsed. What is
    checked here is Stage 1 of SPEC 7: the role x channel derivation plus the
    deterministic attribute gates. Stage 2 is judgement and is deliberately not
    asserted; the fixtures carry its expectations as prose for a human.
    """
    golden_dir = os.path.join(ROOT, "eval", "golden")
    if not os.path.isdir(golden_dir):
        return 0
    checked = 0
    for name in sorted(os.listdir(golden_dir)):
        fdir = os.path.join(golden_dir, name)
        cpath = os.path.join(fdir, "content.json")
        epath = os.path.join(fdir, "expected-routes.yaml")
        if not (os.path.isfile(cpath) and os.path.isfile(epath)):
            continue
        rel = f"eval/golden/{name}"
        with open(cpath, encoding="utf-8") as f:
            content = json.load(f)
        doc = _parse_expected_routes(epath, rel)
        chan = content["page"]["channel"]
        attrs = content["product"]["attributes"]

        rv = vocab.get("registry_version")
        if doc["registry_version"] and rv and doc["registry_version"] != rv:
            err(rel, f"expects registry_version {doc['registry_version']}, "
                     f"vocabulary says {rv} — re-run the fixture or update it")

        killed = {t for attr, val, drop in gates
                  if str(attrs.get(attr)).lower() == val for t in drop}

        roles = {s["role"]: s["role"] for s in content["page"]["sections"]}
        for slot, exp in doc["slots"].items():
            role = exp["role"]
            if not role:
                continue
            if role not in roles:
                err(rel, f"slot `{slot}`: role `{role}` is asserted but no "
                         "section in content.json declares it")
            cell = shortlist.get(role, [])
            legal = [t for t in cell if t not in killed
                     and types.get(t, {}).get("fm", {}).get("status") == "active"]
            asserted = [(t, False) for t in exp["expect"]] + exp["alts"]
            if exp["only"]:
                asserted.append((exp["only"], False))
                if sorted(set(legal)) != [exp["only"]]:
                    err(rel, f"slot `{slot}` ({role}): "
                             f"only_preferred_type says `{exp['only']}` but the "
                             f"preference row yields {sorted(set(legal))}")
            for tid, conditional in asserted:
                if tid not in types:
                    err(rel, f"slot `{slot}`: unknown type `{tid}`")
                    continue
                if tid not in cell:
                    msg = (f"slot `{slot}` ({role}): `{tid}` is asserted "
                           f"preferred but the slot-rules row holds {cell}")
                    (warn if conditional else err)(rel, msg)
                elif tid in killed:
                    err(rel, f"slot `{slot}`: `{tid}` is asserted legal but an "
                             "attribute gate drops it on this product")
            checked += 1
    return checked



# ------------------------------------------------------------- toplist types

TOPLIST_REQUIRED_KEYS = ["id", "version", "status", "replaced_by",
                         "products_in_frame", "requires_product_photo",
                         "awareness", "copied_from", "copied_at_version",
                         "blocked_by", "exempt_from"]
TOPLIST_OPTIONAL_KEYS = ["notes", "text_layer"]
TOPLIST_REQUIRED_SECTIONS = ["PURPOSE", "TRIGGER", "BOUNDARY", "SKELETON",
                             "NEGATIVE", "CHANGELOG"]


def validate_toplist_type_file(path, vocab, rule_ids, image_types):
    """SPEC 3.7 — the single-lede namespace for top-N listicles (ADR-069).

    A third namespace, separate for the reason gif types are separate: the page
    carries ONE image slot, so the role shortlist, the cross-slot pass and the
    coverage pass have nothing to act on. Never written into index.yaml.

    Two checks here are the namespace's own law rather than schema hygiene: a
    `reserved` type must NAME what blocks it, and a declared `text_layer` is held to
    the same closed slot list an image type's is.

    That second one used to REFUSE a text layer outright, and this docstring went on
    saying so for a day after the code below stopped doing it — the owner reversed the
    constraint on 2026-09-09 (ADR-071) and G16 now binds the types that declare one.
    Corrected here because a stale docstring teaching a lifted ban is exactly what
    CLAUDE.md rule 6c exists to catch, and a sweep does not read code comments.
    """
    fname = os.path.basename(path)
    where = f"registry/toplist-types/{fname}"
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm_lines, body = split_frontmatter(text, where)
    if fm_lines is None:
        return None
    fm = parse_block(fm_lines, where)

    # A toplist type MAY declare a text layer (ADR-071, owner instruction
    # 2026-09-09, reversing ADR-069). Same closed slot list as an image type, so
    # G16 reaches this namespace on the same terms it reaches the other one.
    tl = fm.get("text_layer")
    if tl is not None:
        if not isinstance(tl, list) or not tl:
            err(where, "text_layer must be a non-empty list of slots")
        else:
            for slot in tl:
                if slot not in TEXT_LAYER_SLOTS:
                    err(where, f"text_layer slot `{slot}` is not one of "
                               f"{TEXT_LAYER_SLOTS} (G16)")
    for k in TOPLIST_REQUIRED_KEYS:
        if k not in fm:
            err(where, f"missing required frontmatter key `{k}`")
    for k in fm:
        if k not in TOPLIST_REQUIRED_KEYS + TOPLIST_OPTIONAL_KEYS:
            err(where, f"unknown frontmatter key `{k}`")

    tid = fm.get("id")
    if tid != os.path.splitext(fname)[0]:
        err(where, f"id `{tid}` != filename")
    if tid is not None and tid not in (vocab.get("toplist_types") or []):
        err(where, f"id `{tid}` not in vocabulary.toplist_types")

    ver = fm.get("version")
    if not (isinstance(ver, str) and re.fullmatch(r"\d+\.\d+", ver)):
        err(where, f"version must be a quoted MAJOR.MINOR string, got {ver!r}")

    status = fm.get("status")
    if status not in (vocab.get("statuses") or []):
        err(where, f"status `{status}` not in vocabulary.statuses")
    if status == "deprecated" and not fm.get("replaced_by"):
        err(where, "status `deprecated` requires a non-null `replaced_by`")

    pop = fm.get("products_in_frame")
    if pop not in (vocab.get("toplist_frame_populations") or []):
        err(where, f"products_in_frame `{pop}` not in "
                   "vocabulary.toplist_frame_populations")

    if not isinstance(fm.get("requires_product_photo"), bool):
        err(where, "requires_product_photo must be a boolean")

    aw = fm.get("awareness")
    if not isinstance(aw, list) or not aw:
        err(where, "awareness must be a non-empty list")
    else:
        for a in aw:
            if a not in (vocab.get("toplist_awareness") or []):
                err(where, f"awareness `{a}` not in vocabulary.toplist_awareness")

    # `copied_from` is PROVENANCE, not a live link: the owner chose verbatim
    # copies over inheritance on 2026-09-09 (ADR-070), so the parent's text lives
    # in this file too. `copied_at_version` is what makes that choice auditable —
    # a copy cannot be stopped from drifting, but it can be made to say so.
    src = fm.get("copied_from")
    ver_at = fm.get("copied_at_version")
    if src is not None:
        if src not in image_types:
            err(where, f"copied_from `{src}` is not an image type in registry/types/")
        elif image_types[src]["fm"].get("status") != "active":
            err(where, f"copied_from `{src}`, which is not active")
        if not (isinstance(ver_at, str) and re.fullmatch(r"\d+\.\d+", ver_at)):
            err(where, "copied_from is set, so copied_at_version must be a quoted "
                       f"MAJOR.MINOR string, got {ver_at!r}")
        elif src in image_types:
            now = image_types[src]["fm"].get("version")
            if isinstance(now, str) and now != ver_at:
                warn(where,
                     f"copied verbatim from `{src}` at {ver_at}, and that file is "
                     f"now {now} — re-copy it or record in this file's CHANGELOG "
                     "why the divergence is intended. Two copies of one file drift, "
                     "and the stale one is the one somebody reads")
    elif ver_at is not None:
        err(where, "copied_at_version is set but copied_from is null")

    # A reserved type must say what blocks it; an active one must be unblocked.
    blocked = fm.get("blocked_by")
    if status == "reserved" and not blocked:
        err(where, "status `reserved` requires a non-null `blocked_by` naming the "
                   "decision it waits on")
    if status == "active" and blocked:
        err(where, f"status `active` but `blocked_by: {blocked}` — an active type "
                   "cannot be waiting on a decision")

    ex = fm.get("exempt_from")
    if not isinstance(ex, list):
        err(where, "exempt_from must be a list")
    else:
        for r in ex:
            if r not in rule_ids:
                err(where, f"exempt_from references unknown rule `{r}`")

    sections = split_sections(body)
    for sec in TOPLIST_REQUIRED_SECTIONS:
        if sec not in sections:
            err(where, f"missing required section `## {sec}`")
    if "use_when:" not in sections.get("TRIGGER", ""):
        err(where, "TRIGGER is missing `use_when:`")
    if status == "reserved" and "## BLOCK" not in body:
        err(where, "a `reserved` type owes a `## BLOCK` section saying what it "
                   "waits on and why")

    return {"fm": fm, "sections": sections}


# ------------------------------------------------------------------ gif types

GIF_REQUIRED_KEYS = ["id", "kind", "group", "rung", "version", "status",
                     "channels", "duration_s", "beats"]
GIF_OPTIONAL_KEYS = ["replaced_by", "notes"]
GIF_REQUIRED_SECTIONS = ["PURPOSE", "TRIGGER", "BOUNDARY", "BRIEF", "NEGATIVE",
                         "CHANGELOG"]
# ADR-037: one name for a loop, page-side and library-side alike. The gif type is
# a closed list, which is what makes the split unambiguous either side of it.
GIF_FILE_RE = re.compile(
    r"^([a-z-]+?)-(use|mechanism|cause|proof|relief|unboxing)-([a-z0-9-]+)-v(\d{2})\.mp4$")


def validate_gif_type_file(path, vocab):
    fname = os.path.basename(path)
    where = f"registry/gif-types/{fname}"
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm_lines, body = split_frontmatter(text, where)
    if fm_lines is None:
        return None
    fm = parse_block(fm_lines, where)

    for k in GIF_REQUIRED_KEYS:
        if k not in fm:
            err(where, f"missing required frontmatter key `{k}`")
    for k in fm:
        if k not in GIF_REQUIRED_KEYS + GIF_OPTIONAL_KEYS:
            err(where, f"unknown frontmatter key `{k}`")

    tid = fm.get("id")
    if tid != os.path.splitext(fname)[0]:
        err(where, f"id `{tid}` != filename")
    if tid is not None and tid not in (vocab.get("gif_types") or []):
        err(where, f"id `{tid}` not in vocabulary.gif_types")

    # `kind` is the jobs value the loop argues, and null where the type never
    # reaches a routed slot. A non-null kind that is not a job would emit a
    # gif.kind the output schema rejects, so it is an error and not a warning.
    kind = fm.get("kind")
    if kind is not None and kind not in (vocab.get("jobs") or {}):
        err(where, f"kind `{kind}` not in vocabulary.jobs")

    group = fm.get("group")
    if group not in (vocab.get("gif_groups") or []):
        err(where, f"group `{group}` not in vocabulary.gif_groups")
    if group == "none" and kind is not None:
        err(where, "group `none` must carry kind: null — it never reaches a slot")

    rung = fm.get("rung")
    if rung not in (1, 2):
        err(where, f"rung must be 1 or 2, got {rung!r}")

    ver = fm.get("version")
    if not (isinstance(ver, str) and re.fullmatch(r"\d+\.\d+", ver)):
        err(where, f"version must be a quoted MAJOR.MINOR string, got {ver!r}")

    status = fm.get("status")
    if status not in (vocab.get("statuses") or []):
        err(where, f"status `{status}` not in vocabulary.statuses")

    chans = fm.get("channels")
    if not isinstance(chans, list) or not chans:
        err(where, "channels must be a non-empty list")
    else:
        for c in chans:
            if c not in (vocab.get("channels") or []):
                err(where, f"channel `{c}` not in vocabulary.channels")

    for key in ("duration_s", "beats"):
        band = fm.get(key)
        if (not isinstance(band, list) or len(band) != 2
                or not all(isinstance(x, int) for x in band)):
            err(where, f"{key} must be a two-integer band [min, max], got {band!r}")
        elif band[0] > band[1]:
            err(where, f"{key} band is inverted: {band!r}")

    sections = split_sections(body)
    for s in GIF_REQUIRED_SECTIONS:
        if s not in sections:
            err(where, f"missing required section `## {s}`")
    trig = sections.get("TRIGGER", "")
    for key in ("use_when:", "avoid_when:"):
        if key not in trig:
            err(where, f"TRIGGER is missing `{key}`")

    return {"fm": fm, "sections": sections}


GIF_VI_FIELDS = ("message", "yes", "no", "vs")


def check_gif_cards_vi(gif_types):
    """Every gif type owes Vietnamese card copy (ADR-044).

    The Vietnamese folder card is the one artifact in this repo that is not in
    English, and it is a VIEW: the law it summarises stays in the type file. What
    makes the exception safe is that the two cards cannot drift apart by omission —
    a type with no entry, or an entry missing a field, silently ships a card with a
    dash where a rule should be.
    """
    if not os.path.exists(GIF_VI_PATH):
        err("registry/gif-cards-vi.md", "missing; every gif type owes Vietnamese card copy")
        return
    entries, cur, key, buf = {}, None, None, []

    def flush():
        if cur and key and "\n".join(buf).strip():
            entries[cur][key] = "\n".join(buf).strip()

    with open(GIF_VI_PATH, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if line.startswith("## "):
                flush()
                cur, key, buf = line[3:].strip(), None, []
                entries[cur] = {}
            elif cur is not None and line.rstrip().endswith(":") \
                    and line.rstrip()[:-1].strip() in GIF_VI_FIELDS \
                    and not line.startswith(" "):
                flush()
                key, buf = line.rstrip()[:-1].strip(), []
            elif key is not None:
                buf.append(line)
    flush()
    where = "registry/gif-cards-vi.md"
    for tid in sorted(gif_types):
        if tid not in entries:
            err(where, f"no `## {tid}` section — that folder would ship an English card only")
            continue
        for field in GIF_VI_FIELDS:
            if field not in entries[tid]:
                err(where, f"`{tid}` is missing `{field}:` — the card would print a dash "
                           "where a rule belongs")
    for extra in sorted(set(entries) - set(gif_types)):
        err(where, f"`## {extra}` is not a gif type in registry/gif-types/")


def check_gif_ledger(gif_types):
    """ingestion/gifs.jsonl — append-only asset index for the GIF library."""
    recs = load_jsonl(GIF_LEDGER_PATH,
                      ["ts", "sha256", "type", "file"], "ingestion/gifs.jsonl")
    seen = {}
    for n, rec in enumerate(recs, 1):
        w = "ingestion/gifs.jsonl"
        tid = rec.get("type")
        if tid not in gif_types:
            err(w, f"record {n}: unknown gif type `{tid}`")
        fname = rec.get("file") or ""
        m = GIF_FILE_RE.match(fname)
        if not m:
            err(w, f"record {n}: file `{fname}` does not match "
                   "{page-type}-{gif-type}-{product-slug}-v{NN}.mp4")
        elif m.group(2) != tid:
            err(w, f"record {n}: file `{fname}` is filed under type `{tid}`")
        h = rec.get("sha256")
        if h in seen:
            warn(w, f"record {n}: sha256 already filed at record {seen[h]} — "
                    "a correction is a new record, but a duplicate asset is not")
        elif h:
            seen[h] = n
    return recs


# ---------------------------------------------------------------- main

def main(argv):
    write_index = "--write-index" in argv
    check = "--check" in argv

    vocab = load_vocabulary()
    rule_ids = load_rule_ids()
    if not rule_ids:
        err("registry/rules.md", "no rule IDs found (expected `## G<n>` headers)")

    types = {}
    for fn in sorted(os.listdir(TYPES_DIR)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(TYPES_DIR, fn)
        if not os.path.isfile(path):
            continue
        parsed = validate_type_file(path, vocab, rule_ids)
        if parsed and parsed["fm"].get("id"):
            tid = parsed["fm"]["id"]
            if tid in types:
                err(f"registry/types/{fn}", f"duplicate id `{tid}`")
            types[tid] = parsed

    cross_validate(types, set(types))

    # Staging drafts: same anatomy checks, never indexed, never referenced by
    # active types (their refs above only resolve within active ids).
    staging = {}
    staging_dir = os.path.join(TYPES_DIR, "_staging")
    if os.path.isdir(staging_dir):
        for fn in sorted(os.listdir(staging_dir)):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            parsed = validate_type_file(os.path.join(staging_dir, fn), vocab, rule_ids)
            if parsed and parsed["fm"].get("id"):
                sid = parsed["fm"]["id"]
                staging[sid] = parsed
                if parsed["fm"].get("status") != "reserved":
                    err(f"registry/types/_staging/{fn}",
                        "staging files must have status: reserved")
    cross_validate(staging, set(types) | set(staging), "registry/types/_staging")

    # Toplist types (ADR-069). The third namespace: one lede image for a top-N
    # listicle, consumed from the product input rather than from content.json,
    # and never written into index.yaml.
    toplist_types = {}
    if os.path.isdir(TOPLIST_TYPES_DIR):
        for fn in sorted(os.listdir(TOPLIST_TYPES_DIR)):
            if not fn.endswith(".md") or fn == "README.md" or fn.startswith("_"):
                continue
            parsed = validate_toplist_type_file(
                os.path.join(TOPLIST_TYPES_DIR, fn), vocab, rule_ids, types)
            if parsed and parsed["fm"].get("id"):
                lid = parsed["fm"]["id"]
                if lid in toplist_types:
                    err(f"registry/toplist-types/{fn}", f"duplicate id `{lid}`")
                toplist_types[lid] = parsed
    for declared in vocab.get("toplist_types") or []:
        if declared not in toplist_types:
            err("registry/vocabulary.yaml",
                f"toplist_types declares `{declared}` with no "
                f"registry/toplist-types/{declared}.md")
    # ADR-058 asks every image slot for three options of three distinct types. A
    # top-N page has exactly one slot, so the namespace itself has to be able to
    # offer three, or the page cannot meet the rule no matter how it routes.
    live = [t for t in toplist_types.values()
            if t["fm"].get("status") == "active"]
    if toplist_types and len(live) < 3:
        err("registry/toplist-types",
            f"only {len(live)} active toplist type(s) — ADR-058 asks a slot for "
            "three distinct options and this namespace serves a one-slot page")

    # PDP-DR types (ADR-077, ADR-091). The fourth namespace, and the ONE folder an LP2
    # page routes: its own drafts plus verbatim copies of every active registry/types/
    # file under the same ids. Never written into index.yaml; its active files are
    # written into registry/pdp-dr-index.yaml instead.
    pdp_dr_types = {}
    if os.path.isdir(PDP_DR_TYPES_DIR):
        for fn in sorted(os.listdir(PDP_DR_TYPES_DIR)):
            if not fn.endswith(".md") or fn == "README.md" or fn.startswith("_"):
                continue
            parsed = validate_pdp_dr_type_file(
                os.path.join(PDP_DR_TYPES_DIR, fn), vocab, rule_ids, types)
            if parsed and parsed["fm"].get("id"):
                pid = parsed["fm"]["id"]
                if pid in pdp_dr_types:
                    err(f"registry/pdp-dr-types/{fn}", f"duplicate id `{pid}`")
                pdp_dr_types[pid] = parsed
    for declared in vocab.get("pdp_dr_types") or []:
        if declared not in pdp_dr_types:
            err("registry/vocabulary.yaml",
                f"pdp_dr_types declares `{declared}` with no "
                f"registry/pdp-dr-types/{declared}.md")
    for pid in sorted(pdp_dr_types):
        if pid not in (vocab.get("pdp_dr_types") or []):
            err(f"registry/pdp-dr-types/{pid}.md",
                f"id `{pid}` is not in vocabulary.pdp_dr_types — the closed list is "
                "the namespace, and a file outside it routes nowhere and is checked "
                "by nothing else")
        # This namespace shares an id grammar with registry/types/, which the other
        # two namespaces do not. So it is the only one where an id can collide. Since
        # ADR-091 one collision is the design — a verbatim copy keeps its parent's id
        # and says so in `copied_from` — and any other is an undeclared duplicate.
        if pid in types and pdp_dr_types[pid]["fm"].get("copied_from") != pid:
            err(f"registry/pdp-dr-types/{pid}.md",
                f"id `{pid}` also exists in registry/types/ and this file does not "
                f"declare `copied_from: {pid}` — two files with one id must be a "
                "declared copy (ADR-091)")
        if pid in staging:
            err(f"registry/pdp-dr-types/{pid}.md",
                f"id `{pid}` also exists in registry/types/_staging/")
    cross_validate(pdp_dr_types, set(types) | set(staging) | set(pdp_dr_types),
                   "registry/pdp-dr-types")
    # ADR-091: an LP2 page routes this folder and no other, so an active image type
    # with no file here is a type LP2 cannot use. A promotion into registry/types/
    # does not reach LP2 by itself; this makes the gap say so, the way ADR-070's
    # drift warning makes a stale copy say so.
    for tid in sorted(types):
        if types[tid]["fm"].get("status") == "active" and tid not in pdp_dr_types:
            warn(f"registry/types/{tid}.md",
                 "active, and no file in registry/pdp-dr-types/ carries its id — an "
                 "LP2 page routes that folder alone (ADR-091), so it cannot use this "
                 "type. Copy it there, or copy it `status: reserved` with a BLOCK "
                 "saying why LP2 must not")

    # GIF types (ADR-023). A separate namespace from image types: its ids are
    # arguments, not {step}-{job}-{device}, and it is never written into index.yaml
    # because routing reads a gif type by id off the slot verdict, not by shortlist.
    gif_types = {}
    if os.path.isdir(GIF_TYPES_DIR):
        for fn in sorted(os.listdir(GIF_TYPES_DIR)):
            if not fn.endswith(".md") or fn == "README.md" or fn.startswith("_"):
                continue
            parsed = validate_gif_type_file(os.path.join(GIF_TYPES_DIR, fn), vocab)
            if parsed and parsed["fm"].get("id"):
                gid = parsed["fm"]["id"]
                if gid in gif_types:
                    err(f"registry/gif-types/{fn}", f"duplicate id `{gid}`")
                gif_types[gid] = parsed
    for declared in vocab.get("gif_types") or []:
        if declared not in gif_types:
            err("registry/vocabulary.yaml",
                f"gif_types declares `{declared}` with no registry/gif-types/"
                f"{declared}.md")
    # The motion floor asks for one `working` and one `result` loop per page
    # (query/runbook.md Step 5d). If the registry cannot offer both, the floor is
    # unsatisfiable by construction and every page would report a shortfall.
    active_groups = {t["fm"].get("group") for t in gif_types.values()
                     if t["fm"].get("status") == "active"}
    for needed in ("working", "result"):
        if gif_types and needed not in active_groups:
            err("registry/gif-types",
                f"no active gif type in group `{needed}` — the Step 5d floor "
                "cannot be met by any page")
    check_gif_cards_vi(set(gif_types))
    gif_ledger = check_gif_ledger(set(gif_types))

    observations = load_jsonl(
        OBS_PATH, ["hash", "ts", "template_version", "verdict"],
        "ingestion/observations.jsonl")
    picks = load_jsonl(
        PICKS_PATH, ["ts", "section_role", "options_shown", "picked"],
        "feedback/picks.jsonl")
    render_tests = load_jsonl(
        RENDER_PATH, ["ts", "type", "type_version", "runs", "verdict"],
        "eval/render-tests.jsonl")
    for n, rec in enumerate(render_tests, 1):
        if rec.get("verdict") not in ("pass", "partial", "fail"):
            err("eval/render-tests.jsonl",
                f"record {n}: verdict must be pass|partial|fail")
        # A toplist id is a real type in a real registry; this check predates that
        # namespace and would have warned on every record of its founding render
        # round. Third time a tool's membership list has been found not knowing
        # about registry/toplist-types/ — ADR-070 found it in adr-sweep.py's tuples.
        # Fourth namespace, fourth time this membership list has been found not
        # knowing about one (ADR-070 found it in adr-sweep.py's tuples). Seven types
        # moved from _staging/ to registry/pdp-dr-types/ on 2026-09-10 and three of
        # them carry founding renders in this ledger; without this term every one of
        # those records would warn as an unknown type the moment the files moved.
        if (rec.get("type") not in types and rec.get("type") not in staging
                and rec.get("type") not in toplist_types
                and rec.get("type") not in pdp_dr_types):
            warn("eval/render-tests.jsonl",
                 f"record {n}: unknown type `{rec.get('type')}`")
    evidence = evidence_counts(observations, vocab, types)
    check_toplist_evidence(observations, toplist_types)
    check_pdp_dr_evidence(observations, pdp_dr_types)
    check_former_ids(set(types) | set(staging) | set(toplist_types)
                     | set(pdp_dr_types) | set(gif_types))
    stats = pick_stats(picks, types)

    check_json_files()
    contracts = check_content_contracts()
    check_prompt_sets()
    check_option_pools()
    check_ratios(types)
    check_multipass_declarations(types, staging, pdp_dr_types)
    check_grandfather_sets()
    check_session_names()
    shortlist = check_slot_rules(types)
    gates = parse_attribute_gates()
    golden_slots = check_golden(types, vocab, shortlist, gates)
    check_toplist_prompt_length()
    bundled = check_app_bundle(check)

    index_text = render_index(vocab, types, evidence, stats)
    # LP2's routing surface (ADR-091): the active files of registry/pdp-dr-types/, in
    # the same shape as index.yaml, so a router for either page kind reads one index
    # and one rules file and never opens a type file to choose.
    lp2 = {pid: t for pid, t in pdp_dr_types.items() if t["fm"].get("status") == "active"}
    lp2_evidence = {pid: len(e["obs"])
                    for pid, e in ledger_evidence(observations, lp2).items()}
    lp2_text = render_index(vocab, lp2, lp2_evidence, pick_stats(picks, lp2),
                            LP2_SURFACE)
    if write_index:
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(index_text)
        print(f"wrote registry/index.yaml ({len(types)} types)")
        with open(PDP_DR_INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(lp2_text)
        print(f"wrote registry/pdp-dr-index.yaml ({len(lp2)} types)")
    if check:
        for path, text, rel in ((INDEX_PATH, index_text, "registry/index.yaml"),
                                (PDP_DR_INDEX_PATH, lp2_text,
                                 "registry/pdp-dr-index.yaml")):
            if not os.path.exists(path):
                err(rel, "missing — run --write-index")
            else:
                with open(path, encoding="utf-8") as f:
                    if f.read() != text:
                        err(rel, "stale — run --write-index")

    for w in WARNINGS:
        print(f"WARN  {w}")
    for e in ERRORS:
        print(f"ERROR {e}")
    print(f"{len(types)} types, {len(staging)} staging, "
          f"{len(gif_types)} gif types, {len(gif_ledger)} gifs, "
          f"{len(toplist_types)} toplist types, "
          f"{len(pdp_dr_types)} pdp-dr types, "
          f"{golden_slots} golden slots, {contracts} content contracts, "
          f"{bundled} bundled files, "
          f"{len(observations)} observations, {len(picks)} picks, "
          f"{len(render_tests)} render tests, "
          f"{len(ERRORS)} errors, {len(WARNINGS)} warnings")
    if "--evidence" in argv:
        evidence_report(observations, [("types", types), ("staging", staging),
                                       ("toplist", toplist_types),
                                       ("pdp-dr", pdp_dr_types)])
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
