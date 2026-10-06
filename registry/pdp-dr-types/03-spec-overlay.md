---
id: 03-spec-overlay
step: 3
job: spec
device: overlay
version: "0.19"
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
- **A PROMPT NAMES ONLY A PRODUCT THE OWNER CAN ATTACH A PHOTOGRAPH OF** (ADR-131), and the set
  asks him WHICH before it is written. Measured on `section-12`: **2 of 2** frames of the product he
  had a photograph of drew the right product, **0 of 6** frames of the two he did not. Note the test
  carefully: no product photograph for any of the three is in `image-library-assets/` — he attaches
  it by hand at render time from a library this lane cannot see, so the repo cannot answer the
  question and only he can. Every prompt ends with *Use the attached product photo as the exact
  reference*, so naming a product he has no photo of sends the renderer to whatever photo IS
  attached, and it draws that instead.
- **A prompt never asserts anatomy nobody has seen** (ADR-131). No display, screen, dial, lamp,
  port, button or indicator is named unless it is visible in the attached photograph. Where the
  brief's copy names a part the photograph does not show, **the photograph wins** — ADR-120 ruled
  that for how a product works and this widens it to what it IS. Measured: a colour display grafted
  onto a receiver pen that has none 1 of 1, two `view` frames with no screen to show 2 of 2, and a
  re-run that invented a reading of `14.40 V` on an invented screen.
- **The `view` form requires a screen in the photograph.** It is the one form whose whole subject is
  anatomy, and with no screen it returns a plain product shot, 3 of 3.
- **A frame never shows the work being done the way the product makes unnecessary** — and this
  reaches the DRAWN LAYER, not only the photograph (ADR-131). An icon of what the product fixes
  shows the FAULT, never the repair method the product replaces: asked for an icon of *wires*, the
  renderer drew a wire stripped back to bare frayed strands, which is the one thing this tool exists
  not to need, 1 of 1. Where the claim
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

## FLOW

**The owner's own eight steps, 2026-10-06, and they run as written** (ADR-134, ADR-111). A set's
notes show the work at each step, so the thinking can be corrected instead of the prompt.

`Content → Extract feature → Choose one message → Visual proof → Scene → Hierarchy → Minimal copy/marks → Prompt`

**Step 0, before his step 1: is the chosen claim an OBJECT claim or a DELIVERY claim?** (ADR-136).
An OBJECT claim — what the thing is made of, how light it is, which part it has — is proved by
photographing the object, and the object then fills the frame: his `ULTRA-LIGHT`, his
`Non-Reactive Surface`. A DELIVERY claim — what you see, hear, find, cover, save — is proved by
photographing **what comes out**, and the object is the ANCHOR, not the hero. Measured on one round
of eleven, same product and same day: the one block of three that was an object claim returned
**36.4** colourfulness at value **0.64**; the two delivery blocks, built as object claims, returned
**9.3 to 22.7** against the owner's median of 39.1. **A delivery claim built as an object claim is
why a set reads flat however varied its compositions are** — that round's closest composition pair
was 30.8 against his own 30.3 and it failed anyway.

1. **Read the content and split it** into **feature · action · context · benefit**.
2. **Choose ONE message.** *Không cố nhồi toàn bộ content vào một ảnh.* **It may be a detail inside
   the copy rather than the block's title** — the owner's own example takes *Ultra-Flexible
   Gooseneck* out of a block whose title is about tracing behind panels.
3. **Turn the claim into VISUAL PROOF.** For each claim word, ask what would have to be photographed
   for it to be undeniable: *flexible* → the gooseneck is visibly bent; *crowded wires* → a genuinely
   crowded bundle; *reach tight spaces* → the probe threaded into a narrow gap. **Name the physical
   fact, never the adjective.**
4. **Build the scene**: the environment, then the hero object, the action, the background and the
   minor props.
5. **Set the visual hierarchy explicitly**: the product is the most prominent thing, the feature is
   seen at once, everything else is demoted.
6. **Cut the copy to the minimum**: ONE short headline, **or** one Apple-style icon callout, never
   both and never more. The rest is carried by the photograph.
   **A drawn word never restates a word the page already prints** (ADR-136). The LP2 features block
   prints the headline, the body copy and a pill beside the image, and a set drew that pill's exact
   string into 11 of 11 frames. Counted across his 21 references: **4 carry a word headline, 8 lead
   with a FIGURE and its unit, 5 carry an icon with a short label, 4 carry no lettering at all.**
   His own instructions say it twice — *text is the minimum the picture cannot say*, *a chip
   restating title or copy is cut*. **So the line is EARNED, by a figure or a unit the block's copy
   does not print, and a set of six letters in at most TWO frames.** The slot rule is unchanged: one
   short line is allowed (`mapping/pdp-dr-rules.md`, *Slot kinds*). What is banned is the echo.
   **EVERY FRAME CARRIES EXACTLY ONE VISUAL CUE, AND ZERO IS A FAILURE** (ADR-135). The cue is a
   drawn mark, **or** an Apple-style icon callout, **or** the product's own indication made
   unmistakable. *Minimal is not none*: a set shipped with no cue at all in 9 of 9 frames was
   rejected on sight, against 16 of the owner's 17 references that carry one. More than one is the
   *callout dày* step 8 bans. **A cue is a mark or an icon, never a caption** (ADR-136): a frame
   that carries no words still owes its cue, and a headline does not discharge it.
7. **Keep fidelity to the reference photo** — shape, colour, structure. The model may still get
   small text and logos wrong, which is a grading problem, not a prompt one.
8. **State the art direction and the negative constraints**: white seamless, daylight on location,
   or studio — **and the ground's VALUE is read off the PRODUCT, never chosen as a style**
   (ADR-136, owner: *tôi không ưu tiên tone tối trừ khi sản phẩm đặc thù*). A dark ground is allowed
   only where the product is saturated or emits: his orange radio measures **44.1** colourfulness on
   one, his telescope holds a galaxy, his tent holds a lamp. A matte-black, non-emitting product on
   a dark ground returns the picture nothing — 5 of 11 frames at value ≤ 0.22 against his median of
   0.46, and the round's two worst-textured frames, 6.6 and 9.2 against his 27.4, were both dark
   studio. Where the product is dark and dead, the third direction is **daylight on location**;
   **one accent colour — and that binds the DRAWN LAYER, not the photograph** (ADR-135): the scene
   keeps the colour of its own world. Read as an instruction to desaturate the picture it cost 22.3
   colourfulness against the owner's 43.5, the lowest of five rounds. Few words. **Banned: a badge,
   a heavy lettered callout, a dense infographic, a crowd of icons.**

This supersedes the derivation order that stood before it, and steps 5 and 8 replace two things this
type legislated wrong: the ground was never the fault, the HIERARCHY was, and the form spread of
ADR-129 is suspended because step 8 bans three of its six forms outright.

## FRAME

**The photograph is legislated before the drawn layer, and a frame is graded as a photograph
first** (ADR-132). A frame that would be a poor photograph with its layer removed is a fail,
whatever the layer does. Three decisions in a row — ADR-129, ADR-130, ADR-131 — legislated the
overlay and wrote no clause about the picture under it, and the owner failed all nine of
`section-12`: *"tất cả các ảnh mới đều tệ … chất lượng quá tệ, kém hơn cả các ảnh tôi làm cách đây
nửa năm trước với những model AI sơ khai"*. Measured against his own seventeen reference stills
with `scripts/frame-colour.py`: colourfulness **25.6 against 43.5**, texture **15.9 against 24.6**,
saturation **0.21 against 0.35**, warmth **−4.6 against +9.2**. The richest of the nine was below
his median.

- **FIRST, CLASSIFY THE BLOCK: does its title name an EVENT or an ATTRIBUTE?** (ADR-133). This is
  the first step of writing a feature image and it is not visual. **An attribute can only be shown
  by photographing the object, so every frame becomes a packshot and they converge**; an event has a
  place, a moment and a hand, so each one forces a different scene. Measured on the same product,
  the same law and the same day: nine frames from three INVENTED attribute lines had a closest
  composition pair of **15.9**; nine from the page's own three EVENT lines had **42.8**, further
  apart than the owner's own two most-alike references at 30.3. Where a block names an attribute,
  the event comes from its copy's verb or the set is told it cannot have variety.
- **A frame whose scene contradicts its own block is void**, however good the picture (ADR-133): the
  `icon` frame for *Trace Through Trim Panels* came back showing a dash with its trim already
  removed. Grade the scene against the block's claim before anything else.
- **The product is the most READABLE thing in the frame, not necessarily the largest** (ADR-136,
  narrowing what stood here). Sharp, lit, unobstructed, in its working configuration and nameable in
  every crop — **never laid flat, never dark-on-dark, never a components lay-out.** It is the frame's
  ANCHOR. Whether it is also the frame's SUBJECT is decided by FLOW step 0: on an OBJECT claim it
  is, and it fills the frame; on a DELIVERY claim the subject is what comes out of it, and the
  product may be small. **Unreadable is the fault; small is not.** His compact camera sits at
  roughly a seventh of the panorama frame and is perfectly readable; his peacock frame carries no
  product at all and still sells the sensor. The clause this replaces — *the largest, brightest,
  best-resolved thing in frame ... roughly a third to a half in the owner's references* — was
  measured on his packshot frames only, and reading it as a law for every frame is what kept eleven
  renders at a hand holding a tool.
- **The product is in its WORKING CONFIGURATION, assembled.** Two bodies are connected and doing the
  job, not laid side by side like a parts list. His dark-studio frames are not voids: the phone is
  mounted on the telescope, the pan is on the hob with food in it.
- **A studio frame still has something behind it that ARGUES** — the world the product serves,
  defocused; a graduated ground that gives the product form; or a graphic ground that means
  something, as his technical grid does — **and a plain white seamless is equally allowed**
  (ADR-134: the owner's art direction is *nền trắng / studio / contextual*). **But a studio ground
  still carries a WORLD** (ADR-135, restoring what ADR-134 over-relaxed): in all three directions the
  product is doing something and the place it belongs to is implied — his own `ULTRA-LIGHT` white
  seamless implies a hand and a pocket, and a ground with nothing happening on it was rejected 9 of
  9. **The ground was never the fault; the HIERARCHY and the EMPTINESS were** — a small dark product lying flat on it. ADR-132 banned the plain ground and that
  was an over-correction, narrowed here. The clause *with no place and no person* stays retired,
  because it forbade the hierarchy too.
- **The scene names at least one real saturated colour that BELONGS to it** (ADR-136). Measured:
  a round median of 16.2 colourfulness against his 39.1, with 9 of 11 frames below his 10th
  percentile of 19.1 — and the prompts had asked for it, specifying *wrapped edge to edge in
  unbroken black harness tape* in every frame of a block, when a real automotive harness is a bundle
  of red, yellow, blue and green wires. Where the world has a colour, the prompt NAMES it; where it
  has none, **the place is re-chosen rather than the picture graded**. The accent rule binds the
  drawn layer and has never bound the world (ADR-135).
- **Every frame of his has a subject that proves the claim** — mountains behind the camera, a galaxy
  behind the telescope, a peacock feather for the resolution, a scallop searing for the heat — and
  the drawn device is the smallest part of the picture, often a corner element.
- **No two frames in a set share a composition** (ADR-132). Checked with a 16×16 luma signature: any
  pair under **25** is a repeat. The failed round had three pairs at 10.7, 14.7 and 19.1, closer to
  each other than any two of the owner's seventeen, whose nearest pair is 30.3.
- **A round is measured against the owner's corpus when it is graded**, not only clause by clause:
  `scripts/frame-colour.py` on the renders must land inside his band on colourfulness and texture,
  and a round below it fails even if every clause matched. Grading a render against the prompt that
  made it is what let ADR-131 call this round the cleanest this type had had.

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
- **ONE drawn line to a frame, and that line is the only lettering** (ADR-133, and
  `registry/pdp-dr-instruction.md` has said so since ADR-106: *a feature image may carry one short
  line and nothing else*). **A row of icons goes UNLABELLED and the one line names what they are** —
  the owner's `7 NOAA CHANNELS` over three unlabelled weather icons is the pattern. `callout` may
  point with leaders but only one of them carries words. Measured: the renderer divides the
  available size by the number of things it must letter — the two three-label `callout` frames came
  back at **7.4 and 12.6 px**, the two smallest drawn words this type has produced, the three-label
  `icon` frames at 19.2 and 14.4, and the single-line `tag` frames at 17.0 and 20.9. The owner's own
  corpus agrees: his frames that pair icons with ONE line carry his largest words, and the one frame
  that labels three icons separately carries his smallest.
- **ONE word-form to a SET** (ADR-133). The only round that ever held the floor was `section-11`,
  nine prompts carrying one `tag` clause: **9 of 9, 19.6 to 35.3 px**. Every mixed-form set since has
  failed. The device spread of ADR-129 survives, because `mark` and `view` carry no words at all.
- **EVERY form's clause carries the size rule, not just `tag`'s** (ADR-131). A headline, a label
  under an icon, a call-out label and a figure in its card each state their height as a share of the
  picture, and 18 px is the floor for all of them. ADR-127 bought the floor and wrote it into the
  `tag` clause; ADR-129 added five more forms and carried it into none, and the words went straight
  back under: **11.3, 14.4, 15.7 and 16.5 px, 4 of 4**, the callout labels the smallest drawn word
  since the badge ADR-127 retired. **A floor bought once is lost the moment a form is written
  without it.**
- **On a light ground the words take a dark HALO, not an edge** (ADR-131). *A soft dark edge*
  measured **2.2:1** against the 4.5 target on a white wall. The clause names a dark halo wide
  enough to separate the letters from the ground, and the contrast is read with
  `scripts/text-size.py` before grading.
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
- **Where the claim is about something HIDDEN, the cue is a WINDOW onto the hidden state, never a
  symbol of the medium** (ADR-136). A set drew concentric arcs leaving the speaker grille into empty
  air in 3 of 3 frames: they say the product has a speaker, they never reach the loom, and they
  prove nothing about finding a break. His device is a window — the feather magnified in a disc
  beside the monocular, the ridge inside the binocular's field, the galaxy inside the lens. The
  window shows the state the buyer cannot see, AT the place the product is pointing: for a tester,
  the copper inside the loom, whole along its length and broken at the one point under the tip.
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
a product laid flat, dark on a dark ground, or small in its own frame, a components lay-out of a
product that assembles, an empty floor offered as a studio ground, two frames of one set sharing
a composition, a round below the owner's corpus band on colourfulness or texture,
a frame with no visual cue at all, a photograph desaturated to serve the accent rule, a studio
ground with nothing happening on it,
a badge, a heavy lettered callout, a dense infographic, a crowd of icons, more than one accent
colour, a frame with no stated visual hierarchy, an adjective asked for in place of the physical
fact that proves it, a whole content block crammed into one image,
a second line of lettering in a feature image, a row of icons each with its own label, a set
that letters in more than one form, a frame whose scene contradicts the block it illustrates,
a drawn word whose capital falls under 18 px on a 390-px phone, a drawn word whose clause states
no size, a drawn word under 4.5:1 against the ground it sits on, a headline running past a third
of the frame width, a plate, band or box behind a HEADLINE or a LABEL, a set that plays one
overlay form more than three times in nine, a person in a frame whose argument is the product's
own indication, range or compatibility, a product named in a prompt with no photograph of it on
disk, a display, screen, dial, lamp or port named that the attached photograph does not show,
a `view` frame of a product with no screen, an icon drawing the repair method the product
makes unnecessary,
a product connected to nothing, a product held by the wrong part, an action that belongs to no step
of the product's own procedure, a frame needing a third hand, a loose spare part or a coiled lead
the step does not use, a light in the gap of an open jaw,
a hand closing or holding a clip, a plug or a connector, a second copy of any lead, clip or
body the product carries only one of,
a delivery claim built as a packshot, a frame of a delivery claim in which the product's own output
is nowhere, a dark ground under a matte product that neither emits nor carries a saturated colour,
a scene with no real saturated colour named in it, a drawn word that restates a word the page
already prints beside the image, a set of six lettering in more than two frames, a caption offered
in place of the frame's one cue, a symbol of the medium where the claim is about a hidden state,
a flat graphic square to the camera pasted over the photograph, a mark asked for as arcs, a band,
a bar, a wave or a ring, a mark whose colour the prompt leaves to the renderer, red or orange on a
working signal, a state in which nothing happens, a labelled prop, a legend of icons floating in
empty sky attached to nothing, a product presented on a bench with nothing happening,
a chip that is the brightest colour in the frame, a warm cast over the whole picture,
[G6] + a sentence of copy, a second line of words, a marketing word, a mark floating beside the
product and touching nothing, a mark painted on the product, any mark drawn on a wire, a loom or a cable,
a generic glowing arc where the thing has a form of its own, red or green marks,
bars or readings on a mark, a hole cut in anything the buyer owns, a figure that contradicts
the frame, the product unreadable — soft, unlit, obstructed or unnameable in its crop — the product
enlarged against the hand or body beside it,
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
- 0.19 (2026-10-06, ADR-136): the compositions reached his own corpus — closest pair 30.8 against
  his 30.3 — and the pictures still read flat, so the fault was never variety. A claim is classified
  OBJECT or DELIVERY before the frame is built, and a delivery claim is proved by photographing what
  comes OUT; the product is the most READABLE thing, not the largest; the ground's value is read off
  the product, so a dark ground needs a product that emits or is saturated; the scene names a real
  colour; a drawn word never restates the pill the page already prints, and a set of six letters in
  at most two frames; a hidden state is shown through a WINDOW, not a symbol of the medium.
- 0.18 (2026-10-06, ADR-135): the flow fixed the thinking and this lane emptied the picture — every
  frame carries exactly ONE visual cue and zero is a failure (an either/or was read as a neither);
  `1 màu nhấn` binds the drawn layer, not the photograph, which lost 4 points of colourfulness to
  the misreading; and a studio ground still carries a world.
- 0.17 (2026-10-06, ADR-134): the owner's eight-step flow becomes the skeleton, verbatim — read the
  content, choose ONE message, turn each claim word into a visual proof, build the scene, state the
  hierarchy, cut to one headline or one icon callout, keep fidelity, declare the art direction and
  the negative constraints. It corrects two things this type had wrong: the plain ground is allowed
  again because the fault was hierarchy, and the form spread is suspended because his constraints
  ban three of the six forms.
- 0.16 (2026-10-06, ADR-133): classify the block first — an EVENT line makes nine different
  pictures, an ATTRIBUTE line makes packshots that converge (15.9 against 42.8, same product, same
  day); ONE drawn line to a frame and ONE word-form to a set, which the instruction has said since
  ADR-106 and this type's callout and icon forms broke; a frame that contradicts its own block is
  void.
- 0.15 (2026-10-06, ADR-132): the owner failed all nine — three decisions in a row legislated the
  drawn layer and none the photograph. A new FRAME section puts the picture first: the product is
  the subject, assembled and working, a studio ground still argues, no two frames share a
  composition, and a round is measured against the owner's corpus. Measured gap: colourfulness 25.6
  against his 43.5, texture 15.9 against 24.6, closest composition pair 10.7 against his 30.3.
- 0.14 (2026-10-06, ADR-131): all six overlay forms landed first time and six of nine frames drew
  the WRONG product — a prompt names only a product whose photograph is on disk (2 of 2 against 0 of
  6) and never asserts anatomy nobody has seen; every form's clause carries the size rule, because
  adding five forms without it put the words back under the floor 4 of 4; a dark halo replaces the
  soft edge; the drawn layer may not show the repair the product makes unnecessary.
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
