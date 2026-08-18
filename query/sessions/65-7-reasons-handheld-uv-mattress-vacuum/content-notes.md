# content.json — how each field was derived (page 65)

`content.json` validates against `mapping/content.schema.json`, which closes every
level with `additionalProperties: false`. The reasoning below therefore cannot live
inside it, and lives here instead. It is read by people, never by `build.py`.

## Source

| | |
|---|---|
| file | `landing-page-7-reasons-this-handheld-uv-mattress-vacuum-helps-tackle-hidden-dust-mites.json` |
| page_id | 65 |
| lpTypeId | `listicle` |
| template | TPL-ADV06 |
| shopifyProductGid | null |
| imageBriefs | null |

The export is not a `content.json`. It carries `page.content`, `page.htmlCompiled`
and `brief`, but no `product.attributes` block and no `reference_photos`. Every
attribute below is DERIVED and marked as such — none was supplied by the source.

## Channel

`lpTypeId` is `listicle`, which is not one of the four channels in
`registry/vocabulary.yaml` and has no column in `mapping/slot-rules.md`. Routed as
**advertorial** on the page's own evidence rather than by guess: a bylined author
with a credential line, an About-the-author bio, a seven-comment thread with names,
a disclosure line, and editorial footer navigation. A listicle is an advertorial
format, not a fifth channel.

## Awareness

**problem-aware.** `brief.awarenessStage` says `problem` and the copy agrees: the
hero spends its whole opening re-establishing the symptom before naming anything,
`copyFramework` is PAS, and reasons 0 to 2 are all failures of the tool the reader
already owns rather than features of the one being sold. The schema has no field for
this and that is deliberate — `query/runbook.md` Step 5b says awareness is READ from
the copy, never asked for.

## Attributes, and what each one decides

| attribute | value | why, and what it gates |
|---|---|---|
| `operation` | `active` | The user pushes the unit over a mattress in passes. Sets the POSE branch to mid-action, hands engaged, gaze on the point of use. |
| `visible_output` | UV lamp light and a red/blue dust-level indicator | TWO real emissions, both named in `brief.specification`. G8 is satisfied without inventing anything — but the HEAT at 149F is NOT an emission any register can show, and no option argues it. |
| `mounting` | `handheld` | Handheld and corded. G7-X's installed mode never binds, and `06-relief-hero --context` is unavailable because its inset is defined as the product in its real installed position, which a handheld does not have. |
| `colorways` | one | A second colorway in any layer would violate G2. |
| `body_contact` | `false` | The page's most consequential gate: the product acts on a mattress, not a body, so `03-mechanism-ghostbody` is dropped by its own `avoid_when` and every mechanism slot goes to `03-mechanism-xray`. |
| `symptom_visibility` | `visible` | Photographable on a body — waking congested, rubbing eyes, a child scratching eczema — and on an object, as grey powder in the dust cup. |
| `result_visibility` | `on-object` | A filled dust cup and an indicator turned blue. NOT on-body: nobody can photograph waking up un-congested, which is why `06-relief-scene` is dropped by its own `avoid_when` and the closing image is `06-relief-hero` with the product in frame. |
| `multi_step_usage` | `false` | One pass, one action. Drops `03-use-sequence` by its `avoid_when`, "the product has one obvious action". |

`build.py` now evaluates four of these gates from this file at build time and
reports which fired and whether any option used a type they killed. Before
2026-08-18 nothing read `content.json` at all.

## Sections

One section per image slot. The template's `reasons.items.N` are separate cards with
their own heading and copy, and their roles differ per item — grouping them under
one section would throw away the roles the router reads.

`author` was added to the role vocabulary on 2026-08-18 for the two portrait slots.
Before that, `content.json` had no legal role to declare them under, so they were
either mislabelled `cta` or left out of the contract entirely.

## Known gaps

1. **Seven body slots declare `aspect-[4/3]` with `object-cover`, and only two types
   in the library declare 4:3** — `05-social-snapshot` and `06-relief-scene`. Every
   other type legally declares 16:9 and 1:1 only. Those seven are routed by argument
   and rendered at the chosen type's own declared ratio; the layout then centre-crops.
   `build.py` counts this: 21 of 42 options render at a ratio their slot does not
   declare. ADR-016's standing RATIO sweep is the real fix and it is a type-file edit.

2. **`reference_photos` is empty.** `imageBriefs` and `shopifyProductGid` are both
   null, so there is no product photograph to hash (SPEC §6.4) and `attachments` is
   omitted from every option rather than invented. Per ADR-021 this is a gap in the
   EXPORT, not a blocked prompt: the owner uploads the reference in the tool.

3. **The reviews section places `reviews.photos.0-5` inside the same section element
   as six named quotes**, each carrying a five-star row and a green Verified label.
   `05-social-snapshot`'s authenticity fence bars a generated snapshot from sitting
   beside a name, star row or verified badge. Eighteen prompts carry the precondition.

4. **`brief.rawFeatures` warns that the page's claims outrun the evidence**: mattress
   vacuuming has limited effect on total allergen load on its own, the 99.9 percent
   figure needs the manufacturer's test data because UV dose depends on dwell time,
   and UV-C is harmful to eyes and skin with the lift-off cut-out unconfirmed. No
   image on this page asserts a kill rate, a percentage or a health outcome.
