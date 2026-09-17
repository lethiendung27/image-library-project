---
id: 06-relief-animal
step: 6
job: relief
device: animal
version: "0.2"
status: deprecated
replaced_by: 06-relief-hero
channels: [landing-page]
requires_product_photo: false
generation_mode: single-pass
axes: {}
variants: []
exempt_from: [G3, G4]
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: null
---

# 06-relief-animal — RETIRED, absorbed by the relief types

Promotion status (2026-09-10): **3 observations, 3 distinct sources — and the file argues
against its own existence.**

| source | frame | register |
|---|---|---|
| lp3-14petstable-sale50 | border collie lying on a bright green seamless, head down, eating visible fresh food from a shallow white bowl | **studio** — hard key upper left, defined shadow, fully saturated ground |
| lp2-19halden-densifol | tan-and-white dog at full stretch across mown grass, panning shot, animal sharp and ground smeared | **documentary** — low golden light, no product, no person |
| lp3-7-redpine-tileno40 | beagle rolled onto its back in sunlit grass, play-grin, two hands rubbing its chest from the bottom of frame | **phone snapshot** — hard afternoon light, a collar, a wedding ring |

**Three frames, three registers.** SPEC §3.2 absorbs at the cheapest level that fits and only
escalates when the lower level demonstrably fails: a **device** is *the signature visual
mechanism*, and there is no shared mechanism here. What the three share is that the beneficiary
is an animal, which is a value in a slot, not a way of making a picture.

**The device name says so out loud.** `animal` names WHAT is photographed. ADR-065 corrected
exactly that fault twice in one pass — `03-spec-ingredient` became `03-spec-stilllife` and
`03-spec-range` became `03-spec-lineup`, both because the id has to name how the argument is
made. This id fails that test and keeps the ledger's name only so the three records filed under
it can be followed.

## PURPOSE
Sell the state after buying where the buyer is not the beneficiary. A dog eats, runs or rolls
over, and its body reports the outcome. Recorded because the corpus carries the pattern across
three pet and supplement pages; **not** because a distinct visual mechanism has been found.

## TRIGGER
use_when: >
  RETIRED — see RETIRED; the relief types route this beat. The pattern belongs
  to the outcome beat of a pet product page, where the animal is what the product
  acts on and the owner is the reader. Today the frames it names are served by 06-relief-hero, 06-relief-scene and
  05-social-snapshot with a non-human subject, and the routing question is whether
  those types' subject slots already take one.

## SKELETON
**Not written.** A skeleton would have to pick one of the three registers and the evidence does
not pick one. Writing one now would legislate whichever exemplar was read last, which is the
`06-relief-claimstack` fault ADR-065 caught in its own diff: *the file ships with the fault named
in its own KNOWN-FLAKY rather than silently widened, because widening it now would be a guess.*

## THE FINDING WORTH KEEPING
Two things are true about an animal subject that are not true about a person, and they are the
reason this file exists at all rather than being deleted as a mis-filing:

1. **G9 arrives for free.** G9 exists because a human face performing relief is not evidence —
   the rule ranks physical evidence above expression. An animal cannot be coached into an
   expression for the lens, so its body IS the evidence. The rule this library had to write for
   people is a property of the subject here.
2. **The pain→relief pair cannot be shot.** `06-relief-scene` declares `pairs_with:
   [01-pain-scene]` and its `PARTS/subject` demands *the same demographic and the same person as
   the paired pain image*. There is no pet equivalent — nobody photographs a dog in pain to sell
   a supplement — so the arc that type is built on is unavailable, and the frame has to close
   without a bookend.

Both are statements about a SUBJECT SLOT, which is the argument for the axis and against the
type.

## SLOT CONSTRAINTS
- **G13 still binds** — two of three exemplars are outdoors with hands in frame, and a pet page
  reaches for a child beside a dog by default. No private-room setting, no age in years.
- **G14 binds the snapshot exemplar.** The beagle frame is a phone photograph with a wedding
  ring and a beaded bracelet in it. Put that on a tile carrying a reviewer's name, or under a
  lead that says customers sent the photos in, and it is a fabricated endorsement whichever
  type drew it (ADR-088; a harness that renders flags that slot, ADR-089).
- **A15 binds the studio exemplar.** The bowl frame's argument is *visible fresh food* —
  identifiable grains, kale, squash. That is a composition claim made by a photograph, and the
  library has no rule saying where it comes from.

## NEGATIVE
```
[G6] + a distressed animal, a veterinary setting, a cone, a bandage, a cage,
a person's face, a stated breed the reference does not show, a product held to the lens
```

## RETIRED — 2026-09-17

**This type is deprecated. The relief types take an animal subject instead** (owner decision,
2026-09-16, ADR-095: *"tại sao phải là relief-animal riêng trong khi có thể đưa vào relief tuỳ
sản phẩm"* — why a separate relief-animal when relief can take it, depending on the product).
The file argued the same thing from its first day. `replaced_by` names `06-relief-hero`, whose
purpose is this file's purpose with the product in frame; `06-relief-scene` and
`06-relief-claimstack` take the animal too, each in its own section.

**The pass the paragraph below asked for was run: all three refused an animal.**
`06-relief-hero`'s subject was one person, `06-relief-scene`'s the same person as the paired pain image, and
`06-relief-claimstack`'s a person or the product. The paragraph's plan for that answer was an
axis; the owner's answer is cheaper — the subject is a value picked from the product, the
parameter rung of SPEC §3.2 — so no `beneficiary` axis ships and `vocabulary.yaml` gains no
value. It is written in each LP2 file, not in `registry/types/`: since ADR-091 this folder holds its own copies of the active types, which
removed the reason this file gave for waiting.

**The ledger is not re-filed, because it does not need to be.** The three records name
`06-relief-hero` once and `06-relief-scene` twice as their `type`, with this id as
`proposed_id`. Each also breaks its type in a second way — a studio seamless where the hero
wants a room, and no product where the scene wants one — and those stay what they were:
deviations the relief types do not absorb, which nothing here widens. `05-social-snapshot`,
which the paragraph below also named, is a step-5 type and not a relief type, and it is not
widened either.

**The sections above are the record of the proposal, not instructions.** The paragraph below is
the block as it stood.

**Waiting on a ladder decision that this namespace cannot take.** The question is whether
`06-relief-scene`, `06-relief-hero` and `05-social-snapshot` already take a non-human subject —
and answering it means editing `PARTS/subject` on three ACTIVE types in `registry/types/`.
Under the namespace's own charter (`registry/pdp-dr-instruction.md`) this folder holds types the
shared registry does not have; it does not widen the ones it does.

**The precedent for widening rather than splitting is in this very folder.**
`06-relief-claimstack` was drafted around *a person carrying a felt state* because its single
exemplar had one; four of nine later sources put the PRODUCT there instead, and the fix was to
widen the slot to take a person, the product, or the product in use — not to draft a second
type. A `beneficiary` axis with values `self` and `animal`, declared once in `vocabulary.yaml`
and available to every relief type, is the same move and is what the ladder points at.

**What would settle it:** one pass over the three active types asking whether their subject
slots refuse an animal today. If they do not, this file is deleted and its three observations are
re-filed. If they do, the axis ships and this file is still deleted.

## KNOWN-FLAKY
- **Nothing observed.** No prompt, no render.
- The panning exemplar is a **motion** frame — a sharp animal against a smeared ground. If this
  ever becomes anything, that frame may belong to `registry/gif-types/` under `relief` rather
  than to a still type, and the ledger record should be re-read with that in mind.

## CHANGELOG
- 0.2 (2026-09-17): **RETIRED**, `status: deprecated`, `replaced_by: 06-relief-hero`. Owner decision
  of 2026-09-16: the relief types take an animal subject, picked from the product, so no type and
  no `beneficiary` axis. The pass this file asked for found all three relief subjects refusing an
  animal, and each LP2 file now takes one. `BLOCK` becomes `RETIRED`; the ledger is not re-filed.
  "eight records" corrected to three. ADR-095.
- 0.1 (2026-09-10): drafted from three observations across three distinct sources in batches
  2026-08-31-A and B — including `lp2-19halden-densifol`, the one source in this corpus whose
  slug carries the correct LP number. Filed reserved with no skeleton and with the case against
  its own existence written into it, because three registers over three frames is a subject and
  not a device. New device value `animal`, marked reserved and provisional in
  `vocabulary.yaml`. ADR-077.
