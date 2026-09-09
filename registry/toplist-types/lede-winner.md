---
id: lede-winner
version: "0.6"
status: active
replaced_by: null
products_in_frame: one
requires_product_photo: true
awareness: [product-aware, most-aware]
text_layer: [title, badge]
copied_from: null
copied_at_version: null
blocked_by: null
exempt_from: [G7]
---

# lede-winner

## PURPOSE
The designed promotional hero of a top-N page. Cut-out product on a loud designed ground,
carrying **oversized display type, a verdict mark, or both** — and the words are the
argument, not a caption on it. This is the frame a reader recognises as "the offer" or
"the pick" before reading anything in it.

**The type was drafted as "the number one alone, presented as chosen: a packshot carrying
a verdict".** The owner named three examples on 2026-09-09 and two of them had been filed
elsewhere by this session, which is what corrected the definition. A packshot with a small
badge is not this type; a television under the words TV DEALS, with no mark at all, is.

## TRIGGER
use_when: >
  The page's lede has to announce a verdict or an offer rather than show a field or a
  test. Purchase-intent traffic, where the reader has decided to buy in this category and
  the page's value is the pick. Take it over lede-collage when the frame carries words or
  a mark; take lede-collage when the units carry the argument alone.

## BOUNDARY
**Against `lede-collage`, and this is the line the owner's three examples drew:** a winner
frame carries **display type, a mark, or both**; a collage carries **neither**, and its
argument is the units themselves. Checkable at a glance, and it survives the frame having
several products — one of the owner's three has three laptops in it.

The boundary was previously drawn on product COUNT, which is why two of the owner's three
examples were misfiled. Count is not the discriminator; **words are**.

**Against `07-identity-pack`** (image registry, staging) — that type argues IDENTITY, what
the thing is as it arrives, on a quiet ground and with no words. This one argues SELECTION,
loudly. The near-white sheets frame carrying a small awards badge sits on that line and is
filed `variant-candidate` rather than `match` for exactly that reason.

**Against `lede-testing`** — no bench, no apparatus, no hands.

## SKELETON
```
TYPE: lede-winner v0.6
REGISTER: designed promotional composition, one frame.

[PRODUCT REFERENCE]  the attached photo is the exact reference.       -> G1
[SUBJECT]            the unit cut out and floating, hero-lit.         -> PARTS/subject
[GROUND]             a designed field: light, strongly coloured.      -> PARTS/ground
[DISPLAY TYPE]       the page's own line, oversized. Optional.        -> PARTS/title
[VERDICT MARK]       the page's own verdict, as a mark. Optional.     -> MARKS

At least ONE of DISPLAY TYPE and VERDICT MARK is present. Neither is a collage.
```

## PARTS

**`subject`** — the unit **cut out, with no scene behind it**, floating over the ground and
lit as a hero rather than as a photograph of a place. It carries no shadow that implies a
surface.

**Frame population is `one` by default and `many` is a real observed form.** Two of the
five corpus frames carry three and five products. That form inherits the blocker
`lede-lineup` and `lede-collage` carry — one attached reference photo per prompt against
ADR-021's limit of one — so a multi-product winner is not routable until that decision is
taken, and the frontmatter stays `one`.

**`ground`** — a DESIGNED field, measured on this type's five corpus frames and nothing
imported:

| | measured |
|---|---|
| texture | **1.5** — smooth, no grain, no paper, no vignette |
| value | **0.99** — light, at the very top of the namespace |
| saturation | **0.55** — strongly coloured |
| value spread around the ring | 0.17 — evenly lit by construction |
| hue spread | **138°, 175°, 177°, 179°** on the four loud frames |

**A two-hue gradient travelling most of the colour wheel, or a graphic field of stripes and
blocks in the same two-hue register.** Magenta to lime, purple to teal, magenta to orange,
red to blue. This is the loudest ground in the namespace and it is the type's signature —
`lede-testing` sits at 0.13 saturation, `lede-lineup` at 0.26.

**The one quiet frame is filed as a variant-candidate, not as evidence.** A near-white
sheets packshot with a small awards badge measures 0.03 saturation and 0° of hue spread,
against the owner's three at 0.55–0.60 and 138–179°. It is recorded as diverging rather
than folded in as a second mode; deciding whether it belongs here or with
`07-identity-pack` is the owner's.

**`title`** — **oversized DISPLAY TYPE, and it is a slot rather than a caption.** In the
corpus it is set larger than any word in the rest of the namespace, sits BEHIND or ACROSS
the cut-out units, and is routinely **cropped by the frame edge** — `LAPTOPS` runs off both
sides, `TV DEALS` fills the upper third. One or two words, the page's own line about its
own ranking or offer.

**This is the one place in the library where type may be cut by the edge**, and it is
deliberate: G10's safe area governs words that must be READ in full, and a display word
that runs off the frame is being used as a graphic. The words that must be read in full —
the mark's line — still keep the margin.

## MARKS

**The type owns the badge's FORM; G16 owns its WORDS.** Named per product; never a default.

| form | shape | observations |
|---|---|---|
| `plaque` | a rectangle with a rule across it, a short line above and a year below | **2** — the two CNET frames |
| `sticker` | a die-cut circle sitting on the ground like an applied label, often tilted | **1** — the AirPods frame |
| `none` | display type carries the whole argument and no mark is present | **1** — the TV DEALS frame |
| `band` | a horizontal band across the frame | 0 — the owner's own named form, untested |

**One mark per frame.** **Three corners are open and the bottom-right is not** — the tool's
watermark (`adapters/nano-banana.md` Rule 7). **The mark may sit OVER a unit**: both plaque
frames place it across the centre product.

**A badge is not flat and it is not one word at one size** (G16, ADR-068). At least one
internal tone step — a rim, a ring, an outline inset from the edge — and at least two type
sizes. Both corpus plaques carry a label over a big word over a year.

## SLOT CONSTRAINTS
- **The verdict text comes from the product input's rank or verdict field and from nowhere
  else.** A prompt may not invent a placing. The field does not exist yet, so
  `mapping/toplist-rules.md` layer 1 refuses this type on every page until it does.
- **A SCORE carries A15's leash**: it enters the frame only where the input carries it.
- **Another party's mark stays refused.** The corpus carries `CNET LAB TEST WINNER`,
  `CNET PEOPLE'S PICKS` and `GOOD HOUSEKEEPING BEDDING AWARDS` because on those publishers'
  own pages they are the issuing body. On a page that is not theirs it is a trademark
  question, unanswered since 2026-08-18. **Three of five corpus frames carry one**, which
  makes this the most-breached refusal in the namespace and worth the owner's attention.
- **A fabricated endorsement stays refused** — a customer's name, star row, review count or
  verified mark. G14, and it binds the SLOT.
- **G16 binds every word and the mark.** Not restated here.

## NEGATIVE
```
[G6] + a real scene, a room, a surface the unit stands on, a person,
a price, a fabricated rating or star row, a certification seal,
a press logo, a third-party award mark, an invented placing or score
```

## FOUNDING RENDER ROUND

**One render, 2026-09-09 — round 2 prompt 5, rendered at v0.5.** Wireless translation
earbuds, `sticker` mark, the FLAT ground form. Verdict **`partial`**, self-assigned under
ADR-011 on a render that was opened and looked at. Ledger: `eval/render-tests.jsonl`,
ts `2026-09-09`.

**Three clauses got their first evidence.** Measured with the ring metric of
`scripts/ground_audit.py`, so these numbers and the corpus numbers come from one function:

| clause | asks for | this render |
|---|---|---|
| `PARTS/ground` texture | 1.5, smooth | **1.3** |
| ring value spread | 0.17 | **0.15** |
| flat form, hue spread | under 13° | **1°** |
| `PARTS/ground` value | 0.99 | 0.84 |
| `PARTS/ground` saturation | 0.55 | **0.92** |

**`PARTS/title` delivered exactly as written**, which is worth recording because it is the
strangest clause in this file: EARBUDS set BEHIND the case, overlapped by it, and cut by
BOTH side edges — measured from x=0 to x=1198 in a 1200px frame. It reads as a graphic
rather than as a mistake, which is what the clause claims and had never been tested.

**The `sticker` mark carried an interior, and that is the first time anywhere in this
library.** ADR-068 measured 5 of 6 direct-response badges dead flat at 0.02–0.09 of
internal value spread and closed the gap with a clause that nothing had yet met. This
render meets it: a white ring inset from the die-cut edge, a tone step across the fill,
BEST OVERALL over 2026 at two sizes. n=1, and it is the only n that clause has ever had.

**The ground came back louder than this type's own corpus.** *"A clear cobalt"* returned
saturation 0.92 where the five corpus frames sit at 0.55 and none exceeds 0.60. **Recorded,
not patched**: 1 of 1 is below SPEC §6.2's threshold, and one render cannot separate a
prompt's word choice from a property of the type.

### What this render cannot settle, and both belong to the owner

- **Was the product DEPICTED or INVENTED?** The earbuds render as a recognisable
  real-world form carrying an `R`. ADR-075 permits depicting a real brand from an attached
  reference and refuses an invented one; which of the two happened is visible only to
  whoever attached the photo.
- **G10 and `PARTS/title` are in conflict, and this render is what exposed it.** G10's
  scope reads *"every layer of every type ... No exemptions"* and its text says no word may
  touch or cross a frame edge. `PARTS/title` licenses exactly that and ADR-074 reasons for
  it — but SPEC §5 says a type opts out only through `exempt_from` and only where the
  rule's own scope permits, and this file declares `exempt_from: [G7]` alone. The library
  is teaching a G10 exception that no rule grants. Amending a global rule is not taken
  here.

## CHANGELOG
- 0.6 (2026-09-09): **FOUNDING RENDER ROUND** — one render, round 2 prompt 5 at 0.5,
  `partial`. First evidence under `PARTS/ground` (texture 1.3 against 1.5, spread 0.15
  against 0.17, the flat form at 1° of hue spread) and under `PARTS/title`, which returned
  a display word cut by both side edges exactly as written. The `sticker` mark carried the
  interior ADR-068 asked for — the first time that clause has been met in this library's
  output. Ground saturation 0.92 against the corpus 0.55: recorded, not patched, at 1 of 1.
  Two questions raised for the owner, one of them G10 against `PARTS/title`.
- 0.5 (2026-09-09): **rewritten after the owner named three examples and two had been
  filed elsewhere by this session** (ADR-074). The discriminator against `lede-collage` was
  product COUNT and is now WORDS: a winner frame carries display type, a mark, or both; a
  collage carries neither. `PARTS/title` is new and central — oversized display type, set
  behind or across the units and routinely cropped by the frame edge. `PARTS/ground`
  rewritten on 5 frames: texture 1.5, value 0.99, saturation 0.55, hue spread 138-179.
  MARKS gains `none` as an observed form. The bimodality reported this morning was my own
  misclassification, not a property of the type.
- 0.4 (2026-09-09): `PARTS/ground` **rewritten from this namespace's own 32 frames**, with
  no rule imported (ADR-073, owner instruction). The clause gains what a prompt actually
  needs and 0.3 did not carry: smoothness as a measurement (texture 0.8, the smoothest
  ground in the corpus), and the gradient's FORM — two hues roughly opposite on the wheel,
  running diagonally, 179° of spread.
- 0.3 (2026-09-09): owner audit. **`PARTS/ground` added and it reverses half of what 0.2
  shipped**: ADR-068's rule was imported whole and this type's corpus runs saturation 0.60
  against its 0.06 — light transfers, quiet does not, because a cut-out unit leaves the
  ground as the only place colour can live. **`MARKS` added**: the type declared a badge
  and owned no form library, which is the gap ADR-068 closed for the three staging types
  and this file reopened. BOUNDARY's "the reason the file is reserved" is stale and
  corrected. Recorded plainly: the type is ACTIVE on **one** corpus observation, and that
  observation carries a discount sticker rather than a rank.
- 0.2 (2026-09-09): **reserved → active** (ADR-071, owner instruction). The verdict mark
  is permitted where it is the PAGE'S OWN — the distinction 0.1 put to the owner is the
  one taken. `text_layer: [title, badge]`, so G16 binds this type. `BLOCK` becomes `SLOT
  CONSTRAINTS`: the verdict text comes from the input's rank field, a score carries A15's
  leash, and a third-party mark and a fabricated endorsement stay refused because the
  permission did not cover them.
- 0.1 (2026-09-09): drafted `reserved`. Recorded plainly: without its verdict mark this
  type collapses into `07-identity-pack`, which is the absorption ladder of SPEC §3.2
  doing its job rather than a defect in the draft. ADR-069.
