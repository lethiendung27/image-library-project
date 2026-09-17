---
id: 03-spec-hero
step: 3
job: spec
device: hero
version: "0.3"
status: reserved
replaced_by: null
channels: [landing-page, marketplace]
requires_product_photo: true
generation_mode: single-pass
axes:
  inset_mode: [none, detail, context]
text_layer: [title, copy, badge]
variants: []
exempt_from: []
pairs_with: []
never_with: []
avoid_adjacent: [06-relief-hero]
requires_pair: null
blocked_by: "Criterion 2, the router-confusion test against 06-relief-hero, which is ACTIVE at 19 sources on this corpus and is the same device with a different job. Criterion 3 has no render."
---

# 03-spec-hero — PDP-DR DRAFT

Promotion status (2026-09-11): **6 distinct sources — criterion 1 CLEARED.**

| source | the scene | the claim the headline makes |
|---|---|---|
| capix-mat | the mat in a tent, on white, and its own surface in close | fabric, integral pillow, 10cm thickness |
| glowy-liff | a woman holding the wand, twice across two colourways | the modality list, with three LED-state insets |
| gripi-mata | feet on the mat in four settings — room, entryway, folded, in-use | resilience, non-slip backing, absorbency |
| moisosat | the dehumidifier **standing in a snowdrift** | automatic defrost |
| mozzapx | the lamp at dusk, in rain, in daylight, with a hand on the mesh | solar power, IPX5, dual charging, safety gap |
| pawdi-cas | the camera on a desk, and turned away on a nightstand | TF card storage, privacy mode |

Criterion 2 is the binding gap. Criterion 3 has no render. **Not routable.**

**The construction is the commonest in the corpus and the registry half-owns it already.**
Counting this type with its two job siblings, one photograph carrying a baked headline block
appears in **23 of 36 sources**. `06-relief-hero` is ACTIVE and holds 19 of those.

## PURPOSE
One photograph and one baked headline block, and the headline makes a claim about what the
product IS or DOES. No panels, no cut-out, no card — the words sit in the picture's own quiet
area. The tile that carries a single feature when a claim stack would be four claims too many.

**It is the owner's "Hero + Angle & Detail"** (ADR-094): shape, identity and craftsmanship, the
product as the object of the frame — which is this type's claim about what the product IS, shown
by the angle that makes it visible.

## TRIGGER
use_when: >
  The page needs one tile to carry ONE feature and to show it happening. A gallery tile
  between the packshot and the spec block, a feature tile that has to work at thumbnail size,
  or the tile that replaces a paragraph about a single capability. Choose 06-relief-hero when
  the headline names a FELT STATE or an outcome rather than a property — that is a different
  job and SPEC 3.1 makes two jobs two types however alike the picture. Choose
  03-spec-claimstack when there are three or more features to name at once. Choose
  03-spec-macro when the claim is about a surface or a component and the whole product does
  not need to be in frame.

## SKELETON
```
TYPE: 03-spec-hero v0.3
REGISTER: commercial product photograph or lifestyle photograph. One frame.

[PRODUCT REFERENCE]  the attached photo is the exact reference.   -> G1
[SCENE]              the product doing the thing the headline claims. -> PARTS/scene
[SETTING]            a quiet ground, or the place the claim is true in. -> PARTS/setting
[LIGHT]              whatever the setting has; the claim stays legible.
[QUIET AREA]         where the words go, decided before they are written. -> PARTS/quiet-area

[TITLE]              the claim, as a hook, 2–5 words.             -> SLOT CONSTRAINTS
[TAGLINE]            optional, 4–8 words, one line, same alignment. -> SLOT CONSTRAINTS
[BADGE]              one short stamp. Optional, and only where earned. -> MARKS
```

## PARTS

**`scene`** — the product doing, or having done, the thing the headline claims. This is the
type's whole discipline and the corpus keeps it: a foot pressing a mat leaves a depression, a
lens turned away IS privacy mode, rain falling on a lamp IS the ingress rating, a finger on a
mesh IS the safety gap. **A headline over a product that is merely present is the failure
mode**, not a variant.

**A claim about FORM is shown by the angle that makes the form visible** (ADR-094). One piece, a
contour, how a thing is made: there the product as the object of the frame IS the demonstration,
on a seamless with a floor plane and a cast shadow or in its place, and the camera is chosen for
the part the claim names. An angle that hides that part is the merely-present failure again. A
claim about FUNCTION is still shown happening.

**`setting`** — a quiet ground by default: light in value, close to neutral in colour
(ADR-068). A real place is legal and is the better choice where the claim is about a
condition — rain, night, a doorway, a bathroom floor.

**`quiet-area`** — decided BEFORE the words are written, not after. Five of the six sources
put the block in a band the photograph already leaves empty: the shadowed end of a tent, the
sky above a lamp, the white above a cropped product. G16's own measurement applies —
**never reserve space you do not fill**, because a short block in a large empty field gets
drawn twice.

## MARKS
**No leader, no decorative line, and no chip unless it is earned** (ADR-094). The owner's five
hero renders under the instruction: one clean, a title alone on a seamless; the others drew a
sweeping line that meant nothing, ran a leader from the copy to empty ground, set a chip
restating the copy, and titled a distorted product "Ergonomic Perfection".

Optional and plain. Where a badge appears in the corpus it is a single icon in a disc — a
snowflake for defrost, a foot-and-slip glyph for a non-slip backing, a shield for a safety
claim. **One badge, and it names the same thing the headline names**; a badge making a second
claim turns this type into a claim stack with a picture.

## SLOT CONSTRAINTS
- **The headline is a HOOK, not a caption, and it is short** (ADR-094). An identity hook of 2–5
  words, never more than 6, with an optional tagline of 4–8 words on one line in the same
  alignment — centred, or upper left with a margin. A caption describes the frame; a hook
  describes the reader; and G16 recorded that length was never what separated them.
- **Never a product name the page did not write.** One of the owner's hero renders titled the
  product with a brand of its own invention.
- **G2 binds hardest here.** The PRODUCT slot may carry position, angle, scale in frame and
  relation to other objects — nothing about shape, material, colour or construction. This is
  the type most likely to break it, because the headline is usually ABOUT the material and the
  writer reaches for the product's own adjectives.
- **No exemption from G7.** Unlike every other type in this namespace, this one is
  photographic and its settings are real places, so context integrity binds whole. See BLOCK
  for the one thing the corpus does that G7 refuses.
- **A15 binds the headline.** `capix-mat` asserts "10CM thickening" with nothing behind it in
  one tile and photographs a tape measure against the same edge two tiles later. Since the
  owner's decision of 2026-09-16 (ADR-095) both are legitimate where the page supplies the
  figure; the second is the stronger form, and the one to reach for first.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a product that is merely present rather than doing the thing claimed,
a second headline, a paragraph, a claim stack, a certification seal, an award,
a press mark, a figure the page did not supply, a gradient bar behind
the words, a setting the product could not actually be in, a leader line, a decorative line,
a product name the page did not write
```
Where the page names a certification, an award or an outlet and the tile carries its mark, the
prompt drops that item from this list (ADR-095).

## BLOCK
**Waiting on criterion 2 against `06-relief-hero`**, which is ACTIVE, holds 19 distinct
sources on this corpus, and is the same device with a different job. Those two plus
`03-use-hero` — one source, no file — are one construction spread across three jobs, and
between them they cover 23 of the corpus's 36 sources. A router that cannot separate a
capability headline from an outcome headline will route this type or that one at random on
every product page. That test has never been run and it is the largest single routing risk
this namespace holds.

**Criterion 3 has no render.**

**And one thing the corpus does that this type may not.** `gripi-mata` composites a bath mat
onto cloud forms; `moisosat` stands a mains dehumidifier in a snowdrift. Two sources, two
categories, both building an IMPOSSIBLE setting to make a claim literal. G7's context
integrity refuses a product in a place it could not be, and this type takes no G7 exemption.
Whether that is a gap in G7 or a discipline this type should keep is an owner decision; until
it is taken, the NEGATIVE above refuses it.

## KNOWN-FLAKY
- **No prompt from this file has rendered.** The five hero renders in the owner's instruction
  runs are recorded under MARKS as the instruction's evidence, not this file's.
- Predicted from the corpus: the failure mode is a headline over a product that is not doing
  anything. Five of the six sources avoid it and `mozzapx` does not — its solar tile shows a
  lamp lit in full daylight while the same page's copy claims the lamp turns itself off during
  the day. Recorded as the first thing a founding round should check.

## CHANGELOG
- 0.3 (2026-09-17): two owner decisions of 2026-09-16 (ADR-095). A figure the page supplies may
  stand without an instrument in frame, which stays the stronger form; a certification, award or
  press mark the page names may be drawn, and the negative drops it then.
- 0.2 (2026-09-16): the owner's Hero + Angle & Detail lands here (ADR-094). A FORM claim is shown
  by the angle that makes the form visible; the title is an identity hook of 2–5 words with an
  optional one-line tagline; no leader, no decorative line, no chip unless earned, no invented
  product name — the faults four of the owner's five hero renders showed.
- 0.1 (2026-09-11): drafted from eighteen observations across six distinct sources, batches
  2026-09-11-A, D, E, G, H and I. Criterion 1 cleared at six; criterion 2 against
  `06-relief-hero` is the binding gap and criterion 3 is unrun. Filed as a spec-job sibling
  under SPEC 3.1 rather than merged into the active relief-job type. `03-use-hero` stands at
  one source and deliberately gets no file. Device `hero` already exists. Raised and evidenced
  by `_CURATION-2026-09-11.md`. ADR-078.
