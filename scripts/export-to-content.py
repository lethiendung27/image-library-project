#!/usr/bin/env python3
"""Convert a flunnel page export into the QUERY operation's `content.json`.

SPEC 1 says QUERY's input is a `content.json` valid against
`mapping/content.schema.json`. A live export satisfies none of it. This script is
the missing step, and `mapping/export-to-content.md` is its specification.

WHAT IT DOES AND DOES NOT DO, because the difference is the whole design.

MECHANICAL — taken from the export, never invented:
  - the image slots, from every element in `page.htmlCompiled` carrying
    `data-field-type="image"`, whose `data-field` IS the slot id;
  - their ORDER, which is the document's;
  - their grouping into sections, by ADR-050's arithmetic on the slot id and NOT
    by `<section data-block-key>` — see `section_of`. The markup groups more
    coarsely because a `<section>` is a styling container: measured across the 57
    exports on disk, the two rules agree on 27 and differ on 30;
  - each slot's ratio, from the rendered box where the markup states one and the
    asset's own dimensions otherwise, snapped to ADR-016's five;
  - which slots the library does not cover at all (logos, avatars, the first
    gallery image, video posters, trust badges);
  - `product.name`, `personas`, `raw_features`, `specification` from `brief`.

JUDGEMENT — never guessed here, and the reason is recorded in each case:
  - `role` and `copy_summary`. Role follows what a section's COPY argues, not
    which block it sits in. Measured: in
    `query/sessions/advertorial-cord-tensioner-cam-lock-v01/content.json`, seven
    sibling cards of ONE repeating block (`content.items.0` ... `.6`) carry six
    different roles. A block -> role table collapses all seven into one and
    destroys the page arc `mapping/slot-rules.md` cross-rule 3 enforces.
  - `page.channel`. The export does not carry it. The router learned it by
    GUESSING it from `lpTypeId` for five sessions running, which is half of why
    ADR-059 removed channel as an admission test. This script will not repeat
    that guess.
  - the eight `product.attributes`. Owner decision of 2026-09-11: the app
    supplies them. They are validated here, never derived.
  - `product.category` and `problems_solved`. Category is OPTIONAL (ADR-085):
    left undecided in the work file, it is omitted rather than shipped as a
    placeholder.

So the run is two passes. `scaffold` emits a worksheet carrying every mechanical
fact plus the copy a reader needs to assign roles; `build` takes the export and
the filled worksheet and emits `content.json`, refusing to write one that does
not satisfy the contract.

    python3 scripts/export-to-content.py scaffold EXPORT.json -o work.json
    python3 scripts/export-to-content.py build EXPORT.json -d work.json -o content.json

Stdlib only, Python >= 3.9. `schema_errors` is imported from `scripts/validate.py`
rather than reimplemented: two validators drift, and the one in the validator is
the one CI runs.
"""

import argparse
import html as htmllib
import json
import os
import re
import sys
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate import schema_errors            # noqa: E402  (path set above)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_PATH = os.path.join(ROOT, "mapping", "content.schema.json")

# ADR-016's five. A ratio outside them is a ratio the router is not allowed to
# ask the renderer for, so a measured box is snapped to the nearest of these and
# the snap is reported rather than applied quietly.
ALLOWED_RATIOS = [(16, 9), (4, 3), (1, 1), (3, 4), (9, 16)]

# `visible_output` is the only one of the eight typed as an open string rather
# than an enum, so the contract cannot catch prose in it. Four of the repo's
# fifteen content.json files carry 49-140 characters of prose there, and
# `mapping/slot-rules.md`'s gate is `visible_output != none` — which prose
# satisfies, so G8 binds by accident. Warned, not failed: the schema does allow
# it, and failing here would reject files the contract accepts.
VISIBLE_OUTPUT_TOKENS = {"mist", "spray", "water-jet", "steam", "foam",
                         "light", "particles", "none"}

REQUIRED_ATTRS = ["operation", "visible_output", "mounting", "colorways",
                  "body_contact", "symptom_visibility", "result_visibility",
                  "multi_step_usage"]


class ConversionError(Exception):
    """Refuse to emit rather than emit something the contract rejects."""


# --------------------------------------------------------------- scope filter

def out_of_scope(field):
    """Why the library does not cover this image, or None if it does.

    Every reason cites the rule it comes from. This is the one piece of judgement
    the script does make, and it is made from written rules rather than from the
    picture.
    """
    leaf = field.rsplit(".", 1)[-1]
    if leaf == "logo" or re.search(r"(^|\.)logos?(\.\d+)?$", field):
        return "brand or press logo — G6 bans logos outright"
    if (leaf in ("avatar", "author_avatar", "bio_image")
            or leaf.endswith("_avatar")):
        # The `author` row's own rationale names these: "a byline avatar, an
        # About-the-author image, a comment thread of faces". Verified rather
        # than guessed from the name — `closing.bio_image` sits beside
        # `closing.bio_title` "About the specialist" and a signed `closing.
        # signature`, so the picture is of a named person.
        return ("portrait of a named person — `mapping/slot-rules.md`'s `author` "
                "row is empty by decision")
    if field == "product.gallery.0":
        return ("first gallery image — `mapping/slot-rules.md` cross-rule 6 puts "
                "the standard product shot out of library scope")
    if leaf == "poster":
        return "video poster frame, not an argued image"
    if "badge" in leaf:
        return "trust badge, not an argued image"
    return None


# ------------------------------------------------------------- section identity

def section_of(slot_id):
    """ADR-050's rule, verbatim from `query/runbook.md`.

    A section is the slot id's top-level prefix, plus its next segment when that
    segment is a NUMBER. A number directly after the prefix is a BLOCK index and
    each block is its own section; a number after a container word — `items`,
    `photos`, `shots`, `quotes` — is an ITEM index and the list stays one section.

    THIS, not `<section data-block-key>`, decides a section. Measured across the
    57 exports on disk: the two rules give the same grouping on 27 and a
    DIFFERENT one on 30. Where they differ the markup is coarser, because a
    `<section>` is a styling container — the advertorial template wraps seven
    argument cards, a product shot, a closing card and four review photos in one
    `features` element. ADR-050 exists precisely to stop a template's packaging
    being read as the page's argument structure, and it was derived from routed
    pages rather than from markup.

    The DOM still decides ORDER; it just does not decide grouping.
    """
    p = slot_id.split(".")
    return f"{p[0]}.{p[1]}" if len(p) > 1 and p[1].isdigit() else p[0]


# -------------------------------------------------------------- ratio derivation

def _reduce(w, h):
    g = gcd(w, h)
    return (w // g, h // g)


def snap_ratio(w, h):
    """Snap a measured box to the nearest of ADR-016's five.

    Returns (ratio_string, exact_string, note). `note` is non-empty when the
    measured box was not already one of the five, or when the two nearest
    candidates are close enough that the choice is not obvious.
    """
    exact = "%d:%d" % _reduce(w, h)
    if _reduce(w, h) in ALLOWED_RATIOS:
        return exact, exact, ""
    r = w / h
    ranked = sorted(ALLOWED_RATIOS, key=lambda p: abs(r - p[0] / p[1]))
    best, second = ranked[0], ranked[1]
    d1 = abs(r - best[0] / best[1])
    d2 = abs(r - second[0] / second[1])
    chosen = "%d:%d" % best
    note = "measured %s (%.3f) snapped to %s" % (exact, r, chosen)
    if d2 - d1 < 0.02:
        note += (" — NEAR TIE with %d:%d (%.3f vs %.3f); confirm by hand"
                 % (second[0], second[1], d1, d2))
    return chosen, exact, note


def ratio_for(tag):
    """Derive a slot's ratio from one <img> tag.

    Precedence: the rendered box the markup states (`aspect-[a/b]`,
    `aspect-square`) outranks the asset's intrinsic `width`/`height`, because the
    rendered box is the shape the reader sees. Both are recorded so a
    disagreement is visible rather than resolved silently.
    """
    # Tailwind states a rendered box three ways and all three appear on image
    # fields in the exports on disk: aspect-[a/b] (435), aspect-square (695) and
    # aspect-video (6). `aspect-video` is 16/9 and missing it left eight
    # `hero.image` slots — the most important slot on the page — with no ratio.
    # `aspect-auto` (2) is NOT a ratio and must not be read as one.
    cls = None
    m = re.search(r"aspect-\[(\d+)\s*/\s*(\d+)\]", tag)
    if m:
        cls = (int(m.group(1)), int(m.group(2)))
    elif re.search(r"\baspect-square\b", tag):
        cls = (1, 1)
    elif re.search(r"\baspect-video\b", tag):
        cls = (16, 9)

    attrs = None
    mw = re.search(r'\swidth="(\d+)"', tag)
    mh = re.search(r'\sheight="(\d+)"', tag)
    if mw and mh and int(mw.group(1)) > 0 and int(mh.group(1)) > 0:
        attrs = (int(mw.group(1)), int(mh.group(1)))

    box, source = (cls, "rendered box (aspect class)") if cls else \
                  (attrs, "asset dimensions (width/height)") if attrs else (None, None)
    if box is None:
        return None

    ratio, exact, note = snap_ratio(*box)
    disagree = ""
    if cls and attrs and _reduce(*cls) != _reduce(*attrs):
        disagree = (" — markup says %d:%d, asset is %d:%d; the rendered box wins"
                    % (_reduce(*cls) + _reduce(*attrs)))
    return {"ratio": ratio, "measured": exact, "source": source,
            "note": (note + disagree).strip(" —")}


# ----------------------------------------------------------- export parsing

def load_export(path):
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    kind = doc.get("kind")
    if kind != "flunnel-page-export":
        raise ConversionError(
            "not a flunnel page export: `kind` is %r, expected "
            "'flunnel-page-export'" % (kind,))
    ver = doc.get("schemaVersion")
    if ver != 1:
        raise ConversionError(
            "export schemaVersion is %r; this converter was measured against "
            "version 1 only. Re-measure before trusting it." % (ver,))
    if not isinstance(doc.get("page"), dict):
        raise ConversionError("export carries no `page` object")
    if not doc["page"].get("htmlCompiled"):
        raise ConversionError(
            "export carries no `page.htmlCompiled` — that string is where the "
            "section structure lives, and there is no second source for it")
    return doc


def parse_sections(html):
    """Split htmlCompiled into its `<section data-block-key=...>` elements.

    Depth-counted rather than regex-matched to the closing tag: sections nest
    other elements and a non-greedy match to the first `</section>` truncates
    every one of them.
    """
    out = []
    opens = list(re.finditer(r"<section\b([^>]*)>", html))
    for m in opens:
        attrs = m.group(1)
        key = re.search(r'data-block-key="([^"]*)"', attrs)
        if not key:
            continue
        depth, i = 1, m.end()
        while depth and i < len(html):
            nxt = re.search(r"<(/?)section\b", html[i:])
            if not nxt:
                break
            depth += -1 if nxt.group(1) else 1
            i += nxt.end()
        vis = re.search(r'data-visible="([^"]*)"', attrs)
        sid = re.search(r'\sid="([^"]*)"', attrs)
        out.append({
            "block_key": key.group(1),
            "html_id": sid.group(1) if sid else None,
            "visible": (vis.group(1) if vis else "true") != "false",
            "inner": html[m.end():i],
            "start": m.start(),
            "end": i,
        })
    return out


def image_fields(fragment):
    """Every image-typed bound element in a fragment, in DOM order.

    Keyed on `data-field-type="image"` rather than on the tag being <img>: the
    attribute is what the export declares, and a declared type outranks a guess
    from the tag name.
    """
    found = []
    for m in re.finditer(r"<(\w+)\b([^>]*)>", fragment):
        attrs = m.group(2)
        if 'data-field-type="image"' not in attrs:
            continue
        name = re.search(r'data-field="([^"]*)"', attrs)
        if not name:
            continue
        found.append((name.group(1), m.group(0)))
    return found


def text_of(fragment, limit=400):
    """Readable copy from a fragment, for the worksheet's role decision."""
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", fragment, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = htmllib.unescape(t)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:limit] + ("..." if len(t) > limit else "")


def check_marker_coverage(doc, warnings):
    """Every non-meta `page.content` key must carry a `data-field` marker.

    This bijection is what lets the section walk stand for the whole page: it
    held at 138/138 and 245/245 on the two exports measured 2026-09-11. If it
    stops holding, slots are being missed, and that must be loud.
    """
    content = doc["page"].get("content") or {}
    html = doc["page"]["htmlCompiled"]
    marked = set(re.findall(r'data-field="([^"]*)"', html))
    missing = [k for k in content if not k.startswith("__") and k not in marked]
    if missing:
        warnings.append(
            "%d `page.content` key(s) carry no data-field marker and cannot be "
            "placed: %s%s" % (len(missing), ", ".join(sorted(missing)[:8]),
                              " ..." if len(missing) > 8 else ""))
    return missing


def brief_bullets(raw_features):
    """The '•'-prefixed lines of brief.rawFeatures, one per entry."""
    if not raw_features:
        return []
    return [ln.lstrip("•").strip()
            for ln in raw_features.splitlines()
            if ln.strip().startswith("•")]


def brief_specification(doc):
    """The manufacturer's own line, preferring the page's own spec field."""
    content = doc["page"].get("content") or {}
    if content.get("product.spec"):
        return content["product.spec"]
    raw = (doc.get("brief") or {}).get("rawFeatures") or ""
    m = re.search(r"Specification:\s*(.+)", raw, re.S)
    return m.group(1).strip() if m else None


# ------------------------------------------------------------------ scaffold

def scaffold(doc, export_path):
    page = doc["page"]
    brief = doc.get("brief") or {}
    html = page["htmlCompiled"]
    warnings = []
    check_marker_coverage(doc, warnings)

    # Which <section> an image sits in. Provenance only — it does not group the
    # slots (see section_of) and it does not supply the copy either.
    block_of = {}
    for sec in parse_sections(html):
        for field, _tag in image_fields(sec["inner"]):
            block_of.setdefault(field, sec["block_key"])

    # The copy a reader needs to assign a role, gathered PER ADR-050 SECTION from
    # the export's own `page.content`, in document order.
    #
    # Taking it from the containing <section> instead is wrong for exactly the
    # case ADR-050 exists to handle, and the clip-fan advertorial is that case:
    # `content`, `product`, `product_end` and `reviews` are four sections by the
    # slot-id rule and ONE `<section data-block-key="features">` in the markup, so
    # all four came back carrying the same 4,000-character blob. A reader asked to
    # assign four different roles was shown the same text four times.
    copy_by_section = {}
    content = page.get("content") or {}
    for m in re.finditer(r'data-field="([^"]*)"', html):
        field = m.group(1)
        val = content.get(field)
        if not isinstance(val, str) or not val.strip():
            continue
        if val.startswith(("http://", "https://", "data:")):
            continue
        bucket = copy_by_section.setdefault(section_of(field), [])
        text = htmllib.unescape(re.sub(r"<[^>]+>", " ", val))
        text = re.sub(r"\s+", " ", text).strip()
        if text and text not in bucket:
            bucket.append(text)

    # One pass over every image field in DOM order. Grouping is ADR-050's;
    # ordering is the document's; an image outside every <section> is placed
    # like any other, which is why there is no "unplaced" case any more.
    groups, order = {}, []
    for field, tag in image_fields(html):
        key = section_of(field)
        if key not in groups:
            groups[key] = {"slots": [], "dropped": [], "blocks": []}
            order.append(key)
        g = groups[key]
        b = block_of.get(field)
        if b and b not in g["blocks"]:
            g["blocks"].append(b)
        reason = out_of_scope(field)
        if reason:
            g["dropped"].append({"slot_id": field, "reason": reason})
            continue
        r = ratio_for(tag)
        if r is None:
            g["slots"].append({
                "slot_id": field,
                "ratio": None,
                "RATIO-UNRESOLVED": ("the markup states no rendered box and the "
                                     "asset carries no width/height; supply one "
                                     "of ADR-016's five"),
            })
        else:
            slot = {"slot_id": field, "ratio": r["ratio"]}
            if r["note"]:
                slot["ratio_note"] = r["note"]
            g["slots"].append(slot)

    sections = []
    for key in order:
        g = groups[key]
        sections.append({
            "id": key,
            "role": None,
            "copy_summary": None,
            "image_slots": g["slots"],
            "_block_keys": g["blocks"],
            "_copy": " · ".join(copy_by_section.get(key, []))[:900],
            "_out_of_scope": g["dropped"],
        })

    unresolved = [sl["slot_id"] for s_ in sections for sl in s_["image_slots"]
                  if not sl.get("ratio")]
    if unresolved:
        warnings.append(
            "%d in-scope slot(s) have no derivable ratio and need one of "
            "ADR-016's five by hand: %s" % (len(unresolved),
                                            ", ".join(unresolved)))

    return {
        "_README": [
            "WORKSHEET — fill every NEEDS-DECISION value, then run `build`.",
            "Keys beginning with `_` are context for the reader and are ignored "
            "by `build`.",
            "`role` must be one of the contract's twelve and follows what the "
            "section's COPY argues, not which block it sits in. `_copy` is there "
            "to be read.",
            "A section whose role stays null is dropped unless it has image "
            "slots, in which case `build` refuses: an image slot with no role "
            "cannot be routed.",
            "Sections are ADR-050's grouping of the slot ids, in document "
            "order. SPLIT one further where a repeating block's items argue "
            "different things and give each its own id and role: "
            "advertorial-cord-tensioner-cam-lock-v01 split content.items.0-6 "
            "into seven sections carrying six different roles. Merging two is "
            "not a thing to do — the grouping is already the coarsest the "
            "cross-slot rules allow.",
        ],
        "_source": {
            "export": os.path.basename(export_path),
            "lpTypeId": page.get("lpTypeId"),
            "handle": page.get("handle"),
            "title": page.get("title"),
            "pageId": (doc.get("sourceRefs") or {}).get("pageId"),
            "exportedAt": doc.get("exportedAt"),
        },
        "_warnings": warnings,
        "channel": "NEEDS-DECISION: one of marketplace | landing-page | "
                   "paid-social | advertorial. The export does not carry it and "
                   "ADR-059 forbids guessing it from lpTypeId.",
        "product": {
            "name": brief.get("productName"),
            "category": "NEEDS-DECISION (optional, ADR-085): the product's "
                        "category as a string, or empty when there is none.",
            "reference_photos": [],
            "attributes": "NEEDS-DECISION: the eight product.attributes, "
                          "supplied by the app (owner decision, 2026-09-11). "
                          "Replace this string with the object.",
            "problems_solved": "NEEDS-DECISION: array of what the buyer suffers, "
                               "at least one. `_persona_core_pain` below is the "
                               "material.",
            "specification": brief_specification(doc),
            "raw_features": brief_bullets(brief.get("rawFeatures")),
            "personas": [brief["persona"]] if brief.get("persona") else [],
            "_persona_core_pain": brief.get("personaCorePain"),
            "_awareness_stage": brief.get("awarenessStage"),
        },
        "sections": sections,
    }


# --------------------------------------------------------------------- build

def build(doc, decisions, export_path):
    page = doc["page"]
    warnings = []
    check_marker_coverage(doc, warnings)

    channel = decisions.get("channel")
    if not isinstance(channel, str) or channel.startswith("NEEDS-DECISION"):
        raise ConversionError(
            "`channel` is still unanswered. The export does not carry it and "
            "ADR-059 forbids deriving it from lpTypeId.")

    dp = decisions.get("product")
    if not isinstance(dp, dict):
        raise ConversionError("the worksheet carries no `product` object")

    attrs = dp.get("attributes")
    if not isinstance(attrs, dict):
        raise ConversionError(
            "`product.attributes` is still unanswered. The app supplies the "
            "eight (owner decision, 2026-09-11); this converter validates them "
            "and never derives them.")
    missing = [k for k in REQUIRED_ATTRS if k not in attrs]
    if missing:
        raise ConversionError(
            "`product.attributes` is missing %d of the eight: %s"
            % (len(missing), ", ".join(missing)))
    vo = attrs.get("visible_output")
    if isinstance(vo, str) and vo not in VISIBLE_OUTPUT_TOKENS:
        warnings.append(
            "`visible_output` is %r, which is not one of the eight documented "
            "tokens. The contract types it as a free string so this passes, but "
            "`mapping/slot-rules.md` gates on `!= none`, so any prose here binds "
            "G8 and makes the output the primary subject."
            % (vo[:60] + ("..." if len(vo) > 60 else ""),))

    sections, seen = [], set()
    for s in decisions.get("sections") or []:
        role = s.get("role")
        slots = [sl for sl in (s.get("image_slots") or [])]
        if role in (None, "") or (isinstance(role, str)
                                  and role.startswith("NEEDS-DECISION")):
            if slots:
                raise ConversionError(
                    "section `%s` carries %d image slot(s) and no role — an "
                    "image slot with no role cannot be routed. Read its `_copy` "
                    "and assign one." % (s.get("id"), len(slots)))
            continue
        sid = s.get("id")
        if not sid:
            raise ConversionError("a section in the worksheet has no `id`")
        if sid in seen:
            raise ConversionError(
                "two sections share the id `%s`; ids must be distinct so a "
                "prompt can name the slot it fills" % sid)
        seen.add(sid)

        clean = []
        for sl in slots:
            if not sl.get("ratio"):
                raise ConversionError(
                    "slot `%s` in section `%s` has no ratio; supply one of "
                    "ADR-016's five" % (sl.get("slot_id"), sid))
            clean.append({k: v for k, v in sl.items()
                          if k in ("slot_id", "ratio", "position")})
        out = {"id": sid, "role": role, "image_slots": clean}
        if s.get("copy_summary"):
            out["copy_summary"] = s["copy_summary"]
        else:
            warnings.append("section `%s` has no copy_summary" % sid)
        sections.append(out)

    if not sections:
        raise ConversionError(
            "no section survived: every one was left without a role. The "
            "contract requires at least one.")

    # `category` is optional since ADR-085. An undecided worksheet value — the
    # scaffold's placeholder, or an empty string — is dropped rather than
    # shipped: the placeholder is a non-empty string, so the schema would accept
    # it as a category. A decided value ships unchanged, in its old position.
    product = {"name": dp.get("name")}
    category = dp.get("category")
    if (isinstance(category, str) and category.strip()
            and not category.startswith("NEEDS-DECISION")):
        product["category"] = category
    product.update({
        "reference_photos": dp.get("reference_photos") or [],
        "attributes": attrs,
        "problems_solved": dp.get("problems_solved"),
    })
    for opt in ("specification", "raw_features", "personas"):
        if dp.get(opt):
            product[opt] = dp[opt]

    content = {"product": product,
               "page": {"channel": channel, "sections": sections}}
    if page.get("lpTypeId"):
        content["page"]["lpTypeId"] = page["lpTypeId"]

    with open(SCHEMA_PATH, encoding="utf-8") as f:
        schema = json.load(f)
    problems = schema_errors(content, schema)
    if problems:
        raise ConversionError(
            "the result does not satisfy mapping/content.schema.json:\n  - "
            + "\n  - ".join(problems[:12])
            + ("\n  ... and %d more" % (len(problems) - 12)
               if len(problems) > 12 else ""))
    return content, warnings


# ---------------------------------------------------------------------- main

def main(argv):
    ap = argparse.ArgumentParser(
        description="flunnel page export -> content.json (SPEC 1, QUERY input)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("scaffold", help="emit a worksheet to fill in")
    a.add_argument("export")
    a.add_argument("-o", "--out")

    b = sub.add_parser("build", help="export + filled worksheet -> content.json")
    b.add_argument("export")
    b.add_argument("-d", "--decisions", required=True)
    b.add_argument("-o", "--out")

    args = ap.parse_args(argv)
    try:
        doc = load_export(args.export)
        if args.cmd == "scaffold":
            result = scaffold(doc, args.export)
            warnings = result["_warnings"]
        else:
            with open(args.decisions, encoding="utf-8") as f:
                decisions = json.load(f)
            result, warnings = build(doc, decisions, args.export)
    except ConversionError as e:
        print("REFUSED  %s" % e, file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError) as e:
        print("REFUSED  %s" % e, file=sys.stderr)
        return 2

    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print("wrote %s" % args.out)
    else:
        sys.stdout.write(text)

    for w in warnings:
        print("WARN  %s" % w, file=sys.stderr)
    if args.cmd == "scaffold":
        n = sum(len(s["image_slots"]) for s in result["sections"])
        d = sum(len(s["_out_of_scope"]) for s in result["sections"])
        print("scaffold: %d sections, %d image slots in scope, %d out of scope"
              % (len(result["sections"]), n, d), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
