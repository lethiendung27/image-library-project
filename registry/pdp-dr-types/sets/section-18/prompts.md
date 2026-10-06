# pdp-dr set section-18 — two feature blocks of the dash cam, three options each

**Type:** `03-spec-overlay` v0.19, written to ADR-136. **Field:** `features.items.*`.
**Page:** `pdp-dr-360-surround-view-4-channel-dash-cam-v01`. **Status: UNCOMMITTED, owner-gated.**

These are **three alternatives for each of two slots**, not a six-frame experiment — the owner
renders all three of a block and picks one. **No control is declared here**, because ADR-136's test
already has one: `sets/section-17/` frame 6 is `section-16`'s construction rebuilt in daylight, and
a second control on a second product would measure the same thing twice.

## Step 0, per block — OBJECT or DELIVERY (ADR-136)

| block | the page prints | kind | what must be photographed |
|---|---|---|---|
| **A** `Locked Crash Clips` · *Integrated G-sensor protects footage immediately upon detected impact.* | a part you cannot photograph doing a thing you cannot photograph | **DELIVERY** | **the moment that gets kept** — the contact itself, with the product present and seeing it |
| **B** `Continuous Video Loop` · *Continuous automatic file cycling maintains uninterrupted daily recording.* | a process inside the storage | **DELIVERY** | **that it is already running, unasked** — and, once, what is already on the card |

Both are hidden states, so ADR-136 decision 6 binds: **the cue is a window onto the hidden state or
the product's own indication, never a symbol of the medium.** That is why no frame carries a loop
arrow, a filmstrip, a memory-card graphic or a bird's-eye composite. A loop arrow would be the
symbol of the medium exactly as `section-16`'s cyan arcs were.

## NO LETTERING, 6 of 6 — and why that is not a lapse

The page prints the block title, the body copy and a pill beside each image. **`section-16` drew
that pill's own string into 11 of 11 frames**, and the owner's verdict was that the words appear far
too often and many images could carry none and still resonate. Counted across his 21 reference
stills: 4 carry a word headline, 8 lead with a figure and its unit, 5 carry an icon with a short
label, **4 carry no lettering at all**.

ADR-136 lets a line in only when a **figure or unit the block's copy does not print** pays for it.
Neither of these blocks has one — the brief's figures (170°, 120°, 1080p, 8 infrared lights, F1.8,
100 g, 3.5 m / 6 m) all belong to other claims, and borrowing the 24-hour parking monitor for a
loop-recording block would be a false claim, since the brief says that mode needs a hardwire kit.
**So the words stay on the page and the pictures do the showing.** Every frame still carries exactly
one cue; a cue is a mark, an icon or the product's own indication, never a caption (ADR-135).

## What anatomy these prompts rely on, and where it comes from

**No photograph of this product is on disk** (ADR-131: six of nine frames once drew the wrong
product from asserted anatomy). These prompts name three things and no more:

| named | source |
|---|---|
| **the hub**, on the windscreen glass | the page's own `product.box.0`, *Main 4-Channel Windscreen Hub* |
| **the rear camera module**, on the rear glass | `product.box.2`, *Rear Camera Module* |
| **its built-in screen** | the brief's AliExpress confirmation of 2026-09-22, *built-in screen*, 3 listings |

Nothing else — no lens count, no housing, no finish, no lamp, no port. **ATTACH THE PRODUCT PHOTO
to all six.** If it has no screen, frames 2, 4, 5 and 6 are rewritten; a 3-camera version without
the rear module takes frame 3 out.

## The six frames

| # | block | art direction | the SUBJECT | the one cue |
|---|---|---|---|---|
| 1 | A | car park, open daylight | the moment of contact, a door edge on the flank | an icon: a closed padlock |
| 2 | A | junction, open daylight | the van crossing the line, shown twice | the product's own indication: screen agrees with window |
| 3 | A | rear window, open daylight | the car behind at the moment it dips | an icon: a shield |
| 4 | B | driveway, bright morning | the recording already running, unasked | the product's own indication: screen agrees with window |
| 5 | B | town street, open daylight | what is already on the card | a window: a disc of an earlier part of the same journey |
| 6 | B | macro on a daylit road | the built-in screen itself | the product's own indication: the screen is the only sharp thing |

Two frames of block A use an icon and two frames of block B use the indication, because these are
alternatives for one slot rather than a set that must span the forms. The events, the places and
the channels differ in every one.

**Watch items**
1. Is the frame's subject the thing the product DELIVERS, or did it slide back to a hand holding a
   product? The second is what ADR-136 was written about.
2. Frames 2, 4 and 6: does the screen carry a plain picture, with no interface, text or numbers —
   and in 2 and 4, is it the SAME thing the window shows?
3. Frame 5: is the disc BESIDE the hub with nothing drawn on the hub, and is what is inside it a
   photograph of the same journey rather than a graphic?
4. `scripts/frame-colour.py`: colourfulness toward the owner's 39.1, value toward 0.46. A cabin
   interior is the easiest place in this library to lose a picture to shadow.
5. Did the renderer invent a lens cluster, a lamp or a second screen the photograph does not show?

---

## `features.items.*` — A · Locked Crash Clips

### 1 — the car-park ding · the padlock · no words

```
Editorial realism product feature image seen from inside a parked car in a daylit open car park, through the driver's window: the door of the red car in the next bay has swung open and its edge is touching the flank, the paint dimpled under it. The hub of the 360 Surround View 4 Channel Dash Cam, mounted on the windscreen glass and running, sits sharp in the near foreground. The subject of this frame is the moment of contact, and the red of that door is the most saturated thing in the picture. One thin white line icon of a closed padlock stands beside the hub, about a tenth of the picture's height, and nothing else is drawn. The hub is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. The art direction is the real place in open daylight, bright enough to read the moulding on the product, and the picture keeps the colour of its own world. Nothing in the picture carries any lettering. Use the attached product photo as the exact reference.
```

### 2 — the van crossing the line · window and screen agree · no words

```
Editorial realism product feature image inside a car stopped at a daylit junction: through the driver's window a white van is drifting across the lane line toward the flank, close enough to fill it, the brake lights of the car ahead burning red beyond. The hub of the 360 Surround View 4 Channel Dash Cam, mounted on the windscreen glass and running, sits sharp in the near foreground, and its built-in screen is carrying the same van, seen from the side channel. The subject of this frame is the van at the moment it crosses the line, shown twice — once through the glass and once on the screen. That agreement between window and screen is the only cue, and nothing is drawn. The hub is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. Any screen shows only a picture, with no interface, text or numbers. The art direction is the real place in open daylight, bright enough to read the moulding on the product, and the picture keeps the colour of its own world. Nothing in the picture carries any lettering. Use the attached product photo as the exact reference.
```

### 3 — the car behind · the shield · no words

```
Editorial realism product feature image seen from inside a car at its rear window in daylight: a blue car a short length behind has its nose dipped under hard braking, its brake lights burning red, sharp through the glass. The rear camera module of the 360 Surround View 4 Channel Dash Cam, mounted on the rear glass and running, sits sharp in the near foreground. The subject of this frame is the car behind at the moment it dips. One thin white line icon of a shield stands beside the module, about a tenth of the picture's height, and nothing else is drawn. The module is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. The art direction is the real place in open daylight, bright enough to read the moulding on the product, and the picture keeps the colour of its own world. Nothing in the picture carries any lettering. Use the attached product photo as the exact reference.
```

---

## `features.items.*` — B · Continuous Video Loop

### 4 — the morning drive · window and screen agree · no words

```
Editorial realism product feature image inside a car pulling out of a driveway on a bright morning, a green hedge and a red front door passing the side window: both of the driver's hands rest on the wheel and nothing is being touched. The hub of the 360 Surround View 4 Channel Dash Cam, mounted on the windscreen glass and running, sits sharp beside the mirror, and its built-in screen is carrying the same street the windscreen shows, framed the same way. The subject of this frame is the recording already running, unasked. That agreement between window and screen is the only cue, and nothing is drawn. The hub is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. Any screen shows only a picture, with no interface, text or numbers. The art direction is the real place in open daylight, bright enough to read the moulding on the product, and the picture keeps the colour of its own world. Nothing in the picture carries any lettering. Use the attached product photo as the exact reference.
```

### 5 — what is already on the card · the disc · no words

```
Editorial realism product feature image inside a car moving along a daylit town street lined with green trees. The hub of the 360 Surround View 4 Channel Dash Cam, mounted on the windscreen glass and running, sits sharp beside the mirror. The subject of this frame is what is already on the card. A clean circular inset, about a third of the picture wide, floats beside the hub in clear air and is joined to it by a thin leader: inside the disc is an earlier part of the same journey, a roundabout under the same daylight, photographed the same way. Nothing is drawn on the hub itself. The hub is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. Any screen shows only a picture, with no interface, text or numbers. The art direction is the real place in open daylight, bright enough to read the moulding on the product, and the picture keeps the colour of its own world. Nothing in the picture carries any lettering. Use the attached product photo as the exact reference.
```

### 6 — the screen itself, macro · no words

```
Editorial realism product feature image framed as a macro inside a car on a daylit road with a green verge beyond the glass. The hub of the 360 Surround View 4 Channel Dash Cam, mounted on the windscreen glass and running, fills a third of the frame. The subject of this frame is its built-in screen: the screen is the only sharp thing in the picture, carrying the road ahead, and the real road beyond the glass falls away soft behind it. That sharpness is the only cue, and nothing is drawn. The hub is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. Any screen shows only a picture, with no interface, text or numbers. The art direction is the real place in open daylight, bright enough to read the moulding on the product, and the picture keeps the colour of its own world. Nothing in the picture carries any lettering. Use the attached product photo as the exact reference.
```

---

## After the render

1. Log six lines in `eval/render-tests.jsonl`, and grade the picture before the prompt that made it
   (ADR-131).
2. `python3 scripts/frame-colour.py` on all six and `python3 scripts/compo-spread.py` on all six,
   beside the owner's 39.1 / 0.46 / 27.4 / 0.33 and his closest pair of 30.3.
3. The question this set answers is narrow: **can a feature frame carry its block with no lettering
   at all?** Grade that first, before anything about the picture's quality.
