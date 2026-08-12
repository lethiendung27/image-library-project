# Runbook — render-test a skeleton

The library's value is TESTED skeletons. This is the loop that turns
`run: untested` into `pass` — or into an evidence-backed patch. It is the render-side
twin of ingestion: observations classify other people's images; render tests judge our
own prompts against the real model.

## 1. Pick a target

Priority order:
1. Types about to serve a real page (query results waiting on confidence);
2. Worked examples carrying a `Predicted failure` — confirm or refute it;
3. Stress products far from the type's origin domain (the seed corpus practice:
   a skeleton born on cushions gets tested on filters and sharpeners).

A target = type + variant/axes + a real product (with reference photo when
`requires_product_photo: true`) + ratio.

## 2. Fill and render

Fill the prompt exactly as `query/runbook.md` Step 5 prescribes (or reuse the type's
worked example), then apply `adapters/nano-banana.md`. Multi-pass types follow their
`steps[]` script — testing the script is part of the test.

## 3. Generate 2–3 runs

Recurrence needs a denominator. One run proves nothing either way (SPEC §6.2).

## 4. Record — one line per test session

Append to `eval/render-tests.jsonl` (append-only):

```json
{"ts": "<ISO date>",
 "type": "01-pain-split", "type_version": "1.2",
 "variant": "object", "axes": {},
 "product": "rolling knife sharpener", "ratio": "1:1",
 "runs": 3,
 "verdict": "pass | partial | fail",
 "failures": [
   {"slot": "[HOTSPOTS]", "observed": "5 scattered hotspots instead of 3", "recurrence": "2/3"}
 ],
 "output_refs": ["sha256:<hash of a representative output, optional>"],
 "notes": "<anything the fields cannot carry>"}
```

`failures[].slot` names the skeleton slot or zone; `observed` says what the model
actually drew; `recurrence` is `x/y` over this session's runs. A `pass` has an empty
`failures` list.

## 5. Patch by the evidence rule (SPEC §6.2)

- Recurrence **≥2/3** (or ≥3 observations across sessions) → patch the type file:
  slot ambiguity → split the slot; model weakness (hands, text, faces) → NEGATIVE;
  structural → skeleton with MAJOR bump. CHANGELOG cites the render-test `ts` +
  product.
- One-off → the type's KNOWN-FLAKY, with the `ts`. Do not touch the skeleton.
- A `Predicted failure` that did NOT occur → delete the prediction line from the
  worked example (stale caution is noise).

## 6. Update the worked-example status

When the tested prompt corresponds to a worked example, update its header
(`run: untested` → `pass|partial|fail`, and `skeleton@` to the version tested). If the
session produced a better example than one of the two stored, replace the weaker
(hard cap 2 stands). Then:

```sh
python3 scripts/validate.py --write-index
```

Commit the render-test session as ONE commit (ledger line + patches + regenerated
index) once the validator is clean; report hash + revert path (ADR-007).

**Who assigns the verdict (ADR-011).** The owner may state it, and their word always
wins. Where they delegate, the harness assigns it — under three conditions, all
binding:

1. **The render must be in hand.** A verdict for an image the harness has not examined
   is fabrication, and that has not changed. The owner drops renders in
   `image-library-assets/feedback/`; if a render is not there, there is no verdict.
2. **Label against the skeleton, and say whose label it is.** Every self-assigned
   record carries `verdict_by: "harness"` in `notes` and names what was checked. A
   `pass` still means an empty `failures` list, so a render with a visible defect is
   `partial` even when the owner has approved the set — otherwise the defect vanishes
   from the evidence base that justifies patching it.
3. **Promotion is excluded.** SPEC §6.3(3) still requires the owner's own verdict, so
   a self-assigned label can support a patch under §6.2 but can never make a staging
   type routable.

The owner keeps the veto. The ledger is append-only, so a disputed label is corrected
by a new record, never by an edit.
