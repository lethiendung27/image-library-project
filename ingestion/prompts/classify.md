# Classification template — c1.0

Per-image instruction for INGEST (SPEC §6.1). `template_version: "c1.0"` goes into
every record produced with this template. Any change to this file bumps the version
(c1.1, …) in the same commit — curation discounts records from older templates.

## Context contract

You have in context: `registry/index.yaml`, `registry/vocabulary.yaml`, this template,
and ONE image. Nothing else. You may load ONE full type file only when a suspected
match requires comparing slots — say so in the breakdown.

## Procedure — the absorption ladder, in strict order

Classify by ARGUMENT STRUCTURE (what the image sells and through which device), never
by subject matter or visual similarity. Walk the ladder; escalate only when the level
demonstrably fails:

1. **Parameter?** Differences that are runtime values (ratio, colorway, panel count,
   cast, environment) do not change identity → verdict `match`.
2. **Axis value?** Same argument, different presentation on a global axis
   (register/camera_lock/gaze/context_mode/inset_mode) → verdict `match`, record the
   axis values you observed.
3. **Variant?** Same job+device, exactly ONE structural decision differs from the
   type's skeleton → verdict `variant-candidate`, name the one decision.
4. **New type?** Different job OR device than everything in the index → verdict
   `new-candidate`, propose an id in `{NN}-{job}-{device}` grammar (new job/device
   values are allowed but must be flagged).

Other verdicts: `duplicate` (same or near-same as an already-ledgered image — check
recent observations if provided), `reject` (not an e-commerce product argument image:
memes, raw product photos, screenshots of text, illegible).

## Record format (full breakdown — every image, ADR G3 decision)

Append ONE line to `ingestion/observations.jsonl`:

```json
{"hash": "sha256:<file hash>",
 "ts": "<ISO date>",
 "template_version": "c1.0",
 "verdict": "match | variant-candidate | new-candidate | duplicate | reject",
 "type": "<matched or nearest type id, null for reject>",
 "proposed_id": "<only for new-candidate>",
 "axes": {"<axis>": "<observed value>"},
 "deviations": [{"slot": "<skeleton slot name>", "observed": "<what the image does differently>"}],
 "breakdown": "<8-15 sentences: zones/layers and their jobs; the argument structure (what it sells, to whom, at which funnel step); signature devices; color semantics vs G3; register; camera; which global rules it obeys or breaks; what is strong; what is broken>",
 "quality_flags": ["low-res" | "watermarked" | "cropped" | "ai-artifacts"],
 "source_batch": "<batch id>"}
```

Rules:
- `deviations` is empty for a clean `match`; for `variant-candidate` it contains
  exactly the ONE structural decision; never patch a type from here — curation does
  that with the ≥2/3 rule.
- The breakdown is evidence for future curation — write it so someone who cannot see
  the image can still judge the classification.
- One line per image. Never edit existing lines (append-only ledger).
