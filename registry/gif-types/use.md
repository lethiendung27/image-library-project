---
id: use
kind: use
group: working
rung: 1
version: "1.0"
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
`SHOT` names the hand and the whole product, and the distance.
`ACTION` names the act in the order it happens, one clause per beat, at most four.
`RESULT` names the state the act leaves the product in — not its effect on the world.
`MATCH` names the register and light of the still it accompanies.

## NEGATIVE
No text, digits, arrows, cursors or callouts anywhere in frame (G6). No cut to another
place or time — a cut turns a demonstration into an edit. No speed ramp and no reverse:
an act that plays backwards is a claim the act undoes itself. No hand entering from
outside the frame at the loop seam.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.0 (2026-08-19): founding entry, ADR-023. Strongest motion carrier measured: 2 of 2
  `use`-role slots earned a positive gif verdict across the five routed sessions, and
  motion lands here on 3 of 3 market pages that carry any (FIXD "What is It?", NeckFan
  Step 1/2/3, Teant "simple operation"). Absorbs the `use-howto` / `use-interaction`
  split proposed and rejected in the same decision, and the act half of `spec-transform`.
