---
id: 01-pain-scene
step: 1
job: pain
device: scene
version: "1.6"
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
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 01-pain-scene v1.6 [--candid | --confront] [+ --marked]
REGISTER: cinematic film still. Single frame.

[SUBJECT] name the force being applied, and the body under it.   -> PARTS/subject
[EVIDENCE] the symptom as physical fact. Required, G9.           -> PARTS/evidence
[ENVIRONMENT] one specific place, and the clutter of the routine
              it disrupts.                                       -> PARTS/environment
[GAZE]                                                           -> PARTS/gaze
[LIGHT]                                                          -> PARTS/light
[MIRROR] --confront only, optional.                              -> PARTS/mirror
[MARK] --marked only. One, on the evidence, count closed.        -> MARKS
[GRADE] desaturated: one unresolved state, G11.                  -> PARTS/grade

No product, no panels, no insets. No mark unless --marked is in use.
STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
```

## PARTS

**`subject`** — [age/gender] in [ordinary specific wardrobe, lived-in not styled], mid-way
through [an ordinary daily action]. Then `Under that force:` [which limb, which brace,
where the weight goes], and `Face:` [the involuntary signs, named by muscle].

**State the force, never the meaning.** The slot names a force being applied or a movement
in progress — never a pause, never an intention. "Both hands stopped over the jar" and "an
ordinary lunch interrupted" both rendered as nothing; "both hands locked on the lid,
turning against it, the lid has not moved" rendered correctly.

**Restraint governs EMOTION, not effort.** A flat face over a slack body renders as nothing
at all. Where the moment is physical exertion the face still carries the involuntary signs
— jaw set, breath held, lips dragged at one corner — and those are not drama.

**The moment must be mundane** — something anyone lives daily, never a demonstration of
wrong behaviour. It has no picture of its own, so it is a rule here and never a prompt slot.

**`evidence`** — the symptom as physical fact. Mandatory in every variant (G9): expression
alone carries nothing. Pick the strongest rank present and write **only that one** into the
prompt; ranking is the writer's job and the model needs the choice, not the ladder.

1. the symptom itself on the body or object;
2. physical residue or debris it produces — what it leaves behind, and where;
3. the failed tool, in the state that shows it failed — "the jar key lying where it slipped
   off, its jaws still spread", because "already tried" is a meaning and has no picture;
4. gesture alone — weakest, only when 1-3 are impossible, and then at least one object in
   frame must imply the problem independently.

Evidence status: rank 1 has carried the passing renders and rank 3 held in the jar frames;
rank 2 has never yet been the ONLY evidence in a render, and rank 4 has never been rendered.

**`environment`** — [one specific ordinary place, tied to where the problem gets noticed],
[time of day], and the lived-in clutter belonging to that place, signalling the routine it
disrupts: [3-4 mundane objects]. Nothing arranged, nothing removed to tidy the frame.

Specificity is the only defence against the "stock photo of back pain" failure mode.
Generic is dead.

**`gaze`** — two values, each carrying its own problem class.

- `candid` (default) — unaware of the camera, gaze on the task or the ground. Physical pain
  and physical limitation; moments nobody would choose to be seen in.
- `confront` — looking directly into the lens, holding the viewer's eye. A half-turned
  glance reads as a model waiting for direction. Appearance, self-image, daily frustration.

**Gaze and light are bundled today, and two records say they should not be.**
`vocabulary.yaml` carries a third value, `reflect`, that this type does not declare; ADR-009
recorded an image fitting neither declared value, and the founding record flagged the same
bundling. Two records against a §6.2 bar of three. Un-bundling would make combinations
legal that are not legal today, so it is the owner's rule change, not a restructure.

**`light`** — two values, each selected by the gaze variant that names it.

- `low-key` (with `--candid`) — Key: [source, direction, colour temperature]. Fill: [weaker
  source]. Rim light separating subject from background. Deep shadow across [X%] of frame.
- `flat-ambient` (with `--confront`) — even ambient daylight, bright, minimal shadow, flat
  and unflattering.

**`mirror`** — optional, `--confront` only. A mirror behind or beside the subject showing
them from another angle, the reflection consistent with their actual position. It earns its
space twice: it gives the confrontation a natural reason, and it doubles the symptom
evidence without adding a second person. Render-confirmed 2026-08-12 on a thinning-hair
frame — the mirror carried the crown the subject cannot see himself.

**`grade`** — Desaturated [dominant hue], fine film grain, shallow depth of field, [lens
character]. `--candid` adds crushed blacks. This is G11's single-state clause: the whole
frame is one unresolved state, so the grade is absolute and not a difference between sides.

## MARKS

This type's own mark library, called by name from the skeleton and used by `--marked`
alone. Every mark obeys G3 and carries a count. `also in` notes keep a same-looking mark in
another type visible from here.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `glow` | a soft red radial glow sitting ON the evidence, sized to it and no larger, fading out before it touches anything else | red only | exactly 1 | 1 render · also in `01-pain-split` (hotspots), `02-symptom-rail` (vignettes) |
| `ring` | a thin red ring — a clean open circle of even line weight drawn around the evidence, touching nothing else | red only | exactly 1 | 0 renders · a proposal, and its first render is its founding evidence |

**The mark POINTS AT evidence. It never delivers a verdict.** No X, no check, no VS, no
thumbs, no exclamation glyph — that is `01-pain-split`'s language, and a glyph is text,
which G6 routes out of the render and into post.

**If `evidence` has nothing physical to point at, `--marked` is ILLEGAL** — use the base
variant. A mark over an empty frame invents the pain instead of marking it.

The mark owns a named slot and closes its own count inside that slot ("the only mark in
this image"), because a mark buried in prose is the one that vanishes (adapter Rule 7).
Deliberately NOT in the negative list: any phrasing like `second mark`. That qualifies a
noun the variant requires, which is Rule 1a's exact bleed shape.

Red appears ONLY in the mark, and the desaturated grade stays exactly as `grade` sets it.
G3 note: the base type is `exempt_from: [G3]` because it uses no signal colour at all —
this variant uses one, so its mark obeys G3 (red = pain) while the exemption stands for the
rest of the frame.

**Budget: exactly ONE mark, and never two classes in one frame.** This type's argument is
recognition, not diagnosis. A second mark makes it a diagram, which is `01-pain-split`'s
job and the reason the two are `never_with`.

## SLOT CONSTRAINTS
- **No red pixel anywhere, on `--candid` and `--confront`.** Those variants replace the red
  pain signal with acting, and a red glow there makes the image confess it is an ad.
  `--marked` is the sanctioned exception and narrows the rule to "red appears only in the
  mark": natural skin, food and household colour were never the target of this ban, and
  writing around them cost a render (see CHANGELOG 1.3).
- **The prompt budget.** A clause earns its place in a rendered prompt only if a render has
  failed without it. Everything else is a rule for the writer and stays in this file.
  Reference sizes, measured rather than guessed: the one proven `--marked` render at
  1669 characters, and the v1.5 set at 1760/1770/1880. Adapter Rule 6 asks for a re-read
  past 2500 and nothing this type has shipped has come near it. The measured history runs
  the opposite way from drift — forcing exertion out of prose alone took the jar prompt from
  1379 to 2153 characters, and the marked rewrite of the same image did three more jobs
  at 1669.

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

**Four more bleed in EVERY variant** — `studio lighting` here, plus `bright airy
lighting`, `flat daylight look` and `warm flattering light` in the variant blocks. Each
qualifies *light*, which every prompt in this type requires, so each is the shape Rule 1a
measured as `one panel brighter than the others` suppressing a required exposure drift.
The canonical list keeps them; the adapter drops them and the body asserts the lighting
positively instead. `golden hour` is safe — it qualifies nothing a prompt needs.

## VARIANTS
Diffs only. Each variant names the PARTS values it takes; the definitions stay in PARTS.

### --candid (default)
Channels: paid-social, advertorial header. Reads cinematic, survives being scrolled past.
Diff vs base: `gaze` = candid · `light` = low-key · `grade` adds crushed blacks.
- Negative additions: `bright airy lighting, flat daylight look, looking at camera`

### --confront
Channels: advertorial body, landing-page. Legible at thumbnail size.
Diff vs base: `gaze` = confront · `light` = flat-ambient · `mirror` becomes available.
- Negative additions: `golden hour, warm flattering light, exaggerated grimace, theatrical anger`

### --marked
The only variant that carries a graphic layer, and the only one that uses MARKS. It
composes WITH the gaze variants rather than replacing them — name both in the prompt
(`--confront --marked`), because gaze and mark are independent decisions.
Diff vs base: `[MARK]` becomes required and takes exactly one entry from MARKS · the base
line "No mark unless --marked is in use" is replaced by that entry's own closed count · the
mark is model-drawn (ADR-008 approach A).
- Negative additions: `badge, checkmark, VS, thumbs, exclamation glyph, arrow, text label`
- Three tokens DROP from the rendered avoid line — `red glow`, `pain hotspots`,
  `graphic overlay`. The reasoning is in NEGATIVE.

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
- **Unrequested four-pointed sparkle glyph, bottom-right, 2 of 2 jar renders examined
  2026-08-13.** Same corner and same form in both, and it takes the tone of whatever is
  beneath it — wood on the tabletop, white on the envelopes — which is a composite
  overlay's signature rather than a drawn element. Not this type's defect: it is the
  platform artefact `adapters/nano-banana.md` Rule 7 tracks, and the blend behaviour is
  new evidence for the watermark reading there. Intermittent — this type's mark-free
  control of 2026-08-12 recorded none. The v1.5 prompt set runs Rule 7's own untried test:
  one prompt names that corner as bare, two omit the clause.

## CHANGELOG
- 1.6 (2026-08-13): **restructured into a call-map plus two libraries** (ADR-012), on the
  owner's instruction to repeat the `02-cause-anatomy` shape. Same slots, same laws, same
  image — MINOR, as the model type's own 1.7 was. `PARTS` owns `subject`, `evidence`,
  `environment`, `gaze`, `light`, `mirror`, `grade`; `MARKS` owns `glow` and `ring`, the
  second entering with zero renders as a labelled proposal. The compression is where the
  duplication was: VARIANTS restated filler the skeleton already named and drops
  4052 → 1354, the skeleton block 1315 → 967. NOT copied
  from the model type: its removal test and 2:1 test, which are gates for a two-panel
  comparison this type has none of. `PARTS/gaze` records the gaze/light bundling and does
  not act on it — two records against a §6.2 bar of three. File 19394 → 22478.
- 1.5 (2026-08-13): **avoid-line law completed; the corner glyph recorded.** The NEGATIVE
  note dropped three Rule 1a bleeds under `--marked` and missed four that bleed in every
  variant — `studio lighting`, `bright airy lighting`, `flat daylight look` and `warm
  flattering light` all qualify *light*, which every prompt here requires. Nothing about
  what renders changed, and no passing render would have been forbidden by it. KNOWN-FLAKY
  opens with the unrequested bottom-right sparkle, 2 of 2 jar renders examined, carrying
  one fact the adapter does not have: the glyph takes the tone of the surface beneath it,
  so it is a composite overlay and not a drawn element. Shipped with it, three `--marked`
  prompts at 1760/1770/1880 characters against the variant's one proven render at 1669,
  Rule 1a gate clean at 0 unexplained hits with the checker verified against known-bad
  input first. `--marked` still stands on ONE render: the set asks whether the ring class
  exists at all, whether the glow survives crushed blacks, and whether the mark may sit on
  residue instead of on the body. File 17118 → 19394 characters.
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
