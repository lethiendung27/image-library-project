# pdp-dr set section-12 — six overlay forms across nine frames, on three products

**Type:** `03-spec-overlay` v0.13. **Rules under test:** ADR-129 — a set spans the overlay forms,
at least four of six and none more than three times; a feature frame is product-led and often has
no place at all; a headline and a label sit directly on the picture while a figure keeps its FIGURE
CARD (ADR-130, this type's own device, not the gallery's flat chip form) and an icon keeps its box;
a mark may stand in the AIR between the product and its subject. Plus
ADR-128, still binding: no hand closes, presses or holds a clip; nothing is drawn ON a wire, a loom
or a cable; a headline runs between a quarter and a third of the frame's width.
**Status: APPROVED by the owner 2026-10-06 ("cho phép tất cả") and COMMITTED at v0.13. Never rendered at any version.**

**Why this set was rewritten before it was ever rendered.** Its first draft used `tag` nine times
out of nine — a photograph and one line of white text, nine times — and the owner said so:
*"cả 9 prompt đều chỉ trả ra ảnh và 1 dòng chữ trắng, thiếu các loại ảnh khác nhau, các loại visual
khác nhau"*. The type has carried six overlay forms since 0.1 and the instruction spells out what a
feature image may carry; ADR-106 measured the owner's own frames and found the FIGURE the commonest
form of all. The first draft used it zero times.

**Why three products.** A fix re-run on the product that broke proves nothing. One line stays on the
Automotive Circuit Tester — the line whose page still has no usable image — and two lines move to
products the new rules have never been tried on, whose claims have the same shape: *without
choosing*, *without stripping*.

## The nine frames

| # | slot | product | form | register | person |
|---|---|---|---|---|---|
| 1 | `features.items.2` | Automotive Circuit Tester | `icon` | dark seamless studio | — |
| 2 | `features.items.2` | Automotive Circuit Tester | `tag` | under a dashboard | yes |
| 3 | `features.items.2` | Automotive Circuit Tester | `callout` | dark studio | — |
| 4 | `features.items.0` | Smart Automatic Car Battery Charger | `figure` | an engine bay | — |
| 5 | `features.items.0` | Smart Automatic Car Battery Charger | `view` | dark studio macro | — |
| 6 | `features.items.0` | Smart Automatic Car Battery Charger | `icon` | dark seamless studio | — |
| 7 | `features.items.1` | True RMS Digital Multimeter | `mark` | a basement ceiling box | — |
| 8 | `features.items.1` | True RMS Digital Multimeter | `tag` | a wall outlet | yes |
| 9 | `features.items.1` | True RMS Digital Multimeter | `view` | dark studio macro, the control | — |

Six forms, none more than twice. Five frames in a studio against four in a real place, which is the
owner's own 8-to-9 split. Two frames carry a person, which is his 2 of 17. Two frames carry no word
at all, which his corpus does three times.

## THE PRODUCT READING

**Automotive Circuit Tester (34)** — carried from `section-11` unchanged. **PARTS.** The
TRANSMITTER, the box carrying the three-position switch marked TONE / OFF / CONT, a status lamp and
two captive leads ending in one RED and one BLACK alligator clip. The RECEIVER, the pen with the
flexible gooseneck probe, a sensing tip, its own LED work light, a button and a speaker. *The leads
belong to the box. The pen has no leads.* **CONNECTIONS.** RED clip on the circuit being traced,
BLACK on bare metal. The pen connects to nothing; it only listens. **GRIP** (from the brief; no
usage photo on disk, so untested). The box hangs where it was clipped; the pen is held like a pen.
**SEQUENCE.** 1 clip on · 2 switch to TONE · 3 run the tip along the loom · 4 the sound stops at the
fault. **THE INDICATION.** The box's lamp; the pen's sound and its own LED on whatever the tip is
over. **WHAT IT MAKES UNNECESSARY.** Cutting, stripping, unplugging or unwrapping the loom.

**Smart Automatic Car Battery Charger (20).** **PARTS.** One rugged case carrying a display that
shows the detected voltage and the charge stage, and two captive leads ending in one RED and one
BLACK clamp; a mains lead leaves the other end. **CONNECTIONS.** RED clamp on the positive post,
BLACK on the negative post or a ground point, mains lead to a socket. **GRIP** (from the brief; no
usage photo on disk, so untested). Once the clamps are on, the case is set down or hung and no hand
is needed. **SEQUENCE.** 1 clamps on · 2 mains in · 3 the unit decides 6V or 12V by itself · 4 the
display shows the stage and it runs unattended. **THE INDICATION.** The display: the detected
voltage and the stage. **WHAT IT MAKES UNNECESSARY.** Choosing a voltage or a chemistry by hand, a
drawer of separate chargers, and watching it so it does not overcharge.

**True RMS Digital Multimeter (25).** **PARTS.** One body carrying a colour display with a numeric
reading and a bar graph beside it, a rotary dial, a flashlight on the body, and an NCV sensor at the
top edge; two probe leads, one RED and one BLACK, with pointed probes. **CONNECTIONS.** For
non-contact detection *nothing is connected at all* — the top edge is brought near the cable.
**GRIP** (from the brief; no usage photo on disk, so untested). One hand holds the body like a
phone, thumb near the dial; the other steadies the cable or the faceplate. **SEQUENCE.** 1 the dial
to NCV · 2 the top edge near the cable · 3 the screen turns and the alert sounds. **THE
INDICATION.** The screen's colour and its reading, the audible alert, and the body's own flashlight.
**WHAT IT MAKES UNNECESSARY.** Stripping insulation, pulling a conductor out, or touching bare metal
to find out whether a wire is live.

## THE LOCK — stated in identical words wherever it applies

| field | the sentence or clause |
|---|---|
| the cable rule, all nine | `Nothing is drawn on any wire, loom or cable.` |
| no other text, all nine | `Nothing else in the picture carries text.` |
| light, the four real places | `The light is the place's own — a work lamp and the daylight behind it — true colour, neutral whites, no cast over the picture; the colour comes from the scene itself:` |
| light, the five studios | `The light is studio light on a seamless ground — one soft key from the left and a cool rim behind — true colour, neutral whites, no cast over the picture; the colour comes from the product and its own leads.` |
| `tag` | `set once in plain bold white letters directly on the photograph with a soft dark edge, no plate or band behind them, the capitals about a twentieth of the picture's height and the line running between a quarter and a third of its width` |
| `icon` | `Three line icons in thin white strokes, each inside its own rounded square outline, stand in a row across the top of the frame, and under each one its name is set in plain bold white capitals directly on the picture.` |
| `callout` | `Three short labels in plain bold white stand on straight white leader lines, each line ending ON the part it names, set directly on the picture with no plate behind them.` |
| `figure` | `stands inside a drawn card with a thin glowing cyan border and a faint translucent fill, floating in the scene beside the product at about the size of a hand, the figure itself in plain bold white.` |
| `mark` | `A set of concentric arcs in luminous cyan stands in the air between them, each arc thinner than the last, reaching the cable without touching it.` |
| `view` | no drawn word at all: the product's own screen carries the argument |
| reference (G1) | `Use the attached product photo as the exact reference.` — last |

**Predicted.** The two `view` frames should be the safest in the set — one body, its own screen, no
drawn layer and no second object to confuse. `9` is the **control**. The `icon` frames are the first
test of whether this renderer can draw a line icon inside a box without turning it into clip art,
which it failed 3 of 3 the last time a graphic was asked for by name (ADR-125) — the difference now
is that the icon is named as a drawn symbol and the SCENE behind it is a plain studio ground, so
there is nothing for it to sit badly on top of. The `figure` card is the device ADR-128 banned by
accident and the owner's own references use four times.

**Watch items**
1. Count the forms: at least four of six, none more than three times.
2. Is any hand closing, pressing or holding a clip, clamp, plug or connector?
3. Count the clips, clamps and leads against what the product carries. More is a fail.
4. Is anything drawn ON a wire, loom or cable? The arcs in 7 must stand in the AIR.
5. Is a HEADLINE or a LABEL on a plate? Fail. Is the FIGURE in its card and the ICON in its box?
   That is the law now, not a fault.
6. Measure every drawn word with `scripts/text-size.py`: capitals at or over 18 px on a 390-px
   phone, and a headline at or under a third of the frame width.
7. Do the two studio grounds read as seamless, or did the renderer invent a place?

---

## `features.items.2` — Solve Multiple Electrical Faults · Automotive Circuit Tester

### 1 — `icon` · the three faults named, on a studio ground

```
Editorial realism product feature image, a dark seamless studio ground with no place and no person: the Automotive Circuit Tester is presented as a pair — the transmitter, the box carrying the three-position switch and its two captive leads ending in one red and one black alligator clip, lying with its status lamp lit, and the receiver, the pen with the flexible gooseneck probe, lying beside it at a slight angle. Both bodies are razor sharp, the moulding and the printed switch positions legible, and the leads curve away into the dark. Three line icons in thin white strokes, each inside its own rounded square outline, stand in a row across the top of the frame, and under each one its name is set in plain bold white capitals directly on the picture: a blade fuse under the word FUSES, a run of wire under the word WIRES, a battery under the word DRAINS. Nothing is drawn on any wire, loom or cable. Nothing else in the picture carries text. The light is studio light on a seamless ground — one soft key from the left and a cool rim behind — true colour, neutral whites, no cast over the picture; the colour comes from the product and its own leads. Use the attached product photo as the exact reference.
```

### 2 — `tag` · the tip on a closed loom, in the car

```
Editorial realism product feature image, a close macro up under a car's dashboard: a North American man in his fifties, in a navy work shirt, is tracing a circuit with the Automotive Circuit Tester — his left hand lifts a taped loom clear of the bulkhead, the tape unbroken along its whole length, and his right hand holds the receiver, the pen with the gooseneck probe, its sensing tip resting on the tape at one spot. The pen's own LED throws a small hard pool of white light on that spot, and the weave of the tape and the dust on it are razor sharp inside that pool while everything an inch away falls into the dark. The transmitter, the box with the two clip leads, hangs deeper in the dark where it was clipped, its status lamp a small point of red. Nothing in the picture is cut, stripped or unwrapped: every wire stays taped and whole. Nothing is drawn on any wire, loom or cable. The words "Fuses, wires, drains" are set once in plain bold white letters directly on the photograph with a soft dark edge, no plate or band behind them, the capitals about a twentieth of the picture's height and the line running between a quarter and a third of its width. Nothing else in the picture carries text. The light is the place's own — a work lamp and the daylight behind it — true colour, neutral whites, no cast over the picture; the colour comes from the scene itself: the red and black leads, the car's paint, the oil on his knuckles. Use the attached product photo as the exact reference.
```

### 3 — `callout` · the two bodies labelled, on a studio ground

```
Editorial realism product feature image, a dark studio three-quarter view with no place and no person: the Automotive Circuit Tester is presented as a pair on a plain dark ground — the transmitter, the box carrying the three-position switch and its two captive leads ending in one red and one black alligator clip, standing upright with its status lamp lit, and the receiver, the pen with the flexible gooseneck probe, standing beside it with the gooseneck curved toward the camera. Every moulded edge, the printed switch positions and the teeth of both clips are razor sharp. Three short labels in plain bold white stand on straight white leader lines, each line ending ON the part it names, set directly on the picture with no plate behind them: one on the switch, one on the red clip, one on the sensing tip at the end of the gooseneck. Nothing is drawn on any wire, loom or cable. Nothing else in the picture carries text. The light is studio light on a seamless ground — one soft key from the left and a cool rim behind — true colour, neutral whites, no cast over the picture; the colour comes from the product and its own leads. Use the attached product photo as the exact reference.
```

---

## `features.items.0` — Automatic 6V/12V Detection · Smart Automatic Car Battery Charger

### 4 — `figure` · the range in its card, at the car

```
Editorial realism product feature image, a close macro on the inner wing of a car with the bonnet up and no person in frame: the Smart Automatic Car Battery Charger sits on the painted wing beside the battery, its two leads already run to the posts with the red clamp bitten on the positive and the black clamp on the negative, both shut tight, and its mains lead running away off frame. The charger's display and the stage lamps beside it are razor sharp and lit, and the moulding of the case and the dust on the wing are sharp with them. Nothing in the picture is being chosen by hand: there is no switch being moved and no dial being turned, because the unit has already decided. The figure "6V/12V" stands inside a drawn card with a thin glowing cyan border and a faint translucent fill, floating in the scene beside the product at about the size of a hand, the figure itself in plain bold white. Nothing is drawn on any wire, loom or cable. Nothing else in the picture carries text. The light is the place's own — a work lamp and the daylight behind it — true colour, neutral whites, no cast over the picture; the colour comes from the scene itself: the red and black clamps, the car's paint, the battery's casing. Use the attached product photo as the exact reference.
```

### 5 — `view` · its own display, filling the frame

```
Editorial realism product feature image, an extreme close studio macro with no place, no person and no drawn layer: the display of the Smart Automatic Car Battery Charger fills the middle of the frame, lit and reading, the detected voltage and the charge stage shown on its own screen, with the stage lamps burning beside it and the moulded ribs of the case falling away into soft focus on either side. The pixels of the screen, the texture of the moulding and the fine print around the display are razor sharp. The two captive leads leave the bottom of the frame, the red and the black, already run out to a battery beyond it. Nothing in the picture is being chosen by hand: there is no switch being moved and no dial being turned, because the unit has already decided. Nothing is drawn on any wire, loom or cable. Nothing else in the picture carries text. The light is studio light on a seamless ground — one soft key from the left and a cool rim behind — true colour, neutral whites, no cast over the picture; the colour comes from the product and its own leads. Use the attached product photo as the exact reference.
```

### 6 — `icon` · the three machines it replaces

```
Editorial realism product feature image, a dark seamless studio ground with no place and no person: the Smart Automatic Car Battery Charger stands alone in the middle of the frame, three-quarter on, its display lit and reading, its two captive leads ending in one red and one black clamp curving away to either side and its mains lead behind. The case's moulded ribs, the fine print around the display and the jaws of both clamps are razor sharp. Three line icons in thin white strokes, each inside its own rounded square outline, stand in a row across the top of the frame, and under each one its name is set in plain bold white capitals directly on the picture: a car under the word CAR, a motorcycle under the word BIKE, a ride-on mower under the word MOWER. Nothing in the picture is being chosen by hand: there is no switch being moved and no dial being turned, because the unit has already decided. Nothing is drawn on any wire, loom or cable. Nothing else in the picture carries text. The light is studio light on a seamless ground — one soft key from the left and a cool rim behind — true colour, neutral whites, no cast over the picture; the colour comes from the product and its own leads. Use the attached product photo as the exact reference.
```

---

## `features.items.1` — Non-Contact Voltage Detection · True RMS Digital Multimeter

### 7 — `mark` · the sensing field, standing in the air

```
Editorial realism product feature image, a close macro at an open ceiling-rose box in a basement, no person in frame: the True RMS Digital Multimeter — the body with the colour display, the rotary dial and the sensor at its top edge — is clamped in a small stand with that top edge held a finger's width from a grey cable that is whole and unstripped, and the cable runs away into the joists behind. Nothing touches the cable. The colour display is razor sharp and has turned, its reading and the bar graph beside it clear. A set of concentric arcs in luminous cyan stands in the air between them, each arc thinner than the last, reaching the cable without touching it. Nothing in the picture is stripped, cut or pulled out: every conductor stays inside its sheath. Nothing is drawn on any wire, loom or cable. Nothing else in the picture carries text. The light is the place's own — a work lamp and the daylight behind it — true colour, neutral whites, no cast over the picture; the colour comes from the scene itself: the red and black probe leads, the cable's grey sheath, the raw joists. Use the attached product photo as the exact reference.
```

### 8 — `tag` · the same step at a wall outlet, from her eye

```
Editorial realism product feature image, a close over-the-shoulder view down at a wall outlet with its cover plate off: a North American woman in her forties, in a grey work shirt with the sleeves turned back, holds the True RMS Digital Multimeter — the body with the colour display, the rotary dial and the sensor at its top edge — with that top edge held close to the outlet's terminals, and her left hand rests on the wall beside it. Nothing touches the terminals: there is a finger's width of air between the meter's top edge and the metal. Her face is sharp and lit from below by the colour display, which has turned and shows its reading and the bar graph beside it. Nothing in the picture is stripped, cut or pulled out: every conductor stays inside its sheath. Nothing is drawn on any wire, loom or cable. The words "It knows without touching" are set once in plain bold white letters directly on the photograph with a soft dark edge, no plate or band behind them, the capitals about a twentieth of the picture's height and the line running between a quarter and a third of its width. Nothing else in the picture carries text. The light is the place's own — a work lamp and the daylight behind it — true colour, neutral whites, no cast over the picture; the colour comes from the scene itself: the red and black probe leads, the painted wall, the outlet's cream plastic. Use the attached product photo as the exact reference.
```

### 9 — `view` · the screen itself · **CONTROL**

```
Editorial realism product feature image, an extreme close studio macro with no place, no person and no drawn layer: the colour display of the True RMS Digital Multimeter fills the middle of the frame, lit and turned, the numeric reading large on it and the analogue bar graph running beside it, with the rotary dial's detents and the moulded shoulder of the body falling away into soft focus around it. The pixels of the screen, the fine print on the dial and the texture of the rubber over-moulding are razor sharp. The two probe leads, one red and one black, leave the bottom of the frame coiled and unused, because this mode needs neither. Nothing in the picture is stripped, cut or pulled out: every conductor stays inside its sheath. Nothing is drawn on any wire, loom or cable. Nothing else in the picture carries text. The light is studio light on a seamless ground — one soft key from the left and a cool rim behind — true colour, neutral whites, no cast over the picture; the colour comes from the product and its own leads. Use the attached product photo as the exact reference.
```
