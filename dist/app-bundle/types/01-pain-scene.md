---
id: 01-pain-scene
step: 1
job: pain
device: scene
version: "1.17"
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
avoid_when: >
  Marketplace galleries, main image, or any position where the product must be
  visible. Cannot sell alone — must be paired with a relief/proof image. Never
  in the same set as 01-pain-split: one pain beat per page, and two of them
  compete for the same job rather than building on each other.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 01-pain-scene v1.17 [--candid | --confront] [+ --marked]
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
carried the passing renders, rank 3 held in the jar frames, **rank 2 has now carried two
frames as the ONLY evidence** (2 of 2), and rank 4 has never been rendered. Rank 2 is the safe
rung for a mark-free frame: debris is an OBJECT and a renderer never refuses an object, where it
may refuse a symptom.

**A SYMPTOM DESCRIBED AS A COMPARISON DOES NOT RENDER.** "Half again the size of the other arm"
and "fingers drifting sideways away from the thumb" both returned an ordinary body. State the
abnormality without reference to anything else — cords standing out, ankles over shoe edges,
callus pads on a sole. Write the thing, never the difference.

**Evidence may be SMALL, and an inset is not available.** A calf, a crown: small in frame and
instantly readable, because the action names the problem and the evidence confirms it. So a
weak image is not repaired by enlarging the evidence, and it cannot be repaired by an inset —
`vocabulary.yaml` defines `scene` as a single cinematic frame with **no panels and no
insets**, which is the device and not this type's preference. A pain argument that genuinely
needs a magnified inset is a `hero`- or `macro`-device image in another slot.

**`cost`** — [what the pain is taking away], in the same frame and subordinate to the body it
is being taken from. Required in every variant.

`subject`, `evidence` and any mark all answer WHERE IT HURTS; nothing here answered WHAT IT
TAKES AWAY, which is fault **A14** and the reason a set correct in every slot agitated in none
of them. Adding this block and moving nothing else reversed it on the same six products: the
block rendered as written in 6 of 6 and stayed subordinate in 6 of 6, and no failure in that
set was a failure of this block.

Five forms have rendered, and choosing between them IS the argument: the activity happening
without them · the abandoned object of it, left as they left it · the thing they cannot finish ·
the person waiting, or the one they cannot turn to · someone doing it instead.

- **Say the subordination in the prompt**: `sharp enough to read and never larger, nearer or
  brighter than the body it is being taken from`. Held 6 of 6.
- **A cost is not clutter.** Clutter says where the frame is, a cost says what the pain
  prevents. Papers and a mug said `office`; a bare worktop read as a demonstration until a
  younger pair of hands reached in to take the jar.
- **An OBJECT cost argues as strongly as a person cost** (1 of 1) and carries no G13 exposure,
  so it is first choice wherever a minor would otherwise enter the frame. G1 survives it.
- **Where the cost is a minor, G13 binds this block too** — neutral face, distress signs as
  explicit negations, which did not bleed in 3 of 3.
- **LOCK THE COST TO THE PART THAT HURTS.** Not "someone is waiting" — the one thing this exact
  body part is FOR, refused. Costs that were merely present rendered 6 of 6 and agitated in none.
- **THE FAILURE HAS ALREADY HAPPENED.** A still frame cannot show that a movement STOPPED: a
  stalled reach and an arrested turn both came back as the action succeeding. Name a finished
  failure.
- **ITS RESIDUE IS A DISPLACED OBJECT, NOT A STATE.** A car "pulled over with hazards on" came
  back driving; a mug on its side, a case burst open, keys on a doormat, oranges in a gutter and
  shopping left at the foot of a flight all rendered. 11 of 12.

**`place`** — [one ordinary place, tied to where the problem gets noticed], [time of day]. One
phrase, nothing else in it. The clutter inventory is WITHDRAWN at 1.16: the owner's instruction
is that this type attends to the pain and not the surroundings, and a four-word phrase returned
the richest environment of the round-2 set unasked. Where a routine object matters to the
argument it is not clutter — it is the COST.

**`gaze`** — two values, each carrying its own problem class. The variant that names the gaze
also names the light; the two are bound together today.

- `candid` (default) — unaware of the camera, gaze on the task or the ground. Physical pain
  and physical limitation; moments nobody would choose to be seen in.
- `confront` — looking directly into the lens, holding the viewer's eye. A half-turned glance
  reads as a model waiting for direction. Appearance, self-image, daily frustration.

**`light`** — **the real light of the place and nothing added.** Name the source actually
there — a window over a sink, sodium street lamps, supermarket strips, an overcast sky, rain —
and let the surroundings be as bright, dark or wet as that place is.

`low-key` with its key, fill, rim and "deep shadow across [X%] of frame", and its `--confront`
twin `flat-ambient`, are **withdrawn at 1.17** on the owner's rejection and on measurement: the
midtone share of a frame went 28.4% → 61.0% when this block replaced them, across 18 renders.
The old grade also ate the mark, taking one glow to peak R−G 45 against 111-203 elsewhere.

**A dark PLACE is not a dark PICTURE.** A car at night and a dim stairwell both came back
readable. Name the place's own light and the exposure follows.

**`mirror`** — optional, `--confront` only. A mirror behind or beside the subject showing them
from another angle, the reflection consistent with their actual position. It earns its space
twice: it gives the confrontation a natural reason, and it doubles the symptom evidence
without a second person. Composes with `--marked`, confirmed 2 of 2 — the single mark appears
in the reflection alone and the count survives a doubled subject.

**`grade`** — **an ordinary photograph in ordinary light.** Normal exposure, detail held in
both the shadows and the highlights, the midtones open across most of the frame. Colour true to
life and muted rather than vivid, every surface keeping its own real colour.

**`exempt_from: [G11]` as of 1.17, narrowly.** G11's instrument is "reduced saturation ... cool or
neutral, never warm"; the muted half is kept and the rest is not, because **G11 never asks for
darkness** and darkness is what the withdrawn wording produced. Taken by ID on
`04-proof-lockedframe`'s precedent, which G11's own text names. Reasoning and the prior "never
warm" breach are in ADR-049. What carries the unresolved state instead is the argument: the
`cost` block, and the mark where one is used.

## MARKS

This type's own mark library, called by name from the skeleton and used by `--marked` alone.
Every mark obeys G3 and carries a count. `also in` notes keep a same-looking mark in another
type visible from here.

| form | how it is drawn | count | evidence |
|---|---|---|---|
| `glow` | a soft radial bloom sitting ON the target, brightest at its centre and fading outward | exactly 1 | 26 renders · lands where a HAND already is · a POINT landmark binds it, a span does not · also in `01-pain-split` (hotspots), `02-symptom-rail` (vignettes) |
| `ring` | a clean open circle of even line weight drawn around the target, touching nothing else | exactly 1 | 6 renders · holds its extent exactly · the class for a small target |

**Two forms, and colour supplies the meaning.** The form only makes the thing read AS a mark;
G3 says what it means — red for pain and wrong, orange for wrong heat and wrong pressure.
Confirmed: red glow on a body reads as pain, orange glow on an object reads as too hot to
touch, red ring on a small target reads as look-here.

**Rank the forms by what they MEAN here, not by how cleanly they draw.** `ring` came back
textbook 3 of 3 in round 2 and the owner's ruling was that it is the less effective of the two:
a ring says LOOK HERE where this type needs the frame to say IT HURTS. So `glow` gets contained
rather than withdrawn — a boundary record is not grounds to retire a mark.

**No FILLED form, ever, in this register.** A mark reads as a mark only when its form is one
the photographed scene could not have produced — emitted light, or drawn geometry. A filled
region that follows an object's own surface is exactly what paint, dye, tape and fabric look
like, so the eye reads it as material: a red tint made a glass into a pink glass, an orange
contact band made a sock look like it had an orange cuff. Both forms work in `02-cause-anatomy`,
which is drawn throughout; this type is photographic and a fill has no way to announce itself. Wrong pressure is therefore an ORANGE GLOW on the contact, not a band.

**Four admission gates. Check them before choosing a class.**

1. **The fault must have a PLACE** — a knuckle, a kneecap, a neck muscle, a plug, a crusted
   collar: somewhere a viewer could put a finger. A mark LOCATES a fault; it cannot ADJUDICATE
   one. Where the fault is a quality spread over a whole object (dirty, cloudy, blunt, worn)
   there is nothing to point at, and `--marked` is ILLEGAL.
2. **A mark competes with the evidence it points at.** Over a surface condition it covers the
   very thing the viewer must see. So `--marked` is a CHOICE, not a default: on object
   subjects weigh the base variant first and let light and scale carry the evidence. A set of
   prompts should carry mark-free cases deliberately. **Mark-free is conditional on the
   force**: two such frames in one set, same macro, same absent face, same rank-1 evidence —
   the jar passed because forcing a lid that has not moved IS diagnostic, the mouse failed
   because a hand resting on a mouse is not, and with nothing pointed at the pain left its own
   frame. That mouse frame had read fine a round earlier WITH a `ring`. So a mark can carry a
   force that is not diagnostic, and dropping it is safe only where `subject`'s diagnostic law
   is genuinely met. **Mark-free has two safe routes and no others**: rank-2 residue as sole
   evidence (2 of 2), and GROSS swelling stated absolutely (2 of 2). Not fine deformity, which
   the renderer twice declined to draw; not where the pose can cover the evidence.
3. **Name a BOUNDED STRUCTURE as the target, never a size.** "Sized to it and no larger" does
   not bind. Name a structure and the mark takes its extent; name a patch, a scatter or a
   split and the model substitutes the nearest bounded object or spreads the mark across the
   area. Same finding as `02-cause-anatomy`. **But a size bound says how big, not where to
   start**: landmark plus size bound bound the EXTENT 4 of 4 (largest connected component
   8.1-9.6% x 12.5-14.1% of frame, against synthetic tight and wide controls), and in 2 of
   those 4 the bloom still formed on the soft mass beside the landmark. The 2 that landed each
   named what the mark must NOT reach. **That sentence is REFUTED and must not be written** —
   carried twice and breached twice, omitted twice and landed twice, with the omitting pair the
   most concentrated marks this type has made.

   **Placement is bound by the STRUCTURE'S SHAPE.** Name a POINT — a kneecap, an ankle bone, the
   ball of a thumb. A SPAN slides along itself, and a landmark the camera cannot see cannot be
   marked at all. **The size bound stays**: it has no measurable effect on extent, and it is kept
   only because SLOT CONSTRAINTS removes a clause once a render has done without it and come back
   CORRECT — one of three unbounded frames produced no mark at all.

4. **A HAND ON THE BODY IS ALREADY A POINTER, SO PUT THE MARK WHERE THE HAND IS.** Every marked
   frame that read has them coincident; the one that put the hand at a nose and the bloom on a
   cheek named two places and confirmed neither. **Never pose a hand where the model has a
   stronger idiom** — the pose moves and the mark is left stranded.

**One form limit, and it belongs to `fill`.** `fill` needs an OPAQUE object whose colour is far
from the tint; on transparent pale glass the tint becomes the material and no mark is visible at
all. `glow`'s old limit — a radial falloff cannot be stopped at an outline, so route a hard
boundary to `ring` or `fill` — is RETIRED at 1.16. Its extent binds (gate 3), and the routing
was never legal anyway in a register that admits no filled form.

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
- **A minor in the subject slot is where this type gets REFUSED, not merely criticised.**
  **G13** binds and carries the rules; they reduce the flagged bundle without removing it,
  because the force inventory and the covert gaze ARE this type. Where a frame is still
  refused, take the object-only execution — the failed tool and its residue, nobody in
  frame — which the ledger records twice.
- **The prompt budget.** A clause earns its place in a rendered prompt only if a render has
  failed without it. Everything else is a rule for the writer and stays in this file.
  Reference sizes, measured rather than guessed: the one proven `--marked` render at
  1669 characters, and the v1.5 set at 1760/1770/1880. Adapter Rule 6 asks for a re-read
  past 2500 and nothing this type has shipped has come near it. The measured history runs
  the opposite way from drift — forcing exertion out of prose alone took the jar prompt from
  1379 to 2153 characters, and the marked rewrite of the same image did three more jobs
  at 1669. Measured at 1.16: `cost` costs 300-447 characters, mean 372, and
  took the same six products from 1412-1583 to 1306-1999 — 3 of 6 over the 1800
  ceiling four other types declare, and none near Rule 6's 2500.

## NEGATIVE
```
[G6] + red glow, pain hotspots, graphic overlay, arrows, badges, split panel,
white background, studio lighting, stock photo look, posed model, fake grimace,
smiling, clean staged interior, saturated colors, advertising composition,
product placement
```
This list is canonical and model-agnostic. Since ADR-014 it is **not rendered into the
prompt at all** — the owner removed the `Strictly avoid:` sentence by hand, re-rendered, and
the output did not change. The list stays here and in the query output's `avoid` field for a
future model with a real negative channel. Seven of its tokens were Rule 1a bleeds when it
WAS rendered (`red glow`, `pain hotspots`, `graphic overlay` under `--marked`; `studio
lighting` plus the three lighting tokens in the variant blocks, all qualifying *light*), and
that is why the bounds they carried are asserted positively in the body instead.

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
- **Unrequested four-pointed sparkle glyph, bottom-right, 16 of 16 renders, last
  counted 2026-08-25.** Same corner and same form throughout, and it takes the tone of whatever
  is beneath it — wood, envelopes, a bath panel, a navy shirt — which is a composite overlay's
  signature rather than a drawn element. Not this type's defect: it is the platform artefact
  `adapters/nano-banana.md` Rule 7 tracks, and the blend behaviour is evidence for the watermark
  reading there. Intermittent — this type's mark-free control of 2026-08-12 recorded none.
  Rule 7's own test, proposed here at v1.5, **has still never run**: no set since has named that
  corner as bare.
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

- 1.17 (2026-08-25): **the type asks for a photograph, not a film still.** `light` takes the
  real light of the place, `grade` an ordinary exposure, `REGISTER` drops `cinematic film still`;
  midtone share 28.4% → 61.0%. `exempt_from` gains **G11** narrowly (ADR-049). Also: the cost is
  LOCKED to the part that hurts; a failure must be finished and its residue a DISPLACED OBJECT;
  the mark goes where the HAND is; a POINT landmark binds placement; the exclusion sentence is
  REFUTED; rank 2 carries a mark-free frame alone; a COMPARISON does not render. · this commit
- 1.16 (2026-08-25): **a pain frame must say what the pain TAKES AWAY, not only where it
  hurts.** New required PART `cost`, earned 6 of 6 where adding it alone reversed the owner's
  `does not agitate` on the same six products; new fault **A14**. `environment` becomes `place`,
  one phrase, no clutter inventory. `glow` NOT withdrawn — its extent binds at 4 of 4, which
  corrects 1.13, and marks rank by meaning over craft. Mark-free is conditional on a diagnostic
  force. Ratios corrected to ADR-016's legal set. · 60d5714
- 1.15 (2026-08-21): **a minor in the subject slot is a renderability constraint, not a
  taste one.** Owner reported nano banana REFUSING a pain frame built on a child. New global
  rule **G13** carries the three writer's rules; SKELETON and SLOT CONSTRAINTS reference it
  by ID. Mechanism and measurement are in the commit. · 0104619
- 1.14 (2026-08-13): **type PASSED by the owner; file finalised.** WORKED EXAMPLES returns
  with the two renders that earned it — the mark-free laundry frame and the blister ring — in
  full text per SPEC §3.3, closing the gap opened at 1.7. ADR-014 adopted: the canonical
  NEGATIVE list is no longer rendered into a prompt. Contributed to `argument-faults.md`: the
  glassware failure joins A3, and **A11 is new** — a mark must have a form the register could
  not have produced. · this commit
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
