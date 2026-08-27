---
id: 02-cause-scene
step: 2
job: cause
device: scene
version: "0.1"
status: reserved
replaced_by: null
ratios: ["5:3", "16:9", "4:5", "1:1"]
channels: [advertorial, paid-social, landing-page]
requires_product_photo: false
generation_mode: single-pass
variants: []
exempt_from: [G1, G3, G4]
pairs_with: [01-pain-scene, 02-cause-anatomy, 06-relief-hero]
never_with: []
---

# 02-cause-scene — STAGING DRAFT

Promotion status: **3/5 exemplars** (obs `sha256:30c956…` exposed wiring,
`sha256:4e8f23…` illegible fuse labels, `sha256:e2e21c…` scratched floor — 2 funnels,
3 culprit modes). Not routable. Still needs: 2 more exemplars, router-confusion test,
≥1 render-test `pass|partial`, human review.

## PURPOSE
Indict an object, system or method in the customer's life by photographing its real
condition or the damage it leaves. The documentary twin of `02-cause-anatomy`: where
anatomy DRAWS the invisible cause, this SHOWS the visible one. People are absent or
anonymous — the viewer must inspect the thing, not empathize with a person.

## TRIGGER
use_when: >
  The "look what the old way involves / costs" beat of an advertorial or
  landing page, before the product answer. Use when the culprit or its
  damage photographs well: dangerous state (exposed wiring), chaotic state
  (illegible labels), or inflicted damage (scratched floors). A
  person-subject would soften the indictment — this type keeps humans out
  of it.

## SKELETON
```
TYPE: 02-cause-scene v0.1
RATIO: [5:3 / 16:9 / 4:5 / 1:1]
REGISTER: documentary photograph. Single frame. NO graphic overlays,
no signal colors.

[PROTAGONIST: THE CULPRIT OR ITS CONSEQUENCE]
[the indicted object, or the damage it causes], owning the frame's attention:
[2-4 concrete condition details — exposed tangled wires, crossed-out labels,
scratch trails, worn or failing components]. The object's real condition IS
the argument: physical fact, never narration (G9 transposed to things).

[HUMANS: ABSENT OR ANONYMOUS]
Either no person at all, or a partial anonymous presence: a wary hand
entering frame, a cropped torso, workers with heads out of frame.
Never a face. A face turns the image into a story about a person;
this image is an exhibit about a thing.

[MOMENT RULE]
A moment that genuinely occurs: mid-repair, mid-move, mid-inspection.
Nothing arranged for the camera (G7 at full strength).

[ENVIRONMENT]
[the place this problem actually lives], lived-in and specific,
cluttered as found, with time and wear markers.

[LIGHT]
Found light only: [raking window light / a bare bulb / flat overcast].
Low-key or plain. Never staged-bright, never flattering.

[GRADE]
Desaturated documentary palette, or full black-and-white when texture
carries the argument. Fine grain, believable optics.
NO red highlights, no glows — the decay itself is the signal.

[FORBIDDEN]
No product. No overlays, arrows, badges, glows or split panels.
Diegetic text ON the object (labels, stamps, handwriting) is permitted
per the G6 scope note.

STYLE: editorial documentary photography, natural, unstaged.
NO overlay text, no logo, no watermark.
```

## SLOT CONSTRAINTS
- The boundary against `01-pain-scene` is the protagonist: a PERSON feeling something
  → pain-scene; a THING in a state → cause-scene. Never blend (a suffering face next
  to the culprit collapses both arguments).
- Three culprit modes observed so far — name one explicitly when filling:
  `dangerous-state` | `chaotic-state` | `inflicted-damage`.
- Full monochrome is a legitimate grade here (2 of 3 exemplars) — commit to it or to
  desaturated color; never half-way.

## NEGATIVE
```
[G6] + red glow, highlights, arrows, badges, split panel, visible faces,
posed people, staged arrangement, clean styled interior, studio lighting,
saturated colors, product placement, new undamaged objects presented as evidence
```

## WORKED EXAMPLES
### example: furniture-mover-scratched-floor — skeleton@0.1, run: untested
Product: none in frame · ratio 5:3 · mode: inflicted-damage
- PROTAGONIST — a dark hardwood living-room floor scored with long pale scratch trails from dragged furniture, gouges catching window light and running diagonally through the frame's centre; marks fresh, splintered at the edges, unmistakably recent
- HUMANS, ANONYMOUS — two movers carry a fabric sofa through the upper frame, heads cropped out by the framing, plain work clothes, no face visible anywhere
- MOMENT — an ordinary mid-move minute: boxes half-packed against the wall, one open with packing paper spilling out
- ENVIRONMENT — a lived-in family living room mid-relocation, window light raking low across the floor so every scratch throws a shadow
- LIGHT — natural window light only, low and directional, no fill, no styling
- GRADE — full black-and-white, fine grain, deep blacks, believable 35mm optics
Predicted failures: (1) the model adding a visible face on the movers —
faceless framing is an unusual ask; (2) scratch trails rendering as wood grain
instead of damage — the raking-light instruction is the mitigation.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Step-2 pairing logic: `02-cause-anatomy` draws the invisible mechanism of harm;
`02-cause-scene` documents the visible one. A page uses one or the other for a given
cause — both together argue the same point twice.

## CHANGELOG
- 0.1 (2026-08-10): staging draft from three exemplars across two funnels — obs
  `sha256:30c956…` (dangerous-state), `sha256:4e8f23…` (chaotic-state),
  `sha256:e2e21c…` (inflicted-damage). Job `cause` × device `scene` had no type;
  both values already existed in vocabulary.
