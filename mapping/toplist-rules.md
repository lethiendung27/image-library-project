# Toplist rules — selecting the lede image

Layer 2 of the four in `registry/toplist-instruction.md`. **The preference table below is
a HYPOTHESIS with no evidence behind it** and this sentence is the most important one in
the file. It was written from the owner's own reading of the format on 2026-09-09, not
from anything this library has measured, and it is here so that the first pages routed
have something to disagree with.

The library has been caught once already writing a rule that felt obvious and moved a
whole render set off the market: ADR-068, where three type files were told to take the
ground from the product's own register and nobody measured the corpus first. This table is
the same shape of risk, declared in advance.

## Layer 1 — mechanical admission. Refuses. No awareness, no judgement.

Runs first and runs on the product input alone.

| condition | effect |
|---|---|
| `status: reserved` | not routable, ever. **No type is reserved today** — `lede-authority` was the last and went active at its own 0.3 (2026-09-09, commit `c81ae0d`). The row stays because the mechanism does |
| `products_in_frame: many` and the input carries fewer than 3 distinct products | refuse |
| `products_in_frame: many` and the input carries no photo for a unit | refuse — one reference per unit since ADR-076 |
| `requires_product_photo: true` and `reference_photos` is empty | refuse, and say so in the session notes rather than shipping a prompt the owner cannot run |
| `result_visibility: invisible` | drop `lede-inuse` |
| the input carries no rank or verdict for the winning product | drop `lede-winner` — its mark is the type, and the mark's words come from the input (ADR-071). The field does not exist yet, so this refuses on every page until it does |

After layer 1 on a page with one product and one photo, the live pool is `lede-pain`,
`lede-inuse`, `lede-testing` and `lede-authority` — **four** types, one more than
ADR-058 asks a slot for. On a page carrying three or more products with a photo each,
`lede-lineup` and `lede-collage` join them (ADR-076), and `lede-winner` joins on any page
whose input carries a rank.

**No input does either yet, and that is worth stating once rather than implying it three
times.** `content.json` carries exactly ONE `product` and no rank field, so on every page
routable today those three types are active and refused at layer 1 — the same shape as
`requires_product_photo: true` meeting an empty `reference_photos`. Both absences are item
1 and item 2 of the missing-field list in `registry/toplist-instruction.md`, and both are
schema jobs rather than type jobs. **Admission is therefore never the binding constraint
here; ORDER is.**

## Layer 2 — preference order, keyed on awareness. HYPOTHESIS.

| awareness | preferred, best first | the reasoning, such as it is |
|---|---|---|
| `unaware` | `lede-pain` | nothing else can earn a click from someone who does not know the category exists |
| `problem-aware` | `lede-pain`, `lede-inuse` | message match with the ad creative; the reader recognises the problem before the product |
| `solution-aware` | `lede-inuse`, `lede-testing`, `lede-authority` | the category is accepted; the question is whether it works — answered by a measurement, or by someone who lived with it |
| `product-aware` | `lede-testing`, `lede-winner`, `lede-lineup`, `lede-collage`, `lede-authority` | the reader is comparing names and wants to know the work was done; a field of rivals IS the comparison |
| `most-aware` | `lede-winner`, `lede-lineup`, `lede-collage`, `lede-testing` | one question left, and it is which |

`lede-lineup` and `lede-collage` went active at ADR-076 and need one reference photo per
unit. `lede-winner` is active as of ADR-071 but needs a rank on the input, which layer 1
refuses without. `lede-authority` went active at its own 0.3 (`c81ae0d`) on a reading of
its three refusals against their own text rather than on a waiver. **No type is reserved.**

**`lede-collage` and `lede-authority` were missing from the table above until 2026-09-10.**
Both went active after it was written and neither was added, so two of seven active types
carried a row in layer 1 and none in layer 2 — admitted, then ordered by nothing. They are
placed here from their own declared `awareness` and `use_when` and from nothing else, which
makes their placement **the same hypothesis as every other row rather than a weaker one**:
`lede-collage` sits directly beside `lede-lineup` because ADR-069 kept those two apart on
HOW they claim the five — possession against enumeration — and not on who the reader is;
`lede-authority` sits behind `lede-testing` wherever both appear, because G9 prefers the
physical fact to the person and that type's own BOUNDARY says the same.

**Awareness is read from the input and from nowhere else, and it is deliberately weak.**
The owner's instruction of 2026-09-09 was to carry it and not to lean on it, and SPEC §7.5
says awareness should be read from a page's own copy rather than declared as an input
field. There is no page copy here, so it is declared — a stated departure from §7.5, not
an oversight — and it is confined to this one table, which orders and never refuses.

**A second signal is available and is NOT used yet.** The product block's prose carries a
shape: a brief heavy in `problems_solved` is written problem-first, and one heavy in
`specification` and `raw_features` is written feature-first. That ratio is derivable with
no new field and would order the same five rows without any declared stage. It is left
unbuilt on purpose — writing a second unmeasured rule beside the first is how the ground
clauses of ADR-068 happened.

## Layer 3 — FIT, and the record it must leave

The order above proposes. What decides is judgement over each type's `use_when` and
`BOUNDARY` against the product prose — which is the state ADR-059 accepted knowingly when
it removed the last mechanical gate: *"judgement does not scale and no regex audits it"*.

**So every choice cites the sentence of product copy that decided it.** One line per
option, in `prompts.md` and in the session's `prompts.json`, naming the field and quoting
the sentence. That is ADR-059's own mitigation and it is law in this namespace: it turns
an unauditable judgement into a record that a later pass can grade.

## Layer 4 — pick rate, and the plan to make this table real

`feedback/picks.jsonl` per SPEC §7.7: a soft prior at ≥20 contested observations per cell,
never overriding an admission rule. It holds **0 records** today.

One slot per page means **one record per page**, and with a single role the cell is keyed
on the type alone rather than on (type × role). **Twenty top-N pages make this prior
live** — the fastest any cell in this library can fill, and the reason this format is the
right place to replace judgement with measurement rather than to argue about it.

When that cell fills, the table above is graded against it. If the two disagree, the
measurement wins and this file is rewritten with the disagreement recorded.
