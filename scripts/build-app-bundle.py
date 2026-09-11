#!/usr/bin/env python3
"""Generate the app bundle — the library as a consuming app receives it.

The app vendors a copy of the library. A copy shaped by hand is how a rule and
its documentation drift, and the drift is invisible because nothing compares the
two. This makes the copy a GENERATED artifact instead: the reduction is code,
reviewable in a diff, and every file carries a sha256 in the manifest so a stale
vendor directory is a hash mismatch rather than a silent wrong answer.

**The routing surface is shipped whole, not slimmed.** `registry/index.yaml` is
already the slim view — it exists precisely so routing never opens a type file
(SPEC invariant 2), and it is 17k characters. A second reduction on top of it
saves nothing measurable and drops fields the runbook's own cross-slot rules
need: `status`, `requires_pair`, `avoid_adjacent` and `generation_mode` between
them decide whether a routed SET is legal at all, and a Call 1 that cannot see
them can emit a set that is legal slot by slot and broken as a page.

Usage:
  python3 scripts/build-app-bundle.py             # write dist/app-bundle/
  python3 scripts/build-app-bundle.py --out DIR   # write somewhere else
  python3 scripts/build-app-bundle.py --check     # fail if the bundle is stale
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUT = os.path.join(ROOT, "dist", "app-bundle")

# What the app needs, grouped by the call that reads it. Adding a file here is a
# deliberate act: the bundle is the app's whole view of the library, so anything
# missing is a rule the app cannot apply and will silently skip.
#
# TWO NAMESPACES ARE DELIBERATELY ABSENT, and the reasons differ. Written here
# because the absence is otherwise indistinguishable from an oversight — a
# dev-readiness audit on 2026-09-11 read it as exactly that.
#
#   registry/toplist-types/  — outside this bundle because it is outside the QUERY
#       operation. SPEC 3.7: its input is the `product` block, not content.json.
#       SPEC 1 now carries it as a fifth operation, LEDE. gif types ARE here by
#       contrast because gif suggestion is a STEP of QUERY (runbook Step 5c/5d),
#       so a page routed from content.json gets gif verdicts and needs the law.
#       Ship toplist the day an app implements LEDE, and not before.
#
#   registry/pdp-dr-types/   — INSIDE QUERY (SPEC 3.8), and needs no path of its
#       own: promotion out of that namespace is a `git mv` into registry/types/,
#       so a promoted type enters index.yaml and this bundle by itself. Nothing is
#       missing today because nothing there routes. What WILL need adding when the
#       first type promotes is registry/pdp-dr-instruction.md, which carries law
#       that registry/rules.md does not — the G3 split, the substantiation models,
#       the compatibility-bar question.
FILES = {
    # Call 1 — route and plan. Nothing else may be opened at this stage.
    "route": [
        "registry/index.yaml",
        "mapping/slot-rules.md",
    ],
    # Call 2 — fill. The selected type file plus the law it references by ID.
    "fill": [
        "registry/rules.md",
        "registry/argument-faults.md",
        "adapters/nano-banana.md",
    ],
    # Closed lists and contracts. The app validates its own output against these.
    "contract": [
        "registry/vocabulary.yaml",
        "mapping/content.schema.json",
        "query/output.schema.json",
        "query/runbook.md",
        "SPEC.md",
    ],
    # Motion. The gif registry and the law shared by every gif type.
    "gif": [
        "registry/gif-instruction.md",
    ],
}
DIRS = [
    ("registry/types", "types", ".md"),
    ("registry/gif-types", "gif-types", ".md"),
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git(*args):
    try:
        return subprocess.run(["git", "-C", ROOT, *args], capture_output=True,
                              text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def registry_version():
    with open(os.path.join(ROOT, "registry", "vocabulary.yaml"), encoding="utf-8") as f:
        for line in f:
            if line.startswith("registry_version:"):
                return line.split(":", 1)[1].strip().strip('"')
    return ""


def collect():
    """[(source path relative to ROOT, path inside the bundle, group)]"""
    out = []
    for group, rels in FILES.items():
        for rel in rels:
            out.append((rel, os.path.basename(rel), group))
    for src_dir, dest_dir, ext in DIRS:
        d = os.path.join(ROOT, src_dir)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if fn.endswith(ext) and not fn.startswith("_") and fn != "README.md":
                out.append((f"{src_dir}/{fn}", f"{dest_dir}/{fn}",
                            "gif" if "gif" in src_dir else "fill"))
    return out


def sources_dirty(items):
    """True when a file this bundle VENDORS is uncommitted.

    Scoped deliberately. The flag's whole job is to tell a vendoring app that the
    sources behind this copy were uncommitted, and a dirty file the bundle does
    not carry says nothing about that. Unscoped, the check was
    `git status --porcelain` over the whole tree, so any parallel lane — another
    session's owner-gated type pass, an unreviewed prompt set — marked every
    bundle DIRTY TREE and the flag stopped carrying information. Measured
    2026-09-11: four consecutive bundle commits reported dirty on account of one
    unrelated toplist lane that touched no bundled file.

    Paths are the sources, not the destinations: `registry/types/03-spec-macro.md`
    rather than `types/03-spec-macro.md`, plus the source directories themselves so
    a NEW or DELETED file in one counts.
    """
    paths = sorted({src for src, _dest, _group in items})
    paths += [src_dir for src_dir, _dest_dir, _ext in DIRS]
    return bool(git("status", "--porcelain", "--", *paths))


def build(out_dir, write=True):
    items = collect()
    manifest = {
        "registry_version": registry_version(),
        "source_commit": git("rev-parse", "HEAD"),
        "source_dirty": sources_dirty(items),
        "note": "Generated by scripts/build-app-bundle.py. Never hand-edit a file "
                "in this directory — edit the source in the repo and regenerate. "
                "The app compares source_commit and the per-file sha256 against "
                "what it vendored; a mismatch means the vendor copy is stale.",
        "files": {},
    }
    missing = []
    for rel, dest, group in items:
        src = os.path.join(ROOT, rel)
        if not os.path.exists(src):
            missing.append(rel)
            continue
        manifest["files"][dest] = {"from": rel, "group": group,
                                   "sha256": sha256(src),
                                   "bytes": os.path.getsize(src)}
        if write:
            target = os.path.join(out_dir, dest)
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copyfile(src, target)
    if write:
        os.makedirs(out_dir, exist_ok=True)
        pruned = prune(out_dir, manifest)
        with open(os.path.join(out_dir, "MANIFEST.json"), "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            f.write("\n")
        manifest["_pruned"] = pruned
    return manifest, missing


def prune(out_dir, manifest):
    """Delete anything in the bundle that no longer has a source.

    The build only ever COPIED, so a file removed or renamed in registry/types/
    stayed in dist/app-bundle/types/ forever — and the manifest did not list it,
    because the manifest is built from the sources. An unlisted orphan is the
    exact failure this bundle's header says it exists to prevent: drift that is
    invisible because nothing compares the two copies. An app that enumerates the
    directory rather than reading the manifest would load a type the library has
    retired.

    Found on 2026-09-11 by leaking a test fixture into a commit, which is a poor
    way to find it and the only way it had been found in 34 builds.
    """
    keep = set(manifest["files"]) | {"MANIFEST.json"}
    removed = []
    for dirpath, _dirnames, filenames in os.walk(out_dir):
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, out_dir)
            if rel not in keep:
                os.remove(full)
                removed.append(rel)
    return sorted(removed)


def main(argv):
    out_dir = DEFAULT_OUT
    if "--out" in argv:
        out_dir = os.path.abspath(argv[argv.index("--out") + 1])
    check = "--check" in argv

    if check:
        fresh, missing = build(out_dir, write=False)
        mpath = os.path.join(out_dir, "MANIFEST.json")
        if not os.path.exists(mpath):
            print(f"ERROR {out_dir}: no MANIFEST.json — run without --check")
            return 1
        with open(mpath, encoding="utf-8") as f:
            have = json.load(f)
        stale = []
        for dest, meta in fresh["files"].items():
            got = have["files"].get(dest)
            if not got:
                stale.append(f"{dest}: missing from the bundle")
                continue
            if got["sha256"] != meta["sha256"]:
                stale.append(f"{dest}: sha256 differs from source")
            # The manifest is a claim about files on disk, so check the disk and
            # not only the claim. Comparing manifest to manifest passed a bundle
            # with a deleted file, which is the failure this whole script exists
            # to prevent.
            onfile = os.path.join(out_dir, dest)
            if not os.path.exists(onfile):
                stale.append(f"{dest}: listed in MANIFEST.json but not on disk")
            elif sha256(onfile) != meta["sha256"]:
                stale.append(f"{dest}: the copy on disk does not match its source")
        for dest in have["files"]:
            if dest not in fresh["files"]:
                stale.append(f"{dest}: in the bundle but no longer in the repo")
        for s in stale:
            print(f"ERROR dist/app-bundle/{s}")
        if missing:
            for m in missing:
                print(f"ERROR {m}: listed in the bundle but not in the repo")
        print(f"bundle check: {len(fresh['files'])} files, {len(stale)} stale, "
              f"{len(missing)} missing")
        return 1 if (stale or missing) else 0

    manifest, missing = build(out_dir, write=True)
    for m in missing:
        print(f"ERROR {m}: listed in the bundle but not in the repo")
    by_group = {}
    for meta in manifest["files"].values():
        by_group[meta["group"]] = by_group.get(meta["group"], 0) + 1
    total = sum(m["bytes"] for m in manifest["files"].values())
    print(f"wrote {len(manifest['files'])} files ({total} bytes) to {out_dir}")
    print("  " + " · ".join(f"{g}: {n}" for g, n in sorted(by_group.items())))
    print(f"  registry_version {manifest['registry_version']} · commit "
          f"{manifest['source_commit'][:7]}"
          f"{' (DIRTY TREE — regenerate after committing)' if manifest['source_dirty'] else ''}")
    for rel in manifest.get("_pruned") or []:
        print(f"  PRUNED {rel} — no source; it had been orphaned in the bundle")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
