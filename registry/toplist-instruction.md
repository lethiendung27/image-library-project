# Toplist instruction — law shared by every toplist type

Stated once here and **never restated in a type file**, exactly as
`registry/gif-instruction.md` treats the motion registry and as SPEC §5 treats the
global rules. A toplist type file carries what is different about that type and
nothing else.

Read this before `registry/toplist-types/<id>.md`. SPEC §3.7 is the contract; this
file is the working law under it.

## What this namespace is for

**One image.** A top-N listicle — "the best 5 X of 2026" — carries a single lede image
(lead image, featured image, hero) and then goes to text. Everything else on the page is
a product card, and product cards are not this library's business.

That single fact is the whole reason for a third namespace. With one slot, over half of
SPEC §7 has nothing to act on:

| SPEC §7 step | in a top-N page |
|---|---|
| 2 · Stage 1 shortlist by role affinity | **dead** — one slot, one role, so affinity is a constant |
| 3 · Stage 2 portfolio, cross-slot rules | **dead** — `never_with`, `avoid_adjacent`, `pairs_with`, one-type-once all need a second slot |
| 5 · coverage pass over Trust Ladder rungs | **dead** — one image cannot cover a ladder |
| 4 · three options, three distinct types | **alive and still the deliverable** |
| 6 · at least two variations | **alive** |
| 8 · adapters at render time | **alive, unchanged** |
| 9 · picks ledger | **alive, and see SELECTION below** |

Keeping the dead half alive in a one-slot format is machinery that cannot run. That is
the same reasoning SPEC §3.6 gives for gif types reaching their registry by id rather
than through a shortlist.

**And N is FIVE.** Owner, 2026-09-09. The format is not an open-ended list this library
sizes to taste: **a top list is written about five products**, so a type that shows the
FIELD shows five of them and a prompt that builds one asks for five. It governs the
`use_when` of every type that carries more than one unit.

**Two things already sit across it, and both are named rather than smoothed over.**

- **Layer 1's admission gate does not say five.** `mapping/toplist-rules.md` refuses
  `products_in_frame: many` on an input carrying fewer than THREE distinct products, and
  no decision in the log says why three. Whether the gate should rise to five is a routing
  decision and it waits on `products[]` existing at all.
- **`lede-collage` holds three corpus frames carrying ONE product** — two `split-frame`,
  one `polaroid` — against its own `products_in_frame: many`, and two of its rendered cells
  are built that way. Whether this namespace admits a one-product collage is the owner's
  call; that file flags it and deliberately leaves its frontmatter alone, because the value
  is a routing promise.

Neither is decided here. The format fact is stated; where a type or a gate disagrees with
it, the disagreement is the record.

Recorded in `lede-collage.md` first, and moved here on 2026-09-10 because it was never
that one type's own.

## Input is the PRODUCT block, not `content.json`

`content.json` is `{ product, page }`. A top-N page has no `page.sections` to route and,
since ADR-059, `page.channel` admits nothing. So this namespace consumes the `product`
half alone, extended.

**What the product block already carries** and every type may read:

| field | what it is | machine-readable |
|---|---|---|
| `attributes` | 8 keys, mostly closed enums | **yes** — the gates below run on it |
| `problems_solved[]` | what the buyer suffers | no, prose |
| `personas[]` | who the buyer is | no, prose |
| `specification` | the manufacturer's own line, verbatim | no, prose |
| `raw_features[]` | feature claims as the brief states them | no, prose |
| `reference_photos[]` | sha256 hashes; **empty is a statement, not a gap** | yes |
| `name`, `category` | identity | yes |

**What a top-N page needs that the block does not have yet**, named here so a reader is
not surprised by an absence:

1. `products[]` — the schema carries exactly ONE product; a top-N is five. Since ADR-076
   this no longer reserves a type: `lede-lineup` and `lede-collage` are ACTIVE and declare
   `products_in_frame: many`, and the absence refuses the PAGE at layer 1 rather than the
   type. Every page routable today is refused, because every input carries one product.
2. a rank or verdict per product — "Best Overall", "Best Budget". Nothing carries it.
3. test facts — what was measured, with what. `lede-testing` works without them and
   would be better with them.
4. `category` is one coarse string (`home`); a top-N is about a narrow category.

`awareness` IS carried on the input. See SELECTION for how little it is trusted.

## SELECTION — four layers, and only one of them uses awareness

The owner's instruction of 2026-09-09 was to carry awareness but not to lean on it. This
is the shape that obeys it: the two layers that can REFUSE a type are mechanical and
awareness-free, and awareness only orders what survives.

**Layer 1 — mechanical admission. Refuses. No judgement, no awareness.**

- `status: reserved` → not routable, ever.
- `products_in_frame: many` → needs `products[]` with ≥3 entries and one reference photo
  per unit. The attachment cap was lifted at ADR-076, so this no longer refuses a type; it
  refuses a PAGE whose input carries fewer than three products.
- `requires_product_photo: true` with `reference_photos` empty → refused, and say so in
  the session notes rather than shipping a prompt the owner cannot run.
- The `product.attributes` gates of `mapping/toplist-rules.md`, which **restate by
  toplist id** every gate a copied type should carry. A gate in `mapping/slot-rules.md`
  names the parent and does not reach a copy — see *Copying* below. Live example:
  `result_visibility: invisible` drops `06-relief-scene` there and `lede-inuse` here, and
  the second line exists because the first one cannot do the work.

**Layer 2 — preference order. Orders. This is the only place awareness is read**, and
`mapping/toplist-rules.md` says in its own first paragraph that it is a hypothesis with
no evidence behind it.

**Layer 3 — FIT, by judgement, on `use_when` and `BOUNDARY` against the product prose.**
This is what actually decides, and the library has known since ADR-059 that "judgement
does not scale and no regex audits it". The mitigation ADR-059 named is the one this
namespace adopts as law: **every choice cites the sentence of product copy that decided
it**, which turns a judgement into a record somebody can audit later.

**Layer 4 — pick rate.** `feedback/picks.jsonl` per SPEC §7.7, at ≥20 contested
observations per cell. It holds 0 records today. One slot per page means one record per
page and a cell keyed on the type alone, so **20 pages make this real** — the fastest
this prior can fill anywhere in the library, and the reason this format is worth
measuring rather than arguing.

## Text: some types carry one, and G16 binds them

**A toplist type MAY bake words and a badge into the frame** — owner decision, 2026-09-09
(ADR-071), reversing the constraint of the same day that this file was first written on.
The corpus classified in batches 2026-09-09-A/B agrees: **7 of 32 reference frames carry
baked text**, including both forms the owner named — a winner packshot under a verdict
band, and a cut-out collage under a "BEST X" line.

**Which types carry one is decided by evidence, not by permission.** Two do:

| type | `text_layer` | why |
|---|---|---|
| `lede-winner` | `[title, badge]` | the verdict mark IS the type — strip it and `07-identity-pack` already does the picture |
| `lede-collage` | `[title, badge]` | the market form the owner named, and **2 of the 3** corpus collages that are actually several products carry an award badge |

The other five do not, and that is the corpus talking rather than a rule: **5 of 5**
`lede-lineup` observations carry no text at all, and **10 of 11** `lede-testing`
observations carry none — the single exception is a video thumbnail rather than a page
lede. Adding a text layer to those two would be a clause with one observation against ten.

**So G16 binds this namespace after all**, on exactly the types that declare the key —
four rounds of measured work on line caps, the badge interior, the mobile floor, the
size anchor and the watermark corner arrive intact and are not restated here. No ground rule is imported from
that work: this namespace measures its own, below.

**What is still refused, and it was not part of the instruction.** The owner permitted the
PAGE'S OWN verdict about its own ranking. Two of G16's content rows are marked `LAW, not
taste` and neither was addressed:

- **another party's mark** — a certification seal, a press logo, a third-party award. The
  corpus carries these (`CNET LAB TEST WINNER`, `CNET PEOPLE'S PICKS`) because on CNET's
  own page CNET is the issuing body. On a page that is not theirs it is a trademark
  question, and the library declined to answer that one on 2026-08-18.
- **a fabricated endorsement** — a customer's name, star row, review count or verified
  mark. G14 calls it illegal under FTC endorsement rules and binds the SLOT rather than
  the type, so there is nothing here to waive.

A publisher's own SCORE sits between them and is permitted with a leash: it is a figure,
so `argument-faults.md` A15's working position holds — **the number enters the frame only
where the product input carries it**, never where a prompt invents one.

## Ground: built from this corpus, and from nothing else

**No ground rule is imported into this namespace** (owner instruction, 2026-09-09;
ADR-073). ADR-068's finding was measured on 119 direct-response product-page frames and
was carried in here twice — once whole, once half-corrected — and both times it was a rule
about a different kind of picture. What follows is measured on the 32 frames of
`stills/top list/`, classified in batches 2026-09-09-A/B, and on nothing else.

**One measurement splits the namespace in two, and it is not colour.** The mean
adjacent-pixel difference in the outer 8% ring — call it TEXTURE — separates a ground that
was DESIGNED from one that was PHOTOGRAPHED, with no overlap:

| family | n | texture | value | saturation | ring spread |
|---|---|---|---|---|---|
| `lede-winner` | 1 | **0.8** | 0.91 | 0.60 | 0.15 |
| `lede-collage` | 5 | **1.9** | 0.90 | 0.49 | 0.25 |
| `lede-lineup` | 5 | **2.9** | 0.81 | 0.26 | 0.33 |
| *proposed* `lede-mosaic` | 3 | **2.8** | 0.76 | 0.43 | 0.35 |
| `lede-authority` | 3 | 7.0 | 0.67 | 0.15 | 0.51 |
| `lede-testing` | 11 | 7.1 | 0.65 | 0.13 | 0.67 |
| `lede-inuse` | 1 | 10.0 | 0.16 | 0.26 | 0.34 |

Everything at or under 2.9 is a made surface; everything at 7.0 and over is a room. There
is nothing between 2.9 and 7.0 in 32 frames.

**The split has an exposure floor, found by the founding render round and measured in both
directions.** Texture is a mean ABSOLUTE pixel difference, so it scales with how much light
is in the frame. Round 2's `lede-pain` render — a photograph of a real office at dusk —
measured texture **2.8** and was filed DESIGNED. The same two pictures, with nothing changed
but their exposure:

| the SAME frame, brightness × | value | texture | reads as |
|---|---|---|---|
| `lede-pain` render, ×1.0 | 0.25 | **2.8** | DESIGNED |
| `lede-pain` render, ×2.8 | 0.69 | **5.1** | photographed |
| `lede-authority` render, ×1.0 | 0.64 | **6.8** | photographed |
| `lede-authority` render, ×0.4 | 0.25 | **2.7** | DESIGNED |

A real room crosses into the designed band at about **value 0.35–0.40**. Every one of the
32 corpus frames the split was measured on sits at value 0.65–0.90, so **nothing above is
wrong — it is bounded**: texture separates a made surface from a room only on a frame that
is actually lit. Below that, read `spread_v` instead, which holds its side down to at least
value 0.19 and is what says *real light falls off*.

**The obvious repair was tested and is NOT applied.** Requiring `spread_v < 0.35` alongside
the low-texture branch of `designed()` re-files **five corpus frames**, including the alarm
clocks frame that carries `lede-lineup`'s median of 2.9 and therefore ADR-073's finding that
this type sits on the designed side. A fix that moves corpus frames is a curation change
wearing a bug fix's clothes, and it belongs to a curation pass rather than to a render round.

**A second limit, and it is new.** On a type that declares a `text_layer`, the ring measures
the WORDS. Round 2's `lede-collage` render read texture 4.3 on a perfectly smooth gradient
because its title runs edge to edge through both side ring bands. ADR-073 never had to state
this: no frame it measured carried baked text at the frame edge.

**A third limit, and it is the largest: the ring assumes the ground REACHES the frame edge.**
ADR-073 measured 32 frames whose ground was one field, so it did. `lede-collage` now carries
eight named layouts and on most of them the outer 8% band is not ground at all. Measured
across the six renders of that type's set 6, 2026-09-10:

| layout | what the ring actually sampled | ring value / sat |
|---|---|---|
| `open` | **the ground.** Usable | 0.91 / 0.73 |
| `colour-cells`, `rounded-cells`, `outlined-panels` | whichever CELLS reach the edge | 0.97–0.99 / 0.04–0.99 |
| `blocks` | **the white page behind the blocks** | 1.00 / **0.00** |

**The `blocks` frame is the control that fails.** Its composition argues in blue, green,
orange and yellow, and the ring returns saturation 0.00, because the blocks float on a white
page and never touch the edge. A ground figure taken from that ring is a false statement about
the picture rather than a noisy one, so none was published for that set.

On a type with a layout axis, **read the ring only where the layout has no cells**; elsewhere
measure the named region rather than the frame's border. Nothing is repaired in
`scripts/ground_audit.py` here — the ring is right for the grounds ADR-073 measured, and
teaching it to find a ground per layout is a change to a shared instrument that wants its own
diff and its own known-bad input.

**`lede-lineup` is on the DESIGNED side, and that corrects what its own file assumed.**
It reads 2.9, with the group, not 7. Four of its five stand on a smooth studio sweep rather
than in a place. What is real in a lineup is the SURFACE the units stand on and the contact
shadows it takes; the backdrop behind it is not.

Three ground clauses follow, and each type file carries the one that is its own.

### Designed, gradient — `lede-collage`, `lede-winner`, and the proposed `lede-mosaic`

Perfectly smooth: no grain, no texture, no paper, no vignette. **Light AND strongly
coloured** — value about 0.90 with saturation about 0.50, both together, since a dark
saturated field and a light quiet field are each only half of what the corpus does.

**Either a two-hue gradient running diagonally, or one flat tone. Nothing between the two
was observed.** Three of the five collages travel roughly half the colour wheel corner to
corner — measured at 177°, 175° and 177° of hue spread on a diagonal axis, which is green
to red, purple to teal, magenta to orange. The other two hold a single tone at under 13°
of spread. `lede-winner`'s one frame is a diagonal at 179°.

### Designed, seamless — `lede-lineup`

A studio sweep, not a room. **Saturation here is bimodal and the median hides it**: the
five measure 0.03, 0.21, 0.26, 0.66 and 0.71 — three near-white sweeps and two strongly
coloured ones, with nothing at all between 0.26 and 0.66. So this is a CHOICE a prompt
makes rather than a band it lands in. Value runs 0.68 to 0.96.

**No gradient.** Hue spread is small on every frame whose ring is actually ground. The one
reading 175° is a garment flat-lay filling the frame edge to edge, so the metric measured
the subject rather than the backdrop — which is the honest limit of measuring a ground from
a ring, and the reason this clause does not claim a clean 5 of 5.

### Photographed — `lede-testing`, `lede-authority`, and the two copied types

A real place, and measurably so. **Texture ~7.0.** **Mid, not light** — value 0.65 against
0.90, because a bench under working light is not a sweep. **Quiet** — saturation 0.13, with
2 of 11 above 0.25: the colour in these frames is in the apparatus and the product, never
in the room. **Unevenly lit** — value spread 0.67 across the ring, because real light falls
off; a prompt asking for even illumination across the background is asking for a studio.

`lede-inuse` has one observation and it is dark (0.16). `lede-pain` has **none**: this
corpus is editorial review publishing and carries no pain lede at all, so that type's
ground stays whatever its parent gives it and is not written here.

## Copying: verbatim, and made auditable

**Owner decision, 2026-09-09 (ADR-070): a toplist type that reuses an argument carries the
parent's text, not a pointer to it.** Where `copied_from` names an image type, everything
from `PURPOSE` to `KNOWN-FLAKY` in that file is the parent's own text, spliced by script
rather than retyped, and the file stands alone.

Two sections are deliberately NOT copied, for correctness rather than for brevity:

- the parent's **`WORKED EXAMPLES`** — SPEC §3.3 keeps a rendered example's full prompt
  text as the record of what actually rendered, and those renders were the parent's at the
  parent's version. Reprinting them under a toplist id would be a false claim about what
  was rendered.
- the parent's **`CHANGELOG`** — its evidence trail and commit hashes. This file has its
  own.

**`copied_at_version` is what makes the choice auditable.** It records the parent's
version at the moment of the copy, and `scripts/validate.py` **warns** when the parent
moves past it. A copy cannot be stopped from drifting; it can be made to say so. The
warning names the remedy: re-copy, or write into this file's CHANGELOG why the divergence
is intended.

The exposure is recorded rather than argued away. `registry/types/_staging/ready-to-push/`
once shipped byte copies of four type files and they were deleted on 2026-09-03 with the
finding written into that folder's README — *two copies of one file drift, and the stale
one is the one somebody reads*. That remains true here. What is different is that this
namespace has an instrument pointed at it.

**A copy is NOT reached by a rule keyed on the parent's id, and that is the part most
likely to be forgotten.** `mapping/slot-rules.md` says *"drop `06-relief-scene`"* when
`result_visibility: invisible`; nothing in it says `lede-inuse`. Every gate a copied type
should carry is therefore restated by id in `mapping/toplist-rules.md`, and adding one to
the parent later does not add it here.

## Global rules

Every rule in `registry/rules.md` binds unless a type declares `exempt_from`, exactly as
for image types. Three deserve naming because a top-N page walks into them:

- **G1** is load-bearing everywhere here: a lede image whose product is wrong is a lede
  image for a different page.
- **G14** binds the SLOT. A lede image that reads as a customer's own photograph, beside
  a ranking the page presents as editorial, is the shape G14 exists to refuse.
- **SPEC §6.4's brand-mark clause does NOT bind here** (owner instruction, 2026-09-09,
  ADR-075). *"Competitor brand marks never appear in prompts"* would refuse the format's
  whole subject: a top-N page is about several named competing products. §6.4's other half
  still binds — no prompt may aim to reproduce a specific source image.

  **Two things follow and the second is easy to miss.** A real brand may be DEPICTED, from
  the reference photo the owner attaches. A brand may not be INVENTED: a prompt with no
  reference that asks for branded units gets a fabricated logo, which is a different fault
  and one no permission covers. Where a prompt attaches no photo — as `lede-lineup` and
  `lede-collage` must while the one-photo limit stands — the units stay unbranded, and that
  is now a rule about invention rather than about competitors.

  **Still refused, and not covered by this instruction:** a certification seal, a press
  logo or a third-party AWARD mark. G16 marks those `LAW, not taste`, the reason is the
  issuing body's trademark rather than the competitor's, and three of `lede-winner`'s five
  corpus frames carry one.

**Prompt economy is `adapters/nano-banana.md` Rule 6 and is not restated here.** What IS
recorded here is that this namespace ran its render loop for two types without ever measuring
against it, and what that cost. Owner, 2026-09-10: *"prompt hiện tại đang bị phình lớn, chưa
áp dụng luật length"*.

| | set 1 → last | |
|---|---|---|
| `lede-authority`, median chars | 1498 → 1692 → 1689 → 1820 → 1693 → 1876 → **2158** | 7 sets |
| `lede-collage`, median chars | 1646 → 1853 → 2199 → 2090 → 2346 → **2464** | 6 sets |
| rounds 1–3, one prompt per type | 1225 · 1341 · 1476 | inside the band |

**12 of 106 prompts sat in Rule 6's band, and the rise is monotonic in both types.** The
mechanism is not carelessness: every set answered a render failure by ADDING a clause and no
set ever removed one. **A loop with no removal step ratchets**, and the rounds that predate
the loop are the ones still inside the band.

**Three removals put a set back, and each was a rule already written down** — Rule 6.1 caught
an invented `[CONDITION]` block carried by all 42 prompts of seven sets and named nowhere in
any type file; Rule 6.3 caught the count, the layer number and the mark rules each stated
twice; and round 3's ELEMENTS/CONSTRAINTS split settles which of the two a clause belongs in,
since saying it in both is saying it once and padding it once. Nothing earned was dropped.

**`scripts/validate.py` now warns past Rule 6's ~2500 re-read ceiling** for every prompt under
`registry/toplist-types/`. Only the ceiling is gated: the 1450–1600 band is a reference number
measured on a one-subject GIF-inset prompt, and a collage prompt carrying five products, a
layout, a palette, a graphics layer and a badge does not fit it — four cells of a compressed
set land at 1709–1818 with every earned clause intact, and that is **reported rather than
padded down**, exactly as ADR-072 reported 1029–1632. Unlike CLAUDE.md rule 6c's sweep this
one is gateable, because it is a number rather than a claim about meaning.

**Ratio is not declared by these types.** The owner's app resolves the lede ratio
(2026-09-09), so a toplist type carries no `ratios` key and no prompt states one — the
ban on writing a ratio into prompt text (ADR-016, adapter Rule 4) is unchanged.

## Reading a render: one render is one DRAW

**Established 2026-09-10, by the only experiment in this namespace that has ever repeated a
prompt.** `lede-collage` set 7 cell 3 was rendered at 10:52 and again at 10:56 from an
unchanged prompt. The first draw came back a flat vector illustration in every unit; the
second came back photographic, with legible maker's marks. **A clause carried in both draws
cannot explain the difference between them.**

**So a property that varies run to run cannot be evidenced by one frame**, and this namespace
had been doing exactly that. Two rules were written on single draws and both are now
withdrawn: a cap of two graphic layers, from one frame that flipped register; and *"a unit
drawn small stops being photographed"*, from five frames with no repeat among them.

**What follows binds every type here:**

- **A finding about REGISTER — photographic against drawn, material against flat — needs the
  same prompt run more than once.** One frame states what happened, never what the wording
  causes.
- **A finding about GEOMETRY, COUNT or PLACEMENT does not.** Those are things a prompt can
  determine, and this namespace has measured them landing: geometry fixed a unit count 2 of 2
  on the layout that had failed twice, while four prescriptions of taste were ignored 4 of 4
  in round 3. Where a clause names a position, one frame is enough to see whether it took.
- **A control that varies on the axis it is controlling is not a control.** `lede-collage` has
  now lost four: one produced the thing it was told not to, one confounded itself with a second
  variable, one never rendered, and one was answered by a variable nobody was testing.

**This is a rule about evidence, not about pictures, and it is cheap to obey**: render the
control cell twice. A set that reads one frame as proof about wording will keep writing rules
the next draw refutes, which is how both withdrawn rules got written.

## A slot named by its ROLE takes a DEFAULT — name the value

**Four instances in one day, 2026-09-10, across two types.** A prompt block that names what a
slot IS FOR, without naming what goes in it, does not leave the slot empty: the model fills it
with the commonest thing of that kind, and the commonest thing is almost never what the picture
needed.

| the clause | what it named | what came back |
|---|---|---|
| `lede-collage` — *"a small label between rules, a large word, a small year"* | three type LEVELS, two words | a badge printing the literal word `LABEL`, and another arcing `AAFERABLE BREAD QUALITY` |
| `lede-collage` — *"the ground shows as a plain even border"* | a border's ROLE | **white in 5 of 5** |
| `lede-inuse` — *"calm and unbothered"* | a mood | a neutral face, 5 of 6 |
| `lede-inuse` — *"a natural palette"* | a palette's ROLE | colourless, saturation 0.15 in the flattest frame |

**Each was fixed the same way and each fix landed on its first outing.** Name the strings, one
per level: 8 of 8. Name the border's value — *the deepest hue of the palette family* — and
saturation goes 0.02 to 0.67–0.97, 5 of 5. Name the muscles instead of the mood: brow, jaw,
shoulders, and the frame reads.

**This is the same law as §*Writing a clause* seen from the other side.** That section says a
prohibition is inert because it asks for a measurement with no picture attached. This one says a
role is inert because it asks for a category with no instance attached. **Both fail for the want
of a thing to draw**, and the repair in both directions is to supply one.

## Writing a clause: state the FAULT, not the property

**A constraint aimed at one fault but written as a general property removes the entire
dimension it touches.** Three instances in one day — 2026-09-09, across two types:

| clause, written against one fault | what it removed |
|---|---|
| `lede-authority` *"the expression is settled"* | every pose, across twelve renders |
| `lede-authority` *"the backdrop is lighter than the subject's clothing and lighter than the product"* | the ground's whole value range, on pale units |
| `lede-collage` *"all five panels are the same width and the same height"* | the whole layout axis |

**Each clause did the job it was written for, and then kept working.** The first was added
after four of five set-1 frames came back startled; it cured that and left twelve subjects
centred, square to the lens, hands at chest height and faces neutral. The second was a
separation test, and behind white units it forces the ground to near-white — which is the
one washed-out frame in the set that named it. The third was added on top of a
no-favoured-unit law and turned an index into a spec sheet.

**The repair is a finer distinction and never the opposite** — deliberate against caught,
separation against lightness, prominence against uniformity. Swinging to the far end fails
worse, because it still legislates the axis instead of the fault.

**So name the fault and leave the axis open.** A clause that reads as a property of the
whole picture is the shape to distrust; a clause that names what must not happen is the
shape that survives a render round.

Recorded in `lede-collage.md` at 0.8 and moved here on 2026-09-10 — two of the three
instances are another type's, so it was never that one file's law to hold.

## What this namespace is still waiting on

**One decision, down from two, and NO type is reserved behind it.** The reference-photo
limit was taken on 2026-09-09 (ADR-076): a prompt may attach one photo per unit, still in
one generation call, and where the owner's app takes fewer the prompt ships in full and is
rendered elsewhere. `lede-lineup` and `lede-collage` went active on it, and `lede-authority`
followed at its own 0.3 (commit `c81ae0d`). **All seven types are active.**

**What is left is one row of G16, and it is the most-breached refusal here.** A
certification seal, a press logo or a third-party AWARD mark is `LAW, not taste`, and
**three of `lede-winner`'s five corpus frames carry one** — `CNET LAB TEST WINNER`, `CNET
PEOPLE'S PICKS`, `GOOD HOUSEKEEPING BEDDING AWARDS`. ADR-071 permitted the page's OWN
verdict and left another party's mark refused; the corpus says the market does it anyway.

**That row no longer holds a type back, and the correction is worth stating rather than
just deleting.** `lede-authority` was reserved behind the same row's *named expert* clause
until its own 0.3, and the block was lifted by READING the refusals rather than by waiving
them: G16's row governs a text layer that type does not declare, and `mapping/slot-rules.md`'s
`author` row governs a portrait under a real BYLINE, which a top-N lede does not carry.
G14 is the one that genuinely binds and it survives as that type's load-bearing NEGATIVE —
the UGC register is refused. So the award-mark question is now a decision about pictures
this namespace may make, not a lock on any file.

It is not a craft question and it is not the harness's to take.
