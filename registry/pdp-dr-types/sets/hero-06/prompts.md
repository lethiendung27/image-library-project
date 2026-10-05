# pdp-dr set hero-06 — one hero prompt, on a product the law has never seen

**What this is.** One prompt, at the owner's request, to see the hero law work on a fresh
product: the **Furniture Lifting Tool Set** from
`Product Input 8 Sep/11-fill-inputs-furniture-lifting-tool-set.csv`. **Type:** `06-relief-hero`
v1.20, the LP2 copy, commercial register, no inset. **Status: UNCOMMITTED, owner-gated.**

**Rule under test:** the hero section of `registry/pdp-dr-instruction.md` as ADR-108 left it, in
the labelled form — the form the law still names. `hero-05` is what answers whether the owner's
own paragraph form does better, and this prompt deliberately does not mix that question in.

**Attach the product photo.** The brief carries no image, so this prompt only runs if the owner
attaches one photo of the set. Twelve of the fifteen hero renders graded so far came back with a
product that is not the product, every one of them from a prompt whose photo did not reach the
render.

**Where it would sit:** the hero of `t1-deal-final-product-type 2`, field `hero.image`. That
template is the generic deal page, and its hero block crops as every other one does.

---

## What the brief gives, and what the frame takes from it

| the brief says | the frame |
|---|---|
| "a long lever that raises one corner of the furniture, and four sliders that go underneath to take the weight" | the lever in her hand, the sliders under the near corners |
| "a single person can lift and shift items that would otherwise need two people" | she is alone, and the piece has already moved |
| "Dust and allergens build up behind the fridge, the washer and the cabinets" | the gap she has opened behind a tall bookcase, with the skirting board visible |
| persona: homeowners and renters 30–65, and adult children buying for older parents | a woman in her fifties, at ease, not straining |
| "every attempt ends in a screeching drag across the hardwood" | a wood floor, unmarked |

**What the frame does not take:** no strain, no before-and-after, no second person, and no word
anywhere. A hero is the state after buying, so the heavy thing has already moved.

## The lock

| field | the sentence |
|---|---|
| setting | `Setting: a lived-in home where the colours are the room's own.` |
| light | `Light: bright daylight from the left, with natural shadows and real contrast.` |
| grade | `Grade: true colour, neutral whites, no warm filter and no glow.` |
| no words | `Nothing in the picture carries a word, a number, a label or a badge.` |
| the corner | `Nothing is placed in the bottom-right corner of the frame.` |

The light and grade lines are the instruction's hero lines, word for word, and so are its six
hero sentences.

**One sentence this set adds, which no hero prompt has carried before:** the set is two parts and
the sliders appear four times, so the prompt carries the instruction's conditional sentence for a
product in frame more than once.

```
Wherever the product appears more than once in this image it is identical in every instance.
```

## The prediction, written before the render

**PARTIAL.** Three things are new at once and each can miss:
- **The product is a set**, and a set is where a renderer invents a fifth piece or draws two
  sliders unlike each other. The conditional sentence is there for exactly that.
- **The sliders sit on the floor**, which is the bottom fifth the band sentence keeps clear. They
  are placed under the near corners, in front of her feet rather than at the frame's edge, and
  whether that reads is the thing to look at.
- **The lever is long**, so it can easily leave the safe box on the right.

What should hold, because it has held twice: the band of room above her head, and the group in
the right half.

## Watch items

1. **The product.** Exactly its photograph: one lever, four sliders, all four alike, nothing
   added.
2. **The safe box.** Her head clear of the top fifth, the sliders clear of the bottom fifth, the
   lever inside the right half.
3. **The state.** The bookcase has already moved and she is not straining. No second person.
4. **Colour.** From the room itself, nothing placed there to add a colour.
5. **The floor.** Wood, unmarked: the brief's fear is a screeching drag across the hardwood.
6. **Words.** None anywhere.

---

## 1 — `06-relief-hero` v1.20 · hero · `hero.image` on `t1-deal-final-product-type 2` · ATTACH 1 · **CONTROL, the only prompt, predicted PARTIAL**

```
Photograph of a living room where a bookcase has just been moved, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.
Wherever the product appears more than once in this image it is identical in every instance.

A European woman in her fifties, in a teal jumper, stands by the bookcase with the lifting lever in her hand and a natural, relaxed expression. The sliders are under its near corners on bare wood.

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
