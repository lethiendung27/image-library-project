# pdp-dr set hero-05 — three scenes, two prompt forms

**Rule under test:** the hero section of `registry/pdp-dr-instruction.md` as ADR-108 left it —
the room's own colours, and the trial of the owner's feature-image form for a hero. **Type:**
`06-relief-hero` v1.20, the LP2 copy, commercial register, no inset. **Status: UNCOMMITTED,
owner-gated.**

**Where this set comes from.** The owner failed `hero-04` too: *"audit ảnh mới. màu ảnh vẫn
giả"* — the colour still looks fake. Measured against the owner's own corpus of 131 reference
stills, `hero-04` was already inside the band on colour, warm cast and white point. What is left
is elsewhere, and this set separates the two candidates.

| what changed in `hero-04` | measured | still wrong |
|---|---|---|
| neutral light and grade | warm cast fell from 33–58 to 10–29, white drift to about 0 | — |
| colour from more than one family | colourfulness 31–54, inside the corpus band of 22–82 | it bought the colour with **props**: a red tea towel, blue cabinets, a scatter of coloured cushions in four of six frames |
| the band above the head | held in five of six | — |
| a real photograph | — | texture 14–22 against the corpus median of 22, and the frames run darker: value 0.53–0.74 against 0.75 |

**So this set changes two things, one per axis:**
1. **Colour comes from the room, not from props.** No prompt asks for a colour anywhere except on
   the person's clothes.
2. **Half the prompts drop the labels.** Prompts 4, 5 and 6 are the same three scenes written in
   the owner's own feature-image form — one natural paragraph, no labels, ending with the
   instruction's closing sentence. That form is how the owner's reference images were made, and
   it is on trial here exactly as ADR-101 put it on trial for `03-mechanism-signal`.

**Attach the product photo to every prompt.** Twelve of the fifteen hero renders graded so far
came back with a product that is not the product — a cream throw pillow, a drawstring sack, an
extender with no antennas. That is the largest single reason a frame reads as fake, and no
wording fixes it.

| product | attach |
|---|---|
| Ergonomic Memory Foam Seat Cushion | one of the page's six reference photos |
| WiBoofy AC1200 Wi-Fi extender | `wiboofy-final-product-type 2/assets/gallery-1-product.jpg` |
| Hivefold beeswax bread bag, set of 2 | `t2-eco-final-product-type/assets/photo-1-set.jpg` |

---

## The fields

| # | form | page or template | field | scene |
|---|---|---|---|---|
| 1 | labelled — **CONTROL** | `pdp-dr-seat-cushion-l-shaped-v08` | `hero.image` | a man at his desk, seated on the cushion |
| 2 | labelled | `wiboofy-final-product-type 2` | `hero.background` | a couple on the sofa, the extender plugged in beside them |
| 3 | labelled | `t2-eco-final-product-type` | `hero.image` | a man putting a loaf into the bag at the table |
| 4 | paragraph | `pdp-dr-seat-cushion-l-shaped-v08` | `hero.image` | the same scene as 1 |
| 5 | paragraph | `wiboofy-final-product-type 2` | `hero.background` | the same scene as 2 |
| 6 | paragraph | `t2-eco-final-product-type` | `hero.image` | the same scene as 3 |

Each pair is the same scene, the same room, the same person and the same product. Only the form
of the prompt changes, so the pair answers one question: does the labelled form itself make the
picture look made?

## THE LOCK — the labelled prompts, 1 to 3

| field | the sentence |
|---|---|
| setting | `Setting: a lived-in home where the colours are the room's own.` |
| light | `Light: bright daylight from the left, with natural shadows and real contrast.` |
| grade | `Grade: true colour, neutral whites, no warm filter and no glow.` |
| screens | `Any screen shows only a picture, with no interface, text or numbers.` — prompts 1 and 2 |
| no words | `Nothing in the picture carries a word, a number, a label or a badge.` |
| the corner | `Nothing is placed in the bottom-right corner of the frame.` |

The light and grade lines are the instruction's hero lines, word for word, and so are its six
hero sentences.

## The paragraph prompts, 4 to 6

They carry the same law in prose, and they end with the two sentences the owner's instruction
fixes:

```
Use the attached product photo as the exact reference.
Do not change anything related to the original product, including screen, buttons, display, interface, ports, technical indicators, color, shape, proportions, dimensions, or functionality.
```

They carry no `Setting:`, `Light:` or `Grade:` label, and no product block: that closing sentence
is the instruction's own fidelity clause, which is why ADR-101 allowed the trade for
`03-mechanism-signal`.

## THE CONTROL — prompt 1, predicted **PASS**

`hero-04`'s version of this frame was its best: the placement held, the cushion read whole from
the side, and the colour sat inside the corpus band. The only change is that the room is no
longer asked for colours. If the owner still reads it as fake, the labelled form is the fault,
and prompt 4 is the answer.

**Predictions, written before the render:**
- **Prompt 2:** PASS on colour, PARTIAL on the product: the extender has come back without its
  antennas in every set.
- **Prompt 3:** PASS on colour. The staged red-and-blue kitchen should be gone.
- **Prompts 4 to 6:** unknown, which is the point. Watch whether the paragraph form gives a
  warmer, less arranged picture, and whether it holds the safe box without the sentences being
  listed.

## Watch items

1. **Compare each pair side by side** — 1 with 4, 2 with 5, 3 with 6 — and say which reads as a
   real photograph.
2. **Colour.** It should come from the room itself: wood, plants, fabric, skin. No prop placed
   there to add a colour.
3. **The product.** Exactly its photograph, or the render is a fail whatever else it does.
4. **The safe box.** The group in the right half, a clear band of room above every head.
5. **Texture.** Skin with pores, fabric with weave, no bloom and no haze.
6. **Words.** None anywhere.

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

Setting: a lived-in home where the colours are the room's own.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Any screen shows only a picture, with no interface, text or numbers.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 2 — `06-relief-hero` v1.20 · hero · `hero.background` on `wiboofy-final-product-type 2` · ATTACH 1

```
Photograph of a living room at the back of a house, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

A European couple in their thirties, in a mustard-yellow top and a green shirt, watch a film on a laptop, with a natural, relaxed expression. The Wi-Fi extender is plugged into a wall socket by the sofa, level with their shoulders.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.
Any person turns slightly toward the left side of the picture.

Setting: a lived-in home where the colours are the room's own.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Any screen shows only a picture, with no interface, text or numbers.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 3 — `06-relief-hero` v1.20 · hero · `hero.image` on `t2-eco-final-product-type` · ATTACH 1

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

Setting: a lived-in home where the colours are the room's own.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 4 — `06-relief-hero` v1.20 · hero · `hero.image` on `pdp-dr-seat-cushion-l-shaped-v08` · ATTACH 1 · the paragraph form

```
A North American man in his forties, in a sky-blue shirt, sits at his desk on the cushion in a lived-in home office, seen from the side so the whole cushion reads against a chair of a clearly different tone, working at a laptop whose screen shows only a picture, with a natural, relaxed expression and his body turned slightly toward the left of the picture. He and the cushion sit together in the right half, just past the centre and well clear of the right edge, filling about half the picture's height, with a clear band of room above his head and below his hands, each about a fifth; the left half continues the same room, softly blurred and full of daylight, with nothing in it that matters. Bright daylight comes from the left, with natural shadows and real contrast, and the colours are the room's own, in true colour with neutral whites, no warm filter and no glow. It is a real photograph: skin keeps its texture, with no glow and no haze, nothing in the picture carries a word, a number, a label or a badge, and nothing is placed in the bottom-right corner of the frame.

Use the attached product photo as the exact reference.
Do not change anything related to the original product, including screen, buttons, display, interface, ports, technical indicators, color, shape, proportions, dimensions, or functionality.
```

---

## 5 — `06-relief-hero` v1.20 · hero · `hero.background` on `wiboofy-final-product-type 2` · ATTACH 1 · the paragraph form

```
A European couple in their thirties, in a mustard-yellow top and a green shirt, sit on the sofa of a lived-in living room at the back of a house and watch a film on a laptop whose screen shows only a picture, with a natural, relaxed expression and their bodies turned slightly toward the left of the picture, while the Wi-Fi extender is plugged into a wall socket by the sofa, level with their shoulders. They and the extender sit together in the right half, just past the centre and well clear of the right edge, filling about half the picture's height, with a clear band of room above their heads and below their hands, each about a fifth; the left half continues the same room, softly blurred and full of daylight, with nothing in it that matters. Bright daylight comes from the left, with natural shadows and real contrast, and the colours are the room's own, in true colour with neutral whites, no warm filter and no glow. It is a real photograph: skin keeps its texture, with no glow and no haze, nothing in the picture carries a word, a number, a label or a badge, and nothing is placed in the bottom-right corner of the frame.

Use the attached product photo as the exact reference.
Do not change anything related to the original product, including screen, buttons, display, interface, ports, technical indicators, color, shape, proportions, dimensions, or functionality.
```

---

## 6 — `06-relief-hero` v1.20 · hero · `hero.image` on `t2-eco-final-product-type` · ATTACH 1 · the paragraph form

```
A North American man in his thirties, in a green shirt, folds a crusty loaf into the bread bag on the table of a lived-in kitchen after breakfast, with a natural, relaxed expression and his body turned slightly toward the left of the picture, and no box is in the picture. He and the bag sit together in the right half, just past the centre and well clear of the right edge, filling about half the picture's height, with a clear band of room above his head and below his hands, each about a fifth; the left half continues the same kitchen, softly blurred and full of daylight, with nothing in it that matters. Bright daylight comes from the left, with natural shadows and real contrast, and the colours are the room's own, in true colour with neutral whites, no warm filter and no glow. It is a real photograph: skin keeps its texture, with no glow and no haze, nothing in the picture carries a word, a number, a label or a badge, and nothing is placed in the bottom-right corner of the frame.

Where several reference photos are attached, this image uses the large bag and only that one.
Use the attached product photo as the exact reference.
Do not change anything related to the original product, including screen, buttons, display, interface, ports, technical indicators, color, shape, proportions, dimensions, or functionality.
```
