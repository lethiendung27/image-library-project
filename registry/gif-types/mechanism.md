---
id: mechanism
kind: mechanism
group: working
rung: 1
version: "1.2"
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
**Two sentences.** The first names the magnification or the cutaway, which part is in focus,
and the register it keeps. The second names the internal movement and its direction, ending
on what that movement produces AT THE PART — the output, not the room.

**Where a cutaway or a technical render has no room, say so rather than borrowing one.**
This is the type that found the fault: a page 73 brief closed on "same room and light as
still" over a see-through render standing on a plain slate ground, and there was no room to
match. The first sentence is where that goes wrong or goes right, so check it against the
still (G12, ADR-028).
## NEGATIVE
No text, digits, arrows or flow lines (G6) — a labelled diagram is a graphic, and this
library does not draw graphics into a loop. No person as subject. No exploded view
rotating: that reveals parts rather than moving one, and revealing does not earn motion.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.2 (2026-08-20): the brief becomes TWO SENTENCES, ADR-029, and the no-room clause
  moves onto the first of them, which is where the page 73 fault was written.
- 1.1 (2026-08-19): the brief becomes one prose paragraph, ADR-028, and this type
  carries the clause the change was found by: where a cutaway has no room, say so rather
  than closing on `same room and light as still`. Page 73 shipped exactly that over a
  see-through render on a plain slate ground.
- 1.0 (2026-08-19): founding entry, ADR-023. 4 of 7 `mechanism`-role slots earned a
  positive gif verdict across the five routed sessions; the three that failed did so on
  the same ground, an invisible claim (thermal, portability, a shape that holds), which
  is why `avoid_when` names invisibility rather than the role.
