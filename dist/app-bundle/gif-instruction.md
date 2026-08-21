# GIF library — the one instruction every type inherits

Shared law for the GIF library (ADR-023). A type file in `registry/gif-types/` states
only what is TRUE OF THAT TYPE; everything below is true of all of them and is never
restated in a type file, the same way types reference `registry/rules.md` by ID rather
than copying rule text (SPEC §5).

The folder cards an editor reads are GENERATED from the type files by
`python3 scripts/gen-gif-cards.py`. A card inside the library folder is never edited by
hand — it is a view, exactly as `registry/index.yaml` is a view.

## 1. One folder, one message

A GIF belongs to exactly one type, and the type is decided by **what the loop argues**,
not by what it depicts. Two loops that argue the same thing are the same type however
different they look; two loops that argue different things are different types however
similar they look (SPEC §3.1, applied to motion).

Where a GIF carries several beats — and a 3-second ad loop usually does — file it by its
**dominant argument**: the beat the loop would be pointless without. A loop that cuts
through four use cases is still one message ("it handles all of these"), and that message
is `use`.

## 2. What earns motion

A subject earns a loop when its reason to exist is **temporal** — a transition, a
sequence, a state changing, an output flowing. A subject that exists to reveal an angle,
a place, a colorway or a set of parts does NOT: revealing is not changing. This is the
same test `query/runbook.md` Step 5c applies per slot, and it is applied here to the
asset itself.

## 3. Absorption — the anti-explosion rule for motion

Before proposing a new gif type, absorb at the cheapest level that fits:

1. **Parameter** — beat count, duration, ratio, colorway. Changing it does not change
   the argument. Beat count is the trap: one act and four acts are one type.
2. **Execution** — subject class, environment, register, with or without a person.
   Named in `varies_on`, never a new folder.
3. **New type** — a genuinely different argument. Requires a vocabulary addition to
   `gif_types`, which is a taxonomy decision of the same weight as adding an image type
   (SPEC §4).

Two folders behind one message is the failure this rule exists to prevent.

## 4. Naming

```
{gif-type}_{product-slug}_{seq}.webp
```

`use_hinge-tool_003.webp`, `proof_dust-mite-remover_001.webp`. Hyphens inside a field,
underscores between fields, `seq` three digits **issued by the ledger** at classify time
so two people cannot collide. A file is never renamed after it enters the library:
briefs and the ledger both reference it by name.

**A loop is named twice, and since ADR-028 both names carry the gif type.** The line above
is the LIBRARY name, issued by the ledger when a finished loop is filed. The PAGE name is
issued earlier, by the routing that commissioned it, and it is what the editor hands back:

```
{page-type}-{gif-type}-{product-slug}-v{NN}-{slot}.webp
```

`advertorial-mechanism-seat-cushion-l-shaped-v04-features1.webp`. It is the session
directory — `{page-type}-{product-slug}-v{NN}` (ADR-034) — with the gif type inserted after
the page type and the slot appended, so a reader gets the argument, the product, the page and
the slot without opening anything. The slot is derived from the `slot_id` and is required:
two loops on one page may share a gif type, and without it they share a filename (ADR-036).

The page id is deliberately absent. It identifies the source export rather than the loop, it
lives in `prompts.json.page_id`, and one routed session has none at all — a name that depended
on it could not have been written.

Delivery is **animated WebP**, loop-safe, under the size ceiling. It carries no audio track
by format, so there is nothing to mute, and it sits in an `<img>` where a still already sits
rather than needing a `<video>` element the page template does not have — which is what lets a
loop occupy an image slot at all and keeps a loop and a still interchangeable. WebP runs
larger than mp4 at the same quality, so the ceiling binds harder than it did; that is the
trade taken knowingly (ADR-036). The `.gif` extension names the format the owner asks for in
conversation, never the file that ships.

## 5. The one-line description

At classify time each GIF gets ONE line, written to `ingestion/gifs.jsonl`, in this
shape and this order:

```
<what moves> → <what it leaves>, <register>
```

`head glides over the weave → grains lift clear, ugc phone light`. It is written so a
person scanning the ledger can tell two files apart without opening either. It is not a
caption and never ships.

The record it goes into, one per line, append-only — a correction is a new record and
never an edit (SPEC §2):

```json
{"ts": "2026-08-19", "sha256": "<of the file>", "type": "proof",
 "file": "proof_dust-mite-remover_001.mp4", "product": "dust-mite-remover",
 "seq": 1, "duration_s": 2.8, "beats": 2, "desc": "<the one line above>"}
```

`ts`, `sha256`, `type` and `file` are required and validated; the rest is what the
generated cards measure, so a record without `duration_s` and `beats` still files
correctly but contributes nothing to the house standard.

## 6. No text in the frame

G6 binds a loop exactly as it binds a still: no words, digits, arrows, cursors,
callouts or price flashes anywhere in frame. Beyond the register argument there is an
operational one that is decisive here — the same asset serves every clone and every
locale of a product (the catalogue runs about 2.6 landing pages per product across
English, German and UK domains), and one English word in the frame destroys that reuse.

The single exception is the motion brief PLATE, which is production-only, carries the
`--brief` suffix, and never reaches a page (G12, ADR-019/020). Since ADR-028 it is not a
render at all: it is generated by `scripts/gen-plate.py`, so no model draws its lettering
and this rule no longer has to be argued against the one artefact that broke it.

## 7. Where the rest of the law lives

- Per-slot verdict, form (`whole-frame` / `inset`) and the four-field generated plate:
  `query/runbook.md` Step 5c and `registry/rules.md` G12.
- How many loops a page may carry, and how a shortfall is filled:
  `query/runbook.md` Step 5d.
- The ledger's record shape: `ingestion/gifs.jsonl`, append-only (SPEC §2).
