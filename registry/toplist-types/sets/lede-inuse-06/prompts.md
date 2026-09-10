# `lede-inuse` set 6 — every case this type carries, in one set

Written against **`lede-inuse` v0.10**. Owner, 2026-09-10: *"hãy tạo set 6 với tất cả các trường hợp
của lede inuse để tôi test"*, and *"luôn sử dụng người phương tây, châu âu, da màu, da trắng, không
dùng châu á"*.

## What this set is, and what it is not

**This is a COVERAGE set, not an experiment.** Sets 1–5 each moved one variable against a control.
This one puts every case the type declares into the frame at least once, so the owner can see the
whole surface. **Its limit is stated up front: with ten different cases, a failure in one cell
cannot be attributed the way a controlled set attributes it.** What it can do is find which cases
are broken at all — three of them have never been rendered.

**Two cells are still a proper control**, because the gaze failure of set 5 needs settling and it is
cheap to settle here.

## What set 5 settled

**`[DRESS]` works, 4 of 4, against a control drawn twice that came back plain both times** — an
olive linen shirt and an oatmeal knit against a multicoloured print scarf, a houndstooth shirt, an
indigo quilted jacket and a printed shirt over a striped knit. **And the two identical control draws
disagreed about the EVIDENCE while agreeing about the dress**, which is why the dress result is a
rule and why a single draw could not have told you either thing.

**The gaze gate broke 2 of 6, clean 24 of 24 before it.** Both failures took *a half-turn to look
back* from `[POSE]`'s open range. **Turning back is looking at something and the nearest something
is the lens.** The repair at 0.10 is the option list, never the openness — the same open range
produced the wall lean and the greenhouse lean in the two frames that passed.

## The cases

| # | case | product | face |
|---|---|---|---|
| 1 | `evidence` **1 · effect as matter or light** | cordless glue gun | face |
| 2 | `evidence` **2 · the act the problem forbade** | folding step stool | face |
| 3 | `evidence` **3 · work only the benefit allows** | silicone oven mitts | no face |
| 4 | `evidence` **4 · comparison as an object** | long-reach window cleaning pole | no face |
| 5 | `evidence` **5 · tells of duration and quantity** | rolling laundry basket | face |
| 6 | **the LIGHT EXCEPTION** — the place cannot be bright | rechargeable underhood work light | no face |
| 7 | product class **worn-external** | carpenter's tool belt | face |
| 8 | product class **conforming or enclosed → the PACKAGE in frame** | shoe insoles | no face |
| 9 | **`presentation`** — the photograph inside a DESIGNED object | beeswax food wraps | no face |
| 10 | **`gaze: reflect`** — the subject on their own image in glass | mirror demister pad | face |
| 11 | **CONTROL, draw 1 of 2** — keeps set 5's turn-back pose option | fabric shaver | face |
| 12 | **CONTROL, draw 2 of 2** — identical to cell 11 | fabric shaver | face |

**Three of these have never been rendered by this type.** Cell 8 is the `conforming or enclosed`
route the file has described since 3.5 and never drawn: an insole is invisible inside a shoe, so the
product enters as its package. Cell 9 is `presentation`, which landed 2 of 2 in set 1 and has not
been drawn since. Cell 10 is `gaze: reflect`, an existing value of the shared axis with zero
renders here — and it is what this type's only corpus MATCH does.

**Cells 11 and 12 are the control and they are two cells, not one cell rendered twice.** Sets 3 and
4 each asked for a second draw and each got one; set 5 built the repeat into the cell list and got
it. That is kept.

> **Prediction: cells 11 and 12 both come back with the subject looking into the lens**, because
> they alone keep *a half-turn to look back* in the pose range. **If they do not, the 0.10 diagnosis
> is wrong** and the gaze failure came from somewhere else — the full-length standing framing is the
> other suspect, and it would then be the thing to fix.

Predictions for the rest, written before the render:

- **Cells 1–10 keep their eyes off the lens.** The turn-back option is gone from all ten.
- **Casting holds 12 of 12** — `[CASTING]` is named in every cell, and set 5 showed an unnamed
  casting slot taking its own default.
- **Cell 8 is the one most likely to fail**, and the failure mode is named in advance: the package
  becomes the subject and the frame turns into a packshot, which `BOUNDARY` sends to `lede-winner`.
- **Cell 9's designed mat lands** — 2 of 2 in set 1, and this is its third and fourth draw of
  evidence.

Eleven products, none used in any earlier set or round of this namespace. One reference photo each,
one generation call each (ADR-021, ADR-076). Grade on the calibrated instrument — median value,
share of pixels below 0.15, and **mean** saturation.

## Prompt economy — the longest set this type has shipped, and it is at the ceiling

| set | median | range |
|---|---|---|
| `lede-inuse-04` | 1860 | 1741–1918 |
| `lede-inuse-05` | 2236 | 1984–2395 |
| **`lede-inuse-06`, first draft** | **2479** | 2390–2585 |
| **`lede-inuse-06`, shipped** | **2398** | 2292–2487 |

**Four prompts of the first draft went over Rule 6's 2500 ceiling and the gate fired**, as it did on
set 5's draft. The cause is the same and it is now a pattern worth naming rather than fixing twice:
**every clause this type has added since 0.8 was earned, and none of them replaced anything.**
`[COMFORT]`, `[POSE]`, `[CONDITION]`, `[DRESS]` and now `[CASTING]` are five new blocks in three
versions, and the shared CONSTRAINTS list has not lost a line in the same span.

Cut to get under: the product-reference block, the dress line, the clothing refusal, the comfort
range from four options to three, and cell 8's two overlapping package constraints merged into one.

**This set sits 100–200 characters below the ceiling and that is not a comfortable place to be.**
The next set cannot add a block without removing one. **The merge deferred at set 5 is now the
obvious candidate and its evidence is in**: `[POSE]` and `[COMFORT]` both landed as separate slots,
so merging them into one `[EASE]` block risks little and is worth roughly 120 characters. It is not
done here only because this set already carries ten cases and a merge would be an eleventh change.

**Four deliberate departures from the shared wording, so a grader does not read them as slips.**
Cell 9 drops *no drawn element of any kind*, because a designed mat IS a drawn element and is the
case being tested. Cells 3, 4, 6, 8 and 9 carry no face, so their ease floor reads *in the body or
the hands* where the face cells read *on the face or the shoulders*. Cell 10 adds *no phone at a
mirror* to the photographer line, because a person at a mirror is the exact frame G14 refuses and it
is the only cell that goes near it. And the *two states on ONE …* line names its own object in
cells 4, 10 and the control — pane, mirror, sleeve — as the product-readability line always has.

---

## 1 — cordless glue gun · effect as MATTER

**`TYPE: lede-inuse v0.10 — SET 6 CELL 1`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     three-quarter, head to bench: the person, the gun in one hand, the work in front of it.
[EVIDENCE] a clean bead of hot glue laid along the joint and still glossy, a fine thread of it drawn out behind the nozzle, and the two pieces already closed on the bead further back.
[COMFORT]  the ease is real, its form yours — a breath going out, the eyes creasing, a small smile arriving on its own. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: weight settled on one hip, a lean over the bench, the free hand resting flat on the wood.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult mending a wooden box at a workbench on a bright morning.
[ENVIRONMENT] a kept workshop — swept floor, tools racked, the bench clear around the work.
[CONDITION] the product is clean and as-new.
[LIGHT]    a wide window fills the wall beside the bench and the room is bright: pale walls, light timber, daylight across the benchtop, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the joint it is working on are readable.
· The bead is glossy and freshly laid, with a fine thread drawn out behind the nozzle.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening on the face or the shoulders.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· The eyes are open and never find the lens.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 2 — folding step stool · the act the problem FORBADE

**The test in the picture:** reaching the top shelf flat-footed from a stable step is not what a bad
back does. It stretches, or it climbs on a chair.

**`TYPE: lede-inuse v0.10 — SET 6 CELL 2`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     three-quarter, head to floor: the person standing on the stool, the shelf they are reaching, the room around.
[EVIDENCE] both feet flat and square on the step and the top shelf at chest height — a stack of bowls coming down two-handed, with no stretch in the arms and no chair dragged over.
[COMFORT]  the ease is real, its form yours — a breath going out, the eyes creasing, a small smile arriving on its own. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: weight even on both feet, a lean in toward the shelf, the head tipped up to the top row.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult fetching bowls down from a high cupboard on a bright morning.
[ENVIRONMENT] a kept kitchen — clear pale worktop, cupboards in order, a swept floor.
[CONDITION] the product is clean and as-new.
[LIGHT]    a wide window fills the wall behind and the room is bright: pale walls, light wood, clean glass, daylight across the floor, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the feet standing on it are readable.
· Both feet are flat and square on the step, and the shelf is at chest height — not overhead, not stretched for.
· There is no chair, no ladder and nothing else being stood on anywhere in the frame.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening on the face or the shoulders.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· The eyes are open and never find the lens.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 3 — silicone oven mitts · work only the BENEFIT allows · no face

**`TYPE: lede-inuse v0.10 — SET 6 CELL 3`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     close on both mitted hands, the pan they are carrying and the worktop below, from forearm to work.
[EVIDENCE] both hands closed right around the bare iron handles of a heavy casserole straight from the oven — a full grip, fingers wrapped, the lid still steaming — where a cloth would be pinched and slipping.
[COMFORT]  the ease is real, its form yours — the fingers wrapped and unhurried, the wrists level, the shoulders low, the carry steady and slow. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: a lean in over the worktop, weight settled on one hip, the elbows loose.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult setting a casserole down on the worktop on a bright morning.
[ENVIRONMENT] a kept kitchen — clear pale worktop, a plain wooden trivet set out, everything in order.
[CONDITION] the product is clean and as-new.
[LIGHT]    a wide window fills the wall behind and the room is bright: pale walls, light wood, clean glass, daylight across the worktop, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the iron handles inside it are readable.
· Each hand is closed fully around a handle — fingers wrapped, not pinched, not held at the fingertips.
· The pan is plainly hot: the lid is steaming.
· No face, no head and no shoulders in the frame.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening in the body or the hands.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 4 — long-reach window cleaning pole · COMPARISON as an object · no face

**`TYPE: lede-inuse v0.10 — SET 6 CELL 4`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     from the ground looking up: the pole running out of frame at the bottom, the head against an upstairs pane, the wall around it.
[EVIDENCE] one upstairs window with the near half squeegeed clear and the sky reflecting cleanly off it, the far half still grey and streaked, and a hard wet line between the two where the head has stopped.
[COMFORT]  the ease is real, its form yours — the hands loose on the shaft, the arms low and unstretched, the stance settled, the reach unhurried. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: weight settled on one hip, both feet flat on the path, the elbows low.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult doing the upstairs windows from the ground on a bright morning.
[ENVIRONMENT] a kept house front — clean render, a swept path, a tidy border below the wall.
[CONDITION] the product is clean and as-new.
[LIGHT]    open daylight and the frame is bright: pale render, clean glass, a light sky, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the pane it is working on are readable.
· The two states are on ONE pane, with a hard wet line between the clear half and the grey half.
· There is no ladder and no second window being compared.
· No face, no head and no shoulders in the frame.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening in the body or the hands.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 5 — rolling laundry basket · tells of DURATION and QUANTITY

**`TYPE: lede-inuse v0.10 — SET 6 CELL 5`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     three-quarter, head to floor: the person, the basket beside them, the hallway behind.
[EVIDENCE] the basket is loaded to the brim with folded laundry and the line outside the window behind is already empty — a whole wash taken in and folded, standing on its own wheels rather than carried.
[COMFORT]  the ease is real, its form yours — a breath going out, the eyes creasing, a small smile arriving on its own. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: two fingers on the handle, weight settled on one hip, the free arm hanging loose.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult wheeling the folded wash back through the house on a bright morning.
[ENVIRONMENT] a kept hallway — clear floor, a runner straight, everything in order.
[CONDITION] the product is clean and as-new.
[LIGHT]    a tall window fills the end of the hallway and it is bright: pale walls, light wood floor, daylight down the length of it, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the folded load standing in it are readable.
· The basket is full to the brim and the line outside the window is empty.
· The hand on the handle is loose — the basket is being wheeled, not lifted or dragged.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening on the face or the shoulders.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· The eyes are open and never find the lens.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 6 — rechargeable underhood work light · the LIGHT EXCEPTION · no face

**Second draw of the exception**, whose first was the stair light and passed. The frame does not get
to show anyone working in the dark: the work is already lit.

**`TYPE: lede-inuse v0.10 — SET 6 CELL 6`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     close over the wing of a car at night: the open bonnet, the light hooked under it, the engine bay below.
[EVIDENCE] the whole engine bay is lit flat and even under the hooked light — every hose, cap and clip picked out, no shadow anywhere in the bay — and both hands are free on the work with nothing being held up to see by.
[COMFORT]  the ease is real, its form yours — the hands working unhurried, the shoulders low, the reach easy, nothing being felt for. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: leaning in over the wing on both forearms, weight settled on one hip.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult changing a filter after dark.
[ENVIRONMENT] a kept garage — swept floor, tools racked on the wall, the bench clear behind.
[CONDITION] the product is clean and as-new.
[LIGHT]    the work light is the only light and the garage beyond is dark, but the engine bay is fully and evenly lit and every part of the work is clear.
[GRADE]    natural and true colour, warm, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the engine bay it is lighting are readable.
· The bay is lit evenly with no dark corner in it, and both hands are free on the work.
· Nothing in the frame is being felt for, groped after or held up to see by.
· No face, no head and no shoulders in the frame.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening in the body or the hands.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 7 — carpenter's tool belt · product class WORN-EXTERNAL

**`TYPE: lede-inuse v0.10 — SET 6 CELL 7`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     three-quarter, head to thigh: the person, the belt worn at the hip, the frame they are working on.
[EVIDENCE] a row of studs already fixed along the wall behind and the last nail going in, with every tool for it drawn straight off the hip — hammer out, tape and square still in their loops, nothing set down on the floor.
[COMFORT]  the ease is real, its form yours — a breath going out, the eyes creasing, a small smile arriving on its own. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: weight settled on one hip, a lean along the frame, the free hand hooked in the belt.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult framing a stud wall on a bright morning.
[ENVIRONMENT] a kept site room — swept floor, offcuts stacked, timber racked against the wall.
[CONDITION] the product is clean and as-new.
[LIGHT]    a wide window fills the wall opposite and the room is bright: pale plaster, fresh timber, daylight across the frame, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is worn on the body as the outermost layer, and both it and the hip it sits on are readable.
· Every tool in use comes off the belt: the loops are filled and nothing is set down on the floor.
· The row of studs already fixed is visible behind.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening on the face or the shoulders.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· The eyes are open and never find the lens.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 8 — shoe insoles · product class CONFORMING OR ENCLOSED, the PACKAGE in frame · no face

**The route this file has described since 3.5 and never drawn.** An insole is invisible inside a
shoe, so the product enters the frame as its package, standing in the scene as its own object.
**Named failure mode, predicted here: the package becomes the SUBJECT and the frame turns into a
packshot**, which `BOUNDARY` sends to `lede-winner`.

**`TYPE: lede-inuse v0.10 — SET 6 CELL 8`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     close on a hall bench: both hands, one walking boot on its side, and the open package standing on the bench beside it.
[EVIDENCE] one insole is going down into the boot and seating flat along its whole length, the second is still in the open package standing upright beside it, and the flattened old insole lies pulled out on the bench.
[COMFORT]  the ease is real, its form yours — the hands working unhurried, the shoulders low, the fingers loose, the fit going in without force. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: leaning in over the bench, weight settled on one hip.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult fitting new insoles before a walk, on a bright morning.
[ENVIRONMENT] a kept hallway — clear bench, boots paired on the floor, everything in order.
[CONDITION] the product is clean and as-new.
[LIGHT]    a window beside the door fills the hall and it is bright: pale walls, light wood bench, daylight across it, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The package stands as one object among others — not centred, not held up, not the subject: the boot, the bench and the hall are all present around it.
· The insole going into the boot is readable along its whole length.
· No face, no head and no shoulders in the frame.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening in the body or the hands.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 9 — beeswax food wraps · `presentation`, the photograph inside a DESIGNED object · no face

**2 of 2 in set 1 and not drawn since.** The whole frame is a real photograph presented as a graphic
object — the shape this type's second corpus observation takes. **This cell alone drops *no drawn
element of any kind*, because the mat is the drawn element and it is the case being tested.**

**`TYPE: lede-inuse v0.10 — SET 6 CELL 9`**

```
REGISTER: editorial documentary photograph presented as a designed object, single frame.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[PRESENTATION] the photograph sits inside a designed mat on a flat coloured ground: a soft sage field, a warm clay mat with a scalloped inner edge, and a small pressed-flower ornament at each corner of the mat.
[CROP]     inside the mat, close on both hands and a bowl on a worktop, from wrist to work.
[EVIDENCE] a wrap is being pressed down over the rim of the bowl and has taken the shape of it — the wax gone glossy and creased where the warm hands have moulded it, the seal already closed all the way round one side.
[COMFORT]  the ease is real, its form yours — the hands working unhurried, the fingers loose, the press gentle, the shoulders low. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: leaning in over the worktop, weight settled on one hip.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult putting a bowl away on a bright morning.
[ENVIRONMENT] a kept kitchen — clear pale worktop, everything in order.
[CONDITION] the product is clean and as-new.
[LIGHT]    inside the photograph, a window fills the wall behind and it is bright: pale walls, light wood, daylight across the worktop, soft shadows.
[GRADE]    natural and true colour inside the photograph, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the bowl rim it is sealing are readable.
· The wax has visibly taken the shape of the rim, glossy and creased where the hands pressed it.
· The photograph sits inside the mat with the coloured ground visible all the way round it.
· The mat, the ground and the corner ornaments are the ONLY designed elements: no badge, no lettering, no arrows, no inset panel.
· No face, no head and no shoulders in the frame.
· At least one visible sign of ease is happening in the body or the hands.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 10 — mirror demister pad · `gaze: reflect`

**An existing value of the shared axis with zero renders in this type**, and it is what this type's
only corpus MATCH does — a man at a bathroom mirror, eyes on his own reflection.

**`TYPE: lede-inuse v0.10 — SET 6 CELL 10`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     three-quarter from the side: the person at the basin, the mirror in front of them, their reflection in it.
[EVIDENCE] a clear oval wiped through a fogged mirror with the reflection sharp inside it, the grey mist still standing all round the edge, and a hard boundary where the pad has stopped.
[COMFORT]  the ease is real, its form yours — a breath going out, the eyes creasing, a small smile arriving on its own. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: a lean in toward the basin, weight settled on one hip, the free hand resting on the rim.
[GAZE]     on their own reflection in the mirror, never on the camera.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult at the basin after a shower on a bright morning.
[ENVIRONMENT] a kept bathroom — pale tile, clean fittings, everything in order.
[CONDITION] the product is clean and as-new.
[LIGHT]    a window fills the wall beside the basin and the room is bright: pale tile, white fittings, daylight across the glass, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the glass it is clearing are readable.
· The two states are on ONE mirror: a clear oval with a sharp reflection in it, mist all round, a hard boundary between.
· The eyes rest on the reflection in the mirror and never find the camera.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening on the face or the shoulders.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera, no phone at a mirror.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 11 — fabric shaver · CONTROL, draw 1 of 2 — the turn-back pose kept

**Predicted: the eyes find the lens.** This cell and the next are the only two in the set whose
`[POSE]` range still offers *a half-turn to look back*, which is what 0.10 says caused set 5's two
gaze failures.

**`TYPE: lede-inuse v0.10 — SET 6 CELL 11, CONTROL`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     three-quarter, head to hip: the person, the shaver in one hand, the garment over the other arm.
[EVIDENCE] one sleeve half done — the shaved half smooth and even with the weave showing, the rest still furred with bobbles, and a clean line across the cloth where the head has stopped.
[COMFORT]  the ease is real, its form yours — a breath going out, the eyes creasing, a small smile arriving on its own. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: a half-turn to look back, weight settled on one hip, the free hand holding the cloth taut.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult bringing a coat back into wear on a bright morning.
[ENVIRONMENT] a kept bedroom — clear surfaces, a chair with nothing piled on it, everything in order.
[CONDITION] the product is clean and as-new.
[LIGHT]    a wide window fills the wall behind and the room is bright: pale walls, light wood, daylight across the cloth, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the cloth under it are readable.
· The two states are on ONE sleeve, with a clean line between the smooth half and the furred half.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening on the face or the shoulders.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· The eyes are open and never find the lens.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## 12 — fabric shaver · CONTROL, draw 2 of 2 — identical to cell 11

**`TYPE: lede-inuse v0.10 — SET 6 CELL 12, CONTROL`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo, the exact reference — preserve shape, proportions,
            material, finish, colour and every printed mark.
ELEMENTS — style these.
[CROP]     three-quarter, head to hip: the person, the shaver in one hand, the garment over the other arm.
[EVIDENCE] one sleeve half done — the shaved half smooth and even with the weave showing, the rest still furred with bobbles, and a clean line across the cloth where the head has stopped.
[COMFORT]  the ease is real, its form yours — a breath going out, the eyes creasing, a small smile arriving on its own. Pick two, not all.
[POSE]     at ease and unbraced, shape yours: a half-turn to look back, weight settled on one hip, the free hand holding the cloth taut.
[CASTING]  a Western European adult, white or Black.
[DRESS]    dressed like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult bringing a coat back into wear on a bright morning.
[ENVIRONMENT] a kept bedroom — clear surfaces, a chair with nothing piled on it, everything in order.
[CONDITION] the product is clean and as-new.
[LIGHT]    a wide window fills the wall behind and the room is bright: pale walls, light wood, daylight across the cloth, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the cloth under it are readable.
· The two states are on ONE sleeve, with a clean line between the smooth half and the furred half.
· The clothing is particular to this person — nothing that could belong to anyone.
· At least one visible sign of ease is happening on the face or the shoulders.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· The eyes are open and never find the lens.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One person only, and an adult.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **Cells 11 and 12 — do the eyes find the lens?** | the 0.10 gaze diagnosis. If they do not, the cause is the framing, not the pose option |
| 2 | **Cells 1–10 — did any eye find the lens?** | whether removing the turn-back option was enough |
| 3 | **Is every subject Western European, white or Black?** | `PARTS/casting`, new at 0.10 and untested |
| 4 | **Cell 8 — is this a scene, or has it become a packshot?** | the `conforming or enclosed` route, never drawn before |
| 5 | **Cell 9 — does the designed mat still work, and does it stay clear of lettering?** | `presentation`, 2 of 2 and not drawn since set 1 |
| 6 | **Cell 10 — are the eyes on the reflection, and is the frame free of the selfie register?** | `gaze: reflect`, never drawn, and the value nearest the G14 line |
| 7 | **Cell 6 — ease, or coping in the dark?** | the light exception's second draw |
| 8 | **Cell 7 — does the belt read as the outermost layer and the source of every tool?** | the `worn-external` class, on a product that is not a brace |
| 9 | **Name the one thing in each frame that shows the product working** | `PARTS/evidence`, all five methods in one set |
| 10 | **Did `[DRESS]` land in all twelve?** | 4 of 4 in set 5; twelve is the test of whether it holds at volume |
| 11 | **Is any place shabby, or any product scuffed?** | `condition` and the kept-place rule, 6 of 6 so far |
| 12 | **Any word or number anywhere, on a scene object or a product label?** | the standing check, three faults in set 4 |
| 13 | **Did any frame read as a customer's own photograph?** | the G14 firewall, and cell 10 is the closest this type has come to the line |

---

## RESULT — rendered 2026-09-10, all twelve opened and graded under ADR-011

Full finding in `lede-inuse.md` at 0.11. **7 pass, 3 partial, 2 fail.**

| # | case | medV | dark | sat | verdict |
|---|---|---|---|---|---|
| 1 | effect as matter | 0.67 | 18% | 0.35 | **pass** — the best frame in the set, and one of two that read alive |
| 2 | act forbidden | 0.75 | 3% | 0.20 | **partial** — the stool is visibly old and weathered |
| 3 | work only the benefit allows | 0.77 | 8% | 0.21 | **pass** |
| 4 | comparison as an object | 0.88 | 1% | 0.12 | **partial** — a ground-floor window, and no hard clean/grey line |
| 5 | duration and quantity | 0.71 | 1% | 0.16 | **pass** |
| 6 | **LIGHT EXCEPTION** | 0.10 | 57% | 0.59 | **pass** — second draw of the exception, and the other frame that reads alive |
| 7 | worn-external | 0.80 | 2% | 0.18 | **partial** — the belt reads, and she is leaning on the wall with the nail not going in |
| 8 | **package in frame** | 0.80 | 15% | 0.18 | **pass** — a scene, not a packshot |
| 9 | **`presentation`** | 0.77 | 3% | 0.25 | **pass** — the mat exactly as written, no lettering |
| 10 | **`gaze: reflect`** | 0.76 | 5% | 0.16 | **pass** — eyes on the reflection, G14 intact |
| 11 | CONTROL draw 1 | 0.87 | 8% | 0.19 | **fail** — no two-state sleeve; eyes off-frame, not on the lens |
| 12 | CONTROL draw 2 | 0.78 | 5% | 0.15 | **fail** — no clean line; **eyes on the lens** |

**Prediction by prediction:**

- **Cells 11 and 12 predicted to look into the lens.** **One did, one did not.** The turn-back
  option causes it and does not compel it — and against **0 of 10** in the cells where it was
  removed, the 0.10 diagnosis holds. **This is the clearest case yet for drawing a control twice:**
  draw 1 alone would have refuted a correct diagnosis, draw 2 alone would have confirmed it too
  strongly.
- **Cells 1–10 predicted to keep their eyes off the lens.** 10 of 10.
- **Casting predicted to hold 12 of 12.** It did, on the clause's first outing.
- **Cell 8 predicted most likely to fail, as a packshot.** **It passed** — the named failure mode did
  not occur, and the `conforming or enclosed` route the file has described since 3.5 is drawn at
  last.
- **Cell 9's mat predicted to land.** It did, exactly as specified. `presentation` is 3 of 3.

**What the set was not built to find, and found anyway.** Owner: *"mọi thứ đã ổn trừ scene chưa
lively, chưa sống động"*. **Two causes, both written by me into these very prompts.** Every cell
here asked for *a kept X — clear worktop, clear floor, everything in order*, and the frames came
back with bare beds, empty dressers, blank walls and an unpeopled show kitchen. **The only two that
read alive are the two whose rooms are full because of what the room IS** — a chisel rack, a
pegboard. And two cells stopped the ACT: cell 7 leaning with the nail not going in, cell 11 holding
the coat with the shaver against her chest. **A still room and a stopped body make the same dead
picture.** Both fixed at 0.11, in `PARTS/environment` and `PARTS/pose`.

*A liveliness measurement was attempted and DISCARDED — full-frame detail density ranks the extremes
right and does not separate the middle. No figure from it is published.*
