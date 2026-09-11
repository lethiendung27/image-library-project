---
id: 07-identity-inhand
step: 7
job: identity
device: inhand
version: "0.1"
status: reserved
replaced_by: null
channels: [landing-page, marketplace]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [title, badge]
variants: []
exempt_from: [G7]
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Four more distinct sources - one observation is filed under this id today. The first job is a re-filing pass over two frames the ledger put elsewhere."
---

# 07-identity-inhand — STAGING DRAFT

Promotion status (2026-09-03): **1 observation filed under this id**,
`sha256:76290029257588b…` (a fist holding a razor handle upright against a plain ground).
Two further frames read as this argument and **the ledger files them elsewhere**, so they
are provenance rather than exemplars until curation re-files them:
`sha256:fc9d425cf4aeb69…` (a woman holding a sachet up beside her face) is a
`05-social-snapshot` variant-candidate, and `sha256:a8d80295d82a894…` (sock packs fanned in
front of a model) is filed to `03-spec-lineup`, which also cites it. Batch 2026-08-31-A's
summary names the pattern three times — *"PRESENT-TO-LENS … the library has no home for it
at either register"* — and this file answers that, but a summary is not a count.

Criterion 3 MET — one render, owner-verdict pending, proposed `pass` (ADR-011). Criterion 2
not run. **The binding gap is exemplars, and the first job is re-filing rather than
hunting.** Not routable.

**Step 7 and job `identity` do not exist in the vocabulary.** Both ship in the same diff
as this file or the validator errors. This is the owner's Q2b decision taking its first
concrete form: a family whose argument is the object rather than a funnel beat. Whether
that family lives in `registry/types/` under a new step or in its own namespace like
`registry/gif-types/` is the decision this draft is meant to make concrete, not to
pre-empt — the file is written so it can move either way.

**That decision was taken on 2026-09-10 and it went the second way** (ADR-077): the file now
lives in `registry/pdp-dr-types/`, the fourth namespace. The paragraph above is left standing
because it is the reasoning the decision was taken against, and because it is still half
right — this is a namespace, but a **co-registry** rather than a fork, so the id grammar and
the anatomy are `registry/types/`'s and promotion back into it is a `git mv`. The routing
question the paragraph says is deferred is still deferred: nothing here routes.

## PURPOSE
Show the object at human scale, presented rather than used. A hand holds the product up
to the camera so the buyer can read its size, its proportion and its finished face in one
glance. No room, no task, no result — this frame answers "how big is it and what does it
actually look like", which is the question a gallery's second tile is usually asked.

## TRIGGER
use_when: >
  The buyer's doubt is dimensional or physical: how big, how heavy it looks, what
  the finished face really is. The gallery tile right after the plain packshot, a
  size tile beside a spec block, or a marketplace image that has to work at
  thumbnail size. Use when the product is small enough to be held in one hand and
  its scale is genuinely hard to read from a packshot. Not for a product that must
  be seen installed or worn — that is 06-relief-hero's frame — and not where a
  face and an endorsement carry the frame, which is a social type's job.

## SKELETON
A call-map. Definitions live in PARTS or in the named global rule, once, and are expanded
into the rendered prompt.

```
TYPE: 07-identity-inhand v0.1
REGISTER: commercial product photograph. One frame, no panels, no insets.

[PRODUCT REFERENCE]  the attached photo is the exact reference.  -> G1
[GRIP]               how the hand holds it, and what it must not cover. -> PARTS/grip
[PRESENTATION]       which face of the product meets the lens.   -> PARTS/presentation
[SETTING]            one plain out-of-focus tone. No room.       -> PARTS/setting
[LIGHT]              broad and frontal; the silhouette is the point. -> PARTS/light

[TITLE]              the claim.                                   -> G16/title
[BADGE]              one short stamp. Bottom LEFT.                -> G16/badge
```

## PARTS

**`grip`** — the hand holds the product the way a person hands something over, not the way
they operate it: fingers wrapped around the body, thumb along it, wrist relaxed. **The grip
must not cover the feature the frame exists to show.** Choose where the hand sits from where
the product's identity lives, not the reverse — the same rule `06-relief-hero`'s `pose`
earned when a relaxed pose kept burying the contact point.

**One hand, and no face.** A second hand turns the frame into a use moment; a face turns it
into a testimonial, which is a social type's job and carries G14 with it. A forearm may enter;
a shoulder may not.

**`presentation`** — one face of the product, square to the lens: the labelled face, the
branded face, or the profile that makes the silhouette unambiguous. Name which. A
three-quarter turn is legal only when the silhouette is what identifies the object.

**`setting`** — one plain out-of-focus tone, no room, no surface, no second object. **This is
the one type in the library where a bare ground is correct rather than a fault**, and the
reason is that the frame is a measurement: anything else in it competes to be the ruler.
The tone is a runtime value, not identity (`vocabulary.yaml` `parameters: environment`) — name
it in the prompt and it changes nothing about what the type is.

**`light`** — broad and frontal with a soft falloff behind, so the product's edge separates
cleanly from the ground along its whole outline. Hard side light is wrong here: it carves the
silhouette into light and shadow halves and the size stops being readable.

**`scale`** — **the hand IS the scale cue and there is never a second one.** No coin, no ruler,
no phone beside it. Two rulers in a measurement frame is the same defect as two reservations
for one area, measured 2 of 2 on `06-relief-hero`.

## SLOT CONSTRAINTS
- **G1 is the entire frame, not a preamble.** The product occupies roughly the upper half and
  is the sharpest thing in the picture; a reference-faithful render is the deliverable, and a
  redesigned product here is a total loss rather than a flaw.
- **G6's `deformed hands, extra fingers` binds harder here than anywhere else in this
  library.** `adapters/nano-banana.md` Rule 5 names hands at close range as the highest
  failure rate this renderer has, and this type puts a hand across half the frame by
  construction. Keep the hand description short and functional and expect retries. If a
  product cannot survive that risk, the packshot without a hand is the safer tile.
- **G7 exemption, narrow.** A hand holding an object up to a lens is an arrangement that
  exists only to make a photograph, which G7's Placement and Reason tests forbid. The
  exemption covers the presentation pose alone; every other G7 test still binds.
- **G8 is not engaged** unless the product emits something visible in the hand, and it
  usually does not. Never invent an effect to fill the ground.
- **G11 is not engaged.** No state is depicted, so there is nothing to grade.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a second hand, a face, a shoulder, a room, a table, a surface,
a second object of any kind, a coin or ruler or phone for scale,
a cast shadow on a wall behind, motion blur, the product in use
```

## FOUNDING RENDER ROUND — 2026-09-03
One render, ratio 1:1, owner's cord tensioner attached. Verdict proposed **pass** (ADR-011).

**The hand held, and it was the biggest risk in this file.** Five fingers, plausible knuckles
and nail beds, one hand only, no second hand and no face. `adapters/nano-banana.md` Rule 5
names hands at close range as this renderer's highest failure rate and the SLOT CONSTRAINTS
above said to expect retries; 1 of 1 needed none. One run is not a denominator and the warning
stays, but the type is not dead on arrival, which was the open question.

**`grip` did what it was written to do.** The fingers wrapped the body and stayed clear of the
cam lever and the brass roller, both of which read completely — which is the clause about not
covering the feature the frame exists to show, working on its first outing.

Product faithful: brass roller, stainless cam, lever and pivot all present and unaltered.
Text 3 of 3 lines exact. Badge clean in the bottom LEFT. `setting` produced the bare pale
ground the type asks for and nothing competed to be the ruler.

Faults: margins at 6.8% left and 6.7% at the badge, against G10's 8% — the library-wide text
margin problem, not this type's. And the forearm runs out of the lower right corner, which no
clause forbids and which reads fine; note it before writing a rule about it.


## KNOWN-FLAKY
- **One render, and it passed.** Every clause above is still a proposal at n=1; `grip`,
  `presentation`, `setting` and `light` each have exactly one run behind them.
- **`sha256:a8d80295d82a894…` is cited by two proposals** — here, and by `03-spec-lineup` for
  its range argument, because the model in it holds THREE packs fanned out. The boundary is
  the count: one unit presented is this type, several units compared is the lineup. Curation
  should assign that observation to one of them rather than letting both count it.
- **The hand is still the risk, at 1 of 1 clean.** One good hand is not a denominator. If
  hands fail on ≥2 of the next 3, the honest outcome is that this type ships as a product-only
  variant and loses its scale cue, which would make it a packshot and not this type at all.

## NOTES
**Boundary against the three nearest frames.** `06-relief-hero` puts a reduced subject and a
product in one real room filled to the edges; this type deletes the room on purpose.
`03-spec-macro` magnifies a region of the product to argue material; this shows the whole
object to argue size. `05-social-snapshot` and the proposed testimony type put a person in
frame as a witness; here the hand is a ruler and carries no endorsement, which is what keeps
G14 off this type entirely.

## BLOCK
**Waiting on a re-filing pass, then on four more distinct sources.** One observation is filed
under this id; two further frames read as its argument and the ledger puts them elsewhere. The
promotion header names both and states the rule they run into: **a batch summary naming a
pattern three times is not a count.**

## CHANGELOG
- 0.1 (2026-09-03): drafted from three hash-verified observations across two batches and two
  registers. Named by batch 2026-08-31-A as a gap the library had no home for; batch
  2026-09-03-C's razor frame took it past the evidence rule's three-observation bar. First
  type to propose step 7 and job `identity`.
