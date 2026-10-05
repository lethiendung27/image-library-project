# pdp-dr set hero-04 — the same six frames, with neutral daylight and a band above the head

**Rule under test:** the hero section of `registry/pdp-dr-instruction.md` as ADR-107 left it —
neutral daylight, colour from more than one family, a real photograph, and the band above every
head in place of "a few steps back". **Type:** `06-relief-hero` v1.20, the LP2 copy, commercial
register, no inset. **Status: UNCOMMITTED, owner-gated.**

**Why the same six scenes.** `hero-03` ran them under ADR-104's lines and the owner failed the
colour: *"màu ảnh quá AI, quá yellowish, không chân thực"*. Re-running the same frames changes
one variable — the lines — so the next verdict is about the law and not about a new scene. It is
a deliberate exception to the rule that a set takes products it has not used, which is recorded
in ADR-107.

| `hero-03` said | `hero-04` says | because |
|---|---|---|
| `Light: bright, warm daylight …` | `Light: bright daylight …` | the warm cast rose from 26–29 to 33–58 |
| `Grade: editorial realism with vivid, true colour …` | `Grade: true colour, neutral whites, no warm filter and no glow.` | "editorial realism" reads as a warm magazine grade |
| a home with `plants, fruit, bright textiles` | colours from more than one family, and no fruit bowl | five of six renders put a bowl of oranges in the frame |
| `Seen from a few steps back, the group fills …` | `The group fills … with a clear band of the room above every head …` | the camera never moved; a face sat in the top fifth in five of six |
| — | `It is a real photograph: skin keeps its texture, with no glow and no haze.` | window bloom, haze and plastic skin are what read as AI |
| — | G6's screen sentence wherever a screen can appear | a laptop came back carrying a page of model-drawn text |

**Attach the product photo to every prompt.** Five of six `hero-03` renders came back with a
product that is not the product: a knitted throw pillow and a decorative pillow instead of the
cushion, an extender with no antennas, a bag with no print. Nothing in a prompt can fix that.

| product | attach |
|---|---|
| Ergonomic Memory Foam Seat Cushion | one of the page's six reference photos |
| WiBoofy AC1200 Wi-Fi extender | `wiboofy-final-product-type 2/assets/gallery-1-product.jpg` |
| Hivefold beeswax bread bag, set of 2 | `t2-eco-final-product-type/assets/photo-1-set.jpg` |
| TopLaser 2.0 | `aure-toplaser-final 2/assets/gallery-1.jpg` |

---

## The fields

| # | page or template | field | product | what it re-tests |
|---|---|---|---|---|
| 1 | `pdp-dr-seat-cushion-l-shaped-v08` | `hero.image` — **CONTROL** | seat cushion | the one placement that held; now the colour |
| 2 | `pdp-dr-seat-cushion-l-shaped-v08` | `hero.image`, option B | seat cushion | a face that sat in the top fifth |
| 3 | `wiboofy-final-product-type 2` | `hero.background` | WiBoofy | a product that sat in the top fifth |
| 4 | `t2-eco-final-product-type` | `hero.image` | Hivefold | a head cut at the top, a bag in the bottom fifth |
| 5 | `aure-toplaser-final 2` | `hero.image` | TopLaser | a standing person, the third attempt |
| 6 | `pdp-dr-seat-cushion-l-shaped-v08` | `hero.image`, option C | seat cushion | the cushion behind a back, and the warmest frame of the six |

## THE LOCK — every sentence written once here and repeated word for word

| field | the sentence |
|---|---|
| setting | `Setting: a bright, lived-in home with green, blue and red among its colours.` |
| light | `Light: bright daylight from the left, with natural shadows and real contrast.` |
| grade | `Grade: true colour, neutral whites, no warm filter and no glow.` |
| screens | `Any screen shows only a picture, with no interface, text or numbers.` — prompts 1, 2 and 3 |
| no words | `Nothing in the picture carries a word, a number, a label or a badge.` |
| the corner | `Nothing is placed in the bottom-right corner of the frame.` |

The light and grade lines are the instruction's hero lines, word for word, and so are the six
hero sentences. Every prompt carries all six, because every one has a person in frame. The two
seated-cushion prompts carry the instruction's host sentence as well:

```
The chair is in a tone and material clearly different from the cushion.
```

## THE CONTROL — prompt 1, predicted **PASS**

In `hero-03` this frame was the only one whose product read as the product, whole and from the
side, and its placement was the closest to the box. Everything except the colour lines is
unchanged, so a yellow frame here means the new lines did not work.

**Predictions, written before the render:**
- **Prompt 2:** PARTIAL. The face sat in the top fifth; the band sentence is the only change.
- **Prompt 3:** PARTIAL. The socket moves down to the height of a seated shoulder, which should
  bring the extender out of the top fifth.
- **Prompt 4:** PARTIAL. A man standing at a table is the frame that cut a head twice.
- **Prompt 5:** PARTIAL, the standing person, third attempt.
- **Prompt 6:** PASS on colour, PARTIAL on the product — a cushion behind a back is the hardest
  one to see.

## Watch items

1. **Colour.** Do the whites read white? Is there colour from more than one family, and no
   golden wash over everything?
2. **The band above the head.** A clear strip of room above every head, and another below every
   hand.
3. **The photograph.** Real skin texture, no bloom on the windows, no haze.
4. **The product.** Exactly its photograph — the cushion's real form, the extender's antennas,
   the bag's print, the device's white and gold.
5. **The cushion.** Whole, from the side, on a chair of another tone.
6. **Words.** None anywhere, and no interface on a screen.

---

## 1 — `06-relief-hero` v1.20 · hero · `hero.image` on `pdp-dr-seat-cushion-l-shaped-v08` · ATTACH 1 · **CONTROL, predicted PASS**

```
Photograph of a home office at work, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A North American man in his forties, in a sky-blue shirt, sits on the cushion at his desk, seen from the side so it reads whole, with a natural, relaxed expression. The chair is in a tone and material clearly different from the cushion.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home with green, blue and red among its colours.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Any screen shows only a picture, with no interface, text or numbers.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 2 — `06-relief-hero` v1.20 · hero · `hero.image` on `pdp-dr-seat-cushion-l-shaped-v08` · ATTACH 1 · option B

```
Photograph of a home office in the morning, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A European woman in her thirties, in a denim-blue shirt, holds the cushion in both hands at chest height and sets it onto a desk chair, with a natural, relaxed expression.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home with green, blue and red among its colours.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Any screen shows only a picture, with no interface, text or numbers.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 3 — `06-relief-hero` v1.20 · hero · `hero.background` on `wiboofy-final-product-type 2` · ATTACH 1

```
Photograph of a back room of a house, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A European couple in their thirties, in a mustard-yellow top and a green shirt, watch a film on a laptop, with a natural, relaxed expression. The Wi-Fi extender is plugged into a wall socket by the sofa, level with their shoulders.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home with green, blue and red among its colours.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Any screen shows only a picture, with no interface, text or numbers.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 4 — `06-relief-hero` v1.20 · hero · `hero.image` on `t2-eco-final-product-type` · ATTACH 1

```
Photograph of a kitchen table after breakfast, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.
Where several reference photos are attached, this image uses the large bag and only that one.

A North American man in his thirties, in a green shirt, folds a crusty loaf into the bread bag on the table, with a natural, relaxed expression. No box is in the picture.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home with green, blue and red among its colours.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 5 — `06-relief-hero` v1.20 · hero · `hero.image` on `aure-toplaser-final 2` · ATTACH 1

```
Photograph of a bright room beside a window, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

An Australian woman of European descent in her twenties, with light skin and dark hair, in a sage-green top, stands and glides the device along her upper arm, with a natural, relaxed expression.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home with green, blue and red among its colours.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 6 — `06-relief-hero` v1.20 · hero · `hero.image` on `pdp-dr-seat-cushion-l-shaped-v08` · ATTACH 1 · option C

```
Photograph of a living room in the afternoon, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A European woman in her fifties, in a coral knit top, sits back into an armchair and reads, with the cushion behind her lower back, seen from the side so the whole cushion reads, with a natural, relaxed expression. The chair is in a tone and material clearly different from the cushion.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.
Any person turns slightly toward the left side of the picture.

Setting: a bright, lived-in home with green, blue and red among its colours.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```
