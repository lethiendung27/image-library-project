---
id: relief
kind: relief
group: result
rung: 1
version: "1.2"
status: active
channels: [landing-page, advertorial, paid-social]
duration_s: [2, 4]
beats: [1, 2]
---

# relief

## PURPOSE
Life after the purchase, shown at the exact place the problem used to interrupt it. A
stride that no longer stalls, a night that runs through, a work session that does not end
in standing up. The product is present and running, but it is not the subject.

## TRIGGER
use_when: >
  The section sells the after-state, and the after-state contains a CONTINUING ACTION
  that the problem previously stopped. Step 6, outcome beats, the closing scene.
avoid_when: >
  The after-state is a held moment — someone resting, a tidy room, a family watching a
  disc. A held moment is what a still holds best, and a loop over it argues nothing.

## BOUNDARY
Against `proof` — lived against measured. If a viewer could count or compare it, it is
`proof`.

**The tight rule, and it is the tightest in this set:** relief earns motion ONLY when the
motion IS the thing the problem used to block. Pleasant movement that merely happens to be
in an after-scene — curtains breathing, steam curling, a plant swaying — is ambient, and
ambient is switched off by default (query/runbook.md Step 5d, rung 3). This rule has never
been tested against a render; it is written to keep this type from becoming the bucket
every unearned loop falls into, and it is the first thing to revisit once orders come back.

## BRIEF
**Two sentences.** The first names the scene, the person, the product's place in it and the
light: this type's whole claim is that the motion happens at the exact place the problem used
to interrupt it, so the place is the argument and not the backdrop. The second names the
continuing action and, in the same clause, what used to stop it.
## NEGATIVE
No text or digits (G6). No product hero moment — the moment the camera favours the product
this stops being relief. No montage of unrelated happy scenes: one place, one action. No
face held in an expression of pleasure as the subject of the loop; G9 puts physical
evidence over expression.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.2 (2026-08-20): the brief becomes TWO SENTENCES, ADR-029. The place stays in the
  first sentence because for this type the place IS the argument.
- 1.1 (2026-08-19): the brief becomes one prose paragraph and gains the setting,
  ADR-028. This type's whole claim is that the motion happens where the problem used to
  interrupt it, so the place is the argument rather than the backdrop.
- 1.0 (2026-08-19): founding entry, ADR-023. 2 of 4 `relief`/`outcome` slots earned motion
  across the five routed sessions. Both that passed carry a continuing action ("a stride
  that no longer stalls", mist that keeps flowing); both that failed are held after-states.
  The rule in BOUNDARY is written from that split and from nothing else.
