# Global rules

Stable IDs. Types opt out only via `exempt_from` in frontmatter, and only where a rule's
**Scope** permits. Types reference rules by ID; rule text lives here and nowhere else.
Validator parses rule IDs from the `## G<n>` headers of this file.

---

## G1 — Product reference

**Scope:** every type with `requires_product_photo: true`. Exempt only when no product
appears in the image.

Mandatory block at the top of every prompt:

```
Use the attached product photo as the exact reference for the product.
Preserve its shape, proportions, material, finish and color exactly as shown.
Do not redesign, restyle, simplify or add features.
Render it from [angle] at [scale in frame], integrated with the scene lighting.
```

When the product appears in more than one layer (scene + inset, multi-panel), the block
gains: `The product must be identical in every layer of this image.`

## G2 — The PRODUCT slot carries only four kinds of information

**Scope:** every skeleton slot that places the product. No exemptions.

| Allowed | Forbidden |
|---|---|
| Position in frame | Shape, curves, material |
| Viewing angle | Color (except choosing among real colorways) |
| Scale in frame | Construction details (threads, ribs, locks, buttons) |
| Relation to other objects (mounted on, resting on, held in) | Any aesthetic adjective |

The reference photo carries the product's appearance; the prompt only places it.

## G3 — Color semantics (system-wide lock)

**Scope:** all types that use signal colors. Exempt: scene-register types that use no
signal color at all.

- **Red** = pain, wrong, broken. Appears only in "problem" areas.
- **Orange** = wrong pressure, wrong heat.
- **Blue / cyan** = correct support, correct flow, working mechanism.
- **Green** = confirmation badge only.
- **Yellow** = neutral structure (bone, frame).
- No other color may act as a signal.

## G4 — The correct side is always brighter

**Scope:** every comparison layout. Exempt: types with no wrong/right pair in frame, and
deliberately neutral proof layouts (lockedframe).

The "correct" side is always brighter, cleaner and airier than the "wrong" side. Never
inverted. On a page level the same arc applies: pain sections precede relief sections.

## G5 — Register lock

**Scope:** every frame that contains a comparison. Exemptable only with a stated reason
(e.g. `03-spec-split` uses photo-vs-render asymmetry as meaning).

Within one comparison frame both sides must share the same image register: both
photographic, or both illustrated. Never mixed — a register mismatch reads as two
sources and destroys trust.

## G6 — Base negative block

**Scope:** every prompt. Type negatives extend, never replace, this list.

```
text, letters, numbers, watermark, logo, deformed hands, extra fingers,
redesigned product, altered product shape, invented product details,
different product than reference
```

Adapters may translate this canonical list into model-appropriate form
(see `adapters/`), but the canonical form is model-agnostic.

**Scope note — diegetic vs overlay text.** The ban targets OVERLAY text: captions,
labels, badges with words, spec callouts added on top of the image. DIEGETIC text —
text that exists on a photographed or rendered object itself (a product's screen UI,
an instrument's readout, a handwritten label on a prop) — is content, not overlay,
and is permitted. Production rule: screens and readouts are never model-drawn;
render or photograph the real interface and composite it in post. Evidence: 6+
ledger observations (BP-monitor displays, dB meters, disc labels), batches D-E.

## G7 — Context integrity

**Scope:** photographic **scene layers** only. Not binding for: product cutouts /
circular insets / floating product views (read as graphic layers), and technical
registers (3D render, 2D illustration). `context_mode: declared-test` is a controlled
exception: staging is allowed but must look amateur, and only off-marketplace.

```
Every object in frame must appear in a state, position and setting it would
genuinely occupy during real use, real installation or real inspection.
Nothing may be cut, floated, disassembled, clipped, propped or arranged
in a way that only exists to make a photograph.
```

Three tests — the image must pass all three:

1. **Completeness.** Devices in frame are complete; if the product mounts onto something,
   that something is present and whole.
2. **Placement.** Objects sit where a real person would put them.
3. **Reason.** There is a plausible reason this scene exists and is being seen.

**G7-X — Cross-layer consistency.** When more than one layer shows the product, every
layer must depict the **same mode of use**. Installed in one layer and handheld in
another is a contradiction even when each layer is plausible alone.

Negative additions:

```
implausible setup, staged test rig, product half installed, missing components,
device shown incomplete, cut-open product, object floating in a real scene,
item propped in an unnatural position, arrangement that only exists for the photo
```

## G8 — Visible mechanism

**Scope:** photographic hero/scene layers of product-in-frame types. Origin:
`06-relief-hero` v1.2–v1.3 patches, generalized (ADR-003).

If the product emits, produces or moves anything visible (mist, spray, steam, foam,
water, particles, light), that output is the primary subject of the frame: frame, light
and expose to reveal it (backlight / side rim light; subject between light and camera).
It is the only proof the image carries — losing it loses the argument. If the product
produces nothing visible, do **not** invent an effect; use the default lighting of the
type.

## G9 — Physical evidence over expression

**Scope:** scene-register types (no graphic overlays), especially those without a
product in frame. Origin: `01-pain-scene` v1.1 patch, generalized (ADR-003).

Emotion on a face is not evidence — a grimace can mean anything. The symptom or result
must be visible as physical fact. Rank available evidence and use the strongest present:

1. the symptom/result itself on the body or object;
2. physical residue or debris it produces;
3. the failed tool still in hand;
4. gesture alone (weakest — if used, at least one object in frame must independently
   imply the problem).

## G10 — Frame safety

**Scope:** every layer of every type — insets, product views, panels, rails, badges,
and any text a type is permitted to carry. No exemptions: a layer leaving the frame is
not a style choice, it is a defect.

```
No text and no product may touch or cross a frame edge. Keep every element at
least 8% of the frame width from the left and right edges, and 8% of the frame
height from the top and bottom edges.

Content inside a shape is centred on the part of the shape that is INSIDE the
frame, never on the shape's true centre.

A shape may bleed off a corner by at most 10% of its size on each bleeding edge
— a thin crescent, never a quadrant.

When content does not fit the safe area, make it SMALLER. Never move it outward,
never let it run off, never widen the shape.
```

The last clause is the load-bearing one: a prohibition without a sanctioned escape
route is resolved by the model in whichever direction it likes, and outward is the
direction that breaks the frame.

Evidence: render tests 2026-08-11 (`06-relief-hero`, wet-dry floor washer and travel
stroller). A bleed specified as "a quarter of the shape" pushed a four-line label off
the frame; the same session cropped a static product inset by the identical mechanism.
The failure is medium-independent and type-independent, which is why it lives here
rather than in a type file.
