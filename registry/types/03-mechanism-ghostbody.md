---
id: 03-mechanism-ghostbody
step: 3
job: mechanism
device: ghostbody
version: "2.3"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
channels: [marketplace, landing-page, advertorial]
requires_product_photo: true
generation_mode: single-pass
variants: []
exempt_from: [G7]
pairs_with: [01-pain-split, 06-relief-hero]
never_with: []
---

# 03-mechanism-ghostbody

## PURPOSE
Explain WHY the product's shape works, via the mechanism inside the body. The anonymous
white mannequin has no identity, so every viewer projects themselves in — this type
sells to every segment, and it is deliberately cold.

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

## WORKED EXAMPLES
Two renders that happened, kept in full because that text is the only record of what actually
drew (SPEC §3.3). Both are the 2.0 two-panel structure; 2.1 added a length limit to `support`
and restored the ghost's negatives, so read them with that diff in mind.

### example: kneeling-ergonomic-chair — skeleton@2.0, run: pass
Empty failures list. The clearest image this type has produced and the proof of the two-panel
structure: a slumped spine on a plain stool with a flat red block at the lumbar base, against
an upright spine on the reference chair with a flat blue band drawn beside it. Reads at any
size and needs nothing from the viewer.
```
TYPE: 03-mechanism-ghostbody v2.0
REGISTER: 3D technical render on seamless white. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the kneeling
ergonomic chair. Preserve shape, proportions, material, finish and colour exactly.
It keeps its own reference colours and carries no mark of any kind.

PANELS: two equal panels side by side, divided by one thin vertical line. Both
show the SAME featureless matte white mannequin in the SAME pose from the SAME
angle: seated at a desk, seen from the side, facing left, forearms on the desk,
cut along the sagittal plane so the lower spine and pelvis are open to view. The
only differences between the panels are what the figure sits on and what its
pelvis and lower spine do.

LEFT: an ordinary flat stool. The pelvis is rolled backward and the lower spine
slumps into a long outward curve.
RIGHT: the reference kneeling chair, its sloped seat under the buttocks and its
lower pad under the shins. The pelvis is tipped forward and the lower spine stands
in its natural inward curve.

CUTAWAY: the lumbar spine and the pelvis, inside the body silhouette, in both
panels.

MARKS, four, nothing else in either panel is marked. Every one is a flat
unshaded hard-edged overlay laid on top of the render, never a tint or fill of the
anatomy:
- structure: the lumbar vertebrae and the pelvis in yellow off-white ivory, both
  panels.
- stress: LEFT panel only. A flat red shape over the base of the lumbar spine
  where the slump loads it.
- support: RIGHT panel only. A flat blue band drawn BESIDE the lumbar spine,
  running alongside its inward curve and following its line, clearly sitting on
  top of the render rather than inside the bone.
- verdict: one badge in the top corner of each panel - a red filled disc with a
  white X in the left, a green filled disc with a white check in the right. Same
  diameter, not rings.

PALETTE LOCK: achromatic white and grey except the marks.
```

### example: side-sleeper-pillow — skeleton@2.0, run: partial
Kept because it is where the pose finally held in both panels on the third attempt. Its two
faults are the ones 2.1 repairs: the blue band ran the whole thoracic spine without a length
limit, and the mannequin grew a face once the ghost's negatives were cut.
```
TYPE: 03-mechanism-ghostbody v2.0
REGISTER: 3D technical render on seamless white. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the orthopaedic
side-sleeper pillow. Preserve shape, proportions, material, finish and colour
exactly. It keeps its own reference colours and carries no mark of any kind.

PANELS: two equal panels side by side, divided by one thin vertical line. Both
show the SAME featureless matte white mannequin in the SAME pose from the SAME
angle: lying on its LEFT side on a flat mattress, seen from the front of the body,
head to the left, left shoulder underneath taking the weight, cut along the
coronal plane so the neck and shoulder interior are open to view. The only
differences between the panels are what is under the head and what the neck does.

LEFT: a thin flat pillow that gives the head nothing to rest on. The neck bends
sharply toward the shoulder it lies on and the ear drops close to that shoulder.
RIGHT: the reference pillow filling the space between the head and the mattress.
The neck runs straight in line with the spine of the upper back.

CUTAWAY: the cervical spine and the shoulder girdle, inside the body silhouette,
in both panels.

MARKS, four, nothing else in either panel is marked. Every one is a flat unshaded
hard-edged overlay laid on top of the render, never a tint or fill of the anatomy:
- structure: the cervical vertebrae, the collarbone and the shoulder blade in
  yellow off-white ivory, both panels.
- stress: LEFT panel only. A flat red shape at the bend in the neck.
- support: RIGHT panel only. A flat blue band drawn BESIDE the cervical spine,
  running alongside it in a straight line and following its line, clearly sitting
  on top of the render rather than inside the bone.
- verdict: one badge in the top corner of each panel - a red filled disc with a
  white X in the left, a green filled disc with a white check in the right. Same
  diameter, not rings.

PALETTE LOCK: achromatic white and grey except the marks.
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
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 2.3 (2026-08-21): **the cutaway had no bound, and depth is a claim.** Owner verdict on two
  scalp-LED comb renders. `structure`'s count read "as much as the cutaway shows" while
  `cutaway` declared no extent — each bounded by the other. Depth now derives from a closed
  layer list, the silhouette survives the cut, `section` and `window` are the two geometries,
  and `structure` gains soft tissue. ADR-038. · 7534756
- 2.2 (2026-08-13): type passed by the owner; file finalised with two rendered worked examples
  in full text per SPEC §3.3. Closing state: five live marks, `structure` `stress` `support`
  `verdict` proven and `heat` still unrendered; `dims` withdrawn at 1.6 on 0 of 3. `3e32167`
- 2.1 (2026-08-13): **two clauses restored; the budget rule corrected.** Evidence: 3 records at
  2.0 — 1 `pass`, 1 `partial`, 1 `fail`. The 2.0 structure works: the argument reads at any size
  and A11 is fixed at 3 of 3, every mark now a drawn overlay rather than anatomy. Two of the
  five clauses I cut as ceremony were not ceremony — `support`'s length limit and the ghost's
  four negatives — and the next render broke on both. They are back. The rule that let me cut
  them is corrected in ADR-015. `d982bb2`
- 2.0 (2026-08-13): **the comparison becomes the frame, and every mark becomes an overlay.**
  MAJOR bump: the layer structure changes from one main frame plus a corner inset to two equal
  panels. Owner-approved on two recommendations from a self-audit. Evidence: 3 records at 1.6,
  all `partial`, and 12 renders in total.
  The inset went from optional at 1.3 to required at 1.5 to the whole frame at 2.0, and each
  step was forced by a render. Once harm marks were banned from a single-state frame, the
  comparison was the only thing that could argue — and three renders then showed a beautiful
  anatomical study filling nine tenths of the frame and stating little, while two small corner
  panels stated everything. At mobile size the arguing part was the unreadable part.
  Every mark is now a flat, unshaded, hard-edged overlay. `support` drawn as a fill along bone
  came back three times out of three as coloured intervertebral discs — it had not failed to
  draw, it had failed to be a mark, which is fault A11 in `registry/argument-faults.md`.
  Prompt budget measured and written in: 19% of this type's prompts was ceremony no render had
  ever failed without, and the specific clauses are now named as never-again. `1d0b5be`
- 1.6 (2026-08-13): **the inset requirement is proved, and `dims` is withdrawn.** Evidence: 3
  records — 2 `pass` and 1 `partial`; the owner passed the set apart from the pillow.
  The isolation test landed: the same insole that argued nothing, with one inset added and
  nothing else changed, now makes a claim a viewer can read unaided. `support` also read
  correctly for the first time, on the top edge of the arch bones away from the product.
  `dims` is retired on 0 of 3, against a withdrawal condition set at 1.5 before the render that
  triggered it. Three attempts, three failures on count and placement; the letter and number ban
  worked, so it is retired for geometry and not for text.
  One fault from the owner: an inset panel whose pose is left to inherit from the main frame
  comes back illogical. Both panels are now the same body in the same pose, named inside the
  inset, differing only in the thing under argument — and that difference named against the
  structure, never the frame. `c922a37`
- 1.5 (2026-08-13): **the inset becomes required, and `dims` goes on notice.** Evidence: 3
  records, 2 partial and 1 fail. All three 1.4 fixes landed — no harm mark in a main frame, no
  signal colour on a product, `support` on the bone, `dims` free of letters — and the inset
  rendered as a real comparison, the first time this type's argument has read at all. The
  experiment settled the open question: an insole with no inset produced the best-looking render
  this type has made and argued nothing. `[XCHECK] optional` becomes `[INSET] REQUIRED`. Three
  faults written in: never name the slot in a prompt; `support` away from the bone-product
  boundary; `dims` at 0 of 2, tightened and on notice. `62febe7`
- 1.4 (2026-08-13): **three faults from the founding batch, all of them mine.** A harm mark in
  the main frame inverts the argument — red on a shoulder under a pillow reads as the pillow
  hurting the shoulder — so `stress` and `heat` are now `inset`-only and the main frame
  carries `structure` and `support` alone. A mark cannot carry a counterfactual: the shoe asked
  for red where a NARROW shoe would press, and no mark can say "would have". And no mark may be
  placed ON the product, whose own colours are not marks — left unstated, the model painted the
  pillow surface blue and then the whole shoe blue, applying G3's support colour to the thing
  being sold. `dims` gains a letter ban after its arrows returned labelled W and L. 2 records,
  2 fail. `1fa3cc0`
- 1.3 (2026-08-13): restructured into a call-map plus PARTS and MARKS (ADR-012). `PARTS`
  holds register, ghost, cutaway, product and xcheck; `MARKS` names the four palette-lock
  colours as marks for the first time, plus `dims` and `verdict`. The `RATIO:` line dropped
  per adapter Rule 4, which 6 of 6 renders showed a written ratio does nothing. Every mark
  carries **none** for evidence, because this type has never been rendered.
- 1.2 (2026-08-11): channels gain `landing-page` and `advertorial`, for parity with
  `03-mechanism-xray` — two mechanism types answering the same question on different channel
  sets was an accident, not a decision.
- 1.1 (2026-08-10): PRODUCT slot rewritten to G1 reference + G2 placement-only; `dims` gated
  to products with a clear 3D volume. seed: conversation.md.
- 1.0 (2026-08-10): initial as SQR-MECH-GHOSTBODY from the seat-cushion spine exemplar;
  exemplar faults noted (numberless dims as decoration, inset too small for mobile, extension
  lines crossing the product edge). seed: conversation.md.
