---
id: 04-proof-lockedframe
step: 4
job: proof
device: lockedframe
version: "1.17"
status: active
replaced_by: null
channels: [advertorial, landing-page, marketplace, paid-social]
requires_product_photo: true
generation_mode: single-pass
axes:
  camera_lock: [strict, handheld]
  context_mode: [natural-use, declared-test]
variants: [rivals, verdict, timelapse, capture]
exempt_from: [G3, G4, G11]
pairs_with: [02-cause-anatomy, 06-relief-hero, 01-pain-scene]
never_with: []
text_layer: [title, copy]
copied_from: 04-proof-lockedframe
copied_at_version: "1.16"
blocked_by: null
---

# 04-proof-lockedframe

## PURPOSE
Physical proof the skeptic inspects for themselves: multiple panels, everything held
constant, exactly one variable changes. No badges, no glow, no winner declared — it
does not ask for belief, it invites a look.

**Copied verbatim from `registry/types/04-proof-lockedframe.md` at version 1.16** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## LP2 LAW
Added 2026-09-16 (ADR-094): the owner's gallery instruction for Feature + Benefit · Comparative / Proof. This section is
this copy's own and a re-copy keeps it; `registry/pdp-dr-instruction.md` binds the rest.

- **The words.** A spec-led title of 2–5 words. **Panel headers once, above the panels, never
  repeated below**, and they count as copy. Any other copy only as a figure the page supplies with
  its source (A15). The register's "no text" gives way to these on an LP2 page and to nothing else.
- **No icon and no pictogram.** A stopwatch drawn beside one panel came back labelled.
- **Never an invented test, a cycle count, or "tested" or "approved".** One render set a steel
  press on the product under an invented "10,000+ Cycles".
- **A certification the page supplies may be stated in words, with its source; the certification
  MARK may not** — that is the trademark question of 2026-08-18.
- **The generic rival stays plain and unbranded, never broken or mocked** — the fairness rule
  already says so.
- Each of the owner's three comparison renders broke a clause here: headers repeated beneath the
  panels or again as a chip, a copy line printed twice, arrows between the panels, an invented test.

Slots an LP2 prompt adds to the SKELETON above:
```
[TITLE]    spec-led, 2–5 words.                     -> LP2 LAW
[HEADERS]  one per panel, above it, once.           -> LP2 LAW
```

## TRIGGER
use_when: >
  The buyer already understands the problem and mechanism, is now skeptical and
  wants to see for themselves. The "I tried three things" beat of an
  advertorial, or a comparison image in the gallery. Use ONLY when the
  difference is visible to the naked eye inside a static frame — otherwise
  switch variants (see VARIANT SELECTION RULE).

## SKELETON
A call-map. Each arrow names an entry in PARTS; the definition lives there once.
**This type has no MARKS section, and that is the type.** Every other type in the library
argues with something added to the frame; this one argues by adding nothing, so the absence is
not an omission to fill in later.

```
TYPE: 04-proof-lockedframe v1.13 [--rivals | --verdict | --timelapse | --capture]
REGISTER: documentary photography. No overlays, badges, arrows or text.

[LAYOUT] N EQUAL panels, packed to the frame. G15.          -> PARTS/layout
[PRODUCT REFERENCE] attached photo is the exact reference.
[CAMERA] strict or handheld.                                            -> PARTS/camera
[SCENE] constant across every panel.                                    -> PARTS/scene
[VARIABLE] the only thing that changes, named per panel.                -> PARTS/variable
[PRODUCT] the subject of its panel, never the hero.                     -> PARTS/product
[GRADE] one grade across every panel.                                   -> PARTS/grade

[JUDGEMENT] no panel favoured.                                          -> SLOT CONSTRAINTS
STYLE: honest documentary product test photography, unstyled, natural, sharp.
```

## PARTS

**`layout`** — [N] EQUAL panels, thin white gutters, no outer border, striped across the
frame's LONG axis so they pack it rather than slivering: vertical panels on a wide ratio,
which is the case every render of this type has run so far. **At 1:1 the orientation turns
over** — two panels are halves either way, three are horizontal BANDS, four are a 2×2 grid
(G15). **Two is the preferred count at 1:1**: each half of a square carries four times the
area of a third band, and this type's argument is usually one variable across a before and an
after — take three only when the argument genuinely needs a third state.

It said "vertical" until 1.14 and that was written when the type only reasoned about
wide ratios; three vertical panels in a 1024 square are 341px each and nothing this type
photographs survives that.

**The 1 + 2 pack G15 offers other types is unavailable here**, and the reason is the type
itself: a larger frame favours its panel, and no panel may be favoured. Equal, always.

**`camera`** — two values, and the choice is evidence, not taste.

- `strict` — identical position, focal length, height and angle in every panel, with 3-4
  named anchor objects that align across all of them, and identical lighting, exposure and
  white balance.

  **The route is an INVARIANTS BLOCK, single-pass** (ADR-067). State the camera position,
  focal length, height, angle, the named anchor objects, and the lighting, exposure and white
  balance ONCE, BEFORE any panel is described — then describe the panels, and let the only
  difference between them be the variable. This is the mechanism `01-pain-split --mirror`
  measured: describing the invariant inside each panel returned two different subjects,
  naming it once before them returned one, 1 of 1 each way.

  **Until ADR-067 this value declared multi-pass and was therefore unreachable**, because
  ADR-021 removed compositing from the pipeline on 2026-08-14. It had been a value no route
  could select for twenty days while `eval/golden/fixture-002` went on asserting it. The
  invariants block is what makes it selectable again, and it is a claim with one supporting
  render in another type and one contradicting render in a third — see KNOWN-FLAKY.
- `handheld` — shot by one person on a phone on different days. **Describe ONE framing once**
  for every panel — where the subject sits, camera height and distance, what occupies the
  upper and lower thirds — then state the band: it reads as one shot taken [N] times, never
  as [N] different shots. Put the variation on the PROPS, named per panel: a towel refolded,
  an item moved, one thing missing. Light differs only in exposure, never in warmth.
  **Drift may not reveal area another panel does not have.** Opening up part of the room the
  others never show is a change of framing wearing drift's clothes.

**Choose by TIME, not by preference.** `strict` when every panel belongs to one session and
the variable is an object swapped in and out; `handheld` when the panels are separated by
time. A pixel-locked frame across "six months" is proof of staging, not of process — it
betrays its own argument.

**The CAPABILITY gate is retired** (ADR-067). It read "`strict` needs compositing, so where
the renderer cannot composite it is unavailable and the panels run `handheld`" — and since
ADR-021 that condition was permanently true, so the gate was a permanent refusal wearing a
conditional's clothes. `strict` now has a single-pass route and the choice above is by TIME
alone, which is what the type always meant it to be. What a `handheld` fallback costs is
unchanged and worth keeping in view: the alignment that makes a swap self-evident goes, so
the variable has to be the more visible for it.

**The wording law for `handheld`.** Never write the drift as a delta — "shifted 10-20cm" — and
never give each panel its own framing. The first renders one background with the object
swapped, the second renders unrelated photographs. One shared framing plus one small named
per-panel deviation is the only wording that lands in the band, and it is what makes a single
pass viable.

**`scene`** — [specific environment] and [the surface the variable sits on], the SAME in every
panel, with deliberate real-world clutter: [2-3 mundane untidy details]. Flat light, no strong
shadows, no sunlight, no styling. **Perfect alignment reads as CGI and destroys the evidence.**

**`variable`** — the only thing that changes, named panel by panel. Everything else — the
room, the surface, the light direction, the identity of the object — is constant.

**Name the object's INVARIANTS before the panels** — the same loaf, the same outline and
colour. Single-pass handheld does not hold identity on its own, and this is the clause
`01-pain-split` proved on a person.

**The difference must be visible on the object that CARRIES the argument.** Three wraps
differing around three identical sandwiches compares packaging, not outcomes. If the carrying
object will not show it, change the product or change the variable.

**The MOMENT is part of that one variable.** Every panel sits at the same point in the
process: all before, all during, or all after. A surface shown with the food still on it
against one shown after it is lifted compares two things, and the empty one wins for being
empty.

**`product`** — the SUBJECT of the panel it appears in, filling at least [X%] of that panel,
never a small object at the edge of a scene the viewer is actually looking at.

**The product can be the subject; it can never be the hero.** The judgement and fairness rules
forbid winning by treatment, so a brief that says "emphasise the product" belongs in a type
whose law lets it win — `01-pain-split` under G4, or `06-relief-hero` — rather than stretching
this one.

**`grade`** — ONE grade across every panel, coming from the room and the weather rather than
from a filter. **Still colour, never black and white**: a mono conversion on a documentary
register reads as edited and destroys the credibility it is selling.

- `--rivals`: muted and cool, low saturation, no warm tone anywhere. Every panel is an
  unsolved state, so one shared unresolved tone favours none of them. **This is the only
  variant whose grade carries polarity, and it carries it for the WHOLE image.**
- every other variant: neutral, no panel warmer, brighter or more saturated than another. If
  the resolved panel also looks better graded, the image has won by treatment and is void.

## SLOT CONSTRAINTS
- **The judgement rule is the type.** No panel may be favoured: no badge, no glow, no colour
  cue, no brighter exposure. The viewer decides. "Neutral" means no panel is argued for — not
  that the image carries no grade, which `grade` sets for all panels alike.
- **Variant selection.** If the difference between products does not appear inside a static
  frame, do not use `--rivals` or `--verdict`. Switch the variable from *which product* to
  *which state of the same object* — `--timelapse` or `--capture`. This binds every
  invisible-mechanism product: filters, supplements, skincare, software. Verified on a shower
  filter, where the object variants produced pretty and empty images.
- G7 applies at its strictest here, except `--capture`, which runs `context_mode:
  declared-test`.
- **The prompt budget, four parts.** A clause reaches a rendered prompt only if (1) a render
  has failed without it, (2) THAT product can fail that way — drift for handheld,
  identifiable-product for `--capture`, fairness for `--verdict` — (3) **the model can act on
  it inside one generation**, and (4) it is stated once. Part 3 was missing and it is the
  largest cut: "never opens up area another panel does not have" cannot be checked by a model
  drawing ONE frame, so it is a rule for the writer and lives here only. Ceiling **1800
  characters**; past it, re-read for a duplicated block. Since ADR-014 no `Strictly avoid:`
  line is rendered.

## NEGATIVE
```
[G6] + badges, arrows, glows, checkmarks, one panel brighter,
inconsistent lighting between panels, studio background, clean styled set,
staged perfection, saturated colors, red or green cues, motion blur,
people, hands, brand logos, recognizable trademarks
```
For `strict` add: `different camera angle between panels, shifted background elements`.
For `handheld` add: `identical framing between panels, pixel-perfect alignment,
tripod shot, 3D render look, CGI, product visualization,
identical water droplets between panels`.
Canonical and model-agnostic. Since ADR-014 it is **not rendered into the prompt at all**; it
stays here and in the query output's `avoid` field.

## VARIANTS
Diffs only. Each variant names the PARTS it changes.

### --rivals
Three common existing alternatives, unbranded; the product absent. The "I tried three things,
none worked" beat.
Diff: no `[PRODUCT REFERENCE]` and no `product` · `variable` becomes three generic alternatives
people already use, ordinary and plausible · `grade` takes its polarised value, muted and cool
for the whole image · none of them wins and the image makes no claim.
- Channels: advertorial and paid-social only — no product in frame is not marketplace-legal.
- **Uglifying the alternatives confesses staging.** They must look like things the viewer owns.
- Negative additions: `damaged or dirty items, exaggerated flaws, one item obviously better`

### --verdict
Two unbranded alternatives plus the reference product in the LAST panel.
Diff: `product` appears in the final panel ONLY · **order rule** — the product is always last,
because left-to-right reading ends on it and that is the resolution position · the **fairness
rule** replaces the judgement rule.
- **Fairness rule.** Panels 1 and 2 get exactly the same photographic respect as panel 3:
  identical exposure, identical background tidiness, identical framing generosity. The
  alternatives must look like reasonable products someone would genuinely buy, and the two
  chosen are the MOST COMMON ones buyers already own, never the worst. **The difference must
  be visible in the OBJECTS themselves, never in how they are lit, styled, cropped or graded.**
- It may win by physics, never by treatment — otherwise it collapses into a long
  `01-pain-split` and loses all evidentiary value.
- Negative additions: `last panel brighter or cleaner than the others, hero lighting on the
  final panel, alternatives made to look broken, cluttered first panels`

### --timelapse (`camera_lock: handheld`)
Same object across time; the variable is its condition.
Diff: `variable` becomes the condition of ONE component at different points of use — clean,
partial, saturated — and **the texture must stay readable as what it is**, granules staying
granular · the moment is an ordinary inspection, nothing cut open, propped or arranged.
- The strongest proof for invisible-mechanism products: the viewer already believes something
  is in the water or the air, and this shows it without touching any competitor.
- The image only shows. No day counts, no captured-substance claims.
- Negative additions: `cut-open product, cross-section, product standing upright unnaturally,
  staged arrangement, mold, slime, blood-like color, mud, texture losing its granular structure`

### --capture (`context_mode: declared-test`, 2 panels)
Output filtered against unfiltered through an intermediate medium.
Diff: `scene` becomes a declared at-home test staged the way an ordinary person would — cloth
tied with a rubber band, slightly crooked, a basin underneath — because **amateur staging reads
truer than neat staging** · `variable` is panel 1 without the product fitted and the medium
marked, panel 2 with it fitted and the medium clean — and **the product must be identifiable
in panel 2**, not merely present. A clean medium with no visible cause is a clean medium, and
the cause is the only thing this variant supplies.
- Channels: advertorial only. Weaker than `--timelapse`, since the viewer never sees the
  process; if both run, `--timelapse` goes first so it vouches for this one.
- Negative additions: `laboratory equipment, clinical setup, cloth in different position
  between panels, dramatic staining, black mold, cartoonish contrast`

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.17 (2026-09-16): `LP2 LAW` added: the owner's gallery instruction for this type — a spec-led title and headers once above the panels, a figure only with its source, no icon, no invented test, a certification in words and never as a mark. `text_layer` declared. First LP2 edit; `copied_at_version` stays 1.16. ADR-094.
- 1.16 (2026-09-15): copied verbatim from `registry/types/04-proof-lockedframe.md` at 1.16, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.
