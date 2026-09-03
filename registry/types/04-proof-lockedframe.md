---
id: 04-proof-lockedframe
step: 4
job: proof
device: lockedframe
version: "1.16"
status: active
replaced_by: null
ratios: ["16:9", "1:1"]
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
---

# 04-proof-lockedframe

## PURPOSE
Physical proof the skeptic inspects for themselves: multiple panels, everything held
constant, exactly one variable changes. No badges, no glow, no winner declared — it
does not ask for belief, it invites a look.

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

## WORKED EXAMPLES
Both rendered and owner-passed, kept in FULL text per SPEC §3.3. They replace a `run: fail`
example stored at skeleton@1.2 and a pass at 1.5, neither of which teaches the rules earned
since; git holds both. These two predate the 1.9 clauses on the moment and on drift, and are
kept because they are what actually rendered.

### example: bread-storage-rivals — skeleton@1.7, run: pass
```
TYPE: 04-proof-lockedframe v1.7 --rivals, camera handheld
REGISTER: documentary phone photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
Not applicable. No product appears in this image.

[SCENE — the same in all three]
The same corner of a domestic kitchen worktop, the same wooden board, a kettle and a
tea caddy pushed to the back, a faint crumb scatter on the wood. Flat overcast light
from a window off to the left, no strong shadows, no styling.

[FRAMING]
One person photographed this three times across a week from where they always stand,
phone held level with the worktop, the board filling the middle third and the tiled
splashback across the upper third. It reads as one shot taken three times, never as
three different shots. Light differs only in exposure, never in warmth.

[THE VARIABLE]
Three ways people already store a cut loaf, each photographed on day four, each holding
the same kind of white sourdough half-loaf.
1 — in its original plastic bag, the bag slack and beaded with condensation inside, the
cut face gone grey and damp.
2 — under an upturned bowl on the board, the cut face dried to a pale hard crust that has
cracked away at one corner.
3 — wrapped in a tea towel, the towel loose and fallen open, the crumb dry and crumbling
onto the board.

[WHAT ELSE MOVES]
1 — the tea caddy at the back right, lid on. 2 — the caddy turned, lid resting beside it.
3 — the caddy gone, a mug in its place.

[GRADE — the same in all three]
Muted and cool, low saturation, no warm tone anywhere. It comes from the overcast window
and the drab worktop rather than from a filter. Still colour, never black and white. All
three are unsolved states, so one shared unresolved tone favours none of them.

No panel is favoured. No badge, no glow, no colour cue, no brighter exposure. None of the
three wins and the image makes no claim.

STYLE: honest documentary phone photography, unstyled, natural, sharp.
```
The best render this type has produced. The handheld band landed exactly: the board edge and
the kettle shift a little between panels, so it reads as one person's phone across a week.

### example: machine-filter-timelapse — skeleton@1.7, run: pass
```
TYPE: 04-proof-lockedframe v1.7 --timelapse, camera handheld
REGISTER: documentary phone photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the filter unit held in every
panel. Preserve its shape, proportions, material, finish and colour exactly as shown.

[SCENE — the same in all three]
The same utility-room floor in front of an open washing-machine door, the same tiled
floor, a folded towel down to catch drips and a shallow bowl beside it. Flat ceiling
light, no strong shadows, no styling.

[FRAMING]
One person photographed this three times across several months, crouched where they
always crouch, phone held low and close with the machine door filling the upper third
and the tiled floor across the lower third. It reads as one shot taken three times, never
as three different shots. Light differs only in exposure, never in warmth.

[THE VARIABLE]
The condition of the SAME filter unit at three points of use, held in the same hand
position each time, lifted out for an ordinary look — nothing cut open, propped up or
arranged for the camera.
1 — new: the mesh clean and open, the metal bright.
2 — partway: a thin chalky bloom across the mesh, still open, the individual strands of
mesh still separate and readable.
3 — saturated: the mesh crusted with hard white scale, thick enough to bridge between
strands, but the crystalline texture still reading clearly as mineral crust rather than
as mud or slime.

[WHAT ELSE MOVES]
1 — the towel folded square. 2 — the towel rucked at one corner. 3 — the bowl moved
closer, a damp mark on the tile.

[GRADE — the same in all three]
Neutral, coming from the ceiling light and the tiled room rather than a filter. Still
colour, never black and white. No panel warmer, brighter or more saturated than another.

No panel is favoured. No badge, no glow, no colour cue, no brighter exposure. The image
only shows the condition; it makes no count and no claim.

STYLE: honest documentary phone photography, unstyled, natural, sharp.
```
The variant's named risk cleared — the scale crust bridges the mesh strands and still reads as
mineral rather than as mud or mould.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.16 (2026-09-03): `generation_mode` **multi-pass → single-pass** — the last declaration in
  the registry — and `strict` takes the invariants-block route in place of generate/edit/
  composite (ADR-067, owner instruction). The CAPABILITY gate is retired: it made `strict`
  unreachable for twenty days after ADR-021 while `eval/golden/fixture-002` asserted it.
  `ratios` corrected to ADR-016's legal set, `5:3` and `3:2` dropped.
- 1.15 (2026-08-27): **two panels become the preferred count at 1:1.** Owner correction to G15:
  no type is exempt at 1:1, and this type's equal-frames constraint is a narrower form of the
  rule rather than an exemption from it. A half of a square carries four times the area of a
  third band, so a square frame is where the panel count should drop. ADR-063. · this commit
- 1.14 (2026-08-27): **`layout` stops hard-coding VERTICAL.** Panels stripe across the long
  axis so they pack the frame, which at 1:1 makes three panels horizontal bands and four a
  2×2. G15 is the new rule; this type is exempt from its 1 + 2 form because a larger frame
  favours its panel and the judgement rule is the type. The two worked examples keep
  "vertical" — they are records of renders at wide ratios where it was correct. · this commit
- 1.13 (2026-08-13): **type PASSED by the owner; file finalised.** WORKED EXAMPLES keeps the
  two 1.7 passes — the later frames that would replace them are `partial` after the G7
  corrections, and an example is a record of what rendered. Standing note: `--rivals` is legal
  and channel-scoped but carries no product, so it is not sent for render; the owner cannot
  judge an image with no product in it.
- 1.12 (2026-08-13): **the prompt budget gains a fourth part** — a clause reaches a rendered
  prompt only if the model can ACT on it inside one generation. "Never opens up area another
  panel does not have" cannot be checked by a model drawing one frame, so it is a writer's rule
  and lives here only. `STYLE` restating `REGISTER` and a separate `WHAT ELSE MOVES` block go
  with it. Ceiling 2100 → 1800. This entry was missing from the 1.12 commit. · 474e77b
- 1.11 (2026-08-13): **four fixes.** `PARTS/variable` gains an INVARIANTS clause and the rule
  that the difference must show on the object CARRYING the argument. The prompt budget gains
  its two missing parts: a clause enters a prompt only if that product can fail that way, and
  each law is stated once. · b4928de
- 1.10 (2026-08-13): **compression pass; no rule removed.** Case history behind the 1.7-1.9
  rules moved to the commits that made them, and WORKED EXAMPLES rebuilt on two current passes,
  replacing a `run: fail` example stored at skeleton@1.2 and a pass at 1.5.
- 1.9 (2026-08-13): the MOMENT is part of the one variable — every panel at the same point in
  the process. `--capture` panel 2 must show the product IDENTIFIABLY. Handheld drift may not
  reveal area another panel does not have. · f762ca9
- 1.8 (2026-08-13): a panel-1 prompt carries no multi-panel language, and the anchor list moves
  to the EDIT step which enforces alignment by construction. The camera choice gains a
  CAPABILITY gate: `strict` needs compositing, so where the renderer cannot composite,
  `--verdict` runs `handheld`. · c15107c
- 1.7 (2026-08-13): **restructured into a call-map plus PARTS** (ADR-012). **No MARKS section,
  and that is the type** — every other type argues with something added to the frame; this one
  argues by adding nothing, so the absence is law rather than an omission. `RATIO:` dropped per
  adapter Rule 4. · 1da1da2
- 1.6 (2026-08-12): `exempt_from` gains **G11**. The type's `grade` slot legislates saturation
  differently and on purpose — one grade for the WHOLE image, polarity never between panels —
  which is the opposite of what G11 requires of a two-state frame. · see git
- 1.5 (2026-08-12): **the wording law for `handheld`**, and `[PRODUCT PROMINENCE]`. Relative
  drift deltas produced one repeated background; independent per-panel framings produced
  unrelated photographs; one shared framing plus a small named per-panel deviation is the only
  wording that lands. Separately, this was the only product-bearing type with no size or
  placement rule, so the product drifted to the frame edge. · 8949f33
- 1.4 (2026-08-11): channels gain `paid-social`. Self-contradiction: the --rivals
  variant already declares "Channels: advertorial, paid-social only" while the
  frontmatter excluded paid-social. The type-level avoid_when ("never as a
  scroll-stopper") still gates the slow variants there — that is a Stage 2 judgment,
  not a channel ban.
- 1.3 (2026-08-10): camera_lock axis (strict/handheld) with time-gap selection rule;
  granularity constraint on saturated media. Evidence: rendered strict-timelapse output
  read as CGI (user test, seed conversation.md).
- 1.2 (2026-08-10): --timelapse and --capture variants + VARIANT SELECTION RULE.
  Evidence: rendered --rivals/--verdict on shower filter judged "pretty but empty"
  (user test — object variants carry no proof for invisible mechanisms).
- 1.1 (2026-08-10): split into --rivals / --verdict with order and fairness rules.
  seed: conversation.md.
- 1.0 (2026-08-10): initial from the three-car-seat-cushions exemplar. seed: conversation.md.
