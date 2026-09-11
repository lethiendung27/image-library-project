# PDP-DR instruction — law shared by every type in `registry/pdp-dr-types/`

The direct-response **product detail page**, LP2. Law that binds every type in this
namespace is stated here once and never restated in a type file, exactly as SPEC §5
treats global rules and as `registry/gif-instruction.md` and
`registry/toplist-instruction.md` do for their own namespaces.

Read `SPEC.md` §3.8 first. This file is the law; that section is the contract.

---

## What this namespace is for

A product page's image gallery — the tiles a buyer swipes after the first packshot. The
corpus behind it is **159 observations across 26 source pages**, batches `2026-08-31-A`
and `-B` and `2026-09-03-C` through `-H`, filed against **41 distinct type ids**.

**It is separate for none of the reasons the other two namespaces are separate, and
saying so is the point.** SPEC §3.6 and §3.7 both justify a namespace the same way: that
page carries ONE image slot, so the role shortlist of §7.2, the cross-slot pass of §7.3,
the coverage pass of §7.5 and one-type-once have nothing to act on. **A product gallery
carries about twelve slots.** Every one of those passes applies to it, harder than to an
advertorial, because twelve slots is more places for the same argument to appear twice.

So this namespace stands on three differences of LAW, not of machinery:

1. **Text is baked into the image.** Owner decision, 2026-08-31, taken against the
   advice of the session that raised it: an ad image with words is generated with the
   words in the file rather than handed to the page as a clean plate for an HTML
   overlay. Every type here may declare `text_layer` and G16 binds the ones that do.
   Advertorial and listicle types overwhelmingly do not.
2. **The ground rule is measured on this corpus.** ADR-068 measured the outer 8% ring of
   119 frames from these batches: **VALUE median 0.89, SATURATION median 0.06.** That is
   a fact about these pages and it does not transfer — ADR-073 had to re-measure the same
   rule for the toplist corpus and found TEXTURE splitting the namespace in two.
3. **Marketplace legality gates a gallery.** `mapping/slot-rules.md` cross-rule 5 bars the
   ugc register and `01-pain-scene` from marketplace galleries and bars `--rivals`
   outright. An advertorial never meets that gate; a product gallery meets it on every
   tile, because the same gallery is syndicated to a marketplace listing.

## A CO-REGISTRY, not a replacement

`registry/gif-types/` and `registry/toplist-types/` abandoned the `{step}-{job}-{device}`
grammar because their ids are ARGUMENTS. **This namespace keeps the grammar**, and that
follows from the owner's decision of 2026-09-10 rather than from taste: the folder holds
only types the shared registry does not have, so a PDP page routes to
`registry/types/` and to this folder **in one pass**. Two id grammars in one pass is how a
reader loses track of which law applies. Promotion out of here into `registry/types/` is a
`git mv` and a status change, not a rewrite.

**There are no copies here, and therefore no drift instrument.** ADR-070 gave the toplist
namespace `copied_from` + `copied_at_version` and a validator warning, because the owner
had chosen verbatim copies and *a copy cannot be stopped from drifting, but it can be made
to say so*. That machinery is absent here because the decision that made it necessary was
not taken here: nothing in this folder is a copy of an active type.

**What that costs, stated so it is not discovered.** A skeleton here may CALL a part
defined in ANOTHER file by name. **Nothing checks it.** If the definition moves, the call
goes stale silently, and there is no `copied_at_version` to fire a warning the way ADR-070
gave the toplist namespace. Every such call is registered in `mapping/pdp-dr-rules.md`, and
a new one belongs in that register the day it is written — the register is the whole
instrument.

**There are zero live calls today.** The only two this namespace ever had were
`07-identity-callout` reaching into `03-spec-callout`'s `presentation` and `setting`, and
both died when that type was deprecated in favour of the one it was calling into (ADR-078).
The three files written on 2026-09-11 restate their own parts instead. That is the cheaper
habit and it is the one to keep: a call saves a paragraph and costs an unwatched dependency.

## Input is `content.json`, and the gallery is the unit

Unlike the toplist namespace, this one consumes the **whole** `content.json`
`{ product, page }` and routes through `query/runbook.md` unchanged. A product gallery has
`page.sections`; the slots are real; §7 applies.

**The gallery is a SET and the set is what is checked**, which is `mapping/pdp-dr-rules.md`'s
whole job. Three of §7's passes do more work here than anywhere else in the library:

- **One type at most once per page**, and a twelve-tile gallery is not a repeating section
  in cross-rule 2's sense. A roundup's five ranked entries are equivalent list items; a
  gallery's twelve tiles are a linear argument, and repeating a type across a linear funnel
  repeats an argument.
- **The page arc (G4 at page level).** Pain and cause tiles precede relief and outcome
  tiles; pain never reappears after the first relief tile.
- **Step-3 budget.** At most two of `03-mechanism-ghostbody`, `03-spec-split`,
  `03-use-sequence` on one page. Three is a lecture, and a gallery has room to make that
  mistake in a way a six-slot advertorial does not.

**The first gallery image is out of library scope.** It is a standard product shot; the
library covers images 2 and after (`mapping/slot-rules.md`, cross-rule 6).

## Text: every type may declare one, and G16 binds it

G16 is not lifted, it is narrowed one type at a time, and this namespace is where it does
most of its work. Read the rule; three things in it were measured on THESE frames and are
the ones a writer gets wrong:

- **`title` is a HOOK, not a caption.** The market's ten headlines average 8.0 words and
  every one names a result, a feeling or a problem state — something that happens to the
  reader. The ten G16's first draft produced averaged 4.5 words and every one named what is
  in the picture. **A caption describes the frame; a hook describes the reader.** The
  seven-word figure is a LINE cap, not a sentence budget: a 12-word hook over two lines was
  always legal.
- **`copy` does a different job from the title.** Proof, a timeframe, or the mechanism in
  plain words. If deleting it loses nothing, it was a restatement.
- **A badge is a MARK and the type owns its forms** (ADR-012, ADR-043). Never `small`,
  never a percentage: size it against a named object in the frame, which is the one
  instrument that measured 0.51–0.96 where the same instrument on a headline measured
  0.13–0.64 and ran backwards. Three corners are open; the bottom-right carries the
  generation tool's watermark. **A badge carries a colour the photograph does not.**

**Never reserve space you do not fill.** A block that fills a third of the area it was given
will be drawn again to fill the rest — measured at seven ink bands where four were asked
for. Where the words are short and the field is large, the prompt says how much of the
picture the block occupies AND that it appears once, in one place, and nowhere else.

### The two rows that are LAW and not taste

The owner waived G16's caps on 2026-09-03 after finding the copy too weak to ship. **Two
rows did not move**, and neither is G16's to waive:

1. **A named-person or named-profession endorsement.** G14 calls it illegal in its own
   words (FTC endorsement rules), and G14 binds the SLOT rather than the type — so there is
   nothing here for a type-scoped permission to lift.
2. **A certification seal, an award, a rating or a press mark.** The trademark question,
   put to the owner on 2026-08-18 and declined. Until it is answered these are unwritable,
   and two files in this folder record that it is their commonest observed content.

## Ground: quiet by default, and a dark one is a CHOICE

Measured, ADR-068, the outer 8% ring, corpus n=119 against this library's own six renders:

| | corpus | the six renders |
|---|---|---|
| ground VALUE, median | **0.89** | 0.46 |
| ground SATURATION, median | **0.06** | 0.38 |
| darker than 0.70 | 35% | **83%** — 5 of 6 |
| more saturated than 0.25 | 24% | **67%** — 4 of 6 |

The market's ordinary ground is light and almost colourless. **The cause of the six renders
was a rule this library wrote to cure the opposite fault** — three type files told the
writer to take the ground from the product's own register, to cure six frames of identical
pale grey. They cured it and moved the whole set off the corpus, because nobody measured the
corpus before writing them.

```
The ground is QUIET by default — light, and close to neutral. That is what the
market does two times out of three, and it is not a failure of nerve.

A dark or a saturated ground is legitimate and the corpus builds one about a third
of the time. It is a CHOICE, and the prompt says what the choice buys: dark for a
product that emits, saturated where the brand owns that colour, a real room where
context is the argument.

Variety is spent where the corpus spends it — on the marks, the product and the
chips — and not on the wall behind them.
```

**Write the FAULT, not the property.** The clause above bans reaching for a dark ground by
default; it does not ban dark grounds. A constraint written as a general property deletes
the whole axis, which this repo has done to itself three times in one day.

## What binds every prompt, wherever it comes from

- **Every delivered prompt is paste-and-run**: one prompt, one generation call, and as many
  reference photos as the type needs — one per product in frame (ADR-021, ADR-076). Never a
  multi-pass option, an edit chain or a post-assembly step.
- **G1's product-reference block is mandatory** for every type with
  `requires_product_photo: true`, and gains *the product must be identical in every layer of
  this image* wherever the product appears twice.
- **G2 limits the PRODUCT slot to four kinds of information** — position, angle, scale in
  frame, and relation to other objects. Not shape, not material, not colour, not
  construction, not an aesthetic adjective. The reference photo carries appearance; the
  prompt only places it. **This is the clause a gallery breaks most**, because a gallery is
  about the object and the writer reaches for the object's own adjectives.
- **Never state the frame's shape or ratio in prompt text** (ADR-016, adapter Rule 4). A
  written ratio did nothing to this renderer, 6 of 6.
- **A15**: a figure enters a frame only where `content.json` carries the figure AND its
  source, and the source is set beside it. This binds the text layer and it also binds
  anything printed on an object — `07-identity-pack`'s founding render wrote a net weight
  and an ingredient list onto a pouch that nobody asked for.
- **G13 has no exemptions.** A refused prompt returns no image at all, which is a different
  failure class from a weak one.

## A slot named by its ROLE takes a DEFAULT — name the value

The law of 2026-09-09 (`ac10f69`) applies here without change. A skeleton slot that names
what a thing is FOR gets the renderer's habitual answer for that role: `[BADGE] one short
stamp` produced six identical flat rectangles, all `small`, all lower-left, all borrowing a
colour already in the frame. The repair is not a longer role description. **It is to name
the VALUE** — which form, how wide against what object, which corner, which colour the
photograph does not already have.

## What the 157-image corpus measured — 2026-09-11

Ten sources, 156 records, batches A–J. The whole PDP corpus now stands at **315 records, 36
sources, 53 distinct ids**, of which **15 carry 71% of all observations**. Full working in
`registry/pdp-dr-types/_CURATION-2026-09-11.md`; the six findings that bind every type are
here.

### 1. G3 does not hold uniformly, and the split is precise

Seven sources use a signal colour deliberately. Three agree with the rule and four invert it,
and which do is not random:

| G3 HOLDS | G3 INVERTS |
|---|---|
| **pressure** — red arrows into a cyan cushion | **heat** — red and orange for therapeutic warmth |
| **verdicts** — red cross, green tick, correct side brighter | **lift** — red arrows for support under a body |
| **states** — blue working, red tank-full, green tick | **detection** — green means NO TARGET, red means FOUND |

**The market reaches for the colour of the PHENOMENON, not the colour of the judgement.** One
source states its own code in words and then contradicts itself on the same device, using
green for a full battery and green for nothing-found.

**And a distinction this repo has never stated: a product's OWN indicator colours are not
signal marks.** LED wavelengths named in nanometres, a teal status strip, a lit ring, a
charging glow — G3 does not reach any of them. A writer who treats them as marks will refuse
frames the rule never governed, and a reader counting colour usage in the ledger without
holding this will miscount four sources.

### 2. Five honest-substantiation behaviours, found in the wild

A15 proposes a footnote-and-survey shape drawn from one corpus frame. The drop found five
better models, each in a real page, and they are what a substantiation rule should legislate:

1. **the instrument in shot** — a tape measure stood against the edge, substantiating the same
   figure the page asserts bare two tiles earlier
2. **the declared error band** — *"Manual Measurement May Result In An Error Of 1-3 Cm / This
   Will Not Affect Usage / Please Do Not Purchase If You Mind"*
3. **the comparison scale** — a figure placed between two familiar anchors, leaves and
   conversation, so a reader can judge it against things they know
4. **the approximation sign** — `≈45%`, `≤38mm`: a declared bound rather than a false point
5. **the stated limitation** — *"(Non-live cables may be detected by metal objects or not
   detected by the detector)"*, inside a feature tile

**A maximum is falsifiable; a point figure on a render is not.** That sentence separates a
published `≤120mm` detection depth from an invented `4.0mm / 4.5mm` on a rendered tissue
section, and it is the whole of what A13 and A15 are trying to say.

The floor of the scale, for contrast: *"Eases muscle fatigue by up to 30%"* — no source, no n,
no timeframe, and "up to" makes any result satisfy it.

### 3. The slot-spending habit — 7 of 10 sources

A direct-response gallery **spends a slot rather than compressing a variable**. One source
spends eight of twenty-one tiles on a two-colourway by four-plug matrix of ONE frame; others
spend two or three on colourways, display types or contexts. That is the standing argument for
`03-spec-lineup`, whose purpose is to put a matrix in one frame.

**The honest counter-argument is in the same corpus** and belongs beside the finding: a context
tile at full size establishes SCALE against a bench and a building, which a quarter-size grid
cell cannot. Compressing costs the scale cue, and for some products scale is the doubt.

### 4. Two rules the corpus breaks on purpose

- **G7, context integrity.** A bath mat composited onto cloud forms; a mains dehumidifier
  standing in a snowdrift. Two sources, two categories, both to make a claim literal. G7
  refuses a product in a place it could not be, and every type here that takes no G7 exemption
  refuses it too. Whether that is a gap in G7 or a discipline worth keeping is an owner call.
- **G13, minors.** One frame puts a crying infant in a cot in a bedroom — two of G13's three
  rules breached, and G13 names that configuration a REFUSAL class, a prompt that returns no
  image at all. **A baby-monitor category has a gallery slot this library structurally cannot
  fill**, and no prompt craft changes it. The same page carries a compliant frame (living room,
  attentive expression, no age stated) and a partial one, which is the most useful G13
  comparison the ledger holds.

### 5. Motion in a still — three instances, two sources, no name

Ghosted multi-position subjects (a solar panel at three angles; a person crossing a monitored
zone) and curved motion ARCS used as callout leaders (pan and tilt ranges). This registry has
no device for showing movement in a still frame, and the corpus has three ways of doing it.

### 6. A third mark class — the compatibility bar

Six third-party platform marks across the foot of a tile: Alexa, Google Assistant, a vendor
app, a smart-home platform, WiFi, Tuya. This library has refused two mark classes under the
trademark question of 2026-08-18 — the certification seal and the press mark. **A compatibility
mark is different in kind:** it confers no authority on the product, it states an
interoperability fact a buyer can verify by trying it.

Nothing in G16, G14 or the two LAW rows reaches it. **G6 bans logos outright** and the source
carries twelve. Until that is decided, no type here writes a mark library that includes one,
and `03-spec-claimstack` ships with no mark library at all for exactly this reason.

## What this namespace is still waiting on

**Nothing in this folder routes.** Fifteen files: fourteen `status: reserved`, each carrying a
`blocked_by` and a `BLOCK`, and one `deprecated` — `07-identity-callout`, retired on
2026-09-11 and replaced by `03-spec-callout` after a control render and a ten-source corpus
answered the same question the same way. `registry/index.yaml` gains none of them. What routes
on a PDP page today is the shared active types in `registry/types/`, ordered by
`mapping/pdp-dr-rules.md`.

**Three files clear SPEC §6.3 criterion 1 and are the promotion queue**, in order of evidence:
`03-spec-claimstack` (8 distinct sources), `03-spec-dimension` (7), `03-spec-hero` (6). All
three are blocked on criterion 2 alone, and in each case against a named sibling —
`06-relief-claimstack`, `03-spec-callout`, `06-relief-hero`. **Those three router-confusion
tests are now the single largest piece of unfinished work in this namespace**, and they are
the same test three times: can a router separate two types that share a device and differ only
in job?

Four decisions gate the rest of the folder, and three of them are the owner's:

1. **The substantiation rule** (A15). Blocks `04-proof-stat`, and behind it
   `04-proof-instrument` and `04-proof-interface`. A skeleton has to say where a number
   comes from.
2. **The trademark question** of 2026-08-18, now WIDER than when it was asked. It blocked
   `07-identity-callout`'s mark library; that type is retired, and the question moved to
   `03-spec-claimstack`, which ships with no mark library at all because the badge this
   construction actually carries in the corpus is a **compatibility bar** — six third-party
   platform marks. That is a third mark class, neither a certification seal nor a press
   mark, and answering the 2026-08-18 question as asked would not settle it.
3. **The `beneficiary` axis.** Blocks `06-relief-animal`, and settling it means widening
   `PARTS/subject` on three ACTIVE types — work this namespace's charter does not cover.
4. **Criterion 2, the router-confusion test**, which no owner decision unblocks. It is now
   the binding gap on the three best-evidenced files here and on nothing else, and it is
   the SAME test three times — `03-spec-claimstack` against `06-relief-claimstack`,
   `03-spec-dimension` against `03-spec-callout`, `03-spec-hero` against `06-relief-hero`.
   Each pair shares a device and differs only in job. ADR-066 refused to promote past this
   test once already, before any of the three siblings existed to make it concrete.

**No prompt has been written from any file in this folder against this namespace's law, and
no render exists under it.** Three of the eleven carry FOUNDING RENDER ROUND sections from
their time in `_staging/`; those renders are real and their measurements stand, and they
were taken before this file existed.
