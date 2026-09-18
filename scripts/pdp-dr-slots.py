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

A second table in the same file, `## Section routing`, gives every generated field a DEFAULT
ROLE from its section's name (ADR-102, owner decision 2026-09-17: on an LP2 page an image depends
on its section's name and on the copy written in that section). The name is the field's enclosing
`data-block-key`, or its path's first segment where it has none. A row holds backticked globs over
that name and ONE backticked value:
- a role from `section_roles` in `registry/vocabulary.yaml`;
- `@tile`, a gallery tile, which is routed on its own;
- `@copy`, where the section's copy alone decides.
The copy may move any default; the script only says where routing starts.

Since ADR-110 (owner instruction, 2026-09-18) the same table carries a third column, the
section's SECTION TYPE: the type a field in that block takes first. It holds ONE backticked
value, a type with a file in `registry/pdp-dr-types/` or one of four tokens — `@gallery`,
`@hero`, `@pair`, `@copy`. Where a field's own Slot kinds row names a type in its last cell,
that type is the field's and the section's is not read: the table says so, and a pair's two
fields are the case. The script prints the type with its `status` where that is not `active`,
because a reserved draft does not route yet. A table without the column still parses, and
the column then prints as `—`.

Usage:
  python3 scripts/pdp-dr-slots.py TEMPLATE.html            # table per field, then counts
  python3 scripts/pdp-dr-slots.py TEMPLATE.html --json     # the same, as JSON
  python3 scripts/pdp-dr-slots.py --rules                  # both parsed tables
  python3 scripts/pdp-dr-slots.py TEMPLATE.html --rules-from FILE   # another table

Exit 1 when a table cannot be parsed, a role is not in the vocabulary, a section type has no
file, or a field matches no row, 2 on bad usage.
"""
import fnmatch
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES = os.path.join(ROOT, "mapping", "pdp-dr-rules.md")
VOCAB = os.path.join(ROOT, "registry", "vocabulary.yaml")
TYPES_DIR = os.path.join(ROOT, "registry", "pdp-dr-types")
GENERATED = {"hero", "gallery", "section", "pair", "buyer-wall", "closing"}
ROLE_TOKENS = {"@tile", "@copy"}
TYPE_TOKENS = {"@gallery", "@hero", "@pair", "@copy"}
TYPE_ID = re.compile(r"^\d\d-[a-z]+-[a-z]+$")
PORTRAIT_BLOCKS = {"reviews", "expert", "testimonials", "trusted"}
PORTRAIT_MAX_WIDTH = 160
VOID = {"img", "br", "hr", "input", "meta", "link", "source", "area", "base",
        "col", "embed", "param", "track", "wbr"}


def type_status(tid):
    """The `status:` of a pdp-dr type file. A type with no file is a table error."""
    path = os.path.join(TYPES_DIR, tid + ".md")
    if not os.path.exists(path):
        raise ValueError(f"`{tid}` has no file in registry/pdp-dr-types/")
    with open(path, encoding="utf-8") as f:
        if f.readline().strip() != "---":
            raise ValueError(f"{path}: no frontmatter")
        for line in f:
            if line.strip() == "---":
                break
            if line.startswith("status:"):
                return line.split(":", 1)[1].strip()
    raise ValueError(f"{path}: no `status:` in its frontmatter")


def parse_rules(path):
    """Rows of the first table under `## Slot kinds`: (patterns, kind, words, image, type).

    `type` is the first type id backticked in the row's last cell, or None. A row that
    names one gives it to every field it matches.
    """
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
        named = [v for v in re.findall(r"`([^`]+)`", cells[3]) if TYPE_ID.match(v)]
        if named:
            type_status(named[0])
        rows.append((patterns, cells[1].strip("*"), cells[2], cells[3],
                     named[0] if named else None))
    if not rows:
        raise ValueError(f"{path}: the Slot kinds table has no rows")
    return rows


def section_roles(path=VOCAB):
    """The closed role list, read from the `section_roles: [...]` line of the vocabulary."""
    with open(path, encoding="utf-8") as f:
        m = re.search(r"^section_roles:\s*\[([^\]]*)\]", f.read(), re.M)
    if not m:
        raise ValueError(f"{path}: no `section_roles: [...]` line")
    return {r.strip() for r in m.group(1).split(",") if r.strip()}


def parse_sections(path, roles):
    """Rows of the first table under `## Section routing`: (patterns, role, section type).

    The section type is None where the table has no third column headed `section type`.
    """
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"^## Section routing\b.*?$", text, re.M)
    if not m:
        raise ValueError(f"{path}: no `## Section routing` section")
    body = text[m.end():]
    nxt = re.search(r"^## ", body, re.M)
    if nxt:
        body = body[:nxt.start()]
    rows, in_table, has_type = [], False, False
    for line in body.splitlines():
        if not line.startswith("|"):
            if in_table:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not in_table:
            if [c.lower() for c in cells[:2]] != ["section name", "default role"]:
                raise ValueError(f"{path}: the Section routing table must open with "
                                 "`| section name | default role |`")
            has_type = len(cells) > 2 and cells[2].lower() == "section type"
            in_table = True
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        patterns = re.findall(r"`([^`]+)`", cells[0])
        values = re.findall(r"`([^`]+)`", cells[1]) if len(cells) > 1 else []
        if not patterns or len(values) != 1:
            raise ValueError(f"{path}: a Section routing row needs backticked names and ONE "
                             f"backticked role: {line}")
        if values[0] not in roles and values[0] not in ROLE_TOKENS:
            raise ValueError(f"{path}: `{values[0]}` is neither a section role nor a token: {line}")
        stype = None
        if has_type:
            types = re.findall(r"`([^`]+)`", cells[2]) if len(cells) > 2 else []
            if len(types) != 1:
                raise ValueError(f"{path}: a Section routing row needs ONE backticked "
                                 f"section type: {line}")
            stype = types[0]
            if stype not in TYPE_TOKENS:
                if not TYPE_ID.match(stype):
                    raise ValueError(f"{path}: `{stype}` is neither a type id nor a token: {line}")
                type_status(stype)
        rows.append((patterns, values[0], stype))
    if not rows:
        raise ValueError(f"{path}: the Section routing table has no rows")
    return rows


def section_of(f, sections):
    """The Section routing row a generated field's section matches, or None."""
    for patterns, role, stype in sections:
        if any(fnmatch.fnmatchcase(f["block"], p) for p in patterns):
            return role, stype
    return None


def role_of(f, sections):
    """A generated field's default role; '—' for a field the library does not generate."""
    if f["kind"] not in GENERATED:
        return "—"
    row = section_of(f, sections)
    return row[0] if row else None


def section_type_of(f, sections):
    """A generated field's section type, with its status where that is not `active`.

    The field's own Slot kinds row wins where it names a type; otherwise the section's row.
    """
    if f["kind"] not in GENERATED:
        return "—"
    stype = f.get("row_type")
    if stype is None:
        row = section_of(f, sections)
        stype = row[1] if row else None
    if stype is None:
        return "—"
    if stype in TYPE_TOKENS:
        return stype
    status = type_status(stype)
    return stype if status == "active" else f"{stype} ({status})"


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
        for patterns, kind, words, image, row_type in rules:
            if any(matches(p, f) for p in patterns):
                out.append(dict(f, kind=kind, words=words, image=image, row_type=row_type))
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
        sections = parse_sections(rules_path, section_roles())
    except ValueError as e:
        print(f"ERROR {e}", file=sys.stderr)
        return 1
    if "--rules" in argv and not args:
        for patterns, kind, words, image, row_type in rules:
            print(f"{' '.join(patterns):58} {kind:11} {words:22} {row_type or ''}")
        print()
        for patterns, role, stype in sections:
            print(f"{' '.join(patterns):58} {role:18} {stype or '—'}")
        return 0
    if len(args) != 1:
        print(__doc__.split("Usage:")[1].split("Exit")[0], file=sys.stderr)
        return 2
    parser = Fields()
    with open(args[0], encoding="utf-8") as f:
        parser.feed(f.read())
    try:
        rows, unmatched = classify(parser.fields, rules)
        unrouted = []
        for r in rows:
            r["role"] = role_of(r, sections)
            if r["role"] is None:
                unrouted.append(r["field"])
            r["section_type"] = section_type_of(r, sections)
    except ValueError as e:
        print(f"ERROR {e}", file=sys.stderr)
        return 1
    if "--json" in argv:
        print(json.dumps({"template": args[0], "fields": rows,
                          "unmatched": unmatched, "unrouted": unrouted}, indent=1))
    else:
        for r in rows:
            print(f"{r['field']:40} {r['block']:14} {r['kind']:11} {r['frame']:7} "
                  f"{r['role'] or '?':18} {r['section_type']:32} {r['words']}")
        counts = {}
        for r in rows:
            counts[r["kind"]] = counts.get(r["kind"], 0) + 1
        print("\n" + ", ".join(f"{k} {v}" for k, v in counts.items()))
        for u in unmatched:
            print(f"ERROR {u}: matches no row of the Slot kinds table")
        for u in unrouted:
            print(f"ERROR {u}: its section matches no row of the Section routing table")
    return 1 if unmatched or unrouted else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
