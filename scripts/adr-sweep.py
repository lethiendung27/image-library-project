#!/usr/bin/env python3
"""Sweep the repo for a term an ADR is about to ban, rename or retire.

WHY THIS IS A TOOL AND NOT A VALIDATOR CHECK
--------------------------------------------
Twice now a decision was made and the files that TEACH the opposite were left
standing: ADR-020 found a superseded premise still living in a schema
description and a runbook paragraph, and ADR-039 found the multi-pass ban still
being taught by `runbook.md` Step 6, `adapters/nano-banana.md` Rule 3 and
`query/output.schema.json` — three days and eleven ADRs after the ban.

A gate cannot catch this. The banned term legitimately appears in 32 files: the
decision log records it, the render ledger has historical verdicts, type files
declare `generation_mode: multi-pass` as a true statement about what a PICTURE
needs, and `CLAUDE.md` states the ban itself. What went wrong was never that the
string existed — it was that a file gave an INSTRUCTION the ban forbids, and no
regular expression separates "emit steps[]" from "steps[] is retired".

So this is a checklist generator, run by a person at the moment they write an
ADR's Consequences list. That list is a claim about blast radius, and nothing
verifies it; this makes the claim cheap to check instead of cheap to skip.

Usage:
  python3 scripts/adr-sweep.py multi-pass
  python3 scripts/adr-sweep.py "animate the supplied" --context
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Files that INSTRUCT. A hit here is a thing somebody will do — read every one.
TEACHES = (
    "CLAUDE.md", "SPEC.md",
    "query/runbook.md", "query/output.schema.json",
    "mapping/", "adapters/", "registry/rules.md", "registry/vocabulary.yaml",
    "registry/types/", "registry/gif-types/", "registry/gif-instruction.md",
    "registry/argument-faults.md",
    "ingestion/runbooks/", "eval/render-test.md",
)

# Files that RECORD. A hit here is history and is expected to stay.
RECORDS = (
    "decisions/log.md", "conversation.md",
    "eval/render-tests.jsonl", "ingestion/observations.jsonl",
    "feedback/", "query/sessions/", "scripts/",
    "aif-image-type-registry-v1.2.md", "registry/index.yaml",
)

# Generated. Never edited by hand; regenerating is the whole fix.
GENERATED = ("dist/", "registry/index.yaml")


def classify(path):
    if any(path.startswith(p) for p in GENERATED):
        return "GENERATED"
    if any(path.startswith(p) for p in TEACHES):
        return "TEACHES"
    if any(path.startswith(p) for p in RECORDS):
        return "RECORDS"
    return "UNCLASSIFIED"


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    term = argv[0]
    want_context = "--context" in argv[1:]

    try:
        out = subprocess.run(
            ["git", "grep", "-n", "-I", "--fixed-strings", term],
            cwd=ROOT, capture_output=True, text=True).stdout
    except FileNotFoundError:
        print("git not available")
        return 2

    hits = {}
    for line in out.splitlines():
        parts = line.split(":", 2)
        if len(parts) < 3:
            continue
        path, lineno, text = parts
        hits.setdefault(path, []).append((lineno, text.strip()))

    if not hits:
        print(f"no tracked file contains {term!r}")
        return 0

    buckets = {"TEACHES": [], "RECORDS": [], "GENERATED": [],
               "UNCLASSIFIED": []}
    for path in sorted(hits):
        buckets[classify(path)].append(path)

    total = sum(len(v) for v in hits.values())
    print(f"{term!r}: {total} hit(s) across {len(hits)} tracked file(s)\n")

    order = ("TEACHES", "UNCLASSIFIED", "GENERATED", "RECORDS")
    note = {
        "TEACHES": "READ EVERY ONE. A hit here is an instruction somebody "
                   "will follow. This is the bucket both ADR-020 and ADR-039 "
                   "missed.",
        "UNCLASSIFIED": "Not in either list — classify it, then extend this "
                        "script's TEACHES/RECORDS tuples.",
        "GENERATED": "Regenerate rather than edit. Rebuilding is the fix.",
        "RECORDS": "History. Expected to keep the term; do not rewrite.",
    }
    for bucket in order:
        paths = buckets[bucket]
        if not paths:
            continue
        print(f"── {bucket} ({len(paths)} file(s)) — {note[bucket]}")
        for path in paths:
            n = len(hits[path])
            print(f"     {path}  ({n} hit{'s' if n != 1 else ''})")
            if want_context or bucket in ("TEACHES", "UNCLASSIFIED"):
                for lineno, text in hits[path][:4]:
                    print(f"        {lineno}: {text[:104]}")
                if n > 4:
                    print(f"        … {n - 4} more")
        print()

    teaching = len(buckets["TEACHES"]) + len(buckets["UNCLASSIFIED"])
    print(f"Account for {teaching} teaching file(s) in the ADR's Consequences "
          f"list, or say why each is left standing.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
