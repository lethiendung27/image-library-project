---
id: use
kind: use
group: working
rung: 1
version: "1.4"
status: active
channels: [landing-page, advertorial, paid-social]
duration_s: [2, 4]
beats: [1, 4]
---

# use

## PURPOSE
You can operate this without thinking about it. A hand acts on the product and the
product answers — grip, press, glide, pour, fold, attach. The loop sells the ease of
the act itself, not what the act leaves behind.

## TRIGGER
use_when: >
  The section's job is operation — a how-to beat, a feature that IS an action, or a
  tool whose whole claim is that the act is easy. The product and a hand are both in
  frame and the product is legible at normal viewing distance.
avoid_when: >
  The point can only be made by magnifying the working part (that is `mechanism`), or
  the section is arguing the change the act produced rather than the act (`proof`).
  Never where the product does not move and is not moved.

## BOUNDARY
Against `mechanism` — framing decides, not subject. Whole product plus a hand is
`use`; the working part magnified or cut open, with no person as subject, is
`mechanism`. The same electric scissors are `use` in the hand and `mechanism` at the
blade.

Against `proof` — `use` shows the act, `proof` shows the change the act caused. Where
one loop carries both, it is `proof`, and the act is that loop's opening beat.

Beat count is a PARAMETER, never a second type. One continuous act and a three-step
sequence make the same argument at different lengths; splitting them would put two
folders behind one message (ADR-023).

## BRIEF
A shot description in plain words. Name whose hands and what product and where, then the act
in the order it happens, then the state it leaves the PRODUCT in rather than its effect on
the world.

**The beats run in order inside the description, separated by commas with a final `then`,**
at most four. Measured at every beat count a routed slot can carry, the description stays
inside the 25-55 word band, so a multi-beat loop needs no second format (ADR-030).
## NEGATIVE
No text, digits, arrows, cursors or callouts anywhere in frame (G6). No cut to another
place or time — a cut turns a demonstration into an edit. No speed ramp and no reverse:
an act that plays backwards is a claim the act undoes itself. No hand entering from
outside the frame at the loop seam.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.4 (2026-08-20): the brief becomes a plain-words shot description, ADR-031; the
  multi-beat rule stays here and now reads against a description rather than a sentence
  count.
- 1.3 (2026-08-20): the light leaves the brief, ADR-030, and the multi-beat rule lands
  here because this is the type that carries them — up to four, in order, inside the
  second sentence.
- 1.2 (2026-08-20): the brief becomes TWO SENTENCES, ADR-029.
- 1.1 (2026-08-19): the brief becomes one prose paragraph and gains the setting,
  ADR-028. An act is only ordinary somewhere, and ordinariness is what this type sells.
- 1.0 (2026-08-19): founding entry, ADR-023. Strongest motion carrier measured: 2 of 2
  `use`-role slots earned a positive gif verdict across the five routed sessions, and
  motion lands here on 3 of 3 market pages that carry any (FIXD "What is It?", NeckFan
  Step 1/2/3, Teant "simple operation"). Absorbs the `use-howto` / `use-interaction`
  split proposed and rejected in the same decision, and the act half of `spec-transform`.
