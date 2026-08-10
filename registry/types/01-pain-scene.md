---
id: 01-pain-scene
step: 1
job: pain
device: scene
version: "1.1"
status: active
replaced_by: null
ratios: ["16:9", "5:3", "4:5"]
channels: [paid-social, advertorial]
requires_product_photo: false
generation_mode: single-pass
axes:
  gaze: [candid, confront]
variants: [candid, confront]
exempt_from: [G1, G3, G4]
pairs_with: [06-relief-hero, 06-relief-scene, 04-proof-lockedframe]
never_with: [01-pain-split]
---

# 01-pain-scene

## PURPOSE
Make a cold viewer recognize themselves in a raw, cinematic pain moment — before they
know any product exists. Acting and physical evidence carry the pain; zero graphics.

## TRIGGER
use_when: >
  Cold traffic that does not know the product yet. Advertorial header image,
  Facebook/native ad creative, opening image of a story. Its only job is to make
  the viewer recognize themselves and keep reading. Use --candid for physical
  pain and moments nobody would choose to be seen in; use --confront for
  appearance, self-image and daily-frustration problems where the mirror moment
  IS the moment.
avoid_when: >
  Marketplace galleries, main image, or any position where the product must be
  visible. Cannot sell alone — must be paired with a relief/proof image. Never
  in the same set as 01-pain-split: one speaks pain through graphics, the other
  through acting, and the two philosophies read as two brands.

## SKELETON
```
TYPE: 01-pain-scene v1.1
RATIO: [16:9 / 5:3 / 4:5]
REGISTER: cinematic film still. Single frame. NO graphic overlays of any kind.

[SUBJECT]
[age/gender] in [ordinary specific wardrobe, lived-in not styled],
caught mid-action while [everyday transitional movement], or pausing at
[the moment the problem is noticed],
[hand/body position expressing the symptom],
face showing [genuine involuntary discomfort or frustration: which muscles,
which expression]. Body weight unbalanced, mid-motion, not posed.

[MOMENT RULE]
The action must be a mundane moment anyone lives daily,
not a demonstration of wrong behavior.

[SYMPTOM EVIDENCE — required, see G9]
The symptom must be visible as physical fact in the frame, not only as expression.
Rank the available evidence and use the strongest present:
  1. The symptom itself on the body or object ([visible condition])
  2. Physical residue or debris it produces ([what it leaves behind, and where])
  3. The failed tool the person is holding ([what they tried, still in hand])
  4. Gesture alone (weakest, use only when 1-3 are impossible)
If only gesture is available, at least one object in frame must independently
imply the problem.

[GAZE — set by variant, never mix]
--candid: subject unaware of the camera, gaze on their task or the ground.
--confront: subject looking directly into the lens, holding the viewer's eye.
A half-turned glance reads as a model waiting for direction.

[MIRROR] (optional, --confront only)
A mirror behind or beside the subject showing them from another angle.
Gives a natural reason for the confrontation moment and doubles the symptom
evidence without adding a second person.
The reflection must be consistent with the subject's actual position.

[ENVIRONMENT]
[specific ordinary place tied to the moment the problem is noticed],
[time of day], [seasonal or temporal marker].
Real lived-in clutter that belongs to that place and independently signals
the routine being disrupted: [3-4 mundane objects].
Nothing styled, nothing arranged, nothing removed to tidy the frame.

[LIGHT — set by variant]
--candid: low-key. Key light: [source, direction, color temperature].
  Fill: [weaker source]. Rim light separating subject from background.
  Deep shadow across [X%] of the frame.
--confront: even ambient daylight, bright, minimal shadow, flat and unflattering.
Both variants stay desaturated. Neither may use warm flattering light.

[GRADE]
Desaturated [dominant hue] palette, fine film grain, shallow depth of field,
[lens character]. Crushed blacks for --candid.
NO saturated colors. NO red anywhere in the frame.

[FORBIDDEN]
No product. No overlays, arrows, badges, glows, hotspots, insets or split panels.
Nothing that signals advertising.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
NO text, no logo, no watermark.
```

## SLOT CONSTRAINTS
- [SYMPTOM EVIDENCE] is mandatory (G9). Expression alone carries nothing.
- No red pixel anywhere — this type replaces the red pain signal with acting; adding a
  red glow makes the image confess it is an ad.
- [ENVIRONMENT] specificity is the only defense against the "stock photo of back pain"
  failure mode. Generic = dead.

## NEGATIVE
```
[G6] + red glow, pain hotspots, graphic overlay, arrows, badges, split panel,
white background, studio lighting, stock photo look, posed model, fake grimace,
smiling, clean staged interior, saturated colors, advertising composition,
product placement
```

## VARIANTS
### --candid (default)
- Gaze: unaware. Light: low-key. Problem class: physical pain, physical limitation.
- Channels: paid-social, advertorial header. Reads cinematic, survives being scrolled past.
- Negative additions: `bright airy lighting, flat daylight look, looking at camera`

### --confront
- Gaze: direct into the lens. Light: even ambient daylight, legible at thumbnail size.
- Problem class: appearance, self-image, daily frustration.
- Channels: advertorial body, landing-page.
- May use the optional [MIRROR] slot.
- Restraint rule: frustration, not drama — the flatter the face, the truer it reads.
- Negative additions: `golden hour, warm flattering light, exaggerated grimace, theatrical anger`

## WORKED EXAMPLES
### example: mouth-tape-candid — skeleton@1.1, run: untested
```
A cinematic film still, 5:3 ratio. Single frame. NO graphic overlays of any kind.

SUBJECT: A man in his late 30s in a worn grey t-shirt, caught mid-action sitting up on
the edge of an unmade bed in the middle of the night, feet on the floor, shoulders
slumped forward, one hand braced on the mattress, the other reaching for the nightstand.
Unaware of the camera, gaze down and unfocused. Face showing genuine involuntary
exhaustion: eyes heavy and half open, deep creases beneath them, lips dry and parted,
jaw slack.

SYMPTOM EVIDENCE, must be visible as physical fact: an almost empty glass of water on
the nightstand with a second empty glass beside it, the pillow deeply creased and shoved
to one side, the duvet kicked into a tangle at the foot of the bed, a phone face-up on
the nightstand casting a small cold glow. These objects independently signal a night
that has been interrupted more than once.

MOMENT RULE: this is the ordinary act of waking again at 3am, not a demonstration of
wrong behaviour.

ENVIRONMENT: A small suburban bedroom, deep night, curtains half drawn, a chair in the
corner with clothes over the back. Real lived-in clutter, nothing styled, nothing
arranged, nothing removed to tidy the frame.

LIGHT: Low-key. Key light: cold blue streetlight through the gap in the curtains from
behind and to the left. Fill: faint warm glow from a hallway door left ajar. Rim light
along his shoulder and jaw separating him from the dark wall. Deep shadow across most
of the frame.

GRADE: Desaturated blue-grey palette, crushed blacks, fine film grain, shallow depth of
field, 35mm lens character. NO saturated colors. NO red anywhere in the frame.

FORBIDDEN: No product. No overlays, arrows, badges, glows, hotspots, insets or split
panels. Nothing that signals advertising.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
NO text, no logo, no watermark.
```
Predicted failure: the two glasses may collapse into one, losing the "repeats every
night" layer. Fallback evidence: a water-ring stain on the nightstand (carries
repetition in a single object).

### example: knife-sharpener-confront — skeleton@1.1, run: untested
```
A cinematic film still, 5:3 ratio. Single frame. NO graphic overlays of any kind.

SUBJECT: A woman in her early 40s in a plain t-shirt and an apron, standing at a
kitchen counter, turned toward the camera and looking directly into the lens, holding
the viewer's eye. She holds a knife loosely in one hand, the other hand raised slightly
in a small gesture of giving up. Face showing genuine everyday frustration: brow drawn
together, mouth pressed flat and slightly turned down, chin tucked, the look of someone
who has been fighting this for ten minutes.

SYMPTOM EVIDENCE, must be visible as physical fact: on the board in front of her, a
tomato mangled into thick uneven wedges, its skin torn and juice and seeds spread
across the wood. Beside it, a second half-crushed tomato pushed aside. A cheap
pull-through sharpener sits on the counter, clearly already tried and abandoned. A dish
towel bunched under her wrist.

MOMENT RULE: this is the ordinary act of stopping mid-task because the tool will not do
its job, not a demonstration of wrong technique.

ENVIRONMENT: A small ordinary home kitchen, mid-morning, worn wooden counter, an open
drawer behind her with utensils visible, a chopping board leaning against the tiles,
dishes stacked in the sink. Real lived-in clutter, nothing styled, nothing arranged,
nothing removed to tidy the frame.

LIGHT: Even ambient daylight from a window to the left, bright, minimal shadow, flat
and unflattering. No golden hour, no rim light, no drama.

GRADE: Desaturated neutral palette, muted greens and greys, fine film grain, moderate
depth of field, 35mm lens character. NO saturated colors. NO red glow or highlight
anywhere; the tomato is the only red and it must read as ordinary food color.

FORBIDDEN: No hero product. No overlays, arrows, badges, glows, hotspots, insets or
split panels. Nothing that signals advertising.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
NO text, no logo, no watermark.
```
Predicted failures: (1) knife-in-hand + direct gaze may trip safety filters or read as
threatening — fallback: knife down on the board, both hands braced on the counter;
(2) frustration drifting into theatrical anger — the variant lives on restraint.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.1 (2026-08-10): SYMPTOM EVIDENCE made required (→G9); GAZE and LIGHT split into
  per-variant conditionals; [MIRROR] slot added; environment clutter law tightened.
  Evidence: seed conversation.md (bathroom-mirror confront exemplar confirmed the
  Test F prediction that gesture alone cannot carry an invisible symptom).
- 1.0 (2026-08-10): initial from the garage car-exit exemplar. seed: conversation.md.
