#!/usr/bin/env python3
"""Give every image field of an LP2 page template its slot kind.

WHY THIS READS A TABLE INSTEAD OF OWNING ONE
-------------------------------------------
ADR-096 (owner decisions, 2026-09-17) made the kind of an image field decide what the
library may put in it: only the product card's gallery carries words, a hero is a banner
the template crops, a buyer-photo tile is always generated and flagged, and a chrome
asset is never generated at all. That law lives in the table under `## Slot kinds` in
`mapping/pdp-dr-rules.md`. This script parses that table and applies it, the way
`parse_attribute_gates()` in `scripts/validate.py` reads `mapping/slot-rules.md`, so the
table stays the only statement of the rule and a template added later needs no edit here.

A template marks an image field with `data-field-type="image"`, a dotted `data-field` path,
`data-locked` and an enclosing `data-block-key`. Rows are tried in order and the first
match wins. A row's first cell holds one or more backticked patterns: a glob over the
field path, or one of two tokens the table defines under it:

  @locked    the field's `data-locked` is `true`
  @portrait  a field in `reviews`, `expert`, `testimonials` or `trusted` whose `width`
             attribute is 160 or less

The frame column is read from the image's own sizing classes and reported for the owner,
who sets the ratio at render time. It never goes into a prompt (ADR-016).

Usage:
  python3 scripts/pdp-dr-slots.py TEMPLATE.html            # table per field, then counts
  python3 scripts/pdp-dr-slots.py TEMPLATE.html --json     # the same, as JSON
  python3 scripts/pdp-dr-slots.py --rules                  # the parsed table
  python3 scripts/pdp-dr-slots.py TEMPLATE.html --rules-from FILE   # another table

Exit 1 when the table cannot be parsed or a field matches no row, 2 on bad usage.
"""
import fnmatch
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES = os.path.join(ROOT, "mapping", "pdp-dr-rules.md")
PORTRAIT_BLOCKS = {"reviews", "expert", "testimonials", "trusted"}
PORTRAIT_MAX_WIDTH = 160
VOID = {"img", "br", "hr", "input", "meta", "link", "source", "area", "base",
        "col", "embed", "param", "track", "wbr"}


def parse_rules(path):
    """Rows of the first table under `## Slot kinds`, as (patterns, kind, words, image)."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"^## Slot kinds\b.*?$", text, re.M)
    if not m:
        raise ValueError(f"{path}: no `## Slot kinds` section")
    body = text[m.end():]
    nxt = re.search(r"^## ", body, re.M)
    if nxt:
        body = body[:nxt.start()]
    rows, in_table = [], False
    for line in body.splitlines():
        if not line.startswith("|"):
            if in_table:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not in_table:
            if [c.lower() for c in cells[:2]] != ["field path", "kind"]:
                raise ValueError(f"{path}: the Slot kinds table must open with "
                                 "`| field path | kind |`")
            in_table = True
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        if len(cells) < 4:
            raise ValueError(f"{path}: row has {len(cells)} cells, expected 4: {line}")
        patterns = re.findall(r"`([^`]+)`", cells[0])
        if not patterns:
            raise ValueError(f"{path}: row with no backticked pattern: {line}")
        rows.append((patterns, cells[1].strip("*"), cells[2], cells[3]))
    if not rows:
        raise ValueError(f"{path}: the Slot kinds table has no rows")
    return rows


class Fields(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.fields, self.seen = [], [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("data-field-type") == "image" and a.get("data-field"):
            path = a["data-field"]
            if path not in self.seen:
                self.seen.add(path)
                blocks = [b for b in self.stack if b]
                self.fields.append({
                    "field": path,
                    "block": blocks[-1] if blocks else path.split(".")[0],
                    "locked": a.get("data-locked") == "true",
                    "width": a.get("width"),
                    "height": a.get("height"),
                    "frame": frame_of(a.get("class", ""), path),
                })
        if tag not in VOID:
            self.stack.append(a.get("data-block-key"))

    def handle_endtag(self, tag):
        if tag not in VOID and self.stack:
            self.stack.pop()


def frame_of(cls, path):
    """The frame the template shows the image in, from its first sizing class."""
    if path.startswith("hero."):
        return "banner"
    m = re.search(r"(?:^|\s)aspect-(square|video|\[?\d+/\d+\]?)", cls)
    if not m:
        return "free"
    v = m.group(1).strip("[]")
    return {"square": "1:1", "video": "16:9"}.get(v, v.replace("/", ":"))


def matches(pattern, f):
    if pattern == "@locked":
        return f["locked"]
    if pattern == "@portrait":
        try:
            w = int(f["width"])
        except (TypeError, ValueError):
            return False
        return f["block"] in PORTRAIT_BLOCKS and w <= PORTRAIT_MAX_WIDTH
    if pattern.startswith("@"):
        raise ValueError(f"unknown token `{pattern}` in the Slot kinds table")
    return fnmatch.fnmatchcase(f["field"], pattern)


def classify(fields, rules):
    out, unmatched = [], []
    for f in fields:
        for patterns, kind, words, image in rules:
            if any(matches(p, f) for p in patterns):
                out.append(dict(f, kind=kind, words=words, image=image))
                break
        else:
            unmatched.append(f["field"])
    return out, unmatched


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    rules_path = RULES
    if "--rules-from" in argv:
        i = argv.index("--rules-from")
        if i + 1 >= len(argv):
            print("--rules-from needs a file", file=sys.stderr)
            return 2
        rules_path = argv[i + 1]
        args = [a for a in args if a != rules_path]
    try:
        rules = parse_rules(rules_path)
    except ValueError as e:
        print(f"ERROR {e}", file=sys.stderr)
        return 1
    if "--rules" in argv and not args:
        for patterns, kind, words, image in rules:
            print(f"{' '.join(patterns):58} {kind:11} {words}")
        return 0
    if len(args) != 1:
        print(__doc__.split("Usage:")[1].split("Exit")[0], file=sys.stderr)
        return 2
    parser = Fields()
    with open(args[0], encoding="utf-8") as f:
        parser.feed(f.read())
    try:
        rows, unmatched = classify(parser.fields, rules)
    except ValueError as e:
        print(f"ERROR {e}", file=sys.stderr)
        return 1
    if "--json" in argv:
        print(json.dumps({"template": args[0], "fields": rows,
                          "unmatched": unmatched}, indent=1))
    else:
        for r in rows:
            print(f"{r['field']:40} {r['block']:14} {r['kind']:11} {r['frame']:7} {r['words']}")
        counts = {}
        for r in rows:
            counts[r["kind"]] = counts.get(r["kind"], 0) + 1
        print("\n" + ", ".join(f"{k} {v}" for k, v in counts.items()))
        for u in unmatched:
            print(f"ERROR {u}: matches no row of the Slot kinds table")
    return 1 if unmatched else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
