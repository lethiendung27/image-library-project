# pdp-dr set hero-02 — the hero in full colour, the camera a few steps back

**Rule under test:** the hero section of `registry/pdp-dr-instruction.md`, as ADR-104 left it.
**Type:** `06-relief-hero` v1.20, the LP2 copy, commercial register, no inset. **Status:
UNCOMMITTED, owner-gated.**

**What changed from `hero-01`, and why** (the owner, on three of its renders: *"màu sắc quá giả,
không sống động, không thân thiện"* — the colour is too fake, not vivid, not friendly):

| `hero-01` said | `hero-02` says | because |
|---|---|---|
| `pale walls, light wood, nothing saturated` | a sunny, lived-in home with a few real colours | every render came back beige: colourfulness 23–27, against 51 for the TopLaser product photo |
| `Grade: bright, neutral, true to life.` | editorial realism, vivid and true colour | G11: a resolved state is full colour; the owner's feature-image instruction asks for vivid color contrast |
| `soft window light … gentle shadows` | bright, warm daylight with natural shadows and real contrast | shadowless haze is what reads as fake |
| `bright and calm` for the left half | softly blurred and full of daylight | "calm" pulled the frame toward grey |
| clothes left to the model, which chose beige | a clear, friendly colour named for each person | the owner's word was "unfriendly" |
| a smile in every prompt | a natural, relaxed expression | the owner's instruction: no posed or exaggerated smile |
| no camera distance | "Seen from a few steps back" | two of three renders put the face in the top fifth |
| a product-only option | a person in every prompt | the owner's instruction: usage first, never a product set down for display |

**Attach the product photo to every prompt.** In `hero-01`, all three products came back generic:
no antennas, a plain bag, a greige device. That is what a render looks like when the photograph
is missing.

| product | attach |
|---|---|
| WiBoofy AC1200 Wi-Fi extender | `wiboofy-final-product-type 2/assets/gallery-1-product.jpg` |
| Hivefold beeswax bread bag, set of 2 | `t2-eco-final-product-type/assets/photo-1-set.jpg` |
| TopLaser 2.0 | `aure-toplaser-final 2/assets/gallery-1.jpg` |

**Testing, as before.** Put each render in place of the template's `assets/hero-banner.webp`,
keeping the original, and check it at a phone width, 768–1023 px, 1024–1536 px and 1920 px.
Please also drop the raw renders into `image-library-assets/feedback/`, so each one can be graded
at full size and recorded by its hash.

---

## The fields

| # | template | field | product | subject |
|---|---|---|---|---|
| 1 | `wiboofy-final-product-type 2` | `hero.background` — **CONTROL** | WiBoofy | a man at work in a far room, the extender plugged in at his shoulder |
| 2 | `t1-deal-final-product-type 2` | `hero.image` | WiBoofy | a woman on a sofa in a back room, the extender plugged in beside her head |
| 3 | `t2-eco-final-product-type` | `hero.image` — known risk | Hivefold | a woman lifting a loaf out of the bag |
| 4 | `t2-eco-final-product-type` | `hero.image`, option B | Hivefold | a man sliding a loaf into the bag |
| 5 | `aure-toplaser-final 2` | `hero.image` | TopLaser | a seated woman using it on her forearm |
| 6 | `aure-toplaser-final 2` | `hero.image`, option B — known risk | TopLaser | a standing woman using it on her upper arm |

**Why these six.**
- **The owner's own products.** The owner asked for a hero test on the templates, so the products
  are the templates' own, and this set repeats them on purpose.
- **Prompt 1** is `hero-01`'s one construction whose placement held: a seated person with a fixed
  product. It is the control for the new colour.
- **Prompts 3 and 6** are the two constructions that lost their placement in `hero-01`.

## THE LOCK — every sentence written once here and repeated word for word

| field | the sentence |
|---|---|
| setting | `Setting: a sunny, lived-in home with a few real colours: plants, fruit, bright textiles.` |
| light | `Light: bright, warm daylight from the left, with natural shadows and real contrast.` |
| grade | `Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out.` |
| no words | `Nothing in the picture carries a word, a number, a label or a badge.` |
| the corner | `Nothing is placed in the bottom-right corner of the frame.` |

The light and grade lines are the instruction's hero lines, word for word. **The hero sentences**
are the instruction's too; all six prompts carry all five, because every one has a person in frame.

**The rest is unchanged from `hero-01`.**
- **Casting** is named positively, and TopLaser's people are Australian, of European descent, with
  light skin and dark hair, as the page's own FAQ requires.
- **G7-X:** the extender is plugged into a wall socket at shoulder or head height.
- **The treatment** stays on the arm.
- **G2:** no part, material or colour of any product is named.
- **The bag's box**, which carries printed words, stays out of frame.

## THE CONTROL — prompt 1, predicted **PASS**

A seated person held the safe box in `hero-01`, so this prompt isolates the new light and grade.
If it comes back beige again, the fault is in the grade lines. If the extender comes back
without its antennas, the photograph was not attached.

**Predictions, written before the render:**
- **Prompt 2:** PASS on colour. PARTIAL risk on the socket's height.
- **Prompt 3, known risk:** PARTIAL. "A few steps back" should clear the top fifth, and the
  counter still pulls the loaf toward the bottom fifth.
- **Prompt 4:** PASS. Sliding a loaf into the bag keeps the hands at counter height.
- **Prompt 5:** PASS.
- **Prompt 6, known risk:** PARTIAL. This is the second test of a standing person; the camera
  distance is the only new variable.

## Watch items

1. **Colour.** Clear, warm, lived-in, with a few real colours, and never beige all over. Compare
   each render with the template's own banner.
2. **The safe box.** At 1920 px no face, hand or product is cut. On a phone the group sits just
   right of centre and whole.
3. **Skin and expression.** Real skin, a relaxed face, no posed grin.
4. **The product.** Exactly its photograph: the extender's antennas, the bag's print, the device's
   white and gold. The extender is plugged in.
5. **The left half.** Full of daylight, blurred, with nothing that matters and no second subject.
6. **Words.** None anywhere, and no box.

---

## 1 — `06-relief-hero` v1.20 · hero · `hero.background` on `wiboofy-final-product-type 2` · ATTACH 1 · **CONTROL, predicted PASS**

```
Photograph of a sunny home office at the far end of a house, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A European man in his thirties, in a denim-blue shirt, works at a desk on a laptop with its screen turned away, with a natural, relaxed expression. The Wi-Fi extender is plugged into a wall socket just above the desk beside him, level with his shoulder.

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

## 2 — `06-relief-hero` v1.20 · hero · `hero.image` on `t1-deal-final-product-type 2` · ATTACH 1

```
Photograph of a sunny garden room at the back of a house, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A North American woman in her forties, in a coral knit top, sits on a sofa with a tablet in her lap, its screen turned away, with a natural, relaxed expression. The Wi-Fi extender is plugged into a wall socket just above the sofa's arm beside her, level with her head.

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

## 3 — `06-relief-hero` v1.20 · hero · `hero.image` on `t2-eco-final-product-type` · ATTACH 1 · known risk

```
Photograph of a sunny home kitchen at breakfast, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.
Where several reference photos are attached, this image uses the large bag and only that one.

A European woman in her thirties, in a mustard-yellow top, lifts a crusty loaf out of the open bread bag on the counter, with a natural, relaxed expression. No box is in the picture.

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

## 4 — `06-relief-hero` v1.20 · hero · `hero.image` on `t2-eco-final-product-type` · ATTACH 1 · option B

```
Photograph of a sunny kitchen in the afternoon, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.
Where several reference photos are attached, this image uses the large bag and only that one.

A European man in his forties, in a sky-blue shirt, slides a fresh loaf into the bread bag on the counter in front of him, with a natural, relaxed expression. No box is in the picture.

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

## 5 — `06-relief-hero` v1.20 · hero · `hero.image` on `aure-toplaser-final 2` · ATTACH 1

```
Photograph of a sunny living room, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

An Australian woman of European descent in her thirties, with light skin and dark hair, in a sage-green top, sits on a sofa and holds the device flat against her forearm, watching it with a natural, relaxed expression.

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

## 6 — `06-relief-hero` v1.20 · hero · `hero.image` on `aure-toplaser-final 2` · ATTACH 1 · option B, known risk

```
Photograph of a sunny hallway beside a tall window, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

An Australian woman of European descent in her twenties, with light skin and dark hair, in a terracotta tank top, stands by the window and glides the device along her upper arm, watching it with a natural, relaxed expression.

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
