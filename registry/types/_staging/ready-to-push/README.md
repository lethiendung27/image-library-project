# Ready to push — three types, six renders

Three staging types whose remaining blocker is **a render**, not more evidence.

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

| type | criterion 1 · ≥5 distinct sources | criterion 2 · router-confusion | criterion 3 · a rendered example |
|---|---|---|---|
| `03-spec-callout` | **CLEARED — 5/5** | not run | **NO RENDER** ← prompts 1, 2 |
| `06-relief-claimstack` | **CLEARED — 9/5** | not run | 2 renders, **but the file changed today** ← prompts 3, 4 |
| `07-identity-pack` | 4/5 — one source short | not run | **NO RENDER** ← prompts 5, 6 |

Criterion 2 I can run against `eval/golden/` whenever you want it; it needs no renders.
Criterion 3 needs you, and criterion 3's verdict is the one SPEC §6.3 says must be yours.

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

Then these, because each answer changes a specific clause in a specific file:

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

## What to send back

The renders and your verdicts. I will write the results into each file's own FOUNDING RENDER
ROUND section with the measurements taken off the files, patch what the evidence moves, and
say plainly what it does not move. If a clause survives a render that ignored it, that clause
is a candidate for deletion — ADR-015: a clause is cut only when a render has done without it.

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
