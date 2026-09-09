---
id: lede-authority
version: "0.2"
status: reserved
replaced_by: null
products_in_frame: one
requires_product_photo: true
awareness: [solution-aware, product-aware]
copied_from: null
copied_at_version: null
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

## FOUNDING RENDER ROUND — a diagnostic, and it did not create a skeleton

**One render, 2026-09-09 — round 2 prompt 7, rendered at v0.1.** A man crouched beside a
sofa in a half-emptied room, holding a furniture lifter, addressing the lens. Verdict
**`partial`**, self-assigned under ADR-011 on a render that was opened and looked at.
Ledger: `eval/render-tests.jsonl`, ts `2026-09-09`. **This file still has no SKELETON and
this section does not write one.**

**The prompt's question was what survives when everything illegal is stripped out.**
Nothing refused appeared in the render: no name, byline, title card, lab coat, clipboard,
lanyard, certification seal, star row, logo, word or number. So the picture is what the
type is allowed to be, and the question is whether that is anything.

**The answer is a DEMONSTRATOR, not an authority.** What is left is a man addressing the
lens while holding the product in a real room. The authority was carried entirely by the
credential — the byline, the title, the lanyard — which is exactly what `BLOCK` says the
type may not show. Strip it and the frame stops arguing *an expert judged it* and starts
arguing *someone is showing you this*, which is a different claim and a weaker one.

**Against the neighbours it was kept apart from.** `BOUNDARY` distinguishes this type from
`lede-testing` on METHOD versus PERSON, and that distinction survives — there is no bench
and no instrument here. What does **not** survive is the distinction from `lede-inuse`: the
same product, the same kind of real room, the same natural light. The one visible
difference is the GAZE — this subject addresses the lens and `lede-inuse` requires a
candid, unaware subject — and a gaze direction is thin ground for a separate type.

**One measurement worth keeping.** This render is the round's **closest match to the
photographed ground clause anywhere in the namespace**: texture 6.8 against the clause's
7.0, value 0.64 against 0.65, ring spread 0.88 against 0.67. The clause is right; the type
carrying it is the one in doubt.

**One failure, 1 of 1:** `[SUBJECT]` — the lifter is held at floor level by its handle,
against *"holding one lifter up at chest height"*.

**What this does not do.** It does not deprecate the type. SPEC §6.3 requires a
`replaced_by` for that and no type covers a to-camera demonstration today, so the honest
state is a reserved placeholder with one render behind its own reasoning rather than none.

## CHANGELOG
- 0.2 (2026-09-09): **FOUNDING RENDER ROUND** — one render, round 2 prompt 7 at 0.1,
  `partial`, run as the diagnostic it was written as and creating no skeleton. Nothing
  refused appeared, so the render shows what this type is permitted to be: a DEMONSTRATOR
  addressing the lens, not an authority. The distinction from `lede-testing` survives; the
  distinction from `lede-inuse` reduces to gaze direction. Not deprecated — SPEC §6.3 wants
  a `replaced_by` and nothing covers a to-camera demonstration. Its ground is the round's
  closest match to the photographed clause: texture 6.8, value 0.64.
- 0.1 (2026-09-09): drafted `reserved` with no skeleton. Filed so the seventh of the
  owner's seven has a record and a reason rather than being silently dropped. ADR-069.
