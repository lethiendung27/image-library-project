---
id: 05-social-snapshot
step: 5
job: social
device: snapshot
version: "1.2"
status: active
replaced_by: null
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
copied_from: 05-social-snapshot
copied_at_version: "1.2"
blocked_by: null
---

# 05-social-snapshot

## PURPOSE
The customer-photo texture for review and social-proof blocks: a single raw snapshot in the
register of a real buyer's phone — imperfect, unstyled, each one from a completely different
home. Authenticity IS the argument; polish is the failure mode.

**Copied verbatim from `registry/types/05-social-snapshot.md` at version 1.2** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## TRIGGER
use_when: >
  Review sections and social-proof blocks on landing pages and advertorials,
  when the trust gap is "does this actually exist and work in a normal home".
  Products bought on skepticism of glossy marketing. Use as SECTION imagery
  with the page's review copy, or beside aggregate ratings.

## SKELETON
A call-map. Each arrow names an entry in PARTS; the definition lives there once and is
expanded into the rendered prompt (SPEC §3.3).

```
TYPE: 05-social-snapshot v1.2

[PRODUCT REFERENCE] attached photo is the exact reference.
[MODE] one of three, chosen before the prompt ships.  -> PARTS/mode
[SCENE] one ordinary home, photographed as found.     -> PARTS/scene
[ANCHOR] one incidental owner object.                 -> PARTS/anchor
[CAMERA] a phone in a hand, not a photographer.       -> PARTS/camera

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
```

## PARTS

**`mode`** — exactly one of three, resolved by the writer and stated plainly; the branch never
reaches the model (`query/runbook.md` Step 5).

- **in-use** (default) — the product mid-operation by its owner, the person visible only
  incidentally: a forearm, two fingers, or nobody.
- **at-rest** — the product simply sitting where it now lives, factory stickers or packaging
  remnants optionally still on it.
- **kit-flatlay** — the opened case or box contents as the owner keeps them, slightly disordered,
  real accessories only.

**`scene`** — one ordinary domestic location, photographed **as found**: real clutter stays,
nothing tidied, nothing added for the camera. Ambient household light only — mixed warm-dim,
window daylight, or a kitchen overhead — and never studio light. G7 does not bind this type the
way it binds a scene layer: the mess IS the argument, and a room that looks arranged has already
failed.

**`anchor`** — exactly ONE incidental owner object: an extension plug, a coiled cable, a manual
page, a mug. It is the authenticity anchor. **Two or more begins to read as set dressing**, which
is the failure this type exists to avoid.

**`camera`** — framing slightly tilted, off-centre or too close; focus adequate but casual; mild
noise or motion softness acceptable; exposure honest to the room. **No negative-space discipline,
no rule of thirds, no depth-of-field styling.** Where the other step-5 types spend their
composition budget on control, this one spends it on giving control away.

**`person`** — incidental limbs only: a forearm in a cuff, fingers on a button. **A face turns
the image into a testimonial portrait**, which is a different type's job and a compliance risk
here.

## SLOT CONSTRAINTS
- **SET DIVERSITY LAW.** When a page requests more than one snapshot, every image must differ
  COMPLETELY — different room class, surface, light temperature, camera distance, and content
  mode where possible. A shared prop, palette or light across two snapshots reads as one shoot,
  and one shoot reads as fake. Generate as independent prompts, never as a batch with shared
  seeds or shared scene text.
- **AUTHENTICITY FENCE, hard and non-negotiable.** This image is page imagery, never a customer
  record.
  - Nothing sits on the tile itself: no reviewer name, no avatar, no handle, no star row, no
    verified label, no post timestamp.
  - No lead over the wall claims the photos came from customers (ADR-088).
  - Named and badged reviews may share the block as TEXT; they never attach to the tile.
  - A harness that renders and meets attribution on the page flags the slot rather than
    refusing it (ADR-089). The frame still carries none of it.
  - It must never imitate a SPECIFIC real customer's photo (structure, not pixels, SPEC §6.4).
- **No MARKS section, and it can never have one.** A drawn arrow, ring or badge is by definition
  something a phone camera did not capture, so it does not merely weaken this register — it
  refutes it (A11: register decides). A snapshot that needs a mark is the wrong type for the slot.
- Legible readouts follow `G6`'s production law: composited in post from a real capture, never
  model-drawn. Illegible-at-size print — stickers, manual pages — may stay generated. Where the
  renderer cannot composite, choose a product with no display.
- `G1` binds even in this register: casual framing may crop the product, but what is visible must
  match the reference exactly.
- **Quality floor:** authenticity tolerates softness, not illegibility — the product must remain
  identifiable at thumbnail size.
- **The prompt budget, four parts.** A clause reaches a rendered prompt only if a render has
  failed without it, THAT product can fail that way, the model can act on it inside one
  generation, and it is stated once. Ceiling **1800 characters**. Since ADR-014 no
  `Strictly avoid:` line is rendered.

## NEGATIVE
```
[G6] + studio lighting, softbox reflections, seamless background, negative
space, color grading, professional composition, styled props, badges, borders,
star ratings, reviewer names, avatars, text overlays, product render look,
perfect symmetry, magazine polish, influencer aesthetic
```
Canonical and model-agnostic. Since ADR-014 it is not rendered into the prompt.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Step-5 family map: `persona-grid` = many faces, breadth; `social-handoff` = a recommendation
staged as an overheard moment; `social-card` = a published review quoted over a lifestyle base;
`social-snapshot` = the customer's own camera, no words at all. Snapshot and card are natural
companions in a reviews block, but the fence differs: card cites a real review verbatim, snapshot
must never claim to BE customer material. Keep distance from handoff on one page — two
staged-social mechanisms side by side read as protest. Against `06-relief-hero--ugc`: relief-ugc
still obeys hero laws and sells the relief state; snapshot obeys almost nothing and sells
existence. Shared register, different argument.

## CHANGELOG
- 1.2 (2026-09-15): copied verbatim from `registry/types/05-social-snapshot.md` at 1.2, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.
