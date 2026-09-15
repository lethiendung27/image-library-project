---
id: 01-pain-split
step: 1
job: pain
device: split
version: "1.9"
status: active
replaced_by: null
channels: [marketplace, landing-page]
requires_product_photo: true
generation_mode: single-pass
variants: [object, mirror, oldway]
exempt_from: []
pairs_with: [06-relief-hero]
never_with: [01-pain-scene]
copied_from: 01-pain-split
copied_at_version: "1.9"
blocked_by: null
---

# 01-pain-split

## PURPOSE
Stop the scroll with pain in a 0.5-second glance. Structurally this is a **before and
after**: the same situation wrong on the left, resolved on the right, judged by badges.
Image 2 on Amazon, ad thumbnails, tiles in a landing-page grid.

**Copied verbatim from `registry/types/01-pain-split.md` at version 1.9** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## TRIGGER
use_when: >
  Need to stop the scroll with pain, or occupy one tile in a gallery/grid where
  the viewer glances for half a second. Use when the wrong state is visible to
  the naked eye. Use --object when the product is the obvious answer (small
  frames, thumbnails); use --mirror when the problem is a body state and the
  change must be shown on the person.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 01-pain-split v1.8 [--object | --mirror | --oldway]

[LAYOUT] two panels, hard vertical 50/50, both running to the frame edge.
                                                              -> PARTS/layout
[PRODUCT REFERENCE] attached photo is the exact reference.
[BEFORE] left panel: the wrong state, desaturated.            -> PARTS/before
[AFTER] right panel: the SAME setting resolved, in colour.    -> PARTS/after
[PRODUCT] in the AFTER panel only.                            -> PARTS/product
[MARKS] verdict always; hotspot + jag on the BEFORE panel.    -> MARKS

STYLE: e-commerce comparison tile, high contrast, sharp. Both panels share one
lighting register and one shooting style (G5).
```

## PARTS

**`layout`** — two panels, a hard vertical split at 50/50, each panel running all the way to
the frame edge. **No outer border and no drawn border line.** Assert it positively and say the
prohibition once: this model does not render a border as a margin, it draws a thin white
rectangle INSET from the edges, floating over the photograph and cutting through whatever is
behind it. 3 of 3 renders, one per variant. The split line itself is the argument's divider
and has rendered correctly every time.

**`before`** — left panel, desaturated grayscale: [age/gender] in [wardrobe], [the wrong
posture, state or struggle] on [surface], face showing [the discomfort, named by muscle].
Neutral cropped background, subject fills the frame.

**`after`** — right panel, full colour: **the SAME situation resolved.** Same room, same
surface, and the same person wherever a person is in frame.

**The AFTER keeps the room, and this is the type's most-lost rule.** The slots used to be
called THE PROBLEM and THE ANSWER, and "answer" is what invited a product photo — a product on
a clean ground answers the question without being an after of anything. One render proved it:
the right panel came back as an isolated shirt on a bare white wall against a lived-in left
panel, which breaks G5 and drops the comparison. G4 still binds — brighter and airier than the
left — but by light and calm, **never by deleting the room**.

**`product`** — ONE unit, in the AFTER panel only, in use, placed per G2: position, angle, scale in frame,
relation to other objects. Never described. It keeps its own reference colours and **carries
no signal colour at all** (`argument-faults.md` A5).

## MARKS

This type's own mark library. Every mark obeys G3 and carries a count.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `verdict` | flat solid disc with the glyph cut out of it, in a TOP corner, both the same diameter | red X left, green check right | exactly 2 | 4 renders · also in `02-cause-anatomy`, `03-mechanism-ghostbody`, `06-relief-hero` |
| `hotspot` | a soft red radial glow on one named structure | red only | one per structure, BEFORE panel only | 4 renders · a glow blooms and cannot be held to a boundary |
| `jag` | short red jagged strokes running ALONG one named structure | red only | 1 structure, BEFORE panel only | 4 renders |

**Name the SIDE as well as the structure.** Naming a structure binds the structure; on a
symmetric body it does not bind the side, and one render put every mark on both arms. Say
"the near wrist" and then say the marks appear on that arm only.

**Name structures, not counts.** "Exactly 3 hotspots" does not bind — a restated number never
has, in this library or in `02-cause-anatomy`. Name the three structures the glows sit on and
the count follows: wrist, forearm, shoulder. This also gives each glow something bounded to
sit on, which is the only thing that governs a mark's extent.

**All marks live in the BEFORE panel.** A mark in the AFTER panel sits in a frame where the
product is working, so it reads as harm the product CAUSES (`argument-faults.md` A1). The
badges are the single exception, because a verdict is not a harm.

**Badges: TOP corners only.** The eye reads top-down; a bottom badge arrives after the verdict
is already formed. Never add a VS badge on top of the X/check pair — one binary argument, one
pair of markers. Source exemplars used VS badges and emoji; market habits, deliberately not
imported.

## SLOT CONSTRAINTS
- **The wrong state must be visible to the naked eye.** This type argues in half a second; a
  problem that needs explaining belongs in `02-cause-anatomy` or `03-mechanism-*`.
- **A comparison must be of a switchable state** (`argument-faults.md` A6): take the product
  away and the wrong state must come back. If the harm persists it is accumulated damage, and
  the AFTER panel claims a repair the product cannot perform.
- Both panels share ONE register (G5): same lighting character, same shooting style. The
  register break is this type's recorded failure mode, always in the same direction — the
  right panel drifting to catalogue lighting the moment it holds a product and nothing else.
- **The prompt budget.** A clause earns its place only if a render has failed without it.
  Since ADR-014 no `Strictly avoid:` line is rendered at all.

## NEGATIVE
```
[G6] + cluttered background on right panel, dim right panel,
mismatched photo style between panels, visible test rigs or props,
red cues on right panel, distorted face, blood, injury,
inset white rectangle, drawn border line
```
Canonical and model-agnostic. Since ADR-014 it is **not rendered into the prompt at all**;
it stays here and in the query output's `avoid` field for a future model with a real negative
channel. `inset white rectangle` and `drawn border line` are kept in the list despite the
skeleton asserting the positive form, because a bordered comparison tile is a strong market
prior and it is this type's only 3/3 failure.

## VARIANTS
Diffs only. Each variant names the PARTS and MARKS it changes.

### --object (default)
The BEFORE is a person with the symptom; the AFTER is the same person and the same room with
the product doing its job. Baseline `before`, `after`, `product` and all three marks.
This is where the same-setting rule is easiest to lose, because the product is the most
interesting thing in the AFTER panel and the model will happily give it a studio.

### --mirror
The strongest comparison form — same person, same shot, only the state changes.
Diff vs base: `after` additionally holds the SAME camera angle, distance, wardrobe and
framing, and only posture, expression, presence of the product and colour grade may differ ·
`hotspot` and `jag` are DROPPED, posture and expression carry the problem · lighting setup and
time of day are identical, only the grade differs.
- **The route is an INVARIANTS BLOCK, single-pass** (ADR-067). Name face, hair, beard,
  clothes, camera height, distance and framing ONCE, BEFORE either panel is described. A
  single pass has been tried both ways: describing the person inside each panel returned two
  different people, and the invariants block returned one, 1 of 1 each way. This variant used
  to declare a `multi-pass` override on top of that finding; it is gone, and the worked
  example below — `wrist-brace-mirror`, `run: pass` — is a single-pass render where the
  identity held. The block is not a formality: without it this variant does not work.
- Negative additions: `different person between panels, different camera angle between panels,
  different wardrobe, different time of day, golden hour on one side only, VS badge, third
  badge, badges at bottom of frame`

### --oldway
The wrong state is the OLD SOLUTION IN USE — a person struggling with the legacy product class
— instead of a symptom on a body. Use when the buyer's real pain is the friction of what they
already own.
Diff vs base: `before` becomes a person struggling with a GENERIC, UNBRANDED legacy device,
ordinary and plausible, never broken, dirty or mocked (the fairness logic of
`04-proof-lockedframe`), with 2-3 friction details · `hotspot` and `jag` are optional, since
the friction is the evidence · the same-setting rule binds hardest here, because the BEFORE
panel is a room with a person struggling in it.
- Never imply the legacy device is a specific competitor.
- Negative additions: `brand logos on the legacy device, damaged or mocked legacy device,
  emoji, money props, price-claim imagery`

## KNOWN-FLAKY
- **The product rendered TWICE in the AFTER panel, 1 of 1, 2026-08-13.** Once in use as
  placed, and again as a second unit lying alone in the foreground under packshot light. Same
  instinct as the register split below — the model reaches for a catalogue shot the moment
  the right panel holds a product — but here it ADDS one instead of replacing the room.
  `PARTS/product` now says ONE unit, in use.
- **Identity breaks across panels when the person is described INSIDE each panel**, 1 of 1,
  2026-08-12. Hair dark and long on the left, lighter and shorter on the right — two people,
  so no comparison. That render is what the invariants block exists to prevent, and the
  worked example is the positive control at 1 of 1. Two renders, opposite results, one
  variable: where the identity is stated matters more than how many passes are used.
- **Register split between panels on `--oldway`, 1/3 renders, 2026-08-12 — addressed at
  v1.6, watch for recurrence.** The garment steamer run put a lived-in room on the left and
  what reads as a studio packshot on the right: an isolated shirt on a plain white wall, no
  room around it. G5 and the base NEGATIVE already barred it, so no law was missing; the
  model reached for catalogue lighting the moment the right panel held a product and
  nothing else. At one observation this sat below the §6.2 threshold and the skeleton was
  left alone. v1.6 then patched it anyway, for a different reason — the owner's naming
  decision required the AFTER panel to keep the setting — so this render is corroboration
  rather than the trigger. If a packshot right panel appears again under v1.6, the
  same-setting rule is not strong enough and the next step is to require the left panel's
  room to be named a second time inside the AFTER slot.

## CHANGELOG
- 1.9 (2026-09-15): copied verbatim from `registry/types/01-pain-split.md` at 1.9, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.
