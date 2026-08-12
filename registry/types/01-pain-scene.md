---
id: 01-pain-scene
step: 1
job: pain
device: scene
version: "1.4"
status: active
replaced_by: null
ratios: ["16:9", "5:3", "4:5"]
channels: [paid-social, advertorial, landing-page]
requires_product_photo: false
generation_mode: single-pass
axes:
  gaze: [candid, confront]
variants: [candid, confront, marked]
exempt_from: [G1, G3, G4]
pairs_with: [06-relief-hero, 06-relief-scene, 04-proof-lockedframe]
never_with: [01-pain-split]
---

# 01-pain-scene

## PURPOSE
Make a cold viewer recognize themselves in a raw, cinematic pain moment — before they
know any product exists. Acting and physical evidence carry the pain. No product, no
layout, no verdict; `--marked` may add ONE mark that points at the evidence.

## TRIGGER
use_when: >
  Cold traffic that does not know the product yet. Advertorial header image,
  Facebook/native ad creative, opening image of a story. Its only job is to make
  the viewer recognize themselves and keep reading. Use --candid for physical
  pain and moments nobody would choose to be seen in; use --confront for
  appearance, self-image and daily-frustration problems where the mirror moment
  IS the moment.
avoid_when: >
  Marketplace galleries, main image, or any position where the product must be
  visible. Cannot sell alone — must be paired with a relief/proof image. Never
  in the same set as 01-pain-split: one pain beat per page, and two of them
  compete for the same job rather than building on each other.

## SKELETON
```
TYPE: 01-pain-scene v1.4 [--candid | --confront] [+ --marked]
REGISTER: cinematic film still. Single frame.

[SUBJECT]
[age/gender] in [ordinary specific wardrobe, lived-in not styled], mid-way
through [an ordinary daily action]: [the force being applied or the movement in
progress]. Never a pause, never a demonstration.
Under that force: [which limb, which brace, where the weight goes].
Face: [the involuntary signs, named by muscle].

[SYMPTOM EVIDENCE — required, G9]
The symptom as physical fact: [strongest evidence present — ladder in SLOT
CONSTRAINTS]. [if it is a failed tool: the state that shows it failed].

[ENVIRONMENT]
[specific ordinary place, tied to where the problem gets noticed], [time of day].
Lived-in clutter belonging to that place, signalling the routine it disrupts:
[3-4 mundane objects]. Nothing arranged, nothing removed to tidy the frame.

[GAZE] — filled by --candid or --confront.
[LIGHT] — filled by --candid or --confront.
[MIRROR] — optional, --confront only.
[PAIN MARK] — required by --marked, absent otherwise.

[GRADE]
Desaturated [dominant hue], fine film grain, shallow depth of field,
[lens character].

[FORBIDDEN]
No product. No insets, no split panels. No mark unless --marked is in use.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
```

## SLOT CONSTRAINTS
- [SYMPTOM EVIDENCE] is mandatory (G9). Expression alone carries nothing. **The ladder —
  pick the strongest present, then write only that one into the slot** (it moved out of
  the skeleton at v1.4 because ranking is the writer's job and the model only needs the
  choice):
  1. the symptom itself on the body or object;
  2. physical residue or debris it produces — what it leaves behind, and where;
  3. the failed tool, in the state that shows it failed;
  4. gesture alone — weakest, only when 1-3 are impossible, and then at least one object
     in frame must imply the problem independently.
- **The moment must be mundane** — something anyone lives daily, never a demonstration of
  wrong behaviour. Also moved out of the skeleton at v1.4: it steers the writer's choice
  of action and has no picture of its own, which is why "an ordinary lunch stopped by a
  jar" rendered as nothing at all.
- **No red pixel anywhere, on `--candid` and `--confront`** — those variants replace the
  red pain signal with acting, and a red glow there makes the image confess it is an ad.
  `--marked` is the sanctioned exception and narrows the rule to "red appears only in the
  mark": natural skin, food and household colour were never the target of this ban, and
  writing around them cost a render (see CHANGELOG 1.3).
- **State the force, never the meaning** (v1.3). The subject slot must name a force being
  applied or a movement in progress, not a pause and not an intention. "Both hands
  stopped over the jar" and "an ordinary lunch interrupted" both rendered as nothing;
  "both hands locked on the lid, turning against it, the lid has not moved" rendered
  correctly. The same applies to [SYMPTOM EVIDENCE] rank 3: a failed tool must be
  described in the state that shows it failed — "the jar key lying where it slipped off,
  its jaws still spread" — because "already tried" is a meaning and has no picture.
- [ENVIRONMENT] specificity is the only defense against the "stock photo of back pain"
  failure mode. Generic = dead.

## NEGATIVE
```
[G6] + red glow, pain hotspots, graphic overlay, arrows, badges, split panel,
white background, studio lighting, stock photo look, posed model, fake grimace,
smiling, clean staged interior, saturated colors, advertising composition,
product placement
```
**Under `--marked`, three tokens DROP from this list: `red glow`, `pain hotspots`,
`graphic overlay`.** That variant requires a red glow or ring, so carrying those tokens
into a rendered avoid line is a Rule 1a bleed — the avoid line has no negative channel
and no operators, so "red glow" beside a required red glow suppresses the mark. Drop,
never rephrase. `arrows` and `badges` stay in every variant: the mark law bars them.

## VARIANTS
### --candid (default)
Problem class: physical pain, physical limitation. Channels: paid-social, advertorial
header. Reads cinematic, survives being scrolled past.
Fills the two variant slots:
```
[GAZE] unaware of the camera, gaze on the task or the ground.
[LIGHT] low-key. Key: [source, direction, colour temperature]. Fill: [weaker
source]. Rim light separating subject from background. Deep shadow across [X%] of
the frame.
[GRADE addition] crushed blacks.
```
- Negative additions: `bright airy lighting, flat daylight look, looking at camera`

### --confront
Problem class: appearance, self-image, daily frustration. Channels: advertorial body,
landing-page. Legible at thumbnail size.
Fills the variant slots:
```
[GAZE] looking directly into the lens, holding the viewer's eye. A half-turned
glance reads as a model waiting for direction.
[LIGHT] even ambient daylight, bright, minimal shadow, flat and unflattering.
[MIRROR, optional] a mirror behind or beside the subject showing them from another
angle, the reflection consistent with their actual position.
```
- The [MIRROR] slot earns its space twice: it gives the confrontation a natural reason,
  and it doubles the symptom evidence without adding a second person. Render-confirmed
  2026-08-12 on a thinning-hair frame — the mirror carried the crown the subject cannot
  see himself.
- Restraint rule: frustration, not drama — the flatter the face, the truer it reads.
  **Scope of that rule (v1.3):** it governs EMOTION, not effort. A flat face over a slack
  body renders as nothing at all. When the moment is physical exertion, the face still
  carries the involuntary signs — jaw set, breath held, lips dragged at one corner — and
  those are not drama.
- Negative additions: `golden hour, warm flattering light, exaggerated grimace, theatrical anger`

### --marked
The only variant that carries a graphic layer. One mark, placed on the evidence, never a
verdict. Composes WITH the gaze variants rather than replacing them — name both in the
prompt (`--confront --marked`), because gaze and mark are independent decisions.
Diff vs base:
```
[FORBIDDEN, replaces the base block]
No product. No insets, no split panels, no badges of any kind.
Exactly ONE graphic mark is permitted, defined in [PAIN MARK]. Nothing else in
the frame is marked.

[PAIN MARK — required slot when this variant is used]
ONE mark class only, chosen from: a soft red radial glow, or a thin red ring.
It sits ON the physical evidence [SYMPTOM EVIDENCE] already names, sized to that
evidence and no larger, fading out before it touches anything else.
Close the count in the slot itself: "the only mark in this image".

[MARK LAW]
The mark POINTS AT evidence. It never delivers a verdict. No X, no check, no VS,
no thumbs, no exclamation glyph — that is 01-pain-split's language, and a glyph is
text, which G6 routes out of the render and into post.
If [SYMPTOM EVIDENCE] has nothing physical to point at, this variant is ILLEGAL:
use the base variant. A mark over an empty frame invents the pain instead of
marking it.

[GRADE adjustment]
The desaturated grade stays exactly as the base sets it — G11's whole-frame
unresolved tone. The mark is an accent on top of it, not a replacement for it.
Red appears ONLY in the mark.
```
- G3 note: the base type is `exempt_from: [G3]` because it uses no signal colour at all.
  This variant uses one, so its mark obeys G3 — red = pain — even though the exemption
  stands for the rest of the frame.
- The mark is model-drawn (ADR-008 approach A) and owns a named slot with a count,
  because a mark buried in prose is the one that vanishes (adapter Rule 7).
- Deliberately NOT in the negative list: any phrasing like `second mark`. That qualifies
  a noun this variant requires, which is Rule 1a's exact bleed shape and the same
  structure as the rule's own worked example `a second badge`. The bound lives in the
  slot's own "only mark in this image" instead.
- Negative additions: `badge, checkmark, VS, thumbs, exclamation glyph, arrow, text label`

## WORKED EXAMPLES
### example: mouth-tape-candid — skeleton@1.1, run: untested
Product: none in frame (G1-exempt) · ratio 5:3 · variant --candid
- SUBJECT — man late 30s, worn grey t-shirt, sitting up on the edge of an unmade bed mid-night, shoulders slumped, one hand braced on the mattress, the other reaching for the nightstand; unaware of camera, gaze down and unfocused; eyes heavy and half open, deep creases beneath, lips dry and parted, jaw slack
- SYMPTOM EVIDENCE — an almost empty glass of water with a second empty glass beside it, pillow deeply creased and shoved aside, duvet kicked into a tangle at the foot, phone face-up casting a cold glow
- MOMENT — the ordinary act of waking again at 3am, not a demonstration of wrong behaviour
- ENVIRONMENT — small suburban bedroom, deep night, curtains half drawn, a chair with clothes over the back
- LIGHT — low-key; key: cold blue streetlight through the curtain gap from behind left; fill: faint warm hallway spill; rim along shoulder and jaw; deep shadow across most of the frame
- GRADE — desaturated blue-grey, crushed blacks, fine grain, shallow depth of field, 35mm
Predicted failure: the two glasses may collapse into one, losing the "repeats every
night" layer. Fallback evidence: a water-ring stain on the nightstand (carries
repetition in a single object).

### example: knife-sharpener-confront — skeleton@1.1, run: untested
Product: none in frame (G1-exempt) · ratio 5:3 · variant --confront
- SUBJECT — woman early 40s, plain t-shirt and apron, standing at a kitchen counter turned to camera holding the lens; knife loose in one hand, the other raised in a small giving-up gesture; brow drawn together, mouth pressed flat and slightly down, chin tucked
- SYMPTOM EVIDENCE — a tomato mangled into thick uneven wedges, skin torn, juice and seeds across the wood; a second half-crushed tomato pushed aside; a cheap pull-through sharpener already tried and abandoned; a dish towel bunched under her wrist
- MOMENT — stopping mid-task because the tool will not do its job, not a demonstration of wrong technique
- ENVIRONMENT — small ordinary kitchen, mid-morning, worn wooden counter, an open utensil drawer behind, a board against the tiles, dishes in the sink
- LIGHT — even ambient daylight from a window left, bright, minimal shadow, flat and unflattering
- GRADE — desaturated neutral, muted greens and greys, fine grain, moderate depth of field, 35mm; the tomato is the only red and must read as ordinary food color
Predicted failures: (1) knife-in-hand + direct gaze may trip safety filters or read as
threatening — fallback: knife down on the board, both hands braced on the counter;
(2) frustration drifting into theatrical anger — the variant lives on restraint.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.4 (2026-08-12): **skeleton compressed, no change to what renders.** Same slots, same
  laws, same image — only where the text lives moved, so this is MINOR: no layer, zone or
  panel changed. The skeleton block drops from 2144 to 1314 characters, 38% smaller, and
  every prompt written from it inherits that.
  Six cuts, each with its reason. (1) The `RATIO:` line is gone — adapter Rule 4 has 6/6
  renders ignoring a written ratio, and keeping it in the skeleton taught every filler to
  write a line the adapter then had to strip. (2) `[MOMENT RULE]` and (3) the four-rank
  evidence ladder moved to SLOT CONSTRAINTS: both are instruments for choosing, and the
  model only needs the choice. Today's evidence for (2) is direct — "an ordinary lunch
  stopped by a jar" was a MOMENT fill and rendered as nothing. (4) `[GAZE]` and `[LIGHT]`
  carried BOTH variants inline, so every writer hauled the unused branch and deleted it;
  the filler text now lives in the `--candid` and `--confront` blocks where it is chosen,
  and `[MIRROR]`'s rationale went to the variant bullet while its filler text went to the
  block. (5) `NO saturated colors` / `NO red anywhere` / `Nothing that signals
  advertising` / `NO text, no logo, no watermark` are gone: the positive form is already
  asserted ("desaturated"), and the rest is G6, which the adapter emits into the avoid
  line — Rule 1 step 1 and Rule 6 rule 2.
  One quality fix, not a cut: `[SUBJECT]` no longer offers "**or pausing at** the moment
  the problem is noticed". That branch is what produced the dead render this morning, and
  it contradicted the state-the-force rule added at 1.3 in the same file. The slot now
  names a force or a movement and says so twice.
  `[PAIN MARK]` is named in the base skeleton as variant-set, so `--marked` is visible to
  anyone reading the skeleton alone.
- 1.3 (2026-08-12): **`--marked` variant added** — one graphic mark, on the evidence,
  never a verdict. Owner decision; the standing instruction is that graphic-element rules
  are the owner's to write, and this is that decision. `vocabulary.yaml` drops "zero
  graphic layers" from the `scene` device in the same change: the device's identity is its
  geometry (one frame, no panels, no insets), and the graphics ban was never carried by
  the device in practice — both `scene` types already state it in their own files
  (`[FORBIDDEN]` here, REGISTER line + NEGATIVE in `06-relief-scene`), so nothing lost a
  law. `--candid` and `--confront` keep the full ban.
  Evidence, three strands. (1) **Measured cost of acting-only emphasis**: the same jar
  prompt went from 1379 characters to 2153 (+774) purely to force visible exertion out of
  prose — elbow, shoulder, neck tendon, held breath — which is a mark's job written the
  long way. The `--marked` rewrite of the same image lands at 1544. (2) **Owner report on
  four renders of this type in one session**: all technically sound, none legible at a
  glance, and a buyer has to study the frame to find the problem. `1.3b` is on the ledger
  as `pass` (`eval/render-tests.jsonl`, 2026-08-12) with the two logic faults recorded as
  prompt faults, not skeleton faults. (3) **A structural gap in routing**: on paid-social
  and advertorial this is the ONLY pain type — `01-pain-split`, the half-second one with
  hotspots and badges, is marketplace/landing-page and requires a product photo. So those
  two channels had no fast-reading pain option at all.
  Also in this change: the SLOT CONSTRAINTS gain the **state-the-force rule** (a slot must
  name a force or a movement, never a pause or an intention — "already tried" and "an
  ordinary lunch" both rendered as nothing), and `--confront`'s restraint rule is scoped
  to emotion rather than effort, because a flat face over a slack body renders as nothing.
  `never_with: 01-pain-split` stands, with its reason updated: it was "graphics versus
  acting", and it is now simply one pain beat per page.
- 1.2 (2026-08-11): channels gain `landing-page`. The type contradicted ITSELF: the
  --confront variant already declares "Channels: advertorial body, landing-page"
  while the frontmatter excluded it. Frontmatter corrected to match the variant.
  Found by the new slot-rules/frontmatter drift check in scripts/validate.py.
- 1.1 (2026-08-10): SYMPTOM EVIDENCE made required (→G9); GAZE and LIGHT split into
  per-variant conditionals; [MIRROR] slot added; environment clutter law tightened.
  Evidence: seed conversation.md (bathroom-mirror confront exemplar confirmed the
  Test F prediction that gesture alone cannot carry an invisible symptom).
- 1.0 (2026-08-10): initial from the garage car-exit exemplar. seed: conversation.md.
