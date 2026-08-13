---
id: 01-pain-scene
step: 1
job: pain
device: scene
version: "1.13"
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
TYPE: 01-pain-scene v1.13 [--candid | --confront] [+ --marked]
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
through [an ordinary daily action]. Then `Under that force:` [which limb, which brace, where
the weight goes], and `Face:` [the involuntary signs, named by muscle].

Four laws, each paid for by a render (see the CHANGELOG entry's commit):

- **State the force, never the meaning.** The slot names a force being applied or a movement
  in progress — never a pause, never an intention.
- **The action must be DIAGNOSTIC** — a force only someone with this problem would apply.
  Both hands wrapped round a calf mid-press; a lid being forced that has not moved. Wiggling
  a plug reads as charging a phone.
- **A face cannot carry effort the body is not making**, and a face is never described by
  ABSENCE. Where the body genuinely strains the involuntary signs arrive unasked. Restraint
  governs EMOTION, not effort.
- **The moment must be mundane** — something anyone lives daily, never a demonstration of
  wrong behaviour. It has no picture of its own, so it never becomes a prompt slot.

**`evidence`** — the symptom as physical fact. Mandatory in every variant (G9): expression
alone carries nothing. Pick the strongest rank present and write **only that one** into the
prompt; ranking is the writer's job and the model needs the choice, not the ladder.

1. the symptom itself on the body or object;
2. physical residue or debris it produces — what it leaves behind, and where;
3. the failed tool, in the state that shows it failed — "the jar key lying where it slipped
   off, its jaws still spread", because "already tried" is a meaning and has no picture;
4. gesture alone — weakest, only when 1-3 are impossible, and then at least one object in
   frame must imply the problem independently.

Status: rank 1 has carried the passing renders and rank 3 held in the jar frames; rank 2 has
never been the ONLY evidence in a render, and rank 4 has never been rendered.

**Evidence may be SMALL, and an inset is not available.** A calf, a crown: small in frame and
instantly readable, because the action names the problem and the evidence confirms it. So a
weak image is not repaired by enlarging the evidence, and it cannot be repaired by an inset —
`vocabulary.yaml` defines `scene` as a single cinematic frame with **no panels and no
insets**, which is the device and not this type's preference. A pain argument that genuinely
needs a magnified inset is a `hero`- or `macro`-device image in another slot.

**`environment`** — [one specific ordinary place, tied to where the problem gets noticed],
[time of day], and the lived-in clutter belonging to that place, signalling the routine it
disrupts: [3-4 mundane objects]. Nothing arranged, nothing removed to tidy the frame.
Specificity is the only defence against the "stock photo of back pain" failure. Generic is
dead.

**`gaze`** — two values, each carrying its own problem class. The variant that names the gaze
also names the light; the two are bound together today.

- `candid` (default) — unaware of the camera, gaze on the task or the ground. Physical pain
  and physical limitation; moments nobody would choose to be seen in.
- `confront` — looking directly into the lens, holding the viewer's eye. A half-turned glance
  reads as a model waiting for direction. Appearance, self-image, daily frustration.

**`light`** — two values, each selected by the gaze variant that names it.

- `low-key` (with `--candid`) — Key: [source, direction, colour temperature]. Fill: [weaker
  source]. Rim light separating subject from background. Deep shadow across [X%] of frame.
- `flat-ambient` (with `--confront`) — even ambient daylight, bright, minimal shadow, flat
  and unflattering.

**`mirror`** — optional, `--confront` only. A mirror behind or beside the subject showing them
from another angle, the reflection consistent with their actual position. It earns its space
twice: it gives the confrontation a natural reason, and it doubles the symptom evidence
without a second person. Composes with `--marked`, confirmed 2 of 2 — the single mark appears
in the reflection alone and the count survives a doubled subject.

**`grade`** — Desaturated [dominant hue], fine film grain, shallow depth of field, [lens
character]. `--candid` adds crushed blacks. This is G11's single-state clause: the whole frame
is one unresolved state, so the grade is absolute, not a difference between sides.

## MARKS

This type's own mark library, called by name from the skeleton and used by `--marked` alone.
Every mark obeys G3 and carries a count. `also in` notes keep a same-looking mark in another
type visible from here.

| form | how it is drawn | count | evidence |
|---|---|---|---|
| `glow` | a soft radial bloom sitting ON the target, brightest at its centre and fading outward | exactly 1 | 7 renders · CANNOT be held to a boundary, 3 of 3 · also in `01-pain-split` (hotspots), `02-symptom-rail` (vignettes) |
| `ring` | a clean open circle of even line weight drawn around the target, touching nothing else | exactly 1 | 3 renders · holds its extent exactly · the class for a small target |

**Two forms, and colour supplies the meaning.** The form only makes the thing read AS a mark;
G3 says what it means — red for pain and wrong, orange for wrong heat and wrong pressure.
Confirmed: red glow on a body reads as pain, orange glow on an object reads as too hot to
touch, red ring on a small target reads as look-here.

**No FILLED form, ever, in this register.** A mark reads as a mark only when its form is one
the photographed scene could not have produced — emitted light, or drawn geometry. A filled
region that follows an object's own surface is exactly what paint, dye, tape and fabric look
like, so the eye reads it as material: a red tint made a glass into a pink glass, an orange
contact band made a sock look like it had an orange cuff. Both forms were borrowed from
`02-cause-anatomy` and both work there, because that type is a 2D ILLUSTRATION where
everything in frame is already drawn. This type is photographic, and a fill has no way to
announce itself. Wrong pressure is therefore an ORANGE GLOW on the contact, not a band.

**Three admission gates. Check them before choosing a class.**

1. **The fault must have a PLACE** — a knuckle, a kneecap, a neck muscle, a plug, a crusted
   collar: somewhere a viewer could put a finger. A mark LOCATES a fault; it cannot ADJUDICATE
   one. Where the fault is a quality spread over a whole object (dirty, cloudy, blunt, worn)
   there is nothing to point at, and `--marked` is ILLEGAL.
2. **A mark competes with the evidence it points at.** Over a surface condition it covers the
   very thing the viewer must see. So `--marked` is a CHOICE, not a default: on object
   subjects weigh the base variant first and let light and scale carry the evidence. A set of
   prompts should carry mark-free cases deliberately.
3. **Name a BOUNDED STRUCTURE as the target, never a size.** "Sized to it and no larger" does
   not bind. Name a structure and the mark takes its extent; name a patch, a scatter or a
   split and the model substitutes the nearest bounded object or spreads the mark across the
   area. Same finding as `02-cause-anatomy`.

**Two form limits.** `glow` BLOOMS — a radial falloff cannot be stopped at an outline, so
where a hard boundary matters the class is `ring` or `fill`. And `fill` needs an OPAQUE object
whose colour is far from the tint; on transparent pale glass the tint becomes the material and
no mark is visible at all.

**A mark can POINT or it can CLASSIFY.** A form only points; the colour classifies. On a BODY
pointing suffices because the viewer supplies the meaning. On an OBJECT it does not, and the
colour has to do the work — which is what orange did on the plug where red could not.

**The mark POINTS AT evidence. It never delivers a verdict.** No X, no check, no VS, no
thumbs, no exclamation glyph — that is `01-pain-split`'s language, and a glyph is text, which
G6 routes out of the render and into post. This is why "warning" resolves to G3's orange
rather than to a triangle.

The mark owns a named slot and closes its own count inside that slot ("the only mark in this
image"), because a mark buried in prose is the one that vanishes (adapter Rule 7).
Deliberately NOT in the negative list: any phrasing like `second mark` — it qualifies a noun
the variant requires, which is Rule 1a's bleed shape.

Signal colour appears ONLY in the mark, and the desaturated grade stays exactly as `grade`
sets it. G3 note: the base type is `exempt_from: [G3]` because it uses no signal colour at
all — this variant uses one, so its mark obeys G3 while the exemption stands for the rest of
the frame.

**Budget: exactly ONE mark, and never two classes in one frame.** This type's argument is
recognition, not diagnosis. A second mark makes it a diagram, which is `01-pain-split`'s job
and the reason the two are `never_with`.

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
- **Unrequested four-pointed sparkle glyph, bottom-right, 10 of 10 renders examined
  2026-08-13.** Same corner and same form in all four, and it takes the tone of whatever is
  beneath it — wood on a tabletop, white on envelopes, dark on a bath panel, pale on a navy
  shirt — which is a composite
  overlay's signature rather than a drawn element. Not this type's defect: it is the
  platform artefact `adapters/nano-banana.md` Rule 7 tracks, and the blend behaviour is
  new evidence for the watermark reading there. Intermittent — this type's mark-free
  control of 2026-08-12 recorded none. The v1.5 prompt set runs Rule 7's own untried test:
  one prompt names that corner as bare, two omit the clause.
- **Filled marks, WITHDRAWN at 1.13 on 0 of 2.** `fill` on a drinking glass and an orange
  `pressure` band on a sock elastic. Both rendered exactly as specified and both stopped being
  marks: the glass read as a pink glass, the band as an orange cuff. Not withdrawn for being
  ugly, but for being unable to announce themselves inside a photograph. Retest only if this
  type ever gains a non-photographic register.
- **Over-acted faces on the `--marked` renders, 2 observations, 2026-08-13.** A pushed-out
  lower lip on the posture frame, acute physical pain on the cable frame where the problem is
  a cable. Below the bar, and both prompts named the signs by muscle as the slot asks. Watch
  whether the mark itself invites the model to overplay the face.

## CHANGELOG
Current law is above; the reasoning behind each entry is in the commit it cites (ADR-013).

- 1.13 (2026-08-13): **a mark reads as a mark only when its form is one the photographed scene
  could not produce.** Filled forms withdrawn at 0 of 2 — a red `fill` turned a glass pink, an
  orange `pressure` band turned into a sock cuff. MARKS reorganised around the two proven
  forms, `glow` and `ring`, with G3 colour supplying the meaning; wrong pressure is an orange
  glow, not a band. Also settled: `glow` cannot be held to a boundary at 3 of 3, so extent
  belongs to `ring`; and the mark-free control read at a glance with nothing pointed at. · this commit
- 1.12 (2026-08-13): **`--marked` is a choice, not a default** — a mark laid over a surface
  condition covers the evidence it points at. On object subjects the base variant is weighed
  first, and prompt sets carry mark-free cases deliberately. Owner judgement on the glassware
  and limescale frames. Compressed to ADR-013 in the same pass: CHANGELOG rewritten to
  decisions plus commit pointers, case histories moved out of PARTS and MARKS. · this commit
- 1.11 (2026-08-13): **the fault must have a PLACE** — a mark locates, it cannot adjudicate,
  so `--marked` is illegal where the fault is a property of a whole object. With it: `glow`
  blooms and cannot be stopped at an outline; `fill` needs an opaque object far in colour
  from the tint; `heat` CONFIRMED on its founding render. · c876815
- 1.10 (2026-08-13): **`heat`, `pressure` and `fill` added**, owner decision, after the
  renders showed `glow` and `ring` only POINT — enough on a body, not on an object. Orange is
  G3's value for wrong heat and is what "warning" resolves to, a glyph being text. Also: a
  face cannot carry effort the body is not making. · ac0309b
- 1.9 (2026-08-13): **a mark binds to a bounded structure, not to a size instruction.** Name
  a structure and the mark takes its extent; name a patch or a split and it does not. · 4f26e39,
  count corrected in f85f8b8
- 1.8 (2026-08-13): **the action must be DIAGNOSTIC** — a force only someone with this problem
  would apply. Naming a force is not enough. Evidence may be small and still read, so an inset
  is not the fix; `scene` has none by definition. · 9089b65
- 1.7 (2026-08-13): compression pass — CHANGELOG preamble added, the two Rule 1a notes in
  NEGATIVE merged, WORKED EXAMPLES removed entirely (owner's call: both were untested and
  named slots that no longer exist). · fc8612c
- 1.6 (2026-08-13): **restructured into a call-map plus two libraries** (ADR-012), on the
  owner's instruction to repeat the `02-cause-anatomy` shape. `PARTS` owns the non-mark blocks,
  `MARKS` the mark library. Not copied: that type's removal and 2:1 tests, which gate a
  two-panel comparison this type has none of. · 7b9e59d
- 1.5 (2026-08-13): four more Rule 1a bleeds found in NEGATIVE, all qualifying *light*, which
  every prompt here requires. KNOWN-FLAKY opened with the unrequested corner sparkle. · 1c1c8c6
- 1.4 (2026-08-12): skeleton compressed 2144 → 1314 characters, no change to what renders.
  `RATIO:` dropped per adapter Rule 4; the moment rule and the evidence ladder moved out as
  instruments for the writer; `[SUBJECT]` lost its "or pausing at" branch. · e7f5556
- 1.3 (2026-08-12): **`--marked` variant added** — one graphic mark, on the evidence, never a
  verdict. Owner decision. `vocabulary.yaml` dropped "zero graphic layers" from the `scene`
  device in the same change. Also here: the state-the-force rule, and `--confront`'s restraint
  scoped to emotion rather than effort. · 2b0f333
- 1.2 (2026-08-11): channels gain `landing-page`. The type contradicted ITSELF: `--confront`
  already declared it while the frontmatter excluded it. Found by the slot-rules/frontmatter
  drift check in scripts/validate.py. · 973addf
- 1.1 (2026-08-10): SYMPTOM EVIDENCE made required (→G9); GAZE and LIGHT split into
  per-variant conditionals; [MIRROR] slot added; environment clutter law tightened.
  Evidence: seed conversation.md.
- 1.0 (2026-08-10): initial from the garage car-exit exemplar. seed: conversation.md.
