# `02-cause-anatomy` set 1 — six products from the Sep 8 list, cause then effect

Written against **`02-cause-anatomy` v1.18**. Owner, 2026-09-15: *"cần có cơ chế, logic so sánh
rõ ràng hơn. tạo bộ prompt 6 sản phẩm bất kì trong danh sách để tôi test lại"* — the mechanism and
the comparison must read more clearly; six products from `Product Input Sep 8.csv`.

## What makes the comparison clearer in every prompt

1. **Each panel is one sentence of cause, then effect**: the object and the one property that
   matters, what it does to the body, and — after *so* — the state the structure is left in. The
   right panel changes only the object, and the other two beats follow from it.
2. **One named difference, everything else identical**: *the only differences are X and what the
   structure does because of it*.
3. **A state big enough to see at whole framing** — a pelvis rolling, a spine bowing or folding,
   a shoulder hiking, a thumb bending. At 1.15 both passes changed a posture; the three cover-test
   failures changed a nostril, a gap and a line on an unchanged head.
4. **No measuring line** (withdrawn at 1.18). One mark class a prompt, each pointing at the state
   the body already shows: a load (`pressure`), an edge (`contour`), an angle (`range`), a joint
   (`fill`), a cause (`force`) or a correct line (`aura`).

## Why these six

The list was screened against what this type needs: **a culprit OBJECT in daily life, a change of
state visible at whole framing, and a mechanism the product's own brief states** in words its
do-not-say line allows. None of the six has a record under this type in `eval/render-tests.jsonl`.

| # | product | brief | culprit | the brief's own mechanism |
|---|---|---|---|---|
| 1 | memory foam seat cushion | 02 | a bare hard chair seat | *a hollow tailbone vent ... so the tailbone floats instead of carrying body weight* |
| 2 | plank ab roller wheel | 37 | a thin standard ab wheel | *at deepest extension ... the load transfers to the lower back*; *a built-in stop prevents over-extension* |
| 3 | furniture lifting tool set | 11 | lifting a sofa corner by hand | *a long handle lets the user push upright rather than bending* |
| 4 | fascia ring massager | 60 | a handheld massage gun | *a handheld forces you to contort your arm behind your back* — no relief claim, which the brief bans |
| 5 | cordless electric scissors | 09 | manual scissors | *the hand only guides the tool — no repeated squeezing* |
| 6 | car armrest box | 83 | the car's own low armrest lid | *so you either hover your arm or hunch toward the wheel*, and the seller's *take pressure off the shoulder* |

**Left out**: open-ear headphones (48), because an ear canal at whole framing is the nostril
failure again; the blood pressure monitor (06), whose chamber covers the arm it argues about; the
hot air styler (96), whose hair shaft cannot share a frame with a person using it; the pedal band
(27), which has no culprit object; the grip strengthener (101), whose difference is one of amount;
the weed burner (28), whose flame would put orange in the correct panel; and the arm trainer,
voice mouse and neck fan (14, 26, 36), whose briefs ban the claim the image would make.

## The set diversity law, checked

No two prompts share more than two of the five levers, and a script asserts it.

| # | style | ground | subject | badge | mark |
|---|---|---|---|---|---|
| 1 | line-engraving | deep graphite | pelvis, tailbone, lower spine | glyph | `pressure` |
| 2 | flat-vector | deep olive | lower spine and pelvis | none | `contour` |
| 3 | flat-vector | deep charcoal violet | spine, pelvis, thigh bones | hazard | `range` |
| 4 | line-engraving | deep umber | shoulder socket | emoji | `fill` |
| 5 | airbrushed | deep slate | thumb bones, base joint, tendon | thumb | `force` |
| 6 | airbrushed | deep plum | collarbone and shoulder blade | glyph | `aura` |

**Style follows the mark.** `line-engraving` failed once, when its hatching pulled a line into a
box, so both its prompts carry filled marks. `flat-vector` bans gradients, so the glow goes to
`airbrushed`.

### Predictions, written before the render

1. **Pass**: the posture closest to the car lumbar roll that passed. Watch whether the engraving
   hatches the two fills.
2. **Partial**: the rival is an ab wheel against an ab wheel, and a same-kind rival came back as
   the product's twin 4 times in `03-mechanism-ghostbody`. Watch that first.
3. **Pass**: folded double against upright is the largest change of state in the set.
4. **Partial**: the arm's position is the mechanism, so the pose differs more than anywhere else.
   Watch whether the socket reads as twisted or merely filled red.
5. **Pass on the hand**, the only prompt with a cause mark and no state mark. Watch finger count.
6. **The red-free control**: the left panel carries no red mark, only its badge. If the hiked
   shoulder still reads as wrong, a state mark on the wrong side is not what carries the verdict.

**Attachments: one reference photo per prompt.** Where a product comes in colourways, attach one
that is not red, blue or green. Ratio at the generation tool, never in the text.

---

## 1 — memory foam seat cushion · `line-engraving`, `pressure`

**`TYPE: 02-cause-anatomy v1.18 — SET 1 PROMPT 1`**

```
MEDIUM: 2D illustration, line-engraving: fine engraved lines and cross-hatching, like an
antique medical plate, every mark a flat solid fill. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the memory foam seat cushion
in the right panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole seated figure from head to feet, seen from the side, the pelvis small within it.
GROUND: deep graphite, the right half one step lighter than the left.
BODY: the pelvis, the tailbone and the lower spine in warm ivory over a translucent outline of
the figure. NOT a full skeleton. Exactly one figure in EACH panel, same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are what the
figure sits on and what the pelvis does because of it. The pelvis appears in both panels and
nothing covers it.
In the left panel, a plain grey chair with a bare hard seat: the seat gives the tailbone nowhere
to go, so the pelvis rolls backward and the tailbone takes the weight.
In the right panel, the reference cushion on the same chair: it holds the tailbone clear of the
seat, so the weight rests on the two sitting bones and the pelvis stands upright.

MARKS, nothing else marked. Two flat solid fills, each bounded by the contact surface and as
wide as that contact: red where the tailbone meets the bare seat in the left panel, blue where
the sitting bones meet the cushion in the right panel. One badge near the top of each panel,
clear of the frame edges: a red filled disc with a white X cut out in the left, a green filled
disc with a white check cut out in the right. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.
```

---

## 2 — plank ab roller wheel · `flat-vector`, `contour`, no badge

**`TYPE: 02-cause-anatomy v1.18 — SET 1 PROMPT 2`**

```
MEDIUM: 2D illustration, flat-vector: flat fills, hard edges, no gradients. NOT photography,
NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the plank ab roller wheel in
the right panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole kneeling figure from hands to feet, seen from the side, head to the left, the
lower spine small within it.
GROUND: deep olive, the right half one step lighter than the left.
BODY: the lower spine and the pelvis in warm ivory over a translucent outline of the figure.
NOT a full skeleton. Exactly one figure in EACH panel, same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are the wheel,
how far it rolls, and what the lower spine does because of it. The lower spine appears in both
panels and nothing covers it.
In the left panel, a thin ordinary single wheel no wider than a hand: nothing stops it rolling,
so the arms reach far past the head, the hips drop and the lower spine bows down toward the
floor.
In the right panel, the reference roller: it stops rolling with the arms just past the head, so
the hips stay level with the shoulders and the lower spine stays straight.

MARKS, nothing else marked. One curved line in each panel along the belly-side edge of the lower
spine: red and bowed in the left panel, blue and straight in the right panel. No badge in either
panel.

G3: red wrong, blue correct, nothing else.
```

---

## 3 — furniture lifting tool set · `flat-vector`, `range`, `verdict-hazard`

**`TYPE: 02-cause-anatomy v1.18 — SET 1 PROMPT 3`**

```
MEDIUM: 2D illustration, flat-vector: flat fills, hard edges, no gradients. NOT photography,
NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the furniture lifting tool set
in the right panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole figure beside the end of a plain grey sofa, seen from the side, the spine small
within it.
GROUND: deep charcoal violet, the right half one step lighter than the left.
BODY: the spine, the pelvis and the thigh bones in warm ivory over a translucent outline of the
figure. NOT a full skeleton. Exactly one figure in EACH panel, same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are what lifts
the sofa's corner and how the spine bends because of it. The corner is raised the same small
height in both. The spine appears in both panels and nothing covers it.
In the left panel, the figure lifts the corner with both hands: the weight sits low, so the body
folds double at the hips and the spine curves forward over the load.
In the right panel, the reference tool under the same corner, pressed down by one hand: the tool
does the lifting, so the figure stands upright and the spine stays straight.

MARKS, nothing else marked. One shaded wedge in each panel between the trunk and the thigh: red
and narrow in the left panel where the hips fold, blue and open in the right panel. One badge
near the top of each panel, clear of the frame edges: a red warning triangle in the left, a
green filled disc with a white check cut out in the right.

G3: red wrong, blue correct, green badge, nothing else.
```

---

## 4 — fascia ring massager · `line-engraving`, `fill`, `verdict-emoji`

**`TYPE: 02-cause-anatomy v1.18 — SET 1 PROMPT 4`**

```
MEDIUM: 2D illustration, line-engraving: fine engraved lines and cross-hatching, like an
antique medical plate, every mark a flat solid fill. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the fascia ring massager in
the right panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole seated figure from the hips up at a plain desk, seen from behind, the right
shoulder small within it.
GROUND: deep umber, the right half one step lighter than the left.
BODY: the top of the right upper-arm bone in its socket and the outer end of the shoulder blade
in warm ivory over a translucent outline of the figure. NOT a full skeleton. Exactly one figure
in EACH panel, same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are what works on
the upper back and where the right arm is because of it. The right shoulder socket appears in
both panels and nothing covers it.
In the left panel, an ordinary handheld massage gun held between the shoulder blades by the
right hand: reaching there bends the arm up behind the back, so the upper-arm bone twists hard
in its socket.
In the right panel, the reference ring strapped around the upper back: nothing has to hold it,
so both hands rest on the desk and the upper-arm bone sits level in its socket.

MARKS, nothing else marked. The right shoulder socket filled flat in each panel: red in the left
panel, blue in the right panel. One badge near the top of each panel, clear of the frame edges:
an angry face emoji in the left, a smiling face emoji in the right.

G3: red wrong, blue correct, nothing else outside the badges.
```

---

## 5 — cordless electric scissors · `airbrushed`, `force`, `verdict-thumb`

**`TYPE: 02-cause-anatomy v1.18 — SET 1 PROMPT 5`**

```
MEDIUM: 2D illustration, airbrushed: soft gradients, modelled volume. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the cordless electric scissors
in the right panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole right forearm and hand cutting a sheet of plain grey cardboard held flat on a
table, seen from the thumb side, the thumb small within it.
GROUND: deep slate, the right half one step lighter than the left.
BODY: the thumb bones, the joint at the thumb's base and the tendon along the thumb in warm
ivory over a translucent outline of the hand and forearm. NOT a full skeleton. Exactly one hand
in EACH panel, same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are the tool in
the hand and what the thumb does because of it. The thumb appears in both panels and nothing
covers it.
In the left panel, ordinary manual scissors with plain grey loops: the blades close only when
the hand squeezes, so the thumb presses down hard and bends sharply at its base.
In the right panel, the reference electric scissors: they cut on their own, so the thumb rests
lightly on the handle and stays straight at its base.

MARKS, nothing else marked. One double-headed curved arrow along the scissor loops where the
squeeze acts, red, in the left panel only. One badge near the top of each panel, clear of the
frame edges: a red filled disc with a thumbs-down cut out in the left, a green filled disc with
a thumbs-up cut out in the right, each a flat pictogram, a solid silhouette, never a photographed
or three-dimensional hand. Same diameter, not rings.

G3: red wrong, green badge, nothing else.
```

---

## 6 — car armrest box · `airbrushed`, `aura`, the red-free control

**`TYPE: 02-cause-anatomy v1.18 — SET 1 PROMPT 6`**

```
MEDIUM: 2D illustration, airbrushed: soft gradients, modelled volume. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the car armrest box in the
right panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole driver from the hips up in a plain grey car seat, left hand on the wheel, seen
from the side, the right shoulder small within it.
GROUND: deep plum, the right half one step lighter than the left.
BODY: the right collarbone and shoulder blade in warm ivory over a translucent outline of the
figure. NOT a full skeleton. Exactly one figure in EACH panel, same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are what the right
elbow rests on and what the right shoulder does because of it. The right shoulder appears in
both panels and nothing covers it.
In the left panel, the car's own low armrest lid, too low to reach: the elbow hangs in the air
above it, so the shoulder hikes up toward the ear to hold the arm.
In the right panel, the reference armrest box on the same console: its top meets the elbow, so
the arm rests and the shoulder drops level.

MARKS, nothing else marked. One soft blue glow along the top edge of the right shoulder, in the
right panel only. One badge near the top of each panel, clear of the frame edges: a red filled
disc with a white X cut out in the left, a green filled disc with a white check cut out in the
right. Same diameter, not rings.

G3: blue correct, red and green only in the badges, nothing else.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **All six — cover the marks: do the panels still read wrong and right?** | the 1.18 rule that the body carries the argument |
| 2 | **All six — can a viewer say what the object does and what the body does back?** | cause then effect, the owner's finding |
| 3 | **All six — is the right half of the ground lighter? Measure it.** | G4 |
| 4 | **Prompts 1 and 4 — are the fills flat, or hatched by the engraving?** | `line-engraving`, untested again |
| 5 | **Prompt 2 — is the rival wheel a twin of the reference?** | the same-kind rival risk |
| 6 | **Prompt 6 — does the left panel read as wrong with no red mark?** | whether a harm mark carries the verdict |
| 7 | **All six — six images, or one image six times?** | the set diversity law |
| 8 | **All six — any word, face or measuring line?** | G6, NEGATIVE, 1.18's withdrawal |

---

## RESULT — 2026-09-15, five renders, 0 pass

Four renders in `image-library-assets/feedback/` at 13:13–13:14 and one inside `download.zip`
beside them, each mapped to its prompt by content. **Prompt 1, the seat cushion, came back with no
render.** Owner, same day: *"mark xuất hiện trong ảnh phải phục vụ mục đích so sánh, làm rõ ưu
nhược điểm, tôi thấy mark của furniture lifting tool và plank ab roller wheel chưa tốt"* — a mark
must serve the comparison and make the cost and the gain plain, and the lifting-tool and ab-roller
marks do not.

| # | product | verdict | what broke |
|---|---|---|---|
| 2 | ab roller | **fail** | one roll-out pose in both panels, so the two lines are the only difference; the red line floats below the belly, off the spine; a person with skin, hair and a face instead of an outline; letters drawn on the product |
| 3 | lifting tool | partial | the two wedges point from the hip at two different things — the hands, the handle — and read as beams of light, not as an angle or a cost; an outline warning triangle beside a filled disc |
| 4 | fascia ring | **fail** | the right panel draws a posture brace, not a ring massager; both shoulders filled in both panels, so colour is the only difference and the resting shoulder is marked as harmed |
| 5 | electric scissors | partial | the thumb's change is small; a badge 2.8% from the left edge |
| 6 | armrest box | partial | the shoulder does not hike, so the named state is not drawn; the blue glow states no cost and no gain; a profile face |

**The marks, against the owner's test: 1 of 5 served the comparison.** The arrow along the scissor
loops states what the culprit keeps doing — the squeeze — and the empty right panel reads as its
absence. The other four either marked two different things in the two panels (wedges), marked the
same place differing only in colour (fills), were the only difference between two identical poses
(lines), or named no cost at all (glow).

**Held**: the ground steps lighter on the right in 5 of 5 — +25.7, +32.7, +76.3, +32.7 and +33.7 of
255, each a corner median checked against a second patch in the same panel; the posture comparison
reads with the marks covered on the lifting tool and the fascia ring; `line-engraving` kept its
fills flat and unhatched, its first clean render; no measuring line and no word anywhere except the
roller's label; the emoji badges sat 15.6% from the top and 9.0% from the side, the only pair inside
G10 — the disc badges measured 3.4–5.7% from the top.

What moved into the type is in its 1.18 CHANGELOG. Set 2 is
`registry/types/sets/02-cause-anatomy-02/`.
