---
id: 03-mechanism-contact
step: 3
job: mechanism
device: contact
version: "0.1"
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
blocked_by: "Criterion 1: four distinct sources of the five SPEC 6.3 asks. Criterion 2, the router-confusion test against 03-mechanism-ghostbody and 03-mechanism-xray, is unrun. Criterion 3 has no render."
---

# 03-mechanism-contact — PDP-DR DRAFT

Promotion status (2026-09-15): **4 distinct sources, 7 observations — criterion 1 is one
source short.** Drafted on the owner's instruction to build types from the Densjet gallery,
whose tile 4 is this construction. ADR-078 withheld every Tier-2 id because a count had once
been taken for evidence (`07-identity-callout`, two of five frames really that device). So
all seven frames below were opened and looked at before this file was written, and **every
source carries at least one frame that is unambiguously this device.**

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
TYPE: 03-mechanism-contact v0.1
REGISTER: product photograph meeting a clean technical render of the body.  -> PARTS/register

[PRODUCT REFERENCE]  the attached photo is the exact reference.        -> G1
[WORKING END]        the part that touches, and where it touches.      -> PARTS/working-end
[TARGET]             the body structure the copy names, rendered.      -> PARTS/target
[CUT]                section | surface                                 -> PARTS/cut
[AGENT]              what crosses the boundary, drawn as itself.       -> MARKS/agent
[REMOVED]            only where the product takes something away.      -> MARKS/removed
[GROUND]             quiet by default.                                 -> PARTS/ground
[TITLE]              the claim, as a hook.                             -> G16/title
[COPY]               the mechanism in plain words.                     -> G16/copy

Nothing in the frame is marked that is not named here.
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

**`cut`** — a parameter, and the copy picks it.
- `section`: the body cut open under the working end, 6 of 7. **Depth is DERIVED, never
  chosen** (A13): name the layers as a closed list from the surface, ending at the first layer
  below the deepest structure the product reaches, and draw nothing deeper. Borrowed from
  `03-mechanism-ghostbody` `PARTS/cutaway`, where an unbounded cut took a scalp comb into the
  cranium 2 of 2. **Untested in this type.**
- `surface`: the body's outer surface seen close, not cut, where the effect shows there — a gap
  between teeth, a heel, a pore. 1 of 7: gallery-4, the owner's example.

The camera is level with the place they touch — feicemat-16's record, and the geometry all
seven share.

**`ground`** — quiet by default (`registry/pdp-dr-instruction.md`, ADR-068): light in value,
close to neutral. Pale blue, lilac, pink and blue-white in 6 of 7; glowy-22's panel is lit red
from within by its own heat glow.

## MARKS

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `agent` | what crosses the boundary, in the phenomenon's own form — pressure rings, wave lines, fine pulses, beams, the stream itself — leaving the working end and stopping at the target | clear cyan-blue (G3: working mechanism); a liquid keeps its own colour | one family | corpus 7 of 7 · 0 renders |
| `removed` | what the product takes away — debris, a plug, flakes — leaving the target only at the contact point | the matter's own colour | only where something is removed | corpus 2 of 7 · 0 renders |

- **The agent carries direction by its own form.** A wave spreads from its source, a stream has
  a nozzle end. Arrows appear in 3 of 7 and never say anything the agent's form does not;
  `03-mechanism-xray` recorded an unrequested arrow over a flow that already ran (1 render). Not
  asked for, and not banned until a render of this type shows one doing harm.
- **`removed` stays at the contact point.** Borrowed from `03-mechanism-xray` `MARKS/caught`:
  matter lifted in open space swirled through the volume and made the product the problem
  (1 render). Untested here.
- **G3 meets heat and does not agree.** glowy-22 draws RF heat in red and orange; G3 gives orange
  to WRONG heat and red to pain. The namespace finding is that the market reaches for the colour
  of the phenomenon. G3 binds here as everywhere, so a heat product in this type is a
  contradiction no render has tested, and the founding set does not write one.

## SLOT CONSTRAINTS
- **The prompt budget** (ADR-013, ADR-015): a clause earns its place only after a render failed
  without it.
- **A15 binds every word.** A figure enters only where `content.json` carries it with its
  source, and the source is set beside it. The corpus puts a figure in 6 of 7 frames and a
  source beside none.
- **A13 binds the cut** — `PARTS/cut`. A depth label is A13 and A15 at once: glowy-23's
  `4.0mm / 4.5mm` is a precision a render cannot carry.
- **A2.** The frame shows the mechanism at the boundary as it happens. An outcome drawn on a
  body — a lifted jaw, a slimmer thigh — is a relief frame's job; feicemat-17's lift arrows say
  WOULD LIFT.
- **G8.** Where the product emits something visible, that output is the primary subject, as
  gallery-4's stream is.
- **G13.** No person in frame; the body is rendered anatomy. A frame that needs a face is not
  this type.
- **The text block sits at the top, above the scene**, 7 of 7. `title` is a hook (G16);
  `copy` carries the mechanism in plain words, the one job the picture cannot finish alone.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a figure, a depth label, a temperature, a frequency, a percentage, a person,
a face, an outcome drawn on a body, a generic tissue the copy does not name, a cut
deeper than the last named layer, the product floating beside the body, a badge, a seal
```

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

**Criterion 3 has no render.** `sets/03-mechanism-contact-01/` is the founding round.

## KNOWN-FLAKY
- **Nothing observed.** No render exists for this file.
- Predicted, from the corpus and two siblings: a figure or depth label appearing unasked (6 of 7
  corpus frames carry one, and `03-mechanism-xray` records a spec label arriving from its seed);
  a section cut deeper than the last named layer (A13, 2 of 2 on `03-mechanism-ghostbody`);
  removed matter spreading through the frame (`03-mechanism-xray` `caught`, 1 render).

## CHANGELOG
- 0.1 (2026-09-15): drafted from seven observations across four distinct sources, batches
  2026-09-03-H, 2026-09-11-C, 2026-09-11-D and 2026-09-15-A, all seven frames opened first.
  Tier 2 at three sources in `_CURATION-2026-09-11.md`; the Densjet tile is the fourth. New
  device `contact`. Owner instruction, 2026-09-15. ADR-092.
