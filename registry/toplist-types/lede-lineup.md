---
id: lede-lineup
version: "0.3"
status: reserved
replaced_by: null
products_in_frame: many
requires_product_photo: true
awareness: [product-aware, most-aware]
copied_from: null
copied_at_version: null
blocked_by: reference-photo-limit
exempt_from: []
---

# lede-lineup

## PURPOSE
The whole field on one surface, in one light, photographed together. Its argument is
POSSESSION: these were all in the same room, so the shortlist was real. This is the
classic top-N hero — Wirecutter, Reviewed, Tom's Guide — and it is the format's strongest
"we tested them" signal short of showing the testing.

## TRIGGER
use_when: >
  The reader has decided to buy something in this category and is choosing between
  names. The input carries three or more distinct competing products. Strongest as the
  lede of a list whose value proposition is coverage — we looked at all of them — rather
  than depth on one.

## BOUNDARY
**Against `lede-collage`, and the distinction is the argument rather than the look.** A
lineup is PHOTOGRAPHED: one surface, one light, real shadows, and it claims the units
were together. A collage is ASSEMBLED: cut-outs on a flat ground, no shared light, and it
claims only that these are the five. Possession against enumeration.

They were nearly folded into one type with a `staging` axis, on the ground that both put
the field in one frame and differ in execution — which SPEC §3.2 would make an axis, not
a type. They are kept apart because **SPEC §3.1 makes the argument the identity**, and
"we had them all" is not "here are the five". **If a render round shows readers take the
same meaning from both, they merge and this file is the one that goes.**

**Against `lede-testing`** — the field, not one unit under measurement.

**Against `03-spec-lineup`** (image registry, staging) — that type shows several units of
ONE product, where exactly one thing differs, and its whole law is that single variable.
Here every unit is a different maker. Same picture shape, opposite argument.

## SKELETON
```
TYPE: lede-lineup v0.3
REGISTER: editorial product photograph, one frame, no words in it.

[PRODUCT REFERENCES]  one attached photo per unit, in rank order.       -> G1, and see BLOCK
[FIELD]               3-5 units on one surface, one light, real contact shadows.
[ARRANGEMENT]         no unit favoured by size, height, centring or light.
[SURFACE]             one real surface the category belongs to.
[LIGHT]               one soft source for the whole group; no unit separately lit.
[GROUND]              a studio seamless, near-white OR saturated. -> PARTS/ground
```

**No unit may be favoured, and the reason is borrowed rather than invented.**
`04-proof-lockedframe` states it four times and its own file says the judgement rule IS
the type: a frame that favours one panel by size or light has decided the comparison
before the reader does. A lineup that centres and up-lights the winner is a
`lede-winner` frame wearing five products.

## PARTS

**`ground`** — a studio SEAMLESS, and the measurement corrected what this file assumed.
Measured on this namespace's own corpus (ADR-073): **texture 2.9**, which puts this type
with the DESIGNED half and not with the photographed one. Four of its five stand on a
smooth sweep rather than in a place. **What is real is the SURFACE the units stand on and
the contact shadows it takes; the backdrop behind it is not.**

**Saturation is bimodal and the median hides it.** The five measure 0.03, 0.21, 0.26, 0.66
and 0.71 — three near-white sweeps and two strongly coloured, with nothing at all between
0.26 and 0.66. **So a prompt CHOOSES one and names it**, rather than aiming at a band:

- a **near-white** sweep, when the units are dark or strongly coloured themselves;
- a **strongly coloured** sweep, when the units are pale or metallic and would otherwise
  disappear. The coffee makers stand on a saturated yellow at 0.66; the alarm clocks on a
  terracotta at 0.71.

Value runs 0.68 to 0.96. **No gradient**: hue spread is small on every frame whose ring is
actually ground, and the one reading 175° is a garment flat-lay filling the frame edge to
edge, so that metric measured the subject rather than the backdrop.

## NEGATIVE
```
[G6] + a favoured unit, a rank number, a badge, a podium, a person,
any word, price or logo baked into the picture
```

**This type carries no text, and that is its own evidence rather than a namespace rule**
(ADR-071 permits a text layer where a type earns one). **5 of 5** corpus lineups carry no
words at all — the alarm clocks, the knitwear, the blenders, the coffee makers, the
desk flat-lay. A badge would also breach the no-favoured-unit law above by marking one.

## BLOCK — why this is `reserved`
**One decision, down from two** (ADR-075 removed the second on 2026-09-09).

**One reference photo per prompt.** `query/runbook.md:81` — *"one prompt, one generation
call, at most one reference photo attached"*. Three to five units need three to five. The
renderer accepts several; the limit is a number in this library's law, and its principle —
one generation call — is not threatened by attaching five.

**The brand-mark clause is gone.** `SPEC.md` §6.4's *"competitor brand marks never appear
in prompts"* does not bind this namespace, so a lineup of five named makers is no longer
refused on that ground. What replaces it is narrower: a real brand may be DEPICTED from an
attached reference, and no brand may be INVENTED — so while the photo limit stands and this
type attaches nothing, its units stay unbranded because a generated logo is a fabricated
brand, not because a rival's is forbidden.

Until the photo limit is answered this type is not routable and no prompt is written from
it.

## CHANGELOG
- 0.3 (2026-09-09): `PARTS/ground` added, measured on this namespace's own 32 frames with
  nothing imported (ADR-073, owner instruction). **The measurement moved this type across
  the line**: texture 2.9 puts it with the designed grounds, not the photographed ones, so
  the backdrop is a studio seamless and only the surface is real. Saturation is bimodal —
  0.03/0.21/0.26 against 0.66/0.71, nothing between — so the clause is a choice a prompt
  names rather than a band.
- 0.2 (2026-09-09): ADR-071 permits a text layer in this namespace; this type does not
  take one, on 5 of 5 corpus observations carrying no words and because a badge would
  favour a unit, which this type's own law forbids. Still `reserved` on the
  one-reference-photo limit.
- 0.1 (2026-09-09): drafted `reserved`. The most valuable genuinely new argument of the
  owner's seven and the one furthest from being renderable. ADR-069.
