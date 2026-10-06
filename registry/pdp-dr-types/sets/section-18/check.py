"""Check section-18 against `03-spec-overlay` v0.19 — ADR-136, on a product with no photograph.

This set is three alternatives for each of two slots, so it is not checked for form spread or for a
control. What it is checked for is the four things ADR-136 decided and the one ADR-131 did:

  STEP 0   every frame states its SUBJECT as the thing the product DELIVERS, in the set's own
           words. A frame that stops at a hand holding a product is what ADR-136 was written about.
  WORDS    SIX of six carry no lettering at all, and no frame quotes a drawn string. The page
           prints the block title, the body and the pill; `section-16` drew the pill into 11 of 11.
  CUE      every frame still carries exactly ONE cue (ADR-135), and no frame carries a symbol of
           the medium - a loop arrow, a filmstrip, a memory card, a bird's-eye composite - where
           the claim is about a hidden state (ADR-136 decision 6).
  GROUND   no frame is dark. A cabin interior is the easiest place in this library to lose a
           picture to shadow.
  ANATOMY  no prompt names anything on the product beyond the three parts the page and the brief
           actually source: the hub, the rear camera module, the built-in screen (ADR-131).

The type's own clauses are READ OUT OF THE TYPE FILE, so a law reworded again fails this set
instead of leaving it quietly stale.

Usage, from the repo root: python3 registry/pdp-dr-types/sets/section-18/check.py [prompts.md]
Exits 1 on any failure.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
PATH = os.path.join(HERE, "prompts.md")
TYPE = os.path.join(ROOT, "registry", "pdp-dr-types", "03-spec-overlay.md")
text = io.open(sys.argv[1] if len(sys.argv) > 1 else PATH, encoding="utf-8").read()
law = io.open(TYPE, encoding="utf-8").read()

GATE = 1800
OPEN = "Editorial realism product feature image"
PRODUCT = "360 Surround View 4 Channel Dash Cam"
G1 = "Use the attached product photo as the exact reference."
G6 = "Any screen shows only a picture, with no interface, text or numbers."
SILENT = "Nothing in the picture carries any lettering."
AD = ("The art direction is the real place in open daylight, bright enough to read the moulding on "
      "the product, and the picture keeps the colour of its own world.")
READ_HUB = ("The hub is sharp, lit and unobstructed, nameable where it sits, and it is not required "
            "to be the largest thing in the picture.")
READ_MOD = ("The module is sharp, lit and unobstructed, nameable where it sits, and it is not "
            "required to be the largest thing in the picture.")

SUBJECT = {
    1: "The subject of this frame is the moment of contact",
    2: "The subject of this frame is the van at the moment it crosses the line",
    3: "The subject of this frame is the car behind at the moment it dips",
    4: "The subject of this frame is the recording already running, unasked.",
    5: "The subject of this frame is what is already on the card.",
    6: "The subject of this frame is its built-in screen",
}
CUE = {
    1: "One thin white line icon of a closed padlock stands beside the hub",
    2: "That agreement between window and screen is the only cue, and nothing is drawn.",
    3: "One thin white line icon of a shield stands beside the module",
    4: "That agreement between window and screen is the only cue, and nothing is drawn.",
    5: "A clean circular inset, about a third of the picture wide, floats beside the hub",
    6: "That sharpness is the only cue, and nothing is drawn.",
}
SCREEN_FRAMES = (2, 4, 5, 6)   # frames in which the built-in screen appears, so G6 rides along
MODULE_FRAME = 3

BANNED = {
    "a symbol of the medium where the claim is a hidden state":
        r"(?i)\b(loop arrow|filmstrip|film strip|memory card|sd card|bird's-eye|composite|timeline|progress bar)\b",
    "a dark ground": r"(?i)\b(dark studio|near-black|dim|moody|low[- ]key|at night|unlit)\b",
    "anatomy no photograph on disk supports":
        r"(?i)\b(lenses|lens cluster|status lamp|indicator lamp|led ring|port|bezel|matte black|glossy)\b",
    "a drawn mark on the product": r"(?i)drawn on the (hub|module|screen|glass)\b(?! itself)",
    "a badge or a chip, which step 8 bans": r"(?i)\b(badge|chip|banner|ribbon)\b",
    # no trailing \b: a degree sign is not a word character, so "120°" never closed one and the
    # pattern silently matched nothing. knownbad.py caught it.
    "a figure the block's copy does not pay for":
        r"\b\d+(\.\d+)?\s?(°|p\b|mm\b|cm\b|g\b|m\b|MP\b|GB\b|hours?\b)",
}

fails = []


def need(cond, msg):
    if not cond:
        fails.append(msg)


blocks = re.findall(r"```\n(.*?)\n```", text, re.S)
need(len(blocks) == 6, f"expected 6 prompts, found {len(blocks)}")

for i, p in enumerate(blocks, 1):
    tag = f"prompt {i}"
    need(len(p) <= GATE, f"{tag}: {len(p)} characters, over the {GATE} gate")
    need(p.startswith(OPEN), f"{tag}: does not open with '{OPEN}'")
    need(PRODUCT in p, f"{tag}: does not name the {PRODUCT}")
    need(p.endswith(G1), f"{tag}: does not close with G1")
    need(AD in p, f"{tag}: missing the art-direction clause in the set's one wording")
    need(SILENT in p, f"{tag}: missing the no-lettering clause")
    need('"' not in p, f"{tag}: quotes a drawn string in a frame that carries no lettering")
    need(SUBJECT[i] in p, f"{tag}: does not state its SUBJECT in the set's words (step 0)")
    need(CUE[i] in p, f"{tag}: missing its one cue - expected '{CUE[i][:46]}...'")
    need((READ_MOD if i == MODULE_FRAME else READ_HUB) in p,
         f"{tag}: missing the readable-not-largest clause (ADR-136 decision 2)")
    need((G6 in p) == (i in SCREEN_FRAMES),
         f"{tag}: the screen sentence present={G6 in p}, this frame says {i in SCREEN_FRAMES}")
    # BANNED maps a description to its pattern, not the other way round: the first draft of this
    # loop read them reversed and searched the prompts for the descriptions, so six mutations
    # walked straight through a checker that printed PASS. knownbad.py is what found it.
    for why, pat in BANNED.items():
        m = re.search(pat, p)
        need(not m, f"{tag}: carries {m.group(0)!r} - {why}" if m else "")

# the set as a whole
need(not re.search(r'[Tt]he words "', text.split("```")[0] or ""), "set: the notes promise lettering")
lettered = [i for i, p in enumerate(blocks, 1) if re.search(r'[Tt]he words "', p)]
need(not lettered, f"set: lettering found at {lettered}; this set letters in none (ADR-136 decision 5)")
need(len({SUBJECT[i] for i in SUBJECT}) == 6, "set: two frames share a subject")

# the law this set claims to follow must still say what the set says it says
need('version: "0.19"' in law, "type: 03-spec-overlay is not at 0.19 - this set was written for it")
for clause in ("OBJECT claim or a DELIVERY claim",
               "most READABLE thing in the frame, not necessarily the largest",
               "never restates a word the page already prints",
               "read off the PRODUCT, never chosen as a style",
               "WINDOW onto the hidden state"):
    need(clause in law, f"type: the clause '{clause[:40]}...' is gone from 03-spec-overlay.md")

fails = [f for f in fails if f]
if fails:
    print(f"FAIL  {len(fails)} problem(s) in section-18")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print(f"PASS  section-18: {len(blocks)} prompts, 6 silent, 0 dark, "
      f"longest {max(len(p) for p in blocks)} characters")
