# Image prompts — page 58, 7-in-1 external DVD / Blu-ray drive

GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit the script and re-run.

- page_id `58` · channel `advertorial` · awareness `problem-aware` · registry `2.0.0`
- 22 image slots: 12 routed, 10 out of library scope
- 36 prompts, three per routed slot, one recommended each
- 2 slots earn motion, each carrying a G12 brief plate as a fourth option below C — a work order the editor renders alongside the still, never a prompt that animates one (ADR-020)

Ratio goes in the generation tool's own aspect-ratio parameter, never in the prompt text (adapters/nano-banana.md Rule 4). The `Strictly avoid:` line is not rendered into any prompt (ADR-014); the exclusion list is kept in the JSON's `avoid` field for a model with a real negative channel.

## Read this first

- **GAP, and it blocks 10 of the 12 routed slots.** The export carries imageBriefs: null and sourceRefs.shopifyProductGid: null, so there is no product photograph anywhere in it and nothing to hash. Every type on this page except 01-pain-scene and 02-cause-anatomy --diagnostic declares requires_product_photo: true, and each of those prompts says 'the attached photo'. Nothing was fabricated: attachments is omitted from every option rather than filled with an invented sha256 (SPEC 6.4). Supply the drive's reference photograph, hash it, and these prompts are runnable as written.
- **Awareness read as problem-aware, and the basis is the copy rather than the brief's own field.** The hero spends its whole opening re-establishing that a new laptop has no disc drive, two full sections run before any solution is named, and the framework is PAS. A problem-aware reader is moved by the cause and the mechanism, which is why 02-cause-anatomy and 03-mechanism-xray carry the middle of this routing rather than more proof.
- **THE TEMPLATE'S PLACEHOLDER TEXT IS FROM A DIFFERENT PRODUCT.** Every placehold.co URL in htmlCompiled is labelled for a weighted blanket - 'Quilted pockets', 'Glass bead fill', 'Halden blanket', 'Folded on bed', 'Wash day', 'Six months on three beds'. TPL-ADV08 was reused without restamping them. Every brief below is derived from the content dict and the product brief, never from those labels; ignore them when placing assets.
- **BLOCKED AS THE PAGE IS BUILT.** 05-social-snapshot's authenticity fence is hard and non-negotiable: no reviewer name, avatar, star row or verified label anywhere near the image in the layout. reviews.shots.0-3 sit inside the same section element as reviews.quotes.0-2, which carry names (Martin K., Gillian R., Derek S.) and a 'Verified Purchase' label each. Rendering these four beside that copy presents generated pictures as customer uploads, which is a fabricated endorsement. Either move the shots out of the attributed block, or drop the names and verified labels from that block, or use real customer photographs - which always win over generated ones.
- **Six comment avatars, two author portraits and two product-card shots are reported out of library scope rather than forced into a type.** Ten of the twenty-two image fields in this export are therefore unrouted by design, which is the cta row of slot-rules being empty and the portrait question being a disclosure decision, not an imaging one.
- **One type appears once per page and two slots hit that wall.** 04-proof-lockedframe was wanted at both problems.items.0 and features.items.4 and went to the second, because its use_when requires a reader who already understands the mechanism. 06-relief-hero runs twice, at features.items.1 and features.items.2, under rung 4 of the widening ladder with inset_mode, subject, place and pose all named as the differing dimensions. A third relief-hero would be past what that rung permits, which is why option B at features.items.3 is flagged as forcing two other slots to change.
- **Page arc holds: every pain image sits above the first relief image.** The one pain cue below it is inside features.items.3 option B's recall inset, which the type permits because pain exists only inside the inset there.
- **02-cause-anatomy is being asked for its first NON-BIOLOGICAL body.** Every subject class it has rendered is anatomical. Its device is a 2D cross-section and its avoid_when asks only for internal structure to draw, which a disc, a track and a lens have - but this is untested and the first render of problems.items.1 is the test.
- **No pick prior was available.** feedback/picks.jsonl is empty, so the >=20-pick tie-breaker in SPEC 7.7 never fired and every recommendation here rests on fit, legality, render evidence, product presence and prompt risk alone. These recommendations make the page argument-complete; they are not conversion-optimised and nothing here is performance-backed.
- **Ratio is set in the generation tool's aspect-ratio parameter, never in the prompt text (adapters/nano-banana.md Rule 4).** The Strictly avoid line is not rendered into any prompt (ADR-014); the exclusion list is kept in each option's avoid field for a model with a real negative channel.

## Slot map

| slot | role | asset | recommended | ratio | gif |
|---|---|---|---|---|---|
| `hero.image` | hero | `58-01-hero-pain-scene.png` | **A** — 01-pain-scene 1.14 `candid` | 16:9 | — |
| `problems.items.0.image` | problem-agitation | `58-02-problems0-pain-scene-object.png` | **A** — 01-pain-scene 1.14 `candid` | 16:9 | — |
| `problems.items.1.image` | cause | `58-03-problems1-cause-anatomy.png` | **A** — 02-cause-anatomy 1.15 `diagnostic` | 16:9 | whole-frame · cause |
| `features.items.0.image` | mechanism | `58-04-features0-xray.png` | **A** — 03-mechanism-xray 1.3 | 16:9 | whole-frame · mechanism |
| `features.items.1.image` | spec | `58-05-features1-relief-hero-detail.png` | **A** — 06-relief-hero 1.15 | 16:9 | — |
| `features.items.2.image` | spec | `58-06-features2-relief-hero-context.png` | **A** — 06-relief-hero 1.15 | 16:9 | — |
| `features.items.3.image` | outcome | `58-07-features3-relief-scene.png` | **A** — 06-relief-scene 3.7 | 16:9 | — |
| `features.items.4.image` | comparison | `58-08-features4-lockedframe-verdict.png` | **A** — 04-proof-lockedframe 1.13 `verdict` | 16:9 | — |
| `reviews.shots.0.image` | social-proof | `58-09-reviews-shot-0.png` | **A** — 05-social-snapshot 1.2 | 1:1 | — |
| `reviews.shots.1.image` | social-proof | `58-10-reviews-shot-1.png` | **A** — 05-social-snapshot 1.2 | 1:1 | — |
| `reviews.shots.2.image` | social-proof | `58-11-reviews-shot-2.png` | **A** — 05-social-snapshot 1.2 | 1:1 | — |
| `reviews.shots.3.image` | social-proof | `58-12-reviews-shot-3.png` | **A** — 05-social-snapshot 1.2 | 1:1 | — |
| `product.image` | cta | `—` | — out of scope | — | — |
| `product_end.image` | cta | `—` | — out of scope | — | — |
| `hero.author_avatar` | author | `—` | — out of scope | — | — |
| `guide.avatar` | author | `—` | — out of scope | — | — |
| `comments.items.0.avatar` | social-proof | `—` | — out of scope | — | — |
| `comments.items.1.avatar` | social-proof | `—` | — out of scope | — | — |
| `comments.items.2.avatar` | social-proof | `—` | — out of scope | — | — |
| `comments.items.3.avatar` | social-proof | `—` | — out of scope | — | — |
| `comments.items.4.avatar` | social-proof | `—` | — out of scope | — | — |
| `comments.items.5.avatar` | social-proof | `—` | — out of scope | — | — |

## Coverage

**Covered**

- step 1 pain — 01-pain-scene twice, a person at the hero and the object-only dongle nest at problems.items.0
- step 2 cause — 02-cause-anatomy --diagnostic at problems.items.1
- step 3 mechanism — 03-mechanism-xray at features.items.0
- step 4 proof — 04-proof-lockedframe --verdict at features.items.4
- step 5 social — 05-social-snapshot across all four review tiles
- step 6 relief — 06-relief-hero twice in the features block and 06-relief-scene at the outcome beat

**Absent**

- step 2 symptom — 02-symptom-rail was trimmed off advertorial on 2026-08-11 and is not a candidate at any rung
- step 3 use — 03-use-sequence declares only 3:4 and 1:1, so it cannot serve any 16:9 slot on this page. The copy would have suited it.
- step 5 personas — 05-persona-grid is marketplace and landing-page only

**Absent on purpose**

- No symptom rung, and that is right for a problem-aware reader who already feels the problem: the copy spends its first two sections re-establishing it in prose and needs the cause and the mechanism next, which both run.
- No 03-mechanism-ghostbody, correctly — body_contact is false for an external drive and the slot-rules attribute gate drops it outright.

**Gaps**

- The page makes a NOISE claim in four separate places — rattled, whisper-quiet, no motor buzzing, silent — and no image on this page can carry it. Silence is not photographable and no library type argues it. It stays a copy claim, and the honest place to prove it is video.
- features.items.2's headline claim is thermal — a casing staying cool over a weekend — which is equally invisible. The recommended option argues the slim half of that section and leaves the thermal half to the copy; it is not proof and is not presented as any.

---

## Prompts

### `hero.image` — hero

*Advertorial header, directly under the headline and byline.* · asset `58-01-hero-pain-scene.png`

**Recommended: option A.** FIT decides it. 01-pain-scene's use_when names this beat in its own words - 'advertorial header image, cold traffic that does not know the product yet' - and --candid is the branch for 'physical limitation and moments nobody would choose to be seen in', which is a man checking a disc he cannot play. PAGE LEGALITY: the type is G1-exempt, so A is one of only two prompts on this page that runs without the missing product photo. EVIDENCE: --candid carries this type's owner-passed worked example and the type passed at 1.14. PRODUCT PRESENCE: none required and none allowed here. PROMPT RISK: 1,5k characters against a type whose measured history runs 1669-1880, and every clause in it is one the type's own PARTS require. B is legal and would win if the beat were self-image rather than physical limitation; C moves the same argument onto degradation, which the copy raises but does not lead on.

#### Option A — 01-pain-scene 1.14 `candid`  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **16:9** · single-pass · 1587 characters
- why: The disc-in-hands force is diagnostic: nobody turns a disc to the light unless they cannot play it. Evidence is rank 1 - the laptop's unbroken edge with no slot, and the box of cases - so the symptom is a physical fact rather than an expression.
- note: G1-exempt: runs today without the missing product photo.

```prompt
TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his forties, work shirt with the collar open, sitting forward on the edge
of a living-room sofa late in the evening, mid-way through turning a DVD disc
over in both hands to check its underside against the light. Under that force:
both elbows on his knees, shoulders rolled forward over the disc, the wrists
angling it back and forth.
Face: brow drawn in, jaw set, eyes down on the disc.

[EVIDENCE]
A slim closed laptop sits on the coffee table in front of him with an unbroken
edge and no slot anywhere along it, and a shoebox of loose DVD cases stands open
beside it with the discs half out of their sleeves, one case lying face down on
the carpet where it slid off the pile.

[ENVIRONMENT]
An ordinary front room, evening. Lived-in clutter belonging to that place: two
mugs on the coffee table, a folded throw pushed to one end of the sofa, a
child's cardigan over the arm, the curtains already drawn. Nothing arranged,
nothing removed to tidy the frame.

[GAZE] unaware of the camera, gaze down on the disc in his hands.

[LIGHT] low-key. Key: a single table lamp beside the sofa, warm and close. Fill:
cold spill from a hallway doorway behind him. Rim light along the shoulder and
the edge of the disc. Deep shadow across most of the frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
```

#### Option B — 01-pain-scene 1.14 `confront`

- varies on: axis: gaze candid -> confront
- ratio parameter: **16:9** · single-pass · 1443 characters
- why: The same beat played as daily frustration rather than physical limitation, with the disc stopped dead against a closed edge. --confront is legible at thumbnail size, which suits a header that may run as a paid-social crop.
- note: No second type survives the hero cell on advertorial, so B varies on the axis per runbook Step 4. Also G1-exempt.

```prompt
TYPE: 01-pain-scene v1.14 --confront
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his forties, work shirt with the collar open, sitting at a kitchen table
turned square to camera, mid-way through pushing a DVD disc into the closed side
edge of a slim laptop where a slot would be, the disc stopped flat against the
casing and his thumb still pressing it there. Under that force: the forearm
locked, the shoulder dropped behind the push, the other hand flat on the table
taking the laptop's weight.
Face: mouth pressed flat, brow drawn in, chin tucked.

[EVIDENCE]
The disc stands proud of the laptop's unbroken edge with nowhere to go, and a
stack of DVD cases sits at his elbow with the top one open and empty, its
inner sleeve still holding the leaflet.

[ENVIRONMENT]
An ordinary kitchen table, early evening. Lived-in clutter belonging to that
place: a cold mug, a school bag slumped against a chair leg, a fruit bowl, a
tea towel over the radiator. Nothing arranged, nothing removed to tidy the
frame.

[GAZE] looking directly into the lens, holding the viewer's eye.

[LIGHT] even ambient daylight from a window behind the camera, minimal shadow,
flat and unflattering.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated neutral, muted greys and greens, fine film grain, moderate
depth of field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
```

#### Option C — 01-pain-scene 1.14 `candid`

- varies on: execution: subject, place and evidence rank
- ratio parameter: **16:9** · single-pass · 1622 characters
- why: Same type and axes as A, different execution: an older subject, a storage room, and the evidence moved to the discs themselves degrading. It argues the clock the copy mentions - 'the discs are slowly degrading while nothing is done' - which A leaves untouched.
- note: G1-exempt. Pairs less tightly with the first-person male byline than A or B.

```prompt
TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Woman in her fifties in a cardigan, kneeling on the floor of a spare room beside
an open storage crate, mid-way through lifting a stack of unlabelled home-video
discs out of it with both hands, the stack sagging apart as it comes up. Under
that force: the back rounded over the crate, both elbows out, one knee taking
her weight on the bare boards.
Face: brow drawn in, lips parted, eyes down on the stack.

[EVIDENCE]
The disc on top of the stack has a dulled milky bloom across its playing side
and a fine scatter of surface scratches catching the light, and two more discs
have slipped from the stack and lie face down on the floorboards beside a crate
lid furred with dust.

[ENVIRONMENT]
An ordinary spare room used for storage, afternoon. Lived-in clutter belonging
to that place: a stripped single bed pushed against the wall, a clothes airer
folded behind the door, two more crates stacked unopened, a roll of wrapping
paper on its side. Nothing arranged, nothing removed to tidy the frame.

[GAZE] unaware of the camera, gaze down on the discs in her hands.

[LIGHT] low-key. Key: thin daylight from one small window high on the wall,
raking across the floor. Fill: none to speak of. Rim light along the forearm and
the edge of the top disc. Deep shadow across most of the frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
```

#### GIF — none

- why: The slot exists to make a cold reader recognise themselves in a held state. Nothing about it is temporal - no transition, no sequence, no output flowing - so it does not earn motion.

### `problems.items.0.image` — problem-agitation

*Beside 'The painful loop of cheap drives and missing ports'.* · asset `58-02-problems0-pain-scene-object.png`

**Recommended: option A.** PAGE LEGALITY decides it over FIT. B is the better literal fit - 04-proof-lockedframe's use_when names 'the I tried three things beat' outright, and the copy's own note label is 'What I tried first'. But that type appears once per page and features.items.4 needs it more: its use_when also requires a buyer who 'already understands the problem and mechanism', which is false this early and true by the time the cost comparison runs. So A takes rung 4 of the runbook's ladder - another execution of a type already on the page, differing on a named dimension, here subject class - which is the precedent the runbook records for object-only pain scenes. EVIDENCE: object-only execution is recorded twice in the ledger. PRODUCT PRESENCE: none, correctly - the product has not been revealed yet. PROMPT RISK: A is G1-exempt and runnable today; B is too, but costs the page its proof image.

#### Option A — 01-pain-scene 1.14 `candid`  ← RECOMMENDED

- varies on: execution: subject class person -> object-only
- ratio parameter: **16:9** · single-pass · 1581 characters
- why: The dongle nest IS the symptom the copy describes, and it is an object fault, so the frame drops the person entirely. Evidence is rank 3, the failed tool in the state that shows it failed: a tray jammed half open with the disc still in it.
- note: Rung 4 of the runbook ladder. Named dimension vs hero.image: subject class. G1-exempt.

```prompt
TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
No person. The subject is a home desk in the state its owner left it, shot low
and close across the desktop so the tangle fills the frame.

[EVIDENCE]
A cheap grey plastic external drive sits skewed on the desk with its tray jammed
half open and a disc still resting in it, its single cable stretched taut across
the desktop to the one free port on a closed slim laptop. Three separate adapter
dongles hang off that same side in a knot, their cables crossing and looping back
on themselves, one of them unplugged entirely and lying on the desk with its
connector face up. A wireless mouse sits at the edge of the desk with its own
receiver stub loose beside it, plugged into nothing.

[ENVIRONMENT]
An ordinary home desk in a corner of a room, evening. Lived-in clutter belonging
to that place: a cold mug ringing the wood, a phone face down, a pair of glasses
folded on a notebook, a charger brick that has nowhere to go. Nothing arranged,
nothing removed to tidy the frame.

[GAZE] no person in the frame.

[LIGHT] low-key. Key: a desk lamp low and to one side, hard and close across the
cables. Fill: cold spill from a screen out of frame. Rim light along the drive's
top edge and the taut cable. Deep shadow across most of the frame.

[FORBIDDEN] No reference product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
```

#### Option B — 04-proof-lockedframe 1.13 `rivals`

- varies on: type: 01-pain-scene -> 04-proof-lockedframe
- ratio parameter: **16:9** · single-pass · 1767 characters
- why: Three panels, three things the reader has already tried, none of them winning - which is exactly the copy's three notes. --rivals carries no product, so it needs no reference photo either.
- note: PICKING B FORCES features.items.4 TO CHANGE - one type once per page, and variants do not lift it. features.4 would fall to a second 06-relief-hero execution. Type note at 1.13: --rivals is never sent for the library's own render tests because there is no product to judge; that is a testing rule, not a page rule.

```prompt
TYPE: 04-proof-lockedframe v1.13 --rivals, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
Not applicable. No product appears in this image.

[SCENE — the same in all three]
The same corner of a home desk, the same dark wood desktop, a closed slim laptop
pushed to the back and a cold mug beside it. Flat overcast light from a window off to the left, no strong
shadows, no styling.

[FRAMING]
One person photographed this three times across a fortnight from where they
always sit, phone level with the desktop, the bare wood filling the middle
third and the laptop across the upper third. It reads as one shot taken three
times, never as three different shots. Light differs only in exposure, never warmth.

[THE VARIABLE]
Three ways people already try to read a disc on a laptop with no drive, each
photographed mid-attempt, each with the same unbranded silver disc present.
1 — a thin unbranded plastic external drive, its tray half open with the disc in
it, its cable running to the laptop's only port; the mug at the back, handle out.
2 — three adapter dongles chained one into another, the disc propped against them
unread, the last connector hanging free; the mug turned, a pen beside it.
3 — a padded post bag lying open with the disc and a folded blank slip inside it,
ready to be sent away; the mug gone, a roll of tape in its place.

[GRADE — the same in all three]
Muted and cool, low saturation, no warm tone anywhere, from the overcast window
and the drab desktop rather than a filter. Still colour, never black and white.

No panel is favoured and no panel is brighter. None of the three wins and the
image makes no claim.
```

#### Option C — 01-pain-scene 1.14 `candid`

- varies on: execution: place, light and evidence rank
- ratio parameter: **16:9** · single-pass · 1520 characters
- why: Same type and object-only execution as A, moved off the desk onto a worktop and lit hard rather than low, with the evidence shifted to the cracked casing and the scratched disc - the failure the copy calls 'ran hot and failed to read our irreplaceable recordings'.
- note: G1-exempt. Shares its named dimension with A, so it is a true execution variant rather than a second route.

```prompt
TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
No person. The subject is a kitchen worktop where the overflow of a desk has
ended up, shot square on from worktop height.

[EVIDENCE]
A cheap grey plastic external drive lies on its side on the worktop with its
tray sprung open and empty, a hairline crack running from one corner of the
casing, and a silver disc face down beside it with a fan of fine scratches
across the playing side. Two adapter dongles sit coiled in a shallow bowl that
normally holds keys, their connectors tarnished, and a bundled cable has been
wound and tucked under the bowl's rim to keep it from unravelling.

[ENVIRONMENT]
An ordinary kitchen worktop by a wall socket, morning. Lived-in clutter
belonging to that place: a bread bin with crumbs at its foot, a jar of wooden
spoons, a tea towel hooked on the oven rail, a charger already occupying the
socket. Nothing arranged, nothing removed to tidy the frame.

[GAZE] no person in the frame.

[LIGHT] low-key. Key: hard morning sun through a window to the right, throwing a
sharp-edged shadow of the drive across the worktop. Fill: weak bounce off the
wall tiles. Rim light along the cracked casing edge. Deep shadow across the left
of the frame.

[FORBIDDEN] No reference product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
```

#### GIF — none

- why: A still life of what was already tried. It is a state the reader inspects, not a process, so nothing in it changes over time.

### `problems.items.1.image` — cause

*Beside 'Why standard external drives constantly fail'.* · asset `58-03-problems1-cause-anatomy.png`

**Recommended: option A.** FIT and PAGE LEGALITY agree. The copy names one mechanism - 'unbalanced internal motors shake the optical core, the laser drifts off track' - and 02-cause-anatomy exists to indict exactly that with a measured pair. It passes the removal test outright: take the unbalanced spindle out of the left panel and the read error goes with it, so this is a switchable state and not accumulated damage. --diagnostic is the variant for the advertorial middle where the culprit is named before the product is revealed, and features.items.0 downstream carries the product, which is the condition the variant sets. EVIDENCE: 30 renders behind measure, 18 behind verdict, and the two-mark budget is the type's proven configuration. PRODUCT PRESENCE: correctly absent, and that makes A G1-exempt and runnable today. PROMPT RISK: the offset difference is far past the 2:1 admission floor. B indicts the second cause the copy names and is the one to run if A's subject class struggles; C stays on vibration but moves the landmark to the platter.

#### Option A — 02-cause-anatomy 1.15 `diagnostic`  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **16:9** · single-pass · 1893 characters
- why: The measured pair is beam-to-track offset: wide on the bare spindle, closed to nothing in the damping carriage. Both lines anchor to the same two landmarks and only the offset differs, which is the type's one-property rule.
- note: FIRST NON-BIOLOGICAL body on this type - every rendered subject class so far has been anatomical (tooth, hair shaft, muscle, kneecap). The device is a 2D cross-section and the avoid_when only requires internal structure to draw, which a disc, track and lens have. Untested; watch the first render for the structures reading as a recognisable assembly. G1-exempt.

```prompt
TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, flat-vector. NOT photography, NOT 3D.

FRAME: the whole optical assembly of a disc drive in shot, seen in cross-section
from the side, the reading lens small within it.
GROUND: deep desaturated slate blue, the right half one step lighter than the
left.
BODY: a disc lying flat with its data track layer drawn as a fine ridged band on
its underside, and below it the reading lens carried on its sled, cut as flat
layers in warm ivory over a translucent drive-body outline. NOT a skeleton, NOT a
human figure. Exactly one assembly in EACH panel, same scale and same side view.

PANELS. LEFT: the assembly mounted on a bare unbalanced spindle motor drawn
realistically and unbranded, the motor's rotation shaking the sled so the lens
sits off to one side of the track and its beam lands on blank disc between two
ridges. RIGHT: the same assembly on the same interface, the sled seated in a
damping groove carriage of the same size, the lens held under the track and its
beam landing on the ridged band itself. The disc and its track layer appear in
both panels and neither the motor nor the carriage covers them.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PERPENDICULAR TO THE
  UNDERSIDE OF THE DISC, running from the centre of the track band down to the
  centre of the lens and STOPPING at both. Both begin at the same point on the
  track band, at the same place in their panel. Identical thickness and dash. One
  property differs: the sideways offset - wide on the left, closed to almost
  nothing on the right. Red left, blue right. Straight lines, not boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP corner,
  green with a white check in the right panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.
```

#### Option B — 02-cause-anatomy 1.15 `diagnostic`

- varies on: execution: which cause is indicted
- ratio parameter: **16:9** · single-pass · 1771 characters
- why: The copy names two causes and this is the second: 'thin laptops cut off power delivery when a drive shares bandwidth'. The measured pair becomes rail width at the port, pinched under a dongle chain and full under one powered hub.
- note: Also non-biological, and airbrushed rather than flat-vector so the two are not one look. Removal test passes: unplug the chain and the starvation goes. G1-exempt.

```prompt
TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, airbrushed. NOT photography, NOT 3D.

FRAME: the whole side wall of a slim laptop in shot with its single port, the
port opening small within it.
GROUND: deep desaturated plum, the right half one step lighter than the left.
BODY: the port opening and the power rail running back from it into the machine,
drawn as soft modelled layers in warm ivory over a translucent laptop-wall
outline, with the rail's width shown along its length. NOT a skeleton, NOT a
human figure. Exactly one port and rail in EACH panel, same scale and same side
view.

PANELS. LEFT: a chain of three separate adapter dongles drawn realistically and
unbranded, plugged one into another and all into that single port, the rail
behind the port drawn pinched narrow where the load meets it. RIGHT: one
combined hub unit of the same size seated at the same port, its own supply lead
running away to the side, the rail behind the port drawn at its full width. The
port and the rail appear in both panels and neither the dongle chain nor the hub
covers them.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PERPENDICULAR TO THE
  OUTER FACE OF THE PORT, running across the rail from one wall of it to the
  other and STOPPING at both. Both sit at the same distance behind the port, at
  the same place in their panel. Identical thickness and dash. One property
  differs: the rail width - narrow on the left, wide on the right. Red left, blue
  right. Straight lines, not boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP corner,
  green with a white check in the right panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.
```

#### Option C — 02-cause-anatomy 1.15 `diagnostic`

- varies on: execution: landmark pair and style
- ratio parameter: **16:9** · single-pass · 1697 characters
- why: Same cause as A, but the measurement moves off the beam onto the platter's tilt over its collar - a landmark pair that is easier to draw unambiguously than a beam, if A's optical section reads muddy.
- note: Front view rather than side, so it does not repeat A's composition. G1-exempt.

```prompt
TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, flat-vector. NOT photography, NOT 3D.

FRAME: the whole spindle motor and disc platter in shot, seen straight on from
the front, the bearing small within it.
GROUND: deep desaturated teal, the right half one step lighter than the left.
BODY: the spindle shaft, its bearing collar and the disc platter seated on it,
cut as flat layers in warm ivory over a translucent chassis outline. NOT a
skeleton, NOT a human figure. Exactly one spindle and platter in EACH panel, same
scale and same front view.

PANELS. LEFT: the shaft running in a bare loose-fitting collar drawn realistically
and unbranded, the platter tilted off level on it and its rim standing high on one
side. RIGHT: the same shaft in a counterweighted collar of the same size at the
same interface, the platter sitting level and its rim at the same height all the
way round. The platter and the collar appear in both panels and neither covers
the other.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PARALLEL TO THE FACE OF
  THE PLATTER, running from the top of the collar up to the underside of the
  platter rim on the raised side and STOPPING at both. Both begin at the same
  point on the collar, at the same place in their panel. Identical thickness and
  dash. One property differs: the gap - wide on the left, closed to almost
  nothing on the right. Red left, blue right. Straight lines, not boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP corner,
  green with a white check in the right panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.
```

#### Option D — GIF brief plate · G12 whole-frame  ← ADDITIONAL, not an alternative

- varies on: deliverable, not execution — the loop's work order, rendered alongside option A rather than instead of it
- ratio parameter: **16:9** · single-pass · 995 characters
- argues: **cause** · why: The cause this slot exists to indict IS temporal - a motor spins, the sled shakes, the beam drifts off the track. The still can only show the endpoint of that. 02-cause-anatomy legislates no motion layer of its own, so the form is whole-frame and the kind is the type's own job, cause.
- note: the plate never ships. Render it as `58-03-problems1-cause-anatomy--brief.png`, never the slot's own asset name (G12). The editor builds the 3s seamless loop from option A's still, replaces the plate, and delivers mp4/webm, under 2 MB.

```prompt
TYPE: G12 motion brief plate, whole-frame card
MEDIUM: a flat card carrying text and nothing else. NOT a photograph, NOT an
illustration, NOT a scene. Nothing is depicted.

The whole picture is flat dark grey, one even tone, no gradient and no texture.
One thin white rule runs inside it as a closed rectangle, its outer edge
finishing a clear margin short of the picture on all four sides, so no part of
it touches or leaves an edge.

Inside that rule, in clean white sans-serif, five short lines, each on one line,
left aligned, the block filling about half the picture's width:
GIF SLOT · 3s · seamless loop
SHOT both panels, held as drawn
ACTION left lens drifts off track
RESULT right lens holds the track
MATCH flat vector, same two grounds

Set those five lines exactly as written, as plain words. No asterisks, no
backticks, no bullets, no markdown of any kind, and no line wrapping.

This is the only text in the picture. No logo, no icon, no border decoration,
no product and no scene.
```

### `features.items.0.image` — mechanism

*Beside 'Anti-shock optical core stops laser vibration'.* · asset `58-04-features0-xray.png`

**Recommended: option A.** FIT is decisive and the gate makes it the only mechanism type available. body_contact is false for an external drive, which drops 03-mechanism-ghostbody by the slot-rules attribute gate, and 03-spec-split and 03-spec-explode are not advertorial types. That leaves xray, which is also exactly right: the section argues from an internal component the buyer cannot see, and xray exists to show real internals through a translucent shell. A is the top-down view because the carriage's length is the argument and it reads longest from above. EVIDENCE: type passed at 1.3 on two owner-passed worked examples; working carries 1 render. PRODUCT PRESENCE: the product IS the frame. PROMPT RISK: G1 binds the silhouette hard here and there is no reference photo yet, so this option cannot run until one is supplied. One mark only - the type's own rule is not to invent an emission, and this drive emits nothing outward, so output and caught are both absent.

#### Option A — 03-mechanism-xray 1.3  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **16:9** · single-pass · 1444 characters
- why: Top-down through the lid: the damping carriage runs the length of the bay so its travel is legible, and the beam standing up onto the disc is the one thing the section exists to show.
- note: Needs the product photo. Only working is used - the drive emits nothing visible outward, and G8 forbids inventing an effect so a render looks alive.

```prompt
TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the external
DVD drive. The outer shell becomes translucent, but its silhouette, proportions
and every visible external part must match the reference exactly. Do not redesign
or add features.

CANVAS: a plain deep charcoal ground, and nothing else in the frame behind the
product.

SHELL: the drive lying flat and seen from above and slightly to one side, its
top casing translucent and glass-like, filling about 75 percent of the frame
width.

INTERNALS, solid and detailed inside the shell, each at its true location: the
optical pickup lens on its sled, carried on a damping groove carriage that runs
the length of the bay; a flat spindle motor at the centre of the bay with a disc
seated on it; a control board along the back edge in its own real board colour;
a ribbon cable folding from the board to the sled.

MARKS, one, nothing else in the frame is marked:
- working: the optical pickup lens shown ACTIVE, throwing a narrow cool cyan
  beam straight up onto the underside of the disc above it, the brightest thing
  in the frame and clearly brighter than the ground. No arrow anywhere - the
  carriage's own line carries the direction of travel.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own.
```

#### Option B — 03-mechanism-xray 1.3

- varies on: execution: viewpoint and internals named
- ratio parameter: **16:9** · single-pass · 1389 characters
- why: End-on from the front edge, which brings the rear port bank into the same section as the optical core. It answers this section and sets up the next one in a single frame.
- note: Needs the product photo. Ground moves to pale warm grey so it is not one look with A.

```prompt
TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the external
DVD drive. The outer shell becomes translucent, but its silhouette, proportions
and every visible external part must match the reference exactly. Do not redesign
or add features.

CANVAS: a plain pale warm grey ground, and nothing else in the frame behind the
product.

SHELL: the drive seen end-on from its front edge and slightly above, the tray
seam facing the camera, its casing translucent and glass-like, filling about 70
percent of the frame width.

INTERNALS, solid and detailed inside the shell, each at its true location: the
optical pickup lens on its sled directly behind the tray seam, seated in a
damping groove carriage; a flat spindle motor behind it; a control board beneath
in its own real board colour; the port bank moulded into the rear wall with its
two rectangular openings, one oval opening and one card slot.

MARKS, one, nothing else in the frame is marked:
- working: the optical pickup lens shown ACTIVE, throwing a narrow cool cyan
  beam upward from the lens face, the brightest thing in the frame and clearly
  brighter than the ground. No arrow anywhere.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own.
```

#### Option C — 03-mechanism-xray 1.3

- varies on: execution: orientation and ground
- ratio parameter: **16:9** · single-pass · 1417 characters
- why: Standing on edge at a low three-quarter, which shows the drive's thinness at the same time as its internals - useful if the page wants the slim claim carried twice.
- note: Needs the product photo. A vertical subject in a 16:9 frame leaves side space; the plain ground absorbs it.

```prompt
TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the external
DVD drive. The outer shell becomes translucent, but its silhouette, proportions
and every visible external part must match the reference exactly. Do not redesign
or add features.

CANVAS: a plain deep olive ground, and nothing else in the frame behind the
product.

SHELL: the drive standing on its long edge and seen from a low front
three-quarter angle, its casing translucent and glass-like, filling about 65
percent of the frame height.

INTERNALS, solid and detailed inside the shell, each at its true location: the
optical pickup lens on its sled part-way along its damping groove carriage; a
flat spindle motor with a disc seated on it above the sled; a control board down
the lower edge in its own real board colour; a bridge chip on that board beside
the port bank.

MARKS, one, nothing else in the frame is marked:
- working: the optical pickup lens shown ACTIVE, throwing a narrow cool cyan beam
  across the short gap onto the disc surface facing it, the brightest thing in the
  frame and clearly brighter than the ground. No arrow anywhere - the carriage's
  own line carries the direction of travel.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own.
```

#### Option D — GIF brief plate · G12 whole-frame  ← ADDITIONAL, not an alternative

- varies on: deliverable, not execution — the loop's work order, rendered alongside option A rather than instead of it
- ratio parameter: **16:9** · single-pass · 1001 characters
- argues: **mechanism** · why: The mechanism is a travelling one - the sled runs its carriage while the disc turns - and a still can only assert that. 03-mechanism-xray legislates no motion layer, so the form is whole-frame and the kind is the type's own job, mechanism.
- note: the plate never ships. Render it as `58-04-features0-xray--brief.png`, never the slot's own asset name (G12). The editor builds the 3s seamless loop from option A's still, replaces the plate, and delivers mp4/webm, under 2 MB.

```prompt
TYPE: G12 motion brief plate, whole-frame card
MEDIUM: a flat card carrying text and nothing else. NOT a photograph, NOT an
illustration, NOT a scene. Nothing is depicted.

The whole picture is flat dark grey, one even tone, no gradient and no texture.
One thin white rule runs inside it as a closed rectangle, its outer edge
finishing a clear margin short of the picture on all four sides, so no part of
it touches or leaves an edge.

Inside that rule, in clean white sans-serif, five short lines, each on one line,
left aligned, the block filling about half the picture's width:
GIF SLOT · 3s · seamless loop
SHOT the render, held as built
ACTION sled tracks, beam stays centred
RESULT beam never leaves the disc
MATCH same charcoal ground, same cyan

Set those five lines exactly as written, as plain words. No asterisks, no
backticks, no bullets, no markdown of any kind, and no line wrapping.

This is the only text in the picture. No logo, no icon, no border decoration,
no product and no scene.
```

### `features.items.1.image` — spec

*Beside 'Built-in hub restores laptop connectivity'.* · asset `58-05-features1-relief-hero-detail.png`

**Recommended: option A.** This slot has no cell of its own and the ladder decides it. The mechanism cell is spent at features.items.0, 03-spec-explode and 03-spec-split are not advertorial, and 03-use-sequence - which the copy would otherwise suit - declares only 3:4 and 1:1, so it cannot serve a 16:9 slot at all. Rung 2 of the ladder moves to an adjacent step and 06-relief-hero carries it: the section's real argument is the after state of a desk, and --detail is the sanctioned way to magnify a feature too small to read at scene scale, which a port bank is. FIT: use_when names gallery images 2-3 and landing-page banners. EVIDENCE: the type is at 1.15 with 12 renders behind its marks, though --detail as a still inset is thinner than --recall. PRODUCT PRESENCE: the product is the desk's centre and every port is occupied, which is the claim. PROMPT RISK: needs the reference photo, and G1 binds it identically in both layers.

#### Option A — 06-relief-hero 1.15  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **16:9** · single-pass · 1917 characters
- why: Every port on the drive is occupied while the laptop keeps one lead and nothing else - the copy's claim made visible as a count rather than asserted. The inset magnifies the port bank, which is the one thing a desk-scale shot cannot resolve.
- note: Needs the product photo, in both layers identically. The inset occupies the space the subject is offset from, per the type's offset rule - no second reservation mid-frame.

```prompt
TYPE: 06-relief-hero v1.15 --commercial, inset --detail
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Man in his forties in a soft grey shirt, sitting back at a home desk with one
hand resting on a wireless mouse and the other loose in his lap, watching the
laptop screen rather than the drive. Relaxed, gaze away from the product.

[PRODUCT]
The drive on the desk between him and the laptop, front three-quarter angle,
whole and unobstructed, close enough to the camera to read. A single cable runs
from it to the laptop's one port. Into the drive's own rear ports run a mouse
receiver, a short cable to a phone lying beside it, and a memory card seated in
its card slot with its edge standing proud.

[SETTING]
A real home desk filled to the edges: a cold mug, a folded pair of glasses, a
notebook with a pen across it, a small plant, a coaster, a drawer unit under the
desk. None of them carries printed words. Background soft, never blank.

[LIGHT]
Soft even window light from the left, background blurred, high-key.

[LAYOUT]
He sits to the right of the frame; the left side carries the desk running away
from the camera.

In the upper left corner sits a rounded rectangular panel about a fifth of the
picture's width, held well clear of both frame edges, with a thin white border.
Inside it, one magnified straight-on view of the drive's rear port bank alone,
lit cleanly, close enough that the two rectangular ports, the single oval port
and the card slot are each separately readable, with a connector seated in one
of them. Nothing else is in the panel. It sits near the drive in the picture and
is joined to it by nothing - no arrow, no line, no glow.

No text on any object in either layer.
```

#### Option B — 06-relief-hero 1.15

- varies on: axis: register commercial -> ugc
- ratio parameter: **16:9** · single-pass · 1915 characters
- why: The same argument shot as a phone photo. An advertorial header register carries into the body well, and ugc buys trust where a clean desk can read as an advert.
- note: Needs the product photo. A crisp inset does not break the ugc register - that is settled on this type at 1.15.

```prompt
TYPE: 06-relief-hero v1.15 --ugc, inset --detail
REGISTER: shot on a phone by an ordinary person. Slightly off exposure, mild
overexposure at the window, no rim light, framing casual and a little too close.
The room is left exactly as it is.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Man in his forties in a T-shirt, leaning back in a desk chair with a mug in one
hand, looking at the laptop screen rather than at the drive. Relaxed.

[PRODUCT]
The drive on the desk beside the laptop, front three-quarter angle, whole and
unobstructed, close to the camera. One cable runs from it to the laptop's single
port. A mouse receiver, a phone lead and a memory card are each seated in the
drive's own rear ports and card slot.

[SETTING]
A real home desk left as it is: a charger brick, a bowl of coins, a crumpled
receipt-sized slip of blank paper, a plant that needs watering, a jumper over
the chair back, a bin under the desk. None of them carries printed words.
Background soft, never blank.

[LIGHT]
Flat daylight through a window behind the desk, slightly blown at the glass. No
studio light.

[LAYOUT]
He sits to the right of the frame; the left side carries the desk and the window.

In the upper left corner sits a rounded rectangular panel about a fifth of the
picture's width, held well clear of both frame edges, with a thin white border.
Inside it, one magnified straight-on view of the drive's rear port bank alone,
lit cleanly, close enough that the two rectangular ports, the single oval port
and the card slot are each separately readable, with a connector seated in one
of them. Nothing else is in the panel. It sits near the drive in the picture and
is joined to it by nothing - no arrow, no line, no glow.

No text on any object in either layer.
```

#### Option C — 06-relief-hero 1.15

- varies on: execution: subject full person -> reduced
- ratio parameter: **16:9** · single-pass · 2073 characters
- why: Hands only, with the card going into the slot. reduced is chosen when the result is more legible than the user, and here the result is a row of occupied ports.
- note: Needs the product photo. reduced requires naming what makes finished look different from unfinished, which this prompt does in its own block.

```prompt
TYPE: 06-relief-hero v1.15 --commercial, inset --detail
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Present only as working hands and forearms: two hands at a kitchen table, one
seating a memory card into the drive's card slot, the other steadying the drive
by its far corner. No face in the frame.

[PRODUCT]
The drive flat on the table, seen from above and slightly to one side, whole and
unobstructed, filling the middle of the picture. A single cable runs from it off
to a laptop at the edge of frame. A mouse receiver and a phone lead are already
seated in its rear ports.

[EVIDENCE IN FRAME]
Every one of the drive's own ports has something in it and the card sits proud in
its slot, while the laptop at the edge of frame has one lead going to the drive
and no other cable touching it anywhere along its side.

[SETTING]
A real kitchen table filled to the edges: a fruit bowl, a folded newspaper-sized
sheet of blank paper, a set of keys, a plant, a cloth over a chair back, a bag on
the floor beyond. None of them carries printed words. Background soft, never
blank.

[LIGHT]
Soft even window light from the right, background blurred, high-key.

[LAYOUT]
The hands and the drive sit to the left of the frame; the right side carries the
table running away from the camera.

In the lower right corner sits a rounded rectangular panel about a fifth of the
picture's width, held well clear of both frame edges, with a thin white border.
Inside it, one magnified straight-on view of the drive's rear port bank alone,
lit cleanly, close enough that the two rectangular ports, the single oval port
and the card slot are each separately readable, with a connector seated in one of
them. Nothing else is in the panel. It sits near the drive in the picture and is
joined to it by nothing - no arrow, no line, no glow.

No text on any object in either layer.
```

#### GIF — none

- why: The argument is a count of ports with things in them - a held state a reader inspects. Nothing flows and nothing changes, so the inset layer that --detail legislates has no temporal content to host a loop.

### `features.items.2.image` — spec

*Beside 'Rugged slim design built for cool operation'.* · asset `58-06-features2-relief-hero-context.png`

**Recommended: option A.** Rung 4: a second execution of a type already on the page, differing on named dimensions - inset_mode, subject, place and pose all change from features.items.1. Nothing else is available. FIT: --context is defined as the mode for when the hero shows the product in hand and the buyer still needs to see where it lives, which is precisely a slim drive going into a sleeve. HONEST LIMIT, and it is the reason this basis is hedged: the section's headline claim is thermal, and no photograph can show a casing staying cool. A argues the half that is photographable - the slim body against a closed laptop's edge - and the thermal claim is left to the copy. PRODUCT PRESENCE: the drive is held at the mouth of the sleeve, its thickness the subject. PROMPT RISK: needs the reference photo in both layers; G7-X binds one mode of use across hero and inset, which both A and C hold.

#### Option A — 06-relief-hero 1.15  ← RECOMMENDED

- varies on: execution: inset_mode detail -> context, and subject
- ratio parameter: **16:9** · single-pass · 1749 characters
- why: The drive measured against a closed laptop's edge is the slim claim made checkable, and the inset shows the same drive zipped in the same sleeve - the place it actually lives.
- note: Needs the product photo. Named dimension vs features.items.1: inset_mode, plus subject, place and pose. G7-X holds - handheld in both layers.

```prompt
TYPE: 06-relief-hero v1.15 --commercial, inset --context
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Woman in her thirties in a knitted jumper, standing at a hallway table with an
open laptop sleeve in one hand, sliding the drive down into it alongside a
closed laptop already inside, looking at the sleeve. Mid-action, hands engaged.

[PRODUCT]
The drive held upright in her hand at the mouth of the sleeve, side-on to the
camera, whole and unobstructed, its full thickness against the closed laptop's
edge behind it so the two read at the same scale.

[SETTING]
A real hallway filled to the edges: a bowl of keys on the table, a folded scarf,
a pair of shoes below, a coat on a hook, an umbrella leaning in the corner, a
radiator along the wall. None of them carries printed words. Background soft,
never blank.

[LIGHT]
Soft even daylight from a door glass to the left, background blurred, high-key.

[LAYOUT]
She stands to the right of the frame; the left side carries the hallway running
back to the door.

In the upper left corner sits a rectangular panel about a fifth of the picture's
width, held well clear of both frame edges, with a thin white border. Inside it,
a plainer closer shot of the same drive in the same place it lives: zipped inside
the same sleeve on the same hallway table, the sleeve's zip closed over it and
its outline just readable through the fabric, shot from a step back so the whole
sleeve is in the panel. Same light and same grade as the picture around it.

No text on any object in either layer.
```

#### Option B — 06-relief-hero 1.15

- varies on: axis: inset_mode context -> none
- ratio parameter: **16:9** · single-pass · 1405 characters
- why: No layer at all, and the argument moves to the long session the copy describes: a man mid-stretch at the end of it, a stack of burned discs beside the drive. It is the closest a photograph gets to the thermal claim without faking it.
- note: Needs the product photo. Simplest option on the page and the one to pick if the two-layer builds come back with the inset cut by a frame edge, which is this type's open geometry fault.

```prompt
TYPE: 06-relief-hero v1.15 --commercial, inset --none
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive.
Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT]
Man in his fifties in a work shirt with the sleeves turned back, sitting at a
dining table late in a long session, one hand resting flat on the table beside
the drive and the other on the back of his neck mid-stretch, looking out of the
window rather than at the machine. Relaxed, gaze away from the product.

[PRODUCT]
The drive flat on the table in front of him, front three-quarter angle, close to
the camera and whole and unobstructed, a disc seated in its open tray and a
short stack of three more discs beside it. One cable runs from it to a laptop
turned away at his elbow.

[SETTING]
A real dining table filled to the edges: a mug on a coaster, a pair of glasses
folded on a cloth, a bowl of apples, a jumper over the chair back, a lamp at the
table's end, curtains drawn back at the window. None of them carries printed
words. Background soft, never blank.

[LIGHT]
Soft even window light from the left, background blurred, high-key.

[LAYOUT]
He sits to the right of the frame; the left side carries the table running away
to the window.

No inset layer of any kind.

No text on any object in the picture.
```

#### Option C — 06-relief-hero 1.15

- varies on: execution: subject reduced, place and inset content
- ratio parameter: **16:9** · single-pass · 1798 characters
- why: Hands lifting the drive clear of a rucksack pocket, with the inset showing it stowed in that same pocket. Portability argued by where it has just come from rather than by a size comparison.
- note: Needs the product photo. Shares inset_mode with A, so it is an execution variant; keep only one of A and C on the page.

```prompt
TYPE: 06-relief-hero v1.15 --commercial, inset --context
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Present only as working hands and forearms: two hands at a study desk, one
lifting the drive clear of a rucksack's open front pocket, the other holding the
pocket's edge back. No face in the frame.

[PRODUCT]
The drive held flat in one hand just above the pocket, seen from above and
slightly to one side, whole and unobstructed, close to the camera.

[EVIDENCE IN FRAME]
The pocket it has come out of still holds a folded cable and a slim notebook and
lies open and slack, while the drive in the hand is clear of everything with
nothing wrapped round it.

[SETTING]
A real study desk filled to the edges: a desk lamp pushed back, a pot of pens, a
water glass, a pair of headphones coiled, a chair arm at the frame edge, a bag
strap trailing off the desk. None of them carries printed words. Background
soft, never blank.

[LIGHT]
Soft even window light from the right, background blurred, high-key.

[LAYOUT]
The hands and the drive sit to the left of the frame; the right side carries the
desk running away from the camera.

In the lower right corner sits a rectangular panel about a fifth of the picture's
width, held well clear of both frame edges, with a thin white border. Inside it,
a plainer closer shot of the same drive in the same place it lives: lying in that
same rucksack front pocket beside the same folded cable, shot from a step back so
the whole pocket is in the panel. Same light and same grade as the picture around
it.

No text on any object in either layer.
```

#### GIF — none

- why: Portability is a property, not an event. The section's other claim, staying cool across a weekend, is invisible in any register - a loop of a drive not overheating shows nothing - so motion would add duration without argument.

### `features.items.3.image` — outcome

*Beside 'Our family memories restored in one evening'.* · asset `58-07-features3-relief-scene.png`

**Recommended: option A.** FIT is unusually literal. 06-relief-scene's use_when asks for a closing image where the promise is a state of living rather than a feature, and the section is titled 'Our family memories restored in one evening'. PAGE LEGALITY: the type requires 01-pain-scene on the same page and it is there twice, so requires_pair is satisfied; the arc holds because every pain image sits above this one. The result_visibility gate does not drop it - the restored state is visible as a family watching a screen. EVIDENCE is where this recommendation is weak and the basis says so: the type is at 3.7 with 32 render records and zero passes at any 3.x version, and 3.7's product law - the label carrying the name and nothing else - was written yesterday and has never rendered. B is the safer type by evidence and the worse fit by argument. PRODUCT PRESENCE: 3.7 requires the drive to stand in frame as its own object with its face readable, which A does on the low table. PROMPT RISK: highest on the page.

#### Option A — 06-relief-scene 3.7  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **16:9** · single-pass · 1816 characters
- why: The situation costs something - three people gathered for something that could not be played before - and the product stands in frame as its own object with its face to the lens, which is 3.7's product law.
- note: Needs the product photo. The type has 0 passes at any 3.x, and this prompt is the first test of 3.7's name-only label clause. Expect to iterate.

```prompt
TYPE: 06-relief-scene v3.7 --none
REGISTER: a candid documentary photograph a passer-by could have taken. Single
frame, natural, unposed, sharp. Nobody aware of a camera.

PRODUCT REFERENCE: use the attached photo as the exact reference. Preserve
shape, proportions, material, finish and colour exactly. Do not redesign or add
features.

A man in his forties is on a sofa between his wife and their daughter, all three
turned toward a television across the room, the daughter half out of her seat
pointing at the screen at something she has just recognised. Not at the camera.
He is upright and leaning in.

His eyes are open and creased at the corners and a small smile has arrived on its
own. His chest is open, his shoulders are rolled back and down, his chin is up.
Nothing is braced and neither hand has gone to the remote.

The drive stands on the low table directly in front of them, close to the camera
in the near part of the frame, a disc seated in its open tray and its face turned
toward the lens so its name can be read. The label carries only the product name
- no other printed text, no back-of-pack panel, no barcode. It is not centred and
not lit for the camera. He is not looking at it and not touching it.

Nothing is drawn onto this photograph. There is no diagram, no inset, no panel
and no glow of any kind.

An ordinary front room: an open DVD case on the table, a throw over the sofa arm,
a lamp on, a plant by the window, curtains drawn back on an evening street.

LIGHT: lamp light and the last of the daylight, kind and even, no rim light, no
glamour lighting.
GRADE: natural colour, light film grain, shallow depth of field. Honest, not
glossy, and not drained.

No printed text on any object in the scene except the product name on the drive.
No logo, no watermark, no arrows, no badges.
```

#### Option B — 06-relief-hero 1.15

- varies on: type: 06-relief-scene -> 06-relief-hero
- ratio parameter: **16:9** · single-pass · 2017 characters
- why: The same outcome on the better-evidenced type. --recall holds one reminder of the problem beside the resolved state, and the pair changes only the machine on the table - which is the type's own 2/2 rule for a recall pair.
- note: Needs the product photo. PICKING B FORCES features.items.1 AND features.items.2 TO CHANGE - three 06-relief-hero executions on one linear funnel is past what rung 4 permits. Also puts a pain cue below the page's first relief image, which the arc rule allows only because it is inside an inset.

```prompt
TYPE: 06-relief-hero v1.15 --commercial, inset --recall
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Man in his forties on a sofa with a girl of about eight leaning against his
shoulder, both turned toward a television across the room, his free arm along the
sofa back. Relaxed, gaze away from the product.

[PRODUCT]
The drive on the low table in front of the sofa, front three-quarter angle, close
to the camera and whole and unobstructed, a disc seated in its open tray, one
cable running to a laptop beside it.

[SETTING]
A real front room filled to the edges: an open disc case on the table, a mug, a
throw over the sofa arm, a cushion pushed down the back, a lamp lit in the
corner, a plant on the sill. None of them carries printed words. Background soft,
never blank.

[LIGHT]
Soft even window light with the lamp lit behind, background blurred, high-key.

[LAYOUT]
The sofa sits to the right of the frame; the left side carries the room back to
the window.

In the upper left corner sit two small square cells side by side, together about
a fifth of the picture's width, held well clear of both frame edges, each with a
thin white border. The same man on the same sofa in the same room in both cells,
and the only thing that differs between them is the machine on the table. In the
first cell a thin unbranded plastic drive sits there with its tray half open and
a disc stuck in it, and that whole cell is desaturated to grey while everything
else in the picture keeps its colour. In the second cell the reference drive sits
in the same spot with the disc seated and the television lit. One plain arrow
runs from the first cell to the second and joins those two cells only. Both cells
match the picture around them in resolution, grade and light quality.

No text on any object in any layer.
```

#### Option C — 06-relief-scene 3.7

- varies on: execution: subject, generation and place
- ratio parameter: **16:9** · single-pass · 1775 characters
- why: The same argument one generation up - a grandmother and a teenager at a kitchen table - which widens the persona the brief describes beyond the byline's own family.
- note: Needs the product photo. Same type risk as A.

```prompt
TYPE: 06-relief-scene v3.7 --none
REGISTER: a candid documentary photograph a passer-by could have taken. Single
frame, natural, unposed, sharp. Nobody aware of a camera.

PRODUCT REFERENCE: use the attached photo as the exact reference. Preserve
shape, proportions, material, finish and colour exactly. Do not redesign or add
features.

A woman in her sixties is at a kitchen table with a laptop open in front of her
and a teenage grandson standing at her shoulder, both watching the screen, the
boy laughing at something on it. Not at the camera. She is upright and leaning
toward the screen.

Her eyes are open and creased at the corners and a small smile has arrived on its
own. Her chest is open, her shoulders are rolled back and down, her chin is up.
Nothing is braced and neither hand has gone to the screen.

The drive stands on the table beside the laptop, close to the camera in the near
part of the frame, a disc seated in its open tray and its face turned toward the
lens so its name can be read. The label carries only the product name - no other
printed text, no back-of-pack panel, no barcode. It is not centred and not lit
for the camera. She is not looking at it and not touching it.

Nothing is drawn onto this photograph. There is no diagram, no inset, no panel
and no glow of any kind.

An ordinary kitchen: a shoebox of loose discs open at the table's end, two mugs,
a tea towel on the oven rail, a window with a garden beyond it.

LIGHT: afternoon daylight from the window, kind and even, no rim light, no
glamour lighting.
GRADE: natural colour, light film grain, shallow depth of field. Honest, not
glossy, and not drained.

No printed text on any object in the scene except the product name on the drive.
No logo, no watermark, no arrows, no badges.
```

#### GIF — none

- why: The slot's reason to exist is an after-state - a family who can watch the disc - and a held state is what it has to prove. 06-relief-scene also bans every layer except the --detail inset, so there is no legislated layer a loop could occupy without breaking the register.

### `features.items.4.image` — comparison

*Beside 'Replaces three separate purchases for less'.* · asset `58-08-features4-lockedframe-verdict.png`

**Recommended: option A.** FIT and EVIDENCE agree, and this is where the page's one 04-proof-lockedframe is best spent. use_when wants a buyer who already understands the problem and the mechanism and now wants to see for themselves - true here and false at problems.items.0, which is why the type lands in this slot and not that one. --verdict is the variant with the product in the last panel, and the copy's claim is a straight count of bodies and cables. The variant-selection rule permits it: this difference IS visible in a static frame, unlike the section's cost claim, which no image can carry. EVIDENCE: 1.13, owner-passed, two rendered worked examples. PRODUCT PRESENCE: last panel only, which is the order rule. PROMPT RISK: needs the reference photo; runs handheld rather than strict because the capability gate says strict needs compositing and this pipeline renders one frame by hand.

#### Option A — 04-proof-lockedframe 1.13 `verdict`  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **16:9** · single-pass · 1795 characters
- why: Three panels on one desk: one plain drive, then three bodies and four cables, then the reference drive alone. The fairness rule is stated in the prompt because the alternatives here are products the reader may already own.
- note: Needs the product photo. generation_mode is multi-pass at type level, but 1.8's capability gate runs --verdict handheld in one pass where the renderer cannot composite, which is the case here.

```prompt
TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the drive in the LAST panel.
Preserve shape, proportions, material, finish and colour exactly.

[SCENE — the same in all three]
The same corner of a home desk, the same dark wood desktop, a closed laptop and
a cold mug pushed to the back. Flat overcast light from a window off to the
left, no strong shadows, no styling.

[FRAMING]
One person photographed this three times from where they always sit, phone level
with the desktop, the bare wood filling the middle third and the laptop
across the upper third. It reads as one shot taken three times, never as three
different shots. Light differs only in exposure, never warmth.

[THE VARIABLE]
What has to sit on a desk to read a disc, move files off a card and keep a mouse
plugged in. Every panel at the same moment: connected, nothing in hand, the same
unbranded silver disc and memory card in all three.
1 — a plain unbranded optical drive alone, one cable, the card beside it
unread; the mug at the back, handle out.
2 — that same drive plus a separate powered hub and a separate card reader,
three bodies and four cables; the mug turned, a pen beside it.
3 — the reference drive alone, one cable, the card in its own slot; the mug gone,
a coaster in its place.

[GRADE — the same in all three]
Neutral, from the overcast window and the drab desktop rather than a filter.
Still colour, never black and white.

Panels one and two get the same exposure, tidiness and framing as panel three;
the alternatives are ordinary products someone would buy, never made to look
worse.
```

#### Option B — 04-proof-lockedframe 1.13 `verdict`

- varies on: execution: scene, framing and the moment compared
- ratio parameter: **16:9** · single-pass · 1767 characters
- why: The same count argued as what has to go in a bag rather than what sits on a desk, shot down onto a kitchen table. Coiled cables read as volume more plainly than connected ones.
- note: Needs the product photo. Every panel sits at the same moment - nothing packed yet - which is the type's moment rule.

```prompt
TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the drive in the LAST panel.
Preserve shape, proportions, material, finish and colour exactly.

[SCENE — the same in all three]
The same kitchen table, the same pale scrubbed wood, a chair back at the frame
edge and a folded cloth pushed to the far side. Flat daylight from a window off
to the right, no strong shadows, no styling.

[FRAMING]
One person photographed this three times from where they always sit, phone above
the table looking down, the bare wood filling the middle third and the
chair back across the upper third. It reads as one shot taken three times, never
as three different shots. Light differs only in exposure, never warmth.

[THE VARIABLE]
What has to go into a bag to take disc reading and card transfer elsewhere.
Every panel at the same moment: laid out beside the same open laptop sleeve,
nothing packed yet, the same unbranded silver disc in all three.
1 — a plain unbranded optical drive, cable coiled beside it; the cloth folded
square.
2 — that same drive, a separate powered hub with its own mains lead and a
separate card reader, each cable coiled; the cloth rucked at one corner.
3 — the reference drive, its one cable coiled; the cloth closer, a spoon beside
it.

[GRADE — the same in all three]
Neutral, from the window and the pale table rather than a filter. Still colour,
never black and white.

Panels one and two get the same exposure, tidiness and framing as panel three;
the alternatives are ordinary products someone would buy, never made to look
worse.
```

#### Option C — 04-proof-lockedframe 1.13 `verdict`

- varies on: execution: place and what carries the argument
- ratio parameter: **16:9** · single-pass · 1795 characters
- why: A living-room shelf rather than a work surface, arguing the count as what has to live permanently in a room. Cables running off the shelf edge are the visible difference.
- note: Needs the product photo. The disc spines behind must stay unbranded and unreadable - the type bars recognisable trademarks outright.

```prompt
TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the drive in the LAST panel.
Preserve shape, proportions, material, finish and colour exactly.

[SCENE — the same in all three]
The same living-room shelf, the same veneered board, a row of unmarked disc
spines and a small plant at one end. Flat room light from a window off to the
left, no strong shadows, no styling.

[FRAMING]
One person photographed this three times from where they always stand, phone
level with the shelf, the board filling the middle third and the spines across
the upper third. It reads as one shot taken three times, never as
three different shots. Light differs only in exposure, never warmth.

[THE VARIABLE]
What has to live beside a television to play discs and read a camera card. Every
panel at the same moment: in place and connected, nothing handled, the same
unbranded silver disc and memory card in all three.
1 — a plain unbranded optical drive, one cable off the shelf, the card propped
against it; the plant at the left end, leaves upright.
2 — that same drive, a separate powered hub and a card reader, three bodies
with four cables; the plant turned, a leaf over the board.
3 — the reference drive alone, one cable, the card in its slot; the plant gone,
a coaster in its place.

[GRADE — the same in all three]
Neutral, from the room light and the veneered board rather than a filter. Still
colour, never black and white.

Panels one and two get the same exposure, tidiness and framing as panel three;
the alternatives are ordinary products someone would buy, never made to look
worse.
```

#### GIF — none

- why: A locked-frame comparison is inspected, not watched - the reader's eye does the travelling between panels. Motion here would also break the judgement rule by drawing the eye to one panel.

### `reviews.shots.0.image` — social-proof

*First of four customer-photo tiles above the review quotes.* · asset `58-09-reviews-shot-0.png`

**Recommended: option A.** MODE and light decide it. A is the default in-use mode and the only one of the four A options that shows the drive actually reading, which anchors the set. Its warm dim lamp light is the furthest from tile 1's flat kitchen overhead, tile 2's mixed floor light and tile 3's cool shelf daylight, so the set diversity law holds at the A level. EVIDENCE: the type passed at 1.2 on 2 of 2 renders, both with empty failure lists, and in-use is the mode its owner-passed socket-tester example used.

#### Option A — 05-social-snapshot 1.2  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **1:1** · single-pass · 1068 characters
- why: in-use at a warm-lit home-office desk, the drive mid-read with a forearm incidentally in frame. The default mode, and the one that shows the product doing something.
- note: BLOCKED AS THE PAGE IS BUILT. 05-social-snapshot's authenticity fence is hard and non-negotiable: no reviewer name, avatar, star row or verified label anywhere near the image in the layout. reviews.shots.0-3 sit inside the same section element as reviews.quotes.0-2, which carry names (Martin K., Gillian R., Derek S.) and a 'Verified Purchase' label each. Rendering these four beside that copy presents generated pictures as customer uploads, which is a fabricated endorsement. Either move the shots out of the attributed block, or drop the names and verified labels from that block, or use real customer photographs - which always win over generated ones.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It sits flat on the desk, seen from above and slightly to one side, cropped the way a casual one-handed photo crops.

CONTENT MODE, in-use: the drive is mid-read on a desk, its tray closed on a disc and its status light lit, one forearm resting on the desk beside it in a rolled shirt cuff and no face in the frame.

ANCHOR: a coiled phone charger pushed to one side.

SCENE: a home-office desk photographed as found - a coffee ring dried on the wood, a cable snaking off the back edge, a radiator half in shot at the frame edge. Warm dim light from a single desk lamp, the room behind it going dark.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### Option B — 05-social-snapshot 1.2

- varies on: mode: in-use -> at-rest
- ratio parameter: **1:1** · single-pass · 1067 characters
- why: The same desk with the drive simply living there, part-peeled factory film still on the lid. at-rest is the mode that best carries 'this exists and someone owns it'.
- note: Needs the product photo. SET DIVERSITY LAW: the four A options are deliberately four different rooms, surfaces, light temperatures, camera distances and content modes. Generate them as independent prompts, never as a batch with shared seeds or shared scene text.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It sits flat on the desk, seen from above and slightly to one side, cropped the way a casual one-handed photo crops.

CONTENT MODE, at-rest: the drive simply sitting where it now lives on the desk, its tray closed and nothing plugged into it, a factory protective film still part-peeled from one corner of the lid.

ANCHOR: a coiled phone charger pushed to one side.

SCENE: a home-office desk photographed as found - a coffee ring dried on the wood, a cable snaking off the back edge, a radiator half in shot at the frame edge. Warm dim light from a single desk lamp, the room behind it going dark.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### Option C — 05-social-snapshot 1.2

- varies on: execution: room class, light temperature and distance
- ratio parameter: **1:1** · single-pass · 1023 characters
- why: in-use again but on a bedroom windowsill under cold overcast daylight, shot further back. Use it if the desk scene collides with another tile.
- note: Needs the product photo. SET DIVERSITY LAW: the four A options are deliberately four different rooms, surfaces, light temperatures, camera distances and content modes. Generate them as independent prompts, never as a batch with shared seeds or shared scene text.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It sits flat on the sill, seen almost straight on from the side, cropped the way a casual one-handed photo crops.

CONTENT MODE, in-use: the drive is mid-read on a desk, its tray closed on a disc and its status light lit, one forearm resting on the desk beside it in a rolled shirt cuff and no face in the frame.

ANCHOR: a pair of earphones tangled at the sill's edge.

SCENE: a bedroom windowsill desk photographed as found - a dusty sill, a mug ring, a curtain hem hanging into the frame. Cold blue-grey daylight from an overcast window right beside it.

CAMERA TRUTH: framing off-centre and a little far back, focus adequate, mild motion softness, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### GIF — none

- why: A customer snapshot argues that the thing exists in a real home. That is a held state, and this type bans every added layer, so there is nothing a loop could occupy.

### `reviews.shots.1.image` — social-proof

*Second of four customer-photo tiles above the review quotes.* · asset `58-10-reviews-shot-1.png`

**Recommended: option A.** MODE carries this tile. kit-flatlay is the one mode that shows what actually arrives in the box, which answers the 'both adapter cables came included' line in the copy without the image claiming anything. Its flat overhead kitchen light and top-down distance are distinct from all three other tiles. PROMPT RISK: the leaflet must stay illegible at size - the type allows generated print only where it cannot be read, and a readable one would be an invented claim.

#### Option A — 05-social-snapshot 1.2  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **1:1** · single-pass · 1046 characters
- why: kit-flatlay on a kitchen table under flat green-tinged overhead light - the opened box as an owner actually keeps it, cables loosely coiled and the lid shoved aside.
- note: BLOCKED AS THE PAGE IS BUILT. 05-social-snapshot's authenticity fence is hard and non-negotiable: no reviewer name, avatar, star row or verified label anywhere near the image in the layout. reviews.shots.0-3 sit inside the same section element as reviews.quotes.0-2, which carry names (Martin K., Gillian R., Derek S.) and a 'Verified Purchase' label each. Rendering these four beside that copy presents generated pictures as customer uploads, which is a fabricated endorsement. Either move the shots out of the attributed block, or drop the names and verified labels from that block, or use real customer photographs - which always win over generated ones.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It lies flat among the other contents, seen from above, cropped the way a casual one-handed photo crops.

CONTENT MODE, kit-flatlay: the opened box contents as the owner keeps them, slightly disordered - the drive, its two cables loosely coiled, and a small folded leaflet, laid out on the table with the empty box lid pushed to one side.

ANCHOR: a mug of cold tea at the corner of the table.

SCENE: a kitchen table photographed as found - crumbs at one edge, a faint water mark on the wood, a chair back blurred at the frame edge. Flat overhead kitchen light, slightly green.

CAMERA TRUTH: framing off-centre and shot from directly above at arm's length, focus adequate, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### Option B — 05-social-snapshot 1.2

- varies on: mode: kit-flatlay -> at-rest
- ratio parameter: **1:1** · single-pass · 990 characters
- why: The same table with just the drive set down after unboxing, a factory sticker still on it whose print stays too small to read.
- note: Needs the product photo. SET DIVERSITY LAW: the four A options are deliberately four different rooms, surfaces, light temperatures, camera distances and content modes. Generate them as independent prompts, never as a batch with shared seeds or shared scene text.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It sits flat on the table, seen from above, cropped the way a casual one-handed photo crops.

CONTENT MODE, at-rest: the drive sitting on the table where it was set down after unboxing, its tray closed, a factory sticker still on the underside edge with its print too small to read.

ANCHOR: a mug of cold tea at the corner of the table.

SCENE: a kitchen table photographed as found - crumbs at one edge, a faint water mark on the wood, a chair back blurred at the frame edge. Flat overhead kitchen light, slightly green.

CAMERA TRUTH: framing off-centre and shot from directly above at arm's length, focus adequate, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### Option C — 05-social-snapshot 1.2

- varies on: execution: room class, light temperature and surface
- ratio parameter: **1:1** · single-pass · 1067 characters
- why: The same flatlay moved onto a living-room carpet under a warm standard lamp and shot from standing height.
- note: Needs the product photo. SET DIVERSITY LAW: the four A options are deliberately four different rooms, surfaces, light temperatures, camera distances and content modes. Generate them as independent prompts, never as a batch with shared seeds or shared scene text.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It lies flat among the other contents, seen from above and at an angle, cropped the way a casual one-handed photo crops.

CONTENT MODE, kit-flatlay: the opened box contents as the owner keeps them, slightly disordered - the drive, its two cables loosely coiled, and a small folded leaflet, laid out on a carpet with the empty box lid pushed to one side.

ANCHOR: a television remote lying beside the pile.

SCENE: a living-room carpet photographed as found - a flattened patch of pile, a stray thread, the foot of an armchair at the frame edge. Warm yellow light from a standard lamp overhead.

CAMERA TRUTH: framing tilted and shot from standing height looking down, focus adequate, mild noise, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### GIF — none

- why: A customer snapshot argues that the thing exists in a real home. That is a held state, and this type bans every added layer, so there is nothing a loop could occupy.

### `reviews.shots.2.image` — social-proof

*Third of four customer-photo tiles above the review quotes.* · asset `58-11-reviews-shot-2.png`

**Recommended: option A.** FIT to the copy decides it. This is the only tile that shows the SD slot in use, and the reviews lead names 'transferred raw camera photos from the SD slot' as one of the three things buyers mention. Its mixed warm-and-cold floor light and kneeling-height distance keep it apart from the other three. COMPLIANCE: fingers only and no face - a face turns a snapshot into a testimonial portrait, which is a different type's job and a risk here.

#### Option A — 05-social-snapshot 1.2  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **1:1** · single-pass · 1081 characters
- why: in-use on a living-room floor in mixed lamp-and-window light, a memory card going into the slot with two fingers just leaving it, shot from kneeling height.
- note: BLOCKED AS THE PAGE IS BUILT. 05-social-snapshot's authenticity fence is hard and non-negotiable: no reviewer name, avatar, star row or verified label anywhere near the image in the layout. reviews.shots.0-3 sit inside the same section element as reviews.quotes.0-2, which carry names (Martin K., Gillian R., Derek S.) and a 'Verified Purchase' label each. Rendering these four beside that copy presents generated pictures as customer uploads, which is a fabricated endorsement. Either move the shots out of the attributed block, or drop the names and verified labels from that block, or use real customer photographs - which always win over generated ones.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It sits flat on the rug, seen from a low angle almost level with the floor, cropped the way a casual one-handed photo crops.

CONTENT MODE, in-use: the drive is connected on a living-room floor beside a laptop, a memory card seated in its slot and its status light lit, two fingers just leaving the card and no face in the frame.

ANCHOR: an open disc case lying face down on the rug.

SCENE: a living-room floor photographed as found - a rug edge rucked up, a scatter of toy pieces pushed aside, a sofa foot at the frame edge. Mixed light, warm lamp on one side and cold daylight from a window on the other.

CAMERA TRUTH: framing tilted and very close, kneeling height, focus adequate, mild motion softness, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### Option B — 05-social-snapshot 1.2

- varies on: mode: in-use -> at-rest
- ratio parameter: **1:1** · single-pass · 1039 characters
- why: The same rug with the drive left where it was used, one cable still trailing off toward a laptop out of frame.
- note: Needs the product photo. SET DIVERSITY LAW: the four A options are deliberately four different rooms, surfaces, light temperatures, camera distances and content modes. Generate them as independent prompts, never as a batch with shared seeds or shared scene text.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It sits flat on the rug, seen from a low angle almost level with the floor, cropped the way a casual one-handed photo crops.

CONTENT MODE, at-rest: the drive sitting on the rug where it was left after use, its tray shut and one cable still trailing from it toward a laptop out of frame.

ANCHOR: an open disc case lying face down on the rug.

SCENE: a living-room floor photographed as found - a rug edge rucked up, a scatter of toy pieces pushed aside, a sofa foot at the frame edge. Mixed light, warm lamp on one side and cold daylight from a window on the other.

CAMERA TRUTH: framing tilted and very close, kneeling height, focus adequate, mild motion softness, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### Option C — 05-social-snapshot 1.2

- varies on: execution: room class and light temperature
- ratio parameter: **1:1** · single-pass · 1024 characters
- why: The card-reader action moved to a garage workbench under cold fluorescent strip light, which is the furthest room class from the other three tiles.
- note: Needs the product photo. SET DIVERSITY LAW: the four A options are deliberately four different rooms, surfaces, light temperatures, camera distances and content modes. Generate them as independent prompts, never as a batch with shared seeds or shared scene text.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It sits flat on the bench, seen from above and slightly to one side, cropped the way a casual one-handed photo crops.

CONTENT MODE, in-use: the drive is connected on a garage workbench beside a laptop, a memory card seated in its slot and its status light lit, two fingers just leaving the card and no face in the frame.

ANCHOR: a screwdriver lying across the bench behind it.

SCENE: a garage workbench photographed as found - sawdust in the grain, a paint mark, a vice bolted at the frame edge. Cold strip light from a fluorescent tube overhead.

CAMERA TRUTH: framing off-centre and close, standing height looking down, focus adequate, mild noise, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### GIF — none

- why: A customer snapshot argues that the thing exists in a real home. That is a held state, and this type bans every added layer, so there is nothing a loop could occupy.

### `reviews.shots.3.image` — social-proof

*Fourth of four customer-photo tiles above the review quotes.* · asset `58-12-reviews-shot-3.png`

**Recommended: option A.** MODE and set balance decide it. Three tiles already show the drive being handled or unboxed, so the fourth earns its place by showing where it ends up living, which is the at-rest mode's whole argument. The disc spines behind it must stay unbranded and unreadable. Its cool falling-off daylight and longer distance complete the four-way separation the set diversity law requires.

#### Option A — 05-social-snapshot 1.2  ← RECOMMENDED

- varies on: baseline
- ratio parameter: **1:1** · single-pass · 1026 characters
- why: at-rest on a living-room shelf beside a row of disc spines under cool falling-off daylight, shot a little far back and slightly low.
- note: BLOCKED AS THE PAGE IS BUILT. 05-social-snapshot's authenticity fence is hard and non-negotiable: no reviewer name, avatar, star row or verified label anywhere near the image in the layout. reviews.shots.0-3 sit inside the same section element as reviews.quotes.0-2, which carry names (Martin K., Gillian R., Derek S.) and a 'Verified Purchase' label each. Rendering these four beside that copy presents generated pictures as customer uploads, which is a fabricated endorsement. Either move the shots out of the attributed block, or drop the names and verified labels from that block, or use real customer photographs - which always win over generated ones.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It stands on the shelf, seen almost straight on from the front, cropped the way a casual one-handed photo crops.

CONTENT MODE, at-rest: the drive sitting on a shelf where it now lives beside a short row of disc spines, its tray shut, one cable dropping away behind the shelf board.

ANCHOR: a set of keys dropped on the board beside it.

SCENE: a living-room shelf photographed as found - a dust line along the board, a photo frame turned slightly out of square, wallpaper seam visible behind. Cool daylight from a window across the room, falling off toward the shelf's far end.

CAMERA TRUTH: framing a little far back and slightly low, focus adequate, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### Option B — 05-social-snapshot 1.2

- varies on: mode: at-rest -> in-use
- ratio parameter: **1:1** · single-pass · 1045 characters
- why: The same shelf with the drive mid-read and a hand withdrawing at the frame edge.
- note: Needs the product photo. SET DIVERSITY LAW: the four A options are deliberately four different rooms, surfaces, light temperatures, camera distances and content modes. Generate them as independent prompts, never as a batch with shared seeds or shared scene text.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It stands on the shelf, seen almost straight on from the front, cropped the way a casual one-handed photo crops.

CONTENT MODE, in-use: the drive is mid-read on the shelf, its tray closed on a disc and its status light lit, one hand just withdrawing from it at the frame edge and no face in the frame.

ANCHOR: a set of keys dropped on the board beside it.

SCENE: a living-room shelf photographed as found - a dust line along the board, a photo frame turned slightly out of square, wallpaper seam visible behind. Cool daylight from a window across the room, falling off toward the shelf's far end.

CAMERA TRUTH: framing a little far back and slightly low, focus adequate, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### Option C — 05-social-snapshot 1.2

- varies on: execution: room class, light and distance
- ratio parameter: **1:1** · single-pass · 1047 characters
- why: at-rest on a hallway table beside a folded laptop sleeve under a single dim warm bulb, shot quickly from above.
- note: Needs the product photo. SET DIVERSITY LAW: the four A options are deliberately four different rooms, surfaces, light temperatures, camera distances and content modes. Generate them as independent prompts, never as a batch with shared seeds or shared scene text.

```prompt
TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. It sits flat on the table, seen from above and at an angle, cropped the way a casual one-handed photo crops.

CONTENT MODE, at-rest: the drive sitting on a hallway table where it now lives beside a folded laptop sleeve, its tray shut and nothing plugged into it.

ANCHOR: an unopened envelope-shaped blank card propped against the wall behind it.

SCENE: a hallway table photographed as found - a scuff on the paintwork behind, a shoe half in frame on the floor below, a coat sleeve hanging into the top of the picture. Dim warm light from a single hallway bulb.

CAMERA TRUTH: framing tilted and shot quickly from above at arm's length, focus adequate, mild motion softness, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect.
```

#### GIF — none

- why: A customer snapshot argues that the thing exists in a real home. That is a held state, and this type bans every added layer, so there is nothing a loop could occupy.

### `product.image` — cta

*Product card in the mid-page 'Our top pick for disc recovery' block.* · asset `—`

**Out of library scope.** The cta row of mapping/slot-rules.md is empty by design across all four channels: a product card's image is a standard product shot, which the library does not cover. This is a deliberately empty cell, not an exhausted one, so the widening ladder does not apply. Shoot or supply the pack shot.

---

### `product_end.image` — cta

*Product card in the closing 'The compact drive that restored our archive' block.* · asset `—`

**Out of library scope.** Same as product.image - a closing CTA product card. Standard product shot, out of library scope.

---

### `hero.author_avatar` — author

*Byline portrait beside 'By Warren Hayes'.* · asset `—`

**Out of library scope.** A portrait of a named author. No library type produces portraits, and generating a face to sit under a real-sounding byline manufactures a person. Use a real photograph of the actual author or drop the avatar.

---

### `guide.avatar` — author

*Portrait in the 'About the author' block.* · asset `—`

**Out of library scope.** Same as hero.author_avatar - a named person's portrait. Out of library scope and a disclosure question rather than an imaging one.

---

### `comments.items.0.avatar` — social-proof

*Commenter portrait, comment 1 of 6.* · asset `—`

**Out of library scope.** A portrait attached to a named commenter. Out of library scope, and generating one would put an invented face beside an invented name in a block that reads as real user comments. 05-social-snapshot's fence names avatars specifically as what a generated image must never sit beside. Supply real avatars or render the block without them.

---

### `comments.items.1.avatar` — social-proof

*Commenter portrait, comment 2 of 6.* · asset `—`

**Out of library scope.** A portrait attached to a named commenter. Out of library scope, and generating one would put an invented face beside an invented name in a block that reads as real user comments. 05-social-snapshot's fence names avatars specifically as what a generated image must never sit beside. Supply real avatars or render the block without them.

---

### `comments.items.2.avatar` — social-proof

*Commenter portrait, comment 3 of 6.* · asset `—`

**Out of library scope.** A portrait attached to a named commenter. Out of library scope, and generating one would put an invented face beside an invented name in a block that reads as real user comments. 05-social-snapshot's fence names avatars specifically as what a generated image must never sit beside. Supply real avatars or render the block without them.

---

### `comments.items.3.avatar` — social-proof

*Commenter portrait, comment 4 of 6.* · asset `—`

**Out of library scope.** A portrait attached to a named commenter. Out of library scope, and generating one would put an invented face beside an invented name in a block that reads as real user comments. 05-social-snapshot's fence names avatars specifically as what a generated image must never sit beside. Supply real avatars or render the block without them.

---

### `comments.items.4.avatar` — social-proof

*Commenter portrait, comment 5 of 6.* · asset `—`

**Out of library scope.** A portrait attached to a named commenter. Out of library scope, and generating one would put an invented face beside an invented name in a block that reads as real user comments. 05-social-snapshot's fence names avatars specifically as what a generated image must never sit beside. Supply real avatars or render the block without them.

---

### `comments.items.5.avatar` — social-proof

*Commenter portrait, comment 6 of 6.* · asset `—`

**Out of library scope.** A portrait attached to a named commenter. Out of library scope, and generating one would put an invented face beside an invented name in a block that reads as real user comments. 05-social-snapshot's fence names avatars specifically as what a generated image must never sit beside. Supply real avatars or render the block without them.

---

