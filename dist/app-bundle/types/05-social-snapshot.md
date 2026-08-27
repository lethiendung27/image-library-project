---
id: 05-social-snapshot
step: 5
job: social
device: snapshot
version: "1.2"
status: active
replaced_by: null
ratios: ["4:3", "1:1", "3:4"]
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

# 05-social-snapshot

## PURPOSE
The customer-photo texture for review and social-proof blocks: a single raw snapshot in the
register of a real buyer's phone — imperfect, unstyled, each one from a completely different
home. Authenticity IS the argument; polish is the failure mode.

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
  record: no reviewer name, no avatar, no star row, no verified label anywhere near it in the
  layout. It must never imitate a SPECIFIC real customer's photo (structure, not pixels, SPEC
  §6.4).
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

## WORKED EXAMPLES
The first is kept in FULL text because that text is the only record of what actually rendered —
the ledger stores verdicts, not prompts (SPEC §3.3). It predates 1.1 and carries two clauses that
are now removed law: a `RATIO:` line (adapter Rule 4) and a closing avoid sentence (ADR-014).
**It is a record, not a template. Current law is in PARTS; fill from there.**

### example: socket-tester-in-use — skeleton@1.0, run: pass
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

### example: bp-monitor-at-rest — skeleton@1.0, run: untested
Product: arm-tunnel blood pressure monitor · ratio 4:3 · mode: at-rest · axes: register=ugc
- MODE — the monitor sitting on a kitchen counter where it now lives, factory instruction sticker still on the side panel
- ANCHOR — a folded paper manual beside it
- SCENE — a kitchen counter photographed as found, crumbs and a faint water mark included, another small appliance blurred at the frame edge; flat overhead kitchen light
- CAMERA — slightly off-centre, a little flat, focus adequate, honest exposure, no styling
Predicted failures: (1) the sticker rendered with legible invented micro-print, which must stay
illegible at size; (2) the counter arriving implausibly clean.

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
- 1.2 (2026-08-14): **type passed by the owner; file finalised.** The pass rests on 2 of 2
  renders, both `pass` with empty failure lists, at 0.1 (socket tester) and 1.0 (clip-on reading
  light). **1.1's restructure is not itself render-tested**, but it added no law except the MARKS
  bar and otherwise only removed clauses ADR-014, ADR-016 and adapter Rule 4 had already retired
  registry-wide. The reading-light prompt text was never stored, so that render survives as a
  verdict and nothing else — the gap `WORKED EXAMPLES` exists to close. `a2307aa`
- 1.1 (2026-08-14): **restructured into a call-map plus PARTS** (ADR-012), with `mode`, `scene`,
  `anchor`, `camera` and `person` owning their definitions and the skeleton cut to the call-map
  alone. Fixed on contact: header read `v0.1` against a 1.0 file; `RATIO:` and the rendered avoid
  line both dropped; `ratios` corrected to ADR-016's set, `3:4` being the phone shape this
  register actually has; G6's screen law referenced, not restated. **MARKS barred permanently**:
  a drawn mark refutes this register rather than weakening it (A11). `3a09d03`
- 1.0 (2026-08-11): PROMOTED staging → active on all four SPEC §6.3 criteria — 12 exemplars
  across five source families and five verticals (batches 2026-08-11-D and -E), router-confusion
  PASS against a purpose-built `eval/golden/fixture-002` at 8/8 slots, the socket-tester worked
  example rendered `pass` on the owner's verdict, and the ADR-007 gate. Same diff: slot-rules
  social-proof cells, worked-example headers, fixture-002. `7e2d9bb`
- 0.1 (2026-08-11): staging draft from six real-UGC exemplars in one batch (2026-08-11-D); device
  value `snapshot` added to vocabulary in the same diff. Content modes parameterised from the
  batch's 3/2/1 split. Set-diversity law and the no-attribution fence encoded at birth on the
  owner's directive: review imagery is UGC-only, never polished, scenes completely unrelated.
