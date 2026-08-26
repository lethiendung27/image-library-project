---
id: 03-spec-macro
step: 3
job: spec
device: macro
version: "0.4"
status: reserved
replaced_by: null
ratios: ["1:1"]
channels: [marketplace]
requires_product_photo: true
generation_mode: single-pass
axes: {}
variants: []
exempt_from: []
pairs_with: []
never_with: [03-spec-split]
avoid_adjacent: []
---

# 03-spec-macro — STAGING DRAFT

Promotion status (2026-08-11): **3 exemplars ledgered, 2-3 distinct sources**
(dominant-frame form: obs `sha256:1fe139…` batch 10-F gold carving disc,
`sha256:ffcabb…` 11-A drill-shear gear head; inset form, scope-contested:
`sha256:290dd7…` 11-E clip-fan clamp dial). Pending: 2 more dominant-frame
exemplars, the scope ruling below, router-confusion test, ≥1 rendered worked
example, human review. Not routable.

## PURPOSE
Build quality exhibited at surface scale: an extreme close-up in which the
material itself — machined teeth, milled edges, braided strands, layered
tread — is the entire argument. Texture as proof of engineering; nothing is
claimed that the surface cannot show.

## TRIGGER
use_when: >
  Categories where buyers finger the merchandise in their head: cutting
  tools, machined metal, braided cords, engineered surfaces. Step-3 gallery
  image for the "is it solid" doubt. Strongest when a live action (mid-cut,
  under load) anchors the texture to function.
avoid_when: >
  Products whose surfaces are honestly unremarkable (smooth plastic shells —
  use explode or xray for what hides inside). Never beside 03-spec-split
  (never_with: two component-superiority arguments protest too much). Not for
  soft/lifestyle positioning where machining aesthetics read as industrial
  coldness.

## SKELETON
```
TYPE: 03-spec-macro v0.4
RATIO: [1:1]
REGISTER: polished commercial studio macro photography. Extreme close range.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. The magnified region
must be a TRUE region of the reference product — same geometry, same
material, same finish. Do not redesign, simplify or add features.

[MACRO SUBJECT — the frame belongs to it]
The [working surface / structural detail] of the product filling [70-90%,
or 55-70% when a locator is present]
of the frame: [the specific machined/engineered feature], every
[tooth / strand / layer / edge] individually resolved.
LIGHT BEHAVIOR LAW: describe how light behaves on the real material —
[glints per tooth edge / matte grain / anodized sheen] — or the model will
render generic texture (verified carry-over risk: generators default to
generic knurling instead of countable features).

[ACTION ANCHOR — include when the product acts]
The surface caught mid-work: [the material being cut / the load being
held / the strand under tension], physically plausible, motion minimal.
The action ties texture to function; without it the image is jewelry.

[SCALE WITNESS — optional]
[One real object or material the surface acts on] at frame edge for scale.
Never a coin, ruler or gauge — measurement props read as a lab claim.

[SIGNAL SILENCE]
No glow rims, no emblems, no etched badges, no color-coded highlights.
The material carries the argument bare (observed market habits — cyan rim
glow, check-and-gear emblems — are excluded: a proof-adjacent device needs
no verdict marks). Product-identity colors stay as the reference shows.

STYLE: premium macro product photography, razor sharp, high detail, 4K.
NO text, no numbers, no logo, no watermark, no badges.
```

## SLOT CONSTRAINTS
- SCOPE RULING (0.1): this type is the DOMINANT-FRAME material macro only.
  The observed packshot-plus-magnifier-inset execution (obs `sha256:290dd7…`,
  clamp dial with rotation arrow) is a different genre — a feature callout,
  annotation-driven, mechanism-flavored — and is deliberately NOT absorbed
  here. It stays a 1-observation open question in the ledger; three sightings
  make it a candidate of its own, not a widening of this one.
- The countable-feature law is the quality bar: teeth, strands and layers must
  resolve as individuals. If the count blurs, the render failed the argument.
- G7 note: the macro crop is a viewing scale, not a staging violation — but
  the SCENE at that scale still obeys G7 (mid-cut means real material, real
  chips; nothing propped for the camera).
- G3: no signal colors at all; this device is exempt from nothing by
  exemption — it simply uses none.

## NEGATIVE
```
[G6] + glow rims, neon edges, etched emblems, badges, check marks,
color-coded highlights, measurement props, rulers, coins, lab equipment,
generic knurling, blurred repeating texture, people, faces, panels,
split frames, dark gothic grading, oil sheen added for drama
```

## WORKED EXAMPLES
### example: drill-shear-gearhead — skeleton@0.1, run: untested
Product: drill-mounted metal shear attachment · ratio 1:1
- MACRO SUBJECT — the gear-cut drive wheel filling about 80% of the frame, every machined tooth individually resolved, bearing race and hex arbor bolt sharp behind it; the magnified region is a true region of the reference
- LIGHT BEHAVIOUR — one crisp glint per tooth edge along the light side, matte tool-steel grain between teeth, no bloom
- ACTION ANCHOR — the wheel caught mid-cut through galvanised sheet metal, a clean curl of cut steel sweeping behind, physically plausible, motion minimal
- SCALE WITNESS — the sheet metal itself at the frame edge
- SIGNAL SILENCE — no glow, no emblem, no highlight colours; bare machined steel carries the argument
Predicted failures: (1) generic knurling instead of countable gear teeth (the
verified carry-over risk — the light-behavior line is the mitigation);
(2) the cut curl rendering as soft ribbon instead of metal; (3) a cyan rim
glow imported from market exemplars (the negative must fire).

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Step-3 magnification family: macro = the surface at dominant scale (build
quality); xray = through the shell (mechanism); explode = apart (census);
relief-hero --detail = one magnified detail INSIDE a hero's inset (feature
legibility).

**A LOCATOR THAT CANNOT BE READ IS NOT A LOCATOR, AND THIS TYPE HAS TO MAKE
ROOM FOR ONE.** Its only job is to let a reader place the magnified region on the
whole product. It is sized by G10's maximisation clause with **this type's floor
raised to ONE THIRD of the frame width**, because a locator must show a WHOLE
product and a whole product at small scale is a silhouette — which is exactly
what 21.2% and 2.4%-of-frame locators returned.

**The MACRO SUBJECT's fill band yields when a locator is present: 55-70% of the
frame rather than 70-90%.** Those two numbers were written a round apart and pull
against each other — tell the subject to fill 70-90% and then tell the locator to
grow until it would touch the subject, and the locator has nowhere to go. The
subject gives up the room, not the locator.

The locator may sit OVER the subject where the subject carries no information
there — plain material, an out-of-focus flank. What it must never cover is the
fit, join or texture the frame exists to show. Two renders failed on this alone — a
21.2% disc carrying a small silhouette, and a 2.4%-of-frame square cramped into a
corner against two edges. The macro still keeps the frame; a bigger locator does
not change that.

**This type MAY carry an inset as of 0.2, and the boundary with `--detail` is
DIRECTION, not furniture.** Owner decision with one render behind it: the macro
keeps the frame and the inset is a small LOCATOR showing the whole product so the
magnified region can be placed on it. `relief-hero --detail` is the opposite — the
SCENE keeps the frame and the magnified detail lives in the inset. Same two
elements, opposite dominance. The 0.1 SCOPE RULING excluding the macro-as-inset
observation is superseded (ADR-054); that observation was already counted among
this type's exemplars, so reversing the ruling adds none.

## CHANGELOG
- 0.4 (2026-08-26): **the locator was being squeezed by this type's own fill band.** MACRO
  SUBJECT drops to 55-70% of frame when a locator is present, the locator's floor is raised to a
  third of frame width, and it may sit over parts of the subject that carry no information. Two
  rules written a round apart were pulling against each other and the locator lost. · this commit
- 0.3 (2026-08-26): **the locator has to be readable to be a locator.** Sizing moves to G10's
  maximisation clause after two renders carried a locator too small to place the magnified region
  — a small silhouette in a 21.2% disc, and a 2.4%-of-frame square cramped against two edges. Also
  from that round: 6 of 6 complex products now read as a FIT between materials, including three
  materials in one frame, and a NO-INSET control read as well as the two with locators — so the
  inset costs nothing in macro quality and must earn its place by being useful. · this commit
- 0.2 (2026-08-26): **first three renders ever, and the inset ban is lifted.** All three subjects
  were a FIT between two materials — the assembly test the 0.1 exemplars never carried — and all
  three read as a fit. `insets` leaves the NEGATIVE list and the 0.1 SCOPE RULING is superseded
  (ADR-054): a render on the owner's instruction kept the macro dominant and the inset a locator,
  which is the opposite dominance from `relief-hero --detail`. Promotion still needs SPEC
  §6.3(3), the owner's verdict, and criterion 1 is still one exemplar short. · this commit
- 0.1 (2026-08-11): staging draft from two dominant-frame exemplars — gold
  carving disc (obs `sha256:1fe139…`, batch 10-F), drill-shear gear head
  mid-cut (`sha256:ffcabb…`, 11-A) — with the countable-feature and
  light-behavior laws lifted from their shared carry-over risk note. Third
  observation (`sha256:290dd7…`, macro-as-inset with rotation arrow) recorded
  and deliberately EXCLUDED by the scope ruling; observed glow-rim and emblem
  habits (`sha256:ffcabb…`) encoded as negatives.
