---
id: 03-mechanism-ghostbody
step: 3
job: mechanism
device: ghostbody
version: "1.1"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
channels: [marketplace]
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
avoid_when: >
  Main image or scroll-stopper positions, or when the product does not act on a
  body structure. This type is cold — there is nobody to empathize with.

## SKELETON
```
TYPE: 03-mechanism-ghostbody v1.1
RATIO: [1:1 / 4:5]
REGISTER: 3D technical render. NOT photography. Seamless white infinity background.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. Do not redesign or add features.

[BASE: GHOST BODY]
Featureless matte white 3D mannequin, no face, no hair, no clothing, no skin tone,
shown [pose] in [interaction with product]. Body cross-sectioned at [cut plane]
to reveal interior. Soft even studio lighting, subtle grey ambient occlusion only.

[ANATOMY CUTAWAY]
[anatomical structure] rendered inside the body silhouette, not floating on top:
bone in off-white ivory, [stress element] highlighted in red.
Anatomically accurate, follows the exact contour of the product.

[PRODUCT]
The reference product, positioned [relation to body], seen from [angle],
the only object with a real material finish in the frame.
Sharp silhouette against white.
Its contour must visibly align with [anatomical structure].

[DIMS] (optional — enable only when the product has a clear 3D volume)
Thin black double-headed arrows measuring [dimension 1] and [dimension 2],
fine extension lines offset clear of the product outline. Drafting style.

[XCHECK] (optional, top-left corner)
Two small rounded-square panels side by side, flat 2D vector illustration,
light grey outline, white fill.
LEFT: [wrong state] with orange heat glow at [pressure point], motion squiggles.
Red circle with white X above.
RIGHT: [correct state] with blue support and yellow [structure] neutral.
Green circle with white check above.

PALETTE LOCK: achromatic white and grey everywhere. The ONLY colors permitted are
red [stress], orange [wrong pressure], blue [correct support], yellow [structure].
STYLE: clean medical-technical product render, e-commerce infographic, sharp, 4K.
NO text, no numbers, no logo, no watermark.
```

## SLOT CONSTRAINTS
- The product is the ONLY object with a real material finish — everything else is matte
  white/grey. This is the type's signature.
- [ANATOMY CUTAWAY] lives inside the silhouette, never floating on top.
- [DIMS] carries no numbers (text ban); without real specs it is decoration — enable
  only when the silhouette benefits from a drafting register.
- Strict palette lock is this type's G3: exactly four signal colors, nothing else.
- G7 exempt: technical render register — context integrity does not bind here.

## NEGATIVE
```
[G6] + human face, facial features, hair, skin tone, clothing,
photographic background, environment, furniture, shadows on floor,
extra colors, rainbow palette, anatomically wrong structures,
floating disconnected organs, dimension lines overlapping product edge,
cluttered inset, gore, realistic flesh, medical horror
```

## WORKED EXAMPLES
### example: mouth-tape — skeleton@1.0, run: untested
```
A 1:1 3D technical render on a seamless white infinity background. NOT photography.

BASE: A featureless matte white 3D mannequin head and upper chest in profile, no face
details, no hair, no clothing, no skin tone, lying back as if asleep. The head is
cross-sectioned along the sagittal plane to reveal the interior airway. Soft even
studio lighting, subtle grey ambient occlusion only.

ANATOMY CUTAWAY: The nasal cavity, soft palate, tongue and throat rendered inside the
head silhouette, not floating on top. Tissue in off-white ivory, the open nasal passage
highlighted with a smooth blue airflow ribbon travelling from the nostril down the
throat. The collapsed area behind the tongue marked in red.

PRODUCT: A single horizontal strip of mouth tape in soft matte beige placed across the
closed lips, the only object with a real material finish, slightly textured fabric
weave, gently rounded corners, sharp silhouette against white.

XCHECK: Two small rounded-square panels side by side in the top-left corner, flat 2D
vector illustration style, light grey outline, white fill. LEFT: an open mouth in
profile with orange heat glow at the throat and small motion squiggles for turbulent
air, red circle with white X above. RIGHT: a closed mouth with a blue airflow arrow
entering the nose and the yellow tongue resting in neutral position, green circle with
white check above.

PALETTE LOCK: achromatic white and grey everywhere. The ONLY colors permitted are red
for collapsed tissue, orange for wrong airflow, blue for correct airflow, yellow for
structure.
STYLE: clean medical-technical product render, e-commerce infographic, sharp, 4K.
NO text, no numbers, no logo, no watermark.
```
(Pre-dates the G2 rewrite — the PRODUCT paragraph still describes texture; when re-run,
replace with a G1 reference block + G2-clean placement.)
Predicted failures: the sagittal head cut sliding into gruesome medical render or into
flat textbook style (register mismatch with the product); [DIMS] was dropped here —
this test is what produced the "3D volume only" gate on DIMS.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Step 3 has three types answering three different questions — a gallery rarely needs
more than one or two: `ghostbody` = "why does this shape work", `03-spec-split` =
"what is better inside", `03-use-sequence` = "can I operate it".

## CHANGELOG
- 1.1 (2026-08-10): PRODUCT slot rewritten to G1 reference + G2 placement-only (matte
  texture and feature description removed); DIMS gated to products with clear 3D
  volume. seed: conversation.md.
- 1.0 (2026-08-10): initial as SQR-MECH-GHOSTBODY from the seat-cushion spine exemplar;
  exemplar faults noted (numberless dims as decoration, inset too small for mobile,
  extension lines crossing the product edge). seed: conversation.md.
