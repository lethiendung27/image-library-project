# pdp-dr set hero-03 — the hero law on a product it has never seen

**Rule under test:** the hero section of `registry/pdp-dr-instruction.md` (ADR-103, ADR-104) —
the safe box, the five fixed sentences, and the light and grade lines. **Type:**
`06-relief-hero` v1.20, the LP2 copy, commercial register, no inset. **Status: UNCOMMITTED,
owner-gated.**

**What this set adds to `hero-02`:**
- **A product the hero law has never met.** Three prompts fill the hero of the seat cushion's
  own page, whose six reference photos the owner already holds
  (`query/sessions/pdp-dr-seat-cushion-l-shaped-v08/content.json`).
- **A product that is sat on.** The cushion is the case the instruction's product section warns
  about: six earlier cushion renders hid it behind the sitter or set it on a chair of its own
  tone.
- **Two people in one frame**, to see whether "the group" still fits the safe box.
- **A standing person framed from the waist up**, which is the construction `hero-01` lost twice.

**Attach the product photo to every prompt** — one photo, the product's own:

| product | attach |
|---|---|
| Ergonomic Memory Foam Seat Cushion | one of the page's six reference photos |
| WiBoofy AC1200 Wi-Fi extender | `wiboofy-final-product-type 2/assets/gallery-1-product.jpg` |
| Hivefold beeswax bread bag, set of 2 | `t2-eco-final-product-type/assets/photo-1-set.jpg` |
| TopLaser 2.0 | `aure-toplaser-final 2/assets/gallery-1.jpg` |

**Testing, as before.** Put each render in place of the template's `assets/hero-banner.webp`,
keeping the original, and read it at a phone width, 768–1023 px, 1024–1536 px and 1920 px. The
cushion's page has no template folder, so its three renders are read in any of the four.
Please drop the raw renders into `image-library-assets/feedback/` as well.

---

## The fields

| # | page or template | field | product | subject |
|---|---|---|---|---|
| 1 | `pdp-dr-seat-cushion-l-shaped-v08` | `hero.image` — **CONTROL** | seat cushion | a woman setting the cushion onto a desk chair |
| 2 | `pdp-dr-seat-cushion-l-shaped-v08` | `hero.image`, option B | seat cushion | a man working, seated on it, seen from the side |
| 3 | `pdp-dr-seat-cushion-l-shaped-v08` | `hero.image`, option C | seat cushion | a woman reading, the cushion at her lower back |
| 4 | `wiboofy-final-product-type 2` | `hero.background` | WiBoofy | two people watching a film, the extender plugged in beside them |
| 5 | `t2-eco-final-product-type` | `hero.image` | Hivefold | a man putting the loaf away after breakfast |
| 6 | `aure-toplaser-final 2` | `hero.image` — known risk | TopLaser | a standing woman, framed from the waist up |

**The page's own words**, for the three cushion prompts: *"Continuous Lower Back Support &
Tailbone Relief"*. The hero carries none of them; the page sets them beside the image.

## THE LOCK — every sentence written once here and repeated word for word

| field | the sentence |
|---|---|
| setting | `Setting: a sunny, lived-in home with a few real colours: plants, fruit, bright textiles.` |
| light | `Light: bright, warm daylight from the left, with natural shadows and real contrast.` |
| grade | `Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out.` |
| no words | `Nothing in the picture carries a word, a number, a label or a badge.` |
| the corner | `Nothing is placed in the bottom-right corner of the frame.` |

The light and grade lines are the instruction's hero lines, word for word, and so are the five
hero sentences. Every prompt carries all five, because every one has a person in frame.

**The seated cushion carries one more sentence**, the instruction's product rule for a product
that is sat on: the chair is asked for as a relation, never as a colour.

```
The chair is in a tone and material clearly different from the cushion.
```

**The rest is unchanged from `hero-02`:** casting named positively; a clear, friendly colour for
each person; a natural, relaxed expression; the extender plugged into a wall socket; the bag's
printed box out of frame; and no part, material or colour of any product named (G2).

## THE CONTROL — prompt 1, predicted **PASS**

The cushion is carried in two hands at chest height, so it is large, whole and inside the middle
band without the frame having to work for it. If this one comes back drained or badly placed,
the fault is in the law rather than in the product.

**Predictions, written before the render:**
- **Prompt 2:** PARTIAL. A sat-on cushion is the instruction's own hard case. Watch for the
  sitter hiding it and for a chair of the same tone.
- **Prompt 3:** PARTIAL. At the lower back the cushion is behind the body; the side view has to
  carry it.
- **Prompt 4:** PARTIAL. Two people widen the group, and the safe box is 33% of the width.
- **Prompt 5:** PASS. One person at a table, the product large in his hands.
- **Prompt 6, known risk:** PARTIAL. `hero-01` cut a standing woman's head twice. This prompt
  adds the waist-up framing to "a few steps back".

## Watch items

1. **The safe box.** At 1920 px nothing of the group is cut. On a phone it sits just right of
   centre and whole.
2. **The cushion is visible.** Whole silhouette, from the side, not swallowed by the sitter, and
   not on a chair of its own tone.
3. **Two people.** Do they still fit between the panel and the right edge?
4. **Colour.** Warm daylight, real shadows, a few real colours, and no beige wash.
5. **The product.** Exactly its photograph. The extender plugged in, the bag's print, the
   device's white and gold.
6. **Words.** None anywhere, and no box in the bread frames.

---

## 1 — `06-relief-hero` v1.20 · hero · `hero.image` on `pdp-dr-seat-cushion-l-shaped-v08` · ATTACH 1 · **CONTROL, predicted PASS**

```
Photograph of a sunny home office in the morning, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A European woman in her thirties, in a denim-blue shirt, holds the cushion in both hands at chest height and is setting it onto a desk chair, with a natural, relaxed expression.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
Seen from a few steps back, the group fills about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a sunny, lived-in home with a few real colours: plants, fruit, bright textiles.
Light: bright, warm daylight from the left, with natural shadows and real contrast.
Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 2 — `06-relief-hero` v1.20 · hero · `hero.image` on `pdp-dr-seat-cushion-l-shaped-v08` · ATTACH 1 · option B

```
Photograph of a sunny home office at work, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A North American man in his forties, in a sky-blue shirt, works at a desk sitting on the cushion, seen from the side so the whole cushion reads under him, with a natural, relaxed expression. The chair is in a tone and material clearly different from the cushion.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
Seen from a few steps back, the group fills about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a sunny, lived-in home with a few real colours: plants, fruit, bright textiles.
Light: bright, warm daylight from the left, with natural shadows and real contrast.
Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 3 — `06-relief-hero` v1.20 · hero · `hero.image` on `pdp-dr-seat-cushion-l-shaped-v08` · ATTACH 1 · option C

```
Photograph of a sunny living room in the afternoon, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A European woman in her fifties, in a coral knit top, sits back into an armchair and reads, with the cushion behind her lower back, seen from the side so the whole cushion reads, with a natural, relaxed expression. The chair is in a tone and material clearly different from the cushion.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
Seen from a few steps back, the group fills about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a sunny, lived-in home with a few real colours: plants, fruit, bright textiles.
Light: bright, warm daylight from the left, with natural shadows and real contrast.
Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 4 — `06-relief-hero` v1.20 · hero · `hero.background` on `wiboofy-final-product-type 2` · ATTACH 1

```
Photograph of a sunny back room of a house, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A European couple in their thirties, one in a mustard-yellow top and one in a green shirt, sit together on a sofa watching a film on a laptop with its screen turned away, with a natural, relaxed expression. The Wi-Fi extender is plugged into a wall socket just behind the sofa, level with their heads.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
Seen from a few steps back, the group fills about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a sunny, lived-in home with a few real colours: plants, fruit, bright textiles.
Light: bright, warm daylight from the left, with natural shadows and real contrast.
Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 5 — `06-relief-hero` v1.20 · hero · `hero.image` on `t2-eco-final-product-type` · ATTACH 1

```
Photograph of a sunny kitchen table after breakfast, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.
Where several reference photos are attached, this image uses the large bag and only that one.

A North American man in his thirties, in a terracotta shirt, folds a crusty loaf into the bread bag on the table, a bowl of fruit beside him, with a natural, relaxed expression. No box is in the picture.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
Seen from a few steps back, the group fills about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a sunny, lived-in home with a few real colours: plants, fruit, bright textiles.
Light: bright, warm daylight from the left, with natural shadows and real contrast.
Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 6 — `06-relief-hero` v1.20 · hero · `hero.image` on `aure-toplaser-final 2` · ATTACH 1 · known risk

```
Photograph of a sunny bright room beside a window, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

An Australian woman of European descent in her twenties, with light skin and dark hair, in a sage-green top, stands and glides the device along her upper arm, framed from the waist up, with a natural, relaxed expression.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
Seen from a few steps back, the group fills about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a sunny, lived-in home with a few real colours: plants, fruit, bright textiles.
Light: bright, warm daylight from the left, with natural shadows and real contrast.
Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```
