# pdp-dr set hero-10 — three heroes for the 360 Surround View 4 Channel Dash Cam

**Type:** `06-relief-hero` v1.20, the LP2 copy, commercial register, no inset. **Field:**
`hero.image`. **Page:** `pdp-dr-360-surround-view-4-channel-dash-cam-v01` (export of 2026-09-10,
`lpTypeId: pdp_dr`), whose hero reads *The Blind Angle Trap* — a standard windscreen camera sees
only straight ahead, so a side swipe, a tight parking scrape or a rear impact captures nothing
useful. **Render at 16:9; the template crops it into a banner.**
**Status: UNCOMMITTED, owner-gated.**

## NO PRODUCT PHOTOGRAPH IS ON DISK, and these prompts are written to survive that

ADR-131 is the reason this section exists: six of nine frames once drew the wrong product because
a prompt asserted anatomy nobody had seen. **So nothing here describes the product's shape, colour,
buttons, lenses or housing.** The prompts name only the two parts the page's own `product.box`
names:

| the page says | these prompts say |
|---|---|
| `Main 4-Channel Windscreen Hub` | **the hub**, on the windscreen glass |
| `Rear Camera Module` | **the rear camera module**, on the rear window |

The mandated product block carries the rest — *preserve its shape, proportions, construction,
seams, surface texture, finish and colour exactly* — and the attached photograph is what tells the
renderer what that is. **ATTACH IT TO ALL THREE.** If it shows a different construction, say so
and the three are rewritten around what it does have.

**No screen is drawn on the product.** The page never gives the unit a display: its three steps end
*Pair via built-in WiFi to inspect live streams... and pull clips directly to your phone*, so the
VIEW lives on the phone. G6's sentence rides in prompts 1 and 2 because a cabin has an infotainment
screen in it whether the prompt asks for one or not.

## What a hero of this product may not do

**A hero carries no words, no marks and no inset** (`registry/pdp-dr-instruction.md`, *The hero*).
So the four channels, the surround composite, the blind angle and the G-sensor **are not drawn
here** — no bird's-eye overlay, no coverage wedge, no split. Every one of those is an argument, and
arguments belong to the feature images. What the hero shows is the system **in place on the glass
with the real surroundings visible through it**, which is the resolved state the page sells.

## And the clauses ADR-136 measured this morning, which a hero obeys too

- **No dark frame.** All three are daylight. A cabin interior is the easiest place in this library
  to lose a picture to shadow: `section-16`'s two worst-textured frames, **6.6 and 9.2 against the
  owner's 27.4**, were both dark.
- **The colour comes from what the place already holds** (ADR-108, ADR-119) — the street through the
  glass, the car behind, the jacket and the sleeves. **One clear colour each and they differ**:
  mustard-yellow, sky-blue, a red hatchback. No beige, no charcoal, no grey on grey.
- **The product is READABLE, not necessarily the largest** (ADR-136 decision 2). The hub is small
  and the law's floor is about an eighth of the width, so each prompt says where across the picture
  it sits — *two thirds across* — rather than leaving it to the fixed sentence's *just past the
  centre*, which returned 50% on `hero-07` and lost the box by five points.

| # | construction | the clear colour | where | predicted |
|---|---|---|---|---|
| 1 | a man chest-up setting the hub, face in frame | mustard-yellow jacket | the front cabin | **PASS** — the control |
| 2 | two hands at the glass, no face | sky-blue sleeves | the windscreen, beside the mirror | **PASS** |
| 3 | the rear module, camera level, a hand from the right | a red hatchback behind | the rear window | **PARTIAL** — the product-forward construction has failed twice |

**Watch items**
1. Open each render **as the 3:1 banner** first: the centre 59.3% of the height, the left 45% under
   the page's words.
2. Is any face, hand or part of the product inside the top third or the bottom third?
3. Is the hub between 55% and 86% across and 28% and 72% down, and is it still recognisable at
   390 px?
4. Did the renderer invent a display, a lens cluster or a second body the photograph does not show?
5. Prompt 3: is the car behind sharp through the glass, and is it the only saturated thing?

---

## 1 — `06-relief-hero` v1.20 · `hero.image` · ATTACH 1 · **CONTROL, predicted PASS**

```
Photograph inside a car, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

The headliner spans the top, the dashboard the bottom: a North American man in a mustard-yellow jacket, chest-up, sets the hub on the glass two thirds across. His expression is relaxed.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about a third of the picture's height and sits across the middle, with the place itself — a ceiling, a wall, a floor, a table — filling the whole of the top third and the whole of the bottom third.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.
Any person turns slightly toward the left side of the picture.

Setting: a car's front cabin where the colours are the cabin's own.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Any screen shows only a picture, with no interface, text or numbers.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 2 — `06-relief-hero` v1.20 · `hero.image` · ATTACH 1 · no face · predicted PASS

```
Photograph inside a car at the windscreen, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

From the passenger seat, the headliner spans the top, the dashboard the bottom: two sky-blue sleeves hold the hub against the glass two thirds across, beside the mirror, a sunlit street beyond. No face is in frame.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about a third of the picture's height and sits across the middle, with the place itself — a ceiling, a wall, a floor, a table — filling the whole of the top third and the whole of the bottom third.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.

Setting: a car's front cabin where the colours are the cabin's and the street's own.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Any screen shows only a picture, with no interface, text or numbers.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## 3 — `06-relief-hero` v1.20 · `hero.image` · ATTACH 1 · product forward · predicted PARTIAL

```
Photograph at a car's rear window, one frame, no panels, no insets, no words.

Use the attached product photo as the exact reference. Preserve its shape, proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent.

The camera is level with the glass, the rear headliner spanning the top and the parcel shelf the bottom: a hand from the right steadies the rear camera module on the window two thirds across, and a red hatchback follows a car's length behind, sharp through the glass. No face is in frame.

The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.
The group fills about a third of the picture's height and sits across the middle, with the place itself — a ceiling, a wall, a floor, a table — filling the whole of the top third and the whole of the bottom third.
The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.
The product is big enough to recognise at a glance, never a small detail in the distance.
It is a real photograph: skin keeps its texture, with no glow and no haze.

Setting: a car's rear cabin where the colours are the cabin's and the road's own.
Light: bright daylight from the left, with natural shadows and real contrast.
Grade: true colour, neutral whites, no warm filter and no glow.
Nothing in the picture carries a word, a number, a label or a badge.
Nothing is placed in the bottom-right corner of the frame.
```

---

## After the render

1. Open each one as the **3:1 banner** before grading it, and log three lines in
   `eval/render-tests.jsonl` with the placement read off that crop (ADR-011, ADR-123).
2. `python3 scripts/frame-colour.py` on all three, beside the owner's band — colourfulness 39.1,
   value 0.46, texture 27.4, saturation 0.33.
3. `python3 scripts/compo-spread.py` on all three: no pair under 25.
