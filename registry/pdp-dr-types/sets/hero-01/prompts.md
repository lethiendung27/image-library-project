# pdp-dr set hero-01 — the hero banner's safe box, on the owner's four templates

**Rule under test:** the hero section of `registry/pdp-dr-instruction.md` (ADR-103) — the safe box
and the fixed hero sentences. **Type:** `06-relief-hero` v1.20, the LP2 copy, commercial register,
no inset. **Status: UNCOMMITTED, owner-gated.**

**The owner tests these on the templates themselves**:
- Put each render in the template's `assets/` folder in place of `hero-banner.webp`, keeping the
  original.
- Open the page at a phone width, a tablet width (768–1023 px), 1024–1536 px and 1920 px.
- The templates stay as they are (owner decision, 2026-09-17).

**Attach one product photo to every prompt that shows the product** — the template's own
gallery image 1:

| product | attach |
|---|---|
| WiBoofy AC1200 Wi-Fi extender | `wiboofy-final-product-type 2/assets/gallery-1-product.jpg` |
| Hivefold beeswax bread bag, set of 2 | `t2-eco-final-product-type/assets/photo-1-set.jpg` |
| TopLaser 2.0 | `aure-toplaser-final 2/assets/gallery-1.jpg` |

---

## The fields

| # | template | field | the hero's words | product | subject |
|---|---|---|---|---|---|
| 1 | `wiboofy-final-product-type 2` | `hero.background` | "Strong Wi-Fi in every room your router never reaches" | WiBoofy | a man at ease in a far room, the extender plugged in at his shoulder |
| 2 | `t1-deal-final-product-type 2` | `hero.image` | "Strong Wi-Fi in the rooms your router never reaches" | WiBoofy | a woman watching a film in a back room, the extender plugged in behind the sofa's arm |
| 3 | `t2-eco-final-product-type` | `hero.image` — **CONTROL** | "Bread that is still good on day three" | Hivefold | a woman slicing a loaf she has just taken from the bag |
| 4 | `t2-eco-final-product-type` | `hero.image`, option B | the same | Hivefold | the bag and the loaf alone, no person |
| 5 | `aure-toplaser-final 2` | `hero.image` | "Permanent Hair Removal at Home, Pain-Free in Just Weeks" | TopLaser | a seated woman using it on her forearm |
| 6 | `aure-toplaser-final 2` | `hero.image`, option B | the same | TopLaser | a standing woman using it on her upper arm |

**Why these six.** Prompts 1 and 2 put a small, fixed product beside a person. Prompts 3 and 5
put the product in someone's hands. Prompt 4 has no person, so it tests the four sentences
alone. Prompt 6 has a standing person, which is the tallest subject a hero meets.

## THE LOCK — every sentence written once here and repeated word for word

| field | the sentence |
|---|---|
| setting | `Setting: a bright, lived-in home in daylight, pale walls, light wood, nothing saturated.` |
| light | `Light: soft window light from the left, gentle shadows, no rim light.` |
| grade | `Grade: bright, neutral, true to life.` |
| no words | `Nothing in the picture carries a word, a number, a label or a badge.` |
| the corner | `Nothing is placed in the bottom-right corner of the frame.` |

**The hero sentences** are the instruction's, word for word. Every prompt carries the first
four, and the fifth goes only where a person is in frame (1, 2, 3, 5, 6).

**Where the rest comes from:**
- **Casting** is named positively (the instruction, *Composition, scene and people*).
  - WiBoofy's and Hivefold's pages name no market, so their people are European or North
    American.
  - TopLaser's page prices in AUD, so its people are Australian, of European descent.
  - They have light skin and dark hair because the page's own FAQ says IPL needs contrast
    between hair and skin.
- **G7-X:** the extender is plugged into a wall socket in both of its prompts. The socket sits at
  shoulder or head height, because a floor-level socket would put the product in the bottom
  fifth.
- **G2:** no prompt names a part, a material or a colour of any product.
- **The product block's variant sentence:**
  - Hivefold's photo shows two bags, so its prompts name the page's own word for one of them,
    "the large bag".
  - The box that photo also shows stays out of frame, because it carries printed words.

## THE CONTROL — prompt 3, predicted **PASS**

A person at counter height, the product large on the board, and the action at the height of her
hands. That places the group in the middle band without asking. If this fails, the fault is in
the hero sentences themselves.

**Predictions, written before the render:**
- **Prompt 1:** PARTIAL. The extender may come back small, since a palm-sized product at shoulder
  height is easy to lose.
- **Prompt 2:** PARTIAL. The socket behind the sofa's arm may drop to floor level.
- **Prompt 4:** PARTIAL. A product with no person tends to be centred.
- **Prompt 5:** PASS, with one watch item: the model's portrait habit may pull her to the centre.
- **Prompt 6:** PARTIAL, the known risk. A standing person tends to fill the height, and this
  prompt tests whether "about half the picture's height" turns her into a waist-up shot or cuts
  her at the edges.

## Watch items — check each render at every width

1. **The safe box.** Faces, hands and the product stay inside 55–88% across and 22–78% down.
   At 1920 px nothing of them is cut at the top or the bottom. On a phone they sit just right of
   centre and whole.
2. **The panel.** Nothing that matters sits under the page's words on a desktop.
   - `t1-deal` at 768–1023 px is a known limit: its panel reaches 72%.
3. **The left half.** Is it calm and bright? It must not be blank (`PARTS/setting`), and it must
   not hold a second subject.
4. **The product.** Recognisable on a phone, unchanged from its photograph, one bag only on
   prompts 3 and 4, and the extender plugged in on prompts 1 and 2.
5. **The person.** Turned slightly toward the left, and never in the top fifth.
6. **Words.** None anywhere, not even on the bag's own box, which must not appear.

## What is NOT written

| left out | why |
|---|---|
| an inset or a product view | a hero carries no inset (the instruction) |
| a ratio or a frame shape | ADR-016; render every prompt at 16:9 |
| a screen facing the camera | G6; both WiBoofy screens are turned away |
| a leg or bikini-line treatment | a leg runs into the bottom fifth; the forearm and the upper arm keep the device in the middle band |

---

## 1 — `06-relief-hero` v1.20 · hero · `hero.background` on `wiboofy-final-product-type 2` · ATTACH 1

```
Photograph of a quiet study at the far end of a house, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A European man in his thirties leans back in a desk chair with a mug, smiling toward a window, a laptop open on the desk with its screen turned away. The Wi-Fi extender is plugged into a wall socket just above the desk, level with his shoulder and close to the camera.

The product and anyone using it sit together in the right half of the picture, just past the centre and well clear of the right edge.
Together they fill about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place in soft focus, bright and calm, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home in daylight, pale walls, light wood, nothing saturated.
Light: soft window light from the left, gentle shadows, no rim light.
Grade: bright, neutral, true to life.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 2 — `06-relief-hero` v1.20 · hero · `hero.image` on `t1-deal-final-product-type 2` · ATTACH 1

```
Photograph of a garden room at the back of a house, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A North American woman in her forties sits sideways on a sofa with her feet tucked up, watching a film on a tablet in her lap with its screen turned away. The Wi-Fi extender is plugged into a wall socket just behind the sofa's arm, at the height of her head.

The product and anyone using it sit together in the right half of the picture, just past the centre and well clear of the right edge.
Together they fill about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place in soft focus, bright and calm, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home in daylight, pale walls, light wood, nothing saturated.
Light: soft window light from the left, gentle shadows, no rim light.
Grade: bright, neutral, true to life.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 3 — `06-relief-hero` v1.20 · hero · `hero.image` on `t2-eco-final-product-type` · ATTACH 1 · **CONTROL, predicted PASS**

```
Photograph of a home kitchen at breakfast, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.
Where several reference photos are attached, this image uses the large bag and only that one.

A European woman in her thirties stands at the counter slicing a crusty loaf she has just taken out of the bread bag, which lies open on the board beside it. She looks down at the bread with a quiet smile. No box is in the picture.

The product and anyone using it sit together in the right half of the picture, just past the centre and well clear of the right edge.
Together they fill about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place in soft focus, bright and calm, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home in daylight, pale walls, light wood, nothing saturated.
Light: soft window light from the left, gentle shadows, no rim light.
Grade: bright, neutral, true to life.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 4 — `06-relief-hero` v1.20 · hero · `hero.image` on `t2-eco-final-product-type` · ATTACH 1 · option B, no person

```
Photograph of a kitchen counter in the morning, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.
Where several reference photos are attached, this image uses the large bag and only that one.

The bread bag lies on a wooden board with a crusty loaf half out of its opening, a few fresh slices and a bread knife beside it. No person and no box is in the picture.

The product and anyone using it sit together in the right half of the picture, just past the centre and well clear of the right edge.
Together they fill about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place in soft focus, bright and calm, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.

Setting: a bright, lived-in home in daylight, pale walls, light wood, nothing saturated.
Light: soft window light from the left, gentle shadows, no rim light.
Grade: bright, neutral, true to life.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 5 — `06-relief-hero` v1.20 · hero · `hero.image` on `aure-toplaser-final 2` · ATTACH 1

```
Photograph of a sunlit living room, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

An Australian woman of European descent in her thirties, with light skin and dark hair, sits on a sofa in a sleeveless top and holds the device flat against her forearm, watching it with a calm smile.

The product and anyone using it sit together in the right half of the picture, just past the centre and well clear of the right edge.
Together they fill about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place in soft focus, bright and calm, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home in daylight, pale walls, light wood, nothing saturated.
Light: soft window light from the left, gentle shadows, no rim light.
Grade: bright, neutral, true to life.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 6 — `06-relief-hero` v1.20 · hero · `hero.image` on `aure-toplaser-final 2` · ATTACH 1 · option B, known risk

```
Photograph of a bright hallway beside a tall window, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

An Australian woman of European descent in her twenties, with light skin and dark hair, stands by the window in a sleeveless top and glides the device along her upper arm, looking at it with a relaxed smile.

The product and anyone using it sit together in the right half of the picture, just past the centre and well clear of the right edge.
Together they fill about half the picture's height, and no face, hand or part of the product enters its top or bottom fifth.
The left half continues the same place in soft focus, bright and calm, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home in daylight, pale walls, light wood, nothing saturated.
Light: soft window light from the left, gentle shadows, no rim light.
Grade: bright, neutral, true to life.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```
