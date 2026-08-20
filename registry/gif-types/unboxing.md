---
id: unboxing
kind: null
group: none
rung: 1
version: "1.4"
status: active
channels: [paid-social]
duration_s: [3, 6]
beats: [3, 6]
---

# unboxing

## PURPOSE
What you actually receive, item by item. The box opens and the contents come out in order
until the whole set is in view.

## TRIGGER
use_when: >
  An ad-channel brief for a product sold as a kit, a set or a multi-piece tool, where the
  buyer's open question is "is it complete". The reveal is the hook.
avoid_when: >
  Anywhere on a landing page. A single-piece product, where there is nothing to enumerate.

## BOUNDARY
**This type is not routable to a page slot, and its `channels` list is the enforcement.**
It enumerates rather than changes, so it fails the temporal test a page slot applies:
laying contents out reveals what exists, and revealing does not earn motion. It is kept
because the ad channel genuinely uses the reveal as an opening hook, which is a different
job from arguing a page section.

Against `use` — the moment a hand starts operating an item rather than presenting it, the
loop is `use`.

It carries `group: none` and `kind: null`: it counts toward no page floor and never
appears as a `gif.kind` in a routed prompt set.

## BRIEF
A shot description in plain words. Name the surface, the box and where the camera sits, then
the items in the order they come out, then the finished layout with everything in view.

**This is the only type that can exceed four beats**, at 3-6. It is also `kind: null` and
`paid-social` only, so it never reaches a routed page slot and never writes a page brief —
which is why the word band was set from the routable types and not from this one.
## NEGATIVE
No text, digits or price flashes (G6). No item entering from off-frame that was never in
the box. No cut that could hide an item being added.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.4 (2026-08-20): the brief becomes a plain-words shot description, ADR-031.
- 1.3 (2026-08-20): the light leaves the brief, ADR-030, and the beat ceiling is
  recorded here: this is the only type above four, and it never reaches a routed page
  slot.
- 1.2 (2026-08-20): the brief becomes TWO SENTENCES, ADR-029.
- 1.1 (2026-08-19): the brief becomes one prose paragraph and gains the setting,
  ADR-028. A kit reveal on a worktop and one on a studio sweep are two different
  arguments.
- 1.0 (2026-08-19): founding entry, ADR-023. Kept from the owner's original type list, but
  scoped to `paid-social` alone once the temporal test was applied to it: no unboxing beat
  exists in any of the 60 image slots across the five routed sessions, and none of the 8
  market pages scanned carries one. Channel restriction is the whole content of that finding.
