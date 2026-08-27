---
id: 01-pain-scene
step: 1
job: pain
device: scene
version: "1.18"
status: active
replaced_by: null
ratios: ["16:9", "3:4"]
channels: [paid-social, advertorial, landing-page]
requires_product_photo: false
generation_mode: single-pass
axes:
  gaze: [candid, confront]
variants: [candid, confront, marked]
exempt_from: [G1, G3, G4, G11]
pairs_with: [06-relief-hero, 06-relief-scene, 04-proof-lockedframe]
never_with: [01-pain-split]
---

# 01-pain-scene

## PURPOSE
Make a cold viewer recognize themselves in a raw, cinematic pain moment — before they
know any product exists. Acting and physical evidence carry the pain, and the COST in the
same frame is what makes it agitate rather than depict. No product, no
layout, no verdict; `--marked` may add ONE mark that points at the evidence.

## TRIGGER
use_when: >
  Cold traffic that does not know the product yet. Advertorial header image,
  Facebook/native ad creative, opening image of a story. Its only job is to make
  the viewer recognize themselves and keep reading. Use --candid for physical
  pain and moments nobody would choose to be seen in; use --confront for
  appearance, self-image and daily-frustration problems where the mirror moment
  IS the moment.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 01-pain-scene v1.18 [--candid | --confront] [+ --marked]
REGISTER: editorial photojournalism, natural and unstaged. Single frame.

[SUBJECT] name the force being applied, and the body under it.   -> PARTS/subject
          Where that body is a minor, G13 binds.
[EVIDENCE] the symptom as physical fact. Required, G9.           -> PARTS/evidence
[COST] what the pain takes away, in frame, subordinate. Required. -> PARTS/cost
[PLACE] one ordinary place and a time of day. One phrase.        -> PARTS/place
[GAZE]                                                           -> PARTS/gaze
[LIGHT]                                                          -> PARTS/light
[MIRROR] --confront only, optional.                              -> PARTS/mirror
[MARK] --marked only. One, on the evidence, count closed.        -> MARKS
[GRADE] an ordinary photograph in ordinary light.                -> PARTS/grade

No product, no panels, no insets. No mark unless --marked is in use.
STYLE: editorial photojournalism, natural and unstaged.
```

## PARTS

**`subject`** — [age/gender] in [ordinary specific wardrobe, lived-in not styled], mid-way
through [an ordinary daily action]. Then `Under that force:` [which limb, which brace, where
the weight goes], and `Face:` [the involuntary signs, named by muscle].

Four laws, each paid for by a render (see the CHANGELOG entry's commit):

- **State the force, never the meaning.** A force being applied or a movement in progress —
  never a pause, never an intention.
- **The action must be DIAGNOSTIC** — a force only someone with this problem would apply.
  Wiggling a plug reads as charging a phone.
- **A face cannot carry effort the body is not making**, and is never described by ABSENCE.
  Restraint governs EMOTION, not effort.
- **The moment must be mundane** — never a demonstration of wrong behaviour. It has no picture
  of its own, so it never becomes a prompt slot.

**`evidence`** — the symptom as physical fact. Mandatory in every variant (G9): expression
alone carries nothing. Pick the strongest rank present and write **only that one** into the
prompt; the model needs the choice, not the ladder.

1. the symptom itself on the body or object;
2. physical residue or debris it produces — what it leaves behind, and where;
3. the failed tool in the state that shows it failed, because "already tried" has no picture;
4. gesture alone — weakest, only when 1-3 are impossible, and then at least one object in
   frame must imply the problem independently.

Status: rank 1 carries most passing renders, rank 3 held in the jar frames, **rank 2 has
carried two frames as the ONLY evidence** (2 of 2), rank 4 has never been rendered.

- **Rank 2 is the safe rung for a mark-free frame.** Debris is an OBJECT and a renderer never
  refuses an object, where it may refuse a symptom.
- **A SYMPTOM DESCRIBED AS A COMPARISON DOES NOT RENDER.** "Half again the size of the other
  arm" and "fingers drifting sideways away from the thumb" both returned an ordinary body.
  State the abnormality without reference to anything else. Write the thing, never the
  difference.
- **Evidence may be SMALL, and an inset is not available.** `vocabulary.yaml` defines `scene`
  as a single frame with no panels and no insets. An argument that genuinely needs a magnified
  inset is a `hero`- or `macro`-device image in another slot.

**`cost`** — [what the pain is taking away], in the same frame and subordinate to the body it
is being taken from. Required in every variant. Nothing else in the skeleton answers WHAT IT
TAKES AWAY, which is fault **A14**.

Five forms have rendered, and choosing between them IS the argument: the activity happening
without them · the abandoned object of it · the thing they cannot finish · the person waiting,
or the one they cannot turn to · someone doing it instead.

- **LOCK THE COST TO THE PART THAT HURTS.** Not "someone is waiting" — the one thing this exact
  body part is FOR, refused. Costs merely present rendered 6 of 6 and agitated in none.
- **THE FAILURE HAS ALREADY HAPPENED.** A still frame cannot show that a movement STOPPED: a
  stalled reach and an arrested turn both came back as the action succeeding.
- **ITS RESIDUE IS A DISPLACED OBJECT, NOT A STATE.** A car "pulled over with hazards on" came
  back driving. A mug on its side, a case burst open, oranges in a gutter: 11 of 12.
- **Say the subordination in the prompt**: `sharp enough to read and never larger, nearer or
  brighter than the body it is being taken from`. Held 6 of 6.
- **A cost is not clutter.** Clutter says where the frame is; a cost says what the pain prevents.
- **An OBJECT cost argues as strongly as a person cost** and carries no G13 exposure, so it is
  first choice wherever a minor would otherwise enter the frame.
- **Where the cost is a minor, G13 binds this block too** — neutral face, distress signs as
  explicit negations, which did not bleed in 3 of 3.

**`place`** — [one ordinary place, tied to where the problem gets noticed], [time of day]. One
phrase, nothing else in it. The clutter inventory is WITHDRAWN at 1.16: a four-word phrase
returned the richest environment of a set unasked. Where a routine object matters to the
argument it is not clutter — it is the COST.

**`gaze`** — two values, each carrying its own problem class.

- `candid` (default) — unaware of the camera, gaze on the task or the ground. Physical pain and
  physical limitation; moments nobody would choose to be seen in.
- `confront` — looking directly into the lens. A half-turned glance reads as a model waiting
  for direction. Appearance, self-image, daily frustration.

**`light`** — **the real light of the place and nothing added.** Name the source actually there
— a window over a sink, sodium street lamps, supermarket strips, an overcast sky, rain — and let
the surroundings be as bright, dark or wet as that place is.

`low-key` with its key, fill, rim and deep shadow, and its `--confront` twin `flat-ambient`, are
**withdrawn at 1.17** on the owner's rejection and on measurement: midtone share 28.4% → 61.0%
across 18 renders. The old grade also ate the mark, taking one glow to peak R−G 45 against
111-203 elsewhere. **A dark PLACE is not a dark PICTURE** — a car at night and a dim stairwell
both came back readable. Name the place's own light and the exposure follows.

**`mirror`** — optional, `--confront` only. A mirror showing the subject from another angle, the
reflection consistent with their actual position. It gives the confrontation a natural reason and
doubles the symptom evidence without a second person. Composes with `--marked`, 2 of 2 — the
single mark appears in the reflection alone and the count survives a doubled subject.

**`grade`** — **an ordinary photograph in ordinary light.** Normal exposure, detail held in both
the shadows and the highlights, midtones open across most of the frame. Colour true to life and
muted rather than vivid, every surface keeping its own real colour.

**`exempt_from: [G11]` as of 1.17, narrowly.** G11's instrument is "reduced saturation ... cool
or neutral, never warm"; the muted half is kept and the rest is not, because **G11 never asks for
darkness** and darkness is what the withdrawn wording produced. Taken by ID on
`04-proof-lockedframe`'s precedent, which G11's own text names. Reasoning and the prior
"never warm" breach are in ADR-049. What carries the unresolved state instead is the argument:
the `cost` block, and the mark where one is used.

## MARKS

This type's own mark library, called by name from the skeleton and used by `--marked` alone.
Every mark obeys G3 and carries a count.

| form | how it is drawn | count | evidence |
|---|---|---|---|
| `glow` | a soft radial bloom sitting ON the target, brightest at its centre and fading outward | exactly 1 | 26 renders · lands where a HAND already is · a POINT landmark binds it, a span does not · also in `01-pain-split` (hotspots), `02-symptom-rail` (vignettes) |
| `ring` | a clean open circle of even line weight drawn around the target, touching nothing else | exactly 1 | 6 renders · holds its extent exactly · the class for a small target |

**Colour supplies the meaning.** The form only makes the thing read AS a mark; G3 says what it
means. Red glow on a body reads as pain, orange glow on an object as too hot to touch, red ring
on a small target as look-here.

**Rank the forms by what they MEAN here, not by how cleanly they draw.** `ring` came back
textbook 3 of 3 and the owner ruled it the less effective of the two: a ring says LOOK HERE where
this type needs the frame to say IT HURTS. A boundary record is not grounds to retire a mark.

**No FILLED form, ever, in this register.** A mark reads as a mark only when its form is one the
photographed scene could not have produced. A fill follows an object's own surface, which is what
paint, dye and tape look like: a red tint made a glass into a pink glass, an orange band made a
sock look like it had an orange cuff. Wrong pressure is therefore an ORANGE GLOW on the contact,
not a band. `fill` also needs an OPAQUE object far in colour from the tint.

**Four admission gates. Check them before choosing a class.**

1. **The fault must have a PLACE** — somewhere a viewer could put a finger. A mark LOCATES a
   fault; it cannot ADJUDICATE one. Where the fault is a quality spread over a whole object
   (dirty, cloudy, blunt, worn) there is nothing to point at and `--marked` is ILLEGAL.
2. **A mark competes with the evidence it points at**, so `--marked` is a CHOICE, not a default,
   and a set should carry mark-free cases deliberately. **Mark-free has two safe routes and no
   others**: rank-2 residue as sole evidence (2 of 2), and GROSS swelling stated absolutely
   (2 of 2). Not fine deformity, which the renderer twice declined to draw; not where the pose
   can cover the evidence; and not where `subject`'s diagnostic law is unmet — a hand resting on
   a mouse failed where forcing an unmoving lid passed.
3. **Name a BOUNDED STRUCTURE as the target, never a size.** Name a patch, a scatter or a split
   and the model substitutes the nearest bounded object. **Placement is bound by the STRUCTURE'S
   SHAPE**: name a POINT — a kneecap, an ankle bone, the ball of a thumb. A SPAN slides along
   itself, and a landmark the camera cannot see cannot be marked at all. **A sentence naming what
   the mark must NOT reach is REFUTED and must not be written** — carried twice and breached
   twice, omitted twice and landed twice, the omitting pair the most concentrated marks this type
   has made. **The size bound stays** despite having no measurable effect on extent, because
   SLOT CONSTRAINTS removes a clause only once a render has done without it and come back
   CORRECT, and one of three unbounded frames produced no mark at all.
4. **A HAND ON THE BODY IS ALREADY A POINTER, SO PUT THE MARK WHERE THE HAND IS.** Every marked
   frame that read has them coincident; the one that put the hand at a nose and the bloom on a
   cheek named two places and confirmed neither. **Never pose a hand where the model has a
   stronger idiom** — the pose moves and the mark is left stranded.

**A mark can POINT or it can CLASSIFY.** A form only points; the colour classifies. On a BODY
pointing suffices because the viewer supplies the meaning. On an OBJECT the colour has to do the
work — which is what orange did on the plug where red could not.

**The mark POINTS AT evidence. It never delivers a verdict.** No X, no check, no VS, no thumbs,
no exclamation glyph — that is `01-pain-split`'s language, and a glyph is text. This is why
"warning" resolves to G3's orange rather than to a triangle.

The mark owns a named slot and closes its own count inside that slot ("the only mark in this
image"), because a mark buried in prose is the one that vanishes (adapter Rule 7). Deliberately
NOT in the negative list: any phrasing like `second mark` — it qualifies a noun the variant
requires, which is Rule 1a's bleed shape.

**Signal colour appears ONLY in the mark**, and the rest of the frame keeps the true-to-life
colour `grade` sets. G3 note: the base type is `exempt_from: [G3]` because it uses no signal
colour at all — this variant uses one, so its mark obeys G3 while the exemption stands for the
rest of the frame.

**Budget: exactly ONE mark, and never two classes in one frame.** This type's argument is
recognition, not diagnosis. A second mark makes it a diagram, which is `01-pain-split`'s job and
the reason the two are `never_with`.

## SLOT CONSTRAINTS
- **No red pixel anywhere, on `--candid` and `--confront`.** Those variants replace the red pain
  signal with acting. `--marked` is the sanctioned exception and narrows the rule to "red appears
  only in the mark": natural skin, food and household colour were never the target of this ban.
- **A minor in the subject slot is where this type gets REFUSED, not merely criticised.** **G13**
  binds and carries the rules. Where a frame is still refused, take the object-only execution —
  the failed tool and its residue, nobody in frame — which the ledger records twice.
- **The prompt budget.** A clause earns its place in a rendered prompt only if a render has
  failed without it, and is removed only once a render has done without it and come back correct.
  Everything else is a rule for the writer and stays in this file. Measured history: shipped
  prompts run 1300-2300 characters, `cost` costs 300-450 of them, and adapter Rule 6 asks for a
  re-read past 2500, which nothing here has reached.

## NEGATIVE
```
[G6] + red glow, pain hotspots, graphic overlay, arrows, badges, split panel,
white background, studio lighting, stock photo look, posed model, fake grimace,
smiling, clean staged interior, saturated colors, advertising composition,
product placement
```
Canonical and model-agnostic. Since ADR-014 it is **not rendered into the prompt at all** —
removing it changed no output. It stays here and in the query output's `avoid` field for a
future model with a real negative channel. Seven of its tokens were Rule 1a bleeds when it WAS
rendered, which is why the bounds they carried are asserted positively in the body instead.

## VARIANTS
Diffs only. Each variant names the PARTS values it takes; the definitions stay in PARTS.

### --candid (default)
Channels: paid-social, advertorial header. Reads cinematic, survives being scrolled past.
Diff vs base: `gaze` = candid · `light` = the real light of the place.
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
Both rendered, both owner-passed, both kept in FULL text per SPEC §3.3 — the render ledger
stores verdicts and not prompts, so this is the only record of what actually rendered. Both
carry a closing `Strictly avoid:` line because they were rendered before ADR-014 dropped it;
do not copy that line into a new prompt. **Their `REGISTER`, `[LIGHT]` and `[GRADE]` lines are
superseded at 1.17** and must not be copied either; the examples stay verbatim because they record
what actually rendered (SPEC §3.3). Both predate `cost` and carry none: they are kept for
the mark decisions they settled, not as templates.

### example: wet-laundry-candid — skeleton@1.12, run: pass
```
TYPE: 01-pain-scene v1.12 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man late 30s, t-shirt and tracksuit bottoms, in a cramped utility room late at night,
mid-way through hauling a sodden tangle of washing out of the machine drum with both
arms: the bundle already clear of the door and sagging heavily between his hands, water
running off it. Under that force: the back rounded over the load, both elbows locked,
the weight dragging his shoulders down and forward.
Face: jaw set, breath held, eyes down on the bundle.

[EVIDENCE]
Water runs off the bundle in a steady stream and has spread into a wide pool across the
vinyl floor, his forearms and the front of his t-shirt soaked through, a dark tide line
already up the leg of his tracksuit bottoms.

[ENVIRONMENT]
Narrow utility room off a kitchen, late night. Lived-in clutter belonging to that place:
a basket of dry washing shoved against the wall, a mop leaning in the corner, boxes of
powder on a shelf, a bin bag by the door. Nothing arranged, nothing removed to tidy the
frame.

[GAZE] unaware of the camera, gaze down on the load in his arms.

[LIGHT] low-key. Key: a bare bulb overhead, hard and close. Fill: cold spill from the
kitchen doorway behind him. Rim light along the shoulder and the wet forearms. Deep
shadow across most of the frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field,
35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers.
```
The mark-free case. Nothing is pointed at and the frame reads at a glance, because the action
is one nobody performs without the problem and the evidence is the whole floor rather than a
detail.

### example: blister-ring-confront — skeleton@1.12, run: pass
```
TYPE: 01-pain-scene v1.12 --confront --marked
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Woman early 30s, office clothes with the jacket off, sitting sideways on a hallway chair
turned to camera, one bare foot hauled up across the opposite knee, mid-way through
pressing a thumb into the ball of that foot to test what is there: the thumb sunk in and
the toes splayed back away from it. Under that force: the ankle gripped hard by her other
hand, the knee pulled in, the shoulders twisted round to face the lens.
Face: mouth pressed flat, brow drawn in, chin tucked.

[EVIDENCE]
A taut shiny blister has risen at the base of the little toe where the shoe has worn, the
skin around it thickened and glazed, one heeled shoe lying on its side on the floor below
with the lining rubbed through at that exact spot.

[ENVIRONMENT]
Narrow hallway of a rented flat, early evening. Lived-in clutter belonging to that place:
a bag dropped by the door, post on the shelf, a coat over the chair back, the other shoe
still upright. Nothing arranged, nothing removed to tidy the frame.

[GAZE] looking directly into the lens, holding the viewer's eye.

[LIGHT] even ambient daylight from a glazed front door, minimal shadow, flat and
unflattering.

[MARK]
ONE thin red ring: a clean open circle of even line weight drawn around THE BLISTER and
sized to it, touching nothing else. It is the only mark in this image.

[FORBIDDEN] No insets, no split panels, no badges, no glyphs. Nothing else in the frame
is marked.

[GRADE] Desaturated neutral, muted greys and greens, fine film grain, moderate depth of
field, 35mm. Red appears only in the ring.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers.
```
The `ring` case. A small target is the one job a ring does better than a glow: it held its
extent exactly where a glow blooms.

## KNOWN-FLAKY
- **Unrequested four-pointed sparkle glyph, bottom-right, 16 of 16 renders, last counted
  2026-08-25.** Same corner and same form throughout, taking the tone of whatever is beneath it,
  which is a composite overlay's signature rather than a drawn element. Not this type's defect:
  it is the platform artefact `adapters/nano-banana.md` Rule 7 tracks. Intermittent — a mark-free
  control of 2026-08-12 recorded none. Rule 7's own test, proposed here at v1.5, **has still
  never run**: no set since has named that corner as bare.
- **Filled marks, WITHDRAWN at 1.13 on 0 of 2.** Both rendered exactly as specified and both
  stopped being marks. Retest only if this type ever gains a non-photographic register.
- **Over-acted faces on `--marked` renders, 2 observations.** Below the bar, and both prompts
  named the signs by muscle as the slot asks. Watch whether the mark itself invites the model to
  overplay the face.

## CHANGELOG
Current law is above; the reasoning behind each entry is in the commit it cites (ADR-013).

- 1.18 (2026-08-25): **compression pass, and three corrections to 1.17.** Case histories and
  measurement narratives move out of PARTS, MARKS, SLOT CONSTRAINTS and KNOWN-FLAKY into the
  commits that cite them (ADR-013); CHANGELOG entries at and below 1.12 collapse to one line.
  No law removed. Corrected: `evidence` Status was left duplicated by a half-matched edit,
  gate 3 contradicted itself on whether a size bound binds extent, and MARKS still referred to
  "the desaturated grade" that 1.17 withdrew. · this commit
- 1.17 (2026-08-25): **the type asks for a photograph, not a film still.** `light` takes the
  real light of the place, `grade` an ordinary exposure, `REGISTER` drops `cinematic film still`;
  midtone share 28.4% → 61.0%. `exempt_from` gains **G11** narrowly (ADR-049). Also: the cost is
  LOCKED to the part that hurts; a failure must be finished and its residue a DISPLACED OBJECT;
  the mark goes where the HAND is; a POINT landmark binds placement; the exclusion sentence is
  REFUTED; rank 2 carries a mark-free frame alone; a COMPARISON does not render. · this commit
- 1.16 (2026-08-25): **a pain frame must say what the pain TAKES AWAY, not only where it
  hurts.** New required PART `cost`, earned 6 of 6; new fault **A14**. `environment` becomes
  `place`, one phrase. `glow` NOT withdrawn — marks rank by meaning over craft, correcting 1.13.
  Ratios corrected to ADR-016's set. · 60d5714
- 1.15 (2026-08-21): **a minor in the subject slot is a renderability constraint, not a taste
  one** — the renderer refused such a frame outright. New global rule **G13**, referenced by ID
  from SKELETON and SLOT CONSTRAINTS. · 0104619
- 1.14 (2026-08-13): **type PASSED by the owner.** WORKED EXAMPLES returns in full text per
  SPEC §3.3. ADR-014 adopted: the NEGATIVE list is no longer rendered into a prompt. **A11 is
  new** in `argument-faults.md`. · this commit
- 1.13 (2026-08-13): **a mark reads as a mark only when its form is one the photographed scene
  could not produce.** Filled forms withdrawn at 0 of 2. MARKS reorganised around `glow` and
  `ring`, with G3 colour supplying the meaning. Its boundary finding is corrected at 1.16. · this commit
- 1.12 (2026-08-13): `--marked` is a CHOICE, not a default — a mark laid over a surface
  condition covers the evidence it points at. · this commit
- 1.11 (2026-08-13): the fault must have a PLACE; `--marked` illegal where the fault is a
  property of a whole object. · c876815
- 1.10 (2026-08-13): `heat`, `pressure` and `fill` added, owner decision; a face cannot carry
  effort the body is not making. · ac0309b
- 1.9 (2026-08-13): a mark binds to a bounded structure, not to a size instruction. · 4f26e39
- 1.8 (2026-08-13): the action must be DIAGNOSTIC; evidence may be small, so an inset is not
  the fix. · 9089b65
- 1.7 (2026-08-13): compression pass — WORKED EXAMPLES removed, CHANGELOG preamble added. · fc8612c
- 1.6 (2026-08-13): restructured into a call-map plus two libraries (ADR-012). · 7b9e59d
- 1.5 (2026-08-13): four more Rule 1a bleeds found in NEGATIVE; KNOWN-FLAKY opened. · 1c1c8c6
- 1.4 (2026-08-12): skeleton compressed 2144 → 1314 characters; `RATIO:` dropped per adapter
  Rule 4. · e7f5556
- 1.3 (2026-08-12): `--marked` variant added — one mark, on the evidence, never a verdict. · 2b0f333
- 1.2 (2026-08-11): channels gain `landing-page`; the type had contradicted itself. · 973addf
- 1.1 (2026-08-10): symptom evidence made required (→G9); GAZE and LIGHT split per variant.
- 1.0 (2026-08-10): initial from the garage car-exit exemplar. seed: conversation.md.
