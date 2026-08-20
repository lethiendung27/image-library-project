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

## G11 — Saturation carries the state

**Scope:** photographic layers that depict a state as part of their type's argument —
the problem, the wrong way, the past, the legacy solution, or the resolved state after
buying. **Not binding for:** technical registers (3D render, 2D illustration), where the
palette is set by the render rather than by the argument; and deliberately neutral proof
layouts, which opt out via `exempt_from: [G11]` — `04-proof-lockedframe` does, because
its own `[GRADE]` slot legislates this differently and on purpose (one grade for the
WHOLE image, polarity never between panels).

```
An UNRESOLVED state is marked as unresolved. Desaturation is the default
instrument: reduced saturation or grayscale, cool or neutral, never warm.
A RESOLVED state is high-key: brighter, airier, full colour, never boosted
past plausible.

Where both states appear in one frame, the difference between them is a
REQUIREMENT, not a stylistic option — it is what makes two states read as two.

Where only ONE state appears, this rule sets the ABSOLUTE grade of the frame.

A type may substitute an explicit signal mark for desaturation — a red hotspot,
glow or X per G3 — where its own skeleton says so; `02-symptom-rail`'s vignettes
and `06-relief-hero --recall` both already do. What is forbidden is an unresolved
state carrying NO marking of any kind.
```

The single-state clause is the load-bearing one, and it is the half **G4 never covered**:
G4 governs relative brightness between the sides of a comparison and says nothing about
an image in which every layer is a failure. That gap is how three panels all meant to
read as unsolved rendered cheerful.

**Evidence.** The convention was practised in seven types and stated in none:
`01-pain-scene`, `01-pain-split`, `02-symptom-rail`, `03-spec-split`, `06-relief-hero`,
`06-relief-scene`, and `04-proof-lockedframe --rivals` in whole-image form. Its absence
produced a real failure — the `--rivals` drain-unblocker triptych of 2026-08-12
(`eval/render-tests.jsonl`), which drove `04-proof-lockedframe` v1.5 and whose CHANGELOG
proposed exactly this rule and deliberately declined to take it.

Market imagery will not teach it. Three ledger observations record source images
declining to desaturate the wrong panel at all — obs `sha256:4f24b8…`, `sha256:6ab523…`,
`sha256:cf4c74…`, all on `01-pain-split`, all "full colour, only duller and flatter".
Those three met the ≥3 threshold pointing the OPPOSITE way, and the library declines to
import them, exactly as it declines the VS-badge dialect (nine observations, recorded in
`01-pain-split`'s CHANGELOG). No practising type's skeleton is weakened by this rule.
G11 exists because the library's own practice is not inherited from the market — which is
precisely what made leaving it unwritten expensive.

## G12 — The motion brief plate

**Scope:** a slot whose `gif` verdict is positive. The plate is the work order the editor
who builds the loop reads, and it carries **four fields and nothing else**:

```
{page}-{seq}-{gif-type}-{slot-slug}.mp4        the file the editor returns
{duration} · {ratio} · {loop behaviour}        what shape and how long
                                               a rule across the two
<the brief>   who or what is in the shot and where, what happens in
              order, and what it leaves the viewer with
```

**The brief is a shot description in plain words**, of the kind you would say out loud to
the person holding the camera. Three movements and no labels: who or what is in the shot and
where; what happens, in the order it happens; what that leaves the viewer with. Measured band
**25 to 55 words** (ADR-029, ADR-031).

**Everyday words, not craft words.** "The gap behind his lower back" and "springs back to its
full thickness" are briefs. "The front lip of the base" and "the slow-rebound contour returns
to full depth" are a type file talking to itself. The editor is the reader.

**Nothing about light, grade or register** (ADR-030). The still the loop accompanies carries
all of it and sits in the same folder; restating it is what produced the page 73 fault, where
a boilerplate register line claimed a room the frame did not have. Removing the field removes
the fault.

**The upshot belongs; the routing argument does not.** "Sitting in that gap day after day is
what starts the ache" is the point of the shot and an editor frames for it. "The declared
reason this section exists is temporal, so the slot earns a loop" is why the pipeline chose
the slot — that is `gif.reason`, and the editor never opens it.

**Name the force.** An object does not move on its own: a pad creeps forward because a body
is on it and the car brakes. Where the loop needs a person the still does not have, the
verdict is a re-execution and `gif.reason` says so.

**A multi-beat loop needs no second format.** The beats run in order inside the description,
separated by commas with a final `then`. Four is the ceiling any routed slot can reach —
`use` declares [1, 4] and every other routable type declares less. `unboxing` goes to six and
is `kind: null`, ad channel only, so it never writes a page brief.

**The filename carries the ARGUMENT, not the still type it replaced.** `06-relief-hero
--recall` hosting a `pain` loop used to produce a file called relief-hero, which named the
wrong thing to the one person who has to file it. The page still numbers by page and an
editor still tracks by slot; the gif type sits between them.

**The ratio is the SLOT's, not the still type's.** On `whole-frame` the loop IS the
delivered image, so it owes the page's shape rather than the shape the still happened to be
rendered at. The plate is drawn at that ratio, so the card is the shape of the deliverable
and the editor reads the aspect off the paper as well as out of it.

**The plate is GENERATED, never drawn by an image model** — `python3 scripts/gen-plate.py`,
and like `registry/index.yaml` and the GIF library's folder cards it is a view that is never
hand-edited. This is the rule's largest change and the evidence for it is the rule's own
history: the five-line format existed because a model draws text badly, and every constraint
below the fields was a workaround for that. A generated card cannot misspell a filename,
cannot return `**GIF SLOT**` with its asterisks intact, cannot wrap a line into the next
one, and costs no generation call. The brief is prose because a prose brief is what a person
actually needs; prose means wrapped lines, and a wrapped line is the one failure the old
format had actually measured.

**The plate never ships.** A page asset carrying one is a defect, so it takes the `--brief`
suffix and a `.svg` extension and is never the slot's own asset filename. On `inset` the
host type's own prompt reserves the legislated layer as a flat empty block carrying no text
at all, and the plate travels beside the still as its own file: ADR-019 required the work
order to reach the editor rather than sit in a document nobody opens, and a file named after
the slot, sitting in the render folder next to the frame it describes, satisfies that without
putting model-drawn lettering into a frame G6 bans text from.

**The plate is a claim about THIS frame, and G7 binds it exactly as it binds the picture.**
What the brief names has to be present and possible in the still: a brief promising a grime
strip turning clean needs a grime strip in frame, and one promising the same room and light
as the still needs the still to have a room. Two of four failed here and it was the dominant
fault; a third was found on page 73 after shipping, where a brief said "same room and light
as still" over a see-through render standing on a plain slate ground. **This is the clause
that survives the change intact, and the field list is what makes it checkable** — the old
quartet had no field for the setting, so the setting was smuggled into `MATCH`, and a
boilerplate `MATCH` line is exactly what nobody re-reads against the frame.

**Retired with the model-drawn plate, and recorded rather than deleted:** the seven-word
line cap, the plain-words rule against markup, the corner and footprint inheritance, the
one-third-to-one-half size band, and the name-where-it-stops clause. Every one of them was
earned by a render and every one of them is a property of a renderer that is no longer
involved. They are in `git log` for the day a model draws reliable lettering and the
question reopens.

**Evidence:** ten renders on 2026-08-14, eight carrying a plate. The four run against the
old rule returned every line exact — 20 of 20, including one carrying nothing but text — so
model-drawn lettering was settled and the geometry never was. That is the measurement that
retires the rule rather than contradicting it: the format was working and it was working at
the cost of a constraint list no field could grow past. Motion itself is still untested: no
loop exists in `eval/render-tests.jsonl`, and `ingestion/gifs.jsonl` holds no record.
