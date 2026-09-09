---
id: lede-authority
version: "0.1"
status: reserved
replaced_by: null
products_in_frame: one
requires_product_photo: true
awareness: [solution-aware, product-aware]
inherits: null
blocked_by: out-of-library-scope
exempt_from: []
---

# lede-authority

## PURPOSE
The writer with the product in their hands — the editorial register, where the page's
credibility is a person rather than a method.

## TRIGGER
use_when: >
  The page's authority is its byline and the brief carries a real author. Rare, and
  reached for when the tone must read as editorial rather than as commerce.

## BOUNDARY
**Against `lede-testing`** — that one argues a METHOD and shows no face; this argues a
PERSON. The library has a strong preference between them and it is written into G9: an
expression is not evidence, a physical fact is.

**Against `05-social-snapshot` and `05-social-handoff`** — those argue that a customer
used it. This argues that an expert judged it.

## BLOCK — why this is `reserved`, and it is the firmest of the four
This type is refused twice over, and one of the refusals is already in the library:

1. **`mapping/slot-rules.md` already declares it out of scope.** The `author` row reads
   *"a portrait of a named person, out of library scope"*. That is not a new decision for
   this namespace; it is the standing one.
2. **G16 marks *"a certification mark, a press logo, an award, a named expert"* as LAW,
   not taste**, and G14 makes a generated person who reads as a real endorser a
   fabricated endorsement.

**The fork is worth stating because it probably ends the type.** If the photograph is of
a real author, it is a photograph and this library does not take photographs — it is out
of scope in the plainest sense. If it is generated, it is a fabricated expert, which G14
and G16 both refuse. There is no third case, so `lede-authority` exists as a placeholder
that records why the owner's seventh type has no file with a skeleton in it.

No SKELETON and no NEGATIVE are drafted, deliberately: writing a skeleton for a frame the
library may not produce is how a banned thing ends up being taught, which is the failure
CLAUDE.md rule 6c exists to catch.

## SKELETON
```
NOT DRAFTED — see BLOCK. This type is reserved and produces no prompt.
```

## NEGATIVE
```
NOT DRAFTED — see BLOCK.
```

## CHANGELOG
- 0.1 (2026-09-09): drafted `reserved` with no skeleton. Filed so the seventh of the
  owner's seven has a record and a reason rather than being silently dropped. ADR-069.
