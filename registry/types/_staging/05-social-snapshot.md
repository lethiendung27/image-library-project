---
id: 05-social-snapshot
step: 5
job: social
device: snapshot
version: "0.1"
status: reserved
replaced_by: null
ratios: ["5:3", "4:3", "1:1"]
channels: [landing-page, advertorial]
requires_product_photo: true
generation_mode: single-pass
axes:
  register: [ugc]
variants: []
exempt_from: [G3, G4]
pairs_with: []
never_with: []
avoid_adjacent: [05-social-handoff]
---

# 05-social-snapshot — STAGING DRAFT

Promotion status (2026-08-11): **6 exemplars ledgered, ~2 distinct source families**
(one socket-tester reviewer set: obs `sha256:78bfce…`, `sha256:932b7a…`,
`sha256:09f8b2…`; one-to-two BP-monitor reviewers: `sha256:62e23f…`,
`sha256:3b860e…`, `sha256:f37e43…` — batch 2026-08-11-D). The §6.3 gate counts
distinct SOURCES: more reviewer sets across more verticals are still needed.
Also pending: router-confusion test, ≥1 rendered worked example, human review.
Not routable.

## PURPOSE
The customer-photo texture for review and social-proof blocks: a single raw
snapshot in the register of a real buyer's phone — imperfect, unstyled, each one
from a completely different home. Authenticity IS the argument; polish is the
failure mode. Commissioned directly by the library owner (2026-08-11): review
imagery is ONLY user-photos or UGC-style product shots, never polished, scenes
completely unrelated to each other.

## TRIGGER
use_when: >
  Review sections and social-proof blocks on landing pages and advertorials,
  when the trust gap is "does this actually exist and work in a normal home".
  Products bought on skepticism of glossy marketing. Use as SECTION imagery
  with the page's review copy, or beside aggregate ratings.
avoid_when: >
  Marketplace galleries (ugc register is barred there). NEVER pair a generated
  snapshot with a reviewer name, avatar, star row or verified badge, and never
  present one as an actual customer upload — that is a fabricated endorsement
  (FTC), the same line 05-social-card draws. When real customer photos exist,
  they always win over generated ones. Not for polished brand storytelling —
  that is 06-relief-hero's register.

## SKELETON
```
TYPE: 05-social-snapshot v0.1
RATIO: [5:3 / 4:3 / 1:1]
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. Do not redesign or add
features. The product may be partially obscured, angled or cropped the way
casual photography actually crops it.

[CONTENT MODE — choose ONE and say it]
in-use (default): the product mid-operation by its owner, person visible only
  incidentally ([a forearm / two fingers / nobody]); if the product has a
  display, the screen is lit and reading plausibly.
at-rest: the product simply sitting where it now lives ([counter / desk /
  shelf]), factory stickers or packaging remnants optionally still present,
  [ONE incidental owner object: a cable, a manual page, a mug] beside it.
kit-flatlay: the opened case or box contents as the owner keeps them —
  slightly disordered, real accessories only.

[SCENE]
[ONE ordinary domestic location], photographed as found: real clutter stays,
nothing tidied, nothing added for the camera. Ambient household light only
([mixed warm-dim / window daylight / kitchen overhead]) — never studio light.

[CAMERA TRUTH]
Framing slightly [tilted / off-center / too close]; focus adequate but casual;
mild noise or motion softness acceptable; exposure honest to the room. No
negative space discipline, no rule of thirds, no depth-of-field styling.

[DIEGETIC SCREENS — production law]
Any legible readout on the product is composited in post from a real capture;
model-drawn digits are gibberish. Illegible-at-size print (stickers, manuals)
may stay generated.

[AUTHENTICITY FENCE — hard, non-negotiable]
This image is page imagery, never a customer record: no reviewer name, no
avatar, no star row, no verified label anywhere near it in the layout. It must
also never imitate a SPECIFIC real customer's photo (structure, not pixels —
SPEC §6.4).

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
NO text overlays, no logo, no watermark, no badges, no borders.
```

## SLOT CONSTRAINTS
- SET DIVERSITY LAW (the owner's core requirement): when a page requests more
  than one snapshot, every image must differ COMPLETELY — different room class,
  surface, light temperature, camera distance and content mode where possible.
  A shared prop, palette or light across two snapshots reads as one shoot, and
  one shoot reads as fake. Generate as independent prompts, never as a batch
  with shared seeds or shared scene text.
- The incidental owner object is the authenticity anchor (extension plug, coiled
  cable, manual page) — exactly ONE per frame; two or more begins to read as
  set dressing.
- Person policy: incidental limbs only (a forearm in the cuff, fingers on a
  button). A face turns the image into a testimonial portrait — a different
  type's job (and a compliance risk here).
- G1 binds even in this register: casual framing may crop the product, but what
  is visible must match the reference exactly.
- Quality floor: authenticity tolerates softness, not illegibility — the product
  must remain identifiable at thumbnail size.

## NEGATIVE
```
[G6] + studio lighting, softbox reflections, seamless background, negative
space, color grading, professional composition, styled props, badges, borders,
star ratings, reviewer names, avatars, text overlays, product render look,
perfect symmetry, magazine polish, influencer aesthetic
```

## WORKED EXAMPLES
### example: socket-tester-in-use — skeleton@0.1, run: untested
```
A real customer's phone photo, 5:3 ratio. One frame, no layout.

Use the attached product photo as the exact reference for the socket tester.
Preserve shape, proportions, material, finish and color exactly. It is held
one-handed up to a wall outlet, slightly angled, cropped the way a casual
one-handed photo crops.

CONTENT MODE, in-use: the tester is mid-test at a living-room outlet, its
screen lit. The screen area is left softly lit for a post-composited readout.
An extension plug hangs from the neighbouring socket — the one incidental
owner object.

SCENE: an ordinary lived-in room photographed as found — aged wood paneling,
a slightly scuffed skirting board. Ambient mixed warm light from a floor lamp.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus
adequate, mild noise, honest exposure. No styling of any kind.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
NO text overlays, no logo, no watermark, no badges, no borders.
```
Predicted failures: (1) the model beautifying anyway — clean walls, styled
light (the negative list and avoid line must both fire); (2) screen digits
drawn as gibberish if the composite step is skipped; (3) product drift under
casual cropping (G1 check at review).

### example: bp-monitor-at-rest — skeleton@0.1, run: untested
```
A real customer's phone photo, 4:3 ratio. One frame, no layout.

Use the attached product photo as the exact reference for the arm-tunnel blood
pressure monitor. Preserve shape, proportions, material, finish and color
exactly. Its factory instruction sticker is still on the side panel.

CONTENT MODE, at-rest: the monitor sits on a kitchen counter where it now
lives, a folded paper manual beside it — the one incidental owner object.

SCENE: an ordinary kitchen counter photographed as found, crumbs and a faint
water mark included, another small appliance blurred at the frame edge.
Flat overhead kitchen light.

CAMERA TRUTH: slightly off-center, a little flat, focus adequate, honest
exposure, no styling.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
NO text overlays, no logo, no watermark, no badges, no borders.
```
Predicted failures: (1) the sticker rendered with legible invented micro-print
(must stay illegible-at-size); (2) the counter arriving implausibly clean.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Step-5 family map, extended: `persona-grid` = many faces, breadth;
`social-handoff` = a recommendation staged as an overheard moment;
`social-card` = a published review quoted over a lifestyle base;
`social-snapshot` = the customer's own camera, no words at all. Snapshot and
card are natural companions in a reviews block (photo texture + quote card),
but the fence differs: card cites a real review verbatim; snapshot must never
claim to BE customer material. Keep distance from handoff on one page
(avoid_adjacent) — two staged-social mechanisms side by side read as protest.
Boundary vs 06-relief-hero--ugc: relief-ugc still obeys hero laws (G8 output
primacy, pose branches, product legibility) and sells the relief state;
snapshot obeys almost nothing and sells existence — the register is shared,
the argument is not.

## CHANGELOG
- 0.1 (2026-08-11): staging draft from six real-UGC exemplars in one batch —
  socket tester in-use ×2 + kit (obs `sha256:78bfce…`, `sha256:932b7a…`,
  `sha256:09f8b2…`), BP monitor in-use + at-rest ×2 (obs `sha256:62e23f…`,
  `sha256:3b860e…`, `sha256:f37e43…`), batch 2026-08-11-D. New device value
  `snapshot` added to vocabulary in the same diff. Content-mode slot
  (in-use/at-rest/kit-flatlay) parameterized from the batch's 3/2/1 mode
  split. Set-diversity law and the no-attribution authenticity fence encoded
  at birth per the owner's directive (2026-08-11): review imagery is UGC-only,
  never polished, scenes completely different from one another.
