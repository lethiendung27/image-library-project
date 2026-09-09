---
id: lede-pain
version: "0.3"
status: active
replaced_by: null
products_in_frame: none
requires_product_photo: false
awareness: [unaware, problem-aware]
copied_from: 01-pain-scene
copied_at_version: "1.18"
blocked_by: null
exempt_from: []
---

# lede-pain

## PURPOSE
Make a cold viewer recognize themselves in a raw, cinematic pain moment — before they
know any product exists. Acting and physical evidence carry the pain, and the COST in the
same frame is what makes it agitate rather than depict. No product, no
layout, no verdict; `--marked` may add ONE mark that points at the evidence.

**Copied verbatim from `01-pain-scene` at version 1.18** (owner instruction, 2026-09-09).
Everything from PURPOSE to KNOWN-FLAKY below is that file's text, spliced by script rather
than retyped. `copied_at_version` in the frontmatter is what makes the copy auditable:
`scripts/validate.py` warns when the parent moves past it, so the drift this file is
exposed to is visible rather than silent. What is deliberately NOT copied is the parent's
WORKED EXAMPLES — SPEC §3.3 keeps a rendered example's prompt text as the record of what
actually rendered, and those renders were the parent's — and its CHANGELOG, which is the
parent's own evidence trail.

## TRIGGER
use_when: >
  Cold traffic arriving from an ad whose creative shows the problem, where this frame is
  the message match and the reader would not yet search the category by name. The
  product block's problems_solved are physical and locatable — a body, an object, a
  room — rather than abstract. Prefer this over lede-inuse when the reader does not yet
  know a product like this exists, and over lede-lineup and lede-testing whenever the
  page has to earn attention before it can earn trust.

## BOUNDARY
**Against `lede-inuse`, and this is the whole line: the product is ABSENT here and
PRESENT there.** No judgement is needed to tell them apart, which is what makes the pair
safe to put in front of a router.

**Against `lede-testing`** — this frame is the READER's situation; that one is the
REVIEWER's bench. The hands belong to different people and the room is a different room.
A frame where the sufferer is also the tester argues neither.

**Against `lede-winner`** — a winner frame presents a choice already made. This one
presents a problem not yet named. They are the two ends of the page and never compete for
the same brief.

Its boundaries against `01-pain-split` and `02-symptom-rail` are the parent's and are not
restated here.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: lede-pain v0.3   (skeleton copied verbatim from 01-pain-scene v1.18)
      [--candid | --confront] [+ --marked]
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

## FOUNDING RENDER ROUND

**One render, 2026-09-09 — round 2 prompt 1, rendered at v0.2.** A man half-risen from a
desk chair, one hand on the small of his back, an office at dusk. Verdict **`partial`**,
self-assigned under ADR-011 on a render that was opened and looked at. Ledger:
`eval/render-tests.jsonl`, ts `2026-09-09`.

**This type has ZERO corpus observations and now has one render.** The corpus is editorial
review publishing and never opens on a pain shot, so this file could not be evidenced from
`stills/top list/` at all. A render is the only evidence it can get, which makes this the
one type in the namespace where the render round is not a second stream but the first.

**What the type is for arrived.** The stall in the movement reads as a physical fact rather
than as an expression — knees bent, hips not straight, weight still on the chair — which is
G9's whole preference. A14's COST is in the same frame and legible: the coat over the chair
back and a colleague's dark, emptied desk behind him say what the back is taking.

**Three failures, all at 1 of 1, and the third is the prompt's own:**

| slot | observed |
|---|---|
| `[GROUND]` | ring value **0.25** and saturation **0.25** against *"mid-toned and almost colourless"*; the frame reads as dusk, not as an ordinary room |
| `[GROUND]` | *"thrown out of focus"* not delivered — the far desk, monitor and telephone hold readable detail |
| safe area | the subject is cut by the bottom edge and the desk runs off the right |

**The safe-area line should not have been in that prompt.** G10 binds text and product, and
this type is defined by having no product and no words. A candid photograph of a person
cannot keep a tenth of the frame clear of its own subject, so the clause was unsatisfiable
the moment it was pasted in. That is a prompt-writing fault, not a render fault, and it is
recorded here because the same boilerplate closes every prompt in the round.

**A measurement caveat that belongs to this render more than to any other.** At value 0.25
the ring texture reads 2.8, which `scripts/ground_audit.py` calls DESIGNED — a photograph of
a real office filed with the flat coloured grounds. See `registry/toplist-instruction.md`
§Ground for the exposure bound; nothing here is patched on it.

## CHANGELOG
- 0.3 (2026-09-09): **FOUNDING RENDER ROUND** — one render, round 2 prompt 1 at 0.2,
  `partial`, and the first evidence this type can have: it holds zero corpus observations
  because editorial review publishing carries no pain lede. The physical fact and A14's
  cost both arrived. Three failures at 1 of 1, none patched — and the third, a safe-area
  breach by the subject's own limbs, is a fault in the prompt: G10 binds text and product,
  and this type has neither.
- 0.2 (2026-09-09): **copied verbatim from `01-pain-scene` at 1.18** — owner decision,
  reversing 0.1's citation (ADR-070). PURPOSE, SKELETON, PARTS, MARKS, SLOT CONSTRAINTS,
  NEGATIVE and KNOWN-FLAKY are that file's text, spliced by script. WORKED EXAMPLES and
  the parent's CHANGELOG are not copied, for the reasons in `toplist-instruction.md`.
  `inherits` becomes `copied_from` + `copied_at_version`, and the validator now warns when
  the parent moves past 1.18.
- 0.1 (2026-09-09): drafted for the top-N lede slot, inheriting `01-pain-scene`, whose
  `use_when` already reads *"Cold traffic that does not know the product yet. Advertorial
  header image, Facebook/native ad creative, opening image of a story"* — the owner's
  type 1 word for word. No skeleton is copied. ADR-069.
