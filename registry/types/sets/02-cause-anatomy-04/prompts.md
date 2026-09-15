# `02-cause-anatomy` set 4 — a colour from each product's world, and the ghost mannequin

Written against **`02-cause-anatomy` v1.18**. Owner, 2026-09-15, on set 3: *"chưa đa dạng sử dụng
màu theo reasoning của sản phẩm, thêm style ghostbody ([GHOST] the SAME featureless matte white
mannequin in both panels, no face, no hair, no clothing, no skin tone)"*.

## The colour rule, as a distinction rather than an opposite

Set 2 used saturated grounds with no reason (0.36–0.87 saturation) and read as bad; set 3 answered with
grey for everything (0.00–0.15) and read as one colour for six products. **Each ground now takes a hue
from the product's own world, DEEP and MUTED**, and never the product's own colour:

| # | product | ground | the reason, from the product | style |
|---|---|---|---|---|
| 1 | ergonomic kneeling chair | deep muted slate teal | a home office's cool light; separates warm wood and the white mannequin | ghost-mannequin |
| 2 | wide-grip ergonomic pen | deep muted walnut brown | a writing desk's wood; warm under ivory finger bones | line-engraving |
| 3 | trekking poles | deep muted heather violet | a mountain trail at dusk; separates black and silver poles | flat-vector |
| 4 | bed wedge reading pillow | deep muted dusk blue | a bedroom at night; separates a pale foam wedge | airbrushed |
| 5 | long-handled shoe horn | deep muted forest green | a front-door hallway; the steel horn and the white mannequin separate on it | ghost-mannequin |
| 6 | dog ramp | deep muted olive khaki | a living room's warm floor; separates a grey carpeted ramp and a tan dog | flat-vector |

**Deep** is back in every name: set 3's greys named without it came back at 158–246 of 255 on four of
six, and one turned into cream paper.

## What else changed from set 3, each from a render

1. **`ghost-mannequin` style**, added on the owner's instruction, in prompts 1 and 5. The figure is the
   ghostbody mannequin, drawn as a 2D illustration; the bones show through one window with a rim.
   Both figures are seen from the side, since a head facing the camera grew a face twice in ghostbody.
2. **Every change of state is one of KIND**: slumped against upright, clenched against relaxed, knee past
   the toes against knee behind them, chin on chest against neck in line, folded double against standing,
   jumping against walking. Set 3's three changes of degree came back unchanged, 3 of 3.
3. **No `contour` on the lower back** — it floated off the body 2 of 2. The one contour is on the neck,
   where it held.

| # | question the mark answers | left answer | right answer | mark | badge |
|---|---|---|---|---|---|
| 1 | how open is the hip angle? | narrow | open | `range` | glyph |
| 2 | which part of the fingers presses? | the fingertip joints | the whole finger pads | `fill` | none |
| 3 | where does the body's weight land? | the front knee | down the poles to the ground | `load` | thumb |
| 4 | which way does the neck bend? | sharply forward | in line with the back | `contour` | hazard |
| 5 | how open is the hip angle? | folded shut | open | `range` | hazard |
| 6 | where does the dog's weight land? | the front elbows | spread down the ramp | `load` | glyph |

**Products.** None is in the Sep 8 list and none has a record under this type. Each claims its
category's own mechanism: the kneeling chair opens the hip angle; the pen spreads the grip over the
finger pads; poles take part of the weight on a descent; the wedge props the upper body so the head is
not forced forward; the long horn lets a shoe go on standing; the ramp lets a dog walk down instead of
jumping.

### Predictions, written before the render

1. **Pass**: the ghostbody chair geometry that passed, in a new style. Watch that the mannequin stays 2D
   and the window has a rim.
2. **Partial**: the hand is the frame's whole object; watch whether the red and blue fills sit on
   different parts of the fingers.
3. **Pass on the arrows**, which answered in set 2 and set 3; watch the knee past the toes.
4. **Partial**: a blue line on a muted blue ground is the set's contrast risk, written in on purpose.
5. **Pass**: folded double against standing is the largest change in the set.
6. **Partial**: the type's first animal since the dog harness; watch the front legs buckle.

**Attachments: one reference photo per prompt**; where a product comes in colourways, attach one that is
not red, orange, blue or green. Ratio at the generation tool.

---

## 1 — ergonomic kneeling chair · slate teal, `ghost-mannequin`, `range`

**`TYPE: 02-cause-anatomy v1.18 — SET 4 PROMPT 1`**

```
MEDIUM: 2D illustration, ghost-mannequin: a featureless matte white figure with soft even shading.
NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the ergonomic kneeling chair in
the right panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole seated figure, seen from the side, facing left, the hip small within it. Nothing
is behind the subject but the ground.
GROUND: deep muted slate teal, the right half one step lighter than the left.
[GHOST] the SAME featureless matte white mannequin in both panels, no face, no hair, no clothing, no
skin tone. Only the lower spine, the pelvis and the thigh bone are drawn, in warm ivory, seen
through one window with a visible rim. Exactly one figure in EACH panel, same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are the seat and
what the pelvis does because of it. The pelvis appears in both panels and nothing covers it.
In the left panel, an ordinary flat stool: the thighs lie level, so the hip angle closes, the pelvis
rolls backward and the lower spine slumps.
In the right panel, the reference kneeling chair: it drops the thighs forward, so the hip angle
opens, the pelvis tips forward and the lower spine stands upright.

MARKS, nothing else marked. One shaded wedge in each panel whose two sides lie along the thigh bone
and the lower spine, meeting at the hip joint: red and narrow in the left panel, blue and open in the
right panel. One badge in each panel in the empty ground above the figure, well inside the panel: a
red filled disc with a white X cut out in the left, a green filled disc with a white check cut out in
the right. Same diameter, not rings.
```

---

## 2 — wide-grip ergonomic pen · walnut brown, `line-engraving`, `fill`

**`TYPE: 02-cause-anatomy v1.18 — SET 4 PROMPT 2`**

```
MEDIUM: 2D illustration, line-engraving: fine engraved lines and cross-hatching, like an
antique medical plate, every mark a flat solid fill. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the wide-grip ergonomic pen in the
right panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole right forearm and hand writing on a sheet of plain paper on a desk, seen from the
thumb side, the fingers small within it. Nothing is behind the subject but the ground.
GROUND: deep muted walnut brown, the right half one step lighter than the left.
BODY: only the finger bones and their joints are drawn, in warm ivory; the rest is a translucent
grey outline with no skin colour, no hair and no face. Exactly one hand in EACH panel, same scale
and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are the pen and how
the fingers grip because of it. Each finger joint appears in both panels and nothing covers it.
In the left panel, an ordinary thin plain grey pen: it is too narrow to rest in the hand, so the
fingertips pinch it hard and their end joints bend back.
In the right panel, the reference pen: it is wide enough to rest against the fingers, so they hold it
lightly along their pads.

MARKS, nothing else marked. One flat solid fill in each panel on the part of the fingers that presses
the pen: red on the fingertip joints alone in the left panel, blue along the whole finger pads in the
right panel. No badge in either panel.
```

---

## 3 — trekking poles · heather violet, `flat-vector`, `load`

**`TYPE: 02-cause-anatomy v1.18 — SET 4 PROMPT 3`**

```
MEDIUM: 2D illustration, flat-vector: flat fills, hard edges, no gradients. NOT photography,
NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the trekking poles in the right
panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole figure stepping down a plain grey rocky slope, seen from the side, the front knee
small within it. Nothing is behind the subject but the ground.
GROUND: deep muted heather violet, the right half one step lighter than the left.
BODY: only the thigh bones, the knees and the shin bones are drawn, in warm ivory; the rest is a
translucent grey outline with no skin colour, no hair and no face. Exactly one figure in EACH panel,
same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are what the hands
hold and what the front knee does because of it. The front knee appears in both panels and nothing
covers it.
In the left panel, empty hands: the whole body drops onto the front leg, so the front knee buckles
forward past the toes.
In the right panel, the reference poles planted ahead: they take part of the weight, so the front knee
stays behind the toes.

MARKS, nothing else marked. One single-headed arrow in each panel tracing where the body's weight goes
on the downward step: red, from the hips ending on the front knee in the left panel; blue, from the
hands running down beside the poles and ending on the ground at their tips in the right panel. One
badge in each panel in the empty ground above the figure, well inside the panel: a red filled disc
with a thumbs-down cut out in the left, a green filled disc with a thumbs-up cut out in the right,
each a flat pictogram, a solid silhouette, never a photographed or three-dimensional hand.
```

---

## 4 — bed wedge reading pillow · dusk blue, `airbrushed`, `contour` on the neck

**`TYPE: 02-cause-anatomy v1.18 — SET 4 PROMPT 4`**

```
MEDIUM: 2D illustration, airbrushed: soft gradients, modelled volume. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the bed wedge pillow in the right
panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole figure reading a plain dark tablet in a plain grey bed, seen from the side, the neck
small within it. Nothing is behind the subject but the ground.
GROUND: deep muted dusk blue, the right half one step lighter than the left.
BODY: only the neck vertebrae and the upper back vertebrae are drawn, in warm ivory; the rest is a
translucent grey outline with no skin colour, no hair and no face. Exactly one figure in EACH panel,
same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are what props the
upper body and what the neck does because of it. The neck appears in both panels and nothing covers
it.
In the left panel, a single flat pillow under the head: the body lies flat, so the head is pushed
forward and the chin presses onto the chest.
In the right panel, the reference wedge under the upper back: it raises the whole upper body, so the
neck stays in line with the back.

MARKS, nothing else marked. One curved line in each panel drawn on the front edge of the neck
vertebrae, touching them from the base of the skull to the shoulders: red and bent sharply forward in
the left panel, blue and in line with the back in the right panel. One badge in each panel in the
empty ground above the figure, well inside the panel: a red filled warning triangle in the left, a
green filled disc with a white check cut out in the right.
```

---

## 5 — long-handled shoe horn · forest green, `ghost-mannequin`, `range`

**`TYPE: 02-cause-anatomy v1.18 — SET 4 PROMPT 5`**

```
MEDIUM: 2D illustration, ghost-mannequin: a featureless matte white figure with soft even shading.
NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the long-handled shoe horn in the
right panel. Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole standing figure putting on a plain grey shoe, seen from the side, facing right, the
hip small within it. Nothing is behind the subject but the ground.
GROUND: deep muted forest green, the right half one step lighter than the left.
[GHOST] the SAME featureless matte white mannequin in both panels, no face, no hair, no clothing, no
skin tone. Only the spine, the pelvis and the thigh bones are drawn, in warm ivory, seen through one
window with a visible rim. Exactly one figure in EACH panel, same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are what reaches the
heel and how the body bends because of it. The spine appears in both panels and nothing covers it.
In the left panel, a short plain grey shoe horn: it only reaches the heel from the floor, so the body
folds double at the hips and the spine curves down over the shoe.
In the right panel, the reference long shoe horn held at hip height: it reaches the heel from standing,
so the figure stays upright and the spine stays straight.

MARKS, nothing else marked. One shaded wedge in each panel whose two sides lie along the thigh bone
and the spine, meeting at the hip joint: red and folded shut in the left panel, blue and open in the
right panel. One badge in each panel in the empty ground above the figure, well inside the panel: a
red filled warning triangle in the left, a green filled disc with a white check cut out in the right.
```

---

## 6 — dog ramp · olive khaki, `flat-vector`, `load`

**`TYPE: 02-cause-anatomy v1.18 — SET 4 PROMPT 6`**

```
MEDIUM: 2D illustration, flat-vector: flat fills, hard edges, no gradients. NOT photography,
NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the dog ramp in the right panel.
Preserve shape, proportions, material, finish and colour exactly.

FRAME: the whole dog getting down from a plain grey sofa, seen from the side, the front legs small
within it. Nothing is behind the subject but the ground.
GROUND: deep muted olive khaki, the right half one step lighter than the left.
BODY: only the dog's shoulder blades and front leg bones are drawn, in warm ivory; the rest is a
translucent grey outline with no skin colour, no hair and no face. Exactly one dog in EACH panel,
same scale and same view.

PANELS: two equal panels split by one thin vertical line. The only differences are how the dog gets
down and what the front legs do because of it. The front legs appear in both panels and nothing
covers it.
In the left panel, a jump from the sofa edge to the floor: the whole dog lands on its front paws, so
the front elbows fold under the impact.
In the right panel, the reference ramp from the sofa to the floor: the dog walks down it, so the front
legs stay straight under the shoulders.

MARKS, nothing else marked. One single-headed arrow in each panel tracing where the dog's weight goes:
red, from the chest ending on the front elbows in the left panel; blue, from the chest ending spread
along the ramp under all four paws in the right panel. One badge in each panel in the empty ground
above the figure, well inside the panel: a red filled disc with a white X cut out in the left, a green
filled disc with a white check cut out in the right. Same diameter, not rings.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **As a set — six colours from six products' worlds, still one scientific series?** | the owner's colour finding |
| 2 | **All six — measure the ground: value well below the ivory, saturation between set 3's greys and set 2's fields.** | *deep* and *muted* |
| 3 | **Prompts 1 and 5 — a flat white mannequin with a rimmed window, and no face?** | `ghost-mannequin`, founding evidence |
| 4 | **All six — cover the marks: do the two bodies differ in kind?** | the kind-not-degree rule |
| 5 | **All six — say the question and each panel's answer.** | the one-question mark rule |
| 6 | **Prompt 4 — does the blue line read on the blue ground?** | the contrast risk |
| 7 | **All six — only the named bones in ivory?** | the positive bound |
| 8 | **Five badges — margin to the nearest edge.** | G10 |

---

## RESULT — 2026-09-15, six renders, 0 pass

Six renders in `image-library-assets/feedback/` at 14:11–14:12, each mapped to its prompt by content.
Owner, same day: the kneeling chair *"phân bổ đều trọng lượng lên 3 điểm làm thẳng lưng"* and its render
shows neither feature nor benefit; the pen and the trekking poles show no clear feature or benefit; the
wedge pillow's comparison is wrong and its anatomy wrong.

| # | product | verdict | what broke |
|---|---|---|---|
| 1 | kneeling chair | partial | **the three contact points never drawn**; the left figure upright on a legless floating stool; range triangles on the pelvis |
| 2 | wide-grip pen | partial | **the fingers bend the same on both pens**; red glows, not fills; the whole hand skeleton |
| 3 | trekking poles | **fail** | **the poles held beside the body, and no arrow runs down a pole** |
| 4 | bed wedge pillow | **fail** | **the neck vertebrae on the throat side**, the neck arched back — the comparison argues nothing true |
| 5 | shoe horn | partial | range drawn as cones off the hip; badges 6.2–6.5% from the top |
| 6 | dog ramp | partial | three blue arrows where one was asked |

**Why the feature was missing: the prompts never named it.** Each right panel said what the body did —
*it drops the thighs forward*, *the poles take part of the weight* — and never where the product did it.
G2 keeps a product's appearance out of a prompt; set 4 read that as a ban on naming any part. G2 also
allows a product's relation to other objects, and *both shins rest on its knee pad* is one. The model
drew a chair, a grip and two poles with nothing connecting them to the benefit. **The wedge fault was
separate**: no orientation was named, and the render put the spine on the wrong side of the neck.

**Colour, which drew no comment this time**: grounds measured 0.18–0.42 saturation and 69–147 of 255 —
between set 3's greys and set 2's saturated fields, as the rule aimed. **`ghost-mannequin` rendered clean
in 2 of 2**, featureless and faceless, but neither drew the rimmed window; the bones showed through the
figure and read.

What moved into the type is in its 1.18 CHANGELOG. Set 5 is
`registry/types/sets/02-cause-anatomy-05/`.
