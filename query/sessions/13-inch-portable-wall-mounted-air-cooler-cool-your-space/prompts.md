# Image prompts — 13-Inch Portable Wall-Mounted Air Cooler (listicle)

Registry 2.0.0 · 14 types · channel advertorial · Stage 1 derived · adapter nano-banana level C · 2026-08-11

**Ten assets, every one routed to a real active type. No fallbacks, no empty image slots.**

## Asset manifest

Render candidates as `…--A.jpg` / `--B` / `--C`; the picked option is renamed to the canonical
name, which is what the page layout references. Ratio is a render PARAMETER, never prompt text.

| # | Asset | Slot | Type | Placement |
|---|---|---|---|---|
| 1 | `cooler-listicle-01-hero.jpg` | `hero-header` | `01-pain-scene` v1.2 | Full-bleed header directly above `hero.title`, before the byline block. |
| 2 | `cooler-listicle-02-editors-pick.jpg` | `reason-0-editors-pick` | `06-relief-hero` v1.7 | Inside the `reason.0` card (The Portable Wall Cooler — Editor's Pick), above `reason.0.body`. |
| 3 | `cooler-listicle-03-alt-window-ac.jpg` | `reason-1-window-ac` | `01-pain-scene` v1.2 | Inside the `reason.1` card, above `reason.1.body`. One of five images in the same repeating section — they must read as ONE editorial series. |
| 4 | `cooler-listicle-04-alt-portable-ac.jpg` | `reason-2-portable-ac` | `01-pain-scene` v1.2 | Inside the `reason.2` card, above `reason.2.body`. One of five images in the same repeating section — they must read as ONE editorial series. |
| 5 | `cooler-listicle-05-alt-floor-cooler.jpg` | `reason-3-floor-cooler` | `01-pain-scene` v1.2 | Inside the `reason.3` card, above `reason.3.body`. One of five images in the same repeating section — they must read as ONE editorial series. |
| 6 | `cooler-listicle-06-alt-desk-fan.jpg` | `reason-4-desk-fan` | `01-pain-scene` v1.2 | Inside the `reason.4` card, above `reason.4.body`. One of five images in the same repeating section — they must read as ONE editorial series. |
| 7 | `cooler-listicle-07-alt-ceiling-fan.jpg` | `reason-5-ceiling-fan` | `01-pain-scene` v1.2 | Inside the `reason.5` card, above `reason.5.body`. One of five images in the same repeating section — they must read as ONE editorial series. |
| 8 | `cooler-listicle-08-mechanism.jpg` | `compare-mechanism` | `03-mechanism-xray` v1.0 | Directly above the `compare` table, beside `compare.intro`. |
| 9 | `cooler-listicle-09-howto.jpg` | `howto-steps` | `03-use-sequence` v1.1 | Inside the `howto` section (#7), beside the three numbered steps. |
| 10 | `cooler-listicle-10-social-1.jpg … -3.jpg` | `social-viral` | `05-social-snapshot` v1.0 | A band ABOVE the `social.items` cards. NEVER inside a card — every card carries a name and a Verified Buyer badge. |
| — | (no image by definition) | `comments-thread` | — | see note below |
| — | (no image by definition) | `offer-atc` | — | see note below |

## Page-level notes

- INPUT: flunnel export, lpTypeId `listicle` (TPL-ADV07). The content contract's enum has no `listicle`, so this routes as `advertorial` — editorial byline (Dana Merrick), an Updated date and a pain-first intro are the advertorial signature.
- STAGE 1 IS DERIVED, not looked up (SPEC 7.2 as of 2026-08-11): candidates come from registry/index.yaml by channel legality, then attribute gates, then role affinity from step+job. On advertorial the legal pool is 10 types covering every step 1-6, which is why no slot in this run is empty and no fallback exists.
- WHAT CHANGED SINCE THE FIRST RUN OF THIS PAGE: thirteen table/frontmatter contradictions were found and fixed (commit 973addf). The earlier output routed 02-symptom-rail, 03-use-sequence and 06-relief-hero on advertorial while their own frontmatter forbade it. use-sequence and relief-hero were widened (their own text demanded it); symptom-rail was NOT, so the problem-agitation beat is now carried by the hero alone.
- THE FIVE ALTERNATIVE ENTRIES now have real images. 01-pain-scene in its object-only execution serves all five, reached by the runbook's widening ladder: rung 2 (adjacent step — a step-1 pain type carries an indicted object) plus rung 3 (repeating section). Ledger precedent: obs sha256:30c9568… and sha256:4e8f238…, both filed as pain-scene with 'no person as subject, only the indicted OBJECT'. When 02-cause-scene promotes (3/5 exemplars) these move to it and gain a tighter skeleton.
- PRODUCT: identical to the advertorial page and to eval/golden/fixture-002. operation=passive, visible_output=mist, mounting=fixed-installed, colorways=[white, grey], body_contact=false, symptom_visibility=visible, result_visibility=on-body, multi_step_usage=true. Reference sha256:d3ce1b73… (cooler.avif).
- COMPLIANCE, the sharp one: every social card on this page carries a name and a `Verified Buyer` badge. 05-social-snapshot's authenticity fence forbids a generated snapshot sitting next to a reviewer name, avatar, star row or verified label. Use these as SECTION imagery — a band above or between the cards — never inside a card. Real customer photos are the only thing that may sit inside those cards.
- UNVERIFIED CLAIMS — not rendered: the brief itself flags 13°C in 10 seconds, 300% efficiency, aerospace-grade refrigeration and 10dB(A) as claims other pages for the same product drop. No prompt visualises a temperature drop, a decibel figure or a percentage. Mist is rendered because it is real; a number is not an image argument.
- CROSS-SLOT: one-type-once holds, with the repeating-section exception used twice and named both times (the five alternatives; the snapshot set). Step-3 budget used 2 of 2 (xray + use-sequence). 04-proof-lockedframe is unused and available if a grouped proof frame is wanted instead of, or beside, the five entries.
- RATIO: passed as the generation parameter only, never written in the prompt (adapter Rule 4 — 6/6 renders ignored a written ratio). Prompts spend their words on composition instead: share of frame, offset side, layer footprints.
- TIE-BREAKERS: feedback/picks.jsonl is empty — no (type x role) cell reaches the 20-pick threshold, priors unused.

---

## `hero-header` — role: hero

**ASSET:** `cooler-listicle-01-hero.jpg` · **RENDER AT:** 16:9 (generation parameter)
**PLACEMENT:** Full-bleed header directly above `hero.title`, before the byline block.

### Option A — `01-pain-scene` v1.2 --candid · single-pass
*varies_on: baseline*
*axes: gaze=candid*

```text
Cinematic film still, frame full. Single frame, NO graphic overlays.

SUBJECT: man late 30s, creased grey t-shirt and loose half-apron, mid-action lifting a pot lid at the stove of a small apartment kitchen on a July evening, leaning back from the rising steam, chin tucked from the heat, one forearm raised to wipe his forehead. Unaware of camera, gaze down at the pan. Brow knotted, eyes narrowed, cheeks flushed and damp, lips parted. Weight unbalanced, not posed.

SYMPTOM EVIDENCE, physical fact: dark sweat patches at collar and underarms, sweat shining on temple and neck, a crumpled towel already damp over his shoulder, a cheap desk fan wedged on the counter with a ribbon fluttering weakly in its warm draft — already tried, changing nothing. Steam from two pots keeps the heat source in frame.

MOMENT: the ordinary act of cooking on a hot evening, not a demonstration.

ENVIRONMENT to the edges: small rented kitchen in a heatwave, window shut with low sun glaring through, cutting board mid-use, open spice jar, oven mitts, a calendar curling at the corner. Lived-in clutter, nothing tidied.

LIGHT: low-key. Hard low evening sun from behind right, hot and unflattering. Weak cool bounce from the hallway. Rim along damp temple and forearm. Deep shadow across half the frame.

GRADE: desaturated amber-grey, crushed blacks, fine grain, shallow depth of field, 35mm. NO red anywhere.

FORBIDDEN: no product, no overlays, arrows, badges, glows, insets or split panels.
Editorial photojournalism, natural, unstaged. No text, no logo, no watermark.
```

**Avoid:** Avoid: text, watermarks, logos, red glow, pain hotspots, graphic overlays, badges, split panels, any visible product, posed stock-photo look, studio lighting. Also: bright airy daylight, looking at camera.

**Render as:** `cooler-listicle-01-hero--A.jpg`

**Why:** Advertorial hero cell. The page's own intro is a pain opening ('Struggling in a hot kitchen? Portable units roar at 53dB(A)'), and --candid fits heat discomfort nobody chooses to be seen in. G1-exempt: no product, no reference needed.

**Notes:** Page-wide: 01-pain-split stays banned (never_with). This type also serves the five alternative entries in a different execution — see slot 03.

### Option B — `01-pain-scene` v1.2 --confront · single-pass
*varies_on: axis: gaze=confront*
*axes: gaze=confront*

```text
Cinematic film still, frame full. Single frame, NO graphic overlays.

SUBJECT: man late 30s in a wrinkled short-sleeve shirt at a desk in a small home office mid-afternoon, turned to camera, looking into the lens, holding the viewer's eye. He has pushed his laptop a hand's width away; one hand still rests on it, the other tugs his damp collar off his neck. Brow drawn, mouth pressed flat, faint sheen at the hairline — an afternoon that has stalled again. Frustration, not drama.

SYMPTOM EVIDENCE, physical fact: damp sheen on forehead and neck, collar and chest darkened with sweat, a desk fan aimed straight at him with a limp ribbon barely lifting — running and useless — a glass of water sweating a ring onto his notepad.

MOMENT: the ordinary act of pausing mid-task in a stuffy room.

ENVIRONMENT to the edges: cramped home office in a rented flat, blinds half-closed, window shut behind him, papers stacked beside the laptop, phone face-down, cable tangle at the desk edge. Real clutter, nothing tidied.

LIGHT: even ambient daylight through the blinds, bright, minimal shadow, flat and unflattering. No golden hour, no rim light.

GRADE: desaturated grey-green, fine grain, moderate depth of field, 35mm. NO red anywhere.

FORBIDDEN: no product, no overlays, arrows, badges, glows, insets or split panels.
Editorial photojournalism, natural, unstaged. No text, no logo, no watermark.
```

**Avoid:** Avoid: text, watermarks, logos, red glow, pain hotspots, graphic overlays, badges, split panels, any visible product, posed stock-photo look, studio lighting. Also: golden hour, warm flattering light, theatrical anger.

**Render as:** `cooler-listicle-01-hero--B.jpg`

**Why:** Same type, confront gaze — a listicle often wants the reader met eye-to-eye before the ranked list starts. The stalled home office is the page's second named pain.

**Notes:** Restraint rule: the flatter the face, the truer it reads.

### Option C — `01-pain-scene` v1.2 --candid · single-pass
*varies_on: execution: sleepless hot bedroom at night, female cast*
*axes: gaze=candid*

```text
Cinematic film still, frame full. Single frame, NO graphic overlays.

SUBJECT: woman early 30s in a loose sleep shirt sitting up on the edge of the bed in the middle of a hot night, feet on the floor, hair stuck to her neck, one hand lifting the hair off her nape, the other holding her collar away from her skin. Unaware of camera, gaze down and unfocused, lids half closed, damp strands at the temple, jaw slack.

SYMPTOM EVIDENCE, physical fact: duvet kicked into a heap at the foot of the bed, sheet creased and thrown back, a pedestal fan turned to face the bed — running all night, moving only warm air — a glass of water beaded with condensation, a faint damp outline on the sheet where she has been lying.

MOMENT: the ordinary act of giving up on sleep in a hot bedroom.

ENVIRONMENT to the edges: small city bedroom in high summer, deep night, window cracked onto a still street, curtains hanging dead still, phone charging on the nightstand, clothes over a chair. Real clutter, nothing tidied.

LIGHT: low-key. Sodium streetlight through the window gap from the left. Faint cold spill from a hallway door ajar. Rim along her shoulder. Deep shadow across most of the frame.

GRADE: desaturated blue-grey, crushed blacks, fine grain, shallow depth of field, 35mm. NO red anywhere.

FORBIDDEN: no product, no overlays, arrows, badges, glows, insets or split panels.
Editorial photojournalism, natural, unstaged. No text, no logo, no watermark.
```

**Avoid:** Avoid: text, watermarks, logos, red glow, pain hotspots, graphic overlays, badges, split panels, any visible product, posed stock-photo look, studio lighting. Also: bright airy lighting, looking at camera.

**Render as:** `cooler-listicle-01-hero--C.jpg`

**Why:** Same type and axes as A, night execution: the light-sleeper persona the brief names, echoed by the page's own 'sleeping mode' review.

**Notes:** If this cast wins, any later 06-relief-scene pair must be re-cast to this woman (requires_pair).


---

## `reason-0-editors-pick` — role: outcome

**ASSET:** `cooler-listicle-02-editors-pick.jpg` · **RENDER AT:** 5:3 (generation parameter)
**PLACEMENT:** Inside the `reason.0` card (The Portable Wall Cooler — Editor's Pick), above `reason.0.body`.

### Option A — `06-relief-hero` v1.7 · single-pass
*varies_on: baseline*
*axes: register=commercial, inset_mode=none*

```text
E-commerce lifestyle banner, frame full.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. Wall-mounted in every layer — the freestanding base never appears.

SCENE right 58%: woman early 30s in a light knit top, medium shot at chest height, leaning back in her desk chair with her eyes closed for a second, shoulders loose, hands resting in her lap off the keyboard, gaze away from the product. The reference cooler is mounted punch-free on the wall above and beside her desk, unobstructed.

OUTPUT primary: a fine dense stream of cool mist drifting down and outward from the outlet across the desk zone, backlit by hard window light behind it so the mist glows against the darker hallway beyond, filling a large part of the frame and readable at thumbnail size. Lens flare and blown highlights welcome.

SETTING to the edges: a small working home office — laptop, glass of iced water, a linen curtain lifting, a shelf of books, a mug, a plant on the sill, a cable tray under the desk. Blurred, never blank; no bare wall or floor bigger than the product.

Bright, warm, sharp, 4K. No text, no logo, no watermark.
```

**Avoid:** Avoid: text, watermarks, logos, pain cues, red glow, invented steam beyond the outlet, product differing between layers, blank wall or floor areas, badges, arrows.

**Render as:** `cooler-listicle-02-editors-pick--A.jpg`  ·  **Attach:** `cooler.avif`

**Why:** The Editor's Pick entry presents the product as the resolved state — the outcome role, not a comparison. G8 binds: mist is the primary subject on the backlight branch. POSE takes the passive branch (it works while she works). Advertorial legality gained in v1.7 (see its changelog).

**Notes:** Attach `cooler.avif` (sha256:d3ce1b73…) at render time. Zone B skipped: the mounted unit is legible at scene scale, and a product view repeating the same angle buys nothing.

### Option B — `06-relief-hero` v1.7 · single-pass
*varies_on: axis: inset_mode=detail*
*axes: register=commercial, inset_mode=detail*

```text
E-commerce lifestyle banner, frame full.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. Wall-mounted in every layer.

SCENE right 58%: woman early 30s in a light knit top, medium shot at chest height, leaning back in her desk chair, eyes closed, shoulders loose, hands in her lap, gaze away from the product. The reference cooler is mounted punch-free on the wall above and beside her desk, unobstructed.

OUTPUT primary: a fine dense stream of cool mist drifting down and outward from the outlet, backlit by hard window light so it glows against the darker hallway beyond, filling a large part of the frame.

SETTING to the edges: a small working home office — laptop, glass of iced water, linen curtain lifting, shelf of books, mug, plant on the sill, cable tray. Blurred, never blank; no bare wall or floor bigger than the product.

DETAIL INSET bottom-right over the scene: PERFECT CIRCLE, 40% of frame width, 3% in from the bottom and right edges, 6px white ring, drop shadow, clear of the woman and the mounted unit. Inside: a magnified view of the unit's touch control panel with its three wind-mode indicators, sharp and legible. Real captured interface composited in, never drawn. Linked by proximity — no arrow, no glow border. Circle 8% clear of every edge; too big, render it smaller — never let it run off.

Bright, warm, sharp, 4K. No text, no logo, no watermark.
```

**Avoid:** Avoid: a rectangular or square inset, gibberish digits, arrows, glow borders, text, watermarks, logos, pain cues, blank wall or floor areas.

**Render as:** `cooler-listicle-02-editors-pick--B.jpg`  ·  **Attach:** `cooler.avif`

**Why:** Varies on the inset_mode axis: the #1 entry sells 3 wind modes and a remote, and --detail is the slot for a control surface too small to read at scene scale.

**Notes:** Attach `cooler.avif` (sha256:d3ce1b73…) at render time. The panel is diegetic UI — composite a real capture, never let the model draw the indicators (G6 production law).

### Option C — `06-relief-hero` v1.7 · single-pass
*varies_on: execution: night bedroom, Soft Wind*
*axes: register=commercial, inset_mode=none*

```text
E-commerce lifestyle banner, night scene, frame full.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. Wall-mounted in every layer.

SCENE right 58%: woman late 20s asleep on her side in a small quiet bedroom, face soft and untroubled, duvet drawn to her shoulder and lying flat and undisturbed — deep still sleep, nothing about her engaging the product. The reference cooler is mounted punch-free on the wall above the bedside, unobstructed.

OUTPUT primary: a fine stream of cool mist drifting slowly down from the outlet, backlit by the soft spill of a streetlamp through the curtain gap so it reads as a faint glowing veil against the dark wall, filling a large part of the frame and readable at thumbnail size.

SETTING to the edges: glass of water and a face-down phone on the nightstand, a paperback, a chair with clothes over the back, a rug edge, curtains half drawn. Deep calm blue-grey grade with the mist as the brightest element. Never blank; no bare wall bigger than the product.

Calm, quiet, sharp, 4K. No text, no logo, no watermark.
```

**Avoid:** Avoid: text, watermarks, logos, pain cues, red glow, invented steam beyond the outlet, product differing between layers, blank wall or floor areas, badges, arrows. Also: harsh lighting.

**Render as:** `cooler-listicle-02-editors-pick--C.jpg`  ·  **Attach:** `cooler.avif`

**Why:** Same type and axes as A, night execution: the page's own review copy leads on the sleep mode ('so quiet I had to check if it was still on'), and darkness makes backlit mist read at its best under G8.

**Notes:** Attach `cooler.avif` (sha256:d3ce1b73…) at render time. Dark-scene grade is a deliberate deviation from the type's bright-airy default, backed by a ledger exemplar (night relief-hero, batch 2026-08-10-C).


---

## `reason-1-window-ac` — role: comparison

**ASSET:** `cooler-listicle-03-alt-window-ac.jpg` · **RENDER AT:** 5:3 (generation parameter)
**PLACEMENT:** Inside the `reason.1` card, above `reason.1.body`. One of five images in the same repeating section — they must read as ONE editorial series.

### Option A — `01-pain-scene` v1.2 --candid · single-pass
*varies_on: baseline*
*axes: gaze=candid*

```text
Documentary photograph, frame full. Single frame, NO graphic overlays, no signal colours.

SUBJECT, the indicted object: a boxy white window air conditioner wedged into the lower half of a sash window in a rented flat, the sash resting on its top, a foam infill strip stuffed into the gap at one side. Ordinary, intact, plausible.

SYMPTOM EVIDENCE, physical fact: four bracket screws biting into the painted window frame, the paint cracked and flaked around each one; the window's view mostly blocked; a power lead running down the wall to a socket.

MOMENT: an ordinary moment in the room, nothing arranged for the camera.

ENVIRONMENT to the edges: a small living room mid-summer, a curtain pushed permanently aside and hooked back, a bookshelf, a mug on the sill. Real lived-in clutter, nothing tidied.

LIGHT: natural window light only, low and directional, raking so the cracked paint around each screw throws a shadow. No fill, no styling.

GRADE: desaturated neutral, fine grain, deep blacks, believable 35mm optics.

FORBIDDEN: no product of ours, no overlays, arrows, badges, glows, insets or split panels.
Editorial documentary photography, natural, unstaged. No text, no logo, no watermark.
```

**Avoid:** Avoid: text, watermarks, logos, overlays, arrows, badges, red or signal colours, faces, a damaged or filthy unit, a comically ugly unit, studio lighting, saturated colours.

**Render as:** `cooler-listicle-03-alt-window-ac.jpg`

**Why:** Listicle entry: reason.1 Traditional Window AC Units. 01-pain-scene in its object-only execution — the ledger records this twice already (obs sha256:30c9568…, sha256:4e8f238…, both filed as pain-scene with 'no person as subject, only the indicted OBJECT'). Reached by runbook rung 2 (adjacent step) plus rung 3 (repeating section) after one-type-once spent 04-proof-lockedframe.

**Notes:** REPEATING SECTION: this slot yields FIVE assets, one per listicle entry, all 01-pain-scene. Cross-slot rule 2 permits the repeat because the instances differ on a named dimension — the indicted object. All five must share ONE register and grade or the block reads as five sources instead of one editorial series. FAIRNESS: the alternative must look like a real product someone genuinely bought. The page's copy dramatises them ('sounded like a jet engine'); the image must not.


---

## `reason-2-portable-ac` — role: comparison

**ASSET:** `cooler-listicle-04-alt-portable-ac.jpg` · **RENDER AT:** 5:3 (generation parameter)
**PLACEMENT:** Inside the `reason.2` card, above `reason.2.body`. One of five images in the same repeating section — they must read as ONE editorial series.

### Option A — `01-pain-scene` v1.2 --candid · single-pass
*varies_on: baseline*
*axes: gaze=candid*

```text
Documentary photograph, frame full. Single frame, NO graphic overlays, no signal colours.

SUBJECT, the indicted object: a generic white floor-standing portable air conditioner on the floor of a small home office, its wide corrugated exhaust hose rising in an awkward arc to a window propped open on a plastic vent panel, gaffer tape sealing one corner. Ordinary, intact, plausible.

SYMPTOM EVIDENCE, physical fact: the unit's footprint eating the walking space between desk and door; the desk chair pushed sideways to clear it; a bin nudged into the corner by the hose.

MOMENT: an ordinary moment in the room, nothing arranged for the camera.

ENVIRONMENT to the edges: a cramped home office, a laptop and papers, a cable tangle, a jacket over the chair back. Real lived-in clutter, nothing tidied.

LIGHT: natural window light only, flat and directional through the propped gap. No fill, no styling.

GRADE: desaturated neutral, fine grain, deep blacks, believable 35mm optics.

FORBIDDEN: no product of ours, no overlays, arrows, badges, glows, insets or split panels.
Editorial documentary photography, natural, unstaged. No text, no logo, no watermark.
```

**Avoid:** Avoid: text, watermarks, logos, overlays, arrows, badges, red or signal colours, faces, a damaged or filthy unit, a comically ugly unit, studio lighting, saturated colours.

**Render as:** `cooler-listicle-04-alt-portable-ac.jpg`

**Why:** Listicle entry: reason.2 Hose-Vented Portable AC Units. 01-pain-scene in its object-only execution — the ledger records this twice already (obs sha256:30c9568…, sha256:4e8f238…, both filed as pain-scene with 'no person as subject, only the indicted OBJECT'). Reached by runbook rung 2 (adjacent step) plus rung 3 (repeating section) after one-type-once spent 04-proof-lockedframe.

**Notes:** REPEATING SECTION: this slot yields FIVE assets, one per listicle entry, all 01-pain-scene. Cross-slot rule 2 permits the repeat because the instances differ on a named dimension — the indicted object. All five must share ONE register and grade or the block reads as five sources instead of one editorial series. FAIRNESS: the alternative must look like a real product someone genuinely bought. The page's copy dramatises them ('sounded like a jet engine'); the image must not.


---

## `reason-3-floor-cooler` — role: comparison

**ASSET:** `cooler-listicle-05-alt-floor-cooler.jpg` · **RENDER AT:** 5:3 (generation parameter)
**PLACEMENT:** Inside the `reason.3` card, above `reason.3.body`. One of five images in the same repeating section — they must read as ONE editorial series.

### Option A — `01-pain-scene` v1.2 --candid · single-pass
*varies_on: baseline*
*axes: gaze=candid*

```text
Documentary photograph, frame full. Single frame, NO graphic overlays, no signal colours.

SUBJECT, the indicted object: a tall grey floor-standing evaporative cooler standing in the middle of a narrow galley kitchen, its water tank visible at the base with the fill flap open. Ordinary, intact, plausible.

SYMPTOM EVIDENCE, physical fact: its power lead crossing the floor at ankle height between unit and socket; the gap left beside it too narrow to pass without turning sideways; a jug left beside it from the last refill.

MOMENT: an ordinary moment in the room, nothing arranged for the camera.

ENVIRONMENT to the edges: a narrow galley, counters both sides, a chopping board mid-use, a kettle, a bin the unit half blocks, a tea towel on the oven rail. Real lived-in clutter, nothing tidied.

LIGHT: natural window light from the galley's end, low and directional, the power lead casting a thin shadow across the floor. No fill, no styling.

GRADE: desaturated neutral, fine grain, deep blacks, believable 35mm optics.

FORBIDDEN: no product of ours, no overlays, arrows, badges, glows, insets or split panels.
Editorial documentary photography, natural, unstaged. No text, no logo, no watermark.
```

**Avoid:** Avoid: text, watermarks, logos, overlays, arrows, badges, red or signal colours, faces, a damaged or filthy unit, a comically ugly unit, studio lighting, saturated colours.

**Render as:** `cooler-listicle-05-alt-floor-cooler.jpg`

**Why:** Listicle entry: reason.3 Bulky Floor-Standing Coolers. 01-pain-scene in its object-only execution — the ledger records this twice already (obs sha256:30c9568…, sha256:4e8f238…, both filed as pain-scene with 'no person as subject, only the indicted OBJECT'). Reached by runbook rung 2 (adjacent step) plus rung 3 (repeating section) after one-type-once spent 04-proof-lockedframe.

**Notes:** REPEATING SECTION: this slot yields FIVE assets, one per listicle entry, all 01-pain-scene. Cross-slot rule 2 permits the repeat because the instances differ on a named dimension — the indicted object. All five must share ONE register and grade or the block reads as five sources instead of one editorial series. FAIRNESS: the alternative must look like a real product someone genuinely bought. The page's copy dramatises them ('sounded like a jet engine'); the image must not.


---

## `reason-4-desk-fan` — role: comparison

**ASSET:** `cooler-listicle-06-alt-desk-fan.jpg` · **RENDER AT:** 5:3 (generation parameter)
**PLACEMENT:** Inside the `reason.4` card, above `reason.4.body`. One of five images in the same repeating section — they must read as ONE editorial series.

### Option A — `01-pain-scene` v1.2 --candid · single-pass
*varies_on: baseline*
*axes: gaze=candid*

```text
Documentary photograph, frame full. Single frame, NO graphic overlays, no signal colours.

SUBJECT, the indicted object: a cheap white plastic desk fan running at close range on a home-office desk, its cage grille dusty between the bars. Ordinary, intact, plausible — a fan someone actually owns.

SYMPTOM EVIDENCE, physical fact: a short ribbon tied to the guard lifting only weakly in the draft; the papers directly in its path barely disturbed; a glass of water with condensation pooling on a notepad.

MOMENT: an ordinary moment in the room, nothing arranged for the camera.

ENVIRONMENT to the edges: a small home office in high summer, window shut, blinds half down, a laptop, a stack of papers weighted with a book, a cardigan discarded over the chair. Real lived-in clutter, nothing tidied.

LIGHT: flat ambient daylight through the blinds, hot and unhelpful. No fill, no styling.

GRADE: desaturated neutral, fine grain, deep blacks, believable 35mm optics.

FORBIDDEN: no product of ours, no overlays, arrows, badges, glows, insets or split panels.
Editorial documentary photography, natural, unstaged. No text, no logo, no watermark.
```

**Avoid:** Avoid: text, watermarks, logos, overlays, arrows, badges, red or signal colours, faces, a damaged or filthy unit, a comically ugly unit, studio lighting, saturated colours.

**Render as:** `cooler-listicle-06-alt-desk-fan.jpg`

**Why:** Listicle entry: reason.4 Standard Plastic Desk Fans. 01-pain-scene in its object-only execution — the ledger records this twice already (obs sha256:30c9568…, sha256:4e8f238…, both filed as pain-scene with 'no person as subject, only the indicted OBJECT'). Reached by runbook rung 2 (adjacent step) plus rung 3 (repeating section) after one-type-once spent 04-proof-lockedframe.

**Notes:** REPEATING SECTION: this slot yields FIVE assets, one per listicle entry, all 01-pain-scene. Cross-slot rule 2 permits the repeat because the instances differ on a named dimension — the indicted object. All five must share ONE register and grade or the block reads as five sources instead of one editorial series. FAIRNESS: the alternative must look like a real product someone genuinely bought. The page's copy dramatises them ('sounded like a jet engine'); the image must not.


---

## `reason-5-ceiling-fan` — role: comparison

**ASSET:** `cooler-listicle-07-alt-ceiling-fan.jpg` · **RENDER AT:** 5:3 (generation parameter)
**PLACEMENT:** Inside the `reason.5` card, above `reason.5.body`. One of five images in the same repeating section — they must read as ONE editorial series.

### Option A — `01-pain-scene` v1.2 --candid · single-pass
*varies_on: baseline*
*axes: gaze=candid*

```text
Documentary photograph, frame full. Single frame, NO graphic overlays, no signal colours.

SUBJECT, the indicted object: a white ceiling fan mounted high in a bedroom, seen from low in the room so it sits small and far away against the ceiling, its blades still. Ordinary, intact, plausible.

SYMPTOM EVIDENCE, physical fact: the mounting plate ringed by a repainted patch where the old fitting was cut in, a capped junction wire just visible at the plate's edge; the distance between the fan at the ceiling and the bed below is the point of the frame.

MOMENT: an ordinary moment in the room, nothing arranged for the camera.

ENVIRONMENT to the edges: a bedroom in high summer, bed with the duvet kicked back, a window cracked onto a still street, a chair with clothes over it, a glass of water on the nightstand. Real lived-in clutter, nothing tidied.

LIGHT: warm bedside lamp and a sodium streetlight through the window gap, low and directional, the ceiling in shadow. No fill, no styling.

GRADE: desaturated neutral, fine grain, deep blacks, believable 35mm optics.

FORBIDDEN: no product of ours, no overlays, arrows, badges, glows, insets or split panels.
Editorial documentary photography, natural, unstaged. No text, no logo, no watermark.
```

**Avoid:** Avoid: text, watermarks, logos, overlays, arrows, badges, red or signal colours, faces, a damaged or filthy unit, a comically ugly unit, studio lighting, saturated colours.

**Render as:** `cooler-listicle-07-alt-ceiling-fan.jpg`

**Why:** Listicle entry: reason.5 Built-in Ceiling Fans. 01-pain-scene in its object-only execution — the ledger records this twice already (obs sha256:30c9568…, sha256:4e8f238…, both filed as pain-scene with 'no person as subject, only the indicted OBJECT'). Reached by runbook rung 2 (adjacent step) plus rung 3 (repeating section) after one-type-once spent 04-proof-lockedframe.

**Notes:** REPEATING SECTION: this slot yields FIVE assets, one per listicle entry, all 01-pain-scene. Cross-slot rule 2 permits the repeat because the instances differ on a named dimension — the indicted object. All five must share ONE register and grade or the block reads as five sources instead of one editorial series. FAIRNESS: the alternative must look like a real product someone genuinely bought. The page's copy dramatises them ('sounded like a jet engine'); the image must not.


---

## `compare-mechanism` — role: mechanism

**ASSET:** `cooler-listicle-08-mechanism.jpg` · **RENDER AT:** 16:9 (generation parameter)
**PLACEMENT:** Directly above the `compare` table, beside `compare.intro`.

### Option A — `03-mechanism-xray` v1.0 · single-pass
*varies_on: baseline*

```text
3D technical see-through render. NOT photography. Dark engineering background.

REFERENCE: attached photo is the wall-mounted personal air cooler. The outer shell becomes translucent, but its silhouette, proportions and every visible external part — top shell, louvered front grille, touch controls — match the reference exactly. Do not redesign or add features.

CANVAS: deep navy engineering canvas, faint copper and cyan circuit traces at very low contrast, two corner blueprint micro-diagrams of a fan-wheel module. Motifs stay dim.

GHOST SHELL: the cooler in its wall-mounted horizontal orientation, shell translucent and glass-like, seen from a slight three-quarter front angle, filling about 70% of frame width.

INTERNALS, solid and detailed, each at its true location: the magnetic levitation motor ring at the drive end with its rotor visibly FLOATING in a narrow gap — no contact, no shaft friction; the long cross-flow wind wheel cylinder running the body's length; the dark porous ice carbon grille behind the front louvers; the built-in water tank low in the housing with its water level visible. Fine cyan wiring linking motor and control board.

VISIBLE MECHANISM: the cooling path shown ACTIVE — wind wheel mid-spin, a fine cool mist streaming out through the front louvers as a bright particle flow drifting down and outward, the brightest element in the frame.

HONESTY CONSTRAINT: render ONLY these component types — maglev motor, cross-flow wind wheel, ice carbon grille, water tank, control board. No invented modules, no exaggerated part counts.

PALETTE LOCK: deep navy and steel grey; cyan marks the working mechanism and the floating rotor gap; copper traces stay decorative and dim.

Premium technical product visualization, sharp, high detail, 4K. No text, no numbers, no spec labels, no logo, no watermark.
```

**Avoid:** Avoid: text, numbers, spec labels, watermarks, logos, photographic background, people, hands, opaque shell, internals outside the product, invented components, exploded parts, bright white background, cartoon style.

**Render as:** `cooler-listicle-08-mechanism--A.jpg`  ·  **Attach:** `cooler.avif`

**Why:** The compare section's intro carries the mechanism claims — maglev motor, water cooling, 3 wind modes. body_contact=false drops ghostbody, so xray is the mechanism answer. The floating rotor makes the zero-contact claim visual instead of verbal.

**Notes:** Attach `cooler.avif` (sha256:d3ce1b73…) at render time. Step-3 budget: with use-sequence at howto, the page then carries its maximum of two step-3 answers.

### Option C — `03-mechanism-xray` v1.0 · single-pass
*varies_on: execution: frontal, one continuous air-path ribbon*

```text
3D technical see-through render. NOT photography. Dark engineering background.

REFERENCE: attached photo is the wall-mounted personal air cooler. The outer shell becomes translucent, but its silhouette, proportions and every visible external part match the reference exactly. Do not redesign or add features.

CANVAS: deep navy engineering canvas, faint copper and cyan circuit traces at very low contrast, two corner blueprint micro-diagrams of an evaporative media stage. Motifs stay dim.

GHOST SHELL: the cooler straight-on in its wall-mounted orientation, shell translucent and glass-like, filling about 75% of frame width.

INTERNALS, solid and detailed, each at its true location: the top air intake; the spiral wind wheel and cross-flow wind wheel in line; the dark porous ice carbon grille just behind the louvers; the water tank low in the housing with its water level visible; the magnetic levitation motor ring at the drive end.

VISIBLE MECHANISM: the full air path shown ACTIVE as ONE smooth flow ribbon — warm air drawn in at the top intake, threading through the spinning wind wheel, passing the water-fed ice carbon grille where it cools, and leaving the front louvers as a fine bright mist stream, the brightest element in the frame. The ribbon enters warm-neutral and exits cool cyan.

HONESTY CONSTRAINT: render ONLY these component types — intake, wind wheels, ice carbon grille, water tank, maglev motor. No invented modules.

PALETTE LOCK: deep navy and steel grey; cyan marks the correct air path; copper traces stay decorative and dim.

Premium technical product visualization, sharp, high detail, 4K. No text, no numbers, no spec labels, no logo, no watermark.
```

**Avoid:** Avoid: text, numbers, spec labels, watermarks, logos, photographic background, people, hands, opaque shell, internals outside the product, invented components, exploded parts, bright white background, cartoon style.

**Render as:** `cooler-listicle-08-mechanism--C.jpg`  ·  **Attach:** `cooler.avif`

**Why:** Same type, the story told as one continuous ribbon — warm in, through the wet grille, cool mist out. This enter-transform-exit grammar is what the type's own rendered-pass example proved on the shower filter.

**Notes:** Attach `cooler.avif` (sha256:d3ce1b73…) at render time.


---

## `howto-steps` — role: how-to-use

**ASSET:** `cooler-listicle-09-howto.jpg` · **RENDER AT:** 4:5 (generation parameter)
**PLACEMENT:** Inside the `howto` section (#7), beside the three numbered steps.

### Option A — `03-use-sequence` v1.1 · single-pass
*varies_on: baseline*
*axes: camera_lock=handheld*

```text
Warm lifestyle photograph, three horizontal panels stacked vertically, thin white gutters, no outer border, no numbers, no arrows, no text.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color, identical in every panel.

CONTINUITY LOCK: the same pair of hands in every panel — same skin tone, nails, wrists, pushed-up sleeves. The same pale painted wall beside the same light-wood desk in every panel. Same warm neutral palette, same soft daylight from the left. Camera distance and framing may shift naturally.

SEQUENCE: one action per panel, never two, readable from the actions alone. The cooler or its plate sits near the centre of every panel.

PANEL 1, MOUNT OR SET: both hands pressing the slim adhesive backing plate flat against the painted wall at chest height, palms flat, the plate level and fully stuck. No drill, no screws, no tools anywhere in frame.

PANEL 2, ADD WATER: one hand pouring cold water from a small measuring cup into the open tank port of the mounted cooler, the water surface visible at the port, the other hand steadying the cup.

PANEL 3, SELECT MODE: a fingertip pressing the mode control on the mounted unit, the first fine stream of cool mist emerging from the outlet, backlit by the window so the mist is clearly visible; the other hand relaxed and open in the cool air below. Warmer light than the previous panels.

ENVIRONMENT: an ordinary small home office, soft daylight, a mug on the desk, a folded throw over the chair. Same location across all three panels.

Warm lifestyle product photography, natural, unstyled, sharp, 4K. No text, no numbers, no logo, no watermark, no arrows, no step markers.
```

**Avoid:** Avoid: text, numbers, watermarks, logos, arrows, step badges, deformed hands, extra fingers, different hands between panels, two actions in one panel, tools, instruction-manual diagram look, cold clinical lighting.

**Render as:** `cooler-listicle-09-howto--A.jpg`  ·  **Attach:** `cooler.avif`

**Why:** The page gives exactly three numbered steps — Mount or Set, Add Water, Select Mode — and this type is three panels read by action logic with no numerals. A one-to-one fit; multi_step_usage=true keeps it. Advertorial legality gained in v1.1 (see its changelog).

**Notes:** Attach `cooler.avif` (sha256:d3ce1b73…) at render time. Close-range hands are the library's highest-risk zone; expect retries. If panel 3 crowds result and centred product, keep the mist and let the product sit off-centre.

### Option C — `03-use-sequence` v1.1 · single-pass
*varies_on: execution: kitchen wall, cook's hands*
*axes: camera_lock=handheld*

```text
Warm lifestyle photograph, three horizontal panels stacked vertically, thin white gutters, no outer border, no numbers, no arrows, no text.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color, identical in every panel.

CONTINUITY LOCK: the same pair of hands in every panel — same skin tone, nails, wrists, rolled linen sleeves. The same white kitchen tile and the same counter edge in every panel. Same warm neutral palette, same soft daylight from the right. Camera distance may vary naturally.

SEQUENCE: one action per panel, never two, readable from the actions alone. The cooler sits near the centre of every panel, mounted punch-free on the kitchen wall above the counter in all three.

PANEL 1, MOUNT OR SET: both hands pressing the adhesive backing plate flat onto the tiled wall above the counter's end, palms flat, plate level. No drill, no screws, no tools in frame.

PANEL 2, ADD WATER: one hand pouring cold water from a jug into the open tank port of the mounted unit, water surface visible at the port, the other steadying the jug.

PANEL 3, SELECT MODE: a fingertip pressing the mode control, the first fine stream of cool mist drifting out over the prep zone, backlit against the tile; a chopping board with herbs resting calm below. Warmer light than the previous panels.

ENVIRONMENT: an ordinary home kitchen, soft daylight, a kettle on the counter, a linen towel on a hook. Same location across all three panels.

Warm lifestyle product photography, natural, unstyled, sharp, 4K. No text, no numbers, no logo, no watermark, no arrows, no step markers.
```

**Avoid:** Avoid: text, numbers, watermarks, logos, arrows, step badges, deformed hands, extra fingers, different hands between panels, two actions in one panel, tools, instruction-manual diagram look, cold clinical lighting.

**Render as:** `cooler-listicle-09-howto--C.jpg`  ·  **Attach:** `cooler.avif`

**Why:** Same type and steps, staged in the kitchen the page opens on. Two legal options for this slot: the type declares one axis value, so the variation is execution.

**Notes:** Attach `cooler.avif` (sha256:d3ce1b73…) at render time.


---

## `social-viral` — role: social-proof

**ASSET:** `cooler-listicle-10-social-1.jpg … -3.jpg` · **RENDER AT:** 5:3 (generation parameter)
**PLACEMENT:** A band ABOVE the `social.items` cards. NEVER inside a card — every card carries a name and a Verified Buyer badge.

### Option A — `05-social-snapshot` v1.0 · single-pass
*varies_on: baseline*
*axes: register=ugc*

```text
Real customer's phone photo. One frame, no layout, no layers.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. It may be cropped or angled the way a casual one-handed phone photo crops.

CONTENT MODE, in-use: the cooler mounted on the tiled wall above a kitchen counter, running, a faint drift of cool air visible at the louvers, photographed from below at counter height the way someone shows a thing off quickly.

ANCHOR: an open bag of flour and a scale on the counter beneath it — the one incidental owner object.

SCENE: an ordinary kitchen photographed as found — crumbs on the counter, a splash mark on the tile, a tea towel bunched by the sink, another appliance blurred at the frame edge. Ambient overhead kitchen light only, never studio light.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, exposure honest to the room. No negative space discipline, no rule of thirds, no styling.

Honest phone photography, unedited look, natural, slightly imperfect. No text overlays, no logo, no watermark, no badges, no borders.
```

**Avoid:** Avoid: studio lighting, softbox reflections, seamless background, negative space, colour grading, professional composition, styled props, badges, borders, star ratings, reviewer names, avatars, text overlays, product-render look, magazine polish.

**Render as:** `cooler-listicle-10-social-1.jpg`  ·  **Attach:** `cooler.avif`

**Why:** The section is six customer comments from six different rooms — exactly this type's use case. Baseline takes the in-use mode in the page's lead scene (Clara's kitchen: 'brutally hot… now I can actually bake').

**Notes:** Attach `cooler.avif` (sha256:d3ce1b73…) at render time. SET DIVERSITY LAW: this slot yields a SET. Every additional snapshot must differ completely — room class, surface, light temperature, camera distance, content mode. Generate as independent prompts, never a batch with shared seeds or scene text.

### Option B — `05-social-snapshot` v1.0 · single-pass
*varies_on: execution: at-rest mode, rented apartment wall*
*axes: register=ugc*

```text
Real customer's phone photo. One frame, no layout, no layers.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. It may be cropped or angled the way a casual phone photo crops.

CONTENT MODE, at-rest: the cooler simply mounted on a rented flat's painted wall where it now lives, switched off, the adhesive plate edge just visible behind it, photographed straight on from a step back.

ANCHOR: the remote control lying on the windowsill below it — the one incidental owner object.

SCENE: an ordinary rented living room photographed as found — a slightly scuffed skirting board, a radiator, a plug socket with a phone charger in it, the corner of a sofa at the frame edge. Flat daylight through a net curtain, never studio light.

CAMERA TRUTH: slightly off-centre, a little flat, focus adequate, exposure honest to the room, no styling.

Honest phone photography, unedited look, natural, slightly imperfect. No text overlays, no logo, no watermark, no badges, no borders.
```

**Avoid:** Avoid: studio lighting, softbox reflections, seamless background, negative space, colour grading, professional composition, styled props, badges, borders, star ratings, reviewer names, avatars, text overlays, product-render look, magazine polish.

**Render as:** `cooler-listicle-10-social-2.jpg`  ·  **Attach:** `cooler.avif`

**Why:** Second image of the set on a different content mode and room class — the renter comment ('no drilling, adhesive strip holding strong').

**Notes:** Attach `cooler.avif` (sha256:d3ce1b73…) at render time. Shares nothing with option A: different room, light, distance, mode. That is the law, not a preference.

### Option C — `05-social-snapshot` v1.0 · single-pass
*varies_on: execution: in-use, camper van at night*
*axes: register=ugc*

```text
Real customer's phone photo. One frame, no layout, no layers.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. It may be cropped or angled the way a casual phone photo crops.

CONTENT MODE, in-use: the cooler mounted on the plywood wall of a camper van interior, running, photographed at night from the bunk with the phone held low.

ANCHOR: a water bottle wedged beside it on the ledge — the one incidental owner object.

SCENE: a real camper interior photographed as found — a rumpled sleeping bag, a cabinet latch, a strip of warm LED light along the ceiling, a hoodie hanging on a hook. Dim mixed warm light only, underexposed and noisy, never studio light.

CAMERA TRUTH: framing tilted, a little too close, focus adequate, visible noise, exposure honest to the dark. No styling of any kind.

Honest phone photography, unedited look, natural, slightly imperfect. No text overlays, no logo, no watermark, no badges, no borders.
```

**Avoid:** Avoid: studio lighting, softbox reflections, seamless background, negative space, colour grading, professional composition, styled props, badges, borders, star ratings, reviewer names, avatars, text overlays, product-render look, magazine polish. Also: clean bright exposure.

**Render as:** `cooler-listicle-10-social-3.jpg`  ·  **Attach:** `cooler.avif`

**Why:** Third scene class for the set — the camper-van comment. Underexposure and noise are credentials in this register, not faults.

**Notes:** Attach `cooler.avif` (sha256:d3ce1b73…) at render time. Quality floor: authenticity tolerates softness, never illegibility — the product must stay identifiable at thumbnail size.


---

## `comments-thread` — role: social-proof

**NO IMAGE BY DEFINITION.** A 48-comment discussion thread is page furniture — text, avatars and timestamps rendered by the template. Not an image slot, so the never-empty rule does not apply. The ledger drew this same boundary twice before (a pricing panel, a hero banner).


---

## `offer-atc` — role: cta

**NO IMAGE BY DEFINITION.** The cta cell is empty by design in mapping/slot-rules.md — a standard product shot, outside library scope. Not an image slot in the library's sense.
