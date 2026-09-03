# Ready to push — three types, six renders

**ROUND 1 HAS RUN AND ROUND 2 IS IN `prompts.md`.** All six founding renders arrived on
2026-09-03, were examined and measured, and their results are written into each type's own
file rather than here: `FOUNDING RENDER ROUND` in `03-spec-callout` and `07-identity-pack`,
`SECOND RENDER ROUND` in `06-relief-claimstack`, a `WORKED EXAMPLES` entry per render carrying
the prompt that produced it, and six records in `eval/render-tests.jsonl`.

**Then the owner audited them: the colour choices are poor and the badges are still not as
rich as the corpus's.** Both were measured against the market before anything was rewritten —
119 direct-response corpus frames for the ground, four corpus badges for the interior — and
both are true. G16 gained a round-4 section, the three type files were corrected, and
`prompts.md` now holds **six new prompts on six products none of these types has seen**.

**What is left is yours**: three verdicts on round 1, and the judgement questions no
measurement reaches. Round 2 is ready to render whenever you want it.

Three staging types whose remaining blocker was **a render**, not more evidence.

**This folder holds no copies of the type files, and that is deliberate.** They live one
directory up and are the law:

    ../03-spec-callout.md
    ../06-relief-claimstack.md
    ../07-identity-pack.md
    ../../../rules.md            G16, the text layer all three declare

An earlier version of this folder shipped byte copies of all four so they could be read
without opening the repo. Inside the repo that is the defect SPEC invariant 1 exists to
prevent: two copies of one file drift, and the stale one is the one somebody reads. Open the
originals.

The folder name is hyphenated rather than spaced because this project lost a whole batch to a
space in a directory name once — a manifest command truncated 653 paths at the space and
reported 0 outstanding (commit `e4af746`). Nothing here would break today; the habit is cheap.

## What each type is blocked on

| type | criterion 1 · ≥5 sources | criterion 2 · router-confusion | criterion 3 · a rendered example |
|---|---|---|---|
| `03-spec-callout` | **CLEARED — 5/5** | not run | 2 renders, **partial · partial** by eye — your verdict outstanding |
| `06-relief-claimstack` | **CLEARED — 9/5** | not run | 4 renders across 2 rounds, latest **pass · partial** — your verdict outstanding |
| `07-identity-pack` | 4/5 — one source short | not run | 2 renders, **fail · partial** — your verdict outstanding |

Criterion 2 I can run against `eval/golden/` whenever you want it; it needs no renders.
Criterion 3's verdict is the one SPEC §6.3 says must be yours — ADR-011 lets me grade a
render I have actually looked at, and I have graded all six, but not for this criterion.

**`07-identity-pack` is the one to read first.** Its `fail` is not a bad frame; it is the
type's own definition firing. `PARTS/light` said a render whose pack lettering is gibberish
is a total failure rather than a flaw, and the juicer cup came back printed `batglie`,
`BRELLING THAT JUICER CUP` and `NONJHUTIVE SUPPORTS`. The repellent pouch in the same round
printed nine lines perfectly. One of each is a denominator, not a rule — and it means this
type cannot be promoted on a source count.

**`07-identity-pack` is one source short and is in this folder anyway**, because it is the
concrete form of your Q2b decision and because a render tells us something a fifth source
would not: whether a diffusion model can hold a pack's own printed lettering. Three frames in
the corpus already came back with malformed labels, and for a type whose whole deliverable is
identity that is a total failure rather than a flaw.

## Why these products

Every product in `prompts.md` comes from `query/product-slugs.yaml`, the repo's own closed
list, and **not one of them appears in any proposal's source list**. The types were built from
supplements, coffee, pet food, wearables and personal-care devices; they are being tested on a
juicer, scissors, earbuds, a vacuum, an arm trainer and repellent balls.

A rule that holds on a product it has never seen is a rule. A rule that holds on the product it
was written from is a coincidence.

## What each pair of prompts isolates

- **1 and 2** run `03-spec-callout` at five clusters and then at eight, on two different
  products. Five is what G16's founding rounds actually measured; eight is what this type's
  own count rule allows. **If eight degrades, the type's ceiling is whatever holds**, and its
  KNOWN-FLAKY says so already.
- **3 and 4** each isolate ONE clause that was widened in `06-relief-claimstack` today.
  Prompt 3 puts the PRODUCT in the subject slot and holds the field at the known-good flat
  tone. Prompt 4 holds the subject at the known-good person and puts the field in a REAL ROOM
  with the words straight on the wall, no panel. Changing one thing at a time is the only way
  a failure attributes.
- **5 and 6** run `07-identity-pack`'s two forms — closed, and with its contents at its foot —
  on two products. Both watch the same thing: the pack's own printed lettering.

## Grading

Give each render a verdict of `pass`, `partial` or `fail`. That verdict is yours under ADR-011
and criterion 3 requires it; I may grade a render I have looked at, but not this one.

**Nine of the thirteen questions below are now answered off the files and the answers are in
the type files.** The four in bold below are yours, because each is a judgement no pixel
measurement reaches. The rest are left standing with their answers so the table still reads
as the record of what the round was for.

| # | question | what it changes |
|---|---|---|
| 1 | Is every word spelled exactly as written? | G16's seven-word line cap, which now rests on 45 lines |
| 2 | **Prompt 2 vs 1: did all eight clusters hold, and did the picture degrade?** | `03-spec-callout` PARTS/callouts — its three-to-six count rule, and G16's budget |
| 3 | Do the leader lines land on the parts they name, or near them? | PARTS/callouts — whether a leader is legislated or dropped for the ring form |
| 4 | **Prompt 3: does a PRODUCT in the subject slot read as well as a person did?** | `06-relief-claimstack` PARTS/subject, widened today on four sources |
| 5 | **Prompt 4: do the words stay legible on an out-of-focus wall with no panel?** | PARTS/field, widened today on three sources |
| 6 | **Prompts 5 and 6: is every word printed on the pack still a real word?** | `07-identity-pack` KNOWN-FLAKY — the risk that decides whether this type is makeable at all |
| 7 | Is the badge clean in the lower LEFT? | confirms the watermark-corner rule, 4 of 4 so far |
| 8 | Does any text come within a tenth of an edge? | G10's 8% floor, breached on every text render so far |
| 9 | Did anything appear that nobody asked for? | goes to that type's NEGATIVE, not into longer prose |
| 10 | **Is the headline a hook or a caption?** Would it be equally true of a competitor? | G16's new copy-craft section — the half the rule was missing until 2026-09-03 |
| 11 | Did any line past seven words render cleanly? | moves G16's line cap off habit and onto evidence |
| 12 | **Is the headline as tall as the thing it was anchored to?** Measure it against that object | decides whether an anchor beats a fraction at sizing — the fourth time this library has tested that pattern |
| 13 | **Is the badge the first thing you see, before the product?** | G16's badge prominence rules — size, position and colour, all three added on the third pass |

## About the copy in these prompts

**Rewritten 2026-09-03 after the owner's verdict that the copywriting was too weak to ship.**
The first draft wrote captions — THIS IS WHAT ARRIVES, EVERY PART NAMED — averaging 4.5 words
against the market's 8.0, and the difference was never length. Every market line names a
result, a feeling or a problem state; every line the first draft wrote named what was in the
picture. A caption describes the frame; a hook describes the reader.

The lines are now hooks and **they are drafted copy, not any page's own copy** — there was no
`content.json` to draw from. They claim only what each object's facts support and carry no
figure, no percentage and no timeframe, so nothing here needs substantiating. On a real page
every word comes from that page's copy.

**Guardrails on text no longer bind** (owner instruction, same day). G16's caps now record
what has been measured rather than fixing a limit, and its content refusals are a cost table
rather than a wall. Two rows in that table are marked LAW rather than taste and are left
standing: a fabricated endorsement, which G14 calls illegal and which binds the SLOT rather
than G16, and a certification or press mark, which is a trademark question the library
declined to answer on 2026-08-18. Either can be struck — with an ADR, so it is a decision
somebody took rather than a side effect.

**Judge the copy as copy.** If a headline here is weak, say so and say why; that is worth more
to the rule than another clean render. The one question the rewrite cannot answer alone is
whether a hook survives at 10 to 14 words, because the old cap was never tested above seven.

## Second pass, 2026-09-03 — four owner findings, all measured

| finding | measured | fixed by |
|---|---|---|
| prompt bloat | 1488–2128 chars against adapter Rule 6's 1450–1600 reference; 4 of 6 over | rewritten to **1431–1708**, down from 1488–2128; four of six inside the reference band, two just over after the badges gained size and colour |
| badge monotonous | 6 of 6 prompts wrote the identical flat rectangle | **a badge is a MARK, not a text slot.** G16 hands the form back to the type; each of the three types now owns a form library, and the six prompts use six forms — chip, tag, pill, seal, roundel, flash |
| background monotonous | 6 of 6 wrote "one plain pale grey ground" | six grounds, each from the product's own register — charcoal, workbench brown, deep teal, a lit wall, a citrus gradient, slate |
| text too small for mobile | headline bands 5.0–6.1% of frame height, everything else 3.3–5.5% — **19–24px and 13–21px on a 390pt phone**, against a 17px platform floor on both iOS and Android | G16 gains a mobile floor. **First attempt stated a fraction and was wrong** — see the third pass below; it is now anchored to a named thing in the frame |

**The badge change is the structural one.** G16 listed `badge` as a third text slot with one
shape, and six prompts written under that reading produced six identical rectangles. The repo
had already settled it twice — ADR-012 gives each type its own MARKS library, and ADR-043
proved a badge is a library of five interchangeable forms rather than a constant. G16 now
governs a badge's WORDS and the type governs its FORM.

**Why maximisation alone left the text small.** G16 said the block grows until it would cover
information. A short block in a large empty field has nothing to grow against, so it stays
small and stays compliant. The floor is what maximisation was missing.

## Third pass, same day — the first two fixes changed the wrong variables

The owner read the rewritten prompts and said the badge was still monotonous and the text
still too small. Both correct. Neither needed a render to check.

**The badge had been given eight FORMS and no PROMINENCE.** Six prompts used six shapes and
were still identical where it counted, because form was never the variable. Checked, not
assumed: there was **no badge size rule anywhere** — not in G16, not in the three MARKS
libraries, not in a prompt; the only size word in six prompts was "small". **6 of 6 badges sat
in the lower left.** And **every badge borrowed a colour already in the frame** — white seven
times, grey twice. A badge sharing the picture's palette recedes into it. All three now vary
per product, and G16 carries the rules rather than each prompt inventing them.

**The text floor was the third fixed number aimed at a sizing problem in this library.** G10
records the first two failing — six inset panels "broadly compliant" between 16.6% and 31.1%
of frame width and still read as too small — and concludes that *maximisation needs no
measurement, which is why it is the rule*. Adapter Rule 4: a written ratio does nothing to
this renderer, 6 of 6. So "a tenth of the picture's height" would have been ignored.

What this library has measured working is an **anchor** — an arrow described by its endpoints
2/2, a badge whose glyph was named 2/2, alignment written as an observable 4/4. Every size
clause now names something in the frame: *as tall as one earbud is long*, *as tall as the
scissor blade*, *as tall as one of the loose balls*. **Mobile legibility comes from choosing a
big anchor**, and question 12 below asks whether it worked.

## What the round answered, and what it did not

| # | question | answer |
|---|---|---|
| 1 | every word spelled exactly? | **33 of 34 lines exact, zero misspelled.** One line gained a word: `The display counts` came back `The display counts reps` |
| 2 | did all eight clusters hold? | **yes, 8 of 8, once each, nothing duplicated.** The picture did not degrade; the ATTACHMENT did — see 3 |
| 3 | do the leaders land on the parts they name? | **9 of 10.** At six labels two leaders cross; the one clean miss is a label written for the open lid landing on the case body |
| 4 | **does a PRODUCT subject read as well as a person did?** | rendered clean, 1 of 1, and structurally safer — no G9 tension, no G13, no cut-out edge. Whether it READS as well is yours |
| 5 | do words stay legible on an out-of-focus wall, no panel? | **yes, 1 of 1.** What made them read is the depth of the defocus, not a panel |
| 6 | is every word printed on the pack a real word? | **1 of 2.** Nine lines perfect on the pouch; three invented strings on the cup |
| 7 | is the badge clean in the lower LEFT? | superseded — badges went to four different corners this round and **6 of 6 landed where asked**. Bottom-right stays barred, and now for every element, not just a badge |
| 8 | does any text come within a tenth of an edge? | **yes, and it is the badge every time.** Text blocks 5.37–10.16%; badges 0.00–6.05%. The corner ribbon reaches both edges by construction |
| 9 | did anything appear nobody asked for? | one inserted word, one headline re-wrapped from two lines to three, and an invented net weight, count and ingredient list printed on a pack |
| 10 | **is the headline a hook or a caption?** | yours. No measurement reaches it |
| 11 | did a line past seven words render cleanly? | **7 such lines, 6 exact.** The one that did not is the inserted word, not a spelling failure. The cap is off habit and onto evidence |
| 12 | is the headline as tall as its anchor? | **no — 0.13 to 0.64 of it, five measured, and the ratios run backwards.** The anchor sizes an OBJECT and does not size a GLYPH. G16 carries the finding |
| 13 | **is the badge the first thing you see?** | yours. Measured at 1.98–5.05% of the frame, in four corners, six colours — but "first thing you see" is perception |

## What to send back

Three verdicts and the four bold answers. Everything the files could answer is already written
into them, with the measurements taken off the renders. If a clause survives a render that
ignored it, that clause is a candidate for deletion — ADR-015: a clause is cut only when a
render has done without it.

**One hole in the test, recorded rather than hidden.** Nothing in the round records whether a
reference photograph was actually attached to prompts 1, 2, 3, 4, 5 and 6. For
`07-identity-pack`, where G1 is the entire frame, that means the juicer-cup failure cannot be
told apart from a missing reference. The next round logs it.

## Reading the skeletons

If you want to change the STRUCTURE rather than the prompt, open the three files one directory
up. Two things worth knowing before you do:

- A skeleton is a **call-map**. Each line names an entry in `PARTS` and the definition lives
  there once. The model never reads the type file, so a called name is expanded into the
  prompt at render time — which is why the prompts here are long and the skeletons are short.
- All three declare `text_layer`, so all three are bound by **G16** in `registry/rules.md`.
  That rule is what the prompts' word caps, badge corner and margin clauses come from, and it
  is the file to read before changing any of them.

## Where this folder sits in the workflow

`_staging/` is not routable — the router never reads it, the validator excludes it from
`index.yaml`, and no active type may reference anything in it. That is exactly the right place
for work being tested: the material is under version control and in front of the next session,
and none of it can reach a page by accident.

Both scripts that read `_staging/` enumerate it with `os.listdir` and filter on `.md`, so this
subdirectory is invisible to them. Checked before it was created, not after.
