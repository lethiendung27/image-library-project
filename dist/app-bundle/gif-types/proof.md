---
id: proof
kind: proof
group: result
rung: 2
version: "1.3"
status: active
channels: [landing-page, advertorial, paid-social]
duration_s: [2, 4]
beats: [2, 3]
---

# proof

## PURPOSE
Before and after, inside one unbroken frame. A lane of fabric goes from grey to clean, an
indicator goes red to blue, a reading climbs, a stack of bags collapses to a third of its
height. The viewer judges the change themselves because nothing was cut.

## TRIGGER
use_when: >
  The section's argument is physical evidence, and the evidence is a measurable change
  the product causes. Steps 3 and 4, comparison beats, any claim a skeptic would want to
  watch happen rather than be told about.
avoid_when: >
  The evidence is a set of states held side by side for inspection — a locked multi-panel
  census, three time points in one frame. The reader's eye does the travelling there, and
  motion replaces a comparison instead of making it.

## BOUNDARY
Against `mechanism` — effect, not cause.

Against `cause` — the product is present here, and its presence is what makes the change
attributable.

Against `relief` — measured against lived. A quantity the viewer can see change is
`proof`; a life running smoothly is `relief`.

**This type is the library's main rung-2 route (query/runbook.md Step 5d).** A `proof`
slot is normally routed to a locked multi-panel still, which correctly earns no motion.
The motion execution is a different staging of the same argument: one continuous frame,
one variable changing. Say so in `varies_on`.

## BRIEF
**Two sentences.** The first names the frame, states that it never cuts, and names what is
in it. The second names the single variable and the direction it moves, ending on a state
the viewer can check against the still.
## NEGATIVE
No text, digits, arrows or progress bars (G6) — a number burned into the frame is a claim
the picture no longer has to earn. No cut between the two states: a cut is an editorial
assertion, and this type exists to avoid making one. **No seamless reverse loop** — clean
returning to dirty argues the effect wears off; delivery holds the after-state or plays
once. No lighting, angle or distance change between states.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.3 (2026-08-20): the light leaves the brief, ADR-030. An unchanged light is still the
  type's law; it is enforced by the still the loop accompanies, not restated in the
  brief.
- 1.2 (2026-08-20): the brief becomes TWO SENTENCES, ADR-029. The light joins the first
  sentence because an unchanged light is part of what makes the proof a proof.
- 1.1 (2026-08-19): the brief becomes one prose paragraph and gains the setting,
  ADR-028. The viewer is asked to judge a change and has to trust the place it happened
  in.
- 1.0 (2026-08-19): founding entry, ADR-023. 0 of 13 `proof`/`comparison`/`spec` slots
  earned motion across the five routed sessions, every one refused on the same ground —
  "inspected, not watched" — which is a verdict about the locked multi-panel EXECUTION
  and not about the argument. Page 65's own copy carries the counter-example the sessions
  passed over: an indicator that turns red to blue as the head passes, which is a
  transition filed as a state. Hence rung 2 and the one-frame rule.
