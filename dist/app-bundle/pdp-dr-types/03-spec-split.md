---
id: 03-spec-split
step: 3
job: spec
device: split
version: "1.4"
status: active
replaced_by: null
channels: [marketplace]
requires_product_photo: true
generation_mode: single-pass
axes:
  register: [commercial]
variants: [products]
exempt_from: [G5, G7]
pairs_with: [03-mechanism-ghostbody]
never_with: []
copied_from: 03-spec-split
copied_at_version: "1.4"
blocked_by: null
---

# 03-spec-split

## PURPOSE
Component-level superiority: old component (real, decayed, photographic) vs new
component (engineered, pristine, rendered), diagonal split, VS badge. No people, no
symptoms. The highest-risk type in the library — see NOTES.

**Copied verbatim from `registry/types/03-spec-split.md` at version 1.4** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## TRIGGER
use_when: >
  Categories where buyers genuinely compare component specs: motors, batteries,
  chips, abrasive materials, filter media, blades. Image 4-6 in a marketplace
  gallery. Use ONLY when the product truly contains the rendered component.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 03-spec-split v1.4 [+ --products]

[PRODUCT REFERENCE] attached photo is the reference for the INSET only.
[SPLIT] one diagonal; the halves unequal in energy.       -> PARTS/split
[OLD] left, photographic: the legacy component aged.      -> PARTS/old
[NEW] right, rendered: the improved component.            -> PARTS/new
[INSET] the finished product, bottom.                     -> PARTS/inset
[MARKS] the seam, and one marker on it.                   -> MARKS

STYLE: high-contrast technical comparison graphic, e-commerce, sharp.
```

## PARTS

**`split`** — ONE diagonal, running from a named corner to its opposite. The two halves must
be visually unequal in energy, the right advancing into the left. Never a vertical split: that
is `01-pain-split`'s geometry and this type's diagonal is what separates them at a glance.

**`old`** — left half, PHOTOGRAPHIC register, desaturated. A generic, unbranded component of
the legacy type, in a dim unstyled setting. **Name the signs of age as things, not as a
number** — a chipped edge, scoring across the face, grey dust settled in the seams — because a
count has never bound in this library. It must read as a real object photographed in the real
world.

**`new`** — right half, 3D RENDER register. The same component class, pristine and of the
improved type, floating against a dark gradient with cool rim lighting and sharp reflective
surfaces. It must read as engineered, not photographed.

**Name the differentiator as LIGHT BEHAVIOUR, not as a material.** "A dense uniform field of
fine crystalline grit catching the light" renders; "diamond coating" does not — the model has
no way to draw a material name.

**`inset`** — the reference product ALONE, complete and whole, on a plain ground inside a
rounded rectangle at 20-25% of frame width along the bottom, **clear of every frame edge by at
least 8% (G10): if it will not fit, make it smaller, never move it outward.** Both faults have
rendered. **The only place the finished product appears.** Dropped by `--products`.

## MARKS

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `seam` | a thin glowing line along the diagonal, with a burst of warm sparks where it crosses the centre | one accent hue, warm sparks | exactly 1 | 1 render |
| `vs` | a large metallic VS at the seam's centre, with a burst of warm sparks | metallic | exactly 1 | 1 render, clean · letters are the risk class |
| `verdict` | a filled solid disc with the glyph CUT OUT of it, one per half, same diameter | red disc left, green disc right — **never name the glyph's own colour** | exactly 2 | 5 renders · also in `01-pain-split`, `02-cause-anatomy`, `06-relief-hero` |

**Both markers are offered; `vs` is the risk class.** The post-composite note carried since 1.0
was inherited, never tested, and the VS rendered clean first time. Letters still fail elsewhere
— ghostbody returned arrows labelled `W` and `L` unasked — so `verdict` is the default at 5
renders and `vs` is chosen where the marketplace dialect wants it.

**Never name the glyph's colour.** Cut-out and white are two constructions; asking for both
returned black on one frame and white on another.

**ONE marker at the seam, never two.** One binary argument takes one marker: `vs` or `verdict`,
not both stacked. Source exemplars used a VS plus emoji; market habit, deliberately not
imported.

**Polarity is locked: the legacy half is on the LEFT.** All four source exemplars inverted it.

## SLOT CONSTRAINTS
- **The G5 exemption IS the message.** Photograph on the left means *what rots in the real
  world*; render on the right means *what was engineered*. This is the only type in the library
  where breaking the register lock carries the argument, which is why it is declared in
  frontmatter rather than argued per prompt.
- **The left component is generic and unbranded** — a claim about a category, never about a
  competitor. No brand mark, no recognisable design, no readable model number.
- **Never render a component the product does not contain.** The census risk of
  `03-spec-explode` in a comparison frame: the right half is a render and proves nothing on its
  own, so the honesty constraint is the only thing holding the claim up.
- **Wear is evidence; catastrophe is staging.** Never broken, shattered or surrounded by debris
  — a demolished legacy part reads as theatre and voids the comparison
  (`argument-faults.md` shares this shape with `04-proof-lockedframe`).
- **The prompt budget.** A clause earns its place only if a render has failed without it. Since
  ADR-014 no `Strictly avoid:` line is rendered at all.

## NEGATIVE
```
[G6] + brand marks, recognizable trademarks, readable model numbers,
both halves rendered, both halves photographic, symmetrical composition,
vertical split, dull center, low contrast, product inset missing,
product inset cropped, cartoonish explosion, fire, smoke, gore,
human hands, human figures
```
Canonical and model-agnostic. Since ADR-014 it is **not rendered into the prompt at all**; it
stays here and in the query output's `avoid` field for a future model with a real negative
channel.

## VARIANTS
Diffs only. Each variant names the PARTS and MARKS it changes.

### --products
Whole-product photographic comparison — category displacement rather than component
superiority: the legacy solution class against the reference product.
Diff vs base: `old` becomes the generic legacy-class PRODUCT, unbranded, aged but plausible ·
`new` becomes the reference product itself, photographic, brighter and cleaner (G4), no hero
lighting beyond that · **both halves are photographs, so the G5 exemption does not apply here**
· `inset` is dropped, the whole products already being in frame.
- **Measured evidence, optional:** matching instrument insets on BOTH halves — same instrument,
  same position, same scale. Instrument digits are diegetic text (G6 scope note) and must come
  from real measurements, composited in post, never model-drawn.
- Negative additions: `shattered or destroyed rival product, debris, exaggerated failure scene,
  check and X badges stacked with the VS, mismatched instrument insets between panels`

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Credibility risks, accepted with open eyes: this aesthetic reads to buyers as a cheap-goods
signal — it lifts conversion on price-driven marketplaces and depresses it upmarket, which is
why the type is `marketplace` only. Both halves are soft claims; the honesty constraint in SLOT
CONSTRAINTS is the guardrail.

## CHANGELOG
- 1.4 (2026-09-15): copied verbatim from `registry/types/03-spec-split.md` at 1.4, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.
