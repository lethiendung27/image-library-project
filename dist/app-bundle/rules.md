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
- **Yellow** = neutral structure (bone, frame) — and, inside an emoji badge only, the
  confirming half of the pair. See the emoji-badge carve-out below.
- No other color may act as a signal.

**Emoji-badge carve-out (ADR-042, owner decision).** A type may declare a verdict badge drawn
in the emoji idiom — a full-colour cartoon face rather than a glyph cut out of a signal-coloured
disc. Inside such a badge the palette above does not bind, for one measured reason: **emoji
carry their own colour vocabulary and it contradicts this one.** The angry face is red, which
agrees with G3. The smiling face is yellow, and there is no green smiling emoji to reach for —
a green face in that vocabulary reads as NAUSEATED. Honouring "green = confirmation" would
therefore invert the meaning of the confirming half. So the carve-out is not a preference, it
is the only way the two systems can both be obeyed.

It is scoped as narrowly as it can be: it applies only inside a badge a type has declared as
emoji-form, only to that badge's own fill, and it changes nothing about marks, structures or
any other colour in the frame. Yellow outside such a badge still means neutral structure, which
is what `02-cause-anatomy` and `03-mechanism-ghostbody` draw their anatomy in.

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

**Scope note — a declared text layer.** A type that declares `text_layer` in its
frontmatter draws words IN the frame under **G16**, and for that type alone this list's
`text, letters, numbers` is narrowed to everything G16 does not permit. Nothing else in
this list bends: `watermark, logo` and the four product clauses bind on a text-carrying
type exactly as they bind on every other. **No type in the registry declares a text layer
today**, so every statement of G6 elsewhere in this repo stands unchanged (ADR-064).

## G7 — Context integrity

**Scope:** photographic **scene layers** only. Not binding for: product cutouts /
circular insets / floating product views (read as graphic layers), and technical
registers (3D render, 2D illustration). `context_mode: declared-test` is a controlled
exception: staging is allowed but must look amateur, and only off-marketplace.

**Arranged product photography is a second controlled exception, and types opt into it
with `exempt_from: [G7]`.** A packshot, a lineup of variants, a still life of a material
and a flat-lay all exist only to be photographed, which is exactly what the Placement and
Reason tests refuse — so a type whose ARRANGEMENT IS THE ARGUMENT may take the exemption,
and it covers the arrangement and nothing else. Every other G7 test still binds: the
product is complete, nothing is cut open or half assembled, no component is missing. A
product cut-out on no ground needs no exemption at all; it already reads as a graphic
layer under the line above (ADR-064).

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

**An inset is sized by MAXIMISATION, never by a target number.** Owner rule, 2026-08-26:

```
Make the inset as large and as clear as it can be. It grows until it would cover
INFORMATION — the part of the subject the frame exists to show, or a face — or
until it would breach the safe area above. Then it stops.

It is never sized to a target. It has a FLOOR: the product inside it is never
smaller than a QUARTER of the frame width, and it fills its panel with only a
thin even margin. A type may raise that floor and may not lower it.
```

**Two corrections in that block, both paid for.** The stop condition used to read "cover the
subject" and that is too strict: what must not be covered is INFORMATION. A locator sitting on
the plain out-of-focus body of a macro subject reads fine — one did — while the same rule read
literally leaves nowhere to grow in a type whose own skeleton tells the subject to fill 70-90% of
the frame. **Two rules in one file were pulling against each other**, written a round apart, and
the inset lost.

And the floor is not the third target number. The two that failed were RANGES a render could sit
inside while still reading small, because the product did not fill the panel. A floor cannot be
satisfied by going small. It is set where the evidence sits: insets whose product filled the panel
at 25.4% and 31.1% of frame width read at a glance, and those at 21.2% and 16.6% did not.

**Two fixed numbers have already failed at this**, one round apart and in the same type.
`05-social-handoff` 2.6 bound the PANEL at 15-20% of frame width; 2.7 moved the bound to the
PRODUCT inside the panel, for the correct reason that a panel carries margin. Measured with a
detector calibrated on planted discs — 10, 20 and 30% read back as 10.0, 20.1 and 30.1 — six
panels then rendered between 16.6% and 31.1% of frame width, broadly compliant, and the owner
still read several as too small. **Panel size does not predict legibility.** What does is whether
the product FILLS its panel: a circle whose product fills the disc read at 25.4%, while a 16.6%
rectangle carried a sliver between wide margins and a 21.2% disc carried a small silhouette.

A ratio of product-to-panel would be the obvious instrument and it is not available: two attempts
to measure it failed their own controls. Maximisation needs no measurement, which is why it is
the rule.

Failures run in one direction. Across ten inset renders every miss was TOO SMALL except one panel
that was too large **and** misplaced — which this clause forbids anyway, because covering the
subject stops the growth.

**Where a type states its own inset bound, that bound stands and maximisation happens inside it.**
`06-relief-hero --detail` and `03-spec-explode`'s `inset` FRAMING mode both say 30-40% of frame
width. This clause tells a writer how to choose within a range, not what the range is.

`06-relief-hero` said 15-25% when this paragraph was written and was corrected at its 1.18 on
2026-08-27: a 15-25% panel cannot hold a product at the quarter-width floor above, so the type
was lowering a floor it may only raise. Its own three `--detail` renders measured 26%, 32% and
42% — none of them inside the band it declared — and the ledger notes rank legibility in that
order. **A type bound that no render obeys is not evidence, and this is the paragraph that was
deferring to one.**

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
{page-type}-{gif-type}-{product-slug}-v{NN}.mp4   the file the editor returns
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

**The filename is the session's own name with the gif type inserted, and it is read without
a lookup.** `{page-type}-{gif-type}-{product-slug}-v{NN}.mp4` (ADR-056 restoring ADR-037).
Take the session directory — `{page-type}-{product-slug}-v{NN}` (ADR-034) — and put the gif
type after the page type. A reader gets what it argues, for which product, and on which page
of that product, from the name alone — and the type names the library folder the file
belongs in.

Two things that are NOT in it and the reason each is out. The page id: it identifies the
source export, not the loop, and it lives in `prompts.json.page_id` where a join key belongs
— one routed session has none at all and still gets a name. The SLOT: it went in at ADR-051
and came out two days later on the owner's instruction; the join back to the frame lives in
`prompts.json` and on the plate, which the editor holds anyway.

**One loop per gif type per page, and the filename is why** (ADR-056 restoring ADR-037,
after a two-day demotion at ADR-051). There is no slot field and no sequence number, so two
loops that argue the same thing on one page would produce the same file. That is a rule
rather than a hazard: a page carries at most one `cause`, one `proof`, one `mechanism`, one
`relief`, one `use` — and it says something true anyway, that a page making the same kind of
motion argument twice is repeating itself. The build fails a page that breaks it.

**Version sits at the END, beside the product it counts.** A version is the Nth page for that
PRODUCT (ADR-034), so `v04` of one product and `v04` of another are unrelated numbers that
happen to match. A field meaningless without its parent belongs next to its parent; put it
earlier and a library folder sorts unrelated pages together while a product's own loops
scatter (ADR-036).

**Delivery is mp4** (ADR-047). It is what the editors actually produce, and a naming law
that disagrees with the files arriving is a law that gets ignored rather than followed.

Two consequences follow and neither is hidden. **Muted is a requirement again**: mp4 carries
an audio track and WebP could not, so what was moot by format is now a rule the brief states.
And an mp4 needs a `<video>` element with `autoplay`, `muted`, `playsinline` and `loop` where
a still sits in an `<img>`; ADR-036 chose WebP precisely so a loop and a still stayed
interchangeable in a page template. That interchangeability is now a **template dependency
outside this repo** rather than a property of the file, and a slot that earns motion needs its
template to carry a `<video>`.

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
suffix and a `.svg` extension and is never the slot's own asset filename. It travels beside the
still as its own file: ADR-019 required the work order to reach the editor rather than sit in a
document nobody opens, and a file named after the slot, sitting in the render folder next to the
frame it describes, satisfies that without putting model-drawn lettering into a frame G6 bans
text from. Since ADR-051 it is a second view of the spec block `prompts.md` carries rather than
the only carrier of it, and no render reserves anything for a loop to land in.

**Every still is a complete picture and ships on its own** (ADR-051, reversing ADR-033). No
render reserves, blanks or leaves empty any part of a frame for a loop to land in; insets are
drawn in full like every other layer the type legislates. A loop replaces the WHOLE slot asset
and is an upgrade to a slot that already works, so no render is ever unfinished waiting for
one. ADR-033 reserved the host layer as a flat empty block and recorded the consequence
honestly — such a render could not ship, and a flat empty block passes unnoticed as a design
element where the old lettering-covered plate could not. That risk is removed at the source
here rather than managed.

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

## G13 — A minor in frame

**Scope:** every frame of every type that can contain a recognisable person — scene
registers, ugc registers, insets and panels alike. **No exemptions.** This is not a style
rule. It is the difference between a prompt that runs and one the renderer refuses to
run at all.

A refusal is a different failure class from the weaknesses the adapter's Rule 5 collects,
and until now nothing in this repo had a place for it. A weak render can be re-rolled and a
wrong one can be patched; a refused prompt produces no image at all, so the constraint has
to sit before the writing rather than after the failure.

**Three rules for the writer. None of them is rendered into the prompt.**

1. **No private-room setting.** A frame containing a minor is never set in a bathroom, a
   bath, a shower or a bedroom. A kitchen, hallway, living room, garden, car, classroom or
   street has been available in every case the library has met, and none of them costs the
   argument anything.

2. **No age in years.** Never `seven years old`, never `a girl of about six`. Where the
   frame has to read young, `a school-age child` does it and the wardrobe and the scene
   carry the rest. A stated age is a signal in its own right, independently of whatever
   surrounds it.

3. **A minor's `Face:` block stays neutral.** Where a skeleton requires a face inventory, a
   minor's is limited to attention, effort or ordinary discomfort. Never `eyes screwed
   shut`, `eyes squeezed shut`, `mouth open`, `tearful`, `whimper`, `crying` or `grimace`.
   This is G9 arriving where it matters most rather than a new constraint fighting it: G9
   already ranks the symptom itself above gesture and says in its own words that emotion on
   a face is not evidence.

**Why three rules and not one clause.** No single clause is what gets refused.
`01-pain-scene`'s skeleton REQUIRES a force inventory, a face inventory, a private domestic
place, a covert gaze and a dark grade. Each is innocent, and making them co-occur in one
frame is the skeleton's whole job — that is what makes it editorial photojournalism rather
than a stock photo. Put a minor in the subject slot and those same mandatory blocks
assemble the exact feature bundle a child-safety classifier is built to catch. The three
rules above take the setting, the stated age and the distress out of that bundle.

**What they do not do, stated rather than implied.** They do not remove a minor from the
subject slot of a pain type. That was proposed on 2026-08-21 and the owner declined it, so
the residual stays: a force inventory and a covert gaze on a child subject. A frame can
therefore still be refused. When one is, the sanctioned move is the **object-only
execution** the type already legislates — the failed tool and its residue with nobody in
frame — rather than a softer adjective. Softening the face is what rule 3 already does; if
that was not enough, the subject is the problem and the object-only route is the answer.

**Evidence:** owner report, 2026-08-21, carrying the refused prompt — a girl of about seven
in school uniform on the edge of a bathtub, pulling away from a brush, `eyes squeezed shut`
and `lips parted in a tearful whimper`. Measured across the nine routed sessions the same
day: **96 prompts name a child, 91 name only a child's OBJECT** as background clutter and
carry no risk whatever, **4 place a young person in a relief scene** with no force and no
covert gaze and are fine, and **exactly 1 carries the full bundle**. So the rule is narrow
by measurement rather than by hope, and it costs the library's domestic texture nothing.

## G14 — A generated image may never pose as a customer's own

Two type files carried this in `avoid_when` until 2026-08-27, and `avoid_when` is gone
(ADR-060). It never belonged there: `avoid_when` said which CASES a type should decline,
and this is not a routing preference at all. It is the one line in this library that the
files themselves call **illegal**, so it moves where it binds every type at once.

**Never present a generated image as an actual customer upload.** Concretely, and these
are the two sentences as they were written:

- `05-social-snapshot`: *"NEVER pair a generated snapshot with a reviewer name, avatar,
  star row or verified badge, and never present one as an actual customer upload — that
  is a fabricated endorsement (FTC)."*
- `05-social-card`: *"When no real reviews exist: NEVER fabricate a quote, name, rating
  or counter — fabricated endorsements are illegal (FTC endorsement rules and
  equivalents)."*

**It binds the SLOT, not the type.** What makes an image a fabricated endorsement is the
furniture around it, not which type drew it. A review block carrying reviewer names and
`Verified Purchase` badges turns ANY generated image dropped into it into a claim that a
customer took that photograph. So the test is read off the page: if the slot sits beside a
name, an avatar, a star row, a verified badge or a review count, it takes a real customer
photograph or it takes nothing.

**When real customer photos exist, they always win over generated ones.**

**Measured on a live page, 2026-08-27.** `advertorial-cord-and-rope-tightening-and-cinching-tool-v01`
carries four `reviews.shots.*` slots in a block with three named "Verified Purchase"
quotes and the lead "Thousands of 5-Star Reviews Agree". Those four slots route to nothing
and the session records `out_of_scope_reason` rather than a prompt. The listicle template
TPL-ADV21 carries six photo slots in a review block with **no** name and **no** badge, and
there the same image is legal — which is the point: the slot decides, not the type.

## G15 — At 1:1 a multi-frame layout PACKS the square; it never stripes it

Owner instruction, 2026-08-27, with a diagram. Any type that lays out more than one frame —
panels, a split, a sequence, a rail, a grid — takes one of these forms when the slot's ratio
is **1:1**, and never N equal stripes:

| frames | form at 1:1 |
|---|---|
| 2 | **halves** — split down the middle or across it, either orientation |
| 3 | **1 + 2** — one rectangle and two squares. The rectangle may sit top, bottom, left or right, standing or lying; the two squares fill the remaining band |
| 4 | **2×2** — four equal frames |

**Why the stripe fails and the pack does not.** Three equal vertical panels in a 1024 square
are 341px wide each. Nothing this library draws survives that: a person, a product on a
surface, a hand at a fastening are all wider than they are tall. `02-cause-anatomy`'s
KNOWN-FLAKY reached the same place from the other direction after two renders duplicated a
canvas into a 2×2 grid — "compose wide-and-short subjects to fill a square frame".

**Reading order survives the pack.** In the 1 + 2 form the rectangle is read first and the two
squares left-to-right after it, so a sequence keeps its order and a before/after keeps its
direction. Where a type locks a side — `02-cause-anatomy` and `01-pain-split` put wrong on the
LEFT and correct on the RIGHT, locked library-wide — it has two frames and takes the halves
form, where that lock is untouched.

**This is a vocabulary for something two types already do.** `02-symptom-rail` is a hero at
72% with three vignettes down the right edge, and `05-persona-grid --1plus3` is one large cell
with three stacked beside it. Both are packs. G15 names the family and makes it the default at
1:1 rather than a per-type invention.

### NO TYPE IS EXEMPT AT 1:1. Two carry a narrower form of the rule

Owner correction, 2026-08-27: the exemptions belong to 16:9. **At 1:1 every multi-frame type
changes layout**, because the reason for the rule is that the square starves each frame of
information and that reason does not care which type is striping.

**`04-proof-lockedframe` uses the EQUAL forms only.** It is not exempt — it changes layout at
1:1 like everything else — but it may not take the unequal 1 + 2, because its own law is "no
panel may be favoured — no badge, no glow, no colour cue, no brighter exposure" and the file
says plainly that **the judgement rule IS the type**. A larger frame favours its panel by size,
the same defect in a different currency. So: **two panels are halves and that is the preferred
count at 1:1**, because two halves of a square give each panel four times the area of a third
band; three are three equal horizontal BANDS when the argument genuinely needs three; four are
2×2. Never vertical stripes, which is what its layout part said until 1.14.

**`03-use-sequence` takes the 1 + 2 form at 1:1**: PREPARE in the rectangle across the top,
USE and RESULT in the two squares below, left to right. The order survives the pack, which is
this type's entire discipline.

Its layout part says "Never describe the frame's shape or ratio", and that stands untouched —
but it bans naming the FRAME, not naming the ARRANGEMENT. The part's own first clause already
names an arrangement, "three photographs stacked one above another", so "one photograph above
two side by side" is the same kind of statement and not the kind the ban was measured against.
What still never enters a prompt is the frame itself: no "square", no "1:1", no "tall image".
That is the sentence's real content and it was read too broadly when G15 was first written.

**The ratio never enters the prompt** either way (adapter Rule 4, ADR-016): it is a generation
parameter. What the prompt names is the LAYOUT — "2×2 grid", "one rectangle above two squares"
— and the writer chooses that form knowing the slot's declared ratio.

## G16 — The text layer

**Scope:** only a type that declares `text_layer` in its frontmatter. Every other type
carries no words at all, and for those types G6 binds exactly as it always has.

G6 is not lifted, it is narrowed one type at a time. A declared text layer is the only
place a word may appear in the frame; `watermark`, `logo` and G6's four product clauses
still bind, and the prompt still asserts them.

### What the words must DO — the half this rule was missing

**Owner finding, 2026-09-03: the copy this rule produced was too weak to ship.** G16 as first
written capped LENGTH, fixed POSITION and refused CLASSES, and said nothing whatever about
whether a line was any good. A rule made entirely of limits produces text entirely within its
limits that does no work.

Measured — ten market headlines from the corpus this library learned from, against the ten
this rule's own test prompts produced:

| the market wrote | this rule produced |
|---|---|
| Get Medspa Quality Results At The Comfort of Your Home | THIS IS WHAT ARRIVES |
| Still switching shampoos while roots keep starving | EVERY PART, NAMED |
| THE PROTEIN YOU NEED, THE COFFEE YOU LOVE | SIX PARTS, ONE TOOL |
| Precision Bite. Maximum Holding Power. | THE PACK, AND WHAT IS IN IT |

Average length 8.0 words against 4.5, **and length is not the difference.** Every market line
names a RESULT, a FEELING or a PROBLEM STATE — something that happens to the reader. Every
line this rule produced names WHAT IS IN THE PICTURE. **A caption describes the frame; a hook
describes the reader.** The cap was never the constraint; the writer was choosing safety over
the job and no clause told them not to.

So each slot now carries a JOB, taken from the owner's own working instruction
(`product gallery img.txt`, the generator this library is being built to replace):

- **`title` is a HOOK.** It names the core idea or the emotion — the reader's result, the
  reader's problem, or a promise reconciled with the objection they were about to raise.
  **6–12 words is the band the market actually writes in.** Never a label for the frame's
  contents, never a category name, and never a sentence that would be equally true of a
  competitor's product.
- **`copy` does a DIFFERENT job from the title, never a restatement.** It adds exactly one of:
  proof, a timeframe, or the mechanism in plain words. 5–15 words. If deleting it loses
  nothing, it was a restatement and it should go.
- **`badge` is a STAMP**: one fact, four words, no verb needed.

**Each line earns its place by doing a job the line above it did not.**

### The block

| slot | job | shape |
|---|---|---|
| `title` | the claim | 1–3 lines, **≤ 7 words per line** |
| `copy` | the support | up to **three** separate lines, ≤ 7 words each, each may carry one simple line glyph |
| `badge` | one short stamp, its own cluster | **≤ 4 words** |

Reading order is title, then copy, one alignment, one typeface. The badge sits away from
the block.

**Where the 7-word line comes from.** The retired G12 plate format capped a line at seven
words and returned 20 of 20 lines exact across four renders on 2026-08-14; `05-social-card`
measured a single cluster at ≤ 12 words glyph-perfect in one pass. Two founding rounds on
2026-09-03 added **12 of 12** lines exact and then **13 of 13**, across seven renders and
four types. The cap now rests on 45 lines and no line has ever been observed to misspell.
**The seven-word figure is a LINE cap and it was read as a sentence budget** — which is how a
12-word hook became a 4-word caption. A 12-word hook set over two lines was always legal here.
That misreading, not the number, produced the copy the owner rejected.

**Owner waiver, 2026-09-03: the caps do not bind.** They record what has been measured and
nothing more. Write the line the copy needs; ten or fourteen words is unmeasured rather than
forbidden, and the render says whether it held. What a writer still owes is the record — a
line past seven words is noted in the render log, so the cap moves on evidence rather than on
habit.

### Never reserve space you do not fill

Round 2 of 2026-09-03 ran one type at two budgets on two products and inverted the
expectation. The **five**-cluster frame returned all five, once each, 13 of 13 words exact.
The **two**-cluster frame drew its whole block a SECOND time, lower and re-wrapped —
measured as seven ink bands where four were asked for.

So the count is not what binds. The two-cluster frame declared a large area empty and put
a short block in the top of it; the five-cluster frame declared the same area and filled
it.

```
The text area is sized to what the words actually occupy. A block that fills a
third of the area it was given will be drawn again to fill the rest.

Where the words are short and the field is large, the prompt says how much of the
picture the block occupies AND that it appears once, in one place, and nowhere else.
```

This is not a new mechanism: `adapters/nano-banana.md` Rule 4 records it for panels — "the
model fills the vertical space it has by repeating what it already drew". Round 2 is the
same finding in text. **A small block in a large empty field is the dangerous
configuration, not a large one.**

### Size, by maximisation

```
The block is as large and as clear as it can be. It grows until it would cover
the subject the frame exists to show, or until it would breach G10's safe area.
Then it stops. It is never sized to a target.
```

G10's own instrument, reused. Two fixed numbers have already failed at sizing an inset in
this library and a third here would fail the same way.

### Placement

1. **The block sits on ground the type's own skeleton has already left clear.** Never over
   the product, the subject, or anything the frame exists to show.
2. **One region, one block.** Where a type offsets its subject, the block occupies that
   offset space and nothing else does — two reservations for one area render as dead air,
   2 of 2 on `06-relief-hero`.
3. **Describe the region, never label it.** "In the upper left area of the picture, on the
   empty stone", never `TOP LEFT:` — adapter Rule 1b, measured on three types.
4. **Name the alignment as an observable.** "Every line begins at the same distance from
   the left edge of the picture", never "left aligned": the phrase "left aligned" was
   ignored 1 of 3 in round 1 and the observable held 4 of 4 in round 2.
5. **Nothing the prompt asks for goes in the bottom-right corner.** That corner carries the
   generation tool's watermark (`adapters/nano-banana.md` Rule 7, settled 2026-09-03). Three
   of three badges placed there were struck through by it; four of four placed bottom-left
   came back clean.

**G10's 8% is not reachable by asking, and this rule does not pretend otherwise.** Round 1
asked for "a clear margin on every side" and eight inked edges measured 5.3–7.4%. Round 2
asked explicitly for a tenth of the picture clear and nine edges measured 6.7–7.3%, one top
edge at 10.6%. Over-asking moved the FLOOR from 5.3% to 6.7% and moved nothing else: this
renderer holds a house margin near 7% whatever the prompt says. Nothing was cut in either
round. A text-carrying prompt therefore keeps asking for a tenth — that is what produced
the 6.7% floor — and **the breach of G10 is real and stated rather than hidden**. Two ways
out and neither is taken yet: ask for a sixth and see whether the house margin moves, or
amend G10 for text blocks on 17 measured edges. This is the shape ADR-061 already named — a
type bound that no render obeys is not evidence.

### Content — the half a re-render cannot fix

**The words come from `content.json` and from nowhere else.** Never from the model's own
knowledge of the category, never researched at write time. The same law `specification`
carries for component names and `colorways` carries for colour.

**This clause survives the waiver, and it is the one that FIXES the copy rather than limiting
it.** It does not say write blandly; it says the hook is written from the page's own argument,
which is the only place a hook can come from. What the owner caught was a writer with no copy
in hand inventing safe text instead of asking for the real thing. **Where a prompt is written
without a `content.json` — a test round, a demonstration — write the best hook the product's
own facts support and mark it as drafted copy. Do not retreat to a caption.**

**Owner instruction, 2026-09-03: the guardrails on text do not bind the writer.** What follows
is therefore a COST TABLE rather than a wall. Three rows are craft or economics and are waived;
two are recorded in this repo as law rather than taste, and they are marked so that striking
them is a decision somebody took rather than a side effect of improving the copy.

| the words may carry | what it costs · WAIVED or LAW |
|---|---|
| a price, a discount, a percentage off, a date | **WAIVED.** Cost: a re-render when the number moves. Measured in this corpus — one five-pouch photograph shot once and shipped twice under two headlines, and a claim tile shipped twice differing in one price figure |
| a second language | **WAIVED.** Cost: one render per language. A wordless still serves all 179 pages of the catalogue; a worded one serves the pages in its own language |
| a claim the product's own copy does not make | **WAIVED as a rule.** `argument-faults.md` A12 stands as the record of what it costs: a figure baked into a frame is a published claim the frame cannot substantiate, and three proposals are blocked behind that fault |
| a person's name, a rating, a star row, a review count, a "verified" mark | **LAW, not taste.** G14's own text calls a fabricated endorsement *illegal* under FTC endorsement rules, and G14 binds the SLOT rather than this rule — so G16 has nothing to waive. Strike it with an ADR if it should be struck |
| a certification mark, a press logo, an award, a named expert | **LAW, not taste.** A certification mark belongs to the body that issues it; this is a trademark question the library declined to answer on 2026-08-18 by leaving the `author` row empty. Same route: an ADR |

**One language per render, and the cost is stated rather than hidden.** A still with no
words serves every clone of a product — the catalogue runs 179 pages over 70 products across
English, German and UK domains. A still with words serves the pages in its own language
only.

### Style

Flat solid colour. No gradient, outline, drop shadow, ribbon or gradient bar. One typeface
for the whole block. Contrast against the ground is stated in the prompt, not assumed: dark
words on a white knockout, light words on a dark surface.

### What flips this rule

The standing evidence rule. If a text layer fails on ≥ 2/3 runs or across ≥ 3 observations
— words misspelled, block cut by an edge, cluster dropped or duplicated — that failure moves
the layer out of the frame and into the page, and this rule is withdrawn with its evidence
cited. G16 is a default, not a promise.
