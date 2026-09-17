---
id: 03-mechanism-signal
step: 3
job: mechanism
device: signal
version: "0.2"
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
blocked_by: "Criterion 1: four distinct sources of the five SPEC 6.3 asks. Criterion 2, the router-confusion test against 03-mechanism-contact and 03-use-grid, is unrun. Criterion 3 now has five renders, all partial, but every verdict is the harness's own and ADR-011 excludes those from promotion."
---

# 03-mechanism-signal — PDP-DR DRAFT

Promotion status (2026-09-17): **4 distinct sources, 10 observations — criterion 1 is one
source short.** Drafted on the owner's instruction of 2026-09-17: the owner rejected a mapping
that proved a Wi-Fi extender's reach with a lineup of product photos, and named two ClikTric
pages whose feature images draw the invisible instead. Every frame below was opened and
looked at before this file was written (ADR-092's discipline).

**Founding round rendered 2026-09-17** — five prompts on the owner's WiBoofy template, all five
partial, graded by the harness under ADR-011. The drawn layer held. Each failure is a single
instance and sits in `KNOWN-FLAKY`, except the product's identity, whose cause the round did not
record.

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

**What the ten share, derived from the set rather than fitted to a definition:**
1. **Something with no visible existence is drawn, 10 of 10.** The forms:
   - arcs or rings leaving the product, 3;
   - a path from the product to what it reaches, 2;
   - marks on the thing detected, 3;
   - waveforms, 2;
   - speech bubbles, 1.
2. **What the signal reaches is in frame, 8 of 10.** ClikTric's arcs name the receivers by their
   marks alone, and ezy-talux draws the signal with nothing at the far end.
3. **The product is in frame, 9 of 10.** pawdi-04 draws the signal over the scene and omits the
   camera.
4. **The result sits on a phone screen as interface text, 4 of 10.** This library cannot draw
   that (G6: screens and readouts are never model-drawn), so the far end has to show the result
   by itself.
5. **A barrier cut open, 2 of 10.** Both are snapi-stud's. This is the one construction that
   shows a signal passing THROUGH something, and it is the claim a Wi-Fi extender makes.
6. **Blue carries a working signal in 7 of 10**: the two cut-wall frames, the sight line, the
   bracket and the zone in pawdi-04 and -09, and both ClikTric frames, where one arrow is green
   and reads as direction. **Red carries an alert in 3 of 10**, all pawdi-cas. G3 gives red to
   pain and wrong states, so this file draws a working signal only.
7. **Words in frame, 10 of 10.**
   - The eight market tiles carry headlines and labels.
   - The two ClikTric section images carry a caption and a platform wordmark.
   - On an LP2 page only the product card's gallery keeps words (ADR-096).

## PURPOSE
Show what the product does at a distance when that action cannot be photographed: a signal it
sends or senses, drawn as clean marks between the product and what it reaches. The frame answers
*"how does it get there"* — through a wall, across a room, into a phone — and the far end
shows that it arrived.

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
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 03-mechanism-signal v0.2
REGISTER: a photograph of the product and what it reaches, the signal drawn over it. -> PARTS/register

[PRODUCT REFERENCE]  the attached photo is the exact reference.       -> the LP2 product block
[SOURCE]             the product at its real place, the sending part clear. -> PARTS/source
[FAR END]            what the signal reaches, as the page names it.  -> PARTS/far-end
[BARRIER]            only where the claim passes through something.  -> PARTS/barrier
[PATH]               arcs | line | rings                              -> PARTS/path
[SIGNAL]             the drawn marks.                                 -> MARKS/signal
[GROUND]             the real place; quiet.                           -> PARTS/ground
[TITLE]              gallery only: what the signal does, 2–5 words.   -> SLOT CONSTRAINTS

Nothing drawn touches the product's surface, and no screen carries interface text.
```

## PARTS

**`register`** — the product and the far end are photographs, and the signal is flat drawn
marks over the photograph. All ten frames build it this way. The drawn layer is thin and clean,
and it never becomes a render of the whole scene.

**`source`** — the product at its real place, whole and legible. A fixed product stays in its
installed position (G7-X): a plug-in unit sits in a wall socket. The marks leave from the part
that sends — an antenna, a lens, a sensor face — and **never start on the product's surface or
cover it**. The owner's runs painted a diagram onto the product 4 times (ADR-094). Of the 9
frames here with the product in them, 8 keep the marks beside the body; pawdi-06 lights the
camera itself red. **Rendered 2026-09-17:** the unit was plugged in 4 of 5, and no mark crossed
its face in any of the five. The one mark that touched it was a band the prompt had asked to be
broad (`KNOWN-FLAKY`).

**`far-end`** — what the signal reaches, and only what the page names: a television, a phone, a
room, a lock, a person, the contents of a wall. It is in frame and legible, **and it shows the
result by itself** — the television playing, the room in use, the lock lit. It never shows the
result as a notification or as interface text. Four of the ten used a phone screen for the
result, and a generated frame cannot. **Rendered 2026-09-17:** a film on a television and a
photograph on a phone stayed pictures, and a football match brought its score graphics, 1 of 3
screens (`KNOWN-FLAKY`).

**`barrier`** — only where the copy's claim is passing THROUGH something: a wall, a floor, a
door. The barrier is cut open as a window, so the path is seen crossing it, and the cut shows the
layers the page names and nothing deeper. snapi-stud cut the wall both times it made this
claim, and no frame in the corpus drew it on a closed wall. **Rendered 2026-09-17, and neither
cut read as damage, 0 of 2.** A cut asked for as the end of the wall the product hangs on read as
a clean section the arcs cross, 1 of 1. A cut asked for in a wall down the hallway came back as a
brick recess the rings run past, 1 of 1 (`KNOWN-FLAKY`).

**`path`** — a parameter, and the copy picks it:
- `arcs` — nested arcs leaving the sending part. Reach and emission, 3 of 10.
- `line` — a dotted or solid path from the source to the far end. A link or a transfer, 2 of 10.
- `rings` — concentric rings around the source, for coverage of a space. snapi-18 is the only
  instance, and it is counted with the arcs above.
- **Each form rendered as it was named, 5 of 5** (2026-09-17): the line in two frames, the arcs
  in two, the rings in one.

**`ground`** — the real place the claim is about: a hallway, a living room, a desk. It is quiet
in value and colour, so the drawn signal is the strongest colour in the frame.

## MARKS

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `signal` | clean flat marks of one family — arcs, rings, or a dotted line — beside the product and running to the far end, fading only where the copy argues loss | one clear blue (G3: working) | one family per frame | corpus 10 of 10, blue on 7 · 5 renders, one family and one blue in all five, no bar or figure |

- **One family, one colour.** snapi-stud's arcs, pawdi-11's sight line and ClikTric's arrows each
  keep to one family. pawdi-cas's detection frames stack brackets, sirens and notifications into
  one picture, and they are the busiest of the ten.
- **Never red or green.** Red is pain and wrong states, and green is the verdict (G3).
  pawdi-cas's red alert marks are a surveillance idiom this file does not import.
- **No bars and no figures on the marks.** A signal-strength meter or an Mbps number drawn on the
  signal is a reading, and A15 and G6 both reach it.

## SLOT CONSTRAINTS
- **The prompt budget** (ADR-013, ADR-015): a clause earns its place only after a render failed
  without it. Every clause above is derived from the corpus. The founding round (2026-09-17)
  added none, because each failure it showed is a single instance.
- **Words.**
  - In the product card's gallery: a title of 2–5 words saying what the signal does, in the
    buyer's words.
  - One 1–3 word label beside the far end, only where the far end is not obvious; it counts as
    the tile's chip.
  - Outside the gallery, no words at all (ADR-096).
  - Rendered 2026-09-17: the gallery title came back exact and once, 1 of 1, and the four
    section images carried no words.
- **G6 on screens.** A television or a phone at the far end may show a picture — a film scene,
  a photograph — but never interface text, notifications, bars or numbers.
- **A15.** No figure on the signal. A figure the page supplies belongs in a gallery tile's
  words, never on the drawing.
- **G8 does not bind a signal**, because there is no visible output. Where the product also
  emits something visible, such as a lit status light, that stays the product's own indicator
  and is not the signal (the corpus finding on indicator colours).
- **G13.** People may be at the far end, doing what the page says. No private room, no age in
  years.
- **One mechanism variant to a set** (`mapping/pdp-dr-rules.md`, rule 3).
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + interface text, notification cards, signal-strength bars, figures on the signal,
red or green signal marks, marks painted on the product, a rainbow gradient, lightning bolts,
a second product, the product floating, a closed wall with marks drawn on its paint
```

## WORKED EXAMPLES
The control of the founding round, kept in full text because that text is the only record of
what rendered (SPEC §3.3). The verdict is the harness's own (ADR-011), so it cannot serve SPEC
§6.3(3).

### example: wiboofy-router-link — skeleton@0.1, run: partial
```
Photograph of a home network link, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.
Render it at 30% of the frame height, plugged into a wall socket right of centre at mid height in a hallway, seen from a front three-quarter angle at waist height.

On a small shelf at the left stands a plain, unbranded grey home router. One dotted line runs level from the router to the product and ends at the product's edge.

Setting: a bright European flat in daylight, pale walls, light oak floors, plain furniture, nothing saturated.
Light: soft daylight from the left, gentle shadows, no rim light.
Grade: bright, neutral, true to life.
Every drawn mark is thin, clean and one clear blue, stays beside the product and never on it, and nothing else in the picture is drawn.
Any screen shows only a picture, with no interface, text or numbers.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```
The line path at its simplest: two objects, one level dotted line, no barrier. The drawn layer
held exactly: the line runs from the router's lit light to the unit's edge, and nothing else is
drawn. The render is partial only because the unit is not the page's extender (`KNOWN-FLAKY`).

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

**Criterion 3 has five renders and no owner verdict.** The founding round,
`sets/03-mechanism-signal-01/`, rendered 2026-09-17 on the fields the owner's WiBoofy template
names: five partial, every verdict the harness's own, which ADR-011 excludes from promotion.

## KNOWN-FLAKY
Five renders, 2026-09-17, set `03-mechanism-signal-01`.
- **The product was not the page's product, 5 of 5.** No render drew the extender's antennas or
  its WPS button, which the template's own product photo shows, and the five bodies differ from
  each other. The round did not record whether the photo was attached, so, as with
  `07-identity-pack` (ADR-095), this is not evidence against the product block. The next round
  records the attachment.
- **Not installed, 1 of 5.** One unit hung on the wall above an empty socket, although the prompt
  plugged it in.
- **A broad path read as a cable, 1 of 1.** Asked to differ from a fine dotted path by width, a
  broad solid path came back as a thick band bent at right angles, and its end rested on the
  product. The prompt had asked for width against the `signal` mark's "thin". Two paths that
  differ by dash alone, both thin, are untested.
- **A sports broadcast brought its graphics, 1 of 3 screens.** A football match came back with a
  score bar. A film and a phone photograph stayed clean under the same screen sentence.
- **A cut asked for down the hallway became a brick recess, 1 of 2 cuts.** The rings ran past it
  rather than through it, so nothing in the frame caused the fade.
- **At the problem block's display width the source was lost, 1 of 1.** Shown 208 px wide, the
  router at the far end of the hallway is a speck, and the product reads as the centre of a
  target.
- **Struck, because it did not occur** (`eval/render-test.md` §5): a cut-open wall read as
  damage, 0 of 2. The other two predictions are now observed above.

## CHANGELOG
- 0.2 (2026-09-17): **founding round — five renders, all partial** (render-test ts 2026-09-17,
  the WiBoofy extender on five template fields). The drawn layer held: one family and one blue in
  all five, each path form as named, no mark across the product, words only in the gallery tile.
  No clause added, since each failure is a single instance: six entries in KNOWN-FLAKY, one
  prediction struck. The control is a worked example, harness-graded.
- 0.1 (2026-09-17): drafted from ten observations across four distinct sources: pawdi-cas,
  snapi-stud and ezy-talux in batches 2026-09-03-H, 2026-09-11-I and -J, and cliktric in
  2026-09-17-A, all ten opened first. Tier 2 at three sources in `_CURATION-2026-09-11.md`, and the owner's ClikTric
  pages are the fourth. New device `signal`. Owner instruction, 2026-09-17. ADR-099.
