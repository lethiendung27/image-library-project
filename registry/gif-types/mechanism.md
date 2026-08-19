---
id: mechanism
kind: mechanism
group: working
rung: 1
version: "1.0"
status: active
channels: [landing-page, advertorial, paid-social]
duration_s: [2, 4]
beats: [1, 2]
---

# mechanism

## PURPOSE
It earns its money because of what happens inside. The working part — impeller, blade,
plate, foam, current path — is magnified or cut open and shown doing the one thing the
product is sold on.

## TRIGGER
use_when: >
  The section explains why the product works, and the explanation is a movement: a
  rotor turning, air travelling a path, foam recovering, a sled running its carriage.
  G8 applies where the mechanism has a visible output.
avoid_when: >
  The claim is invisible in every register this library has — heat, smell, air quality,
  battery chemistry. A loop of a part that merely sits there asserts nothing. Also
  avoid where the section's argument is a shape holding still rather than a part moving.

## BOUNDARY
Against `use` — framing, not subject. No person is the subject here; where a hand
appears it only holds, never performs.

Against `proof` — cause against effect. The impeller turning is `mechanism`; the dust
leaving the mattress is `proof`. A loop that shows both is `proof`, because the viewer
judges the outcome, not the reason.

## BRIEF
`SHOT` names the magnification or the cutaway, and which part is in focus.
`ACTION` names the internal movement and its direction.
`RESULT` names what the movement produces at the part — the output, not the room.
`MATCH` names the register: a cutaway loop keeps the still's drawing convention.

## NEGATIVE
No text, digits, arrows or flow lines (G6) — a labelled diagram is a graphic, and this
library does not draw graphics into a loop. No person as subject. No exploded view
rotating: that reveals parts rather than moving one, and revealing does not earn motion.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.0 (2026-08-19): founding entry, ADR-023. 4 of 7 `mechanism`-role slots earned a
  positive gif verdict across the five routed sessions; the three that failed did so on
  the same ground, an invisible claim (thermal, portability, a shape that holds), which
  is why `avoid_when` names invisibility rather than the role.
