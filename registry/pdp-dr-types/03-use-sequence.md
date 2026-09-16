---
id: 03-use-sequence
step: 3
job: use
device: sequence
version: "1.12"
status: active
replaced_by: null
channels: [marketplace, landing-page, advertorial]
requires_product_photo: true
generation_mode: single-pass
axes:
  camera_lock: [handheld]
variants: [labelled]
exempt_from: [G3, G4]
pairs_with: [03-mechanism-ghostbody]
never_with: []
text_layer: [title]
copied_from: 03-use-sequence
copied_at_version: "1.11"
blocked_by: null
---

# 03-use-sequence

## PURPOSE
Reassure about operation: three stacked panels, one action each, read by action logic
alone — nothing in the frame numbers the steps or points from one panel to the next.
Answers "can I actually use this?" without looking like an instruction manual.

**Copied verbatim from `registry/types/03-use-sequence.md` at version 1.11** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## LP2 LAW
Added 2026-09-16 (ADR-094): the owner's gallery instruction for Use Steps · Sequence. This section is
this copy's own and a re-copy keeps it; `registry/pdp-dr-instruction.md` binds the rest.

- **The words: a title of 2–5 words OUTSIDE the panels, and nothing else.** No copy and no chip.
  `--labelled` adds one label of 1–3 words, or a numeral, touching each panel; arrows stay banned.
- **Nothing drawn anywhere, including on packaging.** Two of the owner's renders printed an arrow
  on the shipping box.
- **No frame and no border around a panel** — the thin white gutters are the only divider. Three
  of the owner's four sequence renders set their panels in rounded frames; the fourth, labelled
  with a numeral and a word touching each panel and nothing framed, was clean.
- **The steps are the page's.** Where the page gives its own steps, those are the panels; where it
  names no fill step, no panel fills anything and `fill` has nothing to mark.
- **The product is the set's one variant in every panel.** One render switched colourway between
  its sequence and the rest of the set.
- **Place:** image 4 or 5, usually the second mechanism-class tile.

Slots an LP2 prompt adds to the SKELETON above:
```
[TITLE]  the ease, 2–5 words, outside the panels.   -> LP2 LAW
```

## TRIGGER
use_when: >
  The product has more than one operation step, or buyers may assume it is
  complicated. Image 4-5 in the gallery. Answers the question "will I manage to
  use this".

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 03-use-sequence v1.9
REGISTER: a real home, close range, available light.          -> PARTS/register

[PRODUCT REFERENCE] the attached photo is the exact reference, in every panel.
[LAYOUT] three panels stacked, thin white gutters.            -> PARTS/layout
[CONTINUITY] one pair of hands, one place, one light.         -> PARTS/continuity
[PANELS] prepare, then use, then result.                      -> PARTS/panels
[ENVIRONMENT] one ordinary room, named once.                  -> PARTS/environment
[MARKS] made of real substance, never drawn.                  -> MARKS
  fill, all three panels     trace, the USE panel
  emission, the USE panel    residue, the RESULT panel
```

## PARTS

**`register`** — a real home photographed plainly at close range, on available light, with
ordinary surfaces and nothing propped or colour-matched. Not a diagram and not a manual.

**The look is not fixed, and fixing it is how this type produced slop.** Sixteen renders came
back as one beige room in one soft light because `register` prescribed a warm neutral palette
and every prompt repeated it: in a single four-prompt set, "warm neutral palette" appears 4
times and "soft daylight" 8. The register fixes the KIND of photograph. The home, the palette,
the light and the person are chosen per prompt, and **two prompts in one set may not share
them** — a set that comes back as one look is a fault in the set, not in the model.

**`layout`** — three photographs filling the whole image, thin white gutters, no outer border,
and no panel other than those three. Their ARRANGEMENT follows the slot's ratio (G15): stacked
one above another on a tall or wide ratio, and **at 1:1 one photograph across the top with two
side by side below it** — PREPARE in the wide one, USE and RESULT beneath, left to right. The
order is unchanged by the pack.

**Never describe the frame's shape or ratio**: the owner sets the ratio at render time, and a
prompt that reasons about frame geometry leaves the model space to reconcile, and it fills that
space with extra small panels. **That bans naming the FRAME, not naming the ARRANGEMENT** — the
clause above already names one, and "one photograph above two side by side" is the same kind of
statement. No "square", no "1:1", no "tall image" ever enters a prompt.

**No numbers, no step markers, no text of any kind, and nothing that points from one panel to
another.** The order is read from the actions themselves, which is this type's entire discipline.

**`continuity`** — the make-or-break. The SAME hands in every panel: same skin tone, same
nails, same wrists, same sleeves. The same subject or surface throughout. **One palette and one
light direction held across all three panels — whichever palette and light this image was
given.** Continuity governs sameness INSIDE one image; `register` governs difference BETWEEN
images, and confusing the two is what produced sixteen identical rooms. Get continuity wrong
and the image reads as three stock photos rather than one sequence.

Camera distance and framing may shift naturally between panels — the `camera_lock: handheld`
axis is definitional here, because pixel-locked framing would read as renders rather than as
someone's hands.

**`panels`** — one action per panel, never two. The original exemplar packed two actions into
its first panel and lost a beat.

- **PREPARE**: the single setup action, hands in frame, and the readiness signal visible — an
  indicator light, an opened part, a loaded state.
- **USE**: the core action in progress, mid-motion.
- **RESULT**: the action finishing, plus a second hand or gesture expressing the outcome, and
  **no new mechanics** — this panel closes on the relationship, not on more machinery, which is
  what separates the type from a dry manual.

**The closing panel is lit exactly like the two above it.** It carried "warmer light than the
previous panels" from 1.0 until 1.8 and shipped that way 15 times across four sets, in flat
contradiction of `continuity` on the same page: one light direction and one palette across all
three. The owner caught it on the images — the last panel always came back a different colour,
which is three photographs of three moments, and this type has exactly one moment. What
resolves the closing panel is `residue`, not a grade.

The product sits near the centre of every panel and is never cropped out.

**These three names are the type file's vocabulary and never reach the model.** A prompt that
carried `PANEL 1, PREPARE:` as a heading had PREPARE, USE and RESULT printed in white capitals
into the frame — adapter Rule 1b, now measured on a third type. Describe each panel in prose:
the top panel, the middle panel, the bottom panel. The whole-image headings shipped in that
same prompt and were not drawn, so what leaks is a name attached to a REGION of the frame, not
capitals as such.

**If the closing action removes a part from the product, the panel must describe the product
without that part.** Asked for a catch jar poured into a filter and told nothing about the
grinder it came off, the model duplicated the jar in one run and dropped the grinder in the
other. 2 of 2. Setting the WHOLE product down needs no such wording — proven on the steamer and
on both wine-opener runs.

**Any part of the product whose state visibly changes is named in every panel, including the
one where it is still empty** — that is `fill` in MARKS. `continuity` declares hands, place and
light identical across the three panels and the model extends that to the product's own state:
a cork named only in the middle panel was already inside the opener's window in the first, so
the first two panels showed one state and the middle beat was empty. 2 of 2.

**`environment`** — one ordinary domestic setting with one or two incidental details, named
once and identical in all three panels.

## MARKS

**Every mark in this type is made of something physically in the scene, and nothing is ever
drawn over the photograph.** That is measured, not a preference: a mark made of real substance
has rendered correctly 7 times out of 7, and a drawn mark at the scale of a seam rendered
usably 0 times out of 8 before `fit` was cut at 1.7. A11 in `registry/argument-faults.md` is
not contradicted — drawn geometry does read in a photographic register at the scale of rings
and glows sized to the whole frame, and that is not a scale this type has any use for.

**No mark carries the reading order**, and nothing points from one panel to another. A step
number or a linking arrow would make this the instruction manual its PURPOSE exists to avoid.

The four entries are the four things a plain photograph of someone using a product does not say
on its own, and between them they carry the type's whole argument.

| name | made of | panel | evidence |
|---|---|---|---|
| `fill` | the level of a real substance inside a transparent part of the product | all three | ~6 correct, no failure attributable to it |
| `emission` | whatever the product visibly puts out — steam, spray, foam, a jet, a falling solid | USE | 7/7 |
| `trace` | the acted-on surface itself: done behind the head, not-yet-done ahead of it | USE | 2, both correct in frames that failed on layout |
| `residue` | what the product removed or produced, collected and visible | RESULT | 2 |

**`fill` is the through-line, and it is what makes three photographs one event.** A tank going
down, a jar filling with grounds, a cork rising into a window, a chamber greying with lint. It
is named in every panel including the one where it is still empty, because `continuity` tells
the model everything is identical across panels and it applies that to the product's own state
unless the state is named each time. It is the only mark that appears in all three panels, and
it is the one to reach for first: it needs no substance leaving the product and no mess left
behind, so it is available on almost every product.

**`emission` exists only if the product genuinely emits** (G8). Never invent one so a panel
looks active — G8's subject is exactly not faking an effect so a photograph looks like it is
working, and a photographic register is where that is easiest and least forgivable. It is a
real thing in the room, lit to be visible, in its own real colour.

**`trace` is A8 applied to this type.** A change of state needs a boundary rather than two
states side by side, so the product sits ON the boundary of one continuous surface: cleared
carpet behind the head and grit ahead of it, wet floor behind the mop and dry ahead, stitched
hem behind the foot and torn ahead. It costs nothing to render because it is the surface
itself, and it is the cheapest proof in the library that the product does something.

**`residue` is how the closing panel resolves.** Lint tipped into a bin, scale rinsing off a
filter, grounds sitting in the paper, the open tin. It replaces the warmer light that used to
close these images and that contradicted `continuity` for eight versions: the last panel is
lit like the others and earns its ending by showing what came out. It is the only mark that may
appear after the action has finished.

**Marks are optional and a bare sequence is not a defect.** The clearest render this type has
produced carried none: three panels, one kettle, no mark of any kind. A mark is added when the
action alone leaves the argument short, never to fill the library.

The type is `exempt_from: [G3, G4]`: no signal colours, no correct-versus-wrong grading. There
is no wrong state here at all — nobody is doing it badly, because the argument is "this is
easy", not "this is better".

## SLOT CONSTRAINTS
- **The prompt budget is this type's hardest constraint, and length is what breaks the layout.**
  Measured across four sets into the same renderer: 1533 characters average and the stack held
  4 of 6; 2054 and it held 1 of 8; 2296, 1 of 8; 2368, 1 of 4. The last set rendered into
  1200x896, the identical frame the first set used, so the frame is not the variable — the
  wording is. Every clause added to fix a content fault was paid for out of the layout. **Keep a
  rendered prompt under about 1500 characters**, and when a new clause is earned, find its cost
  somewhere else in the prompt rather than appending it.
- A clause earns its place only if a render has failed without it, and is removed only once a
  render has done without it and come back correct (ADR-013, ADR-015).
- One action per panel; the order readable without numbering.
- Continuity of hands before everything else.
- **Hands at close range are this type's highest model risk** — adapter Rule 5 names hands as
  the worst failure class in the library, and every panel here is hands. Expect retries.

## NEGATIVE
```
[G6] + step numbers, arrows carrying the reading order, arrows between panels,
badges, different hands between panels,
different subject between panels, two actions in one panel,
product off-center, product cropped out, instruction manual look,
technical diagram, cold clinical lighting, different location between panels,
inconsistent palette, staged perfection
```
Canonical and model-agnostic; the adapter transforms it and no avoid line ships (ADR-014).

## VARIANTS
### --labelled
```
[LAYOUT OVERRIDE] each panel carries ONE label of its own — a number, a step
  word, or a caption — in a bar or badge that touches the panel it belongs to
  and no other. Nothing else in the frame carries a word.       -> G16
[NEGATIVE OVERRIDE] the base list's `step numbers` line is lifted for this
  variant ONLY. Arrows carrying the reading order stay banned.
```

**This variant exists because the market builds it and the base type forbade it flatly.**
The base's whole discipline is that the order is read from the ACTIONS — no numbers, no step
markers, nothing pointing from one panel to the next — and that discipline is not weakened
here. What `--labelled` permits is a label that NAMES a panel; what stays banned is a mark
that CARRIES the reading order between panels. A numeral in a badge on panel two says "this
is two"; an arrow from panel one to panel two says "read this way", and only the second one
replaces the work the actions are supposed to do.

**Three distinct observations from three products, which is curate.md §3's bar:**
`sha256:bc8893e4941bca1d…` (a pet-food page delivering its sequence as separate single-panel
assets each with a numbered badge), `sha256:d9182fe5815f8dd3…` (a coffee page numbering three
panels Step 1 to Step 3 with a caption block under each), `sha256:11b15330dfa36c17…` (an
anti-snoring page captioning four panels in a 2x2 with no numbers at all). The third is why
the variant is called `--labelled` rather than `--numbered`: a caption breaks the same clause
a numeral does.

**Panel count moves with it.** The base is three panels; the 2x2 observation is four. Panel
count is a runtime parameter under SPEC §3.2 and does not change the argument, so four is
legal here — but at 1:1 G15 binds and four panels pack as a 2x2, which is what the observation
already does.

**Untested.** No render exists for this variant. Its first render is its founding evidence,
and the open question is whether a label per panel survives where the base type's own
prompts have never carried a word.

## KNOWN-FLAKY
Below the §6.2 bar, not promoted.

- **The stack reflows.** 2 of 6 renders on 2026-08-13 ignored three-panels-stacked — one came
  back a 2x2 grid of four with the USE beat drawn twice, one a tall left panel with two stacked
  at the right. 4 of 6 held. Untested hypothesis: all six frames arrived 1200x896 landscape
  whatever ratio was asked, and a three-high stack in a landscape frame gives very wide short
  panels that both alternative arrangements fit better.
- **The last panel opens onto new ground.** 1 of 6: a steamer RESULT stood the product on a
  side table that `environment` never named and no panel above it showed. Prompts now state
  that the named details are the whole of the room. One observation is not a rule.

## NOTES
**The corner sparkle is a generator watermark, not a render fault.** 1.3 recorded it here as an
unrequested mark on 2 of 6 renders. That was wrong. Stacking the bottom-right corner of 19
renders across two types, five products and three batches — content cancels, a fixed overlay
survives — leaves a clean 48x48 four-point star whose centre sits 100 px in from the right edge
and 100 px up from the bottom of a 1200x896 frame. A shuffled-offset control of the same 19
leaves nothing, and the bottom-left corner leaves nothing. Round numbers and a fixed position
across unrelated prompts make it an overlay stamped on the output. It is on every render this
library has, faint over light ground and obvious over dark. **No prompt clause can remove it and
none should try** — naming it would spend budget on a thing the model never drew. Whether the
adapter should carry this for all types is with the owner.

Distinction within step 3: `ghostbody` and `xray` explain WHY a product works, `spec-split`
argues what is better inside, and this type answers "can I operate it". A gallery rarely needs
more than two step-3 answers, and this one is usually the second.

## CHANGELOG
- 1.12 (2026-09-16): `LP2 LAW` added: the owner's gallery instruction for this type — a title outside the panels and nothing else, nothing drawn even on packaging, no frame around a panel, the page's own steps. `text_layer` declared. First LP2 edit; `copied_at_version` stays 1.11. ADR-094.
- 1.11 (2026-09-15): copied verbatim from `registry/types/03-use-sequence.md` at 1.11, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.
