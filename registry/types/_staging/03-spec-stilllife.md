---
id: 03-spec-stilllife
step: 3
job: spec
device: stilllife
version: "0.1"
status: reserved
replaced_by: null
ratios: ["1:1", "3:4"]
channels: [landing-page]
requires_product_photo: false
generation_mode: single-pass
axes: {}
text_layer: [title, copy, badge]
variants: []
exempt_from: [G7]
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
---

# 03-spec-stilllife — STAGING DRAFT

Promotion status (2026-09-03): **8 observations across 3 distinct sources** — millbrook,
halden and standfast. Criterion 1 counts SOURCES rather than observations, and the gap
between those two numbers is the point: five of the eight came from the halden page in one
batch and moved the source count not at all. The founding three, one per ground:
`sha256:3765060283b2e736…` (rosemary on a plate), `sha256:505fcda9aaae2253…` (dried root,
knockout), `sha256:76ca0ccfb4de13e4…` (chaste tree, growing).

Criterion 3 MET — three renders on 2026-09-03, owner-verdict pending, proposed `partial`
(ADR-011). Criterion 2 not run. **The binding gap is two more distinct SOURCES.** Not
routable.

**The ledger proposed this as `03-spec-ingredient` and the id is changed here on purpose.**
A `device` is the signature visual MECHANISM (`split`, `grid`, `explode`, `macro`), not the
subject in frame. "Ingredient" names what is photographed; "still life" names how the
argument is made — one named material, alone, presented so it is recognisable. The rename
also earns its vocabulary entry twice over: the same batch proposed `02-cause-stilllife` for
an abundance food frame standing in for a dietary baseline, which is the same mechanism
carrying a different job. That is exactly how `split` already serves both `01-pain-split`
and `03-spec-split`.

**Three things must ship in the same diff as this file or the validator errors:**
`vocabulary.yaml` gains device `stilllife`; `scripts/validate.py` gains `text_layer` in
`OPTIONAL_KEYS`; `rules.md` gains G16 (see `G16-draft.md`). No axis is added — the owner's
call of 2026-09-03, and the repo's own `parameters` line already said so.

## PURPOSE
Argue composition and provenance with one named raw material, alone in frame, and say in
the frame what it is. The product is absent by design — this type answers "what is actually
in it", not "what does it do". The ground it sits on is a runtime VALUE, not identity — `vocabulary.yaml` already lists
`environment` under `parameters`, "things that are runtime parameters and must NEVER become
identity". An earlier draft made it an axis; that was wrong against the repo's own line and is
corrected here.

## TRIGGER
use_when: >
  The copy names a specific material by name — a botanical, a mineral, a fibre, a
  grain — and the buyer's doubt is whether it is really in there and in what state.
  The ingredient row of a product page, a benefit tile that has to carry one
  component, or a gallery tile between the mechanism image and the proof image.
  Name the ground in the prompt: a plain surface when the material is delivered
  prepared, a white knockout when the tile must composite onto any page colour, the
  place it grows when the claim is origin and the material is alive. Not for a
  material the product's own stated composition does not name, and not for a
  component of the product's construction, which is 03-spec-macro's frame.

## SKELETON
A call-map. Each arrow names an entry in PARTS or a global rule; the definition lives there
once and is expanded into the rendered prompt, never restated here.

```
TYPE: 03-spec-stilllife v0.1
REGISTER: commercial still life photograph. One frame, no panels, no insets.

[MATERIAL]  the named material, whole and recognisable.       -> PARTS/material
[SETTING]   what the material sits on or in. A runtime value.    -> PARTS/setting
[LIGHT]     one direction, hard enough to separate form.      -> PARTS/light
[SCALE]     one cue that says how big the material is.        -> PARTS/scale
[CAMERA]    overhead for laid material, level for growing.    -> PARTS/camera

[TEXT]      the claim, then its support.                      -> G16/title, G16/copy
[BADGE]     one short stamp. Optional, and untested.          -> G16/badge
```

## PARTS

**`material`** — name the material EXACTLY: the species, the cut, and the state it arrives
in. "Rosemary" is a hedge; "whole rosemary leaf, needles on the woody stem" is a subject.
An unnamed green herb is the failure mode this slot exists to prevent, and it is the same
failure `03-mechanism-ghostbody` measured when 4 of 6 renders drew the product as an unnamed
grey shape (argument fault A9).

**The material must be one the product genuinely contains, and the source is the brief, not
the model.** It comes from `product.specification` or `product.raw_features` and from
nowhere else — the same law those fields already carry for component names, and the same law
`colorways` carries when it says a fabricated colorway is a G2 violation. Under G16 the
material's name is also printed in the frame, so a wrong material is not a bad render, it is
a published claim in a file that outlives the page. If the brief does not name the material,
this type cannot run.

**`light`** — one direction, hard enough that each piece throws its own shadow and separates
from its neighbours. Flat even light turns a pile of material into a texture swatch, and a
swatch argues nothing: the claim is that this is a real thing of a real size, not a pattern.
PROPOSAL — no render behind it; the three observations all use directional light but three
market images are not this library's evidence.

**`scale`** — exactly one cue, because a material photographed alone has no size. Either the
material occupies a stated share of the frame width, or one ordinary object of known size
shares the frame. Never both, and never a branded object. On a white knockout the share is the
only option available, since there is no ground to read against.

**`camera`** — overhead and square for material that has been laid out; level and at the
material's own height for material that is growing. There is no third position. An oblique
angle on a laid-out material reads as a table setting and pulls the frame toward food
photography, which is a different argument.

## SLOT CONSTRAINTS
- **No product, no packaging, no capsule, no bottle, no hand, no person.** If the product is
  in frame this is the wrong type: a magnified region of the product itself is
  `03-spec-macro`, and a product with its components separated is `03-spec-explode`.
- **One material per frame.** Two named materials in one frame is a range argument and
  belongs in a lineup, not here.
- **G7 exemption, and it is narrow.** This type arranges material for the photograph, which
  G7's Placement and Reason tests forbid for a photographic scene layer. The exemption
  covers the ARRANGEMENT of the material and nothing else — every other G7 test still binds,
  and the growing ground takes no exemption at all because nothing in it is arranged. This is the
  "arranged product photography where the arrangement is the argument" class; it does not
  exist in `rules.md` yet and G7's scope note has to gain it in the same diff.
- **G11 is not engaged.** This type depicts no state — nothing here is the wrong way, the
  past, or the resolved state — so the saturation law has nothing to grade and the type
  takes no exemption from it.
- **G3 is not engaged.** The material carries its own real colour and no signal colour of
  any kind appears in the frame. State that in the prompt.
- **Never state the frame's shape or ratio in a prompt** (ADR-016, adapter Rule 4). The
  owner sets the ratio at the generation tool.
- **Text is only what G16 permits**, and on this type the title is normally the material's
  own name. Nothing else in the frame carries a letter or a number.

## NEGATIVE
```
[G6] + product, packaging, bottle, jar, capsule, tablet, hand, person,
bowl or dish unless the material's delivered form requires one, water droplets
added for gloss, a second unnamed material, a species other than the one named,
scattered petals or leaves added for decoration, a wooden board styled as a prop
```

## PARTS — setting (continued)

**`setting`** — one ground, named in the prompt, never an axis. Three grounds are behind this
type and each is one observation; they are values, not identities:

- **a plain surface** — one real material filling the frame behind the subject, nothing else on
  it, never patterned or branded. The text takes its contrast from it.
  Founding observation `sha256:3765060283b2e736…`; rendered 2026-09-03, text clean.
- **a white knockout** — no ground, no horizon, one faint contact shadow, cut to composite onto
  any page colour. Two consequences: the scale cue must be the frame-share form because there is
  nothing to judge size against, and **the text is DARK here**, which the prompt must say.
  Founding observation `sha256:505fcda9aaae2253…`; rendered 2026-09-03, the cleanest of the three.
- **the place it grows** — the material alive and rooted, with just enough of its surroundings
  to be believable. Natural light replaces the single hard key; the camera is level, not
  overhead; nothing is arranged, so the G7 exemption is not used.
  Founding observation `sha256:76ca0ccfb4de13e4…`; rendered 2026-09-03, and **this is the ground
  with no empty band** — see KNOWN-FLAKY.

## WORKED EXAMPLES
None. This type has never been rendered. Three founding prompts, one per ground, are
in `render-test-set.md`; the first that comes back `pass` or `partial` is rewritten here in
full text per SPEC §3.3, and the other stays diff-only.

## FOUNDING RENDER ROUND — 2026-09-03
Three prompts, one per ground, three materials, ratio 1:1, no reference photo attached.
Verdicts are the owner's to give (ADR-011); what is recorded here is what the frames show,
measured off the files.

| | plain surface, rosemary | white knockout, ginger | growing, chamomile |
|---|---|---|---|
| lines exact | 4/4 | 4/4 | 4/4 |
| both clusters present | yes | yes | yes |
| anything cut by a frame edge | no | no | no |
| G10 8% safe area | breached, 5.3% | breached, 6.5–7.4% | breached, 5.9–7.1% |
| text over the material | no | no | **yes** — the block sits over the field |
| alignment as asked | **no — centred** | yes | yes |
| material recognisable at named cut and state | yes | yes | yes |
| unrequested element | sparkle on badge | sparkle on badge | sparkle on badge |

**Text renders; placement does not, yet.** The two faults are different in kind. The margin
and the alignment are prompt problems with a written fix. The sparkle is the renderer's, and
the only fix is to vacate the corner.

## KNOWN-FLAKY
- **The bottom-right corner is unusable, and it is not this type's fault.** All three
  founding renders came back carrying a pale four-pointed sparkle nobody asked for, at the
  same frame coordinates — about 90% across, 90% down, roughly 5% of frame width —
  regardless of where the badge sat. On the white knockout it is invisible; on a dark badge
  it lands across the last letters. **The badge moves to the bottom LEFT and nothing this
  type asks for goes in the bottom-right.** Nine observations now stand behind this glyph,
  six of them already in `adapters/nano-banana.md`. See G16 Placement.
- **The plain-surface ground lost its text alignment, 1 of 1.** The prompt said "left aligned" and the
  rosemary render centred all three lines; the other two grounds obeyed. Rewritten as an
  observable — "every line begins at the same distance from the left edge of the picture" —
  and untested. Retest before this leaves staging.
- **The growing ground has no empty band and the round did not prove it can make one.** The
  chamomile render read, but the upper band happened to be out-of-focus foliage; the white
  blooms of the material itself sit immediately under and beside the block. The composition
  clause that reserves the upper third for foliage is new and unrendered.
- **G10's 8% is breached on every text render so far**, at 5.3–7.4% across seven inked edges.
  Nothing was cut, but the floor is not met. G16's over-ask clause is the fix and it has not
  been run.
- **The text layer was new to this type and to this library**, and all three ledger
  observations carry NO text — on the live pages the ingredient's name was page HTML beside
  the tile, not pixels in it. Moving it into the frame is the owner's Q1b decision. The round
  above is now that decision's founding evidence here.
- **`light` and `camera` are proposals**, written from three market images rather than from
  a render. Either may be wrong; a render that ignores one and still reads is grounds to cut
  it (ADR-015).
- **One observation per ground in the ledger, one render per ground in the test.** Three
  grounds at n=1 each is thin. A ground that keeps failing is a ground this type does not
  serve, not a fault in the type.

## NOTES
**What this type is NOT, so the boundary is on the record.** `03-spec-macro` magnifies a
region of the product and needs the product; this type has no product. `02-cause-stilllife`
(also proposed 2026-08-31) uses the same still-life mechanism to stand for a baseline the
buyer has lost — job `cause`, not `spec`. `06-relief-detail` (also proposed) isolates a body
zone rather than a material. If a frame shows several materials to argue breadth, that is a
lineup and this is not it.

## CHANGELOG
- 0.1 (2026-09-03): drafted from three distinct observations of the 2026-08-31-B batch —
  `sha256:3765060283b2e736…`, `sha256:505fcda9aaae2253…`, `sha256:76ca0ccfb4de13e4…` — which
  the batch itself read as one argument in three stagings: *"The three differ only in
  staging, which is a parameter, so this wants a presentation axis rather than three
  variants."* First type in the library to declare `text_layer`; first use of axis `ground`;
  first use of device `stilllife`. Id changed from the ledger's `03-spec-ingredient` for the
  reason given at the top of this file.
