---
id: 01-pain-scene
step: 1
job: pain
device: scene
version: "1.8"
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
TYPE: 01-pain-scene v1.8 [--candid | --confront] [+ --marked]
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

**The action must be DIAGNOSTIC.** Naming a force is not enough — it must be a force only
someone with this problem would apply. The renders that read do it before the evidence is
found: both hands wrapped around a calf mid-press, a hand pushing hair off the crown at a
mirror, both hands locked on a lid that has not moved. Nobody performs any of those without
the problem. Wiggling a charging plug reads as charging a phone, and turning a glass to the
light reads as checking a glass; both were written here on 2026-08-13, both named a force,
and neither body said a problem existed.

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

**Evidence may be SMALL, and an inset is not available.** In the two strongest renders the
symptom is a small part of the frame — a calf, a crown — and both read instantly, because
the action named the problem and the evidence only confirmed it. So a weak image is not
repaired by enlarging the evidence, and it cannot be repaired by an inset at all:
`vocabulary.yaml` defines `scene` as a single cinematic frame with **no panels and no
insets**. That is the device, not this type's preference. A pain argument that genuinely
needs a magnified inset is a `hero`-device or `macro`-device image and belongs in another
slot on the page.

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
**Seven of the tokens above are Rule 1a bleeds: DROP them from a rendered avoid line,
never rephrase.** The avoid line is prose to this model — no negative channel, no operators
— so a token qualifying a noun the prompt requires suppresses that noun.
- Under `--marked`: `red glow`, `pain hotspots`, `graphic overlay`. The variant requires a
  red glow or ring.
- In every variant: `studio lighting`, plus `bright airy lighting`, `flat daylight look`
  and `warm flattering light` from the variant blocks. All four qualify *light*, which
  every prompt in this type requires — Rule 1a's measured row `one panel brighter than the
  others`, which suppressed a required exposure drift, is the same shape.

The list stays canonical and model-agnostic; the adapter drops from it at render time and
the body asserts the positive form instead. `arrows` and `badges` stay in every variant,
the mark law bars them; `golden hour` is safe, qualifying nothing a prompt needs.

`02-symptom-rail` measured the general case on 2026-08-13: pasting its canonical list whole
into three prompts produced 27 Rule 1a hits. Copying this block instead of transforming it
is the error. A rendered avoid line here is usually G6 core plus the two hand descriptors
adapter Rule 5 mandates.

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

## KNOWN-FLAKY
- **Unrequested four-pointed sparkle glyph, bottom-right, 4 of 4 renders examined
  2026-08-13.** Same corner and same form in all four, and it takes the tone of whatever is
  beneath it — wood on a tabletop, white on envelopes, dark on a bath panel, pale on a navy
  shirt — which is a composite
  overlay's signature rather than a drawn element. Not this type's defect: it is the
  platform artefact `adapters/nano-banana.md` Rule 7 tracks, and the blend behaviour is
  new evidence for the watermark reading there. Intermittent — this type's mark-free
  control of 2026-08-12 recorded none. The v1.5 prompt set runs Rule 7's own untried test:
  one prompt names that corner as bare, two omit the clause.

## CHANGELOG
Evidence for every entry is in `eval/render-tests.jsonl` and in the commit that made it;
git is the audit surface, so decisions are recorded here and workings are not.
- 1.8 (2026-08-13): **the action must be DIAGNOSTIC**, added to `PARTS/subject`. A force in
  progress is not enough; it must be a force only someone with this problem would apply. The
  owner rejected two of the six v1.7 prompts before rendering — both named a force, neither
  named a problem. Tested against all five passing renders first: every one clears the rule,
  so it forbids no render this type has produced, and it also explains the 1.2 partial and
  the two dead renders behind 1.3. `PARTS/evidence` gains the finding that kills the obvious
  wrong fix: in the strongest renders the symptom is a small part of the frame and reads
  anyway, so a weak image is not repaired by enlarging the evidence — and `scene` is defined
  in `vocabulary.yaml` as having no insets at all, which makes the magnified-inset fix a
  different device rather than a patch here. KNOWN-FLAKY's corner glyph goes from 2 of 2 to
  4 of 4 renders examined, now across four different surface tones. File 17428 → 19695.
- 1.7 (2026-08-13): **compressed, on the owner's instruction.** No law changed and no
  render behaviour changed. The CHANGELOG gains the preamble it never had and entries
  1.3-1.6 are cut to their decisions, the workings staying where they already were, in git.
  NEGATIVE's two Rule 1a notes merged: they stated one mechanism twice, for two groups of
  tokens. WORKED EXAMPLES removed entirely — both examples were `run: untested` since 1.1,
  five versions behind the call-map, and both named slots that no longer exist
  (`SYMPTOM EVIDENCE`, `MOMENT`), so as few-shot material they taught the wrong form. SPEC
  §3.3 makes the section optional and this type is active under ADR-001, so no promotion
  criterion rests on it. What is lost is few-shot at fill time, and the honest note is that
  this type has five passing renders whose prompt text survives nowhere: the section earns
  its place back the first time a rendered prompt can fill it in full, per SPEC §3.3.
  CHANGELOG 6685 → 4061, NEGATIVE 1218 → 1536, WORKED EXAMPLES
  2744 → 0. File 22478 → 17428 characters.
- 1.6 (2026-08-13): **restructured into a call-map plus two libraries** (ADR-012), on the
  owner's instruction to repeat the `02-cause-anatomy` shape. `PARTS` owns `subject`,
  `evidence`, `environment`, `gaze`, `light`, `mirror` and `grade`; `MARKS` owns `glow` and
  `ring`. Same slots, same laws, same image — MINOR, as the model type's own 1.7 was. NOT
  copied from it: the removal test and the 2:1 test, which gate a two-panel comparison this
  type has none of.
- 1.5 (2026-08-13): **four more Rule 1a bleeds found in NEGATIVE**, all four qualifying
  *light*, which every prompt here requires. Tested against this type's five passing renders
  first: none would have been forbidden. KNOWN-FLAKY opened with the unrequested
  bottom-right sparkle, 2 of 2 jar renders examined.
- 1.4 (2026-08-12): **skeleton compressed, no change to what renders** — 2144 to 1314
  characters. The `RATIO:` line dropped per adapter Rule 4; the moment rule and the evidence
  ladder moved out as instruments for the writer; `[GAZE]` and `[LIGHT]` filler moved into
  the variant blocks that choose them; four negative lines dropped as already asserted
  positively or already G6. One quality fix, not a cut: `[SUBJECT]` lost its "or pausing at"
  branch, which had produced a dead render that morning and contradicted the state-the-force
  rule added at 1.3.
- 1.3 (2026-08-12): **`--marked` variant added** — one graphic mark, on the evidence, never
  a verdict. Owner decision, per the standing rule that graphic-element rules are his to
  write. `vocabulary.yaml` dropped "zero graphic layers" from the `scene` device in the same
  change, the device's identity being its geometry. Three strands of evidence: the measured
  cost of forcing visible exertion out of prose alone (figures in SLOT CONSTRAINTS); four
  renders in one session, technically sound and none legible at a glance; and no
  fast-reading pain option existing on paid-social or advertorial at all. Also here: the
  state-the-force rule, and `--confront`'s restraint scoped to emotion rather than effort.
- 1.2 (2026-08-11): channels gain `landing-page`. The type contradicted ITSELF: the
  --confront variant already declares "Channels: advertorial body, landing-page"
  while the frontmatter excluded it. Frontmatter corrected to match the variant.
  Found by the new slot-rules/frontmatter drift check in scripts/validate.py.
- 1.1 (2026-08-10): SYMPTOM EVIDENCE made required (→G9); GAZE and LIGHT split into
  per-variant conditionals; [MIRROR] slot added; environment clutter law tightened.
  Evidence: seed conversation.md (bathroom-mirror confront exemplar confirmed the
  Test F prediction that gesture alone cannot carry an invisible symptom).
- 1.0 (2026-08-10): initial from the garage car-exit exemplar. seed: conversation.md.
