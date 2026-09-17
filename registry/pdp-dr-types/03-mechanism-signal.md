---
id: 03-mechanism-signal
step: 3
job: mechanism
device: signal
version: "0.5"
status: reserved
replaced_by: null
channels: [landing-page, marketplace]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [title]
variants: []
exempt_from: []
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Criterion 1: four distinct sources of the five SPEC 6.3 asks. Criterion 2, the router-confusion test against 03-mechanism-contact and 03-use-grid, is unrun. Criterion 3: the owner failed all five renders of set 01 and all four of set 02 on 2026-09-17, and 0.5 has no render."
---

# 03-mechanism-signal — PDP-DR DRAFT

Promotion status (2026-09-17): **4 distinct sources, 10 observations — criterion 1 is one
source short.** Drafted on the owner's instruction of 2026-09-17: the owner rejected a mapping
that proved a Wi-Fi extender's reach with a lineup of product photos, and named two ClikTric
pages whose feature images draw the invisible instead. Every frame below was opened and
looked at before this file was written (ADR-092's discipline).

**The owner's verdicts, 2026-09-17.** Set 01 (0.1) and set 02 (0.3) both failed next to the
reference images, which the owner makes with the feature-image instruction (`~/Downloads/feature
image.txt`). 0.3 took that instruction's register (ADR-100). 0.4 took set 02's lessons: a known
symbol, both ends large and sharp, the product named. 0.5 is the owner's trial of the
instruction's output format as the skeleton, without the LP2 product block (ADR-101).

| source | frame | what is drawn | the far end | the product |
|---|---|---|---|---|
| snapi-stud | img-08 | arcs from the detector into three wall cutaways | timber, cables, rebar inside the wall | yes |
| snapi-stud | img-18 | rings around the detector; stacked cutaway strata below | four targets at labelled depths | yes |
| pawdi-cas | img-11 | a dotted sight line and a reticle | a smart lock across the hall | yes |
| pawdi-cas | img-04 | detection brackets; a sound waveform; phone notifications | a dog, a crying infant | **no** |
| pawdi-cas | img-06 | a red outline around an intruder; a siren bolt | the intruder, a phone notification | yes |
| pawdi-cas | img-09 | a monitored-zone rectangle, a ghosted walker, a bracket | the walker, a phone notification | yes |
| pawdi-cas | img-15 | two speech bubbles | a child across the room | yes |
| ezy-talux | img-10 | a grey waveform before, an orange one after | none, the signal itself | yes |
| cliktric | lp00412 feature 4 | curved arrows between two devices | a phone showing the photo | yes |
| cliktric | lp00132 feature 3 | WiFi arcs on both sides; iOS and Android marks above | named by marks only | yes |

The two ClikTric pages sell one product and are one source (batch 2026-09-17-A).

**What the ten share, counted from the set:**
1. **Something invisible is drawn, 10 of 10**: arcs or rings from the product 3, a path to what it
   reaches 2, marks on the thing detected 3, waveforms 2, speech bubbles 1.
2. **The far end is in frame, 8 of 10**; **the product, 9 of 10**.
3. **The result is phone interface text, 4 of 10**, which G6 keeps out of a generated frame.
4. **A barrier cut open, 2 of 10**, both snapi-stud's: the one construction for passing THROUGH.
5. **Blue carries a working signal, 7 of 10; red an alert, 3 of 10** (pawdi-cas). This file draws
   a working signal only (G3).
6. **Words in frame, 10 of 10**; on LP2 only the product card's gallery keeps them (ADR-096).

## PURPOSE
Show what the product does at a distance when that action cannot be photographed: a signal it
sends or senses, drawn as luminous marks over an editorial photograph in which the product is
the anchor and in use. The frame answers *"how does it get there"* — through a wall, across a
room, into a phone — and the far end shows that it arrived. It must read in three seconds.

## TRIGGER
use_when: >
  The copy's claim is a signal the product sends or senses and nobody can see: WiFi or
  Bluetooth reach, coverage through walls or floors, a wireless link to a phone or a TV,
  detection of a person, a sound or a hidden object. A gallery mechanism tile, or a feature,
  problem or support section whose copy names what the signal reaches or passes through.
  Take 03-mechanism-contact when the product touches a body at one place;
  03-use-grid when the argument is the range of hosts rather than the link to them;
  03-spec-macro when the claim is the product's own part rather than what that part sends.
  Never a lineup of products: a still cannot show a difference nobody can see.

## SKELETON
**The owner's feature-image OUTPUT FORMAT, with the mark added** (ADR-101). The steps are the order
of the paragraph, not labels in it; each names the PARTS or MARKS entry that defines it once.

```
TYPE: 03-mechanism-signal v0.5

Each prompt is one natural paragraph, starting directly with the image prompt, with no labels
or JSON, in this order:
  1. The photograph: its camera and layout, the product BY NAME, what it is doing, where.
                                                                         -> PARTS/opening
  2. The product: the nearest, largest and sharpest object in the frame, whole and
     unobstructed, filling about 40% of the frame height.                -> PARTS/anchor
  3. The far end: what the signal reaches or is stopped short of, large and in sharp focus,
     showing the result by itself; a barrier only where the claim passes through one.
                                                                         -> PARTS/far-end, PARTS/barrier
  4. The mark, in a sentence of its own: one known glowing symbol from beside the product to
     the far end, and what it shows; then the set's mark sentence.       -> PARTS/path, MARKS/signal
  5. Light and background: the set's two sentences.                      -> PARTS/ground
  6. Words and the corner: the set's sentence; a gallery tile adds its title sentences.
                                                                         -> SLOT CONSTRAINTS
  7. "Use the attached product photo as the exact reference."            -> PARTS/form (G1)

Optional elements:
- Human elements: none, partial hand, body, or a face when contextually relevant.
- Pet elements: only when contextually relevant.

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
  reference.` 0.3 and 0.4 carried the whole block, and it held nothing where no photo existed.
- The paragraph says where a thing is and never names a region (adapter Rule 1b).
- The signal gets a sentence of its own. A mark buried inside another clause is the one that
  vanishes (`01-pain-scene`, adapter Rule 7).
- A sentence the set shares is written once and repeated word for word (LP2 rule 4).
- 0.2's prompts were labelled lines, and the owner failed all five.

**`opening`** — the first sentence says what the photograph is: the camera, who is there, what
they are doing, and where.
- The camera comes from the instruction's list: wide lifestyle, 45-degree usage angle, front-on
  eye level, over-the-shoulder, partial hand, close-up, handheld.
- The layout is one of the instruction's three:
  - a **usage scene** for a product in a hand;
  - an **in-environment installation** for a fixed product;
  - a **feature demonstration** where the product works with nobody touching it.
- The place is the one the page's use happens in, and it explains why the product matters.
- **The product is named** as the page names it — "the portable Bluetooth speaker" — the way the
  instruction takes the product's name as its input. A name says what the object is, and G2
  still keeps its looks to the photograph. 0.3 wrote only "the product", and 2 of 4 renders
  invented one: a well-known brand's camera with its wordmark, and a gadget with a display where
  a floor-vent fan should be. No photo existed for either product.

**`anchor`** — the product, in use or installed, is the visual anchor: **the nearest, largest and
sharpest object in the frame, whole and unobstructed, filling about 40% of the frame height.**
- **Measured** (boxes read by eye): the product filled 7.8% and 25.3% of the two signal
  references, 1.6%–3.2% of 0.2's renders, and 5.9%–16.0% of 0.3's under this sentence, 4 of 4.
  The owner still failed 0.3's, so size was necessary and not enough.
- **In use**: held, pressed, plugged in, installed, or working beside the person it serves.
- **A fixed product stays installed** (G7-X): a plug-in unit sits in its socket. 0.2 kept it
  there 4 of 5.
- **The marks leave from beside the part that sends and never lie on the product**: off its
  face 9 of 9 renders; the owner's own runs painted a diagram on it 4 times (ADR-094).

**`far-end`** — what the signal reaches, and only what the page names, in use, **large and sharp**:
held in the other hand or set across the frame from the product, as the phone is in lp00412-4,
where it fills about half the frame height.
- **0.3 misread that reference**: its soft figure is the person being photographed. 0.3 blurred
  its far end, and set 02's came back small and soft 4 of 4.
- It shows the result by itself: a person streaming, a device working, a room in use.
- It never shows the result as a notification or as interface text. lp00412-4 draws an app on
  its phone; G6 keeps that out of a generated frame, so the far end's screen shows a photograph.
  0.2 got a broadcast's graphics on 1 of 3 screens (`KNOWN-FLAKY`).
- **The screen sentence names the far end's device, never "any screen".** Written for the whole
  scene, it gave the product a display with a picture on it, 2 of 4: a fan that has none, and a
  receiver whose real display G6 leaves to the photograph.

**`barrier`** — only where the copy's claim is passing THROUGH something: a wall, a floor, a
door. The barrier is cut open as a window, so the path is seen crossing it, and the cut shows the
layers the page names and nothing deeper. snapi-stud cut the wall both times it made this
claim, and no frame in the corpus drew it on a closed wall. 0.2 rendered two cuts and neither
read as damage; one became a brick recess the path ran past (`KNOWN-FLAKY`). **Untested under
0.3.**

**`path`** — a parameter, and the copy picks it. **Each form is a symbol a buyer already knows,
drawn as the owner's references draw it:**
- `arcs` — the Wi-Fi symbol: three or four smooth concentric arcs around a small dot, glowing,
  beside the sending part, on one side or both (lp00132-3). Reach and emission, 3 of 10. Set 02
  drew it cleanly, 1 of 1.
- `line` — one or two broad, smooth, sweeping arrows with a blue gradient and soft motion
  streaks, from the product to the far end, one each way for a two-way link (lp00412-4). A
  link or a transfer, 2 of 10. **Never a "trail", and never dotted**: set 02's dotted trails
  came back as strings of glowing beads, 2 of 2, and its continuous trail as a looping wire,
  1 of 1.
- `rings` — glowing rings spreading from the product through the space. Coverage; snapi-18 is
  the only instance, counted with the arcs.
- 0.2 rendered each form as it was named, 5 of 5, but as thin flat lines, and they read as weak.

**`ground`** — the real place the claim is about, **light in tone and simple** — a plain wall, a
bare desk, or a softly blurred place behind both ends — under bright, directional daylight.
Nothing in it competes with the product, the far end or the signal (lp00412-4's plain wall,
lp00132-3's bare desk). The background may blur; the far end never does.
- **The fault 0.2 wrote into its lock was a flat frame**: every surface lit alike, everything in
  focus, "nothing saturated". Luminance contrast measured 0.265 and 0.275 in the two references and
  0.147–0.206 in the renders. Mean saturation did not separate them (0.159 and 0.239 against
  0.119–0.214).
- So the fix is light and focus, not colour, and the namespace's quiet ground stands
  (`registry/pdp-dr-instruction.md`, *Ground*).

## MARKS

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `signal` | one recognisable, clean, glowing symbol — the Wi-Fi arcs with their dot, broad sweeping arrows, or rings — bold enough to read at a glance, beside the product and running to the far end | luminous blue, which may shade toward cyan (G3: working) | one form per frame | corpus 10 of 10, blue on 7; both owner references glow · 0.2's thin flat blue: 5 renders, owner fail · 0.3's glowing trails read as beads or wire 3 of 3, its arcs clean 1 of 1, owner fail 4 of 4 |

- **Bold and luminous, never thin and flat.** 0.2 asked for "thin, clean" marks, and the owner
  failed all five against references whose arcs and arrows glow.
- **One form, one colour.** snapi-stud's arcs, pawdi-11's sight line and ClikTric's arrows each
  keep to one family. pawdi-cas's detection frames stack brackets, sirens and notifications into
  one picture, and they are the busiest of the ten.
- **Never red, and never a flat green.** Red is pain and wrong states, and green is the verdict
  (G3). lp00412-4's arrows shade from blue into green; this file stops the shade at cyan.
- **No bars and no figures on the marks.** A signal-strength meter or an Mbps number drawn on the
  signal is a reading, and A15 and G6 both reach it.

## SLOT CONSTRAINTS
- **The prompt budget** (ADR-013, ADR-015): a clause earns its place after a render failed
  without it. 0.3's clauses — the anchor, the focus, the glow, the paragraph — are earned by the
  owner's fail of all five 0.2 renders on 2026-09-17. **None has rendered yet.**
- **Length.** A prompt stays within 1,800 characters with the reference and closing sentences in
  it; without the block, most run well under.
- **Words.**
  - In the product card's gallery: a title of 2–5 words saying what the signal does, in the
    buyer's words, written as a sentence of the paragraph.
  - One 1–3 word label beside the far end, only where the far end is not obvious; it counts as
    the tile's chip.
  - Outside the gallery, no words at all (ADR-096).
  - 0.2: the gallery title came back exact and once, 1 of 1, and the four section images
    carried no words.
- **G6 on screens.** A television or a phone at the far end may show a photograph or a film
  scene, never interface text, notifications, bars or numbers. The sentence names that device
  (`PARTS/far-end`).
- **A15.** No figure on the signal. A figure the page supplies belongs in a gallery tile's
  words, never on the drawing.
- **G8 does not bind a signal**, because there is no visible output. Where the product also
  emits something visible, such as a lit status light, that stays the product's own indicator
  and is not the signal (the corpus finding on indicator colours).
- **People.** A person or a pair of hands appears where it explains the use. A face is allowed
  where it is relevant, and it never poses for the lens (the owner's instruction). G13 binds:
  no private room, no age in years. Casting follows the namespace.
- **Pets** only where the page's product serves them (the owner's instruction).
- **One mechanism variant to a set** (`mapping/pdp-dr-rules.md`, rule 3).
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + interface text, notification cards, signal-strength bars, figures on the signal,
red or green signal marks, marks painted on the product, a rainbow gradient, lightning bolts,
a second product, the product floating, a closed wall with marks drawn on its paint,
the product small or far off, a flat evenly lit frame, faint thin lines,
the product set out on display with nobody using it, a string of glowing beads,
a looping wire, a far end too small to read, a well-known brand's product or wordmark
```

## BLOCK
**Criterion 1 is one source short**: snapi-stud, pawdi-cas, ezy-talux and cliktric, of the five
SPEC §6.3 asks. The fifth should be a device that reaches a place rather than a person: a
router, a speaker, a hub.

**Criterion 2 is unrun**, against two neighbours:
- `03-mechanism-contact` also draws what crosses a boundary. It does so where the product's
  working end touches a body at one place, and this type reaches something at a distance.
- `03-use-grid` in its compatibility form shows the hosts a product serves, one to a cell. This
  type shows the link to them in one frame.

It also borders two proposals with no file:
- `03-mechanism-emanation`, where a VISIBLE output — mist, light, air — fills a space and is
  photographed;
- `04-proof-interface`, where the argument is a reading on a screen, which this type never
  draws.

**Criterion 3 has no passing render.** On 2026-09-17 the owner failed all five renders of
`sets/03-mechanism-signal-01/` (0.1) and all four of `sets/03-mechanism-signal-02/` (0.3). 0.5
has not rendered; its first set is `sets/03-mechanism-signal-03/`.

## KNOWN-FLAKY
**Under 0.2** (set 01, five renders; the register is gone, so these are checks, not clauses):
- **Not the page's product, 5 of 5**: no antennas, no WPS button, five different bodies. Whether
  the photo was attached is unrecorded, so this is not evidence against the product block.
- **Not installed, 1 of 5**: a unit hung above an empty socket.
- **A broad path read as a cable, 1 of 1**, bent at right angles and resting on the product.
- **A sports broadcast brought its score bar, 1 of 3 screens**; a film and a photo stayed clean.
- **A cut down the hallway became a brick recess the rings ran past, 1 of 2 cuts.**
- **At 208 px, the problem block's width, the far router was a speck, 1 of 1.**
- **Struck, because it did not occur** (`eval/render-test.md` §5): a cut-open wall read as
  damage, 0 of 2.

**Under 0.3** (set 02, four renders, all failed; what 0.4 took is in PARTS):
- **The product was invented where no photo existed, 2 of 4**, once as a well-known brand's
  camera with its wordmark. A set names the photo each prompt needs.
- **Predictions checked:** no glow spilled onto the product, 0 of 4; the enlarged product never
  pushed the far end out, but the far end was small every time; no airflow was drawn, 0 of 1;
  a product's display got a picture, 2 of 4 (now in `PARTS/far-end`).

**Predicted for 0.5, and what set 03 checks first:**
- without the block, the product drifting from its photo even where one is attached;
- a blocked signal, which no earlier set drew, passing through what should stop it;
- a scent, which is not a signal, rendering as smoke: set 03's boundary case.

## CHANGELOG
- 0.5 (2026-09-17): owner instruction, *"hãy thử đặt skeleton giống output format của feature image
  txt"*. The SKELETON is the instruction's output format, one paragraph in seven steps, its
  optional human and pet elements, and its closing sentence. The LP2 product block leaves the
  prompt as a trial, and G1 stays in one reference sentence (ADR-101). No render yet.
- 0.4 (2026-09-17): **the owner failed all four 0.3 renders** against the reference page (render-test
  ts 2026-09-17; speaker, booster fan, camouflage camera, breaker finder). The signal is a known
  symbol — Wi-Fi arcs or broad sweeping arrows, never a trail (beads or wire 3 of 3); the far end
  is large and sharp (small and soft 4 of 4); the product is named; the screen sentence names the
  far end's device (a product display got a picture 2 of 4).
- 0.3 (2026-09-17): **the owner failed all five 0.2 renders** against the reference images. The
  skeleton is rewritten on the owner's feature-image instruction (ADR-100): one paragraph ending
  in the owner's sentence; the product the nearest, largest and sharpest object, in use; a light
  ground out of focus under directional daylight; bold glowing marks. Product share and contrast
  were measured against lp00412-4 and lp00132-3. The failed worked example is dropped.
- 0.2 (2026-09-17): **founding round — five renders, all partial** (render-test ts 2026-09-17,
  the WiBoofy extender on five template fields). The drawn layer held: one family and one blue in
  all five, each path form as named, no mark across the product, words only in the gallery tile.
  No clause added, since each failure is a single instance: six entries in KNOWN-FLAKY, one
  prediction struck. The control is a worked example, harness-graded.
- 0.1 (2026-09-17): drafted from ten observations across four distinct sources: pawdi-cas,
  snapi-stud and ezy-talux in batches 2026-09-03-H, 2026-09-11-I and -J, and cliktric in
  2026-09-17-A, all ten opened first. Tier 2 at three sources in `_CURATION-2026-09-11.md`, and the owner's ClikTric
  pages are the fourth. New device `signal`. Owner instruction, 2026-09-17. ADR-099.
