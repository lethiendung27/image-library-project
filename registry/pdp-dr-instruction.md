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
the coverage pass of §7.5 and one-type-once have nothing to act on. **An LP2 page carries
many slots.** The four templates of 2026-09-17 generate 16 to 37 images each, and that is why
LP1's cross-slot pass does not run on it (ADR-102): with 17 active types, a rule that refuses a
type because another slot holds it leaves the page without types. The gallery keeps its own
checks, most of them warnings. One check runs over the whole page: no two images share a type
and a message (`mapping/pdp-dr-rules.md`, cross-slot rule 13).

So, beside that cross-slot pass of its own, this namespace stands on three differences of LAW:

1. **Text is baked into the image.** Owner decision, 2026-08-31, taken against the
   advice of the session that raised it: an ad image with words is generated with the
   words in the file rather than handed to the page as a clean plate for an HTML
   overlay. Every type here may declare `text_layer` and G16 binds the ones that do.
   Advertorial and listicle types overwhelmingly do not. **Since 2026-09-17 those words
   belong to the product card's gallery alone** (ADR-096); every other image on the page
   is wordless.
2. **The ground rule is measured on this corpus.** ADR-068 measured the outer 8% ring of
   119 frames from these batches: **VALUE median 0.89, SATURATION median 0.06.** That is
   a fact about these pages and it does not transfer — ADR-073 had to re-measure the same
   rule for the toplist corpus and found TEXTURE splitting the namespace in two.
3. **Marketplace legality gates a gallery.** `mapping/slot-rules.md` cross-rule 5 bars the
   ugc register and `01-pain-scene` from marketplace galleries and bars `--rivals`
   outright. An advertorial never meets that gate; a product gallery meets it on every
   tile, because the same gallery is syndicated to a marketplace listing.

## The ONE folder an LP2 page routes

**Owner instruction, 2026-09-15 (ADR-091): each page kind routes one folder, and that folder
holds every type the page may use.** So an LP2 page reads `registry/pdp-dr-index.yaml` and this
folder, and never opens `registry/types/`. The folder holds two kinds of file:

- **a verbatim copy of every active image type**, under the parent's id, carrying
  `copied_from` + `copied_at_version`. These are what route today. Since ADR-094 a copy may
  also carry one `## LP2 LAW` section of its own — see the type map below.
- **LP2's own drafts**, every one `reserved` or `deprecated`. A draft is promoted in place —
  a status change, never a `git mv` out, which would take it out of the folder LP2 routes.

ADR-077 built this namespace the other way, as a CO-REGISTRY: the folder held only the types
the shared registry lacked, and a PDP page routed to `registry/types/` and to this folder in
one pass. ADR-091 retired that.

**The grammar stays `{step}-{job}-{device}`, now for a different reason.** ADR-077 kept it
because two id grammars in one pass lose a reader, and there is no second folder in the pass
any more. It stays because **a copy keeps its parent's id**, and every gate in
`mapping/slot-rules.md` is keyed on an id — so the gates reach the copies with nothing
restated. That is the one respect in which these copies cost less than the toplist
namespace's, where ADR-070 had to restate every gate by toplist id.

**The copies are auditable the way ADR-070 made the toplist copies auditable.** *A copy cannot
be stopped from drifting, but it can be made to say so*: `scripts/validate.py` warns when a
parent moves past `copied_at_version`, and warns on an active image type with no file here,
because a promotion into `registry/types/` does not reach LP2 by itself. The parent's WORKED
EXAMPLES and CHANGELOG are not copied, for ADR-070's reason: those renders were the parent's.

**This file binds the copies, as it binds every file in the folder.** On an LP2 page, where a
copied clause and this file disagree, this file binds; a type that must keep its clause here
says so by editing the copy and its CHANGELOG, which is the divergence `copied_at_version`
exists to make visible. Before ADR-091 this file bound only the drafts, and an LP2 page filled
a shared type without it.

**What the copy instrument does not reach, stated so it is not discovered.** A skeleton here
may CALL a part defined in ANOTHER file by name. **Nothing checks it.** If the definition
moves, the call goes stale silently — `copied_at_version` watches whole files, not calls.
Every such call is registered in `mapping/pdp-dr-rules.md`, and a new one belongs in that
register the day it is written — the register is the whole instrument.

**There are zero live calls today.** The only two this namespace ever had were
`07-identity-callout` reaching into `03-spec-callout`'s `presentation` and `setting`, and
both died when that type was deprecated in favour of the one it was calling into (ADR-078).
The three files written on 2026-09-11 restate their own parts instead. That is the cheaper
habit and it is the one to keep: a call saves a paragraph and costs an unwatched dependency.

## Input is `content.json`, and the gallery is the unit

Unlike the toplist namespace, this one consumes the **whole** `content.json`
`{ product, page }` and routes through `query/runbook.md`. A product page has
`page.sections`; the slots are real; §7 applies, except that Stage 2's cross-slot constraints
are `mapping/pdp-dr-rules.md`'s own and none of `mapping/slot-rules.md`'s rules 1–4 (ADR-102).
**An image routes by its section's name and by the copy written in that section**: the name
gives a default role (`mapping/pdp-dr-rules.md`, *Section routing*), and the copy decides.

**The gallery is a SET and the set is what is checked**, which is `mapping/pdp-dr-rules.md`'s
whole job. No rule there removes a type from a slot because of the type another slot holds
(ADR-102). Three checks watch the gallery more closely than anywhere else in the library:

- **One type at most once in the gallery — a warning.** A gallery's tiles are a linear
  argument, and repeating a type across a linear funnel usually repeats an argument. A gallery
  that needs a type twice takes it twice, with two messages.
- **The gallery's arc (G4 over its tiles).** Pain and cause tiles precede relief and outcome
  tiles; pain never reappears after the first relief tile. This one still binds: it orders the
  tiles and removes no type.
- **The mechanism-class budget — a warning.** At most two mechanism-class tiles in one gallery —
  any mechanism, any comparison or proof, any use steps (`mapping/pdp-dr-rules.md`, rule 3, which
  widened the step-3 trio in ADR-094). Three is a lecture, and the warning says so.

**The first gallery image is out of library scope.** It is a standard product shot; the
library covers images 2 and after (`mapping/slot-rules.md`, cross-rule 6).

## One session, one set: what is LOCKED and what must VARY

**Owner instructions, 2026-09-16** — four rules for the images of a product page (ADR-093),
then the owner's tested gallery instruction, which fixed what the lock holds (ADR-094). The
first and the third rule are about the SET; the second and the fourth are about a tile.

**1. Every prompt a session emits belongs to ONE set.** A page's gallery tiles and its section
images are one body of work: one palette, one typography, one chip form and one lighting family,
while the product keeps the exact look of its reference photograph in every frame. The lock is
written once, before the first prompt — seeded by the page's style line where it has one, and
neutral where it does not — and repeated in every prompt of that session **in the same words**:

| locked | what the lock names |
|---|---|
| grounds | **exactly two treatments** for the set — a seamless and a real room, for instance — and every tile takes one of them. No more than two tiles in a row on the same one. A dark key only where a type's own tone asks for it |
| text colour | one colour for words on a light ground, one for words on a dark ground |
| accent | **ONE colour**, allowed on the chip form, a Callout leader and a badge a type declares, and nowhere else: never a frame, a border, a ring, an arrow, a line, a glow or a mark, and never the product. Red belongs to wrong-state marks and green to the verdict check; the accent is neither |
| typography | **one family for every word** — or, where the page's style line names two, one title face and one copy face, both fixed for the set — written as a style the renderer holds plus two concrete traits, with the title's weight and case and the copy's weight and case |
| chip form | one shape (pill or rectangle), one fill, one text case, flat: no outline, no shadow, no 3D, no stacking and no boxed figure |
| design language | corner radius, margin rhythm, overlay treatment, icon style. **It never names a device** — "leaders", "arrows", "insets" — because a named device gets drawn in every tile. **No frame or border around a photograph or a panel**; only the divider and the gutters a type defines |
| lighting family | one family, with the material vocabulary of the grounds and the props |
| register | photograph or render, wherever the types in the set leave that open |

**The style line seeds the lock and never touches the product.** "An orange theme" means an
orange accent and warm grounds; the product stays what its photograph shows. Without a style
line the lock is neutral — light neutral grounds, charcoal or warm-white text, one muted accent —
because a writer who cannot see the product cannot choose colours to complement it.
**Neutral names the grounds, the text and the accent, never the grade of a photograph.** A
photographed room keeps its real colours, and a resolved state is full colour (G11, ADR-104).

**Each field closes a fault the owner's own runs showed** — 64 renders of one cushion in five
batches and 13 of one comb (ADR-094): a typeface the rest of the set did not use, 3 tiles; a
photograph or a panel inside a drawn frame, 10; a signal blue on a frame, a ring, a line, an
arrow or the product in 6 of the 13 tiles of the two batches that used one; a stacked chip and
a figure boxed inside a chip, once each; and chips set in two text cases within one batch, in 5
of the 6 batches.

This is the lock `clip-fan-01` already ran under, and the one that made
`07-identity-callout`'s control render indistinguishable from a `03-spec-callout` prompt
(ADR-078): with ground, light, grade, type and accent identical, only the argument was left to
tell two tiles apart. That was the lock working. A set is supposed to look like one set.

**2. One tile, one message.** Every gallery tile that carries words says ONE feature or ONE
benefit, and every element in the frame serves it — the title, the copy, each chip, the badge,
the marks, and whatever props the type allows. **An element that would still be there if the
message changed is decoration, and it goes.** A tile naming three unrelated features is two
tiles, or it is a claim stack whose lines all support one message. That is what
`03-spec-claimstack` and `06-relief-claimstack` are for, and what they are not is a list of
everything the product does.

**A set counts its messages as FEATURE KEYS, not as sentences** (ADR-094) — `one-piece`,
`non-slip`, `foam-density`, `portability`, `posture-angle`, `pressure-relief`, `universal-fit`,
`durability`, `context:office`. A new tile needs a new key, and "seamless one-piece", "stays put"
and "won't slide" are one key written three ways. **A title already used in the set marks a
duplicate tile**, not a new one: the owner's comb run shipped one title and one copy line twice.

**"Use it in a place" is one family** — office, car, truck, gaming, wheelchair, pregnancy — and
a set carries at most two such scenes unless the page asks for a persona series. At two, the
idea is re-cut as a feature, an outcome or a grid tile. The cushion's first two batches spent
seven and eight of their twenty tiles each on scenes of use in a place.

**3. Composition varies across the set, and the variety is what makes a gallery look
designed.** Layout, camera angle, crop, the share of frame the product takes, whether the
subject is cut out or in a real place, how the words meet the picture: these change tile to
tile. **A set where every tile is the same three-quarter packshot on the same seamless is the
failure this rule names**, and the fix is never a new type — it is a different camera on the
type already chosen.

**Rules 1 and 3 do not contradict each other, and the line between them is the load-bearing
sentence here: the STYLE SYSTEM is locked, the COMPOSITION is not.** Palette, light, grade,
type and accent hold across the set; layout, angle, crop and scale are where the work shows.

**4. Word count is a support decision, not a budget to spend.** **Every word in the frame is
there because the picture cannot say that part.** The bands, the caps and what a line may never
say are the owner's since ADR-094 and live in the text section below: a title of two to five
words, copy only where it is earned, at most sixteen words in a frame. Chips and labels are the
easiest place to break it, because a type's own part puts them in frame —
`03-spec-callout`'s labels, for instance — so the tile's one message has to cap them. Measured
on the Densjet gallery: the two tiles carrying chips run 2–4 words a chip, and the busiest
carries six.

## The product is the photograph's, never the prompt's

**The prompt writer never sees the reference photograph.** It writes the product block and
PLACES the product; it never describes it. Any product adjective is a guess, and a guess in the
prompt overrides the photograph in the render. This is G2 in the owner's words (ADR-094), and
the owner's runs are why it is written this hard: **five of the six batches showed the product
in more than one colourway inside one set** — the cushion in sage, charcoal, grey and slate
across one batch of twenty, in pink and in grey inside another of eleven, the comb in white and
in pink. The sixth batch was seven tiles long.

**The product block, in these words.** On an LP2 page it takes the place of G1's block and keeps
every G1 obligation, and G1's "do not redesign" sentence stays in it word for word. One type
leaves it out: `03-mechanism-signal`, on the owner's trial of the feature-image output format
(ADR-101).

```
Use the attached product photo as the exact reference. Preserve its shape,
proportions, construction, seams, surface texture, finish and colour exactly.
Do not redesign, restyle, simplify or add features. The product appears in one
of its real colourways only, never restyled to match the scene or the set
palette; no added piping, trim, logos, patterns or printed text. Every part keeps
its photographed colour and finish; no part is tinted toward the set's accent.
```

Two sentences join it only where their case exists, the way G1's own multi-layer sentence
always has:

- **where several reference photographs are attached:** *Where several reference photos are
  attached, this image uses the [variant, in the page's own word] and only that one.*
- **where the product appears more than once:** *Wherever the product appears more than once in
  this image it is identical in every instance.*

**The owner's block named example parts — body, trim, metal rings, buttons, bristles, tips —
and the list is left out here.** Each item is a construction word, which G2 bars, and for a
product that has no metal ring the word is an invitation to draw one. "Every part" says the
same thing and names nothing.

**What the block cannot carry, for the writer:**

- **Place, never describe.** No colour, material, shape, texture or construction word about the
  product anywhere in the prompt — position, angle, scale and relation to other objects only (G2).
- **The lock governs everything except the product.** Grounds, words, chips, props and grade take
  the set's palette; the product takes its photograph's.
- **One variant per set.** A variant exists only as the page names it — "the pink version" — and
  the prompt uses that word and says which photograph to attach; it never says what the variant
  looks like. The whole set shows one: the first photograph attached, or the one the page names.
  Another appears only in a Lineup tile, or where the page asks. **A set that alternates variants
  reads as two products.**
- **Whole, legible, one object.** Never merged into furniture, hidden by a pose, flattened or
  split into pieces. If an angle hides the part the tile is about, change the angle, not the
  product.
- **A seated product is seen from the side or from behind.** Side profile or rear three-quarter,
  so its whole silhouette reads; at least 15% of the frame; and the host chair asked for as a
  RELATION — *in a tone and material clearly different from the product* — never as a named
  colour. Six of the cushion's seated scenes hid it behind the sitter or set it on a chair of its
  own grey.
- **No interior the reference does not show**, and no diagram painted on the product's surface.
  The one exception is `03-mechanism-xray` showing components the page names. Three cushion
  renders cut the cover open or drew a structure inside a product that has none, and four
  painted a heat map, waves or light lines onto the product itself.
- **No printed text the page did not write** — on its packaging, on a prop, or added to the
  product. Two renders printed an arrow on the shipping box. **The product's own printing is the
  reference photograph's** (owner decision, 2026-09-16, ADR-095): the photograph is attached and
  the block keeps it as it keeps every other part, so a render that re-letters it has broken the
  block and is graded as any other product drift.
- **A prompt with the product in frame ships with its reference flag set**, so the owner attaches
  the photograph at render time. A prompt with no product in frame carries no block.

## Text: TITLE ONLY by default, and G16 narrowed for this namespace

**This section governs the product card's gallery tiles**, the only images on an LP2 page that
carry words (ADR-096). Every other image carries none — see *Images outside the product card's
gallery*.

**Owner instruction, 2026-09-16 (ADR-094):** *"TITLE ONLY. Copy and chips are earned, never
template slots."* G16 is not lifted — it is narrowed here, and this namespace is where it does
most of its work. What follows replaces, on an LP2 page only, the bands G16 took on 2026-09-03
from the owner's earlier generator, `product gallery img.txt`. The owner's current one,
`product-gallery-instruction.txt`, was tested on 77 renders before it was written. **G16's own
bands stand for every other type that declares a text layer** — the toplist ledes (ADR-071).

**What a line must DO has not changed.** A title is a HOOK — the reader's result, problem or
feeling — never a caption of what is in the frame, and never a line equally true of a
competitor. **What changed is the length.** G16 recorded that length was never the difference
between a hook and a caption; the owner's runs agree, and set the hook short. Every one of the
76 titled renders in them ran one to five words.

| the words | the law on an LP2 page |
|---|---|
| title | **2–5 words, never more than 6.** Plain text, never inside a chip, a pill or a box |
| copy | **earned or absent** — earned only where the message needs a number, a timeframe or a mechanism the picture cannot show. 6–10 words: one sentence, one line, one full stop |
| chip | **earned or absent** — only a certification, rating or figure the page supplies, verbatim; a part label in a Callout, a Rail or a Lineup; a diagram or model label in a mechanism tile; or a use case the picture does not show. **A chip that restates the title or the copy is cut.** 1–3 words, one to a tile, except where a type keeps its own count |
| the whole frame | **at most 16 words**, labels included |

**Counted over the gallery, per twelve tiles** and scaled to a gallery of any other size: **copy on at
most 6, a chip on at most 4, at least 4 tiles carrying a title and nothing else, and at least 1
carrying no words at all.** At a cap the field is empty. Measured on the owner's runs: the four
batches written without a count put copy on 62–100% of their tiles and a chip on 36–100%, and
one tile of those 64 carried a title alone; the two batches written tighter put copy on 43% and
17%. No batch left a tile without words.

**The words a type takes:**

| type | words |
|---|---|
| `03-spec-hero` | a title, and an optional tagline of 4–8 words on one line in the same alignment |
| `06-relief-scene` | a title of at most 5 words, or none |
| `03-spec-macro` | a title of at most 4 words, off the texture, and nothing else |
| `03-use-sequence`, `03-use-grid` | a title outside the panels and nothing else; `--labelled` adds 1–3 words touching each panel |
| `03-spec-callout` | 3–6 part labels are its chips; a title is optional; no copy |
| `03-spec-lineup` | a title, and one 1–2 word label per unit |
| `02-symptom-rail` | a title, and one 1–2 word SYMPTOM label per vignette — never "relief"; no copy |
| a mechanism tile | a title in the buyer's words; one copy line of at most 10 words is presumed earned and still counted; 1–3 word labels beside the diagram or the model are its chips |

**Never, in any tile:**

- a word that repeats what the picture shows; stacked adjectives; an explanation of the scene;
- the same sentence twice; panel headers plus copy plus a chip; a word twice in a row; an
  ungrammatical title;
- **a superlative or an absolute** — *perfect, perfection, ultimate, ultra, premium, luxury,
  haven, total, zero, cloud-like, every, all-day*. The list is the owner's, and 22 of the 77
  renders carried at least one of its words;
- **a verdict word** unless the page supplies the exact claim — *approved, tested, safe,
  certified, proven, guaranteed, clinical* — 8 of 77;
- **a figure the page did not supply** — a percentage, seconds, grams, an LED count, "millions".
  Specificity is not evidence: the comb batch invented five figures in thirteen tiles. This is
  A15 as the owner settled it (ADR-095) — a figure `content.json` carries may stand, one it does
  not carry may not — and it binds every word;
- **a health or medical outcome** — *better circulation*, *stimulates blood flow* — 5 of 77.

**Read every title, copy line and label back before the prompt ships.** The owner's runs
misspelled one title of 76 and doubled a word inside one copy line.

**How the words are set.** One family, from the lock. Flat type: no outline, no shadow, no
translucent box and no gradient — contrast comes from the ground under the words. Readable on a
phone: copy at about a 32pt equivalent and a chip at about 24pt. One cluster, title above copy,
read title → copy → anything else; off the product and off the edges, in the frame's own quiet
area; no heavy block, ribbon or gradient bar.

**No name from this repo reaches a prompt.** Region names — a panel number, a zone letter,
LEFT, PREPARE — and type, variant and field names alike: one render printed "Material Macro" as
a chip. Describe the region in words (adapter Rule 1b).

**A secondary element is absent by default, and there is at most one.** It proves the tile's
message with something the picture and the title lack: a figure the page supplies, a certification
the page supplies — in words or as its mark — or a plain 2D diagram of the mechanism where the product warrants one. It never covers
the product, and it lives in the frame's empty air. An expert is never a secondary element (the
LAW row below).

**Numbers beat adjectives, and one figure replaces three claims.** If the count is right, the
tile still works with its words removed.

**A badge is a MARK and the type owns its forms** (ADR-012, ADR-043). Never `small`, never a
percentage: size it against a named object in the frame, which is the one instrument that
measured 0.51–0.96 where the same instrument on a headline measured 0.13–0.64 and ran backwards.
Three corners are open; the bottom-right carries the generation tool's watermark. **A badge
carries a colour the photograph does not** — under the lock, the set's accent — and it keeps its
interior, a tone step and two type sizes (ADR-068). **The chip form is a different thing and it
is flat.** The badge form `03-spec-callout` and `06-relief-claimstack` used to call `chip` is
`icon-disc` since ADR-094, so the one word means one thing.

**Never reserve space you do not fill.** A block that fills a third of the area it was given
will be drawn again to fill the rest — measured at seven ink bands where four were asked for.
Where the words are short and the field is large, the prompt says how much of the picture the
block occupies AND that it appears once, in one place, and nowhere else. **The owner's short
titles were drawn once in all 76 renders that carried one**, set large enough to fill their
area; a two-word title still needs its area named.

### One row that is LAW and not taste, and one the owner lifted

The owner waived G16's caps on 2026-09-03 after finding the copy too weak to ship, and set this
namespace's own counts on 2026-09-16. **Two rows moved with neither decision**, because neither
is G16's to waive. The owner has since answered the second:

1. **A named-person or named-profession endorsement — LAW.** G14 calls it illegal in its own
   words (FTC endorsement rules), and G14 binds the SLOT rather than the type — so there is
   nothing here for a type-scoped permission to lift.
2. **A certification seal, an award, a rating or a press mark — MAY BE DRAWN** (owner decision,
   2026-09-16, ADR-095, answering the trademark question put on 2026-08-18). So may the third
   class the corpus showed, a **compatibility bar** of the platforms a product works with.
   **A mark enters a frame only where `content.json` names it** — the body, the award, the
   rating, the outlet, the platform — because the words come from the page and from nowhere
   else (G16), and a mark the page does not name is an invented claim whatever it looks like.
   G6's `logo` gives way for these marks and for nothing else: the product block still bars a
   logo added to the product, and a brand's or a rival's mark stays out. **What stays G14's is
   attribution**: a rating drawn as a mark is the page's claim, while a reviewer's name, an avatar
   or a verified label on a tile still makes the tile a customer's (ADR-088). No render in this
   namespace has drawn one of these marks yet; the first set that does grades each against the
   real mark.

**The owner's Endorsed tile has no generated form this namespace can write** (ADR-094). The
instruction of 2026-09-16 lets an expert figure recommend the product, under a persona the page
supplies or one the writer invents, with a plausible name and role. **An invented expert is a
fabricated endorsement** — row 1 above, whatever the name, because the FTC's endorsement rules
that G14 cites turn on an endorser who exists and holds the expertise claimed. **A real expert is
a real photograph**: the instruction itself forbids generating a real person's likeness, and a
portrait of a named person is the `author` row of `mapping/slot-rules.md`, out of library scope
since 2026-08-18. The render behind the instruction — an invented dermatologist holding the comb
under the words "Expert Approved" — is that case. **Where a page needs the authority an expert
would lend, a mechanism tile carries it**: the `Demonstrated` form in the type map below, an
unnamed person showing how the product works, with no name, no title and no clinical dress.

## Images outside the product card's gallery

**Only the product card's gallery carries words** (owner decision, 2026-09-17, ADR-096). The
hero, every section image, both halves of a before-and-after pair, a buyer-photo tile and a
closing image carry none — no title, no copy, no chip, no label, no badge — because the page
sets its words beside them in HTML. A type that declares `text_layer` fills such a slot without
it: the `[TITLE]`, `[COPY]` and label slots an `LP2 LAW` section adds are for a gallery tile, and
the prompt keeps G6's `text, letters, numbers` whole. The product's own printing is not a word
the prompt writes; the product block keeps it. Which field is which is read from the template by
`mapping/pdp-dr-rules.md`'s *Slot kinds*.

**The hero is a banner the template crops** (ADR-096, re-measured by ADR-103). The owner
renders it at 16:9, the widest ratio the set allows (ADR-016). Read from the markup of the four
templates of 2026-09-17, every one of which crops about the centre on a desktop:

| screen | what the template shows | what a 16:9 render keeps |
|---|---|---|
| desktop, 1024–1536 px | the block at 12:5 | its height from 13% to 87% |
| desktop, 1920 px | about 3:1, because the block stops growing taller at 640 px | its height from 20% to 80% |
| tablet, 768–1023 px | 16:9, with the words stacked above or below | all of it |
| phone | 4:3, anchored to the right edge — at 77% across on `t2-eco` | its width from 25% to 100%, or 19% to 94% |

- **On a desktop the page's words sit in a panel over the image's left side.** On three
  templates the panel reaches 45–46% of the width.
- **`t1-deal` sizes its block by its words and lays its panel over the image from 768 px.**
  - The panel reaches 72% of the width at 768 px and 54% at 1024 px.
  - On a 2560 px screen, a 16:9 render keeps only 27–73% of its height.
  - The owner keeps the templates as they are (2026-09-17), so these are limits a render lives
    with, not faults a prompt can fix.

**The safe box is 55–88% across and 22–78% down.** It is where those windows overlap, less the
panel, and everything the image is about sits inside it:
- **The group** — the product, and anyone using it — fills about half the height. A 3:1 desktop
  then shows it across about four fifths of what it keeps, and a phone shows it just right of centre.
- **The product** is at least about an eighth of the width, so a 390 px phone still shows it
  whole and recognisable.
- **The left half** is the same place continuing: soft in focus, bright and low in contrast. It
  sits under the panel on a desktop and inside the frame on a phone. `PARTS/setting`'s "never
  blank" still holds, but nothing there matters to the argument, and nothing important sits where
  a phone window cuts, 19–25% across.
- **The top and bottom fifths** hold none of the group.
- **The right edge** keeps a margin, because one phone window ends at 94%.
- **The light comes from the left**, the page's side, and a person turns slightly toward it.

**Every hero prompt carries these sentences, word for word, whatever type fills the field.** The
first four go in every prompt; the fifth goes in only where a person is in the frame:

```
The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
Seen from a few steps back, the group fills about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.
```

**A hero is a photograph in full colour** (ADR-104). It shows a resolved state, so G11 asks for
full colour. The owner's feature-image instruction asks for *vivid color contrast* and a tone that
is *bright, premium, realistic, and believable*. So a session whose page has a hero writes its
lock's light and grade in these words, for every image it emits:

```
Light: bright, warm daylight from the left, with natural shadows and real contrast.
Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out.
```

- **The room keeps a few real colours** — plants, fruit, textiles.
- **A person wears a clear, friendly colour**, never the room's beige.
- **A person's expression is natural and relaxed**, never a posed or exaggerated smile (the
  owner's instruction).

**What `hero-01` measured** (ADR-104). Its lock said *pale walls*, *nothing saturated* and
*Grade: bright, neutral*.
- **Colour.** Its three renders scored 23–27 on the Hasler–Süsstrunk colourfulness scale,
  against 39 for Aure's own banner and 51 for the TopLaser product photo. The owner called the
  colour fake, dull and unfriendly.
- **Placement.** The set held it for a seated person. It lost it for a person at a counter and
  for a standing one: both put the face in the top fifth. That is why the second sentence now
  sets the camera back.
- **Products.** All three came back generic — no antennas, no printed bag, a greige device. Every
  hero prompt needs its product photo attached.

The prompt says where things sit and never states the frame's shape (ADR-016). A hero carries no
words and no inset. It routes like any slot, by its section and its copy, with `06-relief-hero`
first on this corpus (*Section routing*). The next set is `registry/pdp-dr-types/sets/hero-02/`,
which the owner grades on the four templates themselves.

**A pair shares one description.** A before-and-after pair fills two image fields, and every
prompt is one call (ADR-021), so nothing but the words holds the two files together.
- Write the locked description once: the subject — the same body area or object, the same
  person where a person shows — the framing, the camera height and distance, the light and the
  ground. Paste it into both prompts word for word.
- The two prompts differ in one line, the state. Nothing else moves: not a prop, not the crop.
- **Untested.** No pair has rendered under this law, and the first set that ships one grades
  whether two calls hold one frame.

**A buyer-photo tile is a phone snapshot, and it is always generated** (ADR-096).
- The register is `05-social-snapshot`'s: an ordinary home, found rather than styled, and a
  different room, light and distance for every tile.
- The image carries no name, star row, verified label or caption; the page sets those.
- Where G14's attribution test fires, the prompt ships with its flag and note (ADR-089), and the
  merchant decides. No LP2 session refuses.

**A block that names a person shows no face** — the `expert` blocks today. A face beside a name
is that person's portrait, and an invented person there is the endorsement this file already
refuses. The product or a pair of working hands carries the block.

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

**The set's grounds are two, and they alternate** (ADR-094). The lock names exactly two
treatments and every tile takes one; no more than two tiles in a row take the same one. A dark
or a saturated ground is still a choice the prompt gives a reason for — the product emits, the
brand owns the colour, the room is the argument — and a type whose own tone is dark is that
reason: `02-cause-anatomy`'s deep field, and `03-mechanism-*` where it takes one. **A seamless
has a floor plane and a cast shadow, never a flat void, and an infographic never sits on pure
white.**

**A real room is not a seamless** (ADR-104). The quiet ground above was measured on the outer
ring of gallery tiles. In a photographed room, quiet means light and uncluttered, never drained:
- the room keeps its real colours, a few of them clear — plants, fruit, textiles;
- the grade is G11's.

`hero-01`'s lock asked for *pale walls* and *nothing saturated*, and every render came back
beige. The owner called the colour fake, dull and unfriendly.

## Composition, scene and people

**Rule 3 says the composition varies; this is how** (owner instruction, ADR-094).

**The camera rotates through the set.** Never the previous tile's angle, and no family more than
twice in twelve: three-quarter hero, eye-level frontal, low angle, top-down flat lay, overhead at
30°, macro detail, profile, over the shoulder, product-in-hand scale, worm's-eye, rear or
underside. Depth of field, elevation and lens feel change with the type. A type that fixes its
layout — a split, a rail, a sequence, a grid, a lineup — still rotates angle, crop, distance and
place inside it.

**Two or three devices in one frame, where the frame earns them:** an inset zoom; a cutaway,
section or ghosted layer; an exploded view; a hard-divided split or before-and-after; callout
lines, at most three outside `03-spec-callout`; a sequence strip; macro against soft-focus
context; typographic negative space; a reflection or a ground plane; the product in its place
with one real functional cue in motion.

**The frame is designed.** One grid, equal margins, deliberate negative space; one reading
order and one focal point; layering, never clutter; a crop with a purpose.

- **The named corners are the top-left, the top-right and the bottom-left.** Nothing is placed in
  the bottom-right corner, which carries the generation tool's watermark (adapter Rule 7). The
  owner's runs put an inset or a locator there twice.
- **A leader, an arrow or a bracket exists only where a type calls for one** — a Callout label, a
  Rail, an Outcome Hero recall arrow, a Lineup label — **and it ends ON the part it names.** Three
  cushion renders ran a leader into empty ground, and a fourth drew a line that meant nothing.
- **Words live in the title, the copy and a type's own labels — never on an arrow, a line or a
  diagram.** A caption set along an arrow came back as *"Hips are lep or one with knees"*, and a
  stopwatch icon came back labelled.

**The scene is a photograph** unless the type's own register is a render — `02-cause-anatomy`,
`03-mechanism-*` — with real weave and grain, a cast shadow and a shallow depth of field, never
the 3D-render look of plastic sheen, uniform surfaces and weightless objects. One lighting family,
balanced, with no flat or blown glare.

- **The functional cue is only what the product really emits or moves** — never an invented mist,
  steam, glow or vibration wave (G8). Three cushion renders drew vibration or light the product
  does not make.
- **Props only where they serve the message**, and in the set's palette; the product keeps its
  photograph's.

**People appear wherever they serve the tile's message** — any number, framing, crop or role —
**and G13 binds as it always has**: no private room, no age in years, a neutral face. The owner's
comb batch brushed a child's hair at a dressing table with a towel over her shoulders, which is
the configuration G13 keeps out of a prompt.

**Casting — owner rule, 2026-09-16.** People present as the target market the page names; where
the page names none, as European or North American; never as Asian-presenting. **Name the
casting positively in the prompt**: a negative alone does not hold, and a name pulls a face toward
itself — the owner records an invented "Dr. L. Chen" rendering an Asian face, 1 of 1.

## What binds every prompt, wherever it comes from

- **Every delivered prompt is paste-and-run**: one prompt, one generation call, and as many
  reference photos as the type needs — one per product in frame (ADR-021, ADR-076). Never a
  multi-pass option, an edit chain or a post-assembly step.
- **An image outside the product card's gallery carries no words** — no title, copy, chip,
  label or badge (ADR-096).
- **The product block is mandatory** in every prompt with the product in frame — this
  namespace's form of G1, in the words the product section above fixes, with its two conditional
  sentences wherever their case exists. **One exception, on trial:** `03-mechanism-signal` follows
  the owner's feature-image output format and carries G1 in one sentence, `Use the attached product
  photo as the exact reference.`, before the instruction's closing sentence (ADR-101).
- **G2 limits the PRODUCT slot to four kinds of information** — position, angle, scale in
  frame, and relation to other objects. Not shape, not material, not colour, not
  construction, not an aesthetic adjective. The reference photo carries appearance; the
  prompt only places it. **This is the clause a gallery breaks most**, because a gallery is
  about the object and the writer reaches for the object's own adjectives.
- **Never state the frame's shape or ratio in prompt text** (ADR-016, adapter Rule 4). A
  written ratio did nothing to this renderer, 6 of 6.
- **A15, as the owner settled it** (2026-09-16, ADR-095): **a figure enters a frame only where
  `content.json` carries it.** No source is required beside it; where the page gives one it may
  sit there, and the five honest forms in the corpus finding below stay the stronger choice. A
  figure the page does not carry never enters, in the text layer or printed on an object.
  **An object's own printing is its reference photograph's**: `07-identity-pack`'s founding
  render wrote a net weight and an ingredient list onto a pouch, in a round that did not record
  whether a photograph was attached, and the owner's answer is the attached photograph and the
  product block rather than a word-by-word check.
- **G13 has no exemptions.** A refused prompt returns no image at all, which is a different
  failure class from a weak one.

## A slot named by its ROLE takes a DEFAULT — name the value

The law of 2026-09-09 (`ac10f69`) applies here without change. A skeleton slot that names
what a thing is FOR gets the renderer's habitual answer for that role: `[BADGE] one short
stamp` produced six identical flat rectangles, all `small`, all lower-left, all borrowing a
colour already in the frame. The repair is not a longer role description. **It is to name
the VALUE** — which form, how wide against what object, which corner, which colour the
photograph does not already have.

## The owner's gallery instruction, type by type

**Owner instruction, 2026-09-16:** *"đưa các cơ chế của instruction vào các type ảnh tương
ứng"* — put the instruction's mechanisms into the matching image types (ADR-094). The
instruction names seven types in gallery order, and this is where each one lives. A type whose
mechanism is written in its own file carries it there: in a `## LP2 LAW` section where the file
is a verbatim copy, and in place where it is LP2's own draft.

| the instruction's type | LP2 id | status | where its mechanism is written |
|---|---|---|---|
| Problem Tile · Before–After Split | `01-pain-split` | active copy | its `LP2 LAW` |
| Problem Tile · Symptom Rail | `02-symptom-rail` | active copy | its `LP2 LAW` |
| Problem Tile · Cause Anatomy | `02-cause-anatomy` | active copy | its `LP2 LAW` |
| Hero + Angle & Detail | `03-spec-hero` | reserved draft | in place, 0.2 |
| Feature + Benefit · Applied Use Storytelling | — | **no file** | below; the nearest corpus proposal is `03-use-demo`, 4 sources, undrafted (ADR-078) |
| Feature + Benefit · Comparative / Proof | `04-proof-lockedframe` | active copy | its `LP2 LAW` |
| Feature + Benefit · Callout | `03-spec-callout` | reserved draft | in place, 0.4 |
| Feature + Benefit · Material Macro | `03-spec-macro` | active copy | its `LP2 LAW` |
| Feature + Benefit · Lineup | `03-spec-lineup` | reserved draft | in place, 0.2 |
| Mechanism · Body | `03-mechanism-ghostbody` | active copy | **below, until its re-copy** |
| Mechanism · Contact | `03-mechanism-contact` | reserved draft | in place, 0.4 |
| Mechanism · Product X-ray | `03-mechanism-xray` | active copy | **below, until its re-copy** |
| Mechanism · Principle | — | **no file** | below; a signal the product sends or senses is `03-mechanism-signal`, a reserved draft (ADR-099) |
| Mechanism · Demonstrated | — | **no file** | below |
| Mechanism · Endorsed | — | **not written** | the LAW row of the text section |
| Use Steps · Sequence | `03-use-sequence` | active copy | its `LP2 LAW` |
| Use Steps · Grid | `03-use-grid` | active copy | its `LP2 LAW` |
| Outcome Hero | `06-relief-hero` | active copy | its `LP2 LAW` |
| Contextual / Lifestyle | `06-relief-scene` | active copy | its `LP2 LAW` |

**A copy's `LP2 LAW` is the copy's own, and a re-copy keeps it.** Every other section of a copy
is its parent's text, spliced by script. `LP2 LAW` is the divergence ADR-091 made room for — *a
type that must keep its clause here says so by editing the copy and its CHANGELOG* — gathered in
one section, beside the frontmatter's `text_layer`, so a re-splice carries both across untouched.
**From its first LP2 edit a copy's `version` is its own sequence**; `copied_at_version` alone
links it to the parent, and it is the only field `scripts/validate.py` compares.

**Two copies take their `LP2 LAW` in the re-copy another lane owes.** `03-mechanism-ghostbody`
and `03-mechanism-xray` are copied at 2.3 and 1.4; their parents stand at 2.4 and 1.5,
uncommitted, in another lane, whose commit owes the re-copy (ADR-091). Their LP2 law is written
here until then, and it binds them now, since this file binds every copy in the folder.

**`03-mechanism-ghostbody` on an LP2 page — the instruction's Body.**
- For a product that changes a body POSITION: posture, angle, curve, where the weight rests.
- **Two body forms.** The copy's own featureless mannequin, which keeps its no-face law; or a
  semi-transparent real person, where a face is allowed — the instruction's form, with no render
  of it as a whole tile yet.
- The spine, the pelvis or the joints are drawn INSIDE the body. The product is placed, never
  described and never opened.
- **The comparison may be split across two tiles.** Where a `02-cause-anatomy` tile on the same
  page draws the same body wrong — its `ghost-mannequin` style is that body — this tile may show
  the right state alone. Otherwise the copy's two panels stand.
- **Marks: one spine line, one pelvis or joint arrow, pressure zones in one neutral tone.** Red
  only inside a wrong-state half, and the set's accent never on the body — so the copy's blue
  `support` band gives way to the neutral tone here, since a set whose accent is blue cannot tell
  the two apart. Name the structure, never a count.
- A dark key is allowed.
- The words: a title in the buyer's words; one copy line of at most 10 words; 1–3 word structure
  labels beside the structures, never on a line.

**`03-mechanism-xray` on an LP2 page — the instruction's Product X-ray.**
- Only components **the page names** are solid inside the shell. **Where the page names none,
  the type is locked** — take the Body form, or the Principle form below. **A cushion, a mat or a
  garment has no interior to show**; two cushion renders drew one anyway.
- **Labels are allowed, and a figure only where the page supplies it.** A 1–3 word label naming a
  component the page names is the type's chip — the owner's comb render labelled its atomiser
  cleanly. The copy's ban on spec and capacity text gives way to a figure `content.json` carries,
  and to nothing else (A15, ADR-095).
- A dark key is allowed. The words as for any mechanism tile.

**Three mechanisms with no file.**
- **Principle** — the science is general physics or biology: a point load against a spread load,
  slow rebound, airflow, an ingredient's action. One clean 2D or 3D diagram BESIDE the product or
  in an inset, in one neutral line colour, **never painted onto the product and never a rainbow
  gradient**; a figure only where the page supplies it. The owner's runs tried the
  form three times and painted all three onto the product — a heat map twice, flow waves once — so
  it has no passing render and no corpus id. **A signal the product sends or senses — WiFi,
  Bluetooth, detection — is not this form.** It is `03-mechanism-signal`, a reserved draft since
  ADR-099, whose marks run from the product to what it reaches.
- **Demonstrated** — an unnamed, untitled person demonstrates the mechanism on a spine or pelvis
  model, or on a seated person; the model may carry 1–3 word part labels. No "recommended by", no
  "clinically", **and no clinical dress or clinic setting**, which would present the demonstrator
  as a practitioner and make the tile the named-profession endorsement the LAW row refuses. The
  authority is the demonstration's. No render and no corpus id.
- **Applied Use Storytelling** — a feature in real, energetic use: the light, motion and water of
  the place, with the product and the place integrated — splashes, sweat, reflections. Copy only
  where earned; a "For [use]" chip only where the picture does not show the use.

**A mechanism tile sits on the set's light grounds** unless it is Body, Contact or X-ray, which may
take a dark key; and **a set carries one mechanism variant** unless the page asks for two
(`mapping/pdp-dr-rules.md`).

**Each type's musts, for the check before a prompt ships:** Split — the product in the after
panel, the verdict marks flat discs; Rail — photographic vignettes, a white ring, symptom labels;
Sequence — nothing drawn inside the panels; Callout — no copy, and every label a part serving the
one claim; Comparative — headers once, any figure the page's; Macro — a title only, a locator never
in the bottom-right, one macro to a set whatever the surface; Grid — no label, chip or badge inside
a cell; Hero — no leader, and no chip unless earned; Mechanism — the variant fits the product
class the page describes, X-ray only with named components, nothing drawn on the product's
surface, one variant to a set; Cause Anatomy — the product absent or a silhouette; every chip in
the lock's form.

## The owner's feature-image instruction — 2026-09-17

**Owner instruction, 2026-09-17** (ADR-100): the first five renders of `03-mechanism-signal` were
*"cực kì tệ"* — extremely poor — next to the reference images, and the owner pointed this
namespace at `~/Downloads/feature image.txt`, the owner's generator for LP2 feature images, *"để
học cách viết prompt cũng như cấu trúc skeleton của type"*: to learn from it how to write the
prompt and how to structure the type's skeleton.

**What the instruction asks for:** a contextual, usage-first photograph that reads in three
seconds.
- The product is in use or installed, the visual anchor, whole and unobstructed, in a real place
  that explains why it matters.
- The light is bright and contrast-driven, and the product separates clearly from its
  background.
- Hands or a person appear where they explain the use. Faces are allowed where relevant and
  never pose. Pets appear only where the product serves them.
- No decorative props, no product set out for display, and no text overlays.
- The prompt is one natural paragraph with no labels, and it ends with the instruction's
  closing sentence word for word.

**Where it binds today:** `03-mechanism-signal`, from 0.3, whose `PARTS/form` carries the
closing sentence. Adapter Rule 6 names the exception to its slot form. **From 0.5 that type's
skeleton IS the instruction's output format**, on the owner's instruction *"hãy thử đặt skeleton
giống output format của feature image txt"* (ADR-101).

**What it changes, on trial, for that type alone:** the product block leaves the prompt. G1's
obligation stays in one sentence, `Use the attached product photo as the exact reference.`, just
before the closing sentence, which carries the rest of the fidelity.

**What it does not change here:**
- The product block stays in every other LP2 prompt.
- The ground stays light by default. The frame's contrast comes from light and focus.
- Only the product card's gallery carries words (ADR-096).
- G6 keeps interface text off every screen, and G2 keeps construction words out of the prompt.

**Not decided:** whether the other types that fill section fields take the same form.

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
better models, each in a real page. **The owner's rule of 2026-09-16 requires none of them**
(ADR-095) — a figure the page supplies may stand bare — so they are the stronger forms a tile
may choose, not a gate:

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

Nothing in G16, G14 or the two LAW rows reached it, and **G6 bans logos outright** while the
source carries twelve. **Decided by the owner on 2026-09-16** (ADR-095): a compatibility bar may
be drawn where `content.json` names the platforms. `03-spec-claimstack` still has no mark
library; the gate on writing one is gone, and the library is written with the first set that
draws a mark.

## What this namespace is still waiting on

**None of LP2's own drafts routes.** Seventeen files: fifteen `status: reserved`, each carrying a
`blocked_by` and a `BLOCK`, and two `deprecated` — `07-identity-callout`, retired on 2026-09-11
and replaced by `03-spec-callout` after a control render and a ten-source corpus answered the
same question the same way, and `06-relief-animal`, retired on 2026-09-17 after the owner put an
animal subject into the relief types (ADR-095). `registry/pdp-dr-index.yaml` gains none of them.
What routes on an LP2 page today is the seventeen verbatim copies of the active image types,
through that index, ordered by `mapping/pdp-dr-rules.md` (ADR-091).

**Six drafts clear SPEC §6.3 criterion 1** — `03-spec-callout`, `06-relief-claimstack`,
`07-identity-pack`, `03-spec-claimstack`, `03-spec-dimension` and `03-spec-hero`, at 11, 10,
10, 9, 7 and 7 distinct sources on 2026-09-17. The counts are `python3 scripts/validate.py --evidence`'s and move with
the ledger; read them there. Until this paragraph was rewritten it named three files at 8, 7
and 6, which the ledger had already passed. **Every one of them is blocked on criterion 2**, and
four of those tests are one test: can a router separate two types that share a device and
differ only in job? — `03-spec-claimstack` against `06-relief-claimstack`, `03-spec-dimension`
against `03-spec-callout`, and `03-spec-hero` and `06-relief-claimstack` each against
`06-relief-hero`. Each file's `blocked_by` names the rest.

**The owner decisions this section used to list are taken** (2026-09-16, ADR-095): a mark the
page names may be drawn; a figure `content.json` carries is substantiated; an animal is a
subject the relief types take, not a type of its own; and LP1 routes `03-mechanism-contact` once
it is promoted, which `mapping/pdp-dr-rules.md` registers. `04-proof-stat` now waits on a fifth
source, its first skeleton and set, and criteria 2 and 3.

**Criterion 2, the router-confusion test, is the one no owner decision unblocks**, and it is the
binding gap on every draft above. ADR-066 refused to promote past it once already, before any of
the siblings existed to make it concrete. **What still waits on the owner is verdicts**: SPEC
§6.3(3) takes the owner's own on a rendered example, and three drafts name one as outstanding —
`03-spec-callout`, `03-spec-lineup` and `03-mechanism-contact`.

**Prompts under this namespace's law exist, and one set has rendered.**
`sets/03-mechanism-contact-01/` rendered six on 2026-09-16, harness-graded; the other sets
under `sets/` are owner-gated and wait on renders. Six drafts carry FOUNDING RENDER ROUND
sections; those renders are real and their measurements stand.
