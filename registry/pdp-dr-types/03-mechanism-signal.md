---
id: 03-mechanism-signal
step: 3
job: mechanism
device: signal
version: "0.7"
status: reserved
replaced_by: null
channels: [landing-page, marketplace]
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
blocked_by: "Criterion 1: four distinct sources of the five SPEC 6.3 asks. Criterion 2, the router-confusion test against 03-mechanism-contact and 03-use-grid, is unrun. Criterion 3: the owner failed all five renders of set 01 and all four of set 02 on 2026-09-17, and 0.5 has no render."
---

# 03-mechanism-signal — PDP-DR DRAFT

Promotion status: **4 distinct sources, 10 observations — criterion 1 is one source short.**
Drafted 2026-09-17 on the owner's instruction, after the owner rejected a mapping that proved a
Wi-Fi extender's reach with a lineup of product photos and named two ClikTric pages whose feature
images draw the invisible instead. Every frame below was opened before it was written (ADR-092).
**The owner has failed every render this type has produced** — set 01, set 02 and set 04 — and the
CHANGELOG says what each round took.

| source | frame | what is drawn | the far end | the product |
|---|---|---|---|---|
| snapi-stud | img-08 | arcs into three wall cutaways | timber, cables, rebar in the wall | yes |
| snapi-stud | img-18 | rings; cutaway strata below | four targets at labelled depths | yes |
| pawdi-cas | img-11 | a dotted sight line, a reticle | a smart lock across the hall | yes |
| pawdi-cas | img-04 | brackets, a waveform, notifications | a dog, a crying infant | **no** |
| pawdi-cas | img-06 | a red outline, a siren bolt | an intruder, a notification | yes |
| pawdi-cas | img-09 | a zone rectangle, a ghosted walker | the walker, a notification | yes |
| pawdi-cas | img-15 | two speech bubbles | a child across the room | yes |
| ezy-talux | img-10 | a grey waveform before, an orange one after | none, the signal itself | yes |
| cliktric | lp00412-4 | curved arrows between two devices | a phone showing the photo | yes |
| cliktric | lp00132-3 | WiFi arcs both sides, iOS and Android marks | named by marks only | yes |

The two ClikTric pages sell one product and are one source (batch 2026-09-17-A).

**The owner's four signal frames of 2026-09-18** (ADR-106), from the twelve of that audit: cited
by sha256, not in the assets tree, not ledgered, and NOT counted toward criterion 1.

| sha256 | product | what is drawn | the subject it lands on | the product |
|---|---|---|---|---|
| `cb0c18d8` | music boxing pad | notes on a staff, equaliser bars, a halo at the strike | the boxer's fist | yes |
| `455e0e9a` | ultrasonic repeller | a frequency chart keyed to four animal silhouettes | the animals it targets | yes |
| `e653edfc` | baby sound machine | a beam to a rounded icon tile of the sound it plays | the room it plays into | yes |
| `459eab20` | translation earbud | four speech bubbles, and a shield with its figure | the ear, and the speech | yes |

**Counted across all fourteen:** something invisible is drawn 14 of 14; the mark is the thing
itself in the owner's four, 4 of 4, landing on the subject 4 of 4, with a glowing arc or arrow 0
of 4 (0 of 12 across the whole audit set); the far end is in frame 8 of 10 in the corpus and the
product 9 of 10; the result is phone interface text 4 of 10, which G6 keeps out; a barrier is cut
open 2 of 10, both of them `snapi-stud`'s WALL; blue carries a working signal 7 of 10 and red an
alert 3 of 10, and this file draws a working signal only (G3); words are in frame 10 of 10.

## PURPOSE
Show what the product does at a distance when that action cannot be photographed: a signal it
sends or senses, drawn as luminous marks over an editorial photograph in which the product is
the anchor and in use. The frame answers *"how does it get there"* — through a wall, across a
room, into a phone — and the far end shows that it arrived. It must read in three seconds.

**The mark is the thing itself** (ADR-106): sound drawn as notes or as a spoken bubble, a
frequency as a chart keyed to what it acts on, a lure as the paths the insects fly. **It lands on
or inside the subject the product acts on**, never floating beside the product touching nothing.

## TRIGGER
use_when: >
  The copy's claim is a signal the product sends or senses and nobody can see: WiFi or
  Bluetooth reach, coverage through walls or floors, a wireless link to a phone or a TV,
  detection of a person, a sound or a hidden object. A gallery mechanism tile, or a feature,
  problem or support section whose copy names what the signal reaches or passes through.
  Take 03-mechanism-contact when the product touches a body at one place;
  03-use-grid when the argument is the range of hosts rather than the link to them;
  03-spec-macro when the claim is the product's own part rather than what that part sends;
  04-proof-stat when the claim IS a figure and the figure is the subject of the frame;
  03-spec-callout when the claim is several capabilities pinned as labels beside the product.
  Never a lineup of products: a still cannot show a difference nobody can see.

## SKELETON
**The owner's feature-image OUTPUT FORMAT, with the mark added** (ADR-101). The steps are the order
of the paragraph, not labels in it; each names the PARTS or MARKS entry that defines it once.

```
TYPE: 03-mechanism-signal v0.7

Each prompt is one natural paragraph, starting directly with the image prompt, with no labels
or JSON, in this order:
  1. The photograph: its camera and layout, the product BY NAME, what it is doing, where.
                                                                         -> PARTS/opening
  2. The product: the nearest and sharpest object in the frame, whole and unobstructed, at
     the size its host gives it, with the camera close enough to read it. -> PARTS/anchor
  3. The far end: what the signal reaches or is stopped short of, large and in sharp focus,
     showing the result by itself; a barrier only where the claim passes through one.
                                                                         -> PARTS/far-end, PARTS/barrier
  4. The mark, in a sentence of its own: the invisible thing drawn in its own form, landing on
     the subject it acts on, and what it shows; then the set's mark sentence.
                                                                         -> PARTS/path, MARKS/signal
  5. Light and background: the set's two sentences.                      -> PARTS/ground
  6. Words and the corner: the set's sentence; a gallery tile adds its title sentences, and a
     feature image may add its one short line.                           -> SLOT CONSTRAINTS
  7. "Use the attached product photo as the exact reference."            -> PARTS/form (G1)

Optional: a person as none, a partial hand, a body or a face where it is relevant; a pet only
where the product serves one.

Always end with this exact sentence:
"Do not change anything related to the original product, including screen, buttons, display,
interface, ports, technical indicators, color, shape, proportions, dimensions, or functionality."
```

## PARTS

**`form`** — the owner's feature-image instruction (`~/Downloads/feature image.txt`, ADR-100,
ADR-101) sets the prompt's form, and from 0.5 the skeleton is its output format: one natural
paragraph that starts with the picture, with no labels and no JSON, ending with this sentence
word for word:

```
Do not change anything related to the original product, including screen, buttons, display, interface, ports, technical indicators, color, shape, proportions, dimensions, or functionality.
```

- **The LP2 product block is left out, as the owner's trial** (ADR-101). G1's obligation stays in
  one sentence just before the closing one: `Use the attached product photo as the exact
  reference.`
- The paragraph says where a thing is and never names a region (adapter Rule 1b).
- The signal gets a sentence of its own; a mark buried in another clause is the one that vanishes
  (adapter Rule 7). A sentence the set shares is written once, word for word (LP2 rule 4).

**`opening`** — the first sentence says what the photograph is: the camera, who is there, what
they are doing, and where.
- The camera comes from the instruction's list: wide lifestyle, 45-degree usage angle, front-on
  eye level, over-the-shoulder, partial hand, close-up, handheld. The layout is one of its three:
  a **usage scene** for a product in a hand, an **in-environment installation** for a fixed one, or
  a **feature demonstration** with nobody touching it.
- The place is the one the page's use happens in, and it explains why the product matters.
- **The product is named** as the page names it — "the portable Bluetooth speaker" — and G2 keeps
  its looks to the photograph. 0.3 wrote only "the product" and 2 of 4 renders invented one, once
  as a well-known brand's camera with its wordmark.

**`anchor`** — the product, in use or installed, is the visual anchor: **the nearest and sharpest
object in the frame, whole and unobstructed, at the size its host gives it.**
- **Scale comes from the host, never from a share of the frame** (ADR-106). A hand, an ear, a
  body, a seat, a pane, a wall or a plant in frame fixes how big the product is, and the prompt
  moves the CAMERA: *shot close enough that the product reads whole*. A share is named ONLY on a
  studio or a graphic ground, where nothing fixes the size, and there it is 40–60%.
- **Measured** (boxes by eye): the owner's twelve feature frames run 20–75% of the frame height,
  median ~47%, always agreeing with the host — the same earbud is 20% on an ear and 48% alone on a
  lit map. 0.5's single *"about 40% of the frame height"* made a charging case the size of a lunch
  box, and the owner failed it: *"tai nghe quá to, đèn led quá to"*. Earlier rounds measured
  7.8%/25.3% in the two references against 1.6–3.2% (0.2) and 5.9–16.0% (0.3), so size was
  necessary and never enough. **Set 04 held the scale 6 of 6, the first set that did.**
- **A thin product is framed on its working END** (ADR-109) — the lens and its ring of lamps, the
  connector, the head. Set 04's endoscope came back as a black cable in a hand, 1 of 1.
- **In use**: held, pressed, plugged in, installed, or working beside the person it serves. **A
  fixed product stays installed** (G7-X); 0.2 kept it there 4 of 5.
- **The marks leave from beside the part that sends and never lie on the product's face**: off it
  15 of 15 renders; the owner's own runs painted a diagram on it 4 times (ADR-094).

**`far-end`** — what the signal reaches, and only what the page names, in use, **large and sharp**:
held in the other hand or set across the frame from the product, as the phone is in lp00412-4,
where it fills about half the frame height. 0.3 blurred it and set 02's came back small and soft
4 of 4.
- It shows the result by itself: a person streaming, a device working, a room in use — never a
  notification or interface text. A screen at the far end carries a photograph (G6); 0.2 got a
  broadcast's score bar on 1 of 3 screens, set 04 an icon and a reading on 1 of 1.
- **The screen sentence names the far end's device, never "any screen".** Written for the whole
  scene it gave the PRODUCT a display with a picture on it, 2 of 4.

**`barrier`** — only where the copy's claim is passing THROUGH something, and **only building
fabric is ever cut** (ADR-109).
- **Cut, as a clean squared window**: a wall, a floor, a ceiling, a duct run, a pipe chase. A buyer
  accepts that a building is opened to be worked on. snapi-stud cut the wall both times it made
  this claim, and no frame in the corpus drew it on a closed wall.
- **Never cut a thing the buyer owns**: a car, a mattress, an appliance, a bag, a case, a piece of
  furniture. **Measured, 3 of 4 cuts this library asked for came back as damage** — set 04's bonnet
  as a torn hole with peeled metal, set 04's mattress as a torn and stained hole with frayed fibres,
  and 0.2's hallway cut as a brick recess the rings ran past. The owner failed both of set 04's on
  sight: *"nhìn như xe hỏng đệm hỏng"*. On a marketplace frame a hole also reads as damage the
  product did.
- **Where the inside of a possession is the argument**, take one of three routes instead: an INSET,
  a separate rounded window beside the product and plainly a drawn panel; the product's own SCREEN
  where it has one — set 04's endoscope did this and kept G6, the set's one clear win; or a REAL
  OPENED STATE the object has, a propped bonnet, an undone zip, a lifted lid.

**`path`** — a parameter, and the copy picks it. **The first question is what the invisible thing
IS, and the mark draws that** (ADR-106); the symbol families below are the case where the thing
is a link or a reach. Every form lands on or inside the subject it acts on.

- `thing-itself` — the invisible thing in its own form: music as notes, speech as a bubble, a
  frequency as a chart keyed to what it targets, a played sound as the icon of what it plays. The
  owner's audit frames 4 of 4; **untested here**.
- `subject-paths` — the paths the subjects take: insects into an intake, air into a vent. Set 04
  drew them as broad white wind streaks with the insects sitting on them, 1 of 1.
- `through-view` — what the user sees, shown where the product really shows it: a screen, an
  eyepiece, a viewfinder. G6 keeps interface text out, so a screen carries a photograph. **Set 04's
  one clear win, 1 of 1.**
- `halo` — a ring of light on the subject where the product reaches it. **It has an edge**: set
  04's came back as an edgeless blur, 1 of 1, and the owner's `525f1c50` holds one that works.

**A mark never runs ALONG a wire, a cable or a cord** (ADR-109). It lands at the ends — at the
port, at the clamp, at the cells. Twice a mark drawn along a line became the line: set 02's
continuous trail read as a tangled wire, and set 04's charge band turned a cable into a glowing
tube, **2 of 2**.

**The link family, each form a symbol a buyer already knows, drawn as the owner's references draw
it:**
- `arcs` — the Wi-Fi symbol: three or four smooth concentric arcs around a small dot, glowing,
  beside the sending part, on one side or both (lp00132-3). Reach and emission, 3 of 10. Set 02
  drew it cleanly, 1 of 1.
- `line` — one or two broad, smooth, sweeping arrows with a blue gradient and soft motion streaks,
  from the product to the far end, one each way for a two-way link (lp00412-4). A link or a
  transfer, 2 of 10. **Never a "trail", and never dotted**: dotted trails came back as strings of
  glowing beads 2 of 2 and a continuous trail as a looping wire 1 of 1.
- `rings` — glowing rings spreading from the product through the space. Coverage; snapi-18 only.
- 0.2 rendered each form as named, 5 of 5, but thin and flat, and they read as weak.

**`ground`** — the real place the claim is about, **light in tone and simple** — a plain wall, a
bare desk, or a softly blurred place behind both ends — under bright, directional daylight.
Nothing in it competes with the product, the far end or the signal (lp00412-4's plain wall,
lp00132-3's bare desk). The background may blur; the far end never does.
- **The place is named so that it carries no signage** (ADR-109). 2 of set 04's 6 frames brought
  print into a frame whose only allowed words are its one line — a shopping street gave shop signs
  and a well-known coffee chain's sign, a sink cupboard gave labelled bottles and a printed box.
  Name a place with no shopfronts, no labelled packaging and no hoardings.
- **The fault 0.2 wrote into its lock was a flat frame** — every surface lit alike, "nothing
  saturated". Contrast measured 0.265/0.275 in the references against 0.147–0.206 in the renders,
  and saturation did not separate them, so the fix is light and focus rather than colour. Set 04
  confirmed it from the other side: `scripts/frame-colour.py` puts 5 of its 6 frames inside the
  owner's own band and the owner failed them all on construction.

## MARKS

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `signal` | the invisible thing drawn in its own form — notes, a spoken bubble, a chart keyed to what it targets, the subjects' own paths, a halo on the subject, the view through the product — or, where the claim is a link, one known symbol: Wi-Fi arcs with their dot, broad sweeping arrows, rings. Bold enough to read at a glance, and it LANDS on the subject it acts on | luminous blue, which may shade toward cyan (G3: working); a warm glow where the thing itself is warm — the owner's `525f1c50` halo | one family to a frame | the thing itself: owner audit 4 of 4, landing on the subject 4 of 4, glowing arcs 0 of 12 (ADR-106) · corpus 10 of 10 draw something invisible, blue on 7 · 0.2's thin flat blue: 5 renders, owner fail · 0.3's glowing trails read as beads or wire 3 of 3, its arcs clean 1 of 1, owner fail 4 of 4 |

- **Bold and luminous, never thin and flat**, and never a soft edgeless glow: 0.2's "thin, clean"
  marks and set 04's blurred halo both failed.
- **It lands on the subject**, and **the mark never covers the product's own face or repaints it**
  (the owner's runs painted a diagram on it 4 times, ADR-094). A mark that floats beside the
  product touching nothing is the fault 0.5 wrote into all six prompts of set 03.
- **One family to a frame, one colour.** `pawdi-cas`'s detection frames stack brackets, sirens and
  notifications into one picture and are the busiest of the ten; set 04 put arcs and a beam in one
  frame, 1 of 1.
- **Never red, and never a flat green** (G3): red is pain, green is the verdict, and this file
  stops the shade at cyan.
- **No bars and no figures on the marks** — a reading, which A15 and G6 both reach.

## SLOT CONSTRAINTS
- **The prompt budget** (ADR-013, ADR-015): a clause earns its place after a render failed
  without it. Every clause here carries its count.
- **Length.** A prompt stays within 1,800 characters with the reference and closing sentences in
  it; without the block, most run well under.
- **Words.**
  - In the product card's gallery: a title of 2–5 words saying what the signal does, in the
    buyer's words, written as a sentence of the paragraph.
  - One 1–3 word label beside the far end, only where the far end is not obvious; it counts as
    the tile's chip.
  - **A drawn figure must be true of the frame it sits in** (ADR-109). A distance, a time or a
    count matches what the frame draws — set 04 wrote `100 m` over a driveway it drew at two metres,
    and the owner failed it in those words. A force, a rating or a capacity names the thing the
    frame shows in use.
  - **In a feature image — a section image whose block argues one named feature, the `mechanism`
    and `how-to-use` roles — one short line (ADR-106)**: a figure with its unit as the page states
    it, and/or a tag of two to five words naming that feature, plus the one-to-three-word labels a
    chart or a call-out needs. Never a sentence, never a second line. The tag takes this type's
    `title` slot and the figure its `badge` slot, so G16 binds as it always has.
  - In every other section image, no words (ADR-096). Lettering itself has held: the gallery title
    came back exact and once 1 of 1 under 0.2, and set 04's three lines 3 of 3.
- **G6 on screens.** A television or a phone at the far end may show a photograph or a film
  scene, never interface text, notifications, bars or numbers. The sentence names that device
  (`PARTS/far-end`).
- **A15.** No figure on the signal; a figure the page supplies belongs in the words.
- **G8 does not bind a signal**, because there is no visible output. A lit status light stays the
  product's own indicator and is not the signal.
- **People.** A person or a pair of hands appears where it explains the use; a face is allowed
  where it is relevant and never poses for the lens. G13 binds, and casting follows the namespace.
  **Pets** only where the page's product serves them.
- **One mechanism variant to a set** (`mapping/pdp-dr-rules.md`, rule 3).
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + interface text, notification cards, signal-strength bars, figures on the signal,
red or green signal marks, marks painted on the product, a rainbow gradient, lightning bolts,
a second product, the product floating, a closed wall with marks drawn on its paint,
the product small or far off, a flat evenly lit frame, faint thin lines,
the product set out on display with nobody using it, a string of glowing beads,
a looping wire, a far end too small to read, a well-known brand's product or wordmark,
the product enlarged against the hand, ear or body beside it, a mark floating beside the
product and touching nothing, a sentence of copy, a second line of words,
a hole cut in a car, a mattress, an appliance, a bag or any other thing the buyer owns,
a mark running along a cable or a wire, a figure that contradicts the distance the frame draws,
shop signs, hoardings or labelled packaging in the background, a soft edgeless glow,
a thin product shown without its working end
```

## BLOCK
**Criterion 1 is one source short**: snapi-stud, pawdi-cas, ezy-talux and cliktric, of the five
SPEC §6.3 asks. The fifth should reach a place rather than a person — a router, a speaker, a hub.
**The owner's four audit frames do not close it**: no named source page, not in the assets tree,
cited for the register only.

**Criterion 2 is unrun**, against `03-mechanism-contact` (its working end touches a body at one
place; this type reaches something at a distance) and `03-use-grid` (the hosts a product serves,
one to a cell; this type shows the link to them). Set 04's prompt 5 was the test and the torn
mattress swamped it. It also borders two proposals with no file: `03-mechanism-emanation`, a
VISIBLE output photographed, and `04-proof-interface`, a reading on a screen.

**Criterion 3 has no passing render.** The owner failed all five of set 01 (0.1), all four of set
02 (0.3), and all six of set 04 (0.6); set 03 (0.5) never rendered and was audited on its words
(ADR-106). 0.7's first set is `sets/03-mechanism-signal-05/`.

## KNOWN-FLAKY
**Under 0.2 and 0.3** (sets 01 and 02, nine renders): both registers are gone and the nine ledger
lines hold their checks. Two still bear on 0.7 — the product was invented where no photo existed,
2 of 4, once with a real wordmark; and a hallway cut became a brick recess, 1 of 2, which set 04
then repeated twice on possessions (`PARTS/barrier`).

**Set 03 (0.5) never rendered**; the owner audited it on its words (ADR-106). Still untested from
it: a blocked signal passing through what should stop it, and a scent rendering as smoke.

**Under 0.6** (set 04, six renders, **all failed by the owner** on 2026-09-18). What HELD, and it
is why 0.6's three clauses stay: the scale 6 of 6, the one short line 3 of 3, the through-view 1
of 1. What failed went into PARTS and SLOT CONSTRAINTS: the cut 2 of 2, the figure against its
frame 1 of 1, the mark along a cable 1 of 1 (2 of 2 with set 02), the thin product as a bare cable
1 of 1, background print 2 of 6. Left here as single instances: the halo as an edgeless blur 1 of
1, two mark forms in one frame 1 of 1, and a screen with an icon and a reading 1 of 1 — the fifth
screen in this type's history to take interface or a picture.
- **0.6's predictions, answered:** the mark did not fall back to a generic glow; nothing spilled
  onto the product's face 6 of 6; the camera sentence held the scale 6 of 6; the line rendered
  clean 3 of 3. A chart keyed to subjects is still undrawn.

**Predicted for 0.7, and what set 05 checks first:**
- a cut in building fabric reading as damage even where the fabric is a wall or a duct;
- an inset panel rendering as a hole in the object anyway;
- a figure that names a force reading as a distance;
- a mark at two ends jumping back onto the cable between them;
- a thin product's working end rendering as a generic plug.

## CHANGELOG
- 0.7 (2026-09-18): **the owner failed all six renders of set 04** (ADR-109; six ledger lines,
  `verdict_by: owner`). Five clauses: a cutaway is cut from building fabric and never from a thing
  the buyer owns, replaced by an inset, the product's own screen or a real opened state (3 of 4
  cuts came back as damage); a drawn figure is true of its frame (1 of 1); a mark never runs along
  a cable (2 of 2); a thin product is framed on its working end (1 of 1); the place carries no
  signage (2 of 6). 0.6's three clauses stand: scale 6 of 6, the one short line 3 of 3, the
  through-view 1 of 1.
- 0.6 (2026-09-18): **the owner audited set 03 on its words, with twelve reference frames**
  (ADR-106). The mark is the invisible thing in its OWN form, landing on the subject (a glowing arc
  is 0 of the owner's 12 frames and was in all six of set 03's prompts); scale comes from the host
  and the share sentence goes; a feature image may carry one short line, inside the declared text
  layer. `PARTS/path` gained four families and the sources the owner's four frames, not counted.
- 0.5 (2026-09-17): owner instruction, *"thử đặt skeleton giống output format của feature image
  txt"*. The SKELETON becomes that output format — one paragraph, seven steps, its closing
  sentence — and the LP2 product block leaves the prompt on trial, G1 staying in one sentence
  (ADR-101). Never rendered; set 03 was audited on its words instead.
- 0.4 (2026-09-17): **the owner failed all four 0.3 renders**. The signal is a known symbol, never
  a trail (beads or wire 3 of 3); the far end is large and sharp (small and soft 4 of 4); the
  product is named; the screen sentence names the far end's device (2 of 4).
- 0.3 (2026-09-17): **the owner failed all five 0.2 renders**. The skeleton is rewritten on the
  owner's feature-image instruction (ADR-100): one paragraph, the product the nearest and sharpest
  object in use, a light ground out of focus, bold glowing marks. Share and contrast were measured
  against lp00412-4 and lp00132-3.
- 0.2 (2026-09-17): **founding round — five renders, all partial**, the WiBoofy extender. The drawn
  layer held: one family and one blue in all five, each path form as named. No clause added.
- 0.1 (2026-09-17): drafted from ten observations across four sources — pawdi-cas, snapi-stud,
  ezy-talux and cliktric — all opened first. New device `signal`. ADR-099.
