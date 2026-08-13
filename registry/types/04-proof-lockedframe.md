---
id: 04-proof-lockedframe
step: 4
job: proof
device: lockedframe
version: "1.7"
status: active
replaced_by: null
ratios: ["5:3", "16:9", "1:1", "3:2"]
channels: [advertorial, landing-page, marketplace, paid-social]
requires_product_photo: true
generation_mode: multi-pass
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
avoid_when: >
  The difference is invisible or only felt in use (then the object variants
  produce pretty-but-empty images — verified failure). Never as a
  scroll-stopper; this type is slow and needs an already-attentive viewer.
  --rivals never on marketplace (no product in frame violates gallery rules).

## SKELETON
A call-map. Each arrow names an entry in PARTS; the definition lives there once.
**This type has no MARKS section, and that is the type.** Every other type in the library
argues with something added to the frame; this one argues by adding nothing, so the absence is
not an omission to fill in later.

```
TYPE: 04-proof-lockedframe v1.7 [--rivals | --verdict | --timelapse | --capture]
REGISTER: documentary photography. No overlays, badges, arrows or text.

[LAYOUT] N equal vertical panels, thin white gutters, no outer border.  -> PARTS/layout
[PRODUCT REFERENCE] attached photo is the exact reference.
[CAMERA] strict or handheld.                                            -> PARTS/camera
[SCENE] constant across every panel.                                    -> PARTS/scene
[VARIABLE] the only thing that changes, named per panel.                -> PARTS/variable
[PRODUCT] the subject of its panel, never the hero.                     -> PARTS/product
[GRADE] one grade across every panel.                                   -> PARTS/grade

No panel is favoured. No badge, glow, colour cue or brighter exposure.
STYLE: honest documentary product test photography, unstyled, natural, sharp.
```

## PARTS

**`layout`** — [N] equal vertical panels, thin white gutters, no outer border.

**`camera`** — two values, and the choice is evidence, not taste.

- `strict` — identical position, focal length, height and angle in every panel, with 3-4
  named anchor objects that align across all of them, and identical lighting, exposure and
  white balance. **Multi-pass is mandatory**: generate one panel, edit-swap the variable,
  composite.
- `handheld` — shot by one person on a phone on different days. **Describe ONE framing once**
  for every panel — where the subject sits, camera height and distance, what occupies the
  upper and lower thirds — then state the band: it reads as one shot taken [N] times, never
  as [N] different shots. Put the variation on the PROPS, named per panel: a towel refolded,
  an item moved, one thing missing. Light differs only in exposure, never in warmth.

**Choose by TIME, not by preference.** `strict` when every panel belongs to one session and
the variable is an object swapped in and out; `handheld` when the panels are separated by
time. A pixel-locked frame across "six months" is proof of staging, not of process — it
betrays its own argument.

**The wording law for `handheld`.** Never write the drift as a delta — "shifted 10-20cm", "a
few centimetres from where it sat". A relative instruction needs a reference point the model
does not have inside one canvas, so it renders one background and swaps the object. But giving
each panel its own independent framing overshoots into unrelated photographs. **One shared
framing plus one small named per-panel deviation** is the only wording that lands in the band,
and it is what makes a single pass viable at all.

**`scene`** — [specific environment] and [the surface the variable sits on], the SAME in every
panel, with deliberate real-world clutter: [2-3 mundane untidy details]. Flat light, no strong
shadows, no sunlight, no styling. **Perfect alignment reads as CGI and destroys the evidence.**

**`variable`** — the only thing that changes, named panel by panel. Everything else — the
room, the surface, the light direction, the identity of the object — is constant.

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
- **The prompt budget.** A clause earns its place only if a render has failed without it.
  Since ADR-014 no `Strictly avoid:` line is rendered at all.

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
marked, panel 2 with it fitted and the medium clean.
- Channels: advertorial only. Weaker than `--timelapse`, since the viewer never sees the
  process; if both run, `--timelapse` goes first so it vouches for this one.
- Negative additions: `laboratory equipment, clinical setup, cloth in different position
  between panels, dramatic staining, black mold, cartoonish contrast`

## WORKED EXAMPLES
### example: herb-storage-rivals-handheld — skeleton@1.5, run: pass
Product: none in frame · ratio param 5:3 · 3 panels · variant --rivals · axes: camera_lock=handheld, context_mode=natural-use · advertorial · single-pass
```
TYPE: 04-proof-lockedframe v1.5 --rivals, camera_lock handheld
REGISTER: documentary phone photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

PRODUCT REFERENCE: not applicable. No product appears in this image.

SCENE, the same in all three: one glass shelf of a domestic fridge, a jar of
jam and a butter dish pushed to the back, a faint dried spill mark on the glass.
Cold even fridge light from above, no styling.

GRADE, the same in all three: muted and cool, low saturation, no warm tone
anywhere. It comes from the fridge light and the drab shelf rather than a
filter. Still colour, never black and white. All three panels are unsolved
states, so one shared unresolved tone across them favours none of them.

FRAMING: one person photographed this three times across a fortnight from where
they always stand, phone held level with the shelf, the shelf edge running
across the lower third. It reads as one shot taken three times, never as three
different shots — drift is a few degrees of tilt and a few centimetres of
position, no more. Light differs only in exposure, never in warmth.

THE VARIABLE: three storage methods people already use, each photographed after
a fortnight, each holding the same bunch of basil.
1 — standing in a tumbler of cloudy water, stems slimy below the waterline,
leaves drooping and blackened at the edges.
2 — unwrapped from a limp damp kitchen towel lying open beside it, the leaves
bruised and darkened where they were pressed.
3 — lifted from a plastic bag, condensation beaded inside it, the leaves
collapsed and translucent.

WHAT ELSE MOVES: 1 — jam jar at the back left, label facing out. 2 — jar turned,
butter dish pulled forward. 3 — jar moved to the right, a new ring of spill on
the glass.

FAIRNESS: three ordinary methods anyone would try, none exaggerated, none
favoured. Every panel ends the same way. The image makes no claim.

Strictly avoid: sparkle glyphs, brand logos, human figures, hands, studio
lighting, staged perfection, identical framing between panels, mould, fur,
liquefied sludge, CGI.
```
Rendered 2026-08-12, owner verdict pass (`eval/render-tests.jsonl`). Kept at full text
because that is the only record of what actually rendered (SPEC §3.3). This is the
variant whose predecessor FAILED and produced v1.5, so its pass is the type's proof
that all three fixes work: the band held on one shared framing plus small named
per-panel prop deviations, and one shared muted grade read as three unsolved states
rather than a neutral lineup.

Replaces an `untested` `--timelapse` example at skeleton@1.3. Nothing evidentiary was
lost — that example carried no verdict, and its evidence chain (a strict-camera
predecessor rendered and read as CGI, panel 3 drifting into mud) is recorded in the
v1.3 CHANGELOG entry below. `--timelapse` now has a real ledger line of its own from
the same session (car cabin air filter, pass), including the granularity constraint
holding.

### example: shower-filter-verdict — skeleton@1.2, run: fail
Full prompt in seed conversation.md (three filters on one shower arm, locked camera).
The lock held perfectly — and the image argued nothing: three filters merely LOOK
different; better-looking is not better-filtering, and buyers know it. Kept as the
boundary case that produced the VARIANT SELECTION RULE. Secondary fault: panel 3
mounted the filter with no shower head behind it — half-installed device, the G7
completeness violation that helped produce G7.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.7 (2026-08-13): **restructured into a call-map plus PARTS** (ADR-012), owner instruction.
  `PARTS` owns `layout`, `camera`, `scene`, `variable`, `product`, `grade`. **There is no MARKS
  section and that is the type** — every other type argues with something added to the frame
  and this one argues by adding nothing, so the absence is recorded as law rather than left to
  look like an omission. `RATIO:` dropped per adapter Rule 4. ADR-014 adopted.
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
