---
id: 03-spec-macro
step: 3
job: spec
device: macro
version: "1.0"
status: active
replaced_by: null
channels: [marketplace]
requires_product_photo: true
generation_mode: single-pass
axes: {}
variants: []
exempt_from: []
pairs_with: []
never_with: [03-spec-split]
avoid_adjacent: []
copied_from: 03-spec-macro
copied_at_version: "1.0"
blocked_by: null
---

# 03-spec-macro

Promoted to active 2026-08-26 **on the owner's explicit override of SPEC §6.3(1)**,
which asks for ≥5 distinct exemplars. This type has **4**, across 4 distinct
batches: `sha256:1fe139…` 10-F gold carving disc, `sha256:ffcabb…` 11-A
drill-shear gear head, `sha256:290dd7…` 11-E clip-fan clamp dial, `sha256:3ca14a…`
11-F. The owner tested the type and ruled; ADR-057 records what the ruling waives
and what it does not. Criteria 2, 3 and 4 hold on their own evidence.

**Criterion 2 passed on a technicality worth knowing.** Router-confusion was run
against every routed slot the library owns — 0 of 14 stolen — but this type is
`channels: [marketplace]` and both golden fixtures are landing-page and
advertorial, so it could not have contested a slot even if its trigger overlapped
one. The test is green because the type was not eligible to play, not because it
competed and lost. The first marketplace fixture this library grows is where this
criterion actually gets tested.

**Superseded the same day by ADR-059**, which removed channel as an admission test
altogether. This type is now a candidate for every slot on every page, so the reason
criterion 2 came back green — ineligibility — no longer exists. The criterion has still
never been tested in substance: it passed because the type could not play, and it has
not been re-run now that it can. Re-run it when a fixture next changes.

## PURPOSE
Build quality exhibited at surface scale: an extreme close-up in which the
material itself — machined teeth, milled edges, braided strands, layered
tread — is the entire argument. Texture as proof of engineering; nothing is
claimed that the surface cannot show.

**Copied verbatim from `registry/types/03-spec-macro.md` at version 1.0** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## TRIGGER
use_when: >
  Categories where buyers finger the merchandise in their head: cutting
  tools, machined metal, braided cords, engineered surfaces. Step-3 gallery
  image for the "is it solid" doubt. Strongest when a live action (mid-cut,
  under load) anchors the texture to function.

## SKELETON
```
TYPE: 03-spec-macro v1.0
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
- 1.0 (2026-09-15): copied verbatim from `registry/types/03-spec-macro.md` at 1.0, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.
