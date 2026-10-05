# pdp-dr set hero-07 — the hero law on a small product: the RFID Blocking Bifold Wallet

**Type:** `06-relief-hero` v1.20, the LP2 copy, commercial register, no inset. **Rule under test:**
the hero section of `registry/pdp-dr-instruction.md` as **ADR-122** left it — the safe box at
55–86% across and 28–72% down, and the second fixed sentence rewritten to a third of the height
with the top and bottom thirds clear. **Status: UNCOMMITTED, owner-gated.**

**RENDERED 2026-10-05, and this set is now a RECORD.** The harness graded the three frames fail / partial / fail (ADR-123, three ledger lines). ADR-123 then rewrote the second fixed sentence, so **`check.py` here FAILS on purpose**: it reads the sentences out of the law file, and the law has moved past the words these three renders were made from. The prompts are left exactly as they were rendered. `hero-08` is the same three constructions under the new sentence.

**What the owner asked, 2026-10-05:** *"test prompt hero đối với sản phẩm RFID Blocking Bifold
Wallet"*.

**Why this product is the right test.** Every hero the law has seen was a large object — an
extender, a bread bag, a laser comb, a seat cushion, a furniture lifting set. This one is
**10.9 × 8.0 × 1.5 cm**. The law asks the product to be at least about an eighth of the width and
big enough to recognise at a glance, and it asks the group to sit inside a band 44% of the height.
A wallet only clears that bar held up near the camera, so all three prompts bring it to the hand
and bring the camera in. If the law cannot do a wallet, it cannot do a phone case, a charger or a
pair of earbuds either.

**Product facts used, from `Product Input 8 Sep/23-fill-inputs-rfid-blocking-bifold-wallet.csv`:**
the side button fans the cards up in a stepped layout in about half a second; the wallet is a
bifold carried in the front pocket; the persona is a male commuter of 25–55 who moves through
crowded transit hubs. Nothing else from the page is drawn — the blocking itself is invisible and
a hero sells the state, not the mechanism.

**ATTACH THE PHOTO, and check one thing first.** The brief records two constructions under the
same name: an aluminium chamber with a side-button eject, and a plain leather bifold with a
lining and no button (ADR-120 — how the product physically works outranks what the page says).
**All three prompts draw the cards fanning from the side button.** If the photo the owner attaches
has no side button, say so and the three prompts are rewritten around what it does have.

---

## The three prompts

| # | construction | what it tests | person | predicted |
|---|---|---|---|---|
| 1 | seated commuter, chest-up, wallet in hand | the hero law's own construction on a small product — **CONTROL** | yes, face in frame | PASS |
| 2 | two hands over a table, no face | the banner kind with no head to lose (ADR-122) | hands only | PARTIAL |
| 3 | the wallet large on a train table, its owner soft behind | the product-forward banner kind (ADR-122) | yes, out of focus | PARTIAL |

**The shared risk, named before the render: the fan.** Cards standing up in a stepped layout is a
mechanical state no render in this library has drawn. Watch for a loose spray of cards, a hand of
playing cards, or cards lying flat.

**Watch items**
1. Is the wallet recognisable at a glance, or a dark rectangle in a hand?
2. Does any face, hand or part of the wallet reach into the top or bottom third?
3. Do the cards stand in a stepped fan from the side button?
4. Is the product the attached photo's — the same body, the same finish?
5. Did the frame bring any print into itself — a sign, a ticket, a card face with a logo?

---

## 1 — `06-relief-hero` v1.20 · hero · `hero.image` on `t1-deal-final-product-type 2` · ATTACH 1 · **CONTROL, predicted PASS**

```
Photograph inside a commuter train carriage, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A North American man in his thirties, in a navy field jacket, sits by the window holding the wallet open, his thumb pressing its side button so the cards stand up in a stepped fan, his other hand lifting the top card. His expression is natural and relaxed.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about a third of the picture's height and sits across the middle, and no face, no hand and no part of the product reaches into the top third or the bottom third.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.
Any person turns slightly toward the left side of the picture.

Setting: a commuter train carriage where the colours are the carriage's own.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 2 — `06-relief-hero` v1.20 · hero · `hero.image` on `t1-deal-final-product-type 2` · ATTACH 1 · no face · predicted PARTIAL

```
Photograph of a plain wooden table by a window in the morning, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

Two hands hold the wallet open above the table, the right thumb pressing its side button so the cards stand up in a stepped fan, the left fingers taking the top card. No face is in the frame, and the sleeves are a plain charcoal knit.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about a third of the picture's height and sits across the middle, and no face, no hand and no part of the product reaches into the top third or the bottom third.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.

Setting: a plain wooden table where the colours are the room's own.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 3 — `06-relief-hero` v1.20 · hero · `hero.image` on `t1-deal-final-product-type 2` · ATTACH 1 · product-forward · predicted PARTIAL

```
Photograph of the fold-down table of a train seat, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

The wallet lies open on the table close to the camera, its cards standing up in a stepped fan, pressed up by the side button, a hand resting beside it. Further back a North American man in his forties, in a charcoal overcoat, sits out of focus, relaxed.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about a third of the picture's height and sits across the middle, and no face, no hand and no part of the product reaches into the top third or the bottom third.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.
Any person turns slightly toward the left side of the picture.

Setting: a train seat table where the colours are the carriage's own.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```
