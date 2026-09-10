# `lede-inuse` set 5 — dress, pose and comfort as INFORMATIVE clauses, against a control drawn twice

Written against **`lede-inuse` v0.9**. Owner, 2026-09-10, on set 4: *"cần phải áp dụng pose, emotion
giống authority. ngoài ra quần áo của user có thể đặc biệt: hoạ tiết hay màu sắc sặc sỡ, không
generic — hãy để prompt mở để model tự suy luận"*.

## What set 4 settled

**The bright rule holds, 5 of 5**, at median value 0.64–0.73 with 2–18% dark. **The exception clause
works on its first outing**: the stair light measured 0.29 / 32% — darker than three of set 3's
failures — and reads as ease rather than coping, because the way down is already lit. **Dark was
never the fault; showing someone cope with it was.**

**`[COMFORT]` is not decoration.** The control carried none and returned a blank face. **And the
prescribed triple is not the answer either**: cell 1 carried *brow smooth, jaw loose, shoulders
dropped* word for word and returned a half-grimace with the free hand splayed palm-up, while cell
3's small unforced smile is the best expression this type has produced.

**The declared removal is vindicated**, the reverse of the cautious guess: all four cells whose
duplicated evidence constraint was cut landed their evidence, and the one cell that kept its pair
failed on evidence anyway.

## What this set tests

**Three clauses that INFORM rather than prescribe, and whether opening them is safe.**

`lede-authority` reached this mechanism at its own 0.10 on the identical owner instruction, after a
prescription of taste flattened twelve of its renders into one centred, square, neutral picture.
Its distinction is **DELIBERATE against CAUGHT**; here it is **AT EASE against BRACED**, because
this type's subject is candid.

**The reconciliation with everything else this namespace knows.** Things to draw land 37 of 37;
prescriptions of taste were ignored 4 of 4 in round 3. **Dress, pose and expression are taste.**
Opening them is not a retreat from *name the thing* — it is the same finding saying which clauses
are things to draw and which never were.

| # | product | evidence | what is open |
|---|---|---|---|
| 1 | long-handled stand-up weed puller | 2 · the act the problem forbade | dress, pose, comfort |
| 2 | adjustable dumbbell | 4 · comparison as an object | dress, pose, comfort |
| 3 | folding shopping trolley | 5 · tells of duration and quantity | dress, pose, comfort |
| 4 | garden pressure sprayer | 1 · effect as matter | dress, pose, comfort |
| 5 | food vacuum sealer | 1 · effect as matter | **CONTROL — no `[DRESS]`, draw 1** |
| 6 | food vacuum sealer | 1 · effect as matter | **CONTROL — no `[DRESS]`, draw 2** |

**The control is two cells, not one cell rendered twice.** Sets 3 and 4 each asked for a second draw
of their control and each got one, because a set is rendered a cell at a time. §*Reading a render*
wants a register finding drawn more than once and dress is a register property, so **the repeat is
built into the cell list where it cannot be missed.** Cells 5 and 6 are the same prompt, character
for character.

**Every cell shows the torso**, which is new and is a requirement rather than a preference: a clause
about clothing cannot be graded on a frame cropped to a pair of hands. Four of set 4's six were.

> **Prediction: cells 5 and 6 both come back in plain, unpatterned, low-saturation clothing** — a
> marl tee, a plain sweatshirt, a dark work top — because the slot is unnamed and takes the
> commonest thing of its kind. That is the role-vs-value default and set 4 was its sixth instance.
> **If either control draw arrives in something particular, `[DRESS]` is decoration** and set 4's
> wardrobe came from somewhere else.

Predictions for the rest, written before the render:

- **Cells 1–4** — four visibly different wardrobes, at least two carrying a print or a strong
  colour, and **no two of the four sharing an expression**. Set 4's four faces were one face.
- **Comfort's floor holds** — every cell shows at least one named ease behaviour, so none returns
  the blank of set 4's control.
- **The risk being run, stated in advance:** opening three clauses at once means a failure cannot be
  attributed to one of them. It is taken because the three are one instruction from the owner and
  one mechanism, and because the control isolates the wardrobe half of it.

Five products, none used in any earlier set or round of this namespace. One reference photo each,
one generation call each (ADR-021, ADR-076). Grade on the calibrated instrument — median value,
share below 0.15, **mean** saturation.

## Prompt economy — this set hit the gate and was cut back

| set | median | range |
|---|---|---|
| `lede-inuse-03` | 1786 | 1510–1842 |
| `lede-inuse-04` | 1860 | 1741–1918 |
| **`lede-inuse-05`, first draft** | **2666** | 2407–2836 |
| **`lede-inuse-05`, shipped** | **2236** | 1984–2395 |

**The first draft put four of six prompts over Rule 6's 2500 ceiling and `scripts/validate.py`
fired**, taking the repo from 31 warnings to 35. That is the ratchet caught by a gate instead of by
a reader, which is what the gate was built for after thirteen sets went unmeasured.

The cause is plain: **three new element blocks went in — `[DRESS]`, `[POSE]`, `[CONDITION]` — and
nothing came out.** What was cut to get back under:

- **Set 4's vindicated removal, applied to four more cells.** A constraint that only restates its
  `[EVIDENCE]` block is gone from cells 2, 3, 4 and the control. Set 4 proved these do no work: the
  four cells whose line was cut all landed their evidence, and the one that kept its pair failed
  anyway. Every constraint carrying an EXCLUSION the element does not — *no rack of other
  dumbbells*, *wheeled not hauled*, *fully upright, not stooped* — is kept.
- **A constraint that restated `[ENVIRONMENT]` and `[CONDITION]` together**, in all six.
- **The comfort floor stopped re-listing** what `[COMFORT]` already lists; it now states only the
  floor.
- **The ranges are ranges, not inventories** — four ease behaviours and three poses, where the
  draft had five and four.

**The control measures the cost of the new clauses, as it did in sets 3 and 4.** Cells 5 and 6
carry no `[DRESS]` and sit at **1984**; the four that do run 2189–2395. So `[DRESS]` and its refusal
cost about 205–410 characters, and the rest of the rise is `[POSE]` and `[CONDITION]`, which every
cell carries.

**Still the longest set this type has shipped**, against a namespace record of *"lede-inuse's sets
run 1375–1696 and are the tightest in the namespace"*. Reported rather than padded down, and the
next removal candidate is named now: **`[POSE]` and `[COMFORT]` are two informative blocks doing one
job** — one is the body, one is the face, and if set 5 shows them landing they are a candidate to
merge into a single `[EASE]` block worth roughly 120 characters a prompt.

**The rule kept from set 4: each thing is stated once.** An informative clause lives in ELEMENTS and
is NOT restated as a constraint, because restating it is prescribing it — which is the thing under
test. CONSTRAINTS carries refusals and falsifiable tests only.

---

## 1 — long-handled stand-up weed puller · the act the problem FORBADE

**The test in the picture:** weeding a whole bed standing upright is not available to a bad back or
a bad knee. Kneeling is what the problem demands.

**`TYPE: lede-inuse v0.9 — SET 5 CELL 1`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     three-quarter, head to shin: the person standing, the tool, and the bed they are working.
[EVIDENCE] a row of pulled weeds already lying along the edge of the bed, roots and all, and the jaws closing on the next one — the whole job done from standing, with no kneeler, no mat and no hand in the soil.
[COMFORT]  the ease is real and its form is yours — a slow breath going out, the eyes creasing, a shoulder dropping, a small smile arriving on its own. Pick two or three, not all.
[POSE]     at ease and unbraced, shape yours: weight settled on one hip, a hand loose on the shaft, a half-turn back down the row.
[DRESS]    this person dresses like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult clearing a long bed on a bright morning.
[ENVIRONMENT] a kept garden — edged beds, a swept path, tools put away.
[CONDITION] the product is clean and as-new.
[LIGHT]    open daylight and the place is bright: pale gravel, fresh green, a light sky, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the weed in its jaws are readable.
· The person is fully upright and standing — not kneeling, not crouching, not stooped over the bed.
· The clothing is particular to this person — nothing plain, nothing that could belong to anyone.
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

## 2 — adjustable dumbbell · COMPARISON as an object

**A switchable state on one object:** the handle carries what a whole rack would, and the rest is
sitting in its cradle beside it.

**`TYPE: lede-inuse v0.9 — SET 5 CELL 2`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     three-quarter, head to knee: the person, the dumbbell in one hand, the cradle on the floor.
[EVIDENCE] the handle has drawn a stack of plates out of the cradle and carries them, and the plates it left behind sit in the cradle in their slots — one object where a rack of eight would stand, and the empty floor around it says so.
[COMFORT]  the ease is real and its form is yours — a slow breath going out, the eyes creasing, a shoulder dropping, a small smile arriving on its own. Pick two or three, not all.
[POSE]     at ease and unbraced, shape yours: weight on one leg, a lean against the wall, a half-turn to the cradle.
[DRESS]    this person dresses like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult mid-session at home, between sets.
[ENVIRONMENT] a kept room — clear floor, a rolled mat stood on end.
[CONDITION] the product is clean and as-new.
[LIGHT]    a wide window fills one wall and the room is bright: pale walls, light wood floor, daylight across it, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both the loaded handle and the cradle it came from are readable.
· There is no rack of other dumbbells anywhere in the frame.
· The clothing is particular to this person — nothing plain, nothing that could belong to anyone.
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

## 3 — folding shopping trolley · tells of DURATION and QUANTITY

**Third draw of method 5**, whose first failed on argument in a dark stairwell and whose second
landed in a desk.

**`TYPE: lede-inuse v0.9 — SET 5 CELL 3`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     three-quarter, head to pavement: the person, the trolley beside them, the street behind.
[EVIDENCE] the trolley is loaded to the top — a week of shopping standing in it, a bunch of leeks out of the mouth of the bag — and the market is already a long way back down the street behind them.
[COMFORT]  the ease is real and its form is yours — a slow breath going out, the eyes creasing, a shoulder dropping, a small smile arriving on its own. Pick two or three, not all.
[POSE]     at ease and unbraced, shape yours: two fingers on the handle, a half-turn to look back, weight settled on one hip.
[DRESS]    this person dresses like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult walking home from the market on a bright morning.
[ENVIRONMENT] a kept street — swept pavement, painted railings, a tidy row of frontages, two or three blurred passers-by.
[CONDITION] the product is clean and as-new.
[LIGHT]    open daylight and the street is bright: pale stone, light render, a light sky, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the load standing in it are readable.
· The hand on the handle is loose — the trolley is being wheeled, not hauled.
· The clothing is particular to this person — nothing plain, nothing that could belong to anyone.
· At least one visible sign of ease is happening on the face or the shoulders.
· The body is not guarding: no hand braced for support, no part held, no weight kept off one side.
· The eyes are open and never find the lens.
· Every object in the scene is plain and unlabelled, and nothing whose content is text is in frame.
· No shop sign, no street name, no printed packaging.
· Made by a photographer: no selfie framing, no arm's-length camera, no phone in shot, no hand holding the camera.
· No badge, no overlay, no inset, no drawn element of any kind.
· No beauty retouching, no plastic skin, no stock-photo look.
· One adult in focus, and any passer-by is blurred and incidental.
```

---

## 4 — garden pressure sprayer · effect as MATTER

**`TYPE: lede-inuse v0.9 — SET 5 CELL 4`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     three-quarter, head to thigh: the person, the lance in one hand, the row in front of them.
[EVIDENCE] a fine even mist standing in the air off the lance, hanging in the light in a broad cone, and the leaves under it already beaded and darkened where it has passed.
[COMFORT]  the ease is real and its form is yours — a slow breath going out, the eyes creasing, a shoulder dropping, a small smile arriving on its own. Pick two or three, not all.
[POSE]     at ease and unbraced, shape yours: weight on one leg, a lean along the row, the free hand loose at the side.
[DRESS]    this person dresses like themselves — a print, a strong colour, an unexpected combination. Yours to choose.
[SUBJECT]  one adult going along a row in a greenhouse in the morning.
[ENVIRONMENT] a kept greenhouse — clean glass, staged pots in order, a swept floor.
[CONDITION] the product is clean and as-new.
[LIGHT]    daylight floods through the glass and the place is bright: white frames, pale staging, fresh green, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the lance it is spraying from are readable.
· The clothing is particular to this person — nothing plain, nothing that could belong to anyone.
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

## 5 — food vacuum sealer · CONTROL, draw 1 of 2 — no `[DRESS]` block

**Predicted: plain, unpatterned, low-saturation clothing.** Everything here is written as cells 1–4
are written except that `[DRESS]` is absent and its constraint line with it.

**`TYPE: lede-inuse v0.9 — SET 5 CELL 5, CONTROL`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     three-quarter, head to worktop: the person, the sealer, the bag going into it.
[EVIDENCE] the bag has drawn tight around what is inside it — the film pulled down onto every edge and corner, the last of the air gone from the neck, the seal a clean flat band across the end.
[COMFORT]  the ease is real and its form is yours — a slow breath going out, the eyes creasing, a shoulder dropping, a small smile arriving on its own. Pick two or three, not all.
[POSE]     at ease and unbraced, shape yours: a lean on the worktop, weight on one hip, the free hand resting open.
[SUBJECT]  one adult putting the week's cooking away on a bright morning.
[ENVIRONMENT] a kept kitchen — clear pale worktop, a plain wooden board.
[CONDITION] the product is clean and as-new.
[LIGHT]    a wide window fills the wall behind and the room is bright: pale walls, light wood, clean glass, daylight across the worktop, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the bag in its jaws are readable.
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

## 6 — food vacuum sealer · CONTROL, draw 2 of 2 — identical to cell 5

**The same prompt, character for character.** Two draws of one control, because a register finding
needs more than one and the last two sets each asked for a second draw and got one.

**`TYPE: lede-inuse v0.9 — SET 5 CELL 6, CONTROL`**

```
REGISTER: editorial documentary photograph, single frame, made by a photographer.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the product — preserve
            shape, proportions, material, finish, colour and every printed mark exactly.
ELEMENTS — style these.
[CROP]     three-quarter, head to worktop: the person, the sealer, the bag going into it.
[EVIDENCE] the bag has drawn tight around what is inside it — the film pulled down onto every edge and corner, the last of the air gone from the neck, the seal a clean flat band across the end.
[COMFORT]  the ease is real and its form is yours — a slow breath going out, the eyes creasing, a shoulder dropping, a small smile arriving on its own. Pick two or three, not all.
[POSE]     at ease and unbraced, shape yours: a lean on the worktop, weight on one hip, the free hand resting open.
[SUBJECT]  one adult putting the week's cooking away on a bright morning.
[ENVIRONMENT] a kept kitchen — clear pale worktop, a plain wooden board.
[CONDITION] the product is clean and as-new.
[LIGHT]    a wide window fills the wall behind and the room is bright: pale walls, light wood, clean glass, daylight across the worktop, soft shadows.
[GRADE]    natural and true colour, light film grain, shallow depth of field.

CONSTRAINTS — binding.
· The product is in use and both it and the bag in its jaws are readable.
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
| 1 | **Cells 1–4 against cells 5 and 6 — did `[DRESS]` change the wardrobe?** | the owner's instruction, and whether an open clause can carry it |
| 2 | **Are cells 5 and 6 both plain?** | the role-vs-value default, seventh and eighth instances if so |
| 3 | **Do the two control draws agree with each other?** | if they diverge, dress is a register property that varies run to run and one draw proves nothing about it |
| 4 | **Do any two of cells 1–4 share an expression?** | set 4's four faces were one face. The open range is meant to break that |
| 5 | **Did comfort's FLOOR hold — is one named ease behaviour visible in every cell?** | the floor is what stops the blank face of set 4's control |
| 6 | **Did opening pose produce anything a prescription would not have?** | `lede-authority`'s finding, tested here for the first time |
| 7 | **Cell 1 — is the person fully upright, and is the row of pulled weeds behind them?** | method 2's fourth draw |
| 8 | **Cell 2 — are the left-behind plates visibly in the cradle, and is there no rack?** | method 4's third draw |
| 9 | **Cell 3 — is the trolley full, and is the distance walked visible?** | method 5's third draw |
| 10 | **Cell 4 — is the mist standing in the air, and are the passed leaves beaded?** | method 1's fifth draw |
| 11 | **Cells 5 and 6 — does the film read as drawn tight onto the contents?** | method 1 on a new product, and the control's evidence |
| 12 | **Any word or number in a frame, on a scene object or on the product's own label?** | three text faults in set 4, one of them written into the prompt |
| 13 | **Is any product soiled, scuffed or worn?** | `PARTS/condition`, new at 0.9, untested |
| 14 | **Did any frame read as a customer's own photograph?** | the G14 firewall, 24 of 24 across four sets |

---

## RESULT — rendered 2026-09-10, all six opened and graded under ADR-011

Full finding in `lede-inuse.md` at 0.10.

| # | product | medV | dark | sat | verdict |
|---|---|---|---|---|---|
| 1 | weed puller | 0.68 | 2% | 0.28 | **fail** — dress, comfort, place and evidence all land, and **the eyes are on the lens** |
| 2 | adjustable dumbbell | 0.76 | 10% | 0.24 | **pass** — a wall lean the prescription would never have written |
| 3 | shopping trolley | 0.85 | 4% | 0.14 | **fail** — the best-composed frame the type has made, and **the eyes are on the lens** |
| 4 | pressure sprayer | 0.73 | 11% | 0.27 | **pass** — everything lands |
| 5 | CONTROL draw 1 | 0.71 | 4% | 0.21 | **pass** — plain olive linen shirt, as predicted |
| 6 | CONTROL draw 2 | 0.73 | 1% | 0.21 | **partial** — plain oatmeal knit, as predicted; the bag is **not** drawn tight |

**Prediction by prediction:**

- **Cells 5 and 6, predicted plain, unpatterned, low-saturation.** Both, on two draws. **`[DRESS]`
  is not decoration** and the role-vs-value default is at instances seven and eight.
- **Cells 1–4, predicted four visibly different wardrobes with at least two carrying a print or a
  strong colour.** Four different, and all four carry a print or a strong colour.
- **Predicted no two of the four sharing an expression.** Held — a broad open smile, a private
  smile with the head down, a warm smile over the shoulder, a quiet smile along the row.
- **Comfort's floor, predicted to hold.** 6 of 6, including both cells with no `[DRESS]`.
- **The two control draws, asked whether they agree.** **They agree on the wardrobe and disagree on
  the evidence.** Draw 1's film is pulled onto every contour; draw 2's bag is loose and unsealed.
  Same prompt, four minutes apart. This is exactly the case §*Reading a render* was written for, and
  it arrived inside the experiment that was relying on it.

**The failure nobody predicted: the gaze gate, 2 of 6.** Clean 24 of 24 across sets 1–4. Cells 1 and
3 both took *a half-turn back down the row* / *to look back* from `[POSE]`'s open range, and both
turned into the lens. **The range carried the trap**, and `lede-inuse.md` 0.10 fixes the option list
rather than the openness — the same open range produced the two frames that passed.

**Question 13, `PARTS/condition`, first outing:** clean 6 of 6. **Light: 11 of 11** across sets 4
and 5.

**One frame breaches a rule written after it was rendered:** cell 2's subject is East Asian, and the
owner's casting instruction arrived the same day. Recorded, not counted against the set.
