---
id: 03-mechanism-contact
step: 3
job: mechanism
device: contact
version: "0.5"
status: reserved
replaced_by: null
channels: [landing-page, marketplace]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [title, copy]
variants: []
exempt_from: [G7]
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Criterion 1: four distinct sources of the five SPEC 6.3 asks. Criterion 2, the router-confusion test against 03-mechanism-ghostbody and 03-mechanism-xray, is unrun. Criterion 3 now has six renders, two pass and four partial, but every verdict is the harness's own and ADR-011 excludes those from promotion."
---

# 03-mechanism-contact — PDP-DR DRAFT

Promotion status (2026-09-15): **4 distinct sources, 7 observations — criterion 1 is one
source short.** Drafted on the owner's instruction to build types from the Densjet gallery,
whose tile 4 is this construction. ADR-078 withheld every Tier-2 id because a count had once
been taken for evidence (`07-identity-callout`, two of five frames really that device). So
all seven frames below were opened and looked at before this file was written, and **every
source carries at least one frame that is unambiguously this device.**

**Founding round rendered 2026-09-16** — six prompts, two pass and four partial, graded by the
harness under ADR-011. What it settled is in `PARTS/cut`, `PARTS/target` and `MARKS`.

**The owner's gallery instruction reached this type the same day** (0.4, ADR-094): its title
band, its labels, a dark key, and the rule that nothing is drawn away from the one contact place.

| source | frame | the working end | the body, and the cut | what crosses the boundary | the frame's claim |
|---|---|---|---|---|---|
| feicemat-v2 | img-16 | a beauty device's head, photographed, LED ring lit | an illustrated lattice of skin cells | grey arrows driven down into the layer | vibration and heat reach the skin |
| feicemat-v2 | img-17 | the same head, **in an inset only** | an illustrated skin section | a drawn electrical arc | the main picture is a face with lift arrows (A2) — weak, same source |
| fosen-ring | img-05 | the whole dual-ring massager, rendered | skin over rows of fat cells, cut | white wave lines from each ring | "body sculpting and fat burning" |
| glowy-liff | img-22 | a wand head, photographed, lit red | a skin and dermis section | a heat glow in the tissue, and a temperature | RF heat reaches the dermis |
| glowy-liff | img-23 | the same head, lit blue | a facial tissue section | cyan beams, and two depth labels | ultrasound reaches the fascia |
| glowy-liff | img-25 | the same head | a skin section | concentric waves, droplets, arrows out | skincare is absorbed |
| densjet-nova | gallery-4 | a nozzle tip only, rendered | four molars **at the surface, not cut** | the water stream, debris leaving the gap | plaque leaves the gap |

**What the seven share, derived from the set rather than fitted to a definition:**
1. **The product appears as its working end.** 6 of 7 show only the part that touches — a
   head, a ring, a tip — entering the frame. fosen-ring shows the whole device.
2. **The body is rendered, never photographed**, 7 of 7 — a technical 3D render or a 2D
   illustration. The product is photographed in 4 and rendered in 3.
3. **Something drawn crosses the boundary in the phenomenon's own form** — waves, beams, a
   glow, an arc, a stream — 7 of 7. Arrows appear in 3, and carry the argument alone only in
   feicemat-16.
4. **A headline at the top, support copy under it**, 7 of 7. No badge, 0 of 7.
5. **A figure, 6 of 7** — a frequency, a temperature, two depths, a percentage. It is this
   construction's commonest content and exactly what A15 and A13 bar.

**Two differences the owner's example brought**, recorded rather than averaged away: gallery-4
shows the contact at the SURFACE where the other six cut the body open, and its agent is the
product's OUTPUT, a water stream, where the other six show the head doing the work. Same
argument both times, so `cut` is a parameter here and not a second type (SPEC §3.2).

## PURPOSE
Show what happens where the product meets the body. Its working end, or what it sends out,
touches one named place; the body there is opened or shown close; and the effect is drawn
crossing the boundary. The frame answers *"what does it actually do when it touches me"* —
which a photograph cannot, because the effect is under the skin or too small to see.

## TRIGGER
use_when: >
  The copy explains HOW the product works on the body at the place it touches — a vibration
  reaching a muscle, a stream reaching a gap, suction lifting what sits in a pore, a current
  reaching the tissue under a pad. A gallery mechanism tile, or a mechanism section whose copy
  names what happens under the product's working surface. Choose 03-mechanism-ghostbody when
  the argument is why the product's SHAPE fits a body, told on a whole anonymous figure;
  03-mechanism-xray when it is what is inside the PRODUCT; 03-spec-macro when the claim is
  about the product's own surface or material rather than what that surface does to a body.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 03-mechanism-contact v0.5
REGISTER: product photograph meeting a clean technical render of the body.  -> PARTS/register

[PRODUCT REFERENCE]  the attached photo is the exact reference.        -> G1
[WORKING END]        the part that touches, and where it touches.      -> PARTS/working-end
[TARGET]             the body structure the copy names, rendered.      -> PARTS/target
[CUT]                section | surface                                 -> PARTS/cut
[AGENT]              what crosses the boundary, drawn as itself.       -> MARKS/agent
[REMOVED]            only where the product takes something away.      -> MARKS/removed
[LABELS]             optional: 1–3 words beside a structure named.     -> PARTS/labels
[GROUND]             quiet by default; a dark key is allowed.          -> PARTS/ground
[TITLE]              what happens, in the buyer's words, 2–5 words.    -> SLOT CONSTRAINTS
[COPY]               the mechanism in plain words, at most 10 words.   -> SLOT CONSTRAINTS

Nothing in the frame is marked that is not named here, and nothing is drawn
away from the one place the product meets the body.
```

## PARTS

**`register`** — the product as a photograph made from the reference, the body as a clean
matte technical render in pale, low-saturation tones. 4 of 7 frames mix the two this way.
**G5 does not reach it**: G5 binds a frame that contains a comparison, and this compares
nothing. feicemat-16's record says G5 "probably should" reach a continuous mixed scene; that is
a question the first renders answer — one image, or a product pasted on a diagram — and not a
clause written before any exists. The pale body leaves the agent as the only strong colour,
which is what 6 of 7 corpus renders already do.

**`working-end`** — the part that touches: a head, a pad, a roller, a tip. It meets the body
at one place near the centre, and the rest of the product runs up out of the frame. **Enough
of it stays in frame to recognise the product**: gallery-4 shows the nozzle tip alone, and its
own record names the cost — *"a tile that never shows what the product looks like."* G1 binds
the visible part hard, because a cropped end is where a model quietly redesigns a product; G2
keeps the prompt to position, angle, scale and relation.

**`target`** — the body structure the COPY names: the muscle a massager reaches, the gap a
stream reaches, the pore a suction tip empties. Never a generic tissue. fosen-ring is the
warning: skin over rows of fat cells, *"generic enough to mean nothing"*, carrying the page's
strongest claim.

**The frame says WHICH region, not only which layers.** The cupping render of 2026-09-16 drew a
correct stack — skin, fat, calf muscle — that nothing in the frame identified as a calf (1 of 4
section renders). Show enough of the region's own outline for the name in the copy to land: a
calf's curve, a thigh's taper, a shoulder's slope.

**`cut`** — a parameter, and the copy picks it.
- `section`: the body cut open under the working end, 6 of 7. **Depth is DERIVED, never
  chosen** (A13): name the layers as a closed list from the surface, ending at the first layer
  below the deepest structure the product reaches, and draw nothing deeper. Borrowed from
  `03-mechanism-ghostbody` `PARTS/cutaway`, where an unbounded cut took a scalp comb into the
  cranium 2 of 2. **Tested here 2026-09-16 and it held 4 of 4** — including the scalp, where the
  list ended at the hair roots and no skull was drawn.
- **The cut is a WINDOW, and the silhouette survives it.** The body continues out of the frame
  on both sides; it is never a segment closed off at each end. Borrowed from the same file,
  after the first control render drew a thigh as a slab cut at both ends (2026-09-16, 1 of 4
  section renders).
- `surface`: the body's outer surface seen close, not cut, where the effect shows there — a gap
  between teeth, a heel, a pore. 1 of 7: gallery-4, the owner's example.
- **The surface form is where the register flips, 2 of 2** (2026-09-16). Both surface renders
  came back as photography — real skin with pores, a real heel — although the prompt named a
  clean matte technical render, and one of them brought a face fragment with it. Naming the
  register is not enough there: say what makes the body DRAWN — flat matte colour, simple
  outlines, the pores or the texture as drawn marks rather than photographed skin.

The camera is level with the place they touch **by default** — feicemat-16's record, and the
boundary runs across the frame in all seven. Level is a default and not a lock: glowy-liff's
three look slightly down onto the contact plane and gallery-4 enters at an angle from the upper
left. The namespace's composition rule (`registry/pdp-dr-instruction.md`, rule 3, 2026-09-16)
asks a page's SET for varied cameras; what a camera may not do here is lose the boundary.

**`ground`** — quiet by default (`registry/pdp-dr-instruction.md`, ADR-068): light in value,
close to neutral. Pale blue, lilac, pink and blue-white in 6 of 7; glowy-22's panel is lit red
from within by its own heat glow. **A dark key is allowed** (ADR-094): the owner's instruction
admits one for this type, and a prompt that takes one says why — the corpus built light grounds
6 times in 7.

**`labels`** — optional, 1–3 words each, set beside the structure they name and never on the
agent, a line or the product; only structures the copy names. They are this type's chips and
count toward the tile's sixteen words (ADR-094). No contact render has carried one; the one
mechanism render in the owner's runs that labelled a named part — a comb's atomiser — held it
cleanly.

## MARKS

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `agent` | what crosses the boundary, in the phenomenon's own form — pressure rings, wave lines, fine pulses, beams, the stream itself — leaving the working end and stopping at the target | clear cyan-blue (G3: working mechanism); a liquid keeps its own colour | one family | corpus 7 of 7 · 6 renders, cyan in all six, none needing an arrow |
| `removed` | what the product takes away — debris, a plug, flakes — leaving the target only at the contact point | the matter's own colour | only where something is removed | corpus 2 of 7 · 2 renders, both confined to the contact |

- **The agent carries direction by its own form.** A wave spreads from its source, a stream has
  a nozzle end. Arrows appear in 3 of 7 and never say anything the agent's form does not;
  `03-mechanism-xray` recorded an unrequested arrow over a flow that already ran (1 render). Not
  asked for, and not banned until a render of this type shows one doing harm.
- **Nothing is drawn away from the contact place** (ADR-094). The agent, the removed matter and
  any label stay where the working end meets the body, and the body elsewhere carries no mark.
  The owner's comb runs drew a network of vessels across a whole head under a scalp brush, twice
  — a rendered body turned into a diagram of everything.
- **`removed` stays at the contact point.** Borrowed from `03-mechanism-xray` `MARKS/caught`:
  matter lifted in open space swirled through the volume and made the product the problem
  (1 render). **Tested here 2026-09-16 and it held 2 of 2**: pore plugs sat on the suction
  lines between skin and tip, callus flakes sat at the roller, and nothing drifted in either
  frame.
- **G3 meets heat and does not agree.** glowy-22 draws RF heat in red and orange; G3 gives orange
  to WRONG heat and red to pain. The namespace finding is that the market reaches for the colour
  of the phenomenon. G3 binds here as everywhere, so a heat product in this type is a
  contradiction no render has tested, and the founding set does not write one.

## SLOT CONSTRAINTS
- **The prompt budget** (ADR-013, ADR-015): a clause earns its place only after a render failed
  without it.
- **A15 binds every word**, as the owner settled it on 2026-09-16 (ADR-095): a figure enters
  only where `content.json` carries it. The corpus puts a figure in 6 of 7 frames and a source
  beside none. A figure the page supplies goes in the copy line, and the prompt then drops
  `a figure` and `a percentage` from the negative; a depth label stays out, because it is A13.
- **A13 binds the cut** — `PARTS/cut`. A depth label is A13 and A15 at once: glowy-23's
  `4.0mm / 4.5mm` is a precision a render cannot carry.
- **A2.** The frame shows the mechanism at the boundary as it happens. An outcome drawn on a
  body — a lifted jaw, a slimmer thigh — is a relief frame's job; feicemat-17's lift arrows say
  WOULD LIFT.
- **G8.** Where the product emits something visible, that output is the primary subject, as
  gallery-4's stream is.
- **G13.** No person in frame; the body is rendered anatomy. A frame that needs a face is not
  this type.
- **The text block sits at the top, above the scene**, 7 of 7. **The title says what happens,
  in the buyer's words, in 2–5 words** (ADR-094); the founding round's hooks ran eight and nine
  words and rendered exactly, and the worked examples keep them as rendered. **One copy line of
  at most 10 words** carries the mechanism in plain words, the one job the picture cannot finish
  alone — presumed earned in a mechanism tile, and still counted over the set.
- **One mechanism variant to a set** (`mapping/pdp-dr-rules.md`, rule 3).
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a figure, a depth label, a temperature, a frequency, a percentage, a person,
a face, an outcome drawn on a body, a generic tissue the copy does not name, a cut
deeper than the last named layer, the product floating beside the body, a badge, a seal,
a mark drawn away from the contact place, a label set on a line or on the product
```

## WORKED EXAMPLES
The two passes of the founding round, kept in full text because that text is the only record of
what actually rendered (SPEC §3.3). Both verdicts are the harness's own (ADR-011), so neither
can serve SPEC §6.3(3). Both were rendered at 0.1 and neither carries the two clauses 0.2 adds,
and both titles run longer than the band 0.4 sets — they stay as they rendered (SPEC §3.3).

### example: ems-pad-shoulder — skeleton@0.1, run: pass
```
Product photograph meeting a clean technical render of the body. One frame, no panels, no insets.

Use the attached product photo as the exact reference for the product.
Preserve its shape, proportions, material, finish and color exactly as shown.
Do not redesign, restyle, simplify or add features.
Render it at 30% of the frame height, integrated with the scene lighting, lying flat on the top of a shoulder at the centre of the frame, its pad against the skin, the whole product in frame.

The body is a clean matte technical render in pale, low-saturation tones, cut open beneath the pad.
The cut shows, from the surface down: the skin, a thin fat layer, the shoulder muscle. Nothing below the shoulder muscle is drawn.
The camera is level with the place they touch.

Fine pulses travel from the pad down through the fat layer into the shoulder muscle and stop there, drawn in clear cyan-blue and brightest at the pad.

Ground: one pale, near-neutral field, light in value and low in saturation, with nothing on it.

A headline across the top in bold grotesque sans-serif, sentence case:
"Unknot a stiff shoulder while you sit and read"
Under it, one line of dark grey medium-weight grotesque sans-serif:
"Gentle pulses reach the muscle beneath"
The headline and the line under it fill the top quarter of the frame, appear once, in one place, and nowhere else.
Nothing is placed in the bottom-right corner of the frame.
```
The whole-product case: at 30% of frame height the pad stays in frame entire, so nothing is
cropped and the contact edge is the only thing to read. The pulses enter under the pad and die
in the deltoid.

### example: scalp-massager-roots — skeleton@0.1, run: pass
```
Product photograph meeting a clean technical render of the body. One frame, no panels, no insets.

Use the attached product photo as the exact reference for the product.
Preserve its shape, proportions, material, finish and color exactly as shown.
Do not redesign, restyle, simplify or add features.
Render it at 50% of the frame height, integrated with the scene lighting, pointing down onto a close patch of scalp, its nodes pressed into the hair at the centre of the frame; the rest of it runs up behind the headline and out of the top edge.

The body is a clean matte technical render in pale, low-saturation tones, cut open beneath the nodes.
The cut shows, from the surface down: the hair, the scalp skin, the hair roots. Nothing below the hair roots is drawn.
The camera is level with the place they touch.

Vibration rings spread from each node down to the hair roots and stop there, drawn in clear cyan-blue and brightest at the nodes.

Ground: one pale, near-neutral field, light in value and low in saturation, with nothing on it.

A headline across the top in bold grotesque sans-serif, sentence case:
"Wake up a tired scalp right at the roots"
Under it, one line of dark grey medium-weight grotesque sans-serif:
"Soft nodes send vibration to the roots"
The headline and the line under it fill the top quarter of the frame, appear once, in one place, and nowhere else.
Nothing is placed in the bottom-right corner of the frame.
```
The A13 case, and the reason the closed layer list is in `PARTS/cut`. `03-mechanism-ghostbody`
drew a scalp comb into the cranium 2 of 2 with an unbounded cut; the same anatomy under a closed
list stopped at the roots, with the bulbs sitting in their own bed and no skull anywhere.

## BLOCK
**Criterion 1 is one source short**: feicemat-v2, fosen-ring, glowy-liff and densjet-nova, of
the five SPEC §6.3 asks. Three are beauty and body-contouring devices; densjet is the only one
outside that family, so the fifth source says most if it is not another face wand.

**Criterion 2 is unrun**, against two ACTIVE siblings, both copied into this folder:
- `03-mechanism-ghostbody` also opens the body, but on a whole anonymous figure in two panels,
  and argues why the product's SHAPE fits. This type zooms to one contact place and argues what
  the effect there is.
- `03-mechanism-xray` opens the PRODUCT; this type opens the BODY at the product's working end.

And it borders one proposal, `03-mechanism-emanation` (4 sources, no file), where the output
fills a space — a mist plume, a lamp's light, an airflow. Where the output meets a named body
structure at one place and the effect there is the subject, it is this type. `lp3-21hume-band`'s
sensing arcs through a wrist sit on that line and stay where they were filed.

**LP1 routes this type too, once it is promoted** (owner decision, 2026-09-16, ADR-095). The
promotion diff also writes it into `registry/types/`, as the parent of this file, and owes what
the register in `mapping/pdp-dr-rules.md` lists — LP1's criteria included. Criterion 2's two
siblings are LP1 types already, so the test above serves both folders.

**Criterion 3 has six renders and no owner verdict.** The founding round,
`sets/03-mechanism-contact-01/`, rendered 2026-09-16: two pass, four partial, every verdict the
harness's own, which ADR-011 excludes from promotion. Set 02 tests the two clauses 0.2 adds.

## KNOWN-FLAKY
Six renders, 2026-09-16, set `03-mechanism-contact-01`.
- **The state boundary did not render, 1 of 1.** The callus prompt asked for skin rough ahead of
  the roller and smooth behind it, with the roller's path as the line between (A8). The heel came
  back uniformly smooth apart from the flakes at the contact. One observation, so it stays here
  and the skeleton is untouched.
- **Three predicted failures did not occur and are struck** (`eval/render-test.md` §5, stale
  caution is noise): no figure or depth label appeared unasked in any of the six; no cut went
  below its last named layer, 4 of 4; no removed matter drifted, 2 of 2.

## CHANGELOG
- 0.5 (2026-09-17): two owner decisions of 2026-09-16 (ADR-095). LP1 routes this type once it is
  promoted, so `BLOCK` names what the promotion diff owes; a figure the page supplies may stand in
  the copy line without a source beside it. No clause about the picture moves.
- 0.4 (2026-09-16): the owner's gallery instruction for this type (ADR-094). The title says what
  happens in 2–5 words; one copy line of at most 10; optional 1–3 word `labels` beside a named
  structure; a dark key allowed; nothing drawn away from the one contact place, which two comb
  renders broke by drawing vessels across a whole head. One mechanism variant to a set. The
  worked examples keep their longer rendered titles.
- 0.3 (2026-09-16): the namespace gained the owner's four gallery rules (ADR-093). `PARTS/cut`'s
  camera line becomes a DEFAULT rather than a lock, so a page's set can vary its cameras under
  rule 3 without leaving this type. Nothing else moves, and no render is affected: all six of
  the founding round were shot level.
- 0.2 (2026-09-16): **founding round — six renders, two pass, four partial** (render-test ts
  2026-09-16; massage gun, EMS pad, blackhead suction, callus remover, scalp massager, cupping
  cup). The closed layer list held 4 of 4 and `removed` confinement 2 of 2, so neither is
  borrowed-untested now. Two clauses added: the cut is a WINDOW and the silhouette survives it
  (1 of 4 drew a segment); the `surface` form must say what makes the body DRAWN (2 of 2 came
  back photographic). `PARTS/target` gains the region test. Two worked examples, harness-graded.
- 0.1 (2026-09-15): drafted from seven observations across four distinct sources, batches
  2026-09-03-H, 2026-09-11-C, 2026-09-11-D and 2026-09-15-A, all seven frames opened first.
  Tier 2 at three sources in `_CURATION-2026-09-11.md`; the Densjet tile is the fourth. New
  device `contact`. Owner instruction, 2026-09-15. ADR-092.
