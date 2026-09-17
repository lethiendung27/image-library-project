#!/usr/bin/env python3
"""Check prompts.json for pdp-dr-seat-cushion-l-shaped-v08 against LP2 law, then prove the checker
live on known-bad copies of the same document.

Run from anywhere: python3 query/sessions/pdp-dr-seat-cushion-l-shaped-v08/check.py
Exit 0 means the clean set passes AND every mutation fires. Exit 1 otherwise.

What it checks, per prompt: the length gate; the LP2 product block exactly when the product is in
frame; the session lock's lines word for word; words only in gallery tiles, as a title of 2-5
words; casting named positively; no ratio, avoid clause or repo name; no product-describing word.
Under ADR-104: every photograph carries the lock's light and grade lines (a 01-pain-split tile the
light line alone); no photograph is set at night or in drained colour; nobody wears a drab colour;
and the build's hero sentences and light and grade lines equal the law file's, read from it.
Per page: three distinct types per field or a stated pool basis; pairs carrying one locked
description; every image field of the exported page either routed or listed as not generated.
"""
import copy
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
EXPORT = os.path.expanduser("~/Downloads/pdp-dr-ergonomic-memory-foam-seat-cushion-v04.json")
LAW = os.path.join(ROOT, "registry", "pdp-dr-instruction.md")
sys.path.insert(0, HERE)
import build  # noqa: E402  (the constants are defined once, in the build)

GATE = 1800
NEVER = ["perfect", "ultimate", "premium", "luxury", "every", "all-day", "approved", "tested", "safe",
         "certified", "proven", "guaranteed", "clinical", "best", "instant", "pain-free", "cure"]
PRODUCT_WORDS = ["black colourway", "mesh", "ribbed", "ribs", "vents", "cut-out", "cutout", "zip",
                 "zipper", "handle", "piping", "foam colour"]
REPO = [r"\b0\d-[a-z]+-[a-z]+\b", r"--[a-z]", r"\bLP2\b", r"\bADR\b", r"\bG\d+\b", r"\bpdp\b",
        r"\bgallery tile\b", r"\bsection image\b"]
LIT_TYPES = {"06-relief-hero", "06-relief-scene", "05-social-snapshot", "05-persona-grid",
             "03-use-grid", "03-spec-macro", "04-proof-lockedframe"}
DRAINED = re.compile(r"\b(night|dusk|evening|lamplight|lamp|fluorescent|overcast|dim|neutral|"
                     r"nothing saturated|pale walls|washed-out)\b")
DRAB = re.compile(r"\b(beige|greige|grey|gray|taupe|oatmeal|khaki)\s+(?:[a-z]+\s+)?(sweater|shirt|"
                  r"trousers|jacket|cardigan|sleeves?|blazer|top|hoodie|jeans|dress)\b")
ALLOWED_RATIOS = {"16:9", "4:3", "1:1", "3:4", "9:16"}


def check(doc, fields):
    fail = []
    law = doc["_law"]
    if build.HERO_FIXED + [build.HERO_PERSON] != law["hero"]:
        fail.append(("page", "the build's hero sentences differ from the law file's"))
    if [build.LIGHT, build.GRADE] != law["lock"]:
        fail.append(("page", "the lock's light or grade line differs from the law file's"))
    slots = [s for s in doc["slots"] if s.get("options")]
    listed = {s["slot_id"] for s in doc["slots"]}
    if set(fields) != listed:
        fail.append(("page", f"image fields not accounted for: missing {sorted(set(fields) - listed)}, "
                             f"extra {sorted(listed - set(fields))}"))
    assets = [s["asset"] for s in slots]
    if len(set(assets)) != len(assets):
        fail.append(("page", "an asset filename is used twice"))
    gallery = [s for s in slots if s["kind"] == "gallery"]
    rec = {s["slot_id"]: s["options"]["ABC".index(s["recommended_option"])] for s in slots}
    titled = [s for s in gallery if '"' in rec[s["slot_id"]]["prompt"]]
    if len(gallery) - len(titled) < 1:
        fail.append(("gallery", "no wordless tile among the recommended options (rule 9)"))
    macros = [s for s in gallery if rec[s["slot_id"]]["type"] == "03-spec-macro"]
    if len(macros) > 1:
        fail.append(("gallery", "more than one macro recommended in the gallery"))
    for s in slots:
        sid = s["slot_id"]
        if s["ratio"] not in ALLOWED_RATIOS:
            fail.append((sid, f"ratio {s['ratio']} outside ADR-016"))
        types = [o["type"] for o in s["options"]]
        if len(set(types)) < 3 and not s.get("pool_basis"):
            fail.append((sid, "fewer than three distinct types and no pool_basis"))
        if s["kind"] in ("buyer-wall", "pair") and not s.get("compliance"):
            fail.append((sid, "a buyer tile or pair without its compliance flag"))
        for o in s["options"]:
            ctx = f"{sid} {o['option']}"
            p = o["prompt"]
            flat = re.sub(r"\s+", " ", p)
            if len(p) > GATE:
                fail.append((ctx, f"LENGTH {len(p)} > {GATE}"))
            has_block = build.BLOCK in flat
            if bool(o["attachments"]) != has_block:
                fail.append((ctx, f"product block present={has_block} but attachments={o['attachments']}"))
            if "Use the attached product photo" in flat and not has_block:
                fail.append((ctx, "the product block is reworded"))
            for line, name in ((build.NOFRAME, "no-frame"), (build.CORNER, "corner")):
                if flat.count(line) != 1:
                    fail.append((ctx, f"lock line {name} appears {flat.count(line)} times"))
            for raw in p.splitlines():
                ln = raw.strip()
                if ln.startswith("Light:") and ln != build.LIGHT:
                    fail.append((ctx, f"a light line in other words: {ln[:50]!r}"))
                if ln.startswith("Grade:") and ln != build.GRADE:
                    fail.append((ctx, f"a grade line in other words: {ln[:50]!r}"))
                if ln.startswith("Ground:") and ln not in (build.ROOM, build.SEAMLESS):
                    fail.append((ctx, f"a ground line in other words: {ln[:50]!r}"))
            split_tile = o["type"] == "01-pain-split" and s["kind"] != "pair"
            if (o["type"] in LIT_TYPES or s["kind"] == "pair") and not (build.LIGHT in p and build.GRADE in p):
                fail.append((ctx, "a photographic frame without the lock's light and grade lines"))
            if split_tile:
                if flat.count(build.LIGHT) != 1:
                    fail.append((ctx, "a split tile without the light line"))
                if build.GRADE in p:
                    fail.append((ctx, "a split tile carrying the grade line, which forbids its grayscale panel"))
            if o["type"] in LIT_TYPES or s["kind"] == "pair" or split_tile:
                hit = DRAINED.search(flat.replace(build.BLOCK, " ").lower())
                if hit:
                    fail.append((ctx, f"a night, dim or drained scene under the daylight lock: {hit.group(0)!r}"))
            hit = DRAB.search(flat.lower())
            if hit:
                fail.append((ctx, f"a drab wardrobe: {hit.group(0)!r}"))
            if s["kind"] == "hero":
                for line in build.HERO_FIXED:
                    if flat.count(line) != 1:
                        fail.append((ctx, f"a hero without the fixed sentence {line[:40]!r}"))
                person = bool(re.search(r"\b(man|woman|person)\b",
                                        flat.replace(build.HERO_PERSON, " ").lower()))
                if (flat.count(build.HERO_PERSON) == 1) != person:
                    fail.append((ctx, f"the hero's person sentence present="
                                      f"{build.HERO_PERSON in flat}, person in frame={person}"))
            quoted = re.findall(r'"([^"]+)"', p)
            if s["kind"] == "gallery":
                if quoted:
                    if len(quoted) != 1:
                        fail.append((ctx, f"more than the title in frame: {quoted}"))
                    q = quoted[0]
                    n = len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", q))
                    cap = 4 if o["type"] == "03-spec-macro" else 5
                    if not 2 <= n <= cap:
                        fail.append((ctx, f"title {q!r} of {n} words, outside 2-{cap}"))
                    if re.search(r"\d", q):
                        fail.append((ctx, f"a figure in the title {q!r}"))
                    for w in NEVER:
                        if re.search(rf"(?<![a-z-]){re.escape(w)}(?![a-z-])", q.lower()):
                            fail.append((ctx, f"never-list word {w!r} in the title"))
                    if not (build.TYPE_LIGHT in p or build.TYPE_DARK in p):
                        fail.append((ctx, "a title without the lock's typography line"))
                    if build.WORDLESS in p:
                        fail.append((ctx, "a titled tile that also says it carries no words"))
                elif flat.count(build.WORDLESS) != 1:
                    fail.append((ctx, "a wordless gallery tile without the no-words line"))
            else:
                if quoted:
                    fail.append((ctx, f"words in an image outside the gallery: {quoted}"))
                if build.TYPE_LIGHT in p or build.TYPE_DARK in p:
                    fail.append((ctx, "a typography line outside the gallery"))
                if flat.count(build.WORDLESS) != 1:
                    fail.append((ctx, "the no-words line missing or repeated outside the gallery"))
            scan = flat
            for line in (build.BLOCK, build.TYPE_LIGHT, build.TYPE_DARK):
                scan = scan.replace(line, " ")
            low = scan.lower()
            if re.search(r"\b(man|woman)\b", low) and "north american" not in low:
                fail.append((ctx, "a person with no casting named"))
            if "asian" in low:
                fail.append((ctx, "casting named in the negative"))
            for w in PRODUCT_WORDS:
                if re.search(rf"(?<![a-z-]){re.escape(w)}(?![a-z-])", low):
                    fail.append((ctx, f"G2: a product-describing word {w!r}"))
            for pat in REPO:
                if re.search(pat, p):
                    fail.append((ctx, f"a repo name reaches the prompt: /{pat}/"))
            if re.search(r"\b\d+\s*:\s*\d+\b", p) or re.search(r"\b(aspect ratio|square format)\b", low):
                fail.append((ctx, "names the frame's ratio"))
            if re.search(r"(?i)\bavoid\b", p):
                fail.append((ctx, "an avoid clause"))
    for s in slots:
        if s["kind"] == "pair":
            for o in s["options"]:
                if "grayscale" in o["prompt"].lower():
                    fail.append((f"{s['slot_id']} {o['option']}", "a pair half is desaturated, a "
                                 "second difference beside the state line"))
    # pairs: both files take the same types in the same order and share the locked description
    by_id = {s["slot_id"]: s for s in slots}
    for s in slots:
        if s["kind"] != "pair":
            continue
        other = by_id.get(s.get("pair_with") or "")
        if not other:
            fail.append((s["slot_id"], "a pair whose partner is missing"))
            continue
        if [o["type"] for o in s["options"]] != [o["type"] for o in other["options"]]:
            fail.append((s["slot_id"], "the two files of a pair offer different types"))
        for a, b in zip(s["options"], other["options"]):
            la = re.search(r"The same scene in both photographs of this pair:[^\n]*", a["prompt"])
            lb = re.search(r"The same scene in both photographs of this pair:[^\n]*", b["prompt"])
            if not la or not lb or la.group(0) != lb.group(0):
                fail.append((s["slot_id"], f"option {a['option']}: the locked description differs "
                                           "between the two files"))
    return fail


def fields_from_export():
    if not os.path.exists(EXPORT):
        raise SystemExit(f"the export is not at {EXPORT}")
    html = json.load(open(EXPORT, encoding="utf-8"))["page"]["htmlCompiled"]
    return re.findall(r'data-field="([^"]+)"[^>]*data-field-type="image"', html)


def mutations(doc):
    """(name, mutate(doc) -> None, expected message fragment)"""
    def m(name, fn, expect):
        return (name, fn, expect)

    return [
        m("drop a field", lambda d: d["slots"].pop(), "image fields not accounted for"),
        m("long prompt", lambda d: _o(d, "hero.image", "A").__setitem__(
            "prompt", _o(d, "hero.image", "A")["prompt"] + " x" * 20 + " " + "y" * 60 * 5), "LENGTH"),
        m("block reworded", lambda d: _sub(d, "hero.image", "A", "Do not redesign, restyle", "Do not change"),
          "product block present=False"),
        m("attachments without block", lambda d: _o(d, "problem.items.1.image", "A").__setitem__(
            "attachments", ["sha256:0000000000000000"]), "product block present=False"),
        m("corner dropped", lambda d: _sub(d, "why.photo", "A", build.CORNER, ""), "lock line corner appears 0"),
        m("light reworded", lambda d: _sub(d, "why.photo", "A", "real contrast", "soft contrast"),
          "a light line in other words"),
        m("ground reworded", lambda d: _sub(d, "how.image", "A", "a few clear colours", "warm-neutral tones"),
          "a ground line in other words"),
        m("words in a section", lambda d: _sub(d, "how.image", "A", build.CORNER,
                                               build.CORNER + ' A sign reads "Home".'),
          "words in an image outside the gallery"),
        m("typography outside gallery", lambda d: _sub(d, "uses.image", "A", build.CORNER,
                                                       build.CORNER + " " + build.TYPE_LIGHT),
          "a typography line outside the gallery"),
        m("six-word title", lambda d: _sub(d, "media.gallery.1.image", "A", '"Hips level, back supported"',
                                           '"Hips level and your back supported"'), "outside 2-5"),
        m("five-word macro title", lambda d: _sub(d, "media.gallery.3.image", "A", '"One piece, no gap"',
                                                  '"One piece and no gap"'), "outside 2-4"),
        m("figure in title", lambda d: _sub(d, "media.gallery.4.image", "A", '"Stays put on leather"',
                                            '"Stays put 100% of time"'), "a figure in the title"),
        m("never-list title", lambda d: _sub(d, "media.gallery.2.image", "A", '"Takes pressure off tailbone"',
                                             '"Best tailbone relief"'), "never-list word 'best'"),
        m("title without typography", lambda d: _sub(d, "media.gallery.4.image", "A", build.TYPE_DARK, ""),
          "a title without the lock's typography line"),
        m("no wordless tile", lambda d: _sub(d, "media.gallery.5.image", "A", build.WORDLESS,
                                             'In the upper left the title reads "Smooth long drives". '
                                             + build.TYPE_LIGHT), "no wordless tile"),
        m("second macro", lambda d: _set_rec(d, "media.gallery.4.image", "C"), "more than one macro"),
        m("no casting", lambda d: _sub(d, "why.photo", "A", "A North American woman", "A woman"),
          "a person with no casting named"),
        m("negative casting", lambda d: _sub(d, "why.photo", "B", build.CORNER, build.CORNER + " She is not Asian."),
          "casting named in the negative"),
        m("product colour", lambda d: _sub(d, "how.image", "C", "Two hands press", "Two hands press the black colourway of"),
          "G2: a product-describing word 'black colourway'"),
        m("repo name", lambda d: _sub(d, "faq.image", "A", build.CORNER, build.CORNER + " Route as 06-relief-hero."),
          "a repo name reaches the prompt"),
        m("ratio", lambda d: _sub(d, "faq.image", "B", build.CORNER, build.CORNER + " Frame 16:9."),
          "names the frame's ratio"),
        m("avoid", lambda d: _sub(d, "faq.image", "C", build.CORNER, build.CORNER + " Avoid clutter."),
          "an avoid clause"),
        m("two types, no basis", lambda d: _by(d, "hero.image")["options"][2].__setitem__("type", "06-relief-hero"),
          "fewer than three distinct types"),
        m("pair basis dropped", lambda d: _by(d, "expect.items.0.before_image").__setitem__("pool_basis", None),
          "fewer than three distinct types"),
        m("flag dropped", lambda d: _by(d, "trusted.cards.2.photo").__setitem__("compliance", None),
          "without its compliance flag"),
        m("pair drift", lambda d: _sub(d, "expect.items.1.after_image", "A", "in a cardigan", "in a blazer"),
          "the locked description differs"),
        m("pair types differ", lambda d: _by(d, "testimonials.items.2.after_image")["options"].reverse(),
          "offer different types"),
        m("bad ratio", lambda d: _by(d, "expert.photo").__setitem__("ratio", "4:5"), "outside ADR-016"),
        m("grayscale pair half", lambda d: _sub(d, "expect.items.2.before_image", "B", "It is a month later",
                                                "This photograph is in grayscale. It is a month later"),
          "a pair half is desaturated"),
        m("macro person uncast", lambda d: _sub(d, "modes.items.2.image", "A", "North American woman's",
                                                "woman's"), "a person with no casting named"),
        m("hero sentence dropped", lambda d: _sub(d, "hero.image", "A", build.HERO_FIXED[1], ""),
          "a hero without the fixed sentence"),
        m("hero sentence reworded", lambda d: _sub(d, "hero.image", "C", "well clear of the right edge",
                                                   "clear of the right edge"), "a hero without the fixed sentence"),
        m("hero person sentence missing", lambda d: _sub(d, "hero.image", "B", build.HERO_PERSON, ""),
          "the hero's person sentence present=False"),
        m("hero person sentence without a person", lambda d: _sub(d, "hero.image", "C", build.HERO_FIXED[3],
                                                                  build.HERO_FIXED[3] + " " + build.HERO_PERSON),
          "the hero's person sentence present=True"),
        m("lit frame unlit", lambda d: _sub(d, "uses.image", "B", build.GRADE, ""),
          "without the lock's light and grade lines"),
        m("lockedframe unlit", lambda d: _sub(d, "safety.image", "B", build.GRADE, ""),
          "without the lock's light and grade lines"),
        m("neutral grade", lambda d: _sub(d, "problem.items.2.image", "C", "Both panels share one grade;",
                                          "Grade: one neutral grade across both panels;"),
          "a grade line in other words"),
        m("law hero drift", lambda d: d["_law"]["hero"].__setitem__(2, "The left half is bright and calm."),
          "the build's hero sentences differ"),
        m("law lock drift", lambda d: d["_law"]["lock"].__setitem__(1, "Grade: bright, neutral."),
          "the lock's light or grade line differs"),
        m("night scene", lambda d: _sub(d, "uses.image", "B", "by a sunny window", "at night"),
          "a night, dim or drained scene"),
        m("drained room", lambda d: _sub(d, "trusted.cards.3.photo", "A", "no studio light",
                                         "pale walls, no studio light"), "a night, dim or drained scene"),
        m("split tile graded", lambda d: _sub(d, "media.gallery.1.image", "A", build.LIGHT,
                                              build.LIGHT + "\n" + build.GRADE),
          "a split tile carrying the grade line"),
        m("split tile unlit", lambda d: _sub(d, "problem.items.0.image", "A", build.LIGHT, ""),
          "a split tile without the light line"),
        m("drab wardrobe", lambda d: _sub(d, "modes.items.2.image", "A", "denim-blue trousers", "grey trousers"),
          "a drab wardrobe"),
    ]


def _by(d, sid):
    for s in d["slots"]:
        if s["slot_id"] == sid:
            return s
    raise KeyError(sid)


def _o(d, sid, letter):
    return _by(d, sid)["options"]["ABC".index(letter)]


def _sub(d, sid, letter, a, b):
    o = _o(d, sid, letter)
    assert a in o["prompt"], f"mutation anchor missing in {sid} {letter}: {a[:40]!r}"
    o["prompt"] = o["prompt"].replace(a, b, 1)


def _set_rec(d, sid, letter):
    _by(d, sid)["recommended_option"] = letter


def law_lines():
    """The hero's five fixed sentences and the lock's two lines, as the law file states them."""
    text = open(LAW, encoding="utf-8").read()

    def block_after(marker):
        i = text.index(marker)
        a = text.index("```", i) + 3
        b = text.index("```", a)
        return [ln.strip() for ln in text[a:b].strip().splitlines() if ln.strip()]

    return {"hero": block_after("**Every hero prompt carries these sentences"),
            "lock": block_after("**A hero is a photograph in full colour**")}


def main():
    doc = json.load(open(os.path.join(HERE, "prompts.json"), encoding="utf-8"))
    doc["_law"] = law_lines()
    assert len(doc["_law"]["hero"]) == 5 and len(doc["_law"]["lock"]) == 2, doc["_law"]
    fields = fields_from_export()
    clean = check(doc, fields)
    bad = 0
    if clean:
        bad += 1
        print("CLEAN SET FAILED:")
        for c, msg in clean:
            print("  FAIL", c, "—", msg)
    n = 0
    for name, fn, expect in mutations(doc):
        n += 1
        d = copy.deepcopy(doc)
        fn(d)
        out = check(d, fields)
        if any(expect in msg for _c, msg in out):
            print(f"fired  {name}")
        else:
            bad += 1
            print(f"MISSED {name}: expected {expect!r}; got {out[:3]}")
    print(f"image fields in the export: {len(fields)}; routed: "
          f"{sum(1 for s in doc['slots'] if s.get('options'))}; prompts: "
          f"{sum(len(s['options']) for s in doc['slots'] if s.get('options'))}")
    print("PASS" if not bad else f"{bad} problem(s)", f"— {n} mutations")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
