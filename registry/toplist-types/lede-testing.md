---
id: lede-testing
version: "0.4"
status: active
replaced_by: null
products_in_frame: one
requires_product_photo: true
awareness: [solution-aware, product-aware]
copied_from: null
copied_at_version: null
blocked_by: null
exempt_from: []
---

# lede-testing

## PURPOSE
The work being done. Hands, an instrument and one unit under test on a working surface,
caught mid-measurement. It argues that somebody actually put these products through
something — the E-E-A-T signal of the format — and it argues it with apparatus rather
than with a number.

## TRIGGER
use_when: >
  The reader is choosing between options that look alike and the page's value is that it
  did the work. The product block carries a specification or raw_features rich enough
  that a measurable property is obvious — heat, draw, grip, flow, noise. Strongest where
  the category is crowded and the differences are invisible in a product photograph.
  Prefer lede-lineup where the argument is that the whole field was gathered rather than
  that one unit was measured.

## BOUNDARY
**Against `lede-inuse`** — the hands here belong to the REVIEWER, not the owner, and the
place is a bench or a working surface rather than a home. An instrument is in frame. Both
tests are checkable at a glance.

**Against `lede-lineup`** — one unit under test, not the field. The moment a second and
third unit stand beside it as candidates the frame is arguing coverage, not measurement.

**Against `lede-winner`** — a testing frame never says which one won.

## SKELETON
```
TYPE: lede-testing v0.4
REGISTER: editorial documentary photograph, one frame, no words in it.

[PRODUCT REFERENCE]  the attached photo is the exact reference.        -> G1
[UNIT]               one unit, in the position the measurement needs it.
[INSTRUMENT]         the measuring device, in contact with or aimed at the unit.
[HANDS]              a hand doing the work, cropped at the wrist or forearm.
[SURFACE]            a working surface — bench, worktop, test rig — with the tools of
                     the measurement and nothing decorative.
[LIGHT]              plain working light, even, no studio key and no rim.
[GROUND]             a real place: mid, quiet, unevenly lit.  -> PARTS/ground
```

**The instrument is the argument and it must be doing something.** An instrument lying
beside the unit is a prop; an instrument in contact with it, held, is evidence. This is
`argument-faults.md` A12 read forwards: the hand carrying the argument must be employed
by the measurement and must not also be presenting the product to the lens.

## PARTS

**`ground`** — a REAL place, and this type has the namespace's largest sample: **11
frames**, measured on its own corpus with nothing imported (ADR-073).

| | measured | against the designed grounds |
|---|---|---|
| texture | **7.1** | 0.8 – 2.9 |
| value median | **0.65** | 0.90 |
| saturation median | **0.13**, 2 of 11 above 0.25 | 0.49 |
| value spread across the ring | **0.67** | 0.15 – 0.33 |

- **Real detail**, not a sweep. Racking, a wall, a bench edge, other work going on.
- **Mid, not light.** A bench under working light is darker than a studio ground, and
  asking for a bright background here produces the studio this type is not.
- **Quiet.** The colour lives in the apparatus and the product; the room carries almost
  none. This is the one clause the corpus states most strongly.
- **Unevenly lit.** Light falls off across the frame. A prompt asking for even illumination
  across the background is asking for the wrong picture.

## NEGATIVE
```
[G6] + a legible number, a digital readout in focus, a gauge whose scale can be read,
a chart, a second product class, a competitor's product, a person's face,
a lab coat, a clipboard, any word, price or logo baked into the picture
```
**The number ban is the type's whole legality and it is not stylistic.** A readable
measurement in the frame is `argument-faults.md` A15 — a figure the picture cannot
substantiate — and it is the fault three proposals (`04-proof-stat`,
`04-proof-instrument`, `04-proof-interface`) are already blocked behind. This type exists
BECAUSE the argument survives without the number: the apparatus and the hands carry it.
The moment a reading is legible, this type has become one of those three and must wait
for the same decision.

**No lab coat, no clipboard.** They are the costume of a credential this page does not
have, and a credential is what G16 refuses at its `named expert` row. **Contradicted once
by the corpus** — observation 25 of batch 2026-09-09-B is a technician in a white coat at
a real bench — and left standing at 1 observation against a clause with none, for
curation to settle rather than this diff.

**This type carries no text, on its own evidence** (ADR-071 permits a layer where a type
earns one): **10 of 11** corpus observations carry no words, and the single exception is
a video thumbnail rather than a page lede.

## FOUNDING RENDER ROUND

**One render, 2026-09-09 — round 2 prompt 4, rendered at v0.3.** A cord and rope
tightening tool in a bench vice, an inline force gauge under load, a real workshop. Verdict
**`partial`**, self-assigned under ADR-011 on a render that was opened and looked at, with
the gauge cropped at 5× on the native file. Ledger: `eval/render-tests.jsonl`,
ts `2026-09-09`.

**The type's whole legality held.** NEGATIVE calls the number ban *"the type's whole
legality and it is not stylistic"*. Checked at 5×: the dial carries a needle and
unreadable ticks and **no figure anywhere**, so `argument-faults.md` A15 is not breached
and this type stays clear of the three proposals blocked behind it.

**What failed is the MECHANISM the prompt chose to guarantee that.** It asked for *"the
gauge's dial turned away from the lens"* and the dial faces the lens, 1 of 1. The outcome
survived on focus rather than on instruction, which is a weaker thing than it looks: the
next render at a shorter focal length or a cleaner dial would print a legible scale and the
type would fall into A15 without a single clause having changed. **The clause to lean on is
the one about the READING, not the one about the dial's direction** — recorded here rather
than patched, because 1 of 1 is below SPEC §6.2 and one render cannot tell an ignored
instruction from an unlucky one.

**Three failures, all at 1 of 1:**

| slot | observed |
|---|---|
| `[HANDS]` | **three hands** against the prompt's two, and one person wears a glove on one hand and not the other |
| `[INSTRUMENT]` | the dial faces the lens, against the instruction to turn it away |
| `[SURFACE]` | the marker pen on the bench carries an **invented brand wordmark**, against *"no word ... in the picture"* |

**The wordmark is a case ADR-075 does not cover.** That decision permits DEPICTING a real
brand from an attached reference and refuses INVENTING one, and it reasons about the
SUBJECT. Here the invented mark arrived on a **prop** — a pen nobody asked to be branded,
in a prompt that banned words outright. A brand can be fabricated onto anything in frame,
not only onto the product, and no clause in this namespace anticipates that.

**The ground is the clause with the largest sample and this render does not test it
cleanly.** Ring value 0.25 and saturation 0.44 against the clause's 0.65 and 0.13 — but the
ring samples the operator's blue sleeve on the left edge and the bench along the bottom, so
it measured the subject. That is the limit ADR-073 already states. By eye the workshop is
what the clause describes: real detail, racking and a doorway behind, and light that falls
off visibly across the frame.

**KNOWN-FLAKY** (2026-09-09, one render, no patch): a hand count above the number the
prompt names, and glove state inconsistent between one person's two hands.

## CHANGELOG
- 0.4 (2026-09-09): **FOUNDING RENDER ROUND** — one render, round 2 prompt 4 at 0.3,
  `partial`. The number ban HELD: checked at 5× on the native file, no figure is legible
  anywhere, so A15 is not breached. What failed is the mechanism chosen to guarantee it —
  the dial was told to face away and faces the lens, 1 of 1 — which means the outcome rests
  on focus rather than on instruction. An invented brand wordmark arrived on a PROP, a case
  ADR-075 reasons about only for the subject. Three failures recorded, none patched at
  1 of 1; hand count and glove state go to KNOWN-FLAKY.
- 0.3 (2026-09-09): `PARTS/ground` added, measured on this type's own 11 frames — the
  largest sample in the namespace — with nothing imported (ADR-073, owner instruction).
  Texture 7.1 against 0.8-2.9 for the designed grounds is what separates the two halves of
  the namespace; value 0.65, saturation 0.13, ring spread 0.67.
- 0.2 (2026-09-09): ADR-071 permits a text layer in this namespace; this type does not
  take one, on 10 of 11 corpus observations carrying no words. The lab-coat ban is marked
  as contradicted once by observation 25 and left standing for curation.
- 0.1 (2026-09-09): drafted. The only one of the owner's seven that is a genuinely new
  argument AND blocked by nothing — one product, one reference photo, no text, no rank,
  no competitor mark, no figure. ADR-069.
