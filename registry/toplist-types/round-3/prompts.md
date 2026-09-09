# Toplist round 3 — built from the owner's feedback, to test BEFORE any type file moves

> **RENDERED 2026-09-09 — 6 of 7, and the results are at the bottom of this file.**
> Prompts 1, 2, 3, 4, 6 and 7 came back. **Two `pass` and four `partial`**, against round
> 2's nought out of six, every verdict self-assigned under ADR-011 on a render that was
> opened and looked at. Logged in `eval/render-tests.jsonl`.
>
> **Prompt 5 — `lede-winner`, smart video doorbell, the `band` mark — was not rendered.**
> `MARKS`'s only zero-observation form still has none, and `lede-winner` is now the only
> active toplist type whose round-3 clause changes are untested.
>
> **Prompt 3 landed, which was the round's whole point.** Five attachments, five distinct
> real units, one generation call — the last untested half of ADR-076's route.

**Owner instruction, 2026-09-09:** per-type feedback with named example frames, plus
*"những chỗ có thể mở prompt, chỉ để đưa gợi ý mang nghĩa inform cho model biết là prompt
của tôi có các yếu tố a,b,c,… model sẽ tự lắp ghép, styling phù hợp"*, and then
*"tạo prompt round 3 theo chỉnh sửa để tôi test trước khi viết vào type"*.

**No type file is changed by this round.** Several prompts below deliberately contradict a
live clause, because that clause is what the feedback moves. Each one says so in its own
`NOTE` line. Nothing here is evidence for anything until it renders.

## The structural change: two registers instead of one

Round 2 was written as one long imperative. Graded, it split cleanly in two:

| kind of instruction | round 2 result |
|---|---|
| **geometry** — *"so large that the word runs off BOTH side edges"* | delivered exactly, 1 of 1 |
| **taste** — *"an upright rectangle"*, *"dial turned away"*, *"one faint contact shadow"*, *"no golden hour"* | **ignored, 4 of 4** |

So the rule this round tests is sharper than *open the prompt up*: **prescribe geometry and
refusals, inform on taste.** Every prompt below carries

- **`ELEMENTS`** — informative. What is in the picture. The model assembles and styles it.
- **`CONSTRAINTS`** — binding. Refusals and frame geometry, which cannot be delegated to
  the model's taste, because a refusal decided by taste is not a refusal.

Round 2 proved why the second block has to exist on its own: prompt 6 asked for a title
*"margin to margin"* and for *"nothing within a tenth of the width of any edge"* in the same
breath, and the model obeyed the first. Measured, that title came within 4.2% of the edge.
`CONSTRAINTS` is also where adapter Rule 6.3 is honoured — anything already asserted
positively in `ELEMENTS` is dropped rather than repeated as a negative.

## What is deliberately NOT in this round

- **No third-party award mark**, anywhere. Four of the eight `lede-winner` frames the owner
  named on 2026-09-09 carry one, which makes the decision unavoidable — and it is still the
  owner's. Every mark below is the page's own verdict.
- **No display type cropped by the frame edge.** Round 2 delivered it perfectly and in doing
  so exposed a conflict: G10's scope admits no exemptions and `lede-winner` declares
  `exempt_from: [G7]` only. Until that is settled the round does not lean on it again.
- **`lede-winner` keeps a gradient ground**, though the feedback newly permits a contextual
  one. The badge `band` form and the added graphics are already two new variables in that
  prompt; a third would make a single render unreadable as evidence. Contextual is round 4.
- **`lede-collage` carries no badge.** Round 2 answered that question — a mark over a unit
  occludes it — and this round changes the layout instead.

## Attachments

| # | type | v | attachments | text |
|---|---|---|---|---|
| 1 | `lede-pain` | 0.3 | **none** — the product is absent by definition | no |
| 2 | `lede-inuse` | 0.3 | 1 | no |
| 3 | `lede-lineup` | 0.4 | **5, one per unit** | no |
| 4 | `lede-testing` | 0.4 | 1 | no |
| 5 | `lede-winner` | 0.6 | 1 | **yes** — `band` mark |
| 6 | `lede-collage` | 0.6 | **5, one per unit** | **yes** — title only |
| 7 | `lede-authority` | 0.2 | 1 | no |

One prompt, one generation call, nothing assembled afterwards (ADR-021). The attachment
count is per product in frame (ADR-076); where your own app takes fewer, these ship in full
and render elsewhere. **Seven new products — none repeats round 1 or round 2.**

---

## 1 — `lede-pain` · knee, stair-climbing category · no attachment, no words

NOTE: round 2's ground came back at value 0.25 and read as dusk. The prompt asked for
"mid-toned"; this one asks for ordinary daylight and makes the exposure a constraint. Its
closing safe-area line is also gone — G10 binds text and product, and a candid photograph
cannot keep its own subject a tenth of the frame from the edge.

```
TYPE: lede-pain v0.3 — ROUND 3
REGISTER: editorial photojournalism, unstaged, single frame.

ELEMENTS — assemble and style these as the picture needs.
[SUBJECT]   a woman in her late fifties stopped partway up a domestic staircase, one hand
            gripping the rail, the other pressed flat above her knee.
[EVIDENCE]  the climb has stalled — the leading foot is on the next tread, the trailing
            foot has not followed, the weight has gone into the rail.
[COST]      two full shopping bags set down on the tread below her, still to be carried up.
[PLACE]     the stairs and hallway of an ordinary home, daylight from a landing window.
[GAZE]      candid, unaware of the lens, looking down at the step.
[GRADE]     an ordinary photograph in ordinary light — normally exposed, detail held in
            the shadows, no filter, no colour cast, no styling.
[GROUND]    the hall behind her, thrown out of focus, plainly lit, the light falling off
            naturally across the frame.

CONSTRAINTS — binding.
· Normal daytime exposure. Not dusk, not a darkened room, not a night interior.
· No product of any kind in frame, and none implied.
· No word, number, logo or badge anywhere in the picture.
```

---

## 2 — `lede-inuse` · cordless neck and shoulder heat massager · one photo, no words

NOTE: round 2 landed every slot and still argued the wrong thing — the sleeper read as
overheated, so the frame stated the pain this type is the relief half of. The fix is not a
new slot; it is that RELEASE is now stated as a fact of the body and repeated as a
constraint on what the picture may say. Owner's added note: bright colour tone.

```
TYPE: lede-inuse v0.3 — ROUND 3
REGISTER: candid documentary photograph, single frame.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cordless neck and
            shoulder heat massager. Preserve shape, proportions, material, finish, colour.

ELEMENTS — assemble and style these as the picture needs.
[SUBJECT]   a man in his forties sitting back on a sofa with the massager over his
            shoulders, mid-exhale, shoulders visibly dropped, hands loose in his lap.
[RELEASE]   the body has already let go — jaw unclenched, head resting back, no bracing
            anywhere in the posture. This is the moment AFTER, not during.
[PRODUCT]   worn and working, part of the moment rather than presented to the lens.
[ENVIRONMENT] his own living room in the middle of the day, a book face down beside him.
[GAZE]      none; his eyes are closed.
[LIGHT]     bright even daylight through a large window, soft shadows.
[GRADE]     a light, warm, natural palette. Honest, not glossy.
[GROUND]    a real living-room wall, out of focus, light and quiet in colour.

CONSTRAINTS — binding.
· The picture states EASE. Nothing in it may read as strain, heat, discomfort or effort.
· One person only.
· No word, number, display reading, logo or badge in frame.
```

---

## 3 — `lede-lineup` · five stainless insulated travel mugs · FIVE photos, no words

NOTE: the five-attachment route is still untested — round 2's prompt 3 was never rendered,
and prompt 6 answered it only at four. This also takes the OTHER branch of the type's
bimodal ground: the units are pale and metallic, so the clause calls for a strongly
coloured sweep rather than a near-white one. Arrangement is a 45° grouped comparison
rather than round 2's front-on row, per the owner's arrangement vocabulary.

```
TYPE: lede-lineup v0.4 — ROUND 3
REGISTER: editorial product photograph, one frame, no words in it.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed word on it. Five different makers, and their real
            brand marks stay as the references show them.

ELEMENTS — assemble and style these as the picture needs.
[FIELD]     the five insulated travel mugs together on one surface, lids on, each turned
            so its body and its lid read.
[ARRANGEMENT] a grouped comparison seen from a 45° hero angle rather than a flat row —
            varied depth, the five reading as one cluster, every unit wholly visible.
[SURFACE]   one clean studio surface, shared by all five, taking real contact shadows.
[LIGHT]     one broad soft key for the whole group, bright, with detail held in the metal.
[GROUND]    a smooth studio sweep in a single strongly saturated colour — these units are
            pale and metallic, and the sweep is what separates them from the frame. No
            visible join between the sweep and the surface.

CONSTRAINTS — binding.
· No unit favoured: same distance from the lens, same light, none centred, none forward.
· No rank number, badge, podium, riser, person, word or price in frame.
· Every unit and every printed mark stays at least 8% of the frame width from any edge.
```

---

## 4 — `lede-testing` · portable power station · one photo, no legible reading

NOTE: this prompt contradicts the live 0.4 file on two clauses, and both are the owner's
correction. The file bans a lab coat and calls for a mid-toned, unevenly lit workshop; the
five frames the owner named measure value 0.80 against the clause's 0.65 and saturation
0.07 against 0.13 — brighter AND less coloured — and one of them is a technician in a white
coat. Round 2's other lesson is applied too: the no-reading outcome is now a constraint on
what is LEGIBLE, not on which way an instrument faces, because the dial was told to face
away and faced the lens.

```
TYPE: lede-testing v0.4 — ROUND 3
REGISTER: editorial documentary photograph, one frame, no words in it.

[PRODUCT REFERENCE] the attached photo is the exact reference for the portable power
            station. Preserve shape, proportions, material, finish and colour exactly.

ELEMENTS — assemble and style these as the picture needs.
[UNIT]      the power station on a test bench, cabled into the apparatus.
[INSTRUMENT] a rack-mounted electronic load bank wired to its output, switched on and
            working, cables dressed and clipped.
[TESTER]    a technician in a white lab coat, hands on the apparatus and doing the work
            rather than presenting the product. Face turned away or out of frame.
[SURFACE]   a clean laboratory bench — cable looms, a torque driver, the tools of the
            measurement and nothing decorative, nothing untidy.
[PLACE]     a real working professional test laboratory: bright, orderly, equipment racks
            and a second bench legible behind.
[LIGHT]     even bright laboratory lighting, cool and neutral, no falloff.
[GROUND]    the laboratory itself, sharp enough to read as real and almost colourless —
            the colour in this picture belongs to the product and the apparatus.

CONSTRAINTS — binding.
· No figure, digit, scale, readout or chart is legible anywhere in frame — on any
  instrument, screen, dial or label. Instruments may be lit; nothing they show is readable.
· No word, price or logo baked into the picture.
· No second product class and no competitor's unit.
```

---

## 5 — `lede-winner` · smart video doorbell · one photo, `band` mark, added graphics

NOTE: `band` is the owner's own named form and the only one in `MARKS` with **zero**
observations behind it; this prompt exists to give it one. The added graphic elements are
the owner's second ask. Ground stays a gradient on purpose — see *What is deliberately NOT
in this round*. The mark is the page's own verdict; no third-party mark appears.

```
TYPE: lede-winner v0.6 — ROUND 3
REGISTER: designed promotional composition, one frame.

[PRODUCT REFERENCE] the attached photo is the exact reference for the smart video
            doorbell. Preserve shape, proportions, material, finish and colour exactly.

ELEMENTS — assemble and style these as the picture needs.
[SUBJECT]   the doorbell cut out and floating, hero-lit, held large in the frame, with no
            surface under it and no shadow implying one.
[GROUND]    a designed field, light and strongly coloured, built as a two-hue gradient.
[GRAPHICS]  design elements in the same register as the ground — concentric arcs radiating
            from behind the unit, a dotted outline echoing its silhouette, a soft halo.
            They sit behind and around the product and never across it.
[MARK]      form `band`: a horizontal banner crossing the frame behind the product,
            carrying BEST OVERALL in large capitals with 2026 smaller beneath. Give the
            band an interior — a rule inset from its top and bottom edge, and a second
            tone within its fill.
[COLOUR]    the band and the graphics take a colour that neither the doorbell nor the
            gradient carries, so the mark clears both.

CONSTRAINTS — binding.
· Every letter on the band is set in full inside the frame and stays at least 8% of the
  frame width from the left and right edges.
· Leave the lower right corner of the frame clear of the product, the band and the graphics.
· No score, star row, rating, review count, certification seal, press logo or third-party
  award mark, and no invented placing.
· No scene, no room, no surface under the product, no person.
```

---

## 6 — `lede-collage` · five desk lamps · FIVE photos, colour-cell grid, halftone

NOTE: contradicts the live 0.6 file, which describes one designed ground and a single
reading row. The owner's five named collage examples are grids and blocks of colour — and
three of the five are currently filed under the proposed `lede-mosaic`, which is why the
layout is the variable here. Five products, per the owner's note that a top list normally
compares five. A print texture is asked for, which is the owner's third ask.

```
TYPE: lede-collage v0.6 — ROUND 3
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish
            and colour. Five different makers, real brand marks as the references show them.

ELEMENTS — assemble and style these as the picture needs.
[LAYOUT]    the frame divided into rectangular cells of unequal size, each cell a flat
            block of its own colour, tiled edge to edge with no gaps and no gutters.
[CUT-OUTS]  the five desk lamps, each cleanly cut out and standing in its own cell, scaled
            to fill that cell comfortably. One lamp per cell.
[PALETTE]   a bright, cheerful, high-saturation set of colours across the cells, chosen so
            that every lamp separates from the block it stands on.
[TEXTURE]   a fine halftone dot screen over the coloured blocks, reading as print texture.
            The cut-out lamps themselves stay clean.
[TITLE]     one cell given to type instead of a lamp: THE BEST FIVE / DESK LAMPS, two
            lines, set large and left-aligned within that cell.
[SHADOW]    a faint contact shadow beneath each lamp, the same for all five.

CONSTRAINTS — binding.
· Every letter of the title sits inside its own cell with clear space around it, and at
  least 8% of the frame width from any frame edge.
· No lamp overlapped by type, and none favoured by scale relative to its own cell.
· No rank number, price, podium, scene, person, star row, certification seal, press logo
  or third-party award mark.
```

---

## 7 — `lede-authority` · knee compression sleeve · one photo · DIAGNOSTIC

NOTE: still a diagnostic and still creating no skeleton. Round 2 asked what survives when
everything illegal is stripped and answered *a demonstrator*. This one tests the owner's
own definition instead — a credible person using and experiencing the product in a fitting,
credible environment — with the credential itself still absent, because a printed one is
what G16 and G14 refuse. Of the three frames the owner named, one is already filed
`lede-inuse` in the ledger, so the question this round has to settle is whether a reader
can tell the two apart at all.

```
TYPE: lede-authority v0.2 — ROUND 3, DIAGNOSTIC. Not a skeleton.
REGISTER: editorial documentary photograph, one frame, no words in it.

[PRODUCT REFERENCE] the attached photo is the exact reference for the knee compression
            sleeve. Preserve shape, proportions, material, finish and colour exactly.

ELEMENTS — assemble and style these as the picture needs.
[SUBJECT]   a woman in her thirties in ordinary running kit, sitting on the edge of a
            running track at the end of a session, the sleeve on her knee, turned toward
            the lens and speaking as if answering someone just out of frame.
[MANNER]    assured and matter-of-fact — someone who has done this a long time and is
            saying what she found. Not posed and not smiling for a camera.
[PLACE]     a real athletics track in daylight, lanes and infield legible behind her.
[LIGHT]     plain overcast daylight, no studio key and no rim.
[GRADE]     a natural palette, light grain. Honest, not glossy.
[GROUND]    the track and infield behind her, thrown out of focus, plainly lit.

CONSTRAINTS — binding.
· Nothing states who she is — no name, byline, caption, title card, bib number, team kit,
  club badge, sponsor logo, lanyard, accreditation or medal.
· No lab coat and no clipboard.
· No word, number or logo anywhere in the picture.
```

---

## Grading

A verdict of `pass`, `partial` or `fail` per render. Then the questions this round can
settle — and the first one is about the prompts rather than the pictures.

| # | question | what it changes |
|---|---|---|
| 1 | **How many `CONSTRAINTS` held, against round 2's 4-of-4 failure on prescribed taste?** | whether `ELEMENTS`/`CONSTRAINTS` becomes the house form for every prompt this library writes |
| 2 | **In 3, did FIVE attachments hold five distinct real units?** | the last untested half of ADR-076's route, and whether `lede-lineup` is makeable |
| 3 | **In 3, does a strongly saturated sweep separate pale metallic units?** | the second branch of `lede-lineup`'s bimodal ground clause, which has never been rendered |
| 4 | **In 3, does a 45° grouped cluster still read as no-unit-favoured?** | whether arrangement can vary without breaking the type's own law |
| 5 | **In 4, is any figure legible anywhere — with a load bank switched on in frame?** | whether an outcome-stated constraint beats round 2's mechanism-stated one. This is the hardest test in the round |
| 6 | **In 4, does a bright clean lab at value ~0.80 still read as a REAL place?** | the owner's correction to `lede-testing`'s ground, and whether "bright" costs the documentary register |
| 7 | **In 5, does the `band` form work, and does it carry an interior?** | `MARKS`'s only zero-observation form, and ADR-068's badge clause at n=2 |
| 8 | **In 5, do the added graphics lift the product or compete with it?** | whether the owner's "yếu tố thiết kế" belongs in the type or in the prompt |
| 9 | **In 6, does a colour-cell grid read as a collage, and does the halftone survive?** | the LAYOUT axis, and whether `lede-collage` absorbs the proposed `lede-mosaic` |
| 10 | **In 6, does the title stay inside its cell and inside the safe area?** | round 2 breached G10 at 4.2% on a self-contradicting prompt; this one is not self-contradicting |
| 11 | **In 2, does the frame state EASE this time?** | the argument fault round 2 found, and whether it was the prompt or the type |
| 12 | **In 7, put beside 2 — can you tell them apart?** | whether `lede-authority` survives as a type or folds into `lede-inuse` under a gaze axis |

## Answers, 2026-09-09

### Question 1 first, because it is about the prompts and it is the reason for this round

**Constraints held 14 of 18.** Every `CONSTRAINTS` bullet across the six rendered prompts,
counted:

| prompt | held | broken |
|---|---|---|
| 1 `lede-pain` | 3 of 3 | — |
| 2 `lede-inuse` | 3 of 3 | — |
| 3 `lede-lineup` | 2 of 3 | same distance from the lens |
| 4 `lede-testing` | 2 of 3 | no second product class |
| 6 `lede-collage` | 2 of 3 | title inside G10's 8% |
| 7 `lede-authority` | 2 of 3 | no logo anywhere |
| **total** | **14 of 18** | **4** |

Against round 2, where the four prescriptions of TASTE embedded in an imperative body were
ignored **4 of 4**. That is suggestive rather than proven — different products, different
pictures, one render each — but it is the first evidence the library has either way, and it
points the same direction as the round-2 split between geometry and taste.

**Two of the four breaks are the prompt author's, not the model's.** Prompt 3's `ELEMENTS`
asked for *"varied depth"* and its `CONSTRAINTS` asked for *"same distance from the lens"* —
the same self-contradiction round 2 was supposed to have taught, committed again in a
different block. Prompt 4's *"no second product class"* was written for a bench and applied
to a laboratory that plausibly holds other units. **So the discipline that matters is not
the two blocks; it is reading them against each other before shipping.**

### The rest

| # | answer |
|---|---|
| 2 | **Yes — five distinct real units from five references, in one call.** The route is complete; round 2 had reached four. The brand marks also rendered legibly and correctly across five different makers, against `07-identity-pack`'s finding that printed lettering fails 1 of 2 |
| 3 | **Yes, cleanly.** A saturated sweep separates pale metallic units — the bimodal clause's second branch, evidenced for the first time. But *"strongly saturated colour"* returned saturation **1.00** against the corpus branch at 0.66–0.71, the same overshoot as round 2's cobalt at 0.92 against 0.55. **2 of 2** |
| 4 | **No.** The cluster reads as one group but the units sit at different depths. The prompt asked for both, so this answers nothing about the type |
| 5 | **Nothing legible — the constraint held under the hardest pressure yet.** Six seven-segment displays lit and facing the lens at frame centre; checked at 6×, not one resolves into a value. Round 2 stated the rule as a mechanism and it was ignored; stated as an outcome it held. **Caveat:** both outcomes rest on the model's inability to render small text (adapter Rule 5), so this is the model's limit rather than its compliance, and it breaks the first time a display is rendered large |
| 6 | **Yes on bright, no on quiet.** Value **0.78** against the owner's five named frames at 0.80, where the live clause says 0.65 — the correction is confirmed. Saturation came back **0.23** against their 0.07, because *"cool and neutral"* light laid a blue cast over a room the clause wants almost colourless. The lab coat appeared and broke nothing |
| 7 | **Unanswered.** Prompt 5 was not rendered |
| 8 | **Unanswered.** Prompt 5 was not rendered |
| 9 | **Yes to both.** The colour-cell grid reads as a collage and is a different picture from round 2's row. The halftone survived, and it is why ring texture reads **16.8** — the frame files DESIGNED only through `designed()`'s second branch at spread_v 0.08, the patterned-ground amendment, which has now earned its keep on a render for the first time |
| 10 | **No — and this is the finding.** Line 1 reaches **3.8%** of the frame width from the right edge, line 2 **7.6%**, against a constraint asking for 8%. Round 2 breached it too, at 4.2%, but that prompt contradicted itself and this one does not. **2 of 2.** A stated safe-area percentage does not control large baked type. Round 2's small badge words did keep their margin, so the failing case is SIZE, not text |
| 11 | **Yes.** Shoulders down, hands loose, jaw unclenched, nothing reading as strain. The round-2 argument fault is not promoted to `argument-faults.md`: one render stating it and one stating its absence is 1 of 2, and what changed was the prompt |
| 12 | **Yes, and it partly reverses round 2.** A second person stands at the frame edge with their back to camera and the subject is answering them — neither asked for nor forbidden. That makes the frame an INTERVIEW, a register `lede-inuse` cannot reach, because that type requires a candid subject unaware of the lens. **The discriminator may be the interlocutor rather than the gaze**, and a prompt can ask for one without naming anybody |

### Two measurement notes this round produced

**The texture confound now has both ends.** Round 2 found a photographed ground filed
DESIGNED because it was too DARK (value 0.25, texture 2.8). Round 3's `lede-inuse` render is
filed DESIGNED because it is too BRIGHT AND SMOOTH — a plain wall thrown out of focus at
value 0.79 returns texture 2.3. **2 of 2, both off `designed()`'s first branch**, and both
times `spread_v` said photographed correctly. The repair tested on 2026-09-09 still moves
five corpus frames and is still not applied here.

**Prompt 1 confirms the floor forwards.** Constraining the exposure moved the same type's
ground from value 0.25 to 0.45, and its texture from 2.8 to 6.3 — across the line, into
PHOTOGRAPHED, where it belongs. Fixing the picture fixed the measurement.
