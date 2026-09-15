---
id: 03-mechanism-ghostbody
step: 3
job: mechanism
device: ghostbody
version: "2.3"
status: active
replaced_by: null
channels: [marketplace, landing-page, advertorial]
requires_product_photo: true
generation_mode: single-pass
variants: []
exempt_from: [G7]
pairs_with: [01-pain-split, 06-relief-hero]
never_with: []
copied_from: 03-mechanism-ghostbody
copied_at_version: "2.3"
blocked_by: null
---

# 03-mechanism-ghostbody

## PURPOSE
Explain WHY the product's shape works, via the mechanism inside the body. The anonymous
white mannequin has no identity, so every viewer projects themselves in — this type
sells to every segment, and it is deliberately cold.

**Copied verbatim from `registry/types/03-mechanism-ghostbody.md` at version 2.3** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## TRIGGER
use_when: >
  Need to explain WHY the product's shape works, through a mechanism inside the
  body that cannot be filmed. Image 3-4 in the gallery, after pain and before or
  after relief. Works for every audience because the body is anonymous.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 03-mechanism-ghostbody v2.3
REGISTER: 3D technical render.                                -> PARTS/register

[PRODUCT REFERENCE] the attached photo is the exact reference.
[PANELS] two equal panels. LEFT wrong, RIGHT correct.         -> PARTS/panels
[GHOST] one pose, named once, identical in both panels.       -> PARTS/ghost
[CUTAWAY] the structure, its layer list, and which cut.       -> PARTS/cutaway
[PRODUCT] RIGHT panel only. Placement and angle.              -> PARTS/product
[MARKS] name each one used, with its count and its panel:     -> MARKS
  required: structure, verdict
  then stress on the LEFT, support on the RIGHT
  nothing in the frame is marked that is not named here

PALETTE LOCK: achromatic white and grey except the marks.
```

## PARTS

**`register`** — a clean medical-technical product render on a seamless white infinity
background, soft even studio lighting, subtle grey ambient occlusion only, no cast shadow on
a floor. Sharp, e-commerce infographic. **The product is the ONLY object in the frame with a
real material finish** — everything else is matte white or grey. That is this type's
signature and the thing a viewer reads first.

**`ghost`** — a featureless matte white mannequin, **no face, no hair, no clothing, no skin
tone** — restored at 2.1 after a defined face appeared in 2 of 3 renders without it: no face, no hair, no clothing, no skin
tone. Named pose, named interaction with the product, and the body opened at a named place to
reveal the interior — `section` or `window`, per `cutaway`. The anonymity is the argument, not a shortcut: nobody is being
empathised with, so nobody is excluded.

**`cutaway`** — the anatomical structure the product acts on, rendered INSIDE the body
silhouette and never floating on top of it. Its contour follows the product's contour,
because the alignment between the two is the whole claim.

**Depth is DERIVED, never chosen.** Name the layers as a closed list from the surface, ending
at the first layer BELOW the deepest structure the product reaches; nothing deeper is drawn.
Scalp LEDs: hair shaft, epidermis, dermis with the bulbs — stop; no skull.

**The silhouette survives the cut.** The outline stays unbroken and the cutaway is a WINDOW
within it, never a bite out of it.

**Two cut geometries, and the layer list picks one** — a parameter, not a variant (SPEC §3.2).
`section`: a plane through the body's volume, for a structure living inside it. `window`: a
shallow opening in the surface layers only, no deeper than the last named layer, outline
intact. A stack ending in the dermis cannot be drawn as a plane through a skull.

**What is revealed CONTINUES the body:** the follicles in the window are the roots of the hair
above them, same direction and density, bulbs deep.

**`product`** — the reference product at a named position and a named angle, G2-clean: place
it, never describe it. Its contour must visibly align with the structure named in `cutaway`.
Sharp silhouette against white.

**`panels`** — **two equal panels side by side, each a full 3D technical render**, divided by a
single thin vertical line. LEFT is the wrong state: the body without the product, or with an
ordinary one. RIGHT is the correct state with the reference product.

This replaced a corner inset at 2.0 and the evidence was unambiguous. From 1.5 the inset was
the only place a comparison could live, and three renders then showed the same shape: a
beautiful anatomical study filling nine tenths of the frame and stating little, while two small
panels in a corner stated everything. At mobile size the part that argued was the part that
could not be read. **The comparison is the argument, so the comparison is the frame.**

Both panels are the SAME body in the SAME pose from the SAME angle, cut the same way, differing
only in the product and in what the structure does — the `measure` discipline from
`02-cause-anatomy`: exactly one thing differs and everything else reads as identical. Naming
the pose ONCE, in `ghost`, and declaring it identical in both panels is what stops the halves
drifting; writing a main frame and an inset separately drifted twice, in opposite directions.

Distinction from `02-cause-anatomy`, now that both types carry two panels: that type is a 2D
illustration indicting a CULPRIT in the customer's life, and its sentence is "this is what harms
you". This one is a 3D technical render of the product's own mechanism, and its sentence is
"this shape exists for a reason".

## MARKS

This type's own mark library, called by name from the skeleton. Its palette lock IS G3 at its
strictest — exactly four signal colours and nothing else — so every mark here is defined by
the colour G3 already assigns it.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `structure` | the neutral anatomy the argument sits in — bone and cartilage, and the soft tissue a surface product acts in: dermis, follicle, nail bed | yellow / off-white ivory | every layer the closed list names, no more | 2 renders · drew cleanly, both skeletal |
| `stress` | a flat hard-edged red overlay on the loaded or deformed element — **LEFT panel only** | red | as many as are loaded, left only | 3 renders in an inset · reads there |
| `support` | a flat hard-edged blue band drawn BESIDE the structure the product carries, following its line and running ONLY the length the product reaches — never a fill of the anatomy — **RIGHT panel only** | blue | 1 per supported structure | 3 renders as an overlay · reads · 0 of 3 as a fill |
| `heat` | a flat hard-edged orange overlay, wrong pressure or wrong heat — LEFT panel only | orange | 1, left only | **none** |
| `dims` | ~~two black double-headed arrows outside the product silhouette~~ **WITHDRAWN at 1.6** | — | — | **0 of 3** · see KNOWN-FLAKY |
| `verdict` | circle badge in the TOP corner of each panel, a FILLED SOLID DISC with the glyph cut out of it | red X, green check | exactly 2, one per panel | 5 renders · also in `01-pain-split`, `02-cause-anatomy`, `06-relief-hero` |

**Every mark here is a FLAT, UNSHADED, HARD-EDGED OVERLAY.** This is the one form a shaded 3D
render never contains, and it is the difference between a mark and a piece of anatomy. Three
renders of `support` came back as blue along or between vertebrae and every one read as coloured
intervertebral discs — which is what a medical render puts there anyway. The mark had not failed
to draw; it had failed to be a mark. Fault A11 in `registry/argument-faults.md`, contributed the
same day from another type: a mark whose form the register could have produced stops reading as
one. Draw marks as clean vector shapes laid ON TOP of the render — flat colour, no shading, no
gradient, hard edges, obviously added. A band beside a bone, never a fill of it, and never a
tint of the anatomy itself.

**A harm mark never appears in the correct panel.** The main frame shows the product IN USE and
working, so everything in it reads as something the product is doing — and a red `stress` mark
there reads as harm the product CAUSES. Two founding renders proved it in one batch: red on
both shoulders under a pillow, red on the big-toe joint inside the shoe, and a viewer reads
"this hurts me". `stress` and `heat` belong in the LEFT panel only; the RIGHT panel carries
`structure` and `support` and nothing else.

**And a mark cannot carry a counterfactual.** The shoe prompt asked for red where a NARROW
shoe would press. No mark can say "would have"; it can only say "is". Marking a harm the
product prevents is the same error as marking something the product does not do.

**No mark may be placed ON the product, and the product's own colours are not marks.** The
product is the only object with a real material finish; the marks go on the BODY. Left
unstated, the two rules collided and the model resolved them by painting the product: a blue
pillow surface, then an entirely blue shoe — G3's correct-support colour applied to the thing
being sold. Say it in every prompt: the product keeps its own reference colours and carries no
signal colour at all.

**`dims` carries no letters either.** The arrows came back labelled `W` and `L`. G6 bans
letters, the prompt banned only numbers, and a dimension arrow attracts a label the way a slot
named ZONE A attracted a printed A. Ban both, or drop the mark.

**Every mark in this type is unproven.** It has never been rendered — zero records in
`eval/render-tests.jsonl`. The first render of each is its founding evidence and should be
logged as such.

**`support` sits ON the bone and away from the contact edge.** Where the mark hugs the boundary
between bone and product it reads as a coloured layer of the product — the insole render's blue
could be a gel insert. Draw it along the bone's own length, on the side away from the product.

**`dims` is WITHDRAWN at 1.6, on 0 of 3.** The withdrawal condition was set at 1.5 before the
render that triggered it, which is the only honest way to retire a mark. Three attempts, three
failures on the same two properties: the count came back as three or four arrows every time,
and at least one arrow lay across or inside the product silhouette every time. The final
attempt named the two arrows as separate items with their own endpoints and said both lay
entirely outside the shoe on the white background; it still returned three, with the topmost
drawn on the metatarsal bones inside the shoe.

What it cost to learn: an arrow crossing the product is worse than no arrow, because it reads
as damage to the thing being sold. What is NOT the reason: text. The letter and number ban
worked on both of the last two renders. The mark is retired for geometry, not for labels, and
if a future model draws reliable extension lines it can come back with evidence.

**`dims` carries no numbers and no letters**, because G6 bans text. Without real specs a dimension arrow is
decoration, so enable it only when the product has a clear 3D volume that a drafting register
actually clarifies. This gate came from the mouth-tape example, where dims were dropped.

**The palette lock is absolute.** Red is stress, orange is wrong pressure or heat, blue is
correct support, yellow is structure. Nothing else carries colour anywhere in the frame. A
fifth colour does not dilute the system, it breaks it — this is the strictest palette in the
library and the reason the type reads as technical rather than decorative.

**Borrowed from types that have been rendered**, so the same faults are not paid for twice:
`verdict` badges drift to outline rings unless the FILLED DISC is named (2 of 6 renders on
`02-cause-anatomy`); exact counts drift unless the mark names ONE bounded structure rather
than repeating a number; and a mark placed where nothing is claimed to be wrong reads as the
product causing harm (`02-symptom-rail` 1.7).

## SLOT CONSTRAINTS
- **The prompt budget** (ADR-013): a clause earns its place in a rendered prompt only if a
  render has failed without it. Measured at 2.0 across this type's own prompts, which had grown
  2056 → 2916 characters in four sets: 19% of a prompt was cut as ceremony,
  and **two of the five cuts were wrong** — corrected at 2.1 (see ADR-015). Gone for good, each
  shown unnecessary by a render that did without it: the register's studio description beyond
  the words "3D technical render"; "rendered INSIDE the silhouette and never floating on top of
  it"; "anatomically accurate"; and the closing enumeration of the palette lock. RESTORED,
  because removing them broke the next render: the ghost's four negatives, and `support`'s
  length limit.
- The product is the ONLY object with a real material finish.
- `cutaway` lives inside the silhouette, never floating on top.
- G7 exempt: technical-render register, so context integrity does not bind — the product need
  not be mounted to anything real.
- The canonical NEGATIVE below is model-agnostic and is never pasted into a prompt verbatim;
  the adapter transforms it (Rule 1), and most of its tokens qualify nouns a prompt requires.

## NEGATIVE
```
[G6] + human face, facial features, hair, skin tone, clothing,
photographic background, environment, furniture, shadows on floor,
extra colors, rainbow palette, anatomically wrong structures,
floating disconnected organs, dimension lines overlapping product edge,
cluttered inset, gore, realistic flesh, medical horror
```

## KNOWN-FLAKY
- **`dims`, WITHDRAWN at 1.6 on 0 of 3.** Three or four arrows where two were asked for, and at
  least one across or inside the product every time. Retired for geometry, not for text: the
  letter and number ban worked on the last two renders. It can return if a future model draws
  reliable extension lines.
- **Two panels rendered as a 2×2 grid, 1 render.** Third observation of the class across two
  types, so it is recorded in `adapters/nano-banana.md` Rule 4 as model behaviour rather than
  here.
- **A pose written twice drifts, 2 renders.** A pillow inset came back with an illogical lying
  posture when the pose was pinned only in the main frame; the next render fixed the inset and
  the MAIN frame then ignored the pose instead. At 2.0 the pose is named ONCE in `ghost` and
  declared identical in both panels, which is the only arrangement that has not drifted.
- **`support` as a fill reads as anatomy, 0 of 3.** Blue along or between vertebrae in a medical
  3D render is indistinguishable from coloured intervertebral discs. Fixed at 2.0 by making
  every mark a flat hard-edged overlay — see MARKS and fault A11.
- **Slot names printed into the image, 1 render** (`XCHECK` in capitals). Second observation of
  the class across the library after `02-symptom-rail`'s circled A, B and C; recorded in the
  adapter as Rule 1b, since it is model behaviour and not specific to this type.
- **A cutaway that removes the evidence, 1 render.** The shoe's upper was cut away exactly where
  the toe-box width was being claimed. Cut the body, not the part of the product the argument
  rests on.

## NOTES
Step 3 has three types answering three different questions, and a gallery rarely needs more
than one or two: `ghostbody` = "why does this shape work", `03-spec-split` = "what is better
inside", `03-use-sequence` = "can I operate it".

Distinction from `02-cause-anatomy`: that type is a 2D illustration indicting a CULPRIT in
the customer's life, and its sentence is "this is what harms you". This one is a 3D render of
the product's own mechanism, and its sentence is "this shape exists for a reason". They may
run in one gallery (02 then 03) but must share one palette or they read as two sources.

## CHANGELOG
- 2.3 (2026-09-15): copied verbatim from `registry/types/03-mechanism-ghostbody.md` at 2.3, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.
