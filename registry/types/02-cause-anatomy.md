---
id: 02-cause-anatomy
step: 2
job: cause
device: anatomy
version: "1.1"
status: active
replaced_by: null
ratios: ["5:3", "16:9", "1:1"]
channels: [landing-page, marketplace, advertorial]
requires_product_photo: false
generation_mode: single-pass
variants: []
exempt_from: [G1]
pairs_with: [01-pain-scene, 03-mechanism-ghostbody]
never_with: []
---

# 02-cause-anatomy

## PURPOSE
Indict a measurable cause in the customer's daily life (car seat, desk, mattress, tap
water) with a 2D medical illustration. A diagnostic image about the culprit — the
product does not appear.

## TRIGGER
use_when: >
  Need to blame a specific object in the customer's everyday life and show its
  measurable harm mechanism. Placed after the pain image and before the product
  mechanism image; fits the middle of an advertorial. The paired dashed
  reference lines are the argument — use only when a measurable landmark exists.
avoid_when: >
  The problem has no internal structure to draw, or the cause cannot be pinned
  to one concrete object. Never as a main image.

## SKELETON
```
TYPE: 02-cause-anatomy v1.0
RATIO: [5:3 / 16:9 / 1:1]
REGISTER: 2D medical illustration, airbrushed textbook style.
NOT photography. NOT 3D render.

[CANVAS]
One continuous pale blue clinical gradient background shared by both panels,
divided by a single thin vertical line, not a hard split.
Background motifs, all very low opacity: hexagon mesh, faint medical cross icons,
oversized ghosted [anatomical structure] as a watermark.
[optional: ghosted silhouette of [context object] behind the right panel]

[BODY TREATMENT, both panels]
[anatomical structure] drawn in warm ivory as the top layer,
the human body reduced to a translucent glowing outline behind it.
Same figure, same scale, same viewing angle in both panels.

[LEFT PANEL: WRONG]
Figure [wrong position] in/on [culprit object, drawn realistically].
[affected elements] highlighted in red. A red curved line tracing [wrong contour].
A red dashed reference line at [landmark], clearly TILTED.
A red double-headed curved arrow along [surface causing the problem].
Red circle with white X badge in the corner.

[RIGHT PANEL: CORRECT]
Same figure [correct position], no object or [supportive object].
[affected elements] highlighted in blue. A soft blue aura along [correct contour].
A blue dashed reference line at the same [landmark], clearly HORIZONTAL.
Green circle with white check badge in the corner.
Brighter and cleaner than the left panel.

[MEASUREMENT RULE]
The paired dashed reference lines are the core argument.
They must be at the identical anatomical landmark in both panels,
identical thickness and dash pattern, differing ONLY in angle.

PALETTE LOCK: pale blue and ivory throughout. The ONLY signal colors permitted are
red [wrong], blue [correct], green [confirmation badge].
STYLE: clinical medical illustration, e-commerce infographic, crisp linework, 4K.
NO text, no numbers, no logo, no watermark.
```

## SLOT CONSTRAINTS
- Wrong on the LEFT, correct on the RIGHT — locked across the whole library. The
  original exemplar inverted this and misread at first glance; never copy that.
- Both panels carry a badge (X left, check right) — one unlabeled panel leaves the
  verdict dangling.
- The dashed reference lines carry the entire argument. Without them the image says
  "sitting curves your back", which everyone already knows.
- The culprit object is drawn realistically but unbranded.
- Strictest G3 compliance in the library; G4 and G5 apply in full.

## NEGATIVE
```
[G6] + photographic elements, 3D render, photorealistic skin, human face,
facial features, gore, wet tissue, correct side on the left,
both dashed lines at the same angle, missing badge on either panel,
different figure scale between panels, extra colors, saturated background,
cluttered motifs, anatomically wrong structures
```

## WORKED EXAMPLES
### example: shower-filter-hair-strand — skeleton@1.0, run: untested
Product: none in frame (G1-exempt) · ratio 5:3
- CANVAS — one continuous pale blue clinical gradient shared by both panels, divided by a single thin vertical line; low-opacity motifs: hexagon mesh, faint water-drop icons, an oversized ghosted hair cross-section watermark, a ghosted showerhead silhouette behind the left panel
- SUBJECT TREATMENT (both panels) — magnified longitudinal cross-section of ONE hair strand in warm ivory as the top layer, cuticle scales clearly defined, surrounding water reduced to a translucent glowing outline behind; same strand, scale and viewing angle both sides
- LEFT PANEL, WRONG — strand under untreated water, hard-water minerals as small angular crystals; cuticle scales lifted, splayed and chipped, highlighted red; red curved line tracing the roughened surface; red dashed reference line, JAGGED AND UNEVEN; red double-headed arrow showing scale accumulating; red X badge in the corner
- RIGHT PANEL, CORRECT — same strand under filtered water, no crystals; scales flat, closed, overlapping, highlighted blue; soft blue aura along the smooth surface; blue dashed reference line at the same position, SMOOTH AND EVEN; green check badge; brighter and cleaner than the left
- MEASUREMENT RULE — the paired dashed lines are the argument: identical position, thickness and dash pattern, differing only in how evenly they run
- PALETTE LOCK — pale blue and ivory throughout; red = damage, blue = healthy, green = confirmation badge, nothing else
Predicted failure: the exemplar's dashed lines differ by ANGLE (a clean binary the
model draws reliably); this test substitutes EVENNESS, a fuzzy variable — the two lines
will likely render identical and the argument collapses. See NOTES.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Untested hypothesis (from the shower-filter stress test): the compared variable of the
dashed reference lines must be **angle, distance or length** — measurable binaries —
never texture or evenness. If the first renders confirm, promote this into
[MEASUREMENT RULE] with a minor bump.

Distinction from `03-mechanism-ghostbody`: 2D illustration vs 3D render; clinical blue
canvas vs infinite white; skeleton over body vs body over skeleton; the object in frame
is the **culprit**, not the product; the sentence is "this is what harms you", not
"this shape exists for a reason". The two may run in one gallery (02 then 03) but must
share one palette or they read as two sources.

## CHANGELOG
- 1.1 (2026-08-11): channels gain `advertorial`. Self-contradiction: use_when already
  says the type "fits the middle of an advertorial" while the frontmatter excluded
  that channel. Frontmatter corrected to match the trigger.
- 1.0 (2026-08-10): initial from the car-seat spine exemplar; exemplar faults encoded
  (correct-side-left inversion, missing X badge). seed: conversation.md.
