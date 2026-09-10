---
id: 05-social-card
step: 5
job: social
device: card
version: "0.4"
status: reserved
replaced_by: null
ratios: ["16:9", "3:2", "1:1", "4:5"]
channels: [landing-page, paid-social, advertorial]
requires_product_photo: true
generation_mode: single-pass
axes:
  register: [commercial]
variants: [verbatim, illustrative]
exempt_from: [G3, G4, G6]
pairs_with: [06-relief-hero, 04-proof-lockedframe]
never_with: []
avoid_adjacent: [05-social-handoff, 05-persona-grid]
blocked_by: "Four more distinct sources - 1 of 5 today. Both card modes have a rendered pass, and no amount of render evidence substitutes for exemplars."
---

# 05-social-card — STAGING DRAFT

Promotion status (2026-08-11): **1/5 exemplars** (obs `sha256:9339ea…`, batch
2026-08-10-H). Criterion 3 comfortably MET — BOTH card modes now have a rendered
pass: `--illustrative` (rolling knife sharpener, 2026-08-10) and `--verbatim`
(L-shape cushion, 2026-08-11), the latter being the first evidence that the
attribution line renders cleanly at card scale. The binding gap is EXEMPLARS:
four more distinct sources are needed, and no amount of render evidence
substitutes for them. Also pending: router-confusion test, human review.
Not routable.

## PURPOSE
Testimonial-card social proof: a review card rendered IN the generated image over a
lifestyle scene (single-pass — this model renders short text reliably; user decision
2026-08-10). The straight-faced sibling of `05-social-handoff`. Two card modes:
`--verbatim` cites a real published review with attribution; `--illustrative` carries
an unattributed representative message. G6-exempt: the card's text is the deliverable.

## TRIGGER
use_when: >
  The social-proof beat on landing pages, paid-social or advertorials, when a
  direct customer quote earns more trust than staging — established products
  with genuine published reviews and real aggregate numbers. The card carries
  the argument; the scene only makes it human.

## SKELETON
```
TYPE: 05-social-card v0.4
RATIO: [16:9 / 3:2 / 1:1 / 4:5]
LAYERS: photographic hero base + review card, BOTH GENERATED in one pass.
REGISTER: bright lifestyle photography with one clean graphic card overlay.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. The product's own printed
label is diegetic and stays as the reference shows it.

[ZONE A: HERO BASE]
[age/gender] holding or just-used the reference product, caught in
[genuine candid delight: mid-laugh, warm smile], gaze OFF-camera,
at [everyday location], [1-2 props reinforcing the usage moment,
e.g. the prepared drink/result in the other hand].
Subject offset to ONE side. The opposite [35-45%] of the frame holds calm
negative space — plain wall, soft foliage, gentle falloff — where the card
sits. Bright, airy, warm grade.

[ZONE B: REVIEW CARD — generated]
A clean white rounded-corner card floating over the negative space,
occupying [28-38%] of the frame width, soft drop shadow, generous padding.
On the card, top to bottom:
  a row of five golden stars;
  the quote in friendly dark sans-serif, large and legible:
  "[EXACT QUOTE TEXT]"
  [--verbatim only: attribution line "[first name + initial] | [platform's
   verified label]", smaller and lighter.]
Render the quote text EXACTLY, character for character, cleanly kerned,
no misspellings, no invented words. No other text anywhere in the image.

[ZONE C: TRUST BAR — optional, --verbatim only]
Slim band along the bottom edge: aggregate star row and a counter
("[N]+ sold / served"), real numbers only.

[AUTHENTICITY RULE — hard, non-negotiable]
--verbatim: quote, reviewer, star count and counters must be real and
verifiable at publish time; the rendered text is proofread character by
character against the source before shipping — one wrong glyph misquotes a
real person, regenerate until exact.
--illustrative: NO attribution, NO "verified" label, NO counters — the card
carries an unattributed representative message and never impersonates a
specific reviewer.
LAYOUT TESTING allowance: rendering the --verbatim layout with an OBVIOUS
placeholder (to QA attribution-line typography) is permitted; placeholder
renders are test artifacts and never ship.

STYLE: clean lifestyle photography for e-commerce, bright, natural, sharp, 4K.
No lettering anywhere outside the card except the product's own reference
label. No logo, no watermark.
```

## SLOT CONSTRAINTS
- G6-EXEMPT with a fence: the card is the ONLY sanctioned text surface. The type's
  own NEGATIVE restates every non-text G6 protection (hands, product integrity,
  watermarks) — exemption covers the text tokens, nothing else.
- GLYPH CHECK is a shipping gate, not a suggestion: proofread the rendered quote
  character by character; any error → regenerate. In --verbatim mode a wrong glyph
  misquotes a real person.
- Card mode is chosen consciously: --verbatim (real review, attribution allowed,
  compliance checklist applies) vs --illustrative (representative message, no
  attribution, no verified label, no counters — never impersonates a reviewer).
- Gaze off-camera is structural: candid delight reads as an overheard moment the
  quote then explains; direct-to-lens turns it into an ad and the quote into a script.
- Negative-space discipline is the layout's reason to exist — if the scene fills the
  frame there is nowhere legible for the card, and the type fails.
- Keep the quote SHORT (≤ 12 words ideal, ≤ 20 hard) — text fidelity degrades with
  length; long quotes belong to page copy, not the image.

## NEGATIVE
G6-exempt (text tokens only) — non-text protections restated in full:
```
watermark, logo, deformed hands, extra fingers, redesigned product,
altered product shape, invented product details, different product than
reference, text outside the review card, misspelled words, distorted or
doubled letters, gibberish characters, extra star rows, second card,
direct eye contact with camera, posed stiffness, cluttered background in
the card zone, dark moody grade, badges, arrows
```

## VARIANTS
### --verbatim
The card cites a real published review. Diff: attribution line ON
("[first name + initial] | [platform's verified label]"); optional [ZONE C]
trust bar allowed. Compliance checklist is a shipping gate: the review exists,
the quote is verbatim, platform naming rules honored, counters match live data.

### --illustrative (default while the product has no published reviews)
Unattributed representative message. Diff: NO attribution line, NO verified
label, NO counters, NO trust bar. The card carries a message, never a person —
it must not impersonate a reviewer.

## WORKED EXAMPLES
### example: l-cushion-office-verbatim — skeleton@0.4, run: pass
--verbatim layout. Quote and name taken verbatim from the product's own landing-page
reviews section (ErgoSupport L-Shape Cushion, flunnel export 2026-08-06); the scene
persona is matched to the quoted reviewer. Ship only if the page's reviews are
genuine; otherwise drop the attribution line (--illustrative).
```
A 3:2 bright lifestyle photograph with a testimonial card overlay.

Use the attached product photo as the exact reference for the L-shape seat cushion.
Preserve shape, proportions, material, finish and color exactly.

HERO BASE: A woman in her late 30s in a soft knit top sits sideways on her office
chair at a tidy home-office desk, turning toward the window with a relaxed
closed-eyes laugh, one hand holding a warm mug — the unguarded ease of an afternoon
without back ache. The reference cushion is clearly visible on the chair she sits
on, hugging the junction of seat and backrest, unobstructed. Late-afternoon window
light, a laptop and a small plant on the desk. She is offset to the right third of
the frame. The left 40 percent of the frame is calm negative space: a plain
warm-grey wall, gently out of focus. Bright, airy, warm grade.

REVIEW CARD: A clean white rounded-corner card floats over the left negative space,
occupying about a third of the frame width, soft drop shadow, generous padding.
On the card, top to bottom: a row of five golden stars; below it, in friendly dark
sans-serif, large and legible, exactly this quote:
"Finally, my back doesn't ache by the end of the day."
Below the quote, a smaller lighter attribution line, exactly this text:
"— Laura"
Render all card text exactly, character for character, cleanly kerned, no
misspellings. No other text anywhere in the image.

STYLE: clean lifestyle photography for e-commerce, bright, natural, sharp, 4K.
No lettering outside the card beyond the product's own label. No logo, no watermark.
```
Predicted failures: (1) glyph errors across the TWO text lines (quote +
attribution) — proofread character by character, regenerate on any miss; (2) the
cushion hidden by the sitter — seat products live UNDER people; the
"clearly visible at the seat-backrest junction" instruction is the mitigation;
(3) product fidelity without an attached reference (G1).

### example: rolling-knife-sharpener-card — skeleton@0.2, run: pass
Cross-domain stress test; mirrored layout (subject left, card right); --illustrative.
```
A 3:2 bright lifestyle photograph with a testimonial card overlay.

Use the attached product photo as the exact reference for the rolling knife
sharpener. Preserve shape, proportions, material, finish and color exactly.

HERO BASE: A man in his late 50s in a denim apron stands at a pale oak kitchen
counter, holding the reference sharpener up in one hand with a proud warm mid-laugh,
gaze off to the side toward the window — genuine candid delight, not a pose. Beside
his other hand, a wooden board fanned with paper-thin uniform tomato slices: the
result doing the bragging. He is offset to the left third of the frame.

REVIEW CARD: A clean white rounded-corner card floats over the right 40 percent of
the frame, against a plain sage-green wall gently out of focus, occupying about a
third of the frame width, soft drop shadow, generous padding. On the card, top to
bottom: a row of five golden stars; below it, in friendly dark sans-serif, large and
legible, exactly this quote:
"Five minutes. My knives glide like new."
Render the quote text exactly, character for character, cleanly kerned, no
misspellings. No attribution line. No other text anywhere in the image.

STYLE: clean lifestyle photography for e-commerce, bright, natural, sharp, 4K.
No lettering outside the card beyond the product's own label. No logo, no watermark.
```
Predicted failures: (1) glyph errors in the quote (shipping gate: proofread,
regenerate); (2) tomato fan degrading into blobs; (3) product fidelity — v0.1 runs
rendered a rod-stand system instead of the rolling sharpener; attach the reference
and verify G1, fall back to composition mode (real product photo as input) if drift
persists.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Step-5 family map: `persona-grid` = many faces, breadth; `social-handoff` = one
recommendation staged as an overheard moment; `social-card` = one published review,
face and quote separated by register (photo vs card). One page should carry at most
one of the three adjacent to conversion sections.

## BLOCK
**Waiting on four more distinct sources** — one of five, and it has been one of five since
2026-08-11. Both card modes have a rendered pass, which is why the promotion header says in
as many words that **no amount of render evidence substitutes for exemplars**.

G14 sits behind the count and is the harder gate: `--verbatim` cites a real published review
with attribution, and a card carrying a name that nobody published is a fabricated
endorsement whichever type drew it.

## CHANGELOG
- 0.4 (2026-08-10): worked-example set rotated under the cap-2 rule — the untested
  comb example (illustrative, redundant with the tested sharpener) replaced by the
  first --verbatim example: L-shape cushion, quote and name sourced verbatim from
  the product's own landing-page reviews (flunnel export 2026-08-06), persona
  matched to the quoted reviewer. A second execution (male persona, "expensive
  office chair" quote, mirrored layout) exists in session notes for swap-in after
  testing.
- 0.3 (2026-08-10): layout-testing allowance added to the authenticity rule
  (placeholder attribution renders permitted for QA, never shipped). Evidence:
  first 0.2 render — quote glyph-perfect in single pass (render-tests ledger),
  user requires the verbatim layout as the production target.
- 0.2 (2026-08-10): card moved INTO the generated image (single-pass) per user
  decision — this model's text rendering supports it; G6 exemption declared with
  non-text protections restated; card modes split into --verbatim (real review,
  attribution, compliance checklist) and --illustrative (unattributed
  representative message); glyph-check shipping gate and ≤12-word quote cap added.
  Evidence: 2 render tests of v0.1 (layer-1 on-spec both runs; user verdict
  "missing testimonial" showed the composite pipeline fought the tool's actual
  strength). Both worked examples rewritten for 0.2, statuses reset to untested.
- 0.1 (2026-08-10): staging draft from the protein-coffee testimonial exemplar,
  obs `sha256:9339ea…` (batch 2026-08-10-H). New device value `card` added to
  vocabulary in the same change. Compliance rules (verbatim real reviews only,
  marketplace prohibition) encoded at birth.
