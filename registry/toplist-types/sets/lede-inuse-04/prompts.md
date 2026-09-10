# `lede-inuse` set 4 — bright, kept, and comfort as a slot of its own

Written against **`lede-inuse` v0.8**. Owner, 2026-09-10, on set 3: *"đặt vị trí vào người đọc, khi
nhìn thấy ảnh sản phẩm đang được sử dụng, đối tượng sử dụng (chủ thể) trong ảnh cần phải thể hiện
được sự tiện nghi, thoải mái, môi trường tươi sáng… ưu tiên nền sáng, tone sáng, tự nhiên, mang lại
cảm giác thoải mái, chân thực (không phải chân thực kiểu đồ vật lộn xộn, cũ)"*.

## What set 3 settled

**The dark-mass hypothesis is dead, killed by its own control.** The clause worked — cell 1 was
written for deep dark and returned median value 0.18 with 45% of pixels below 0.15, cell 5 was
written bright and returned 0.87 / 6%. The control held the old wording, measured 0.67 / 3% / 0.20,
and is the best frame in the set. **A prompt can put the mass of a frame anywhere; dark was the
wrong place to put it.**

Three faults came with it and all three are fixed in the type file rather than here:

- **The anti-method outranks every method.** Cell 5 named the muscles correctly and its `[SUBJECT]`
  line described midday sun and a garment dark with water. The sweat won.
- **A scene object named in ELEMENTS brings its label with it.** Cell 3's binding *no words* lost
  to *a full jar of preserve*, because a jar of preserve has one. Scene objects are now named
  **unlabelled**.
- **`symptom-shaped` products are refused.** A cooling vest works by being wet; so does overheating.

## What this set tests

**One thing: does a bright, kept place plus a named `[COMFORT]` block make a frame a reader wants?**
`[COMFORT]` is new at 0.8 and this is its first outing. Every cell but the control carries one, and
methods 6 and 7's no-face case have moved into it — `evidence` proves the product works, `comfort`
invites the reader in.

| # | product | evidence | comfort | place |
|---|---|---|---|---|
| 1 | electric milk frother | 1 · effect as matter | **face** — muscles named | bright kitchen |
| 2 | ergonomic vertical mouse | 5 · tells of duration | **no face** — hand and place | bright desk |
| 3 | electric wine opener | 2 · the act the problem forbade | **face** — muscles named | bright dining room |
| 4 | mandoline with hand guard | 3 · work only the benefit allows | **no face** — hands and place | bright kitchen |
| 5 | motion-sensor stair light | 7 · the environment witnesses the SOLUTION | **no face** — body and place | **dark — the EXCEPTION** |
| 6 | limescale spray for glass | 4 · comparison as an object | **ABSENT — the CONTROL** | bright bathroom |

**Cell 5 is the owner's own exception, tested.** *"Khi môi trường bắt buộc không tươi sáng cho một
số sản phẩm thì cần thể hiện được việc sản phẩm đã giải quyết được vấn đề."* A stair light's place
cannot be bright; that is the product. So the frame shows the way down already lit and a body
moving easily through it. **The dark is the product's stage, never the reader's experience.** It is
also method 7 done right, after set 3 pointed it at a room full of dust — the environment must
witness the SOLUTION.

**Cell 6 is the control and it differs in exactly one thing: it has no `[COMFORT]` block.** Bright,
kept, a face in frame, and an evidence method already proved twice (de-icer, carpet cleaner), so
nothing else is at risk.

> **Prediction: cell 6 comes back bright and pleasant AS A PLACE, with a neutral face** — the
> default this type has watched four times, at 5 of 6 in set 1 and again in set 2's control. **If
> cell 6's subject reads comfortable anyway, `[COMFORT]` is decoration and a bright kept place is
> the whole rule.**

Predictions for the rest, written before the render:

- **Cells 1–4** — median value above 0.55, dark share under 10%, and all four read comfortable.
- **Cell 5** — dark on the numbers, at or below 0.30 median value, and **reads as ease rather than
  as coping**. If it reads as someone picking their way down a dark stair, the exception clause has
  failed and the type should refuse products whose place cannot be bright.

**Render cell 6 twice.** Set 3 asked for two draws of its control and got one, which is why *bright
is better* stands as a refutation of a prediction rather than as a rule. How a frame is lit and
graded is a REGISTER property, and §*Reading a render* wants the same prompt run more than once.

Six products, none used in any earlier set or round of this namespace. One reference photo each,
one generation call each (ADR-021, ADR-076). Grade full-frame on the calibrated instrument —
median value, share of pixels below 0.15, and **mean** saturation over all pixels, which is what
0.6's table used.

**A comparison's before-half is not the anti-method.** Cell 6 shows a state the product has not
reached yet — scale on the far half of the glass — and that is allowed: the anti-method refuses a
SYMPTOM the body is suffering, not a switchable state on an object. Method 4 has passed twice built
exactly this way.

## Prompt economy — the removal set 3 named is taken here

| set | median | range |
|---|---|---|
| `lede-inuse-02` | 1498 | 1375–1596 |
| `lede-inuse-03` | 1786 | 1510–1842 |
| **`lede-inuse-04`** | **1860** | 1741–1918 |

Set 3 deferred a removal and named it so it would not be forgotten: *the evidence is stated twice
in every cell, once in `[EVIDENCE]` and again as a binding constraint*. **Four such lines are cut
here** — cells 1, 3, 4 and 5 — the ones that restated their `[EVIDENCE]` block and added nothing to
it. Every constraint that adds an EXCLUSION the element does not carry is kept: *the bottle is not
clamped between the knees*, *every fingertip above the blade's path*, *no clawed fingers*. Rule
6.3's own precedent, and nothing earned is dropped. Without it this set would sit at a median of
1921.

**The removal is declared as a variable, not slipped in.** It is graded below at question 13. If
evidence weakens in cells 1, 3, 4 or 5 while cell 6 — which keeps its full pair — holds, the
removal is the first suspect and it goes back. **Cell 6 cannot control both axes at once**: it is
the control for `[COMFORT]` and only incidentally a reference for the duplication, and that limit
is stated rather than papered over.

`[COMFORT]` keeps BOTH statements in every cell that has one. It is the thing under test and it
ships at full strength.

---

## 1 — electric milk frother · effect as MATTER · comfort on a face

**`TYPE: lede-inuse v0.8 — SET 4 CELL 1`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     three-quarter: the head and shoulders, one hand, the frother and a plain glass jug on the worktop.
[EVIDENCE] a standing dome of microfoam risen proud of the jug's rim, fine-bubbled and holding its shape, the milk below it drawn down in a slow vortex.
[COMFORT]  the brow smooth and unfurrowed, the jaw loose with the lips slightly parted, both shoulders dropped well below the collar line, the free hand resting open on the worktop.
[SUBJECT]  an adult making coffee at home in the morning, head tilted a little toward the jug.
[ENVIRONMENT] a kept kitchen — clear pale worktop, one plain white cup set out, everything in good order.
[LIGHT]    a wide window fills the wall behind and the room is bright: pale walls, light wood, clean glass, daylight lying across the worktop, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the jug it is working in are readable.
· The brow is smooth, the jaw loose, both shoulders dropped below the collar line.
· The eyes are open and never find the lens.
· Every object in the scene is plain and unlabelled apart from the product's own printed mark.
· The place is clean, finished and in good repair, and everything in it is in good condition.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 2 — ergonomic vertical mouse · tells of DURATION · comfort with no face

**Second draw of method 5**, after set 3's first drew it in a dark stairwell. Duration is in the
desk, not in the body.

**`TYPE: lede-inuse v0.8 — SET 4 CELL 2`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     close on one hand on the mouse and the desk around it, from mid-forearm to the desk edge.
[EVIDENCE] the afternoon is already spent at this desk — a plain notebook filled to the foot of the page beside it, a drained glass, the chair pushed to its working distance.
[COMFORT]  the wrist flat and unbent with the forearm straight through it, the hand upright and settled on the mouse rather than gripping it, the fingers loose and curved, the shoulder low.
[SUBJECT]  an adult at the end of a long working session, still working.
[ENVIRONMENT] a kept desk — clear surface, cables run out of the way, everything in good order.
[LIGHT]    a window to the left fills the room and it is bright: pale wall, light wood desk, daylight across the whole surface, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the hand on it are readable.
· The wrist is flat and unbent and the forearm runs straight through it.
· The fingers rest curved and loose on the shell — no clawed fingers, no white knuckles.
· No face, no head and no shoulders in the frame.
· Every object in the scene is plain and unlabelled apart from the product's own printed mark.
· The place is clean, finished and in good repair, and everything in it is in good condition.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 3 — electric wine opener · the act the problem FORBADE · comfort on a face

**The test in the picture:** a bottle standing free on the table with one hand on the opener is not
how a weak grip draws a cork — that takes the bottle clamped between the knees or against the body.

**`TYPE: lede-inuse v0.8 — SET 4 CELL 3`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     three-quarter: the head and shoulders, both hands, the opener and the bottle on the table.
[EVIDENCE] the cork is out and riding on the opener's spiral, clear of the neck, and the bottle stands free on the table with two fingertips resting against it.
[COMFORT]  the brow smooth and unfurrowed, the jaw loose, a small smile arriving on its own, both shoulders dropped well below the collar line.
[SUBJECT]  an adult opening a plain unlabelled bottle at a table before a meal, looking at the cork.
[ENVIRONMENT] a kept dining room — a laid table, clean glasses, everything in good order.
[LIGHT]    tall windows fill the room and it is bright: pale walls, light wood, clean glass, daylight across the table, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the bottle neck it is working on are readable.
· The bottle stands on the table under two fingertips — it is not clamped between the knees or held against the body.
· The brow is smooth, the jaw loose, both shoulders dropped below the collar line.
· The eyes are open and never find the lens.
· Every object in the scene is plain and unlabelled apart from the product's own printed mark.
· The place is clean, finished and in good repair, and everything in it is in good condition.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 4 — mandoline with hand guard · work only the BENEFIT allows · comfort with no face

**Second draw of method 3**, whose first was set 2's loose grip on a running breaker.

**`TYPE: lede-inuse v0.8 — SET 4 CELL 4`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     close on both hands, the mandoline and the board beneath it, from wrist to blade.
[EVIDENCE] a stack of paper-thin even slices already fallen below the blade and another leaving it, with the guard holding what is left of the potato square to the cut.
[COMFORT]  the hand on the guard settled flat and loose on top of it, the other hand steadying the frame without tension, the whole action unhurried and repeating.
[SUBJECT]  an adult slicing for supper at a kitchen worktop.
[ENVIRONMENT] a kept kitchen — clear pale worktop, a plain wooden board, everything in good order.
[LIGHT]    a window fills the wall in front and the room is bright: pale walls, light wood, daylight across the board, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the guard riding on it are readable.
· Every fingertip is on top of the guard and above the blade's path.
· No face, no head and no shoulders in the frame.
· Every object in the scene is plain and unlabelled apart from the product's own printed mark.
· The place is clean, finished and in good repair, and everything in it is in good condition.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 5 — motion-sensor stair light · the EXCEPTION · the place cannot be bright

**The owner's own second sentence, tested.** The frame does not get to show a person coping in the
dark; it shows the way down already lit. Method 7, pointed at the SOLUTION this time.

**`TYPE: lede-inuse v0.8 — SET 4 CELL 5`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     from behind and above, mid-back to the treads: the flight below and one foot on it.
[EVIDENCE] every tread down the flight carries a clean warm strip of light along it, the nosings picked out one after another, and the landing at the bottom is fully visible.
[COMFORT]  the foot placed square in the middle of a lit tread, the hand resting along the rail rather than gripping it, the body upright and unhurried, a glass of water carried easily in the other hand.
[SUBJECT]  an adult going down at night for a glass of water.
[ENVIRONMENT] a kept hallway — painted stair, clean runner, a tidy landing below.
[LIGHT]    the stair light is the only light and the frame beyond it is dark, but every tread in use is fully lit and the whole way down is clear.
[GRADE]    natural and true colour, warm, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the treads it is lighting are readable.
· The free hand carries a full glass without spilling it, and the other rests along the rail.
· No face, no head and no shoulders in the frame.
· Nothing in the frame is being felt for, groped after or searched out.
· Every object in the scene is plain and unlabelled apart from the product's own printed mark.
· The place is clean, finished and in good repair, and everything in it is in good condition.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· One person only, and an adult.
```

---

## 6 — limescale spray for glass · COMPARISON as an object · CONTROL, no `[COMFORT]`

**Predicted: bright and pleasant as a place, and a neutral face.** Everything here is written as
cells 1–4 are written except that the `[COMFORT]` block is absent.

**`TYPE: lede-inuse v0.8 — SET 4 CELL 6, CONTROL`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     three-quarter: the head and shoulders and the hand holding the bottle against a shower screen that fills the left of the frame.
[EVIDENCE] the near half of the glass is clear with the tiled wall beyond sharp through it; the far half is still hazed white, and the boundary between them is a hard wet line.
[SUBJECT]  an adult working along that line on a bright morning.
[ENVIRONMENT] a kept bathroom — pale tile, clean fittings, everything in good order.
[LIGHT]    a window fills the wall to the left and the room is bright: pale tile, white fittings, daylight across the glass, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the glass it is working on are readable.
· The two states are on ONE panel of glass, with a hard wet boundary between them.
· There is no second panel, no second room and no before-and-after split.
· The eyes are open and never find the lens.
· Every object in the scene is plain and unlabelled apart from the product's own printed mark.
· The place is clean, finished and in good repair, and everything in it is in good condition.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **Cells 1–4 against cell 6's two draws — does the named `[COMFORT]` block change the subject?** | whether comfort needs a slot, or a bright kept place carries it |
| 2 | **Put yourself in the reader's position on each frame: do you want to be there?** | the owner's own test, and the one that decides |
| 3 | **Cell 5 — ease, or coping?** | the exception clause. If it reads as picking a way down, the type should refuse products whose place cannot be bright |
| 4 | **Is any place shabby, cluttered, unfinished or worn?** | *chân thực* against *đồ vật lộn xộn, cũ*, which set 3 got wrong twice |
| 5 | **Did any prompt describe the problem?** | the anti-method, now ranked above every method after set 3 cell 5 |
| 6 | **Did any scene object arrive carrying print?** | the unlabelled-object fix, after cell 3's jar |
| 7 | **Cell 1 — does the foam stand proud of the rim and hold?** | method 1's fourth draw |
| 8 | **Cell 2 — is the wrist flat, and is the long session visible in the desk?** | method 5's second draw, its first having failed on argument |
| 9 | **Cell 3 — is the bottle standing free? Could a weak grip do that?** | method 2's third draw |
| 10 | **Cell 4 — are the slices thin and even, and every fingertip above the blade?** | method 3's second draw |
| 11 | **Did any frame read as a customer's own photograph?** | the G14 firewall, 18 of 18 across three sets |
| 12 | **Did the prompt's own header print on anything?** | clean in set 3, the first set with the line outside the fence |
| 13 | **Cells 1, 3, 4, 5 — did the evidence still land with its constraint line cut?** | the declared removal. If it weakened while cell 6 held, put the four lines back |

---

## RESULT — rendered 2026-09-10, all six opened and graded under ADR-011

Full finding in `lede-inuse.md` at 0.9. Instrument calibrated first against all four of 0.6's
published rows; saturation is a MEAN over all pixels.

| # | product | medV | dark | sat | verdict |
|---|---|---|---|---|---|
| 1 | milk frother | 0.64 | 2% | 0.18 | **partial** — bright kitchen and a foam dome that holds, and the face is a half-grimace with the free hand splayed palm-up |
| 2 | vertical mouse | 0.67 | 10% | 0.28 | **partial** — wrist flat, duration in the desk, comfort reads; a spread of invented handwriting fills a third of the frame |
| 3 | wine opener | 0.73 | 18% | 0.27 | **pass** — the best expression this type has produced, a small unforced smile, and the unlabelled bottle worked |
| 4 | mandoline | 0.71 | 4% | 0.26 | **pass** — thin even slices, every fingertip above the blade path |
| 5 | stair light · EXCEPTION | 0.29 | 32% | 0.77 | **pass** — ease, not coping. The exception clause works on its first outing |
| 6 | limescale spray · CONTROL | 0.66 | 2% | 0.17 | **fail** — blank face exactly as predicted, no readable two-state comparison, and the label garbled |

**Prediction by prediction:**

- **Cells 1–4, predicted above 0.55 median value and under 10% dark.** Value 4 of 4. **Dark share 2
  of 4** — cell 2 at 10% and cell 3 at 18%, and cell 3 is one of the passes, so the dark-share half
  of the prediction was measuring nothing worth measuring. It is not carried forward.
- **Cell 5, predicted at or below 0.30 median value and reading as EASE.** 0.29, and it reads as
  ease. **Both halves landed**, and this is the finding of the set: **dark was never the fault.**
  Cell 5 is darker than three of set 3's failures and it is one of the best frames this type has.
- **Cell 6, the CONTROL, predicted bright and pleasant as a place with a NEUTRAL FACE.** Exactly
  that. **`[COMFORT]` is not decoration** — the block is what separates cell 3's smile from cell
  6's blank. **Drawn once again where this file asked for two**, second set running.

**Question 13, the declared removal: vindicated, and the reverse of the cautious guess.** The four
cells whose duplicated evidence constraint was cut all landed their evidence — foam, cork, slices,
lit treads. **Cell 6 kept its full pair and failed on evidence anyway**, returning no legible
two-state boundary. The duplication was doing no work and the four lines stay out.

**What the set could not have predicted, and what the owner named next:** all six subjects arrived
in generic clothes — grey marl tee, grey sweatshirt, plain navy, dark apron, dark tee and joggers,
grey work shirt. **6 of 6**, and the copied `PARTS/subject` had asked for it in writing. Fixed at
0.9 by `PARTS/dress`, with `PARTS/pose` beside it.

**Three text faults, one of them written by me.** Cell 2's notebook was named *filled to the foot of
the page* — an object whose content IS text, asked for in the set that added the unlabelled-object
rule. Cell 6's product label garbled at three words, against a type file that promised two render
clean. Cell 4's mandoline carried a faithful Japanese instruction panel, where G1 beats the label
rule. All three are in SLOT CONSTRAINTS at 0.9.
