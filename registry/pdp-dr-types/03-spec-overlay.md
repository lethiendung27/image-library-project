---
id: 03-spec-overlay
step: 3
job: spec
device: overlay
version: "0.13"
status: reserved
replaced_by: null
channels: [landing-page]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [title, badge]
variants: []
exempt_from: []
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Criterion 3: two rounds on the owner's page v17 — section-02 failed by the owner on quality, section-03 (the instruction as it stands) graded by the harness after the owner's word on the size of its words and marks (ADR-112); 0.4 adds the owner's design rules (ADR-113) and has no render; set section-06 is its first, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1: no corpus record carries this id, because the type is written from the owner's image instruction of 2026-09-18 rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-110, and its three reserved neighbours are named in BLOCK."
---

# 03-spec-overlay — PDP-DR SECTION TYPE, DRAFT

**The FEATURES mode of the owner's image instruction** (`~/Downloads/images prompt.txt`,
2026-09-18, ADR-110). One of the seven section types, for the images outside the product card's gallery;
`registry/pdp-dr-instruction.md`, *The section form*, carries the form and the law they all share.

The owner's rules for this mode, word for word:

```
- Depict the feature or problem described in the input
- Product is visible and clearly presented
- Icons, supporting symbols, and concise text overlays allowed
  (infographic-style, functional information only)
- Human faces allowed, but keep expressions neutral and contextual
```

It is the type the instruction's **feature image** was waiting for (ADR-106): a section image
whose block argues ONE named feature, which may carry one short line.

## PURPOSE
Show one named feature at work, as one realistic photograph of the product clearly presented —
in use wherever the feature acts on something — under a small functional drawn layer: the
feature's own mark, an icon, a figure, or one short tag in the page's own words. It answers *"what
does this do to the thing it is for"*. The image sits beside its own HTML copy; the picture makes
that one feature line visible in three seconds.

## TRIGGER
use_when: >
  An LP2 image outside the product card's gallery whose section argues one named
  feature: an item of a features or modes block, a safety or quality block naming what
  the product is built with, any line whose claim is a part, a figure or a capability.
  It is also the type for a claim nobody can see and a camera cannot catch, drawn as
  its own mark over the product in use. Take 03-use-demo when the item is an act of
  the buyer's hands; 06-relief-after when the item is a benefit state a camera can
  catch; 03-mechanism-diagram when the item explains a process rather than shows a
  capability; 03-spec-macro, 03-spec-callout or 04-proof-stat for a gallery tile,
  which this type never fills.

## SKELETON
The section form since ADR-112: the owner's image instruction as it stands. Its Image_Type is this
type's mode and its Description the field's own page values; the prompt is one concise natural
paragraph with no labels, in this order. Each arrow names an entry below or in *The section form*.

**Before a word of the prompt** (ADR-124), the set's notes answer three questions in order. The
owner's verdict on `section-07` was that the mechanism had no thinking in it: six overlay values
offered as a menu, and a writer picking one.

```
  00. THE PRODUCT — read it before anything else (ADR-126): PARTS, CONNECTIONS, GRIP,
      SEQUENCE, THE INDICATION. The set's notes carry all five, from the attached photo
      and the owner's usage photos first, then the brief, then the page's copy.
  0a. THE EVENT  — what physically happens when this feature works? Name it as something
      a camera could see if it were slowed down, opened up or made visible.
  0b. THE FRAME  — stage that event: who or what does it, to what, where, at what moment.
      If nothing is happening in the frame, the frame is wrong, whatever is drawn on it.
  0c. THE LAYER  — draw the EVENT, never a label for it; and say which family it is,
      `event` or `whisper` (MARKS/overlay).
```

```
TYPE: 03-spec-overlay v0.7 [family: event | whisper] [overlay: mark | icon | figure | tag | callout | view]
Image_Type: FEATURES

  1. The register and the camera: "Editorial realism product feature image",
     the angle and distance, the real place the feature matters in.   -> PARTS/scene
  2. The product BY NAME, fully visible and clearly presented; on a seat
     of a clearly different tone where it is sat on.                   -> PARTS/product
  3. The feature at work: what it is doing, to what.                   -> PARTS/feature
  4. The drawn layer, in a sentence of its own: what is drawn, what it
     lands on, and that it is bold and large enough to read on a phone. -> MARKS/overlay
  5. The words, after the mark: the page's own tag, set once, large and bold in
     the lock's typeface and text colour, on a plain ground of the opposite value
     or with a figure in the lock's chip, in the middle of the picture; they may
     sit on or against the product.                                  -> SLOT CONSTRAINTS
  6. The lock's lighting family and colour tone, and the instruction's tone.
  7. G1 in one sentence: "Use the attached product photo as the exact reference."
```

## PARTS

**`product-reading`** — **before the event, read the product** (ADR-126). The set's notes state its
operating model in five lines: **PARTS** (what each body, lead, probe, clip or button is, and which
is which in the attached photo); **CONNECTIONS** (what attaches to what, in what order, and to what
on the vehicle, body or surface); **GRIP** (which part a hand holds and where, as the usage photos
show it); **SEQUENCE** (the real procedure, numbered); **THE INDICATION** (how the product tells the
operator it is working — a lamp, a tone, a reading, a movement); and **WHAT IT MAKES UNNECESSARY**
(ADR-127) — the old way the buyer no longer has to use.
- **A frame never shows the work being done the way the product makes unnecessary.** Where the claim
  is *without cutting*, nothing in frame is cut; *without dismantling*, nothing is apart; *without a
  second tool*, no second tool. A find frame for a tool that traces a fault through a closed loom
  came back with the loom cut open and bare strands at the probe tip, which argues against the page
  it sits on, 1 of 1.
- **What is hidden is shown by the INDICATION and by a mark pointing INTO the closed object** — a
  glow at one spot under intact insulation, the tool's own lamp on that spot — never by opening it. Sources rank: the attached product
photo and the owner's usage photos, then the brief, then the page's copy (ADR-120).
- **Every frame is ONE NAMED STEP of that sequence, and the set says which.** The product is in its
  working state in that step: clipped, gripping, connected, switched on, under load. **A product in
  frame but not doing its job voids the frame**, and so does an action that belongs to no step —
  three of this type's last nine renders had the tool connected to nothing, its parts swapped, or
  its operator inspecting something by eye while the tool watched.

**`event`** — the feature's physical event, and the frame is built on it (ADR-124). **ONE event to
a frame** (ADR-125): where a feature line names several states, modes or capabilities, the frame
draws the one state in which something HAPPENS and the words carry the rest. `OFF` is not drawable,
and neither is a mode that is not selected or a system that is not connected — asked for all three
switch positions at once, a render came back with a stray black line across the middle that meant
nothing. The question is
never *what shall I draw on this product* but *what happens when this feature works*: sound leaving
a speaker and reaching the animal; the wedge of ground a sensor watches; a pan browning three
scallops identically; a tone entering a loom at the clip and stopping at the break. **The frame
contains that event**, with its hand, its subject, its moment — steam, movement, a reaction. A
product presented on a bench with nothing happening is the fault the owner failed 4 of 7 times in
`section-07`, and no drawn layer rescues it.


**`scene`** — **two hands, each with a job the step needs** (ADR-126). The prompt names what the
left hand does and what the right hand does, and asks for nothing that would need a third. **Only
the step's props**: anything the named step does not need stays out of frame — no loose parts, no
coiled spare leads, no second tool. A frame that holds everything at once reads as a rubbish heap,
which is the owner's own word for 2 of 3 in `section-09`.

**`scene`** — **no hand closes, presses or holds a clip, a plug or a connector** (ADR-128). The
connection is already made when the frame opens; the hands are on the product's body, on the panel
or on the loom. Measured: **3 of 3** frames whose prompt put a hand on a clip came back carrying a
clip the product does not have, and 4 of the 6 that did not ask are correct. **The props clause
above does not cover this**, and the distinction is the point: it bans a FOREIGN object, and what
appears here is **a duplicate of the product's own part** — a second red clip is not a prop the step
does not need, it is the step's own prop drawn twice. Naming each body by what it carries does not
fix it either: `section-11` did that in all nine prompts and the rate went 3 of 9 to 5 of 9. Two of
the five are still unexplained, and the lever named twice over is a usage photograph (ADR-126,
ADR-127).

**`scene`** — **no labelled props** (ADR-125). Where a frame needs a second object of a kind that is
always branded — a battery, a bottle, a box, a packet — it is cropped to the part that matters or
kept out: the renderer letters every label it can see, and a frame with three batteries in it came
back carrying `LAWN MOWER`, `COMMERCIAL TRUCKT` and `AUTOKOTIVE`. The lock's no-other-text line does
not reach a prop's own printing (ADR-123).

**`scene`** — the place the feature matters in, named so that it carries no signage (ADR-109:
2 of 6 frames brought shop signs or labelled packaging into a frame whose only words were its
own line). **A person here is the derived USER** (*The person in frame*), with the feature at work in
their hands; the expression is neutral and contextual, as the owner's rule says, and never poses. Their clothes are named pieces they own and could get wet in, never a category (*The person in frame*).

**`product`** — named as the page names it, placed and never described (G2). **Clearly presented**
is the owner's word and it is the difference from `06-relief-after`: here the product is the
subject, the nearest and sharpest thing in the frame. **Scale comes from the host**, never from a
share of the frame, and the prompt moves the camera: *shot close enough that the product reads
whole* (ADR-106; held 6 of 6 in `03-mechanism-signal`'s set 04). A thin product is framed on its
working end (ADR-109). **A seated product sits on a seat of a clearly different tone**, asked as a
relation, never as a colour: arm B of ADR-111 left the sentence out and 2 of its 3 seated frames put
the cushion on a black seat of its own tone, where arm A carried it 4 of 4 (ADR-112). A share of the
frame, 40–60%, is named only on a studio or a graphic ground, where nothing fixes the size.

**`feature`** — the one feature the item names, doing its work on the thing it is for. Where the
feature is a part, the camera shows that part in use; where it is a capacity or a rating, the
frame shows the thing in use that the figure is about: a hold on a joint that is holding, a size
beside the hand that holds it (ADR-109).

## MARKS

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `overlay` | a parameter, and the item's line picks it. `mark`: the invisible thing in its OWN form — sound as notes or a spoken bubble, a frequency as a chart keyed to what it targets, a lure as the paths the insects fly, a signal as the known symbol a buyer already reads. `icon`: one to three plain supporting symbols in the lock's icon style. `figure`: the page's figure with its unit. `tag`: two to five words naming the feature. `callout`: up to three labels on bold leaders, each ending ON the part it names, and the prompt names that part. `view`: an inset shaped like the optic, showing what the user sees | a mark in the colour of the thing itself — luminous blue for a working signal (G3), warm where the thing is warm; an icon in the lock's icon style and text colour; the lock's accent only on a call-out line or a chip (ADR-113); never red, never a flat green, never on the product | one form to a frame, and the one short line beside it | the owner's twelve feature frames (ADR-106): the mark is the thing itself 12 of 12, on or inside the subject 8 of 12, a generic glowing arc 0 of 12 · `03-mechanism-signal` set 04: one short line spelled right 3 of 3 · this type's first three renders, under KNOWN-FLAKY |

- **The words are LARGE, and 18 px is the floor** (ADR-127, held ADR-128). Every drawn word is set
  so its capital measures at least 18 px with the field shown 390 px wide — about 5% of a 4:3
  render's height. **This works and it is the fix to copy**: say the size as a share of the picture,
  *the capitals about a twentieth of the picture's height*, never as an adjective. Measured on
  `section-10`, written as an adjective: 8.3 px on the phone, 3 of 3. Measured on `section-11`,
  written as a share: **19.6 to 35.3 px, median 27.9, 9 of 9**, contrast 11.4 to 15.7:1.
  Measure with `scripts/text-size.py` before grading.
- **A headline runs a quarter to a third of the frame's width, and a third is a CEILING** (ADR-128).
  Given the band as a bare instruction the renderer read it as a floor and overshot in 6 of 9, one
  of them running 92.3% of the width and crowding the picture it was there to label. A line past a
  third is as wrong as a line under the floor.
- **A HEADLINE and a LABEL sit directly on the photograph** (ADR-128, narrowed by ADR-129): no
  plate, no band, no box behind them. Where the ground is light the words stay white and the dark
  edge does the work. A light plate appeared 3 times and brought black letters with it all 3; in the
  owner's seventeen references of 2026-10-05 a headline or a label sits directly on the picture
  9 of 9. **A FIGURE WITH ITS UNIT is the exception and keeps its card** — the FIGURE CARD, a drawn
  card with a thin glowing border and a faint translucent fill, floating in the scene at about the
  size of a hand, which **this type owns** and which is NOT the gallery's flat chip form (ADR-130,
  on the owner's word *"cho phép tất cả"*); the owner's references set the figure this way 4 of 4.
  **An ICON keeps its own outline box.** ADR-128 banned all three by writing the headline's fault as
  a property of every drawn word.
- **A SET spans the overlay forms** (ADR-129). A set of nine uses **at least four of the six**, and
  no form more than three times. One form to a FRAME stands (ADR-125); one form to a SET is the
  fault — `section-12` was written with `tag` 9 times and `figure`, `icon`, `callout`, `view` and
  `mark` none, against a corpus whose commonest form is the figure (7 of 12, ADR-106; 6 of 17 in the
  2026-10-05 references). The form is this type's answer to *what kind of image is this*, and a set
  that uses one has not asked.
- **A feature frame is PRODUCT-LED** (ADR-129): a person appears only where the step needs a hand.
  Measured 2 of 17 in the owner's references against 7 of 9 in the set that was rejected. Where the
  frame argues an indication, a range or a compatibility there is no person and often no place —
  **8 of the 17 references are a dark studio, a seamless ground or a technical grid.**
- **A drawn mark may sit in the AIR between the product and its subject** (ADR-129). Nothing is
  drawn ON a wire, a loom or a cable (ADR-128) — but arcs in the air showing a sensing field reach
  the subject without touching it, which is what the owner's reference does with its radiating
  arcs.
- **A light at a connection reads as INDICATION, never as arcing** (ADR-126). It sits where metal
  actually meets metal, on a CLOSED contact, and never in the gap of an open jaw: a bloom between
  open jaws came back reading as an arc weld, which is a short circuit and the opposite of the
  claim, 1 of 1.
- **The mark is LIGHT IN THE SCENE, named as a physical thing, never as a graphic** (ADR-125). The
  prompt says what the light IS and how it behaves — a soft blue glow that spills onto the wire and
  loses itself in the shadow, the dust hanging in a beam, the sheen it throws along a lead — and
  never *arcs*, *a band*, *a bar*, *a wave*, *a ring*. **A thing asked for as a graphic comes back as
  clip art, 3 of 3 in `section-08` and 7 of 7 in `section-07`**, thick and flat with hard edges,
  sitting on top of the photograph.
- **The mark's colour is ALWAYS stated, and it follows G3** (ADR-125): luminous blue to cyan for a
  working signal, warm where the thing itself is warm, never red or orange unless the claim IS an
  alert. Left unstated, the renderer chose red 2 of 3.
- **The layer lives IN the scene, at frame scale** (ADR-124): the scene's perspective, reaching the
  thing it acts on, and in the owner's references spanning most of the frame. A flat graphic square
  to the camera is retired — `section-07` drew one 7 of 7 and the owner failed all seven.
- **`whisper` is the house default and `event` is earned** (ADR-125): `event` only where the feature's
  event is a thing LIGHT can show — a beam, a glow, a reach. Three whispers scored partial on richness
  alone while three events failed.
- **Two families, and a prompt declares which it is** (ADR-124): **`event`**, where the mark IS the
  picture — the event at frame scale, in perspective, reaching the thing it acts on, with a plain
  headline and no chip; and **`whisper`**, where the photograph carries the feature so richly that the
  layer is one corner badge of an icon and two words — **at the 18-px floor like every other drawn
  word; `small` is retired** (ADR-127). A middling photograph under a middling
  sticker is neither, and it is what failed.
- **The colour comes from the scene, never from the layer** (ADR-124): a chip, a leader or a badge is
  not the frame's colour source. Measured against the owner's stills: saturation 0.16 against 0.35,
  white drift 48.3% against 2.0% — and the fix moved them to 0.30 and 2.1% on the next round.
- **The mark LANDS on the subject the feature acts on** and never floats beside the product
  touching nothing; it never covers the product's own face or repaints it (ADR-094, ADR-106).
- **Nothing is drawn ON a wire, a loom or a cable — not even at one point** (ADR-128). ADR-109
  banned a mark running *along* one on 2 of 2; `section-11` asked for a bloom at ONE spot that
  explicitly *goes no further along it* and got it running along the loom on 2 of 2, so the count is
  **4 of 4** and the narrower form is retired. On a closed run the indication is the tool's OWN
  light — its lamp, its LED pool on the spot the tip is on — and nothing is drawn. The one find
  frame that asked for no drawn mark was the best of its three.
- **A mark that asserts a relation — level, straight, aligned — is drawn where the frame makes it
  true** (ADR-109). A driving posture puts the knees above the hips, and a level line over those
  thighs came back false in both rounds, 2 of 2. Draw it where the frame can hold it: along the
  product's own top surface, which stays level on a sloping seat.
- **Never a hole in a thing the buyer owns** (ADR-109): where the inside matters, the `view`
  inset, the product's own screen, or a real opened state the object has.
- Bold with a clean edge, never thin and flat and never a soft edgeless glow; no bars and no
  readings drawn on a mark (A15, G6).

## SLOT CONSTRAINTS
- **One frame, one feature.** A block of three items is three frames, each on its own item's
  line, differing on a dimension each prompt names (`mapping/pdp-dr-rules.md`, rule 10).
- **Words: the feature image's one short line, and nothing else** (ADR-106) — a figure with its
  unit as the page states it (`badge` slot), and/or a tag of two to five words in the page's own
  words (`title` slot), and the one-to-three-word labels an icon row, a chart or a call-out
  needs. Never a sentence, never a second line, never a brand or a price, never a superlative or a
  verdict word the page does not supply (the instruction's text section). G16 binds both slots.
  **The mark comes first and the words are few** (*The owner's design rules*, ADR-113). The tag
  is set once, large and bold in the lock's typeface and text colour, on a plain ground of the
  opposite value, sized for a phone (*Words and marks on a phone*). A figure over a busy part of
  the picture sits in the lock's chip; the tag never does. The words may sit on or against the
  product, never lettered onto its surface. A feature that needs no naming carries no words.
- **A drawn figure must be true of the frame it sits in** (ADR-109): a distance, a time or a
  count matches what the frame draws, or the figure stays in the page's HTML.
- **A certification, award, rating, press or platform mark** only where `content.json` names it
  (ADR-095).
- **Any screen at the far end** names its device and shows a picture, never interface text,
  notifications, bars or numbers (G6; `03-mechanism-signal` lost this 5 times).
- **Real, never worn** (*The owner's design rules*, ADR-113): nothing in the frame is old, worn,
  scratched, stained or faded.
- **G13 binds**, and casting follows the namespace.
- **Ratio** never goes into the prompt (ADR-016); the owner renders the field at the frame its
  template shows (*The section form*, *The frame*).

## NEGATIVE
```
a cut, stripped or dismantled object in a frame whose product claims it needs none of that,
a drawn word whose capital falls under 18 px on a 390-px phone, a headline running past a third
of the frame width, a plate, band or box behind a HEADLINE or a LABEL, a set that plays one
overlay form more than three times in nine, a person in a frame whose argument is the product's
own indication, range or compatibility,
a product connected to nothing, a product held by the wrong part, an action that belongs to no step
of the product's own procedure, a frame needing a third hand, a loose spare part or a coiled lead
the step does not use, a light in the gap of an open jaw,
a hand closing or holding a clip, a plug or a connector, a second copy of any lead, clip or
body the product carries only one of,
a flat graphic square to the camera pasted over the photograph, a mark asked for as arcs, a band,
a bar, a wave or a ring, a mark whose colour the prompt leaves to the renderer, red or orange on a
working signal, a state in which nothing happens, a labelled prop, a legend of icons floating in
empty sky attached to nothing, a product presented on a bench with nothing happening,
a chip that is the brightest colour in the frame, a warm cast over the whole picture,
[G6] + a sentence of copy, a second line of words, a marketing word, a mark floating beside the
product and touching nothing, a mark painted on the product, any mark drawn on a wire, a loom or a cable,
a generic glowing arc where the thing has a form of its own, red or green marks,
bars or readings on a mark, a hole cut in anything the buyer owns, a figure that contradicts
the frame, the product small or far off, the product enlarged against the hand or body beside it,
the product set out on display with nobody using it, a well-known brand's product or wordmark,
shop signs or labelled packaging in the background, a soft edgeless glow, the accent on a mark,
a ring or the product, a tag inside a chip, words lettered onto the product's surface,
a leader ending off its part, a worn, scratched, stained or faded surface
```

## BLOCK
**Criterion 3 has no passing render by the OWNER, and the record is long.** The owner has failed
every set: `section-02`, `section-03`, `section-07` (7 of 7), `section-08` (6 of 6), `section-09`
(3 of 3) and `section-10` (3 of 3) — ADR-111 to ADR-127, each buying one clause, listed in the
CHANGELOG. `section-11` is the first set graded by the model rather than the owner (ADR-011): 1
pass, 4 partial, 4 fail, and its one pass is a control, so it does not meet this criterion either.

**Criterion 1 cannot be met from the ledger as it stands**: no corpus record carries this id. The
type comes from the owner's tested instruction, so the count is the owner's to waive, as ADR-057
waived it for `03-spec-macro`.

**Criterion 2, run on paper in ADR-110**: of the four templates' fields this type takes the
`features.*` and `modes.*` items that are not an act and not a photographable state, and
`safety.image`. It contests no gallery tile. **Three reserved drafts share its ground** —
`03-mechanism-signal`, `04-proof-stat` and `03-spec-callout`, the three constructions ADR-106
sorted the owner's feature frames into — and here each is an overlay FORM, a parameter. Whether
they retire into this type waits on this type's first passing render.

## KNOWN-FLAKY
Single instances. What recurred is law and lives above; what the ledger already holds is not repeated
here.

- **Open, from the cushion rounds** (`section-02`, `section-03`): words drawn twice; an outline traced
  round a whole product; a level line over thighs that sloped, 2 of 2; an icon placed in the band a
  square crop removes; a tag at 2.7:1 against its ground.
- **Open, from the tester rounds** (`section-07` to `section-11`): the renderer gets the two bodies
  and their leads wrong — 3 of 9 by swapping them, then **5 of 9 by drawing a clip the product does
  not carry**, once by fitting one to the receiver, which has no leads. **Naming each body by what
  it carries was tried in all nine prompts of `section-11` and the rate went up**, so that answer is
  spent (ADR-128). What is left: the constructions that lose the parts are retired above, and the
  lever named by ADR-126, ADR-127 and ADR-128 alike is a usage photograph, which is not on disk.
  Lettering every labelled prop is answered by keeping labelled props out of frame (ADR-125).

## CHANGELOG
Each entry is one line; the reasoning is in `decisions/log.md` and the renders in
`eval/render-tests.jsonl`.
- 0.13 (2026-10-06, ADR-130): the owner allows it all — `sets/section-12/` is approved and
  committed, and the FIGURE CARD is named as this type's own device, distinct from the gallery's
  flat chip form, which is left alone.
- 0.12 (2026-10-06, ADR-129): a set spans the overlay forms — at least four of six, none more
  than three times — and a feature frame is product-led, half of them in a studio; ADR-128's
  no-plate rule narrows to a headline and a label, because a figure keeps the chip the instruction
  legislates and an icon keeps its box.
- 0.11 (2026-10-05, ADR-128): the 18-px floor held 9 of 9 and the closed loom held at every acting
  point; the parts got worse, 5 of 9, so the constructions that lose them are retired instead of
  re-worded — no hand on a clip, nothing drawn on a loom, no plate behind a word, a third of the
  frame width as a ceiling.
- 0.10 (2026-10-05, ADR-127): never show the work done the way the product makes unnecessary — a find
  frame cut open the loom this tool traces through; what is hidden is shown by the indication and a
  mark pointing INTO the closed object; every drawn word meets an 18-px floor on a 390-px phone,
  measured at 8.3; `small` leaves the `whisper` family; a feature slot gets three options.
- 0.9 (2026-10-05, ADR-126): READ the product first — PARTS, CONNECTIONS, GRIP, SEQUENCE, THE
  INDICATION — and make every frame one named step of its own procedure, the product working in it,
  two hands each with a job, only the step's props, a light at a connection reading as indication.
- 0.8 (2026-10-05, ADR-125): the mark is LIGHT named as a physical thing, never a graphic (clip art
  3 of 3); its colour is always stated, G3 (red chosen 2 of 3 when unstated); one event to a frame;
  no labelled props; `whisper` is the default.
- 0.7 (2026-10-05, ADR-124): derive before drawing — THE EVENT, THE FRAME, THE LAYER; the layer lives
  in the scene's perspective at frame scale, in one of two families; the colour comes from the scene.
- 0.1 to 0.6 (2026-09-18 to 2026-09-20, ADR-110 to ADR-115): drafted from the owner's image
  instruction in its FEATURES mode and taken through the owner's design rules, the derived
  person at work, and named garments. Full text in `decisions/log.md`, which is the history.
