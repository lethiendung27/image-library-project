---
id: 06-relief-scene
step: 6
job: relief
device: scene
version: "2.3"
status: active
replaced_by: null
ratios: ["16:9", "4:3", "3:4"]
channels: [paid-social, advertorial]
requires_product_photo: false
generation_mode: single-pass
axes:
  gaze: [candid, reflect]
variants: []
exempt_from: [G1, G3, G4]
pairs_with: [01-pain-scene]
never_with: []
---

# 06-relief-scene

## PURPOSE
The closing bookend of a pain→relief arc: **a relief scene with a suffering scene inset.** The
same person, twice — living without the problem in the main photograph, enduring it in a small
one — so the change is a change in a life rather than on a surface. No product.

## TRIGGER
use_when: >
  Closing image of an advertorial or final frame of an ads creative, when the
  product's promise is a state of living rather than a feature. Pairs naturally
  with a 01-pain-scene of the same person, and no longer depends on one.
avoid_when: >
  Marketplace galleries, main images, or anywhere the image must stand alone.
  Not when the result is invisible on the body or an object — for invisible
  results the closing image must be 06-relief-hero with the product in frame
  (verified boundary, see the worked example).

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.
A rendered prompt expands what it calls — the model never reads this file (ADR-017).

```
TYPE: 06-relief-scene v2.3
REGISTER: candid documentary photograph, single frame.        -> PARTS/register

[SUBJECT] a person living the resolved state, mid-errand.     -> PARTS/subject
[GAZE] candid, or on a reflection. Never on the lens.         -> PARTS/gaze
[ENVIRONMENT] an ordinary public place they would pass through. -> PARTS/environment
[LIGHT] plain daylight, no glamour.                           -> PARTS/light
[GRADE] muted, desaturated, never warm-boosted.               -> PARTS/grade

[MARKS]                                                       -> MARKS
  past        the problem, a desaturated inset. REQUIRED
  evidence    the same thing resolved, in the hero
  carry-over  one thing identical in both cells
  reflection  optional second angle, in real glass
```

## PARTS

**`register`** — a candid documentary photograph a passer-by could have taken. Natural,
unposed, sharp. Not styled, not lit, not aware of a camera.

**`subject`** — the same demographic and the same person as the paired pain image, in
put-together but ordinary clothes from the same palette family, doing an everyday thing in
public and pausing briefly.

**`gaze`** — `candid`, absorbed in their own business, or `reflect`, on their own image in
glass. Both are existing values of the shared axis. **Never at the camera**: looking at the lens
reads as showing off and the barrier goes up. `reflect` is no longer compulsory, which is what
2.0 changed — `candid` is now the default and the ordinary case.

**`environment`** — a public everyday place the subject would actually pass through, with two
or three incidental blurred passers-by or street details, ordinary weather. Nothing
aspirational, no travel-brochure location, no empty clean street. **The problem started in the
bathroom; the promise ends in the world**, which is why this type is never set at home.

**`light`** — even natural daylight, bright, soft shadows. No golden hour, no rim light, no
glamour lighting. Where a pain counterpart exists, keep the same time-of-day character.

**`grade`** — a muted palette, light film grain, shallow depth of field. Desaturated, never
warm-boosted. The hero is full colour; only `past` is drained.

## MARKS

**Every entry is made of the scene; nothing is drawn over the photograph.** Measured across
three sibling types, a mark of real substance renders reliably (`emission` 7/7, `output` 4/4)
and a drawn mark at small scale does not (`fit` cut at 0/8, `hotspot` 1/3). A desaturated inset
is a photograph, not an overlay, so it sits on the reliable side.

| name | made of | where | evidence |
|---|---|---|---|
| `past` | a photograph of the same person in the pain moment — a SCENE, in full colour | a small inset, 15-25% of the frame, one corner | 0/12 as a drained detail; scene form untested |
| `evidence` | what the person is visibly enduring in one cell and visibly free of in the other — a situation, not a surface | both cells, described absolutely | 4/4 crop match once described absolutely |
| `carry-over` | one thing identical in both cells — the jacket, the doorway, the bag | both cells | **none** — proposal |
| `reflection` | the subject's own image in real glass, at a second angle | optional, one surface | 5/5 rendered; proves nothing alone, and sits quietly beside `past` |

**Whatever `evidence` names must be visible in BOTH cells.** A parting named as the evidence
and then hidden under a clip in the hero leaves the after state absent, however good the inset
is. Check the hero shows the same named thing before anything else.

**`past` is the mechanism and it is REQUIRED.** Two angles are two viewpoints of one moment; a
change needs two moments, so the problem has to be physically in the frame. An unmarked past
cell reads as a result, so the drain is load-bearing rather than stylistic.

**The inset is NOT drained, and dropping the drain dissolves the admission test that went with
it.** A drained cell was inherited from `06-relief-hero`, where the past cell is a mundane
moment that could be read either way and needs marking. **A suffering scene marks itself** —
nobody reads a person enduring the problem as the after state. Draining it only makes the
problem harder to see, and it cost this type a whole class of problems: redness, inflammation
and staining by hue are all legible again now that the cell keeps its colour.

Keep the drain only where a past cell's content is genuinely ambiguous. That is the condition
`06-relief-hero`'s 5 observations actually support, and it is not this type's case.

**`evidence` must be nameable rather than inferred.** "A visibly rested face" renders as an
ordinary person; a collar clean where it was marked is a fact a stranger could point at.

**Describe each cell ABSOLUTELY. Never describe one relative to the other.** "Framed the same
way as the hero" and "smaller in the inset than in the main photograph" are relational
instructions about two compositions the model builds independently, and across eight renders
they never once produced a matching crop — `smaller` was read as `wider shot`, which is the
opposite of the intent and destroys the evidence. Give the inset its own absolute close crop and
give the hero the same body part at its own absolute closeness, and let the match be a
consequence.

**The inset is a SCENE, so it needs enough room to be one.** An earlier version of this rule
said the opposite — crop to the evidence and nothing else — and it was right for the macro
comparison this type had accidentally become and wrong for what it is. Twelve renders of
surfaces argued nothing, however well matched. The inset shows the person, what they are doing,
and enough of where they are to read as a moment: the same framing discipline as the hero, at a
smaller size.

**`carry-over` is what stops the pair changing two things at once.** Hold one thing identical
between inset and hero — the same jacket, the same doorway, the same bag — so the change reads
against something that demonstrably did not change. Changing everything at once isolates
nothing; that cost `06-relief-hero` two renders when a recall inset changed the activity as well
as the product.

**`reflection` is demoted to optional and kept only because it renders.** 4 of 4 came back
plausible, sharp and geometrically consistent, including one holding two subjects in a car door
— the best-executed mechanism this library has had on a first attempt, and it carried no
argument at all. Use it where the evidence genuinely needs a second angle, such as the back of a
head. Never as the thing that makes the case.

## SLOT CONSTRAINTS
- **Never describe the frame's shape or ratio in a prompt.** The owner sets the ratio at render
  time (ADR-016); a prompt reasoning about frame geometry gets extra panels to fill the leftover.
- **The zone names never reach the model.** Region labels are the tier that leaks; whole-image
  and subject labels do not (adapter Rule 1b, tiers set by ADR-017). Describe the region:
  "a shop window fills the left third", not `[REFLECTION]`.
- **No object in the scene may carry printed text.** Model-drawn text arrives as gibberish and
  this type bans text outright. Named newspaper filled two `06-relief-hero` frames with nonsense.
- A clause earns its place only if a render has failed without it, and is removed only once a
  render has done without it and come back correct (ADR-013, ADR-015).

## NEGATIVE
```
[G6] + badges, arrows, drawn overlays, looking at camera, posing, laughing,
undrained past cell, past cell larger than the hero subject,
arms raised, celebration gesture, golden hour, warm flattering light,
glamour lighting, beauty retouching, plastic skin, aspirational travel location,
empty clean street, styled outfit, geometrically wrong reflection,
reflection out of focus, product in frame, saturated colors, stock photo look
```

## WORKED EXAMPLES
### example: skatepark-trainers — skeleton@2.0, run: pass
Product: none in frame (G1-exempt) · axes: gaze=candid · frame delivered 1200x896
**Superseded content model — kept as a record, not as a template.** This was the first frame
that read as before-and-after, and 2.3 retired the model it belongs to: both cells are surfaces,
and the type argues with scenes. The drain and the tonal test it depends on are also gone. What
still holds from it is the discipline of two cells showing the same thing at the same closeness.

```
TYPE: 06-relief-scene v2.0
REGISTER: a candid documentary photograph a passer-by could have taken. Single
frame, natural, unposed, sharp. Nobody aware of a camera.

A young man in dark jeans is sitting on a low concrete step at the edge of a
skatepark, forearms on his knees, looking out at the ramps. Not at the camera.
His white trainers are square on in the lower third of the picture.

The change is in the trainers and it must be a fact anyone could point at: the
toe caps and the midsole are one clean white the whole way round, the rubber
edge unbroken and bright, with no grey scuffing across the toe and no dark
grained line along the midsole.

In the upper right corner sits a small photograph, drained to grey, about a
fifth of the picture wide, with a thin white border. It shows the same trainers
on the same step from the same angle, framed the same way as the trainers in the
main photograph — but the toe caps are grey and abraded and a dark grained line
runs the length of the midsole.

The frayed hem of the same dark jeans falls across the ankle the same way in both
the small photograph and the main one. Nothing else is shared.

An ordinary skatepark on a flat afternoon: a scarred concrete ramp, a chained
bin, a bag dumped on the step behind him, one blurred skater on the far side.

LIGHT: even daylight, bright, soft shadows, no rim light.
GRADE: muted concrete grey and denim blue, light film grain, shallow depth of
field, desaturated, never warm-boosted. Only the small photograph is drained.

No text, no logo, no watermark, no product, no arrows, no badges.
```

### example: car-park-windscreen — skeleton@2.2, run: fail
Product: none in frame (G1-exempt) · axes: gaze=candid · frame delivered 1200x896
- HERO — a woman in her fifties at the wheel of a parked car in a supermarket car park, both
  hands on the wheel, about to set off, looking ahead through clear glass
- INSET — the same windscreen from the same seat, drained to grey, a milky film across the
  middle and a greasy arc where the wipers stop
- CARRY-OVER — the same air freshener on the same mirror stem in both
Kept because it shows the fix rather than only the fault. The crop match is exact — the two
cells are the same view of the same glass, which is what 2.2's absolute descriptions bought
after eight renders that never managed it. And the hero is a real moment: a woman about to
drive somewhere. Then the inset repeats her windscreen as a study of glass and the comparison
drops out of the scene onto a surface. **Keep this hero and make the inset another moment.**

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 2.3 (2026-08-14): both cells are SCENES. Absolute description fixed the crop 4/4 after eight
  failures, and with the crops finally matched the images were plainly macro surface studies —
  a spec device, not a relief scene. Owner's correction: relief scene, suffering scene inset.
  The drain goes with it, because a suffering scene marks itself and draining it only hid the
  problem; the tonal admission test dissolves with the drain, so hue-signalled problems return.
  The crop-to-the-evidence rule is reversed: a scene needs room to be one.
- 2.2 (2026-08-14): the crop is the whole problem. Eight renders never once matched crop
  between the cells, because both rules asking for it were RELATIVE — "framed the same way",
  "smaller in the inset" — and `smaller` was read as `wider shot`. Each cell now gets its own
  absolute description. Two conditions added from a clean 2-2 split: the inset holds the
  evidence and almost nothing else, and whatever `evidence` names must be visible in both cells. `423f1b8`
- 2.1 (2026-08-14): the inset mechanism works, with two conditions the first four renders
  bought. `past` gains an admission test — the drain preserves a TONAL problem and destroys a
  COLOUR one, 2/2 against 0/1, so a hue-signalled problem routes to `06-relief-hero --vsinset`
  instead. `evidence` gains a size floor: the hero's copy is never smaller than the inset's,
  which is exactly how the four renders sort. 2 pass, 1 partial, 1 fail. `c795d1b`
- 2.0 (2026-08-14): the argument moves from two angles to two moments. Four first renders
  returned flawless reflections and no argument, so the founding premise is withdrawn: two
  angles are one moment. `past`, a desaturated inset of the problem, becomes the required
  mechanism — 5 obs and 2/2 on `06-relief-hero`. `reflection` demoted to optional. MAJOR:
  layer structure changes and `requires_pair` is dropped, the before now being in-frame.
  `gaze` gains `candid`; `4:3` added. `59678e1`
- 1.1 (2026-08-14): restructured into a call-map plus PARTS and MARKS (ADR-012); skeleton
  cut. First MARKS library, and all three entries are proposals: this type has 0 observations
  and 0 renders, so there is nothing to count. Every entry is made of the scene, because the
  drawn class is the unreliable one across three sibling types. `ratios` move to ADR-016's set —
  `5:3` and `4:5` become `16:9` and `3:4`. `RATIO:` dropped per adapter Rule 4. `3fb74a2`
- 1.0 (2026-08-10): initial from the shop-window reflection exemplar; --reflect gaze
  mode contributed to the shared gaze axis. seed: conversation.md.
