# GIF library — the one instruction every type inherits

Shared law for the GIF library (ADR-023). A type file in `registry/gif-types/` states
only what is TRUE OF THAT TYPE; everything below is true of all of them and is never
restated in a type file, the same way types reference `registry/rules.md` by ID rather
than copying rule text (SPEC §5).

The folder cards an editor reads are GENERATED from the type files by
`python3 scripts/gen-gif-cards.py`. A card inside the library folder is never edited by
hand — it is a view, exactly as `registry/index.yaml` is a view. Each folder carries two:
`README.md` in English, built from the first sentence of each section of the type file so it
cannot drift from the law, and `README.vi.md` in Vietnamese, whose copy is authored in
`registry/gif-cards-vi.md` (ADR-044).

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
{page-type}-{product-slug}-v{NN}-{slot-id}.mp4
```

`advertorial-seat-cushion-l-shaped-v04-content-items-3-image.mp4`. It is the routing session's
own directory name — `{page-type}-{product-slug}-v{NN}` (ADR-034) — with the SLOT appended, its
dots turned to dashes, so a reader gets the product, the page of that product and the exact slot
the loop fills without opening anything (ADR-051).

The gif TYPE is not in the name. It lives in `gif.type_id`, which decides the library folder and
always did. Between ADR-037 and ADR-051 the name carried the type instead of the slot, and what
that bought — the argument readable from the filename — is paid for now by the folder the file
sits in.

**A loop has ONE name.** ADR-023 gave it two, a page-side name and a library name, because the
page numbered by slot and the library numbered by type through a sequence the ledger issued. The
sequence is gone for good and has not come back; the slot has, and one name is unique on both
sides at once, so `ingestion/gifs.jsonl` records the same string the routing commissioned.
Nothing has to be mapped through the sha256 to know that two references are the same file.

**What makes it unique is the slot, which is a field again** (ADR-051). A slot id is unique on a
page by construction, so no rule has to protect the filename. At most one loop per gif type per
page survives as a PREFERENCE rather than a rule: a page making the same kind of motion argument
twice is usually repeating itself, so prefer two different arguments where the copy offers them,
and record the call in `motion.notes` where it does not.

The page id is deliberately absent. It identifies the source export rather than the loop, it
lives in `prompts.json.page_id`, and one routed session has none at all — a name that depended
on it could not have been written. A file is never renamed after it enters the library:
briefs and the ledger both reference it by name.

Delivery is **mp4 or webm**, muted, loop-safe, under the size ceiling (ADR-047, ADR-051). It is
what the editors produce, and a naming law that disagrees with the files arriving is one that
gets ignored rather than followed. Two things follow. Muted is a stated requirement again,
because both containers carry an audio track where WebP could not. And a slot that earns motion
needs its page template to carry a `<video>` with `autoplay`, `muted`, `playsinline` and `loop`,
since a still sits in an `<img>` and neither of these does — the interchangeability ADR-036
bought is a template dependency outside this repo, and adding webm changes nothing about it. The
`.gif` extension names the format the owner asks for in conversation, never the file that ships.

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

- Per-slot verdict, the single `whole-frame` form and the generated plate:
  `query/runbook.md` Step 5c and `registry/rules.md` G12. A loop replaces the WHOLE slot asset;
  no still reserves a layer for one, and every still ships on its own (ADR-051).
- How many loops a page may carry, and how a shortfall is filled:
  `query/runbook.md` Step 5d.
- The ledger's record shape: `ingestion/gifs.jsonl`, append-only (SPEC §2).
