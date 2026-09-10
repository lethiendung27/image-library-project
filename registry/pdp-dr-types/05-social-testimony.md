---
id: 05-social-testimony
step: 5
job: social
device: testimony
version: "0.1"
status: reserved
replaced_by: null
ratios: ["4:5", "3:4"]
channels: [landing-page]
requires_product_photo: false
generation_mode: single-pass
axes:
  register: [ugc]
variants: []
exempt_from: [G3, G4, G7]
pairs_with: []
never_with: []
avoid_adjacent: [05-social-snapshot, 05-social-card, 05-social-handoff]
requires_pair: null
blocked_by: "G14, which binds the SLOT and not the type. A testimonial thumbnail sits beside a name by definition, and G14's test says such a slot takes a real customer photograph or it takes nothing. There is no version of this type that survives its own slot."
---

# 05-social-testimony — PDP-DR DRAFT

Promotion status (2026-09-10): **3 observations, 3 distinct sources on paper — two on
re-reading.**

| source | frame | is it this device? |
|---|---|---|
| lp3-7-redpine-tileno40 | young woman, dark linen shirt, mid-sentence, straight into the lens, plain warm wall and a snake plant. No product, no props, no text | **yes** |
| lp3-15holloway-pruner6 | woman in clear-framed glasses drinking through a straw in a bright kitchen, chest up, attention on or just beside the lens | **yes** |
| lp3-17millbrook-barrierbalm | a pregnant woman and a practitioner side by side in a clinic, both smiling at the lens, both giving a thumbs-up | no — the ledger's own filename calls it `benefit-founder`, and `mapping/slot-rules.md` puts *a portrait of a named person* out of library scope |

**Two sources.** The third is the `author` row of the slot table, which ADR-069 already met from
the other direction — the owner's seventh toplist type was *author / expert* and it turned out
to be already declared out of scope. An empty row records the decision once; counting a frame
against it makes the decision a judgement call again.

**Both real exemplars are VIDEO STILLS**, vertical and softly compressed, and that is the
device rather than an accident of sourcing: the frame is a thumbnail for something that plays,
and the softness is what says a person really said this.

## PURPOSE
One person addressing the lens mid-sentence, in their own room, as the still frame of a
testimonial that plays. The argument is that a specific human is speaking — not that a review
exists, which is `05-social-card`'s job, and not that a photograph was taken, which is
`05-social-snapshot`'s.

## TRIGGER
use_when: >
  NOT YET ROUTABLE — see BLOCK. When it is: the social-proof beat of a product page
  where the page carries real filmed testimonials and this tile is one of their
  thumbnails. Choose 05-social-snapshot when nobody is addressing the camera and the
  argument is that a customer took a photograph. Choose 05-social-card when the words
  of a published review are the deliverable and the person is only the setting. Choose
  05-social-handoff when two people are in frame and one is recommending to the other.

## SKELETON
```
TYPE: 05-social-testimony v0.1
REGISTER: vertical video still, softly compressed, phone-camera optics.

[SUBJECT]      one person, chest up, mid-sentence.
[GAZE]         on the lens.                                -> the one gaze this library allows on the lens
[PLACE]        an ordinary room of their own — kitchen, hallway, living room.
[LIGHT]        whatever the room has. Never a key, never a rim.
[GRADE]        soft, slightly compressed, never graded.
```

**`gaze: confront` is why this type exists and why it is dangerous.** Every other social type in
this library keeps the subject off the lens — `06-relief-scene` says *never on the lens* in as
many words, and `05-social-snapshot` is a photograph somebody else took. A person looking into
the camera and speaking is the one frame that reads as a deposition, and that is exactly the
reading G14 refuses to let a generated image make.

## SLOT CONSTRAINTS
- **G13 has no exemptions and it binds here hardest.** A room of their own, a person addressing
  the lens, and a product page for a family category is the configuration that puts a minor in
  frame by default. No private-room setting, no age in years, and a neutral `Face:` block. A
  refused prompt returns no image at all, which is a different failure class from a weak one.
- **G9 outranks the face.** The subject is speaking, so the temptation is to write an
  expression. G9 already says emotion on a face is not evidence, and here it is not even the
  argument — the argument is that somebody sat down and said it.
- **No product in frame by default.** Two of two exemplars carry none. A product held up to the
  lens turns this into `07-identity-inhand` with a person attached.
- **No text.** Neither exemplar carries any, so this type declares no `text_layer` and G6 binds
  whole.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a name, an avatar, a star row, a verified badge, a review count, a quote,
a second person, a product held to the lens, studio light, a rim light,
a graded or warm-boosted image, a clinic, a uniform, a professional setting
```

## BLOCK
**Waiting on nothing that can be waited for.** G14 binds the SLOT rather than the type: *what
makes an image a fabricated endorsement is the furniture around it, not which type drew it*, and
the test is read off the page — if the slot sits beside a name, an avatar, a star row, a
verified badge or a review count, it takes a real customer photograph or it takes nothing.

A testimonial thumbnail sits beside a name **by definition**. That is what a testimonial is. So
there is no page arrangement under which this type is both itself and legal, and this file
exists to record that the corpus contains the pattern rather than to offer a way to draw it.

**The measured precedent is on a live page.** An advertorial carrying four `reviews.shots.*`
slots in a block with three named *Verified Purchase* quotes routed to nothing, and the session
recorded `out_of_scope_reason` rather than a prompt (2026-08-27). The same listicle template
carrying six photo slots with **no** name and **no** badge was legal with the same image — the
slot decided, not the type.

**What would unblock it, and it is not a rule change.** A page that plays real filmed
testimonials and needs their thumbnails generated is a different request from a page that needs
testimony invented; the first is out of scope for a different reason (it is a crop, not a
generation) and the second is G14. Either way this type is not the answer, and it stays reserved
until someone shows a slot where it is.

## KNOWN-FLAKY
- **Nothing observed.** No prompt, no render.

## CHANGELOG
- 0.1 (2026-09-10): drafted from three observations across three distinct sources in batch
  2026-08-31-B; one re-filed on reading to the `author` row of `mapping/slot-rules.md`, leaving
  two. Filed reserved on G14 rather than on the count, because the count is not what is wrong
  with it. New device value `testimony`. ADR-077.
