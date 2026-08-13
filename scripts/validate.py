#!/usr/bin/env python3
"""Registry validator + index generator (SPEC.md section 8).

stdlib only, Python >= 3.9. Parses the constrained YAML subset defined in
SPEC.md section 3.4 — anything outside the subset is a validation error by design.

Usage:
  python3 scripts/validate.py               # validate, report, exit 1 on errors
  python3 scripts/validate.py --write-index # validate + regenerate registry/index.yaml
  python3 scripts/validate.py --check       # validate + fail if index.yaml is stale
"""
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
RENDER_PATH = os.path.join(ROOT, "eval", "render-tests.jsonl")

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
    "ratios", "channels", "requires_product_photo", "generation_mode",
]
OPTIONAL_KEYS = [
    "axes", "variants", "exempt_from", "pairs_with", "never_with",
    "avoid_adjacent", "requires_pair",
]
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


def validate_type_file(path, vocab, rule_ids):
    fname = os.path.basename(path)
    where = f"registry/types/{fname}"
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
        if k not in REQUIRED_KEYS + OPTIONAL_KEYS:
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

    for r in fm.get("ratios") or []:
        if not re.fullmatch(r"\d+:\d+", str(r)):
            err(where, f"ratio `{r}` is not W:H")
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


def evidence_counts(observations, vocab, types):
    verdicts = set(vocab.get("observation_verdicts") or [])
    seen = {tid: set() for tid in types}
    for rec in observations:
        v = rec.get("verdict")
        if v not in verdicts:
            err("ingestion/observations.jsonl", f"unknown verdict `{v}`")
            continue
        tid = rec.get("type")
        if v in ("match", "variant-candidate") and tid in seen:
            h = rec.get("hash")
            if h:
                seen[tid].add(h)
    return {tid: len(hashes) for tid, hashes in seen.items()}


def pick_stats(picks, types):
    stats = {tid: {} for tid in types}
    for rec in picks:
        role = rec.get("section_role")
        if not role:
            continue
        shown_types = [o.get("type") for o in rec.get("options_shown") or []
                       if isinstance(o, dict)]
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

def render_index(vocab, types, evidence, picks):
    out = []
    out.append("# GENERATED by scripts/validate.py --write-index — do not edit by hand.")
    out.append("# Router surface: routing reads this file plus mapping/slot-rules.md only.")
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
        out.append(f"    ratios: {ylist(fm.get('ratios') or [])}")
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


# ---------------------------------------------------------------- routing table

CHANNEL_COLS = ["marketplace", "landing-page", "paid-social", "advertorial"]


def check_slot_rules(types):
    """The shortlist table is a VIEW of data the type files already own.

    Every type named in a channel column must declare that channel in its own
    frontmatter. Without this check the two drift silently: eight such
    contradictions accumulated before it existed, and query runs routed through
    them, producing prompts that were illegal on their own channel.
    """
    rel = "mapping/slot-rules.md"
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        err(rel, "file not found")
        return
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
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
            if len(cells) < 5:
                continue
            role, cols = cells[0], cells[1:5]
            for chan, cell in zip(CHANNEL_COLS, cols):
                for tid in re.findall(r"`([^`]+)`", cell):
                    tid = re.sub(r"--\w+$", "", tid).strip()
                    if tid not in types:
                        err(rel, f"role `{role}` / {chan}: unknown type `{tid}`")
                        continue
                    declared = types[tid]["fm"].get("channels") or []
                    if chan not in declared:
                        err(rel,
                            f"role `{role}` / {chan}: `{tid}` is listed here but "
                            f"its frontmatter declares channels {declared} — the "
                            f"table and the type disagree")


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
        if rec.get("type") not in types and rec.get("type") not in staging:
            warn("eval/render-tests.jsonl",
                 f"record {n}: unknown type `{rec.get('type')}`")
    evidence = evidence_counts(observations, vocab, types)
    stats = pick_stats(picks, types)

    check_json_files()
    check_slot_rules(types)

    index_text = render_index(vocab, types, evidence, stats)
    if write_index:
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(index_text)
        print(f"wrote registry/index.yaml ({len(types)} types)")
    if check:
        if not os.path.exists(INDEX_PATH):
            err("registry/index.yaml", "missing — run --write-index")
        else:
            with open(INDEX_PATH, encoding="utf-8") as f:
                if f.read() != index_text:
                    err("registry/index.yaml", "stale — run --write-index")

    for w in WARNINGS:
        print(f"WARN  {w}")
    for e in ERRORS:
        print(f"ERROR {e}")
    print(f"{len(types)} types, {len(staging)} staging, "
          f"{len(observations)} observations, {len(picks)} picks, "
          f"{len(render_tests)} render tests, "
          f"{len(ERRORS)} errors, {len(WARNINGS)} warnings")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
