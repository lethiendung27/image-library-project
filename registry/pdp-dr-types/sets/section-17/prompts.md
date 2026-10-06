# pdp-dr set section-17 — the claim is classified before the frame, and the words come off

**Type:** `03-spec-overlay` v0.19. **Status: UNCOMMITTED, owner-gated.** **Supersedes
`sets/section-16/`**, rendered once: 0 pass, 6 partial, 5 fail.

**Why.** `section-16` met every repair ADR-135 asked for — a cue in 11 of 11, the accent scoped to
the drawn layer, a world behind every ground — and it met the composition floor this type has
legislated since ADR-132: closest pair **30.8** against the owner's own **30.3**. It failed anyway,
and his three sentences say on which axes: *tone tối*, *chưa đẩy lên 1 level khác — visual và
meaning*, *chữ xuất hiện quá nhiều*. **Variety was never what was missing.** ADR-136 names what was,
and this set changes four things and nothing else.

| | `section-16` | `section-17` |
|---|---|---|
| **what the frame is OF** | the tool touching a wire, **11 of 11** | **what the tool DELIVERS** — the break found, the reach, the gap entered — in 5 of 6 |
| **the ground's value** | 5 of 11 at value ≤ 0.22, a black product on a dark ground | **daylight or a bright ground, 6 of 6**; no dark frame in the set |
| **the world's colour** | *unbroken black harness tape*, written into the prompts | **the factory harness in red, yellow, blue and green**, named in every frame that has one |
| **the drawn word** | **11 of 11**, and all 11 restate the pill the page prints beside the image | **1 of 6** — an icon with a label the page does not print — **and the control** |

**What is NOT changed**, because it worked: the eight-step derivation, one message per block, the
visual proof per claim word, the stated hierarchy, one cue per frame, and fidelity to the attached
photograph.

## Step 0, per block — OBJECT or DELIVERY

| block | the page's line | kind | why | what must be photographed |
|---|---|---|---|---|
| **A** *Locate Breaks Without Stripping Wires* | the tone travels the wire and you pinpoint the break | **DELIVERY** | the thing bought is a FINDING, not a part | the break itself, and the distance the tone covers |
| **B** *Trace Through Trim Panels* | you follow it behind a panel that stays on | **DELIVERY** | the thing bought is REACH | the tip inside the gap, and what is behind the gap |
| **C** *Tune Out False Signals Instantly* | you set the level by hand | **OBJECT** | the dial is a real part, and a part is proved by photographing it | the knurled wheel, its printed scale, a thumb mid-turn |

Block C is the control's own evidence: it was the only object claim in `section-16` and it returned
the best frame of the eleven — **36.4** colourfulness at value **0.64** against a round median of
16.2 at 0.20. The two delivery blocks were built the same way and returned **9.3 to 22.7**.

## The six frames

| # | block | kind | art direction | the SUBJECT | the one cue | words |
|---|---|---|---|---|---|---|
| 1 | A | delivery | daylight, engine bay | **the break**, inside the loom | a window: a disc inset beside the loom | none |
| 2 | A | delivery | daylight workshop | **the distance** the tone covers | the product's own indication, both bodies lit | none |
| 3 | B | delivery | daylight, open door | **what is behind the panel**, through the gap | a drawn mark: the tone leaving the gap | none |
| 4 | B | delivery | white seamless | **the panel still whole**, every clip seated | an Apple-style icon callout | `CLIPS SEATED` |
| 5 | C | object | white seamless macro | **the dial**, the thumb mid-turn | the lit scale, isolated | none |
| 6 | B | — | daylight on location | **the product**, as `section-16` built it | the crossed-out screwdriver | `Non Destructive Tracing` |

**Frame 6 is the CONTROL and it is predicted to FAIL.** It is `section-16`'s own construction —
product-led, no output in frame, the page's own pill lettered across it — rebuilt in daylight so
that the LIGHT is held constant and only the CONSTRUCTION differs from frames 1 to 5. If the owner
grades it level with the other five, ADR-136 is wrong and the fault was the darkness alone.

**Watch items**
1. Is the frame's subject the thing the tool DELIVERS, in 1, 2 and 3? A frame that stops at the tool
   touching something is frame 6 by another name.
2. `scripts/frame-colour.py`: is colourfulness toward the owner's 39.1 and value toward 0.46? A
   round below his band fails whatever else it did.
3. `scripts/compo-spread.py` on the six: no pair under 25.
4. Frames 1 to 3 and 5: is the picture entirely free of lettering, and does each still carry its cue?
5. Frame 1: is the disc BESIDE the loom, nothing drawn on the loom itself (ADR-128)?
6. Is the receiver sharp, lit, unobstructed and nameable in every frame — including the ones where
   it is small?

---

## `features.items.0` — Locate Breaks Without Stripping Wires

### 1 — daylight engine bay · the window · no words

```
Editorial realism product feature image in an engine bay in full daylight with the bonnet up: a factory wiring harness runs across the frame, a bundle of red, yellow, blue and green wires in their factory colours bound at intervals by tape bands, and the receiver of the Automotive Circuit Tester — the black pen with the speaker grille, the round TEST button, the knurled side thumbwheel and the gooseneck — is held in a hand with its rounded sensing tip resting on the outside of that bundle at one point. The subject of this frame is the break the tool has found. A clean circular inset, about a third of the picture wide, floats beside the harness in clear air and is joined to that one point by a thin leader: inside the disc the same bundle is seen magnified and in section, the copper strands bright and continuous along their length and one strand ended short in a clean break. Nothing is drawn on the harness itself. The receiver is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. The transmitter, the small black box on red and black clip leads, is clipped to a terminal deeper in the bay with its red lamp lit. The art direction is daylight on location: open sky light, bright enough to read the moulding on the product, and the picture keeps the colour of its own world. Neither body carries a screen, a display or a numeric readout of any kind. Nothing in the picture is cut, stripped, unwrapped or taken apart. Nothing in the picture carries any lettering. Use the attached product photo as the exact reference.
```

### 2 — daylight workshop · the product's own indication · no words

```
Editorial realism product feature image in a daylit workshop with a car's door standing open: a factory wiring harness runs the length of the frame from the fusebox at the far end to the near foreground, a bundle of red, yellow, blue and green wires in their factory colours, and the transmitter, the small black box on red and black clip leads, is clipped to it at the far end with its red lamp lit, small and sharp. The subject of this frame is the distance the tone covers: the length of harness between the two bodies is the longest thing in the picture, carried from deep in the frame to the hand in the foreground. The receiver of the Automotive Circuit Tester — the black pen with the speaker grille, the round TEST button, the knurled side thumbwheel and the gooseneck — is held near the camera with its rounded sensing tip on the near end of that same bundle, and the printed arc of dots on its body is lit and the sharpest detail in the frame. The receiver is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. The art direction is daylight on location: daylight from the open roller door, bright and even, and the picture keeps the colour of its own world. Neither body carries a screen, a display or a numeric readout of any kind. Nothing in the picture is cut, stripped, unwrapped or taken apart. Nothing in the picture carries any lettering. Use the attached product photo as the exact reference.
```

---

## `features.items.1` — Trace Through Trim Panels

### 3 — daylight, open door · the mark in the air · no words

```
Editorial realism product feature image at a car's open door in daylight, framed close: a grained grey kick panel stands with its moulded face unbroken and every fastener still seated in it, and at its edge there is a gap no wider than a finger through which a factory wiring harness is visible behind the panel, a bundle of red, yellow, blue and green wires in their factory colours lit by the daylight coming in. The subject of this frame is what is behind the panel, reached through that gap. The receiver of the Automotive Circuit Tester — the black pen with the speaker grille, the round TEST button, the knurled side thumbwheel and the gooseneck — is held beside the panel with its gooseneck bent into a tight curve so that the rounded sensing tip has gone through the gap and sits among those wires. Short luminous cyan pulses rise out of the gap into the open air and travel the short way to the speaker grille, each one fainter than the one before, and nothing is drawn on the harness or on the panel. The receiver is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. The art direction is daylight on location: daylight through the open door, bright enough to read the moulding on the product, and the picture keeps the colour of its own world. Neither body carries a screen, a display or a numeric readout of any kind. Nothing in the picture is cut, stripped, unwrapped or taken apart. Nothing in the picture carries any lettering. Use the attached product photo as the exact reference.
```

### 4 — white seamless · the icon callout · `CLIPS SEATED`

```
Editorial realism product feature image on a white seamless studio ground: a car's grained grey kick panel stands with its moulded face unbroken and every fastener still seated in it, a short run of factory harness in red, yellow, blue and green wires in their factory colours emerging from behind its lower edge, and the receiver of the Automotive Circuit Tester — the black pen with the speaker grille, the round TEST button, the knurled side thumbwheel and the gooseneck — is held in a hand beside it with its gooseneck bent into a tight curve so that the rounded sensing tip has gone into the narrow gap at the panel's edge. The subject of this frame is the panel still whole with its fasteners in it. One thin white line icon of a trim clip, seated in its hole, stands beside the panel at about a tenth of the picture's height, and the words "CLIPS SEATED" are set once under it in plain bold dark letters on the white ground, the capitals about a twentieth of the picture's height. The receiver is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. The art direction is a white seamless studio: a bright, even key with a soft shadow under the panel, and the picture keeps the colour of its own world. Neither body carries a screen, a display or a numeric readout of any kind. Nothing in the picture is cut, stripped, unwrapped or taken apart. Nothing else in the picture carries any lettering. Use the attached product photo as the exact reference.
```

---

## `features.items.2` — Tune Out False Signals Instantly

### 5 — white seamless macro · the lit scale · no words

```
Editorial realism product feature image on a white seamless studio ground, framed as a macro: the receiver of the Automotive Circuit Tester — the black pen with the speaker grille, the round TEST button, the knurled side thumbwheel and the gooseneck — lies along the frame held in a hand, and a thumb is caught mid-turn on the knurled side thumbwheel. The subject of this frame is the dial: the knurled wheel and the printed arc of dots beside it are the only sharp things in the picture, a specular highlight runs up that scale, and everything else falls away soft. The red and black clip leads of the transmitter lie coiled in the near foreground, their red carrying the only saturated colour in the frame. The receiver is sharp, lit and unobstructed, nameable where it sits, and it is not required to be the largest thing in the picture. The art direction is a white seamless studio: a bright, even key raked from the left so the knurling reads, with a soft shadow under the body, and the picture keeps the colour of its own world. Neither body carries a screen, a display or a numeric readout of any kind. Nothing in the picture is cut, stripped, unwrapped or taken apart. Nothing in the picture carries any lettering. Use the attached product photo as the exact reference.
```

---

## `features.items.1` — the CONTROL

### 6 — daylight on location · the crossed-out screwdriver · `Non Destructive Tracing` · **CONTROL, predicted FAIL**

```
Editorial realism product feature image at a car's open door in daylight: a grained grey kick panel stands with its moulded face unbroken and every fastener still seated in it, and the receiver of the Automotive Circuit Tester — the black pen with the speaker grille, the round TEST button, the knurled side thumbwheel and the gooseneck — is held in a hand beside it with its gooseneck bent into a tight curve so that the rounded sensing tip has gone into the narrow gap at the panel's edge. The hero of this frame is the gooseneck bent into the gap: it is the largest, sharpest and brightest thing in it, and everything else is smaller, softer or darker. One thin white line icon of a screwdriver with a bar struck through it stands beside the words at about a tenth of the picture's height, and nothing else is drawn. The art direction is daylight on location: daylight through the open door, bright enough to read the moulding on the product, and the picture keeps the colour of its own world. Neither body carries a screen, a display or a numeric readout of any kind. Nothing in the picture is cut, stripped, unwrapped or taken apart. The words "Non Destructive Tracing" are set once in plain bold white letters directly on the photograph, carried by a dark halo wide enough to hold them off whatever is behind them, the capitals about a twentieth of the picture's height and the line running between a quarter and a third of its width. Nothing else in the picture carries text. Use the attached product photo as the exact reference.
```

---

## After the render

1. Log six lines in `eval/render-tests.jsonl`, `verdict_by` naming whoever graded them, and grade the
   picture before the prompt that made it (ADR-131).
2. `python3 scripts/frame-colour.py` on all six and `python3 scripts/compo-spread.py` on all six, in
   the ADR, beside the owner's 39.1 / 0.46 / 27.4 / 0.33 and his closest pair of 30.3.
3. **Read frame 6 first.** The control decides what the other five mean.
