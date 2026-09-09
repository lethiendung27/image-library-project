---
id: lede-pain
version: "0.1"
status: active
replaced_by: null
products_in_frame: none
requires_product_photo: false
awareness: [unaware, problem-aware]
inherits: 01-pain-scene
blocked_by: null
exempt_from: []
---

# lede-pain

## PURPOSE
The afternoon the reader is already having, before the category exists for them. One
person or animal in the situation the list is about to solve, and **no product anywhere
in the frame**. Its only job is recognition: the reader sees their own week and keeps
reading.

## TRIGGER
use_when: >
  Cold traffic arriving from an ad whose creative shows the problem, where this frame is
  the message match and the reader would not yet search the category by name. The
  product block's problems_solved are physical and locatable — a body, an object, a
  room — rather than abstract. Prefer this over lede-inuse when the reader does not yet
  know a product like this exists, and over lede-lineup and lede-testing whenever the
  page has to earn attention before it can earn trust.

## BOUNDARY
**Against `lede-inuse`, and this is the whole line: the product is ABSENT here and
PRESENT there.** No judgement is needed to tell them apart, which is what makes the pair
safe to put in front of a router.

**Against `lede-testing`** — this frame is the READER's situation; that one is the
REVIEWER's bench. The hands belong to different people and the room is a different room.
A frame where the sufferer is also the tester argues neither.

**Against `lede-winner`** — a winner frame presents a choice already made. This one
presents a problem not yet named. They are the two ends of the page and never compete for
the same brief.

Its boundaries against `01-pain-split` and `02-symptom-rail` are the parent's and are not
restated here.

## SKELETON
```
TYPE: lede-pain v0.1 — inherits 01-pain-scene
REGISTER: editorial photograph, one frame, no words anywhere in the picture.

[SUBJECT]   -> 01-pain-scene PARTS/subject
[EVIDENCE]  -> 01-pain-scene PARTS/evidence     the symptom as physical fact (G9)
[COST]      -> 01-pain-scene PARTS/cost         what the pain PREVENTS, in frame (A14)
[PLACE]     -> 01-pain-scene PARTS/place
[GAZE]      -> 01-pain-scene PARTS/gaze
[LIGHT]     -> 01-pain-scene PARTS/light
[GRADE]     -> 01-pain-scene PARTS/grade
[GROUND]    -> toplist-instruction, the ADR-068 ground rule
```
Every part above is DEFINED in the parent and expanded from there at render time. Nothing
is restated here — see `toplist-instruction.md`, *Inheritance*.

The one addition this slot makes is `GROUND`: a lede is scraped as `og:image` and sits
beside the page's own headline, so it is read at thumbnail size before it is read at all.
ADR-068's measurement applies — light and low-saturation unless the prompt says why not.

## NEGATIVE
```
[parent 01-pain-scene NEGATIVE] + the product, its packaging, a brand mark,
any word, number, price or logo baked into the picture,
an animal in visible distress, restraint or apparent injury
```
**The animal clause is this namespace's own and the repo has no rule behind it yet.** Ad
platforms refuse distressing pet imagery and a top-N list of pet products is a common
brief; `registry/rules.md` covers minors at G13 and says nothing about animals. Recorded
here rather than invented as a global rule on zero observations. **The parent
`01-pain-scene` should carry the same clause when it is next opened**, because the
exposure is the parent's too and this file cannot bind it.

## CHANGELOG
- 0.1 (2026-09-09): drafted for the top-N lede slot, inheriting `01-pain-scene`, whose
  `use_when` already reads *"Cold traffic that does not know the product yet. Advertorial
  header image, Facebook/native ad creative, opening image of a story"* — the owner's
  type 1 word for word. No skeleton is copied. ADR-069.
