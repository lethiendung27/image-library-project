# CLAUDE.md — thin adapter

This repo is a **data library, not an app**. The source of truth for structure and
procedure is `SPEC.md` — read it before changing anything. This file only maps common
tasks to entry points and must stay logic-free.

## Entry points

| Task | Follow |
|---|---|
| Classify a batch of new images | `ingestion/runbooks/classify-batch.md` |
| Classify ONE image with per-step review | `ingestion/runbooks/classify-batch.md` → Interactive mode |
| Curate ledger into patches / staging types | `ingestion/runbooks/curate.md` |
| Calibrate classifier drift | `ingestion/runbooks/calibrate.md` |
| Generate prompts for a landing page | `query/runbook.md` |
| Render-test a skeleton on a real product | `eval/render-test.md` |
| Add / edit an image type | `SPEC.md` §3, then a file in `registry/types/` |
| File new GIFs into the library | `registry/gif-instruction.md` |
| Add / edit a GIF type | `SPEC.md` §3.6, then a file in `registry/gif-types/` |
| Choose the lede image for a top-N listicle | `registry/toplist-instruction.md`, then `mapping/toplist-rules.md` |
| Add / edit a toplist type | `SPEC.md` §3.7, then a file in `registry/toplist-types/` |
| Route images for an LP2 product-gallery page | `registry/pdp-dr-instruction.md`, then `mapping/pdp-dr-rules.md` |
| Read an LP2 template's image slots | `python3 scripts/pdp-dr-slots.py TEMPLATE.html`, then `mapping/pdp-dr-rules.md` → Slot kinds |
| Add / edit a PDP-DR type | `SPEC.md` §3.8, then a file in `registry/pdp-dr-types/` |

## Hard rules for any session

1. Never hand-edit a generated view — regenerate it. `registry/index.yaml` and
   `registry/pdp-dr-index.yaml`: `python3 scripts/validate.py --write-index`. The GIF
   library's folder cards: `python3 scripts/gen-gif-cards.py`. A session's motion brief
   plates: `python3 scripts/gen-plate.py`. The app bundle:
   `python3 scripts/build-app-bundle.py` (run it in the same commit as any change
   under `registry/`, `mapping/`, `adapters/` or the schemas).
2. After **any** edit under `registry/`, run `python3 scripts/validate.py` and fix
   errors before finishing the turn.
3. `ingestion/observations.jsonl` and `feedback/picks.jsonl` are append-only.
4. `registry/types/_staging/` is never routable; promotion criteria are in `SPEC.md` §6.3.
   The same holds for a file in `registry/pdp-dr-types/` whose `status` is `reserved` — it
   owes a `blocked_by` and a `BLOCK` section naming what it waits on, and it is promoted in
   place, never by `git mv` (SPEC §3.8). That folder is the ONE an LP2 page routes: LP2's
   drafts beside a verbatim copy of every active `registry/types/` file, each declaring
   `copied_from` (ADR-091).
5. All artifact content is **English**. Conversation with the user is Vietnamese.
   ONE named exception: the GIF library's Vietnamese folder cards, whose copy lives in
   `registry/gif-cards-vi.md` and which `scripts/gen-gif-cards.py` writes as
   `README.vi.md`. Their reader is an editor filing files, not a harness reading law,
   and everything that BINDS is still English in `registry/gif-types/`. SPEC §3.6,
   ADR-044; `scripts/validate.py` fails a gif type with no entry there.
6. Never commit source images; reference them by sha256 (SPEC §6.4).
6b. **Every delivered prompt is paste-and-run**: one prompt, one generation call, and
   as many reference photos as the type needs — one per product in frame. Never emit a
   `multi-pass` option, an edit chain or a post-assembly step. The COUNT of attachments
   stopped being capped at one on 2026-09-09 (ADR-076); the one CALL did not, and it is
   the call that made the rule. Where a prompt needs more attachments than the owner's
   app takes, it still ships in full and is rendered elsewhere. ADR-021 and ADR-076,
   declared in `query/runbook.md` Step 3.
6c. **Before writing an ADR's Consequences list, sweep for what it bans**:
   `python3 scripts/adr-sweep.py "<term>"`. That list is a claim about blast radius
   and nothing verifies it, so account for every file the sweep puts in TEACHES or
   say why it stands. Twice a decision landed and the files teaching the opposite
   were left: ADR-020 found it in a schema description and a runbook paragraph,
   ADR-039 found the multi-pass ban still taught by `runbook.md` Step 6, the
   adapter's Rule 3 and `output.schema.json` — three days and eleven ADRs late. No
   gate can catch this: the banned term legitimately lives in the decision log, the
   render ledger and every type that truthfully declares it, and no regular
   expression separates "emit steps[]" from "steps[] is retired". A person reading
   a short classified list is the check.
7. ADR-007 autopilot: after any COMPLETED operation (classify batch, curation pass,
   promotion, render-test logging), run `python3 scripts/validate.py --write-index`;
   on 0 errors, `git commit` that operation immediately — one commit per operation,
   evidence cited in the message, and a `Co-Authored-By` trailer naming the model that
   actually performed the operation (`Claude <model> <noreply@anthropic.com>`) — then
   report the commit hash and revert path.
   Never push. The human gate is the user's explicit inputs (image feeds, picks,
   commands, and verdicts where the user gives them). ADR-011: you may assign a
   verdict `pass|partial|fail` yourself, but ONLY for a render you have actually
   opened and looked at, and never for promotion criterion `SPEC.md` §6.3(3). Never
   invent a verdict for an image you have not seen.
