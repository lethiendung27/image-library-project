# Image prompts — page 37, L-shaped ergonomic seat cushion

GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit the script and re-run.

- page_id `37` · channel `advertorial` · awareness `solution-aware` · registry `2.0.0`
- 15 image slots: 12 routed, 3 out of library scope
- 36 prompts, three per routed slot, one recommended each
- 4 slots earn motion, each with its own runnable loop prompt

Ratio goes in the generation tool's own aspect-ratio parameter, never in the prompt text (adapters/nano-banana.md Rule 4). The `Strictly avoid:` line is not rendered into any prompt (ADR-014); the exclusion list is kept in the JSON's `avoid` field for a model with a real negative channel.

## Read this first

- **HOW THE RECOMMENDATION WAS MADE.** Five criteria, applied in this order and named in every slot's recommendation_basis. C1 FIT — does the type's own use_when name this exact beat, in the copy's own words. C2 PAGE LEGALITY — does the option keep the whole-page recommended set legal under one-type-once, never_with, requires_pair and the page arc. C3 EVIDENCE — how many renders stand behind the variant, the style and every mark it uses, counted from the type file and eval/render-tests.jsonl. C4 PRODUCT PRESENCE — is the product in frame where this section's argument needs it. C5 PROMPT RISK — characters against that type's own measured ceiling, and how many clauses in it have never been rendered. Where two criteria disagree the basis says which one decided and why. It is a suggestion: feedback/picks.jsonl records what you actually chose, not what was suggested.
- **ONE RECOMMENDATION IS NOT THE BASELINE.** story.2 recommends option B over A on C3, because `measure` is the mark that carries that type's whole argument and the type file says flat-vector is the style that holds its dash pattern. Every other slot recommends A. That is not a default — it is what happens when C1 fit and C3 evidence point the same way, which they do everywhere else.
- **AWARENESS STAGE — solution-aware, read from the copy rather than declared.** The hero assumes the reader already believes sitting hurts and goes straight to 'without expensive chairs'; story.1 spends a whole block comparing solution CLASSES the reader has already bought (flat pads, lumbar pillows, chiropractor); the comparison table is class-versus-class, not problem-versus-nothing. The brief's own awarenessStage field agrees ('solution'), but the routing did not read it. At this stage mechanism and physical proof decide, and re-amplifying the problem insults the reader — which is why the header closes rather than opens the wound, and why pain gets exactly one section.
- **INPUT DID NOT VALIDATE.** The pasted export is a Shopify page export, not a content.json: it has no top-level product, and its page is content plus htmlCompiled rather than channel plus sections. content.json in this directory is the contract reassembled from it by hand, and it is STILL not valid against mapping/content.schema.json for one reason — see the next note.
- **GAP 1, reference_photos is empty.** imageBriefs is null and shopifyProductGid is null, so there is no product photo to hash. The schema requires at least one sha256. Eleven of the thirteen types on this page declare requires_product_photo: true, and every prompt below that needs one says 'the attached photo'. Nothing was fabricated: attachments is omitted from every option rather than filled with an invented hash. Supply the photo, hash it (SPEC 6.4), and content.json validates.
- **GAP 2 was not a gap.** The image slots ARE declared, in htmlCompiled as data-field-type="image", not in page.content — 21 of them, of which 15 are library-routable and 6 are reviewer avatars. The avatars are portrait headshots attached to named reviews and are not library slots; they are also the sharpest FTC surface on the page and should be real or absent.
- **PLACEHOLDER ALT TEXT IS TEMPLATE RESIDUE.** Every placehold.co caption in the export describes a furniture-lifter product — 'man rolling cabinet on lifter set', 'sofa gliding on hardwood', 'lever under cabinet'. None of it is a brief for this product and none of it was used. If those captions were meant as image direction, say so and this routing changes.
- **CHANNEL is advertorial, taken from lpTypeId.** That is a hard gate, not a preference: it removes 01-pain-split, 02-symptom-rail, 03-spec-explode, 03-spec-split and 05-persona-grid from every slot on this page, because their own channels lists exclude it.
- **CROSS-SLOT RULES APPLIED.** One-type-once holds across the seven argument slots; the six review-grid cells are one type six times under the repeating-section exception, each differing on a named dimension. 01-pain-scene x 01-pain-split never share a page — moot here, pain-split is off-channel. 06-relief-scene's requires_pair is satisfied by 01-pain-scene at story.0, same person and same palette. Page arc holds: pain and cause precede relief, and pain never reappears after story.4. Step-3 budget holds at one.
- **THE OPTION SET IS NOT A COMBINATION SET.** Every option is legal on its own and the recommended set is legal as a whole, but some pairs are not. hero.image B spends the type story.0 needs. story.4 B spends the type hero.image A uses. story.2 C and story.3 C put a car seat in two consecutive sections. story.0 C and hero.image B put the same driveway in two consecutive images. Each of those is written into the option's own composition_notes; change one option and re-read the two around it.
- **GIF FORM, AND WHY ONLY ONE IS AN INSET.** Step 5c offers the inset form only where the type's own SKELETON already legislates a layer to replace — proposing a NEW layer is a graphic-overlay decision this runbook does not make. On this page exactly one routed slot has such a layer: hero.image option A, whose recall panel is legislated by 06-relief-hero. It takes the inset form, and it is the better half to move — the hero is a held state while the panel holds the transition. The other eleven routed slots have no layer at all by their own law: 01-pain-scene bans insets and panels, 05-social-snapshot is one frame with no layout and no layers, 04-proof-lockedframe has no MARKS section at all, 06-relief-scene bans overlays, and the two panels of 02-cause-anatomy and 03-mechanism-ghostbody are the whole argument rather than a layer inside it. Those slots get whole-frame or nothing.
- **EVERY GIF CARRIES A RUNNABLE PROMPT, not just a brief.** It animates the still the recommended option produces and never regenerates it, so the loop cannot drift from the image the page has already approved. The five-field brief stays as the human summary.
- **REVIEW GRID, THE ONE DECISION THAT IS NOT MINE.** 05-social-snapshot carries a hard authenticity fence: never a reviewer name, avatar, star row or verified label near the image, and never presented as a customer upload. In the markup the six-up grid is uncaptioned, which satisfies the fence — but it sits directly under a carousel of five named reviews with avatars and Verified Purchase badges. Ship these as page imagery with no caption tying them to a person and the fence holds. Caption them as customer photos and it is a fabricated endorsement. If real customer photos exist, they win outright.
- **NO PRODUCT IN FRAME AT story.1 OPTION A.** That is what --rivals is, and it is legal on advertorial. It is also the one place the recommendation knowingly fails criterion C4: the copy has not named the cushion yet, and putting it in the last panel here spends the reveal story.3 exists to make. Option B is the pick if the product must be visible this early.
- **04-proof-lockedframe RUNS HANDHELD.** Its strict camera needs compositing, which is not available in this pipeline, so all three options generate three frames separately and the slight framing drift between them is honest. The panel-1 prompt deliberately carries no multi-panel language; the panel list lives in the edit steps.
- **PICKS PRIOR NEVER FIRED.** feedback/picks.jsonl has no records, so the 20-pick tie-breaker in runbook Step 3.5 did not run. Everything here is argued from the type files and the ledger, not from conversion evidence — this page is argument-complete, not conversion-optimised.
- **EVERY MARK IN 03-mechanism-ghostbody IS UNPROVEN — zero records in eval/render-tests.jsonl.** Whichever option ships at story.3, log the render: it is that type's founding evidence.

## Slot map

| slot | role | asset | recommended | ratio | gif |
|---|---|---|---|---|---|
| `hero.image` | hero | `01-hero-relief-hero-ugc.jpg` | **A** — 06-relief-hero 1.12 `--ugc, inset --recall (FORM 1)` | 16:9 | inset |
| `story.0.image` | problem-agitation | `02-story0-pain-scene.jpg` | **A** — 01-pain-scene 1.14 `--candid --marked` | 4:3 | whole-frame |
| `story.1.image` | comparison | `03-story1-rivals.jpg` | **A** — 04-proof-lockedframe 1.13 `--rivals` | 4:3 | none |
| `story.2.image` | cause | `04-story2-cause-anatomy.jpg` | **B** — 02-cause-anatomy 1.15 `--diagnostic` | 4:3 | whole-frame |
| `story.3.image` | mechanism | `05-story3-ghostbody.jpg` | **A** — 03-mechanism-ghostbody 2.2 | 4:3 | none |
| `story.4.image` | outcome | `06-story4-relief-scene.jpg` | **A** — 06-relief-scene 1.0 | 4:3 | whole-frame |
| `story.5.image` | cta | `(supplied)` | — out of scope | — | none |
| `reviews.gallery.0.image` | social-proof | `07-review-grid-kitchen-chair.jpg` | **A** — 05-social-snapshot 1.0 | 1:1 | none |
| `reviews.gallery.1.image` | social-proof | `08-review-grid-car-seat.jpg` | **A** — 05-social-snapshot 1.0 | 1:1 | none |
| `reviews.gallery.2.image` | social-proof | `09-review-grid-gaming-chair.jpg` | **A** — 05-social-snapshot 1.0 | 1:1 | none |
| `reviews.gallery.3.image` | social-proof | `10-review-grid-hallway-unbox.jpg` | **A** — 05-social-snapshot 1.0 | 1:1 | none |
| `reviews.gallery.4.image` | social-proof | `11-review-grid-wheelchair.jpg` | **A** — 05-social-snapshot 1.0 | 1:1 | none |
| `reviews.gallery.5.image` | social-proof | `12-review-grid-lorry-cab.jpg` | **A** — 05-social-snapshot 1.0 | 1:1 | none |
| `offer.image` | cta | `(supplied)` | — out of scope | — | none |
| `hero.sidebar.image` | cta | `(supplied)` | — out of scope | — | none |

## Coverage

**Covered**

- 1 pain — 01-pain-scene at story.0
- 2 cause — 02-cause-anatomy at story.2
- 3 mechanism — 03-mechanism-ghostbody at story.3
- 4 proof — 04-proof-lockedframe --rivals at story.1
- 5 social — 05-social-snapshot across the six review-grid cells
- 6 relief — 06-relief-hero at the header, 06-relief-scene at story.4

**Absent**

- 3 mechanism, second answer — the spec/build rung: what is actually inside the thing

**Absent on purpose**

- how-to-use — multi_step_usage is false. Placing a cushion on a chair is one obvious action, and 03-use-sequence's own avoid_when rules it out.
- personas — 05-persona-grid is not legal on advertorial, and the six review-grid cells already carry the breadth of audience across six separate rooms.

**Gaps**

- None that this channel can fill. The spec rung is genuinely absent and a solution-aware reader comparing constructions would use it — but both types that answer it, 03-spec-explode and 03-spec-split, exclude advertorial in their own channels list, and 03-mechanism-xray's use_when covers products that do NOT act on a body structure. Refusing a wrong type is correct; there is nothing to propose here, so recommended[] is empty.

---

## Prompts

### `hero.image` — hero

*advertorial header, full width above the byline (700x394 in the export)* · asset `01-hero-relief-hero-ugc.jpg`

**Recommended: option A.** C1 and C4 together. The type's own --ugc block names 'advertorial header' as a channel, and A is the only one of the three that puts the product in the header at all — B carries none by definition and C is the same argument in a duller room. C2 also bites: picking B spends 01-pain-scene, which story.0 needs for its exact beat and which 06-relief-scene depends on for its pair. C3 backs it — the recall inset's `past` mark is 2 of 2 rendered.

**GIF · 3s · ping-pong · form `inset`** — The type's SKELETON already legislates the recall panel, so motion replaces a layer that exists rather than adding one. And it is the right half to move: the hero is a held state with nothing to show changing, while the panel holds the transition the whole page is about.

```
SHOT     Locked frame; only the corner panel moves
ACTION   In the panel he levers himself out, stalls
RESULT   The past still hurts; the present does not
MATCH    Panel stays grey, hero keeps its colour
```

Loop prompt — run it on the still option A produces. Delivery: mp4/webm, under 2 MB.

```prompt
MOTION FROM THE STILL — animate the generated hero image, do not
regenerate it.
Animate ONLY the small rectangular panel in the upper left corner. Everything
outside that panel is completely frozen: the man, the car, the light and the
grain do not move at all.
Inside the panel: the same man twists sideways, hauls himself up out of the
driver's seat by the door frame, stalls halfway with his hips still folded,
then settles back down. The panel stays fully desaturated to grey throughout
and keeps the same sharpness as the frame around it.
No camera move, no zoom, no crossfade, no added elements, no text.
```

#### Option A — 06-relief-hero 1.12 `--ugc, inset --recall (FORM 1)`  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **16:9** · single-pass · 1881 characters
- why: The headline is relief-framed ('How I Finally Ended My Sitting Pain'), so the header has to close the loop, not open a wound. The recall panel keeps the problem present without letting pain into the hero, which this type forbids.
- note: Rung-2 derivation, declared: mapping/slot-rules.md gives advertorial hero to 01-pain-scene, but that type is spent at story.0 by the exact beat it exists for, and 06-relief-hero's own --ugc block names 'advertorial header' as a channel. G7-X holds: seated in the car in both the hero and the panel. The zone names never reach the model — the panel is described by its corner.

```prompt
TYPE: 06-relief-hero v1.12 --ugc, inset --recall
REGISTER: shot on a phone by an ordinary person. Slightly off exposure, mild
overexposure on skin and on the windscreen, no rim light, framing casual and a
little too close. The car is left exactly as it is.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion, identical in
every layer. Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT]
Man in his late forties in an open-collar work shirt, sitting in the driver's
seat of an ordinary estate car at the end of the working day, seen from a
front three-quarter angle through the open driver's door. He is settled back,
one hand loose on the wheel, gaze out through the windscreen, an unforced ease
about him.

[PRODUCT]
The cushion in place beneath and behind him: its seat section under his hips,
its lumbar section rising into the small of his back, the line of contact
continuous with no gap left behind the lumbar curve. Unobstructed and legible.

[SETTING]
The car filled to the edges with things that belong there: a travel mug in the
console, a lanyard on the mirror, a folded jacket on the passenger seat, a
phone mount, hedges and a driveway beyond the open door. None of them carries
printed words. Background soft but never blank.

[LIGHT]
Flat late-afternoon daylight through the windscreen and the open door. No
studio light, no rim light.

[LAYOUT]
He sits to the right of the frame. In the upper left corner sits one small
rectangular panel about a sixth of the picture's width, and nothing else
occupies that side.

[PANEL CONTENT]
The same man in the same car on an earlier day, twisted sideways and gripping
the door frame to lever himself out, face tight. This panel is fully
desaturated to grey while the rest of the picture keeps its colour, and it
matches the main picture in sharpness and light quality.
```

#### Option B — 01-pain-scene 1.14 `--candid`

- varies on: type: 01-pain-scene
- ratio parameter: **16:9** · single-pass · 1271 characters
- why: The slot-rules cell for advertorial hero, taken literally. The subtitle IS pain-framed ('Why standard cushions leave you stiff-legged and exhausted'), so a cold-open header is defensible.
- note: PICKING THIS FORCES A RE-ROUTE: 01-pain-scene would then be spent here and story.0 needs its own answer, and 06-relief-scene at story.4 must pair with whichever pain-scene survives (same person, same palette). No product in frame — this type carries none by definition.

```prompt
TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his late forties in an open-collar work shirt, half out of the driver's
seat of an estate car on his own driveway, both hands braced — one on the door
frame, one on the seat back — levering himself upward. Under that force: the
hips still folded, one shoulder driven up, the trailing leg dragging rather
than stepping, the whole body rising in one stiff block instead of unfolding.
Face: jaw set, eyes down, breath held.

[EVIDENCE]
The driver's seat he is leaving has a deep gap where its base meets the
backrest, and a flattened foam pad has slid forward and folded into it.

[ENVIRONMENT]
A suburban driveway at the end of the working day, with the clutter of that
routine: a lunch bag on the passenger seat, a lanyard swinging from the
mirror, a wheelie bin by the gate, a neighbour's hedge. Nothing tidied.

[GAZE] unaware of the camera, gaze down at the ground by his feet.

[LIGHT] low-key. Key: low late-afternoon sun from behind the car, hard. Weak
fill. Deep shadow through the open door.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth
of field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
```

#### Option C — 06-relief-hero 1.12 `--ugc, inset --recall (FORM 1)`

- varies on: execution: the desk at the end of the day instead of the car
- ratio parameter: **16:9** · single-pass · 1829 characters
- why: Same type, same axes, a simpler room. The car interior is the harder generation — a three-quarter view through an open door has to hold the cushion, the man and the panel at once. This is the fallback that keeps the argument if A comes back cramped.
- note: Rear three-quarter angle so the contact line reads. Costs the driver half of the audience, which the review grid then has to carry alone.

```prompt
TYPE: 06-relief-hero v1.12 --ugc, inset --recall
REGISTER: shot on a phone by an ordinary person. Slightly off exposure, mild
overexposure on skin and on the window, no rim light, framing casual and a
little too close. The room is left exactly as it is.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion, identical in
every layer. Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT]
Man in his late forties in an open-collar work shirt, at his own desk near the
end of the working day, seen from a rear three-quarter angle. He is leaned
back with his weight through his hips, one arm hooked over the chair back,
half turned to answer somebody out of frame, relaxed and unhurried.

[PRODUCT]
The cushion in place on the chair beneath and behind him: its seat section
under his hips, its lumbar section against his lower back, the line of contact
continuous and unobstructed from this angle.

[SETTING]
His own office corner filled to the edges with what lives there: a keyboard
pushed back, a mug, a coat on a hook, a stack of trays, a cable run along the
skirting, a window with the blind half down. None of them carries printed
words. Background soft but never blank.

[LIGHT]
Flat late-afternoon daylight from the window plus the overhead strip light. No
studio light, no rim light.

[LAYOUT]
He sits to the right of the frame. In the upper left corner sits one small
rectangular panel about a sixth of the picture's width, and nothing else
occupies that side.

[PANEL CONTENT]
The same man at the same desk on an earlier day, both hands driving down on
the armrests to push himself up, hips still folded, face tight. This panel is
fully desaturated to grey while the rest of the picture keeps its colour, and
it matches the main picture in sharpness and light quality.
```

---

### `story.0.image` — problem-agitation

*beside story block 0, 'My 3:00 PM Office Nightmare' (600x450)* · asset `02-story0-pain-scene.jpg`

**Recommended: option A.** C1 and C3. The copy's scene is the desk at three in the afternoon and A is that scene verbatim — C moves it to the front door, which the copy reaches two sentences later and which the hero already covers. On C3 the mark is safe here: `glow` has 7 renders, the fault has a place a viewer could put a finger on, and red glow on a BODY is confirmed to read as pain. B is the control to run if the glow comes back reading as a tint rather than a mark.

**GIF · 2s · ping-pong · form `whole-frame`** — The slot's declared reason to exist is the act of standing up out of the chair — a transition, so it is temporal. The type bans insets and panels, so there is no layer to animate instead.

```
SHOT     Locked frame, medium, no camera move
ACTION   He pushes up, stalls, hips stay folded
RESULT   Standing up is the hard part
MATCH    Desaturated blue-grey grade, film grain
```

Loop prompt — run it on the still option A produces. Delivery: mp4/webm, under 2 MB.

```prompt
MOTION FROM THE STILL — animate the generated image, do not
regenerate it. Locked camera, no zoom, no pan.
He drives his weight down through both hands on the armrests, rises a few
centimetres, stalls with his hips still folded and his shoulders up around his
ears, then eases back down. The chair rolls back slightly under him.
Everything else in the office stays still.
The red glow stays exactly where it is on his lower back: it does not pulse,
travel, brighten or spread.
Hold the grade: desaturated blue-grey, crushed blacks, visible film grain.
No added marks, no overlays, no text.
```

#### Option A — 01-pain-scene 1.14 `--candid --marked`  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **4:3** · single-pass · 1601 characters
- why: The copy's own scene, beat for beat: the ache starts at the desk in mid-afternoon and standing up is the hard part. The type's use_when names exactly this — cold traffic, the opening image of a story.
- note: Mark admission gate passed: the fault has a PLACE (the lower back against the chair gap), so a glow can locate it. Exactly one mark, count closed in its own slot. No product — this type carries none.

```prompt
TYPE: 01-pain-scene v1.14 --candid --marked
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his late forties in an open-collar work shirt, at an office desk in
mid-afternoon, part-way through pushing himself up out of the chair: both
hands driving down on the armrests, hips half risen, the chair rolling back a
little under him. Under that force: the shoulders hunched up towards his ears,
the neck set, one heel dug into the carpet.
Face: eyes screwed shut, breath held, teeth set.

[EVIDENCE]
The chair he is leaving has a deep gap where the seat base meets the backrest,
and a flattened grey foam cushion has slid forward and folded into it.

[ENVIRONMENT]
An ordinary open-plan office, mid-afternoon. The lived-in clutter of that
place: a cold mug, a lanyard over a monitor, a coat on the chair back, papers
pushed aside. Nothing arranged, nothing removed to tidy the frame.

[GAZE] unaware of the camera, gaze down at the desk.

[LIGHT] low-key. Key: low sun through a blind at the left, hard and warm.
Fill: weak overhead strip light. Rim along the shoulder. Deep shadow across
most of the frame.

[MARK]
ONE soft red radial glow covering THE LOWER BACK where it meets the chair gap,
fading out before it reaches his shoulders or the seat. It is the only mark in
this image.

[FORBIDDEN] No insets, no split panels, no badges, no glyphs. Nothing else in
the frame is marked.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth
of field, 35mm. Red appears only in the glow.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
```

#### Option B — 01-pain-scene 1.14 `--candid`

- varies on: axis: marked=off
- ratio parameter: **4:3** · single-pass · 1434 characters
- why: The type says --marked is a choice and a set should carry mark-free cases deliberately: a mark competes with the evidence it points at. Here the body's own line is the evidence, and the rucked shirt replaces the glow.
- note: Same scene as A with the mark removed and one physical detail added in its place, so the pair tests whether the glow is earning anything.

```prompt
TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his late forties in an open-collar work shirt, at an office desk in
mid-afternoon, part-way through pushing himself up out of the chair: both
hands driving down on the armrests, hips half risen, the chair rolling back a
little under him. Under that force: the shoulders hunched up towards his ears,
the neck set, one heel dug into the carpet.
Face: eyes screwed shut, breath held, teeth set.

[EVIDENCE]
The chair he is leaving has a deep gap where the seat base meets the backrest,
and a flattened grey foam cushion has slid forward and folded into it. His
shirt is rucked up out of his waistband where his back has been pressed into
that gap all afternoon.

[ENVIRONMENT]
An ordinary open-plan office, mid-afternoon. The lived-in clutter of that
place: a cold mug, a lanyard over a monitor, a coat on the chair back, papers
pushed aside. Nothing arranged, nothing removed to tidy the frame.

[GAZE] unaware of the camera, gaze down at the desk.

[LIGHT] low-key. Key: low sun through a blind at the left, hard and warm.
Fill: weak overhead strip light. Rim along the shoulder. Deep shadow across
most of the frame.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth
of field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
No marks, no overlays, no insets, no panels.
```

#### Option C — 01-pain-scene 1.14 `--candid --marked`

- varies on: execution: the front door in the evening instead of the desk
- ratio parameter: **4:3** · single-pass · 1644 characters
- why: The copy's other pain image, in its own words: 'I would hobble to my front door like an 80-year-old man'. A step is a harder, more legible test of a stiff back than a chair is.
- note: Only take this if hero option A stays (the car) — C plus hero B would put the same driveway in two consecutive images. The mark sits above the belt here because the bag would otherwise cover the chair-gap anchor A uses.

```prompt
TYPE: 01-pain-scene v1.14 --candid --marked
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his late forties in an open-collar work shirt with a bag still over one
shoulder, at his own front door in the evening, mid-way through the last two
steps up to it: one hand pressed flat on the door frame taking his weight, the
other holding keys but not reaching the lock yet. Under that force: the
leading knee locked straight, the trailing foot scuffing the step instead of
lifting, the hips leading and the shoulders trailing behind them.
Face: eyes down, mouth set, breath held.

[EVIDENCE]
Behind him on the driveway the car door still stands open, and a flattened
foam pad has slid forward and folded into the gap at the back of the driver's
seat.

[ENVIRONMENT]
An ordinary suburban front step in the evening, with the clutter of that
routine: a recycling box by the wall, a pair of muddy boots, a bike against
the fence, a bin bag not yet taken out. Nothing tidied.

[GAZE] unaware of the camera, gaze down at the step.

[LIGHT] low-key. Key: the porch light overhead, hard and warm. Fill: weak
blue dusk from the street. Deep shadow under the door frame.

[MARK]
ONE soft red radial glow covering THE LOWER BACK just above his belt, fading
out before it reaches his shoulders or the bag. It is the only mark in this
image.

[FORBIDDEN] No insets, no split panels, no badges, no glyphs. Nothing else in
the frame is marked.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth
of field, 35mm. Red appears only in the glow.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
```

---

### `story.1.image` — comparison

*beside story block 1, 'I Spent Hundreds On Half-Measures' (600x450)* · asset `03-story1-rivals.jpg`

**Recommended: option A.** C1 decides it: this type's use_when is written for this exact section, 'the I tried three things beat of an advertorial', and the three panels are the three things the copy names. A fails C4 — no product in frame — and that is the deliberate trade: the copy has not named the cushion yet, and putting it in the last panel here spends the reveal story.3 exists to make. Take B if the page must show the product this early; take C only if the page is being aimed at drivers rather than desk workers.

**No GIF.** The slot exists to hold three states side by side for comparison, not to show one thing changing. A census is spatial, not temporal, and motion would only pull the eye to whichever panel moves.

#### Option A — 04-proof-lockedframe 1.13 `--rivals`  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **4:3** · multi-pass · 1102 characters
- why: This type's use_when is written for this exact section: 'the I tried three things beat of an advertorial'. The three panels are the three things the copy names — a flat pad, a separate lumbar pillow, and the improvised fix.
- note: THE ONE SLOT WITH NO PRODUCT IN FRAME. That is what --rivals is: none of them wins and the image makes no claim. Legal on advertorial only. CAPABILITY GATE: the strict camera needs compositing, which is not available here, so this runs handheld — the frames are three separate generations and the slight framing drift is honest, not a fault.

```prompt
TYPE: 04-proof-lockedframe v1.13 --rivals — PANEL 1 GENERATION
REGISTER: documentary photography. No overlays, badges, arrows or text.

[SCENE]
An unremarkable mesh-backed office chair pulled out from the corner of a desk,
photographed from a standing position slightly above seat height. Office
carpet, daylight from one window to the left, a few ordinary desk objects
visible on the desk edge behind the chair. Nothing styled, nothing tidied.

[SUBJECT OF THIS FRAME]
A flat square foam seat pad lying on the seat base — ordinary, in good
condition, the kind sold everywhere, compressed thin through the middle where
someone has been sitting on it. The gap where the seat base meets the backrest
is clearly visible behind it and is still open: the pad does not reach it.

[GRADE] Muted and cool.

[FAIRNESS] The pad is not dirty, torn or worn out. It is photographed with the
same respect any product would get: honest exposure, no hero light, no styling
that flatters or condemns it.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
No people, no hands, no brand marks.
```

**Pipeline**

1. Pass 1 — generate the frame above as a single image. It carries no multi-panel language at all: one seat, one item on it.
2. Pass 2 — edit that image: 'Keep the chair, the desk, the carpet, the window light, the objects on the desk edge and the camera position. Remove the foam pad from the seat. Buckle a separate strap-on lumbar pillow to the backrest, in good condition, its lower edge stopping well above the seat base so the seat-to-backrest gap stays open. Reshoot from a standing position, so framing and angle shift slightly the way a hand-held camera does.'
3. Pass 3 — edit the pass-1 image again: 'Keep the chair, the desk, the carpet, the window light, the objects on the desk edge and the camera position. Remove the foam pad. Push a neatly folded bath towel into the gap between the seat base and the backrest, the way somebody actually does it. Reshoot from a standing position, so framing and angle shift slightly the way a hand-held camera does.'
4. Assembly — place the three frames side by side in the page layout, in this order, with thin white gutters and no outer border. No panel is retouched to be brighter or cleaner than the others.

#### Option B — 04-proof-lockedframe 1.13 `--verdict`

- varies on: axis: variant=verdict
- ratio parameter: **4:3** · multi-pass · 1130 characters
- why: Same locked frame, but the product takes the last panel. Choose this if the section should resolve rather than only indict — the reader at this stage is sceptical of everything, and the copy has not yet named the cushion.
- note: Fairness rule binds hard: panels 1 and 2 get identical exposure, tidiness and framing generosity, and the difference must be visible in the OBJECTS, never in the lighting. It may win by physics, never by treatment. Product last — left-to-right reading ends on it.

```prompt
TYPE: 04-proof-lockedframe v1.13 --verdict — PANEL 1 GENERATION
REGISTER: documentary photography. No overlays, badges, arrows or text.

[SCENE]
An unremarkable mesh-backed office chair pulled out from the corner of a desk,
photographed from a standing position slightly above seat height. Office
carpet, daylight from one window to the left, a few ordinary desk objects
visible on the desk edge behind the chair. Nothing styled, nothing tidied.

[SUBJECT OF THIS FRAME]
A flat square foam seat pad lying on the seat base — ordinary, in good
condition, the kind sold everywhere, compressed thin through the middle where
someone has been sitting on it. The gap where the seat base meets the backrest
is clearly visible behind it and is still open: the pad does not reach it.

[GRADE] Neutral, honest to the room.

[FAIRNESS] The pad is not dirty, torn or worn out. It gets exactly the same
photographic respect as every other frame in this test: identical exposure,
identical tidiness, identical framing generosity.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
No people, no hands, no brand marks.
```

**Pipeline**

1. Pass 1 — generate the frame above as a single image. It carries no multi-panel language at all: one seat, one item on it.
2. Pass 2 — edit that image: 'Keep the chair, the desk, the carpet, the window light, the objects on the desk edge and the camera position. Remove the foam pad from the seat. Buckle a separate strap-on lumbar pillow to the backrest, in good condition, its lower edge stopping well above the seat base so the seat-to-backrest gap stays open. Reshoot from a standing position, so framing and angle shift slightly the way a hand-held camera does.'
3. Pass 3 — edit the pass-1 image again, with the product photo attached: 'Keep the chair, the desk, the carpet, the window light, the objects on the desk edge and the camera position. Remove the foam pad. Put the attached cushion on the chair instead, its seat section on the seat base and its lumbar section filling the gap against the backrest, matching the attached photo exactly. Same exposure and same tidiness as the other frames, no hero light. Reshoot from a standing position, so framing and angle shift slightly the way a hand-held camera does.'
4. Assembly — place the three frames side by side with thin white gutters, product LAST. Order rule: left-to-right reading ends on the product, and that is the resolution position.

#### Option C — 04-proof-lockedframe 1.13 `--rivals`

- varies on: execution: a car driver's seat instead of an office chair
- ratio parameter: **4:3** · multi-pass · 1093 characters
- why: Half the persona is long-distance drivers, and the narrator's worst moment is the drive home. The three failed fixes are the ones a driver actually owns: a service-station pad, an inflatable roll, a rolled towel.
- note: Same variant and camera as A, different subject class. Pairs naturally with hero option A, which is also in the car; against hero C it leaves the office unrepresented until story.2.

```prompt
TYPE: 04-proof-lockedframe v1.13 --rivals — PANEL 1 GENERATION
REGISTER: documentary photography. No overlays, badges, arrows or text.

[SCENE]
The driver's seat of an ordinary saloon car, photographed through the open
driver's door from just outside it, at about seat height. Worn upholstery, a
gritty floor mat, daylight through the windscreen, the steering wheel and door
card in frame. Nothing styled, nothing tidied.

[SUBJECT OF THIS FRAME]
A flat square foam seat pad lying on the seat base — ordinary, in good
condition, the kind sold at every service station, compressed thin through the
middle where someone has been sitting on it. The gap where the seat base meets
the backrest is clearly visible behind it and is still open: the pad does not
reach it.

[GRADE] Muted and cool.

[FAIRNESS] The pad is not dirty, torn or worn out. It is photographed with the
same respect any product would get: honest exposure, no hero light, no styling
that flatters or condemns it.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
No people, no hands, no brand marks.
```

**Pipeline**

1. Pass 1 — generate the frame above as a single image. It carries no multi-panel language at all: one seat, one item on it.
2. Pass 2 — edit that image: 'Keep the seat, the door card, the steering wheel, the floor mat, the light through the windscreen and the camera position. Remove the foam pad from the seat. Strap an inflatable lumbar roll to the backrest, in good condition, its lower edge stopping well above the seat base so the seat-to-backrest gap stays open. Reshoot from a standing position, so framing and angle shift slightly the way a hand-held camera does.'
3. Pass 3 — edit the pass-1 image again: 'Keep the seat, the door card, the steering wheel, the floor mat, the light through the windscreen and the camera position. Remove the foam pad. Push a rolled bath towel into the gap between the seat base and the backrest, the way somebody actually does it. Reshoot from a standing position, so framing and angle shift slightly the way a hand-held camera does.'
4. Assembly — place the three frames side by side in the page layout, in this order, with thin white gutters and no outer border. No panel is retouched to be brighter or cleaner than the others.

---

### `story.2.image` — cause

*beside story block 2, 'The Pelvic Roll Trap Discovered' (600x450)* · asset `04-story2-cause-anatomy.jpg`

**Recommended: option B.** C3, against the baseline. `measure` is the mark that carries this type's whole argument, and the type file says flat-vector is the style that HOLDS its dash pattern — that outranks A's advantage on the third mark, where `force` has 6 renders against `pressure`'s 3 of 6. A third mark is decoration next to the pair that makes the claim. C1 is a tie: all three are the same beat. C is the driver's version and stays available if the page leans that way, but its `aura` mark adds nothing the measure pair does not already say.

**GIF · 3s · ping-pong · form `whole-frame`** — The declared argument is a pelvis rolling backward into a void — a state changing, which is temporal. The two panels are the whole argument rather than a layer inside it, so there is no inset to replace and the loop takes the frame.

```
SHOT     Static illustration, no camera move
ACTION   Pelvis rolls back, lumbar curve collapses
RESULT   The gap is what does it
MATCH    Flat 2D illustration, G3 palette only
```

Loop prompt — run it on the still option B produces. Delivery: mp4/webm, under 2 MB.

```prompt
MOTION FROM THE STILL — animate the generated two-panel
illustration, do not regenerate it. No camera move.
In the LEFT panel only: the sacrum slides back into the gap, the pelvis rolls
backward and the lumbar curve collapses into a backward bow, then returns. The
RIGHT panel is completely still.
The dashed measure line in the left panel stretches with the distance it spans
and stays anchored at both of its landmarks. The badges do not move, blink,
scale or change colour.
Palette unchanged: red wrong, blue correct, green badge, warm ivory structure.
No new marks, no text, no numbers.
```

#### Option A — 02-cause-anatomy 1.15 `--diagnostic`

- varies on: baseline
- ratio parameter: **4:3** · single-pass · 2014 characters
- why: The section names a culprit object and its mechanism — 'standard chairs have a deep gap at the backrest, the pelvis rolls backward into this void'. That is this type's sentence exactly.
- note: REMOVAL TEST PASSED: take the chair's gap away and the pelvis stops rolling, so the two panels are one structure in two states rather than accumulated damage. measure admission passed: the gap spanned goes from a real distance to contact, well past the 2:1 floor.

```prompt
TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, airbrushed with soft gradients and modelled volume.
NOT photography, NOT 3D.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cushion.

[FRAME] The whole seated body in shot in both panels, the chair small within
it.

[GROUND] A dark teal field, stepping once in value at the divider: the right
half one clear step lighter.

[BODY] Exactly one seated figure per panel, same scale and same side view in
both: the pelvis, sacrum and lumbar spine in warm ivory inside a translucent
seated outline. Not a full skeleton, no skull.

[PANELS]
LEFT, wrong: the figure sitting on an ordinary office chair, drawn
realistically and unbranded, with an open gap where its seat base meets its
backrest. The sacrum has slid back into that gap, the pelvis has rolled
backward, and the lumbar curve has collapsed into a backward bow.
RIGHT, correct: the same figure at the same interface, sitting on the
reference cushion, drawn at a size and angle where its L shape is obvious. The
seat section is under the hips and the lumbar section fills the gap against
the sacrum; the pelvis stands upright and the lumbar curve holds its forward
arch.
The spine appears in both panels. The chair and the cushion each touch the
pelvis where they act, and neither covers it.

[MARKS] Three marks, no others.
measure: two dashed straight lines, one per panel, identical in thickness and
dash pattern, each running from the front face of the backrest to the back of
the sacrum and stopping at both. Red left, blue right. Only the distance
spanned differs.
force: one red double-headed curved arrow, left panel only, following the seat
surface backward into the gap.
verdict: one badge in the top corner of each panel, a filled solid disc with
the glyph cut out of it, same diameter in both: red with an X on the left,
green with a check on the right.

Red is wrong, blue is correct, green is the badge, warm ivory is structure;
nothing else carries colour.
```

#### Option B — 02-cause-anatomy 1.15 `--diagnostic`  ← RECOMMENDED

- varies on: axis: style=flat-vector, third mark=pressure
- ratio parameter: **4:3** · single-pass · 2047 characters
- why: Flat vector holds the measure dash pattern, which is the mark that carries the argument. pressure then answers a second question the copy raises — where the load actually lands once the pelvis has rolled.
- note: Same removal test, same measure pair. pressure is a filled region bounded by the contact surface, never a line and never an edge glow — that distinction is what the mark failed on before.

```prompt
TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, flat vector: flat fills, hard edges, no gradients.
NOT photography, NOT 3D.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cushion.

[FRAME] The whole seated body in shot in both panels, the chair small within
it.

[GROUND] A deep indigo field, stepping once in value at the divider: the right
half one clear step lighter.

[BODY] Exactly one seated figure per panel, same scale and same side view in
both: the pelvis, sacrum and lumbar spine in warm ivory inside a translucent
seated outline. Not a full skeleton, no skull.

[PANELS]
LEFT, wrong: the figure sitting on an ordinary office chair, drawn
realistically and unbranded, with an open gap where its seat base meets its
backrest. The sacrum has slid back into that gap and the pelvis has rolled
backward.
RIGHT, correct: the same figure at the same interface, sitting on the
reference cushion, drawn at a size and angle where its L shape is obvious, the
seat section under the hips and the lumbar section filling the gap against the
sacrum, the pelvis upright.
The spine appears in both panels. The chair and the cushion each touch the
pelvis where they act, and neither covers it.

[MARKS] Three marks, no others.
measure: two dashed straight lines, one per panel, identical in thickness and
dash pattern, each running from the front face of the backrest to the back of
the sacrum and stopping at both. Red left, blue right. Only the distance
spanned differs.
pressure: one filled region per panel bounded by the contact surface between
the body and the seat, as wide as that contact and never a line or an edge
glow — red left where load falls on the tailbone, blue right where it
spreads across the seat.
verdict: one badge in the top corner of each panel, a filled solid disc with
the glyph cut out of it, same diameter in both: red with an X on the left,
green with a check on the right.

Red is wrong, blue is correct, green is the badge, warm ivory is structure;
nothing else carries colour.
```

#### Option C — 02-cause-anatomy 1.15 `--diagnostic`

- varies on: execution: a car driver's seat as the culprit, aura as the third mark
- ratio parameter: **4:3** · single-pass · 1958 characters
- why: The same trap in the other seat the persona sits in all day. A car seat has a deeper, more obvious gap than an office chair, which makes the measure pair easier to read.
- note: aura is blue and right-panel only, so it cannot read as harm the product causes. Subject class is this type's widest diversity lever — the culprit changes, the anatomy does not.

```prompt
TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, airbrushed with soft gradients and modelled volume.
NOT photography, NOT 3D.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cushion.

[FRAME] The whole seated body in shot in both panels, the car seat small
within it.

[GROUND] A dark teal field, stepping once in value at the divider: the right
half one clear step lighter.

[BODY] Exactly one seated figure per panel, same scale and same side view in
both: the pelvis, sacrum and lumbar spine in warm ivory inside a translucent
seated outline. Not a full skeleton, no skull.

[PANELS]
LEFT, wrong: the figure sitting in an ordinary car driver's seat, drawn
realistically and unbranded, with an open gap where its seat base meets its
backrest. The sacrum has slid back into that gap and the pelvis has rolled
backward, the lumbar curve collapsed into a backward bow.
RIGHT, correct: the same figure at the same interface, sitting on the
reference cushion in the same car seat, the cushion drawn at a size and angle
where its L shape is obvious, its seat section under the hips and its lumbar
section filling the gap against the sacrum, the pelvis upright.
The spine appears in both panels. The seat and the cushion each touch the
pelvis where they act, and neither covers it.

[MARKS] Three marks, no others.
measure: two dashed straight lines, one per panel, identical in thickness and
dash pattern, each running from the front face of the backrest to the back of
the sacrum and stopping at both. Red left, blue right. Only the distance
spanned differs.
aura: one soft blue glow following the lumbar curve, right panel only.
verdict: one badge in the top corner of each panel, a filled solid disc with
the glyph cut out of it, same diameter in both: red with an X on the left,
green with a check on the right.

Red is wrong, blue is correct, green is the badge, warm ivory is structure;
nothing else carries colour.
```

---

### `story.3.image` — mechanism

*beside story block 3, 'An Integrated, One-Piece Solution' (600x450)* · asset `05-story3-ghostbody.jpg`

**Recommended: option A.** C1, and nothing else separates them. The section's claim is 'keeping the hips and lumbar spine aligned as a single unit', which is a sagittal claim — A shows exactly that plane. B answers a tailbone-pressure claim the copy never makes, and C is A in a car seat, which duplicates whatever story.2 already chose. C3 is neutral: every mark in this type is unproven at zero render records, so fit has to decide and does.

**No GIF.** The slot exists to show an alignment that holds, not a sequence. Its argument is a shape existing for a reason, and animating a static geometry invents a change the product does not make.

#### Option A — 03-mechanism-ghostbody 2.2  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **4:3** · single-pass · 2085 characters
- why: The section explains WHY the shape works — 'keeping the hips and lumbar spine aligned as a single unit' — through a mechanism inside the body that cannot be filmed. body_contact is true, so ghostbody serves and xray does not.
- note: Every mark in this type is unproven — zero records in eval/render-tests.jsonl — so this render is founding evidence and should be logged as such. Marks are flat hard-edged overlays laid ON the render; support is a band beside the bone, never a fill, and no mark touches the cushion.

```prompt
TYPE: 03-mechanism-ghostbody v2.2
REGISTER: 3D technical render.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cushion.

[PANELS] Two equal panels side by side, each a full 3D technical render,
divided by a single thin vertical line. Left is the wrong state, right is the
correct state.

[GHOST] A featureless matte white mannequin — no face, no hair, no clothing,
no skin tone — seated on a plain matte white chair form in side view, hands
resting on the thighs. The same pose, the same angle and the same chair form
in both panels. Cross-sectioned along the vertical plane through the spine so
the interior shows.

[CUTAWAY] The lumbar spine, sacrum and pelvis, inside the body silhouette. In
the left panel the sacrum has slid back into the open space behind the seat
and the pelvis is rolled backward, the lumbar column bowed the wrong way. In
the right panel the pelvis stands upright and the lumbar column holds its
forward curve.

[PRODUCT] Right panel only: the reference cushion on the chair form, its seat
section under the pelvis and its lumbar section filling the space behind the
sacrum, in the same side view. Its contour visibly follows the lumbar column's
curve. It keeps its own reference colours and carries no signal colour at all.
No mark is placed on it.

[MARKS] Four marks and no others, every one a flat unshaded hard-edged overlay
laid on top of the render, obviously added.
structure: the lumbar vertebrae, sacrum and pelvis in warm off-white ivory, in
both panels.
stress: a flat red overlay on the two lowest lumbar vertebrae, left panel only.
support: a flat blue band beside the lumbar column, on the side away from the
cushion, running only the length the cushion's lumbar section reaches. Right
panel only, never a fill of the bone.
verdict: one badge in the top corner of each panel, a filled solid disc with
the glyph cut out of it: red with an X on the left, green with a check on the
right.

PALETTE LOCK: everything else in the frame is achromatic white and grey. The
cushion is the only object with a real material finish.
```

#### Option B — 03-mechanism-ghostbody 2.2

- varies on: execution: transverse cut at the sitting bones instead of the sagittal lumbar cut
- ratio parameter: **4:3** · single-pass · 1992 characters
- why: The same claim from underneath: the product's other named job is taking load off the tailbone. A different cut plane answers the buyer who sits, rather than the buyer who drives.
- note: Same palette lock and the same four marks; only the cut plane and the named structures change. Both options obey the harm-mark rule: stress lives in the left panel only.

```prompt
TYPE: 03-mechanism-ghostbody v2.2
REGISTER: 3D technical render.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cushion.

[PANELS] Two equal panels side by side, each a full 3D technical render,
divided by a single thin vertical line. Left is the wrong state, right is the
correct state.

[GHOST] A featureless matte white mannequin — no face, no hair, no clothing,
no skin tone — seated on a plain matte white chair form, seen from behind and
slightly above, arms hanging. The same pose, the same angle and the same chair
form in both panels. Cross-sectioned along the horizontal plane just above the
seat so the sitting bones and the tailbone show from below.

[CUTAWAY] The two sitting bones and the tailbone, inside the body silhouette.
In the left panel the tailbone has dropped lowest and carries the load. In the
right panel the two sitting bones sit level and lowest and the tailbone is
clear of the surface.

[PRODUCT] Right panel only: the reference cushion on the chair form, its seat
section under the sitting bones, in the same view. Its contoured relief
visibly aligns with the tailbone's position. It keeps its own reference
colours and carries no signal colour at all. No mark is placed on it.

[MARKS] Four marks and no others, every one a flat unshaded hard-edged overlay
laid on top of the render, obviously added.
structure: the sitting bones and the tailbone in warm off-white ivory, in both
panels.
stress: a flat red overlay on the tailbone, left panel only.
support: a flat blue band beside each sitting bone, on the side away from the
cushion, running only the length the cushion's seat section reaches. Right
panel only, never a fill of the bone.
verdict: one badge in the top corner of each panel, a filled solid disc with
the glyph cut out of it: red with an X on the left, green with a check on the
right.

PALETTE LOCK: everything else in the frame is achromatic white and grey. The
cushion is the only object with a real material finish.
```

#### Option C — 03-mechanism-ghostbody 2.2

- varies on: execution: a car-seat form and a driving pose instead of a chair form
- ratio parameter: **4:3** · single-pass · 2096 characters
- why: Same sagittal argument in the driving posture, where the copy also places the pain. Hands at a wheel give the ghost a reason for its pose, which the chair version has to assert.
- note: Do not run this with story.2 option C — a car seat in both would make the cause and the mechanism read as one image split in two.

```prompt
TYPE: 03-mechanism-ghostbody v2.2
REGISTER: 3D technical render.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cushion.

[PANELS] Two equal panels side by side, each a full 3D technical render,
divided by a single thin vertical line. Left is the wrong state, right is the
correct state.

[GHOST] A featureless matte white mannequin — no face, no hair, no clothing,
no skin tone — seated on a plain matte white car-seat form in side view, hands
at a matte white steering wheel. The same pose, the same angle
and the same seat form in both panels. Cross-sectioned along the vertical
plane through the spine so the interior shows.

[CUTAWAY] The lumbar spine, sacrum and pelvis, inside the body silhouette. In
the left panel the sacrum has slid back into the open space behind the seat
and the pelvis is rolled backward, the lumbar column bowed the wrong way. In
the right panel the pelvis stands upright and the lumbar column holds its
forward curve.

[PRODUCT] Right panel only: the reference cushion on the seat form, its seat
section under the pelvis and its lumbar section filling the space behind the
sacrum, in the same side view. Its contour visibly follows the lumbar column's
curve. It keeps its own reference colours and carries no signal colour at all.
No mark is placed on it.

[MARKS] Four marks and no others, every one a flat unshaded hard-edged overlay
laid on top of the render, obviously added.
structure: the lumbar vertebrae, sacrum and pelvis in warm off-white ivory, in
both panels.
stress: a flat red overlay on the two lowest lumbar vertebrae, left panel only.
support: a flat blue band beside the lumbar column, on the side away from the
cushion, running only the length the cushion's lumbar section reaches. Right
panel only, never a fill of the bone.
verdict: one badge in the top corner of each panel, a filled solid disc with
the glyph cut out of it: red with an X on the left, green with a check on the
right.

PALETTE LOCK: everything else in the frame is achromatic white and grey. The
cushion is the only object with a real material finish.
```

---

### `story.4.image` — outcome

*beside story block 4, 'Sitting Pain, Gone In Days' (600x450)* · asset `06-story4-relief-scene.jpg`

**Recommended: option A.** C1 and C2. The copy closes on a state of living — 'I finally joined Sarah for our evening walks' — which is this type's use_when word for word, and the reflection is the only mechanism that proves a change without a product in frame. C2 kills B outright: it is 06-relief-hero, which hero option A already uses, and one type appears once per page. C is A in a car park and works, but a shopping parade reads as the walk the copy actually names.

**GIF · 3s · seamless · form `whole-frame`** — The slot's reason to exist is a stride that no longer stalls — walking is a sequence, so it is temporal, and the reflection moves with him. The type forbids overlays, so there is no layer to animate instead.

```
SHOT     Locked frame, medium wide, no camera move
ACTION   He walks through, pauses, glances at the glass
RESULT   An even stride, nothing guarded
MATCH    Muted blue-grey grade of the paired pain still
```

Loop prompt — run it on the still option A produces. Delivery: mp4/webm, under 2 MB.

```prompt
MOTION FROM THE STILL — animate the generated image, do not
regenerate it. Locked camera, no zoom, no pan.
He walks through the frame at an even unhurried stride, slows, glances at his
own reflection in the glass, and carries on. His back stays straight and both
shoulders stay level throughout. The reflection tracks him correctly and stays
geometrically consistent. Two or three passersby drift behind him.
Hold the grade: muted blue-grey, light film grain, shallow depth of field.
No overlays, no badges, no text, no product.
```

#### Option A — 06-relief-scene 1.0  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **4:3** · single-pass · 1644 characters
- why: The copy closes on a state of living, not a feature — 'I finally joined Sarah for our evening walks'. That is this type's use_when, and its requires_pair is satisfied by the pain scene at story.0.
- note: REQUIRES_PAIR: only legal because 01-pain-scene is on the page at story.0 — same man, same muted blue-grey palette, same lens character. The reflection IS the evidence mechanism; without the glass this is a stock photo of a man on a street. No product in frame, by the type's own law.

```prompt
TYPE: 06-relief-scene v1.0
REGISTER: candid documentary photograph. Single frame. NO graphic overlays.

[SUBJECT]
The same man in his late forties as the paired pain image, in an open-collar
shirt and a jacket of the same muted palette, walking past a parade of shops
in the early evening, pausing a moment mid-stride.
Gaze on his own reflection in the shop window beside him.
Expression: a small closed-mouth smile, private and understated.
Not performing, not aware of a camera.

[EVIDENCE OF CHANGE]
His back is straight and his hips are square under him: the trunk stacked over
the pelvis, both shoulders level and dropped, the trailing leg swinging
through into a full even stride, neither hand anywhere near his lower back.
This must be readable in the direct view and in the reflection alike.

[REFLECTION]
The shop window fills about a third of the frame and shows him from a
different angle, sharp enough to read the line of his back. The reflection is
geometrically consistent with where he is standing.

[ENVIRONMENT]
An ordinary suburban shopping parade he would pass on an evening walk. Two or
three blurred passersby, a bus shelter, a wheelie bin, damp pavement. Ordinary
weather, nothing aspirational, no styling.

[LIGHT]
Even natural early-evening daylight, bright, soft shadows. Slightly kinder
than the paired pain image but the same time-of-day character. No golden hour,
no rim light.

[GRADE]
Muted blue-grey matching the paired pain image, light film grain, shallow
depth of field. Desaturated, never warm-boosted.

STYLE: candid lifestyle photography, natural, unposed, sharp.
NO text, no logo, no watermark, no product.
```

#### Option B — 06-relief-hero 1.12 `--ugc, inset --none`

- varies on: type: 06-relief-hero
- ratio parameter: **4:3** · single-pass · 1452 characters
- why: Closes the section with the product in frame instead of a productless scene. Choose it if the page needs the cushion visible at the moment relief is claimed.
- note: COLLIDES WITH hero.image OPTION A: both are 06-relief-hero, and one type appears at most once per page outside a repeating section. Pick this only alongside hero option B.

```prompt
TYPE: 06-relief-hero v1.12 --ugc, inset --none
REGISTER: shot on a phone by an ordinary person. Slightly off exposure, mild
overexposure on skin and windows, no rim light, framing casual and a little
too close. The room is left exactly as it is.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly.

[SUBJECT]
Man in his late forties in an open-collar work shirt, seated at his own desk
late in the working day, leaned back with his weight through his hips, one arm
hooked over the chair back, talking to somebody out of frame. Relaxed, gaze
away from the cushion.

[PRODUCT]
The cushion in place on the chair beneath and behind him, seen from a rear
three-quarter angle so the seat section under his hips and the lumbar section
against his lower back are both visible, the contact line continuous and
unobstructed.

[SETTING]
His own office corner, filled to the edges with what lives there: a keyboard
pushed back, a mug, a coat on a hook, a stack of trays, a cable run along the
skirting, a window with a blind half down. None of them carries printed words.
Background soft but never blank.

[LIGHT]
Flat late-afternoon daylight from the window plus the overhead strip light. No
studio light, no rim light.

[LAYOUT]
He sits to the left of the frame; the room's own depth fills the right side.
No panel, no inset, no second image anywhere in the frame.
```

#### Option C — 06-relief-scene 1.0

- varies on: execution: a car park and car glass instead of a shopping parade and a shop window
- ratio parameter: **4:3** · single-pass · 1703 characters
- why: The same proof against a reflective surface the driver half of the audience meets every day. A car park is also a more forgiving reflection than a shop window, which has a lit interior competing behind the glass.
- note: The bag in one hand is deliberate: it gives the level shoulders something to be level despite. Same pair requirement as A.

```prompt
TYPE: 06-relief-scene v1.0
REGISTER: candid documentary photograph. Single frame. NO graphic overlays.

[SUBJECT]
The same man in his late forties as the paired pain image, in an open-collar
shirt and a jacket of the same muted palette, crossing a supermarket car park
in the early evening with a bag in one hand, pausing a moment mid-stride.
Gaze on his own reflection in the side glass of a parked car.
Expression: a small closed-mouth smile, private and understated.
Not performing, not aware of a camera.

[EVIDENCE OF CHANGE]
His back is straight and his hips are square under him: the trunk stacked over
the pelvis, both shoulders level and dropped despite the bag, the trailing leg
swinging through into a full even stride, neither hand anywhere near his lower
back. This must be readable in the direct view and in the reflection alike.

[REFLECTION]
The car's side glass and door fill about a third of the frame and show him
from a different angle, sharp enough to read the line of his back. The
reflection is geometrically consistent with where he is standing.

[ENVIRONMENT]
An ordinary suburban car park he would cross on the way home. Two or three
blurred people with trolleys, a trolley bay, painted bay lines, wet tarmac.
Ordinary weather, nothing aspirational, no styling.

[LIGHT]
Even natural early-evening daylight, bright, soft shadows. Slightly kinder
than the paired pain image but the same time-of-day character. No golden hour,
no rim light.

[GRADE]
Muted blue-grey matching the paired pain image, light film grain, shallow
depth of field. Desaturated, never warm-boosted.

STYLE: candid lifestyle photography, natural, unposed, sharp.
NO text, no logo, no watermark, no product.
```

---

### `story.5.image` — cta

*beside story block 5, 'A Fractional Cost For Freedom' (600x450)* · asset `(supplied)`

**Out of library scope.** A cta cell: the section's whole argument is price against premium chairs and recurring physiotherapy, closing on the guarantee. That is a standard product shot, which is out of library scope (mapping/slot-rules.md, cta row).

---

### `reviews.gallery.0.image` — social-proof

*review grid cell 1 (160x160)* · asset `07-review-grid-kitchen-chair.jpg`

**Recommended: option A.** C1 and the SET. A is the cheapest thing a sceptic checks — the thing is real and already in the room — and it is the only at-rest morning-daylight cell in the six. B puts a limb in a cell that does not need one, and C moves the scene to a room class the grid already covers.

**No GIF.** The cell exists to prove the thing exists in a normal room — a place, not a change. The type is one frame with no layers, so there is nothing to animate as an inset either, and motion in a 160px thumbnail breaks the register it depends on: real people's photos do not move.

#### Option A — 05-social-snapshot 1.0  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **1:1** · single-pass · 1187 characters
- why: Newly unpacked and already in the room where it lives — the cheapest thing to prove and the first thing a sceptic checks.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion simply sitting where it now lives, on a wooden dining
chair pushed under a kitchen table, still holding the shallow creases of the
compression bag it came out of.

[SCENE] An ordinary kitchen photographed as found: crumbs on the table, a cereal bowl
not cleared, a chair pulled out at an angle. One coiled phone charger lies on
the table beside it. Nothing tidied, nothing added.

[LIGHT] Morning window daylight only, cool and a bit flat.

[CAMERA TRUTH] Framing slightly off-centre and taken from standing height looking down; focus
adequate but casual; exposure honest to the room. No negative space, no rule of
thirds, no depth-of-field styling.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option B — 05-social-snapshot 1.0

- varies on: axis: content mode=in-use
- ratio parameter: **1:1** · single-pass · 1067 characters
- why: Shows the thing being fitted rather than found, which answers whether it actually stays put on a hard chair.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] in-use: two fingers pressing the cushion's seat section down onto a wooden
dining chair to seat it properly. No face, no other part of the person.

[SCENE] An ordinary kitchen photographed as found: crumbs on the table, a cereal bowl
not cleared, a chair pulled out at an angle. One coiled phone charger lies on
the table beside it. Nothing tidied, nothing added.

[LIGHT] Morning window daylight only, cool and a bit flat.

[CAMERA TRUTH] Framing too close and tilted, taken leaning over the chair; mild motion
softness; exposure honest to the room.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option C — 05-social-snapshot 1.0

- varies on: execution: a home-office folding chair instead of a kitchen dining chair
- ratio parameter: **1:1** · single-pass · 1058 characters
- why: The universal-fit claim tested on the worst chair in the house — a folding one with no contour at all.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion sitting on a folding chair in the corner of a spare room
used as an office, the chair turned half away from a small desk.

[SCENE] A spare-room office photographed as found: a printer on the floor, a laundry
airer folded against the wall, a box not yet unpacked. One roll of parcel tape
sits on the desk. Nothing tidied.

[LIGHT] Late-morning daylight through a net curtain, soft and slightly grey.

[CAMERA TRUTH] A medium frame from the doorway, slightly tilted; focus adequate but casual;
exposure honest to the room.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

---

### `reviews.gallery.1.image` — social-proof

*review grid cell 2 (160x160)* · asset `08-review-grid-car-seat.jpg`

**Recommended: option A.** C1. The driver is the loudest voice in this page's review copy, and A is the gesture that voice describes — pressing it into the seat corner. B empties the frame of any human trace, which four other cells already do; C moves to the back seat, where nobody in the reviews sits.

**No GIF.** The cell exists to prove the thing exists in a normal room — a place, not a change. The type is one frame with no layers, so there is nothing to animate as an inset either, and motion in a 160px thumbnail breaks the register it depends on: real people's photos do not move.

#### Option A — 05-social-snapshot 1.0  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **1:1** · single-pass · 1177 characters
- why: The driver in the reviews is the loudest voice in this page's copy; a forearm pressing it into the seat corner is the gesture that voice describes.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] in-use: the cushion fitted into a car's driver seat, one forearm reaching in
through the open door to press its lumbar section back into the seat corner.
No face, no other part of the person.

[SCENE] The inside of an ordinary used car photographed as found: a crumpled receipt
in the door pocket, floor mats gritty, a child's toy in the footwell behind.
One key fob dangles from the ignition. Nothing tidied.

[LIGHT] Late evening, the car's dome light plus orange street light through the
windscreen. Warm and uneven.

[CAMERA TRUTH] Framing too close and tilted, taken leaning in through the door; mild motion
softness; exposure honest to the dark interior.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option B — 05-social-snapshot 1.0

- varies on: axis: content mode=at-rest
- ratio parameter: **1:1** · single-pass · 1084 characters
- why: Reads the cushion more clearly at thumbnail size, because no limb crosses it.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion alone on the driver's seat, the door open and nobody in
the car yet.

[SCENE] The inside of an ordinary used car photographed as found: a crumpled receipt
in the door pocket, floor mats gritty, a child's toy in the footwell behind.
One key fob dangles from the ignition. Nothing tidied.

[LIGHT] Late evening, the car's dome light plus orange street light through the
windscreen. Warm and uneven.

[CAMERA TRUTH] A medium frame from just outside the open door, slightly off-centre; focus
adequate but casual; exposure honest to the dark interior.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option C — 05-social-snapshot 1.0

- varies on: execution: the rear passenger seat in daylight instead of the driver's seat at night
- ratio parameter: **1:1** · single-pass · 1042 characters
- why: Covers the passenger rather than the driver, which no other cell in the set does.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] in-use: the cushion fitted into a rear passenger seat, one hand reaching in to
straighten it. No face, no other part of the person.

[SCENE] The back of an ordinary family car photographed as found: a child's seat
beside it, crumbs in the seat crease, a scuffed door card. One folded pushchair
rain cover lies on the floor. Nothing tidied.

[LIGHT] Flat midday daylight through the open door and the rear window.

[CAMERA TRUTH] Framing too close and tilted, taken leaning in through the rear door; focus
adequate but casual.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

---

### `reviews.gallery.2.image` — social-proof

*review grid cell 3 (160x160)* · asset `09-review-grid-gaming-chair.jpg`

**Recommended: option A.** C1 and the SET. One of the five named reviewers is a gamer, and A is the only cell in the six shot wide, at night, with two clashing light temperatures — dropping it costs the grid its widest and darkest frame. B and C both narrow that.

**No GIF.** The cell exists to prove the thing exists in a normal room — a place, not a change. The type is one frame with no layers, so there is nothing to animate as an inset either, and motion in a 160px thumbnail breaks the register it depends on: real people's photos do not move.

#### Option A — 05-social-snapshot 1.0  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **1:1** · single-pass · 1119 characters
- why: One of the five named reviewers is a gamer. A wide dim room is the furthest this set gets from the others in light and distance.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion sitting in a gaming chair in a bedroom, seen from across
the room with the chair turned half away from the desk.

[SCENE] A young adult's bedroom photographed as found: an unmade bed edge in the
foreground, a hoodie over the chair arm, cables trailing down the desk leg. One
empty energy-drink can stands on the desk. Nothing tidied.

[LIGHT] Night. A warm bedside lamp on one side and the cold blue glow of two monitors
on the other, mixing badly.

[CAMERA TRUTH] A wide frame taken from the doorway, slightly tilted; visible noise in the
shadows; exposure honest to the dim room.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option B — 05-social-snapshot 1.0

- varies on: axis: content mode=in-use
- ratio parameter: **1:1** · single-pass · 1120 characters
- why: Proves the cushion stays put when the chair is moved, which the copy's does-not-slide claim invites.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] in-use: a forearm dragging the gaming chair round by its backrest, the cushion
still seated in it. No face, no other part of the person.

[SCENE] A young adult's bedroom photographed as found: an unmade bed edge in the
foreground, a hoodie over the chair arm, cables trailing down the desk leg. One
empty energy-drink can stands on the desk. Nothing tidied.

[LIGHT] Night. A warm bedside lamp on one side and the cold blue glow of two monitors
on the other, mixing badly.

[CAMERA TRUTH] A medium frame taken standing beside the chair, off-centre; mild motion
softness; exposure honest to the dim room.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option C — 05-social-snapshot 1.0

- varies on: execution: a shared student kitchen-diner under strip light instead of a bedroom at night
- ratio parameter: **1:1** · single-pass · 1050 characters
- why: A green-cast fluorescent room is a light temperature nothing else in the set carries.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion on a hard-backed chair at a shared kitchen table, pushed
in, a laptop closed in front of it.

[SCENE] A shared student kitchen-diner photographed as found: someone else's washing
up stacked by the sink, a wall calendar curling, four mismatched chairs. One
phone cable is plugged into the wall socket. Nothing tidied.

[LIGHT] Overhead fluorescent strip light, flat and slightly green, no daylight.

[CAMERA TRUTH] A medium frame from standing height looking down the table, off-centre; focus
adequate but casual.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

---

### `reviews.gallery.3.image` — social-proof

*review grid cell 4 (160x160)* · asset `10-review-grid-hallway-unbox.jpg`

**Recommended: option A.** C1 and the SET. A is the only kit-flatlay in the six and it answers a different scepticism from the rest — what actually arrives in the box. B gives that up and becomes a fifth at-rest cell; C keeps the flatlay but on a bed, which reads as styled rather than dropped.

**No GIF.** The cell exists to prove the thing exists in a normal room — a place, not a change. The type is one frame with no layers, so there is nothing to animate as an inset either, and motion in a 160px thumbnail breaks the register it depends on: real people's photos do not move.

#### Option A — 05-social-snapshot 1.0  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **1:1** · single-pass · 1188 characters
- why: The only flatlay in the set: it answers what actually arrives in the box, which is a different scepticism from does-it-work.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] kit-flatlay: the cushion just unpacked on a hallway floor, laid out the way the
owner dropped it — the cushion itself, its zip-off cover half peeled back, and
the flattened compression bag it shipped in, slightly disordered. Real contents
only, nothing added.

[SCENE] A narrow hallway photographed as found: worn laminate, a doormat with grit on
it, one shoe on its side at the frame edge. One pair of scissors lies where it
was put down. Nothing tidied.

[LIGHT] A single overhead hall bulb, warm and dim, throwing one hard shadow.

[CAMERA TRUTH] Shot from standing height straight down, too close, the frame cutting the bag
off at one edge; focus adequate but casual.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option B — 05-social-snapshot 1.0

- varies on: axis: content mode=at-rest
- ratio parameter: **1:1** · single-pass · 1060 characters
- why: The delivery-just-landed moment, which is the most common real customer photo of all.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion propped against the hallway wall beside the front door,
still half inside its compression bag, waiting to be carried through.

[SCENE] A narrow hallway photographed as found: worn laminate, a doormat with grit on
it, one shoe on its side at the frame edge. One pair of scissors lies where it
was put down. Nothing tidied.

[LIGHT] A single overhead hall bulb, warm and dim, throwing one hard shadow.

[CAMERA TRUTH] A close frame from standing height, tilted; focus adequate but casual;
exposure honest to the dim hallway.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option C — 05-social-snapshot 1.0

- varies on: execution: a bed instead of a hallway floor
- ratio parameter: **1:1** · single-pass · 1182 characters
- why: Daylight rather than a bulb, if the hall version comes back too orange to read the product.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] kit-flatlay: the cushion just unpacked on a made bed, the cushion itself, its
zip-off cover half peeled back and the flattened compression bag beside it,
slightly disordered. Real contents only, nothing added.

[SCENE] An ordinary bedroom photographed as found: a duvet not straightened, a paper
bag from the delivery on the floor, a bedside table with a glass on it. One
kitchen knife used to open the parcel lies on the duvet. Nothing tidied.

[LIGHT] Grey daylight through a half-drawn curtain, soft and directionless.

[CAMERA TRUTH] Shot from standing height straight down, slightly tilted, the frame cutting the
bag off at one edge; focus adequate but casual.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

---

### `reviews.gallery.4.image` — social-proof

*review grid cell 5 (160x160)* · asset `11-review-grid-wheelchair.jpg`

**Recommended: option A.** C1. Wheelchair users are named in the product's own fit list and appear nowhere in the page's copy, so this is the only place the page can show them — and A shows the cushion being used, not just present. B empties it of the person entirely, and C moves outdoors, where the flat indoor overcast light the set needs is lost.

**No GIF.** The cell exists to prove the thing exists in a normal room — a place, not a change. The type is one frame with no layers, so there is nothing to animate as an inset either, and motion in a 160px thumbnail breaks the register it depends on: real people's photos do not move.

#### Option A — 05-social-snapshot 1.0  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **1:1** · single-pass · 1112 characters
- why: Wheelchair users are named in the product's own fit list and nowhere in the page's copy; this is the only place the page can show it.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] in-use: the cushion fitted into a wheelchair seat, two fingers entering the
frame to tuck its lumbar section down against the backrest. No face, no other
part of the person.

[SCENE] A living room by a window, photographed as found: a side table with a week's
post on it, a folded blanket over the sofa arm, a rug rucked at one corner. One
walking stick leans against the wall. Nothing tidied.

[LIGHT] Flat grey overcast daylight through the window, no lamps on.

[CAMERA TRUTH] A medium frame taken from a seated position looking across; slightly
off-centre; exposure honest and a little dull.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option B — 05-social-snapshot 1.0

- varies on: axis: content mode=at-rest
- ratio parameter: **1:1** · single-pass · 1036 characters
- why: Reads the L shape against the wheelchair seat more clearly, with no hand crossing it.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion sitting in an empty wheelchair parked by the living-room
door, nobody in the room.

[SCENE] A living room by a window, photographed as found: a side table with a week's
post on it, a folded blanket over the sofa arm, a rug rucked at one corner. One
walking stick leans against the wall. Nothing tidied.

[LIGHT] Flat grey overcast daylight through the window, no lamps on.

[CAMERA TRUTH] A medium frame from standing height looking down at the chair; off-centre;
exposure honest and a little dull.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option C — 05-social-snapshot 1.0

- varies on: execution: a patio outdoors instead of a living room
- ratio parameter: **1:1** · single-pass · 1047 characters
- why: The only outdoor cell available to the set, if the grid needs one.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] in-use: the cushion fitted into a wheelchair on a back patio, one hand on the
push rim. No face, no other part of the person.

[SCENE] A small suburban back patio photographed as found: a plastic garden chair with
rainwater in the seat, a coiled hose, weeds in the paving joints. One pair of
garden gloves lies on the step. Nothing tidied.

[LIGHT] Bright overcast daylight outdoors, flat and slightly cold.

[CAMERA TRUTH] A medium frame taken from standing height slightly behind; tilted; exposure
honest to the bright grey sky.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

---

### `reviews.gallery.5.image` — social-proof

*review grid cell 6 (160x160)* · asset `12-review-grid-lorry-cab.jpg`

**Recommended: option A.** C1 and the SET. The truck driver's review is the most specific one on the page, and dawn in a cab is a light temperature nothing else in the six has. B adds a glove but loses the empty-cab stillness that makes the hour read; C swaps the cab for a van and the dawn for midday, which duplicates cell 2's daylight.

**No GIF.** The cell exists to prove the thing exists in a normal room — a place, not a change. The type is one frame with no layers, so there is nothing to animate as an inset either, and motion in a 160px thumbnail breaks the register it depends on: real people's photos do not move.

#### Option A — 05-social-snapshot 1.0  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **1:1** · single-pass · 1061 characters
- why: The truck driver's review is the most specific one on the page. Dawn in a cab is a light temperature nothing else in the set has.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion on the driver's seat of a lorry cab, the door open and
nobody in it yet.

[SCENE] A working lorry cab photographed as found: a bunk curtain half drawn behind
the seat, a grubby dashboard, a hi-vis jacket bundled on the passenger seat.
One vacuum flask stands in the door pocket. Nothing tidied.

[LIGHT] Dawn. Cold blue light through the windscreen, the cab interior still dark.

[CAMERA TRUTH] Too close, shot from below at the open door looking up into the cab, tilted;
noticeable noise; exposure honest to the low light.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option B — 05-social-snapshot 1.0

- varies on: axis: content mode=in-use
- ratio parameter: **1:1** · single-pass · 1079 characters
- why: A work glove dates the shot to the start of a shift, which the copy's road-vibration claim leans on.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] in-use: a gloved hand pressing the cushion back into the corner of a lorry
cab's driver seat. No face, no other part of the person.

[SCENE] A working lorry cab photographed as found: a bunk curtain half drawn behind
the seat, a grubby dashboard, a hi-vis jacket bundled on the passenger seat.
One vacuum flask stands in the door pocket. Nothing tidied.

[LIGHT] Dawn. Cold blue light through the windscreen, the cab interior still dark.

[CAMERA TRUTH] Too close, shot from below at the open door, tilted; mild motion softness;
exposure honest to the low light.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

#### Option C — 05-social-snapshot 1.0

- varies on: execution: a delivery van cab at midday instead of a lorry cab at dawn
- ratio parameter: **1:1** · single-pass · 1036 characters
- why: Broadens the driver persona from long-haul to local delivery, which the brief names as well.
- note: One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode must all differ from every other cell that ships — so swapping this cell's option means re-checking the other five. Generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.

```prompt
TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion on the driver's seat of a delivery van, the side door
rolled back and parcels stacked behind.

[SCENE] A working van cab photographed as found: a clipboard wedged by the gear stick,
a sandwich wrapper in the door pocket, parcels strapped behind the seat. One
handheld scanner sits on the passenger seat. Nothing tidied.

[LIGHT] Flat midday daylight through the open door, bright and unmodelled.

[CAMERA TRUTH] A medium frame from just outside the open door, off-centre; focus adequate but
casual.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders.
```

---

### `offer.image` — cta

*offer card product image (360x360)* · asset `(supplied)`

**Out of library scope.** The cta cell's standard product shot — out of library scope (mapping/slot-rules.md, cta row).

---

### `hero.sidebar.image` — cta

*Editor's Pick sidebar product image, top of page (300x300)* · asset `(supplied)`

**Out of library scope.** A standard product shot inside a rating sidebar — out of library scope, and the same shot as offer.image.

---

