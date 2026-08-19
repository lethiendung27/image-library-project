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

## Hard rules for any session

1. Never hand-edit a generated view — regenerate it. `registry/index.yaml`:
   `python3 scripts/validate.py --write-index`. The GIF library's folder cards:
   `python3 scripts/gen-gif-cards.py`. A session's motion brief plates:
   `python3 scripts/gen-plate.py`. The app bundle:
   `python3 scripts/build-app-bundle.py` (run it in the same commit as any change
   under `registry/`, `mapping/`, `adapters/` or the schemas).
2. After **any** edit under `registry/`, run `python3 scripts/validate.py` and fix
   errors before finishing the turn.
3. `ingestion/observations.jsonl` and `feedback/picks.jsonl` are append-only.
4. `registry/types/_staging/` is never routable; promotion criteria are in `SPEC.md` §6.3.
5. All artifact content is **English**. Conversation with the user is Vietnamese.
6. Never commit source images; reference them by sha256 (SPEC §6.4).
6b. **Every delivered prompt is paste-and-run**: one prompt, one generation call, at
   most one reference photo the owner attaches in the tool. Never emit a `multi-pass`
   option, an edit chain or a post-assembly step — take the type's own single-pass
   route, and where it has none, route to the next candidate and say so. ADR-021,
   declared in `query/runbook.md` Step 3 and enforced by `scripts/validate.py`.
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
