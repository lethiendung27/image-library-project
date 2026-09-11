---
id: lede-inuse
version: "0.15"
status: active
replaced_by: null
products_in_frame: one
requires_product_photo: true
awareness: [problem-aware, solution-aware]
copied_from: 06-relief-scene
copied_at_version: "3.7"
blocked_by: null
exempt_from: []
---

# lede-inuse

## PURPOSE
The closing bookend of a pain→relief arc: one photograph of a person visibly letting go of
something they had been bracing against, **with the product there in the scene as the reason**.
Candid, single frame, no inset and no graphics — the product is part of the life, not presented
to the camera.

**Copied verbatim from `06-relief-scene` at version 3.7** (owner instruction, 2026-09-09).
Everything from PURPOSE to KNOWN-FLAKY below is that file's text, spliced by script rather
than retyped. `copied_at_version` in the frontmatter is what makes the copy auditable:
`scripts/validate.py` warns when the parent moves past it, so the drift this file is
exposed to is visible rather than silent. What is deliberately NOT copied is the parent's
WORKED EXAMPLES — SPEC §3.3 keeps a rendered example's prompt text as the record of what
actually rendered, and those renders were the parent's — and its CHANGELOG, which is the
parent's own evidence trail.

## TRIGGER
use_when: >
  The reader knows the problem and is weighing whether this kind of product is the
  answer. The product block's result_visibility is on-body or on-object, so there is a
  RESULT a photograph can hold. Editorial pages that open with a use scene rather than a
  problem scene take this; so does an ad-traffic page whose creative already showed the
  problem, where repeating it wastes the lede. Prefer lede-pain instead where the reader
  does not know the category exists.

## BOUNDARY
**Against `lede-pain`** — the product is present here and absent there.

**Against `lede-winner`** — this is a scene and that is a packshot. This one argues
living; that one argues choosing. A scene that has quietly become a hero shot on a clean
surface has crossed the line and should be filed as the other type.

**Against `lede-testing`** — the product here serves the OWNER, in the owner's own place,
and no instrument is in frame. A measuring device anywhere in the picture makes it a
testing frame.

**Against a customer's own photograph — and this is the FIREWALL, missing until 0.4.** G14
refuses a generated image that poses as a customer's own, and `registry/toplist-instruction.md`
records it binding the SLOT: *"a lede image that reads as a customer's own photograph, beside a
ranking the page presents as editorial, is the shape G14 exists to refuse."*

**The register this file copied invites exactly that read.** `PARTS/register` says *"a candid
documentary photograph a passer-by could have taken"* — on a product page that is a style note;
on a top-N lede beside an editorial ranking it is the UGC register by name. `lede-authority` met
the same problem and resolved it with a distinction rather than a reversal: **the frame is made
by a PHOTOGRAPHER, not by the subject.** Candid stays; amateur goes.

Visible and checkable: no selfie framing, no arm's-length camera, no phone in shot, no phone at
a mirror, no hand holding the camera. Those are in NEGATIVE.

**Against `lede-authority`, and one sentence over there is now stale.** That file's NEGATIVE
reasons: *"A frame that shows mess argues this is real life, which is `lede-inuse`'s argument."*
**It is not this type's argument any more.** The owner's instruction of 2026-09-10 — *chân thực*
but not *đồ vật lộn xộn, cũ* — took mess off this type at 0.8, and 0.9 adds `PARTS/condition` on
top. The real line between the two is elsewhere and always was: **that type is `to-lens` and this
one refuses the lens at the gate**, which `PARTS/gaze` fails a frame for.

*`lede-authority` is finished at 0.11 and committed (`c81ae0d`), and a type file is the owner's to
open. The stale sentence is recorded here and NOT edited there. Its correction is one line in that
file's NEGATIVE prose and nothing in this namespace depends on it — the boundary it draws still
lands, on a premise that has moved.*

The parent's own boundaries and its pairing with `01-pain-scene` are not restated.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.
A rendered prompt expands what it calls — the model never reads this file (ADR-017).

```
TYPE: lede-inuse v0.15  (copied from 06-relief-scene v3.7; MARKS removed, see CHANGELOG)
      This line is the FILE's header. It never enters a prompt body — SLOT CONSTRAINTS.
REGISTER: editorial documentary photograph, made by a photographer. -> PARTS/register

[SUBJECT] one adult, doing a thing that asks something.       -> PARTS/subject
[CASTING] Western European. White or Black, never Asian.      -> PARTS/casting
[DRESS] particular, not issued. Range open to the model.      -> PARTS/dress
[GAZE] candid, or on a reflection. Never on the lens.         -> PARTS/gaze
[POSE] at ease, not braced, and the act NEVER stops.          -> PARTS/pose
[ENVIRONMENT] cared-for and PERSONAL, and it ASKS something.  -> PARTS/environment
[CONDITION] the product is clean and as-new.                  -> PARTS/condition
[LIGHT] a bright, naturally lit place — name the surfaces.    -> PARTS/light
[GRADE] natural and true. Authentic is not shabby.            -> PARTS/grade
[COMFORT] a floor that is drawn, a range left open.           -> PARTS/comfort

[CROP] the product ON the body, close enough to read both. -> PARTS/crop
[EVIDENCE] one visible thing the product is DOING, shaped     -> PARTS/evidence
           the way the material actually behaves.
[PRODUCT] in the scene as the reason, never presented.        -> PARTS/product
[RELIEF] the moment of letting go, in a situation that        -> PARTS/relief
         would have demanded bracing.

VARIANT, at least one cell in every set:
[MAT] the photograph sits inside a designed mat.             -> PARTS/presentation
[GROUND] one flat designed field around the mat.             -> PARTS/presentation
```

## PARTS

**`register`** — **rewritten at 0.7 to say what BOUNDARY has been refusing since 0.4.** An
editorial documentary photograph, made by a photographer standing in the right place. Candid
stays and amateur goes: natural, unposed, sharp, the subject unaware of the camera — but the
frame is composed and the light is CHOSEN.

Two phrases of the copy are struck. *"A passer-by could have taken"* names the UGC register
that BOUNDARY refuses under G14 by quoting this very sentence, and it sat here unchanged for
three versions while the paragraph forty lines above called it the fault. *"Not lit"* is the
seed of what `light` below now spends its whole entry undoing.

**`subject`** — **rewritten at 0.9.** It read *"the same demographic and the same person as the
paired pain image, in put-together but ordinary clothes from the same palette family, doing an
everyday thing in public and pausing briefly."* Three of those are wrong here: the paired pain
image is a product-page device this slot does not have, *in public* went at 0.7, and **`ordinary
clothes from the same palette family` is a written instruction to make the wardrobe generic.**

*It is struck for what it would do, not for what it did. No prompt ever quoted it — see `dress`
below for what actually produced set 4's wardrobe.*

One adult, doing an everyday thing that asks something of the body, dressed as `dress` below says.

**`casting`** — **new at 0.10, owner instruction, 2026-09-10.** *"Luôn sử dụng người phương tây,
châu âu, da màu, da trắng, không dùng châu á"*.

**Subjects are Western European — white and Black — and never East or South-East Asian.** It is a
market-fit decision for the owner's landing pages, which are written for a Western readership, and
it binds every frame this type produces. Set 5 cell 2 is the one breach in the type's history and
it predates the instruction.

**Confirmed 12 of 12 on its first outing at set 6.** It is a CASTING slot, so it takes a value or
it takes a default — the same law as the wardrobe
below. Left unnamed, the model casts from its own prior, which is how a set of six arrived carrying
one East Asian subject that nobody asked for. Name it in every prompt.

**`dress`** — **new at 0.9, on owner instruction.** *"Quần áo của user có thể đặc biệt: hoạ tiết
hay màu sắc sặc sỡ, không generic — hãy để prompt mở để model tự suy luận"*.

**CONFIRMED at 0.10, 4 of 4, against a control drawn twice — the cleanest experiment this type has
run.** The four cells carrying `[DRESS]` returned denim dungarees with a multicoloured print scarf;
a houndstooth shirt; an indigo quilted jacket over a mustard shirt; a printed shirt over a striped
knit. **The two control draws, identical prompts four minutes apart, both returned plain**: an
olive linen shirt and an oatmeal knit. **Two draws agreeing is what makes this a rule rather than a
frame**, and the same pair disagreed about evidence on the same prompt, which is precisely what
§*Reading a render* warns a single draw cannot tell you.

**And the OPEN form is what produced them.** No prescription in this file would have written a
multicoloured scarf over dungarees. This is `registry/toplist-instruction.md`'s own sorting seen
from the useful side: things to draw must be named, and taste must not be.

**Set 4 is 6 of 6 generic**, and it is the clearest thing in the set: a grey marl tee, a grey
sweatshirt, a plain navy top, a dark apron, a dark tee and joggers, a grey work shirt. Six
different people, six different rooms, one wardrobe.

**And the cause is the role-vs-value default, not the copied clause.** Set 4's prompts never
shipped `subject`'s *ordinary clothes from the same palette family* — they said only *an adult
making coffee at home in the morning*. **The wardrobe was an UNNAMED slot and took the commonest
thing of its kind**, which is the sixth instance of the law `registry/toplist-instruction.md`
carries, after the white border, the badge that printed `LABEL`, the neutral face, the colourless
palette and set 4's own blank control. The copied clause is struck anyway, because it would have
produced the same result on purpose the first time a prompt quoted it.

**A pattern or a strong colour is allowed and wanted** — this person is somebody rather than a
figure. **The clause INFORMS and does not prescribe**: name the range and let the model choose the
garment. `CONSTRAINTS` keeps only the refusal, which is *nothing generic, nothing that looks
issued*.

**Not `lede-authority`'s `expertise`, and the difference matters.** That clause dresses a subject
so the reader can tell what they DO; this one dresses a subject so the reader believes they are a
particular person. A trade uniform is the right answer there and often the wrong one here.

**`gaze`** — **the gate broke for the first time at set 5, 2 of 6, and `PARTS/pose` names the
cause: an open pose range that offered *a half-turn to look back*.** Clean across sets 1–4, 24 of
24. The refusal stands unchanged; what changed is that a clause somewhere else can defeat it.

`candid`, absorbed in their own business, or `reflect`, on their own image in
glass. Both are existing values of the shared axis, and `candid` is the default. **Never at the
camera**: looking at the lens reads as showing off and the barrier goes up. It fails at the
gate — a render that meets every other rule is still a fail if the eyes find the lens.

**`environment`** — **rewritten at 0.7, and it is the fault this clause was always about.** The
copy says *"a public everyday place the subject would actually pass through… The problem started
in the bathroom; the promise ends in the world, which is why this type is never set at home."*

**The type's own evidence refutes the property and keeps the fault.** Its single corpus MATCH is
a man brushing his teeth in a dark bathroom — the exact room the clause names as the wrong one.
Set 2's best frame is a car interior on a motorway, which is neither public nor a place anyone
passes through. Set 2 put 3 of 6 cells indoors or on private ground and all three landed.

**So the setting must make a DEMAND** — a load to carry, a flight already climbed, a hard floor,
a cold morning, a tool that fights back. `THE RELIEF` has said so in its own words since the
copy arrived: *"a public place is not a style preference; it is where something is asked of a
body."* Publicness was the proxy; the demand is the thing, and this is the same repair
`registry/toplist-instruction.md` §*Writing a clause* names — state the fault, leave the axis
open. n = 1 corpus + 3 renders. The wide public street is not banned; it is one setting among
several, and where the setting IS a street, two or three incidental blurred passers-by or street
details keep it a place rather than a set. Nothing aspirational, no travel-brochure location, no
empty clean street — those asked nothing, which is why they were listed.

**CARED-FOR IS NOT EMPTY — corrected at 0.11, and the clause below caused the fault it corrects.**
Owner, 2026-09-10, on set 6: *"mọi thứ đã ổn trừ scene chưa lively, chưa sống động"*.

**0.8 met NEGLECT and answered it with CLEAR.** Every prompt of sets 4, 5 and 6 says *a kept X —
clear worktop*, *clear floor*, *clear surface*, *everything in good order*, *the bench clear around
the work*. **It worked, and then kept working**: set 6 returned a hallway with nothing on its walls,
a bedroom with a bare bed and an empty dresser, a patio with a blank rendered wall, and a show
kitchen with an empty floor. **This is §*Writing a clause* for the fourth time in this type** — a
constraint aimed at one fault, written as a general property, removing the whole axis it touches.
The axis here is how much LIFE is in the room.

**The two frames of set 6 that read alive are the two whose rooms are full for structural reasons**
— a workshop with a rack of chisels and a wall of tools, a garage with a pegboard of spanners. They
survived the clause because their contents are what the room IS. Nothing else in the set did.

**So name what is in the room, as things to draw.** Herbs on the sill and a bowl of lemons; a cloth
over the rail and pots on the open shelf; coats on the hooks and boots below them; a plant, a stack
of books, a half-drunk cup, a jar of brushes. **A cared-for room is FULL of a life being lived in
it.** What stays refused is neglect — grime, damage, bare unfinished surfaces, things broken or
piled where they fell — and that is a different thing from a room with things in it.

**Confirmed at 0.12, 4 of 4, and the control refined what the axis actually is.** Set 7's four
lived-in cells came back with the named objects present and belonging to somebody: herbs, lemons, a
jar of spoons and flour dusted on the worktop; coats, a scarf, a basket of gloves; books, a throw,
cushions that had been sat on; pots by the door, a trug of cuttings, a jacket over the bench.

**The two control draws were NOT both empty, and that is the useful part.** One returned a bare
worktop with a single bowl; the other returned a kitchen with open shelves, crockery, a knife block
and a kettle — furnished, and with nothing in it that belongs to a person. **So the axis is not
FULL against EMPTY, it is PERSONAL against IMPERSONAL.** Fixtures do not count: a knife block is
what a kitchen has, a bowl of lemons is what somebody bought. **0 of 2 control draws personal, 4 of
4 lived-in cells personal.**

**The failure mode of naming objects, and set 7 shows it once.** The hall came back with a coat, a
scarf, a basket and a coat hung in an evenly spaced row — **arranged rather than left**. Name the
objects, then name that they were put down mid-life: boots kicked off rather than paired, a scarf
half on its hook, the cup where somebody set it.

**Confirmed at 0.14, 6 of 6.** Set 8's halls came back with boots dropped where they were pulled
off, a waxed jacket hanging as it was hung, a basket of post on a stool and a book left face down on
the arm of a chair. **Nothing in the set reads arranged**, and the repair is one clause about how
the objects got there rather than a longer list of objects.

*A measurement was attempted here and DISCARDED. Full-frame detail density ranks the extremes
correctly — a greenhouse at 12.9 against a blank bathroom at 4.1 — and does not separate the
middle: set 6's dead frames run 3.8 to 6.5 and its lowest live one is 6.6. No figure from it is
published, and the reading above is by eye.*

**And the place must be CARED FOR — new at 0.8, and it is the second half of the owner's note.**
*Chân thực* is not *đồ vật lộn xộn, cũ*. Set 3 produced a dank concrete stairwell with a scuffed
barrow and grimy gloves, and a room stripped back to bare plaster under dust; both are honest
places and both are ones a reader recoils from. A demand on the body does not require squalor:
the demand can be made in a clean kitchen, a bright workshop, a tidy room. **Name the place as
kept** — swept, finished, in good repair, the equipment in good condition.

*0.7 argued here that an interior was the type's best setting because it is where a dark mass can
be put. That justification died with the dark-mass hypothesis and is struck. Interiors stay, on
the evidence above and on nothing else.*

**`light`** — **replaced at 0.8. 0.7's version is refuted by its own set against its own
control, and the owner named the replacement.**

Owner, 2026-09-10, on set 3: *"đặt vị trí vào người đọc… đối tượng sử dụng (chủ thể) trong ảnh cần
phải thể hiện được sự tiện nghi, thoải mái, môi trường tươi sáng… ưu tiên nền sáng, tone sáng, tự
nhiên, mang lại cảm giác thoải mái, chân thực (không phải chân thực kiểu đồ vật lộn xộn, cũ)"*.

**Default: a bright, naturally lit place, and NAME THE SURFACES that make it bright.** Daylight
through a large window or open sky; pale walls, pale stone, light wood, clean glass; a light
ground the subject stands on. *Bright* on its own is a role and takes a default — the surfaces
are the things to draw.

**Where the product forbids a bright place, the frame shows the problem ALREADY SOLVED.** This is
the owner's own second sentence and it is the whole exception: a stair light, a night drive, a
cellar. The frame does not get to show a person coping in the dark. It shows the treads lit and a
foot going down easily, the road ahead clear, the wall dry. **The dark is the product's stage,
never the reader's experience.**

Direction stays released — the best frame in set 3 is plain warm sunlight, and what remains
banned is FLATTERY: beauty retouching, plastic skin, a styled outfit, the stock-photo look.

**`grade`** — **replaced at 0.8. Natural and true, and authentic is NOT shabby.** Owner: *chân
thực (không phải chân thực kiểu đồ vật lộn xộn, cũ)*. 0.7's *one colour carries the frame, cool or
warm* is struck: it produced the two frames of set 3 that read worst — a cold blue-grey concrete
stairwell and a cold blue-grey room stripped to bare plaster, both of them exactly the
cluttered-and-worn authenticity the owner excludes.

Kept from the parent, because nothing has argued with them: light film grain, shallow depth of
field, and **honest, not drained**.

**`comfort`** — **new at 0.8, and it is the owner's central instruction: put yourself in the
READER's position.** A lede image of a product in use has to make the reader feel ease before it
proves anything. `THE RELIEF` below says what a released body looks like and that stands; this
entry says the ease is a NAMED SLOT rather than something the other blocks are trusted to carry.

**It has its own slot because set 3 showed it losing when it did not have one.** Cell 5 named the
muscles inside `[EVIDENCE]` — brow smooth, jaw loose, shoulders dropped — and `[SUBJECT]` in the
same prompt described midday sun and a garment dark with water. The frame came back with a man
sweating, mouth open, plainly straining. **When the prompt describes the problem anywhere, the
problem wins, even against a correctly written relief clause.**

**And a product class is refused here.** Cell 5's vest works BY BEING WET, and wet is what the
heat it relieves also produces. **Where the product's working state is indistinguishable from the
problem's symptom, this type cannot argue with it** — take the package route, or take another
type. Add it to the three classes under `product`.

**CONFIRMED at 0.10, floor held 6 of 6** — every cell of set 5 showed real ease, including both
control draws, which carried no `[DRESS]`. So comfort is independent of the wardrobe and the floor
is what stops the blank face of set 4's control.

**Reworked at 0.9: a FLOOR that is drawn, and a RANGE that is open.** Owner: *"cần phải áp dụng
pose, emotion giống authority"*. `lede-authority`'s `pose` clause was added on the same instruction
in its own words — *"author cần có đa dạng pose, biểu cảm (để mở cho model tự chạy)"* — after a
prescription of taste flattened twelve of its renders to one centred, square, neutral picture.

**Set 4 shows both halves of the problem at once.** Cell 6, the control, carried no `[COMFORT]`
block and returned a completely blank face — so the slot cannot simply be opened and left. Cell 1
carried the prescribed triple word for word and returned a half-grimace: brow not smooth, mouth
open, the free hand splayed palm-up in a gesture nobody makes. **One prescription, six subjects, and
the frames that worked are the ones where the model had somewhere to go** — cell 3's small
unforced smile is the best expression this type has produced.

**So: something must be DRAWN, and WHICH thing is the model's.** The floor is that the body is not
guarding and the face is not caught — those two are the type's own measured refusals. Above the
floor, list a range and let the model pick: a small smile arriving on its own, a slow breath out,
eyes creasing, a shoulder dropping, a head tipping toward the work, an unhurried hand. **Name three
or four as a range, never one as a specification.**

**This is the round-3 finding, not a new one.** Four prescriptions of taste were ignored 4 of 4
there, while geometry and count landed 15 of 15. **Taste is the half that never held when it was
dictated**, and expression, pose and dress are taste. Nothing here weakens the rule that a thing to
draw lands — it says which clauses are things to draw and which are not.

**`pose`** — **new at 0.9, the same mechanism as `comfort` and imported from `lede-authority`
0.10.** The distinction there is **DELIBERATE against CAUGHT, not neutral against expressive**, and
it holds here with one word changed: this type's subject is candid rather than deliberate, so the
distinction is **AT EASE against BRACED**. A lean on the counter, a crouch to the work, a hip
against the bench, weight on one elbow — all belong. What is refused is the guarded body the type
already lists: a hand braced on furniture, a part held or covered, weight kept off one side.

**It works: set 5's open range produced a wall lean and a lean along a greenhouse row**, neither of
which a prescription would have written, and both in the two best frames of the set.

**And it broke the gaze, 2 of 6 — the range itself carried the trap.** Set 5 offered *a half-turn
back down the row* and *a half-turn to look back* among the options, and both cells that took them
came back with the subject looking into the lens. **Turning back is looking at something, and the
nearest something is the camera.**

**So: an open range may not contain an option that turns the subject toward the viewer.** Every
option must face the subject INTO their own business — down at the work, along the row, at the
thing in their hands. The repair is the option list, not the openness: closing the range would cost
the wall lean, and `registry/toplist-instruction.md` §*Writing a clause* says the fix for a clause
that did its job and kept working is a finer distinction, never the opposite end.

**Set 9 confirms the OTHER suspect, and it is the one 0.11 could not separate.** The gaze broke
again, 1 of 13, on a cell with no turn-back option anywhere in it: a crouching full-body subject
with space around her, who looked straight into the lens. **So the option list was half the cause
and the FRAMING is the other half** — a subject seen whole, at a distance, with room around them,
is portrait grammar whatever the pose range says. 0.12 named this as the better explanation for
set 6's paused bodies and could not test it; set 9 tested it by accident and it holds.

**Set 6 tested that and it holds: the option present, 1 of 2 looked into the lens; the option
removed, 0 of 10.** The control's two draws split — one looked off-frame, one into the lens — which
is the whole argument for drawing a control twice, since either draw alone would have settled this
wrongly in one direction or the other.

**The act anchor is NOT confirmed, and the control says so.** Set 7 predicted that the two draws
without it would show a stopped body; **both came back mid-act**, lid off and crank turning. So the
anchor costs nothing and has not yet been shown to buy anything — set 6's two paused bodies are
better explained by their framing, a full-length subject standing back from the work, than by the
missing clause. Kept, unproven, and the next set that carries a standing full-length crop is where
it gets tested.

**A THIRD pull toward the portrait, and it is the one still open: the action stops.** Set 6 cell 7
leans on the wall smiling with the hammer held and the nail not going in; cell 11 holds the coat out
with the shaver against her chest. **Both are people PAUSED for a photograph**, which is a portrait
even when the eyes stay away from the lens, and the frames that read alive are the ones caught
mid-bead and mid-wipe. **So the range must be anchored to the act**: every pose option is a shape
the body takes *while the work is going on*, never a rest between goes. This is the second half of
the owner's *chưa sống động* — a still room and a stopped body make the same dead picture.

**`address` is NOT imported and importing it would destroy the type.** `lede-authority` is
`to-lens` and says so as its whole argument. `PARTS/gaze` here refuses the lens at the gate.

**0.9 said that and it was not enough.** Declining to import a clause does not stop the clauses you
DO import from carrying its grammar: a full-length standing subject with an open pose is portrait
grammar, and set 5 cell 1 is a portrait. **What crosses between types is not only what you copy.**

**This slot takes over two of `evidence`'s seven methods, and the split is the point.** Method 6
(*name the muscles, never the mood*) and method 7's no-face case are about what the READER feels;
methods 1–5 are about proving the product works. They were one list and they are two jobs.
**`evidence` proves; `comfort` invites.** Where there is a face, `comfort` names the muscles —
brow, jaw, shoulders, the hand open rather than clenched. Where there is none, it names the body
and the place: a foot square on a lit tread, a hand resting on a rail rather than gripping it, an
unhurried posture, a kept room around it.

**`crop`** — **new at 0.4, and it is the biggest divergence from the parent.** The copied
`subject` and `environment` describe a whole person mid-errand in a public place with blurred
passers-by. **Neither frame this type actually holds looks like that.**

| the two observations | what it is | value | texture |
|---|---|---|---|
| `1920.avif`, **match** | a man brushing his teeth, close crop on head and hand, dark bathroom, eyes off-lens | **0.16** | 10.0 |
| `WILI_BEDROCK-MOUNTAIN-CLOGS-02`, variant | feet in sandals on a sunlit rock — **no face, no person above the shin** | **0.94** | 3.1 |

**Both crop tight to the product ON a body**, and one of them contains no person at all beyond a
pair of legs. The parent's whole-person public scene has exactly one render in this type and it
is the founding round, which failed on argument.

**n=2, which is under SPEC §6.2's threshold of three, so this is not yet a rule.** It is recorded
with its n beside it and set 1 tests it directly: the tight crop against the parent's wide scene,
same argument, everything else held.

**The tight crop also answers the G14 firewall**, which is why it is worth testing rather than
merely noting. A frame with no face and no camera-holder cannot read as a selfie, and a close
crop on a hand and a product is the register of an editorial detail shot rather than of a phone
snap.

**`presentation`** — **the second corpus frame is a photograph inside a DESIGNED OBJECT**, and
that is a shape this file has no vocabulary for. A real in-use shot sits on a mint ground inside
a pink mat with a scalloped edge and small corner ornaments; the ledger recorded it as *"a use
photograph presented as a graphic OBJECT"*. Measured, its ring reads value 0.94 and texture 3.1
— a designed ground, not a room, which is why it sits so far from the other observation.

**3 of 3 rendered, across set 1 and set 6.** Set 6 returned it exactly as written — a sage ground,
a clay mat with a scalloped inner edge, a pressed-flower ornament at each corner, no lettering
anywhere. This is the most reliable thing in the file after the G14 firewall.

**THE MAT HOLDS A FACE — settled at 0.15, 2 of 2, and the two draws agree.** Set 9 drew the
never-drawn case twice. Draw 1 gave the whole head with room around it and a real smile reading
clearly inside the mat; draw 2 clipped the crown and the expression still read. **The framed
variant is NOT a no-face form**, which is what the prediction said and what the repeat now carries.
**And the mat's SHAPE is a free choice**: a scalloped edge and a plain square with an inner rule
both landed. `presentation` is **7 of 7** across sets 1, 6 and 9.

**But the GROUND drifts to PATTERN when the mat is named in detail — 2 of 4 framed cells.** Both
asked for *one flat designed field in a second hue*; one returned an ornate damask wallpaper, the
other a dotted halftone. **The mat took the attention and the ground took a default**, which is the
role-vs-value law arriving inside a clause that already names a value. The ground needs its own
word — FLAT, unbroken, no pattern and no texture — not just its hue.

**PROMOTED TO A STANDING VARIANT at 0.13, on the owner's question, and the drift it corrects is a
PROCESS fault rather than a craft one.** Owner, 2026-09-10: *"các inuse có frame đâu? lede-inuse
v0.4 — SET 1 CELL 3. lede-inuse v0.4 — SET 1 CELL 4"*.

**It was drawn in 2 of 8 sets.** Set 1 cells 3 and 4, set 6 cell 9, and nowhere else — three draws
against more than thirty plain ones. **The cause is how a set gets written**: every set since 1 has
chased whatever fault was open — evidence, light, comfort, dress, liveliness — and a MAT is a
wrapper that does not interact with any of them, so it was never the thing under test and never got
picked. **A variant that is not the current fault is never drawn**, and three draws is not enough
to promote it or to retire it.

**So it stops depending on what is broken this week.** Every set carries at least one framed cell
until the count reaches ten, at which point it is either a settled form or a refused one. What is
still open about it is real and none of it can be answered at n=3: whether the mat's SHAPE may vary
(a scalloped edge is 2 of 3 and a plain rule has never been drawn), whether the ground's hue
relationship follows the namespace's designed-ground clause, and whether a framed cell can hold a
FACE — all three drawn cells are tight crops with no face in them.

**The tension with PURPOSE is recorded rather than resolved.** *"No inset and no graphics"* refuses
a graphic laid ON the photograph; a mat is the page's frame AROUND it, which is the shape the
corpus's second observation actually takes. Every drawn cell has kept that line — the mat and the
ground are the only designed elements and nothing is drawn over the picture.

**1 of 2 in the corpus, and it is the other half of the G14 answer.** Wrapping the photograph in a frame the
page drew is the page saying *this is our picture*. Set 1 tests it as a variable rather than
adopting it.

**`evidence`** — **new at 0.5, and it is the fault this type has had since its first render.**
Owner, 2026-09-10: *"sự dễ chịu chưa được thể hiện rõ qua thái độ (mặt), môi trường (nếu không
có mặt)"*.

**Relief has been specified almost entirely as ABSENCES.** Set 1's six prompts asked for *not
guarding*, *no wince*, *no hand braced*, *calm and unbothered*, *not squinting, not flushed*.
Every one is a prohibition, and this namespace has already measured what a prohibition is worth:
across `lede-collage`'s twelve sets, clauses naming a distance or a refusal landed **0 of 12**
while clauses naming a thing to draw landed **37 of 37**. An absence returns NEUTRAL, and
neutral is not ease.

**Set 1 is that measured: benefit visible in 1 of 6.** The one that worked is the headlamp, and
it worked because the product's effect is an OBJECT in the frame — a beam of real light falling
on rock and on the hands clipping a carabiner. Nothing about the face; the picture shows the
product doing its job.

**And the crop hypothesis of 0.4 is REFUTED by the same set.** 0.4 predicted the tight crop
would read better than the parent's wide scene. It does not: the wide wrist-brace frame is
composed as well as the tight knee-brace one, and both fail on the same thing. **Crop is not the
variable; evidence is.** The two corpus frames are tight for their own reasons and the file no
longer reads that as a rule.

### Seven ways to put the benefit in the frame, most direct first

Each is a THING to draw, which is the only kind of clause this namespace has ever seen land.

1. **The effect as matter or light.** A beam on a surface, a mist plume, hair and a collar lifted
   by airflow, paint blistering under a heat gun. Strongest, because it is evidence rather than
   expression — but it is only available where the product emits something.
2. **The act the problem forbade, at full commitment.** Not a braced knee near a step; a knee
   folded all the way to the heel on a hard floor. **The test: could a person with the problem
   hold this pose?** If yes, the frame proves nothing.
3. **A body part doing work only the benefit allows.** Bare fingertips working a screen in snow,
   with the gloves the reason the rest of the hand can stay out.
4. **A comparison inside the frame, as an OBJECT and never as a second person.** Half a
   windscreen clear beside half still iced; the bare hand beside the gloved one. It must be a
   **switchable state** — remove the product and the harm returns — which two different people
   can never be.

   **THE BOUNDARY MUST BE THE SHAPE THE MATERIAL MAKES — new at 0.12, and it is the fault the
   owner named.** Owner, 2026-09-10, on set 7: *"sofa cleaning product seems fake, không chân
   thực"*. The pet-hair cell asked for *a clean stripe* with *a hard edge where the roller has
   run*, and returned a **perfect dark rectangle with square corners** cut into a uniform pelt —
   a frame that reads as a paste-up rather than a photograph, which is the one thing that breaks
   this type's whole register.

   **Sorted across five draws, and it sorts by physics rather than by wording:**

   | the material | boundary asked for | result |
   |---|---|---|
   | ice melting on a windscreen | *a hard wet line* | **landed** — a melt front IS a hard line |
   | a wet disc on carpet | *a hard damp curve* | **landed** — so is a wetted edge |
   | condensation wiped from a mirror | *a hard boundary* | **landed** — so is a wiped film |
   | a squeegee on dry glass | *a hard clean/grey line* | **never appeared** — a pass leaves streaks |
   | hair lifted off upholstery | *a hard edge* | **fake** — fibres do not cut square |

   **CONFIRMED at 0.14, 1 of 1.** Set 8's suede cell asked for no line at all — a lifted nap thinning
   unevenly into worn leather, strokes still showing across it — and returned exactly that: no
   straight edge, no square corner, and a flattened area that reads as a worn sheen rather than a
   pile standing off the hide. **The owner's fault is repaired by naming the material's behaviour.**

   **Where the physics makes a hard boundary, name it. Where it does not, name a feathered,
   uneven, partly-cleared edge** — thinning rather than stopping, a few fibres still lying over
   the line — or the frame stops being a photograph.

   **And the QUANTITY has to be plausible for the material too.** *The pale mat of hair still
   standing on both sides* returned a pelt an inch deep, which is carpet underlay and not a cat.
   Name what the material actually does: a haze, a scatter, a light drift caught in the weave.
5. **Tells of duration and quantity.** The stack already carried, the stairs already below, the
   distance already covered. Evidence of what has been done, not of how it feels.
6. **Where there IS a face: name the muscles, never the mood.** *Calm* is a mood and returns a
   neutral expression. **Brow smooth and unfurrowed, jaw loose with the lips slightly parted,
   eyes soft and half-lidded, shoulders dropped below the collar line** are things to draw.
7. **Where there is NO face: the environment is the witness.** Frost melted on the back of a
   glove, a collar that is dry, the dark beyond the beam, dust settling.

### The anti-method: never describe the problem — and it OUTRANKS everything above

**Four instances now, and set 3 settled the precedence.** Cell 5 carried method 6 written
correctly — *brow smooth and unfurrowed, jaw loose with the lips slightly parted, shoulders
dropped below the collar line* — and its `[SUBJECT]` line described midday sun and a garment dark
with water. **The frame came back with a man sweating and straining.** The relief clause was
present, well-formed, and lost.

Cell 2 lost the same way from the other direction: method 7 asks the environment to witness, and
the environment chosen was a room full of plaster dust, which witnesses the PROBLEM. **Method 7 is
only available where the environment's trace is of the SOLUTION** — frost melted, a wall dry, a
stair lit — and set 3's cell was a mis-pick, not a failure of the method.

**So the order is: the anti-method first, then a method.** A prompt is checked for a description
of the problem BEFORE it is checked for evidence, because no amount of correct evidence survives
one. The four: the founding round's *a room that is plainly hot*; set 1 cell 5's *the cold is
plainly real*; set 3 cell 2's dust; set 3 cell 5's sun and sweat.

**The founding round and set 1 cell 5 made the same mistake and it is mine both times.** One
asked for *"a room that is plainly hot"*, the other for *"the cold is plainly real"*, and both
then left the relief to the product's presence. **A prompt that renders the problem vividly gets
the problem.** State the situation as a demand on the body — a load, a distance, a darkness —
and never as a symptom the body is suffering.

### The dark-mass hypothesis, and how set 3 killed it

**Read this before the table below, because the table is correct as MEASUREMENT and inverted as
JUDGEMENT.** 0.6 measured two frames it called editorial against two it called stock, found the
editorial pair dark and the stock pair light, and wrote the clause that chases dark. Set 3 tested
that against a declared control and the result is unambiguous.

**The clause landed, 6 of 6 on the numbers.** Cell 1 was written for deep dark and returned median
value 0.18 with 45% of pixels below 0.15 — the editorial column's own figures, 0.18 and 44%. Cell
5 was written bright and returned 0.87 and 6%. A prompt can put the mass of a frame wherever it is
told; that much is now established and it is the one thing worth keeping from 0.7.

**And the best frame in the set is the CONTROL, which held the copied wording**: 0.67 / 3% / 0.20,
sitting inside the column 0.6 labelled *stock*. Set 3 predicted, in writing, that cell 6 would come
back at *"median value above 0.55, dark share under 10%, saturation near 0.15"* and would read
stock. **All three numbers came in as predicted and the frame is the one a reader would want.**
What failed was not the measurement but the name attached to the column.

The two deep cells failed on more than light — cell 1's barrow shows none of the stair-climbing
mechanism that is its product, and cell 2's environment witnesses the PROBLEM rather than the
solution — so light is not the sole cause of those two verdicts. The control is what carries this
finding, and **it was drawn once where the set asked for two draws**, so the register rule's
requirement is unmet: *bright is better* is not yet established as a rule. **What IS established is
that 0.7's prediction is refuted**, which needed only the one draw, since the prediction was about
that frame.

*One measurement was attempted here and DISCARDED. A warm-hue share ranked set 3's six frames in
almost exactly the order the eye ranks them, and then failed its control: the set 2 driver frame,
which 0.6 named editorial, reads low on it, and the set 2 heat-gun frame, which 0.6 named stock,
reads high. No figure from it is published and the ordering above is by eye alone.*

### The measurement 0.6 took — a second intended divergence (ADR-070)

Owner, 2026-09-10, on set 2: *"logic ảnh đã tốt, tuy nhiên ánh sáng, màu ảnh vẫn chưa đạt được
editorial feel"*.

**0.6 measured this and then left the clauses it condemned standing.** The finding below was
written into the CHANGELOG and into a section of its own; `PARTS/light` and `PARTS/grade` kept
the copied wording, the SKELETON's call-map kept *plain daylight, no glamour* and *muted,
desaturated*, and NEGATIVE kept all three bans. **0.7 applies the decision 0.6 took** — which is
CLAUDE.md rule 6c's failure mode inside one file, found by reading the file top to bottom before
writing a set from it.

**The first hypothesis was that the light was flat, and it is REFUTED.** Set 2's ring spread_v
runs 0.34 / 0.63 / 0.67 / 0.68 / 0.84 / 0.91, **median 0.68** — sitting exactly on the 0.67 that
`registry/toplist-instruction.md` §Ground measured for the photographed families. These frames
are unevenly lit. Evenness is not the fault.

**What separates them is where the MASS of the picture sits.** Measured full-frame, not on the
ring, so the §Ground bound does not apply:

| frame | median value | share of pixels below 0.15 | saturation |
|---|---|---|---|
| set 2 cell 5, lumbar cushion — **editorial by eye** | **0.18** | **44%** | 0.38 |
| `1920.avif`, this type's only corpus **match** | **0.22** | **32%** | 0.41 |
| set 2 cell 2, kneeling pad | 0.41 | 25% | 0.27 |
| set 2 cell 4, de-icer | 0.60 | 13% | 0.29 |
| set 2 cell 1, heat gun — **stock by eye** | 0.77 | 8% | 0.30 |
| set 2 cell 6, ankle brace — **stock by eye** | 0.61 | **3%** | **0.15** |

**The control holds**: the two frames named editorial before the measurement are the two darkest
and the two most coloured, and one of them is the corpus rather than a render of mine. **Dynamic
range does NOT separate them** — every frame runs 0.86 to 0.98 — so this is not contrast in the
range sense. It is a frame that is predominantly dark with light picking out the subject, against
a frame that is predominantly light and evenly filled.

**Three inherited clauses cause it, and they conspire.** `[LIGHT] even natural daylight,
**bright**, soft shadows` pushes the median up; `[GRADE] a **natural palette**` is a role with no
value and defaults to colourless — the fourth time this session has watched that default, after
the white plate border, the badge that printed `LABEL`, and the neutral face; and the copied
NEGATIVE bans *golden hour*, *rim light* and *warm flattering light*, which are the light
qualities that give a frame a direction.

**Set 2 cell 5 broke that ban and is the best frame in the set.** Low warm side-light through a
car window, a real shadow across the far side of the face, a dark interior against a bright
exterior. 1 of 1 against the ban, in this namespace's own register.

**The repair is a distinction, not a reversal.** The parent's anti-glamour clauses were written
to stop `06-relief-scene` becoming an advert on a product page. Half of them are about FLATTERY
and half are about LIGHT QUALITY, and only the first half belongs here:

- **kept** — no beauty retouching, no plastic skin, no stock-photo look, no styled outfit.
- **released** — golden hour, rim light, warm light. A photograph may have a direction.
- **named instead of refused** — at 0.7 this read *the key's source, position and hardness; what
  it leaves dark, as a share of the frame; a colour position, cool or warm*. **0.8 keeps the
  grammar and inverts the target**: name the surfaces that make the place BRIGHT, and where the
  product forbids a bright place, name the problem already solved. See `PARTS/light`.

**What survives all of this is one narrow fact, and it is worth keeping.** A clause naming a share
of the frame puts the mass of a picture where it says — 6 of 6 in set 3, on both sides of the
axis. 0.6 had written *how much of the frame sits below mid-grey*, which asks the model to
measure, and this namespace lands that clause kind at 0 of 12; the share wording lands. **So the
instrument works and the target was wrong**, which is the cheapest kind of mistake to have made
and the reason set 3 was worth rendering.

**The saturation column was nearly mis-stated here, and the check that caught it is the standing
one.** Recomputing this table found value and dark share reproducing exactly and saturation
diverging by up to 0.13, because 0.6 took a MEAN over all pixels where the obvious reading is a
median. Publishing a second column beside 0.6's on a different instrument would have made every
comparison in this file false. **The method is mean saturation over all pixels**, recorded here so
the next pass does not have to find it again.

## THE RELIEF

**Relief is a body that has stopped defending itself, in a situation that would have demanded
defence.** Both halves are required and neither works alone.

**The situation has to cost something.** A man walking a towpath with his hands in his pockets
is not relieved of anything, because nothing is being asked of him. Kneeling on a hard floor,
carrying a full load up steps, sitting out in bright light, plunging hands into cold water —
these are situations the problem would have made a person avoid, ration or brace against.
Choose the situation from what the problem forbade.

**`environment` and cost are one rule seen twice, 8 of 8.** Domestic or idle settings — a bed, a
bench, an empty yard — asked nothing and the release did not read. Real load — a box onto a
shelf, a toddler onto a hip, a crate on cobbles, a reach to a high shelf — read every time. A
public place is not a style preference; it is where something is asked of a body.

**The body must not be guarding.** Guarding is visible and specific: bracing a hand against
furniture, holding or covering a part, favouring one side, keeping a part tucked away or out of
the light, bearing weight through one leg. Relief is the same body doing none of that — weight
even through both sides, the part in the open, limbs loose, nothing held.

**RELEASE ALONE IS COLLAPSE. Relief is release PLUS something coming back.** A smile alone is
a mood, no expression is nothing, and letting-go alone produces bodies that have given out —
which says the opposite of the argument. The discriminator is visible, and mostly the eyes:

| | collapse | relief |
|---|---|---|
| eyes | shut, lolling | **open, or opening**; creased at the corners |
| head | thrown back, throat bared, mouth slack | level or lifted, the chin doing something |
| limbs | flung, limp | loose but with tone, doing something small |
| direction | everything sinking | the chest opening, shoulders back AND down |
| face | slack | a small smile that arrives on its own |

**The smile is a consequence, never a pose.** Not one performed at a camera-friendly moment:
the one that turns up by itself because something stopped hurting — small, often only in the
eyes, while the person looks at something other than the lens.

Photograph the second the release happens, and require all three of these together:

- **expression** — the breath going out AND the eyes coming open, the brow releasing, a small
  involuntary smile
- **gesture** — the chest opening, shoulders rolling back and down, a held part stretched out,
  a hand opening
- **action** — doing the thing freely, mid-movement, with the product visibly the reason

Any one alone reads as an ordinary photograph. Release without the return reads as collapse.

**`product`** — the product is in the scene as the reason the release is happening, and G1
binds it: the attached photo is the exact reference.

**It must STAND IN THE FRAME AS ITS OWN OBJECT, near the camera, turned so it can be read.**
Measured twice: of four renders at 3.2 and eight more at 3.5–3.6, the only two a viewer could
name were a bottle upright on a desk and an open tub on a worktop, both near the lens with the
label toward it. Everything inside, under or edge-on failed.

**A LABEL THAT CAN BE READ IS TEXT, and the type banned both.** The one nameable product in
eight carried its name in clean type; the one turned away came back with a gibberish
back-of-pack panel and read as a household cleaner. The no-text rule's evidence was a named
NEWSPAPER — an object whose content IS text — and it was over-generalised onto labels, where G1
binds the product to the reference anyway. **The label carries the NAME and nothing else.**
Amount is the discriminator: two words render clean, a paragraph renders as gibberish.

**Not presented still holds** — the person does not hold it up, look at it or offer it, and it
is not centred or lit for the camera. It simply occupies its own space in the picture the way a
documentary photographer standing in the right place would include it.

**`condition`** — **new at 0.9, and clean 6 of 6 on its first outing at set 5.** The product is
clean and as-new, always. It is the thing the page
is recommending and a reader cannot be asked to want a soiled one. **Signs of a life lived belong
on the person and on the room, never on the unit.**

**This type's own evidence, not an import.** Set 3 cell 1 returned a scuffed sack barrow with
grimy gloves in a dank stairwell and it is one of the three fails in that set; the owner named the
same fault in general terms the same day — *chân thực* is not *đồ vật lộn xộn, cũ*. `PARTS/grade`
and `PARTS/environment` took the room and the tone at 0.8 and **left the UNIT uncovered**, which is
the gap this closes. `lede-authority` reached the identical clause from its own set 1 and its
wording is worth having beside this one, but its counts are its own and none are borrowed.

**Four product classes. The third takes `--detail` rather than being excluded; the fourth is
REFUSED by this type.**

| class | test | route |
|---|---|---|
| **standalone** | sits in the scene as its own object | `--none` — the eye-drops bottle |
| **worn-external** | can be the outermost layer if the wardrobe allows | `--none`, on a wardrobe condition |
| **conforming or enclosed** | no silhouette of its own, or always inside another object | **its package in frame, `--detail` for the mechanism** |
| **symptom-shaped** | its working state LOOKS LIKE the problem's symptom | **refused — take another type** |

**Symptom-shaped is new at 0.8 and set 3 cell 5 is the instance.** An evaporative cooling vest
works by being wet, and wet is also what the heat it relieves produces. The prompt asked for *the
vest dark with water across the shoulders and down the spine* and the frame returned a soaked
t-shirt on a man visibly overheating. **There is no wording that separates the two**, because the
picture is the same picture. The class is small and worth naming: anything whose evidence of
working is a fluid, a flush or a strain that the problem also causes.

**Worn-external** — a compression sock, a knee support, a wrist brace — IS the visible surface
once the wardrobe exposes the limb. The wardrobe must be chosen for the product and the
situation must make it ordinary; a trouser leg pushed up for the camera is a pose and fails.

**Conforming and enclosed fail differently.** An insole is enclosed, inside a shoe where no
camera reaches. A patch is conforming — flat against a curve, so no silhouette. In shot is not
identifiable.

**Neither is a reason to refuse a product — but THE INSET IS NOT THE PRODUCT.** 3.5 and 3.6
tried to admit this class by drawing it instead of photographing it, and the product then left
the frame in 4 of 8. `requires_product_photo` and G1 bind in every variant, and a drawn product
satisfies neither.

**DRAWN for the first time at set 6 and it works.** The insole cell returned a scene rather than
the packshot this file predicted it would: the box standing open on a hall bench as one object among
several, the new insole going down into the boot, the flattened old one lying pulled out beside it,
boots paired on the floor below. **The named failure mode did not occur**, and the route the file
has described since 3.5 is now evidenced at 1 of 1 rather than argued.

**So it enters the frame AS ITS PACKAGE** — box, tub, sleeve or packet standing in the scene as
its own object under the rule above — and `--detail` says what the contents do. The package is
the photographed product, the cutaway is the mechanism, and neither substitutes for the other.

**The admission test.** If the resolved state cannot be shown as a body behaving differently in
a situation that costs something, this type is the wrong one. Close with `06-relief-hero`, which
presents the product and can argue with an inset because its register expects composed layers;
a candid documentary photograph does neither.

## MARKS

**This type carries NO marks, and that is an intended divergence from the copy (ADR-070).**

The parent's `cutaway` and `reach` exist only inside its `--detail` inset. This file's own
PURPOSE says *"no inset and no graphics"* and its NEGATIVE bans *"insets of any kind"*, so the
copy arrived carrying a MARKS section that its own PURPOSE forbids. **That contradiction shipped
at 0.2 and stood until 0.4.**

It is resolved by removing MARKS rather than by permitting the inset, for three reasons stated
rather than argued:

- **The evidence was never this type's.** Every count in the parent's table is borrowed — 14
  renders for `cutaway`, 5 for `reach`, all in the parent's register. `a-borrowed-mark-must-be-
  retested` is the standing rule: A11 is a claim about a REGISTER, not about a mark, and this
  type has never rendered one.
- **A top-N lede has no room for a diagram.** It is scraped as `og:image` and sits beside the
  page's own headline; the parent's inset belongs to an advertorial that can afford a second
  register.
- **The parent keeps them.** Nothing is lost: `06-relief-scene` still holds the full table, its
  renders and its `--detail` variant, and re-copying would bring them back.

`scripts/validate.py` warns when the parent moves past `copied_at_version`, which is the
instrument ADR-070 built for exactly this; the divergence is written here and in the CHANGELOG so
a later reader sees it as a decision rather than as drift.

## SLOT CONSTRAINTS
- **The prompt's own header can be PRINTED INTO the frame.** Set 2 cell 3 returned
  anti-vibration gloves with `LEDE-INUSE V0.5` printed across both backs, mirrored on the left —
  the model read the prompt's `TYPE:` line as content. It happened on the one product in the set
  with a large blank branded surface, which is what `lede-collage`'s set 4 measured at 2 of 2:
  the model fills a conspicuous empty brand surface, and what it reached for was the nearest
  text. **The type and version line stays out of the prompt body**; a set file may carry it as a
  markdown heading above the fence instead.
- **Never describe the frame's shape or ratio in a prompt.** The owner sets the ratio at render
  time (ADR-016); a prompt reasoning about frame geometry gets extra panels to fill the leftover.
- **The zone names never reach the model.** Region labels are the tier that leaks; whole-image
  and subject labels do not (adapter Rule 1b, tiers set by ADR-017). Describe the region:
  "a shop window fills the left third", not `[REFLECTION]`.
- **No object in the SCENE may carry printed text** — a named newspaper filled two
  `06-relief-hero` frames with nonsense. **The product's own label is the exception**: it carries
  the product NAME and nothing else, because the product law requires a label that can be read.
  Never a back-of-pack panel, body copy or barcode; those come back as gibberish.
- **An object whose CONTENT is text may not be named at all**, and naming it unlabelled does not
  save it. Set 4 cell 2 asked for *a plain notebook filled to the foot of the page* as a tell of
  duration and returned a spread of invented handwriting across a third of the frame, in the very
  set that added the unlabelled rule. **A jar can be plain; a filled notebook cannot** — its
  content IS the words, which is the `06-relief-hero` newspaper finding arriving a third time.
  Closed book, blank pad, a screen turned away, or choose a different tell.

  **Third instance at 0.15, and this one is worse than the first two: the clause already existed
  and I wrote past it.** Set 9 cell 8 named *a road atlas in the door pocket* as a lived-in prop,
  in a set written five versions after the rule went in, and the atlas came back with its cover
  lettering legible. **A rule a writer has to remember is a rule that gets broken**; the check that
  works is reading the prop list of every cell against this clause before the set ships.
- **The product's own label is not safe at three words.** The type has taught since 3.5 that *two
  words render clean, a paragraph renders as gibberish*. Set 4 cell 6 returned a spray bottle
  reading `CO2-EALC BATHSOOM CLEANER` — three words, garbled. **The threshold is not a word count
  and the claim is now weaker than it was written**: what is safe is a mark the reference photo
  carries and the frame shows LARGE and square-on; what is not is any label small, angled or
  behind glass. Cell 6's bottle was all three.
- **G1 and the label rule collide on a product that ships an instruction panel.** Set 4 cell 4's
  mandoline came back carrying a full multi-line Japanese instruction panel — faithful to a real
  product, and `[PRODUCT REFERENCE]` requires preserving *every printed mark exactly*. **G1 wins**:
  the panel is the product, not invented lettering, and the type's *name and nothing else* clause
  governs what a prompt may ASK FOR, never what the reference truthfully carries. Recorded because
  a grader reading the no-text check would otherwise fail a correct frame.
- **And the ban is not enough on its own — NAME THE SCENE OBJECT AS UNLABELLED.** Set 3 cell 3
  carried *No words and no numbers anywhere in the frame except the product's own printed mark* as
  a binding constraint and still returned a jar of preserve wearing a full gibberish back-of-pack
  panel, because the prompt had asked for *a full jar of preserve* and a jar of preserve has a
  label. **The prohibition is inert for the same reason every prohibition here is** — it asks for
  an absence, and the ELEMENTS block had named a thing that comes with the text attached. Write *a
  plain glass jar with no label*, *an unbranded carton*, *a blank enamel tin*. Any scene object of
  a class that normally carries print gets named without it.
- A clause earns its place only if a render has failed without it, and is removed only once a
  render has done without it and come back correct (ADR-013, ADR-015).

## NEGATIVE
```
[G6] + selfie framing, arm's-length camera, phone in shot, phone at a mirror,
a hand holding the camera, badges, arrows, drawn overlays, insets of any kind, looking at camera,
posing, laughing as the relief, a situation that costs nothing,
a guarded body, hand braced on furniture, a part held or covered,
arms raised, celebration gesture,
beauty retouching, plastic skin, aspirational travel location,
empty clean street, styled outfit, product presented to camera,
product centred or held up, product hidden inside or under something,
product turned away so its face cannot be read, back-of-pack label, barcode,
bar chart, bars of stepped or graded height, arrowheads, translucent marks,
trouser leg or sleeve pushed up for the camera, blank expression,
collapsed posture, head lolled back, limbs flung limp, eyes shut and slack,
drained joyless grade, stock photo look,
a neglected or dilapidated place, bare unfinished walls, grimy or damaged equipment,
sweat patches, a straining face, an open panting mouth,
a soiled or damaged product, clothing that could belong to anyone,
a plain marl t-shirt or sweatshirt as the whole wardrobe
```

**The last two lines are new at 0.9** and both name what set 4 returned 6 of 6. They are backstops;
the working clause is `PARTS/dress`, which INFORMS rather than refuses, and a prohibition here
lands at 0 of 12.

**The last two lines are new at 0.8** and both name faults set 3 produced: a dank stairwell with a
scuffed barrow and a room stripped to bare plaster, against the owner's *chân thực* that is not
*đồ vật lộn xộn, cũ*; and a roofer sweating in full sun, where the frame was meant to argue that
he was cool. **They are backstops and the real fix is in `PARTS/light`, `PARTS/environment` and
`PARTS/comfort`** — this namespace lands prohibitions at 0 of 12, and the working clause is the
one that names what to draw.

**Four bans were struck at 0.7 and each is named rather than quietly dropped**: *golden hour*,
*warm flattering light* and *glamour lighting* are the light-quality half of the parent's
anti-glamour clause, released under `PARTS/light`; *saturated colors* contradicted the type's own
measurement, where the corpus MATCH sits at saturation 0.41 and the flattest render at 0.15.
**The flattery half is untouched** — beauty retouching, plastic skin, styled outfit, stock photo
look, drained joyless grade — because that is the fault those clauses were written against.

**This released four bans on one supporting frame (set 2 cell 5, 1 of 1), which is thinner
evidence than ADR-013 asks for.** ADR-013 removes a clause once a render has done without it and
come back correct; the release was made together because 0.6 measured the bans conspiring.

**Set 3 tested it and the release SURVIVES, for a reason nobody predicted.** Its control carried
the copied `[LIGHT]` and `[GRADE]` and the glamour ban, and produced the best frame in the set —
plain warm daylight on pale linen. That is the frame *golden hour* and *warm flattering light*
would once have refused on a product page, and it is what the owner asked for here. The bans stay
struck; what changed at 0.8 is the clause that replaced them, not the removal.

*Precisely: a set prompt ships its own CONSTRAINTS list rather than this NEGATIVE block, so what
cell 6 actually held was the two copied clauses plus the glamour ban — three of the four. The
fourth, `saturated colors`, was in no prompt of set 2 or set 3 either way.*

## KNOWN-FLAKY
(populated from observation evidence only)

## FOUNDING RENDER ROUND

**One render, 2026-09-09 — round 2 prompt 2, rendered at v0.2.** A wall-mounted air cooler
above a bed, a woman asleep on top of it, a hot bedroom. Verdict **`partial`**,
self-assigned under ADR-011 on a render that was opened and looked at. Ledger:
`eval/render-tests.jsonl`, ts `2026-09-09`.

**The slots landed and the ARGUMENT did not, and that is the finding.** Every block
arrived: the cooler is mounted, running and present as the reason the room is bearable
rather than as the subject of the photograph, which is the hardest thing this type asks
for. The ground is right for the family — texture 5.0, value 0.48, ring spread 0.86, a real
place unevenly lit.

**But the frame argues PAIN.** PURPOSE, copied verbatim from `06-relief-scene` at 3.7, is
*"a person visibly letting go of something they had been bracing against, with the product
there in the scene as the reason"*. The woman reads as still overheated — sprawled, arm
flung over the eyes, mouth open. Nothing in the picture says the cooler has worked.

**The prompt built that.** It asked for *"a room that is plainly hot — window open, curtain
still"* and for a sleeper with an arm over her eyes, then relied on the presence of a
running cooler to supply the relief. A product in a pain scene is not a relief scene; the
release has to be in the BODY, and this type inherits a parent whose entire argument is
that release.

**Recorded, and deliberately NOT written into `argument-faults.md`.** SPEC §6.2 routes
argument failures there rather than into the type that found them, and this one qualifies
in kind — a render correct in every slot and wrong in what it says. It does not qualify in
weight: 1 of 1, and this type has no second render to test a new fault against. Writing an
A-number from one frame is how the ground clauses of ADR-068 happened.

**Second failure, 1 of 1:** `[LIGHT]` returned warm low-angle sun with a hard wedge on the
wall, against *"even natural daylight, bright, soft shadows. No golden hour"*.

## CHANGELOG
- 0.15 (2026-09-11): **set 9 rendered — thirteen cells, the framed variant's open question closes,
  and the gaze's other suspect is confirmed by accident.** All thirteen opened and graded under
  ADR-011: **8 pass, 4 partial, 1 fail.** **THE MAT HOLDS A FACE, 2 of 2, and the two draws agree**
  — one gave the whole head with room around it, the other clipped the crown and the expression
  still read. The framed variant is not a no-face form, which is what the prediction said. **The
  mat's SHAPE is a free choice**: a scalloped edge and a plain square with an inner rule both
  landed, so `presentation` is now **7 of 7** across sets 1, 6 and 9. **New fault inside it: the
  designed GROUND drifts to PATTERN when the mat is named in detail, 2 of 4 framed cells** — an
  ornate damask and a dotted halftone against *one flat designed field*. The mat took the attention
  and the ground took a default; it needs its own word, FLAT and unbroken, not just its hue. **The
  gaze broke 1 of 13 with no turn-back option anywhere in the cell** — a crouching full-body subject
  with space around her, looking into the lens. **So 0.11's option-list repair was half the cause
  and the FRAMING is the other half**, which 0.12 named as the better explanation for set 6's paused
  bodies and could not test. Set 9 tested it by accident and it holds. **Every second draw held**:
  the physics fix 2 of 2 on a new material, the light exception 3 of 3, `gaze: reflect` 2 of 2, the
  enclosed-package route 2 of 2 and again a scene rather than a packshot. **And I broke my own clause
  writing the set that came after it** — set 9 cell 8 named *a road atlas in the door pocket*, an
  object whose content is text, five versions after the rule banning exactly that went in. Third
  instance, and the first where the clause already existed: a rule a writer has to remember is a rule
  that gets broken, so the prop list of every cell is read against it before a set ships. Cell 1 also
  returned a visible barcode on the product's own label, which the type bans and G1 permits from a
  reference — recorded, not resolved.
- 0.14 (2026-09-10): **set 8 rendered — 6 of 6 pass, the length cut is vindicated, and the physics
  fix repairs the fault the owner named.** All six opened and graded under ADR-011. **The cut
  holds**: five constraint lines were removed from four cells and **none of the five faults appeared
  in any of them** — no badge, no overlay, no retouched skin, no second person, no guarded body, and
  clothing still particular because `[DRESS]` names it. The two uncut control draws agree with the
  cut cells on every axis. **So the lines were ballast**, and ADR-013's converse has now been run
  properly for the first time in this type: a clause removed, a render done without it, and the
  render correct. Cut cells sit at a median 1974 against the control's 2307 — **333 characters, 14%
  — and the owner's *lưu ý về dung lượng* is answered with evidence rather than with trimming.**
  **The physics fix lands 1 of 1**: the suede cell asked for no line at all and returned a ragged
  feathered front with strokes across it, and a flattened area reading as worn sheen rather than a
  pile. **The staging fix lands 6 of 6** — boots kicked off where they were pulled off, a jacket
  hanging as it was hung, nothing arranged. Lived-in personal rooms 6 of 6; light 35 of 35; casting,
  dress, gaze, condition and the ease floor all held. **Nothing in this set failed**, which is the
  first time that has been true, and it is why set 9 is a full-coverage set rather than another
  one-variable experiment.
- 0.13 (2026-09-10): **`presentation` promoted to a standing variant, on the owner's question, and
  the drift it corrects is a PROCESS fault.** Owner: *"các inuse có frame đâu? lede-inuse v0.4 — SET
  1 CELL 3. lede-inuse v0.4 — SET 1 CELL 4"*. **It had been drawn in 2 of 8 sets** — set 1 cells 3
  and 4, set 6 cell 9 — three draws against more than thirty plain ones, and **3 of 3 passing**,
  which is the best rate in this file after the G14 firewall. **The cause is how a set gets
  written**: every set since 1 chased whatever fault was open, and a mat is a wrapper that
  interacts with none of them, so it was never the thing under test and never got picked. **A
  variant that is not the current fault is never drawn.** No render evidence contradicted it and no
  decision retired it; it simply fell out of the loop, and neither the type file nor any set file
  said it should be there. **Fixed by making it structural rather than topical**: the SKELETON now
  carries `[MAT]` and `[GROUND]` as a declared variant, and every set carries at least one framed
  cell until the count reaches ten. Three questions are open at n=3 and none is answerable yet —
  whether the mat's SHAPE may vary, whether the ground follows the namespace's designed-ground hue
  clause, and whether a framed cell can hold a FACE, since all three drawn cells are tight crops
  with none. Set 8 gains two framed cells at the cut length, which also asks whether the wrapper
  survives a shortened prompt.
- 0.12 (2026-09-10): **set 7 rendered — the lived-in repair lands 4 of 4, the control refines what
  the axis is, and the owner named a new fault that is a rule about PHYSICS.** All six opened and
  graded under ADR-011: **4 pass, 1 partial, 1 fail**. Owner: *"sofa cleaning product seems fake,
  không chân thực"* and *"lưu ý về dung lượng, độ dài prompt"*. **The fake frame is method 4's
  boundary and the clause caused it**: *a clean stripe* with *a hard edge where the roller has run*
  returned a perfect dark rectangle with square corners cut into a uniform inch-deep pelt — a
  paste-up, which is the one thing that breaks this type's register. Sorted across five draws it
  goes by PHYSICS, not by wording: a melt front, a wetted edge and a wiped film all take a hard
  boundary and all three landed; a squeegee pass never produced one; fibres lifted off upholstery
  produced a fake one. **Where the material makes a hard boundary, name it; where it does not, name
  a feathered, partly-cleared edge** — and the QUANTITY has to be plausible too, since *a pale mat
  of hair standing on both sides* returns carpet underlay rather than a cat. **`PARTS/environment`
  confirmed 4 of 4**, and the control did the more useful thing by NOT being empty: one draw came
  back bare, the other furnished with shelves, crockery, a knife block and a kettle and **nothing
  in it belonging to a person**. So the axis is **PERSONAL against IMPERSONAL**, not full against
  empty — fixtures do not count, 0 of 2 control draws personal against 4 of 4. **Named-object
  staging is the failure mode and set 7 shows it once**, a hall with coats hung in an evenly spaced
  row: name the objects AND name that they were put down mid-life. **The act anchor is NOT
  confirmed** — both control draws came back mid-act without it, so set 6's paused bodies are better
  explained by the standing full-length framing; kept, unproven, and flagged for the next set that
  carries that crop. **The `[EASE]` merge cost nothing**: the four cells with the longer range gave
  four good expressions, the two control draws with set 6's shorter range gave one grimace and one
  good. Light 29 of 29; casting, dress and gaze all held.
- 0.11 (2026-09-10): **set 6 rendered — twelve cells covering every case the type declares. Three
  cases drawn for the first time and all three work; the gaze diagnosis holds against its control;
  and the owner named the one thing left.** All twelve opened and graded under ADR-011: **7 pass, 3
  partial, 2 fail**. **The three never-drawn cases**: `conforming or enclosed → the package in
  frame` returned a SCENE and not the packshot this file predicted, at 1 of 1; `presentation` came
  back exactly as written and is now **3 of 3**; `gaze: reflect` landed on its first draw with the
  G14 firewall intact at the closest approach this type has made to the line. **`PARTS/casting` is
  12 of 12** on its first outing. **The gaze control split 1 of 2** — one draw off-frame, one into
  the lens — against **0 of 10** where the turn-back option was removed, so 0.10's diagnosis holds
  and **either draw alone would have settled it wrongly in one direction or the other.** Owner:
  *"mọi thứ đã ổn trừ scene chưa lively, chưa sống động"*. **Two causes, and I wrote both.** First,
  `PARTS/environment`'s *kept* clause of 0.8 met NEGLECT and answered it with CLEAR, so sets 4–6
  asked for *clear worktop*, *clear floor*, *everything in order* and got a bare bed, an empty
  dresser, a blank wall and a show kitchen — **§*Writing a clause* for the fourth time in this type**,
  a property deleting the axis it touches, the axis being how much life is in the room. **Cared-for
  is not empty**, and the only two frames that read alive are the two whose rooms are full for
  structural reasons — a chisel rack, a pegboard. Second, `PARTS/pose`: **a third pull toward the
  portrait, and this one stops the ACT** — cell 7 leans on the wall with the nail not going in, cell
  11 holds the coat with the shaver against her chest. A stopped body and a still room make the same
  dead picture, so every pose option is now a shape the body takes WHILE the work goes on. A
  detail-density measurement was attempted for liveliness and **DISCARDED for failing to separate
  the middle** — it ranks a greenhouse at 12.9 against a blank bathroom at 4.1 and then puts dead
  frames at 3.8–6.5 against a live one at 6.6. No figure from it is published. One `condition`
  breach in twelve: a visibly weathered step stool.
- 0.10 (2026-09-10): **set 5 rendered — `[DRESS]` is CONFIRMED against a control drawn twice, and
  the gaze gate broke for the first time in the type's history.** All six opened and graded under
  ADR-011: **3 pass, 1 partial, 2 fail**. **The control was finally drawn twice**, after sets 3 and
  4 each asked and each got one — the repeat was built into the cell list as two identical cells
  rather than as an instruction, which is the whole of the fix. **`[DRESS]` lands 4 of 4**: a
  multicoloured print scarf over denim dungarees, a houndstooth shirt, an indigo quilted jacket
  over mustard, a printed shirt over a striped knit — none of them anything a prescription would
  have written. **Both control draws returned plain**, an olive linen shirt and an oatmeal knit,
  which is the role-vs-value default's seventh and eighth instances. **And the same two draws
  DISAGREED about evidence** — one bag drawn tight onto its contents, one still loose — so
  §*Reading a render* earned its keep in the same experiment that used it: the wardrobe finding is
  a rule because two draws agree, and an evidence finding from either draw alone would have been
  wrong. **The gaze broke 2 of 6 and `PARTS/pose` carries the cause**: the open range offered *a
  half-turn to look back*, and turning back is looking at something, and the nearest something is
  the lens. **An open range may not contain an option that turns the subject toward the viewer** —
  the repair is the option list, not the openness, since the same open range produced the wall lean
  and the greenhouse lean in the two best frames. 0.9 wrote that `address` was deliberately not
  imported; **that was not enough, because declining to copy a clause does not stop the clauses you
  DO copy from carrying its grammar.** `PARTS/comfort`'s floor held 6 of 6 including both
  `[DRESS]`-less controls, so comfort is independent of the wardrobe; `PARTS/condition` is clean 6
  of 6 on its first outing; the light rule is now **11 of 11** across sets 4 and 5, at median value
  0.68–0.85. Owner then gave a standing casting instruction — *"luôn sử dụng người phương tây, châu
  âu, da màu, da trắng, không dùng châu á"* — written up as **new `PARTS/casting`**, a market-fit
  decision for landing pages aimed at a Western readership. It is a slot, so it takes a value or it
  takes a default: set 5 cell 2 is the type's one breach and it predates the instruction.
- 0.9 (2026-09-10): **set 4 rendered — the bright rule holds 5 of 5, the exception clause works,
  the `[COMFORT]` control fires exactly as predicted, and the wardrobe is generic 6 of 6.** All six
  opened and graded under ADR-011: **3 pass, 2 partial, 1 fail**. **0.8's light rule is confirmed**
  — cells 1–4 and 6 came in at median value 0.64–0.73 with 2–18% dark, clustered on set 3's control
  at 0.67 / 3%, and every one of them is a place a reader would sit in. **The exception clause is
  confirmed on its first outing**: cell 5's stair light measured 0.29 / 32% — as dark as the frames
  0.8 rejected — and reads as ease rather than coping, because the treads are already lit, the hand
  rests along the rail and a full glass rides in the other. **Dark was never the fault; showing
  someone cope with it was.** **`[COMFORT]` is not decoration**: the control carried no such block
  and returned a blank face, the fifth instance of the role-vs-value default. Owner then named the
  next two: *"cần phải áp dụng pose, emotion giống authority… quần áo của user có thể đặc biệt: hoạ
  tiết hay màu sắc sặc sỡ, không generic — hãy để prompt mở để model tự suy luận"*. **New
  `PARTS/dress` and `PARTS/pose`, both INFORMATIVE**, and `PARTS/comfort` reworked to a drawn FLOOR
  with an open RANGE — cell 6 proves the slot cannot be dropped and cell 1 proves the prescribed
  triple returns a half-grimace, so the repair is a range rather than either extreme. Mechanism
  imported from `lede-authority` 0.10, taken on the same owner instruction after a taste
  prescription flattened twelve of its renders; **`address` deliberately NOT imported**, since that
  type is `to-lens` and this one refuses the lens at the gate. **The generic wardrobe is the
  role-vs-value default, sixth instance** — set 4's prompts named no clothing at all, so the slot
  took the commonest thing of its kind; the copied `subject`'s *ordinary clothes from the same
  palette family* is struck as well, for what it would do rather than for what it did, since no
  prompt ever quoted it. **New `PARTS/condition`**: the product is
  clean and as-new, on set 3 cell 1's scuffed barrow and the owner's own words; 0.8 fixed the room
  and the tone and left the unit uncovered. **Three text findings, and one is mine**: an object
  whose CONTENT is text may not be named at all — cell 2's *notebook filled to the foot of the
  page* was written by me one set after the unlabelled-object rule went in; the product's own label
  garbled at THREE words, so the two-words-render-clean claim is weaker than it was written and the
  real variable is size and angle; and G1 beats the label rule where a real product ships an
  instruction panel, as cell 4's mandoline does. **The declared removal is vindicated**: the four
  cells whose duplicated evidence constraint was cut all landed their evidence, while cell 6 kept
  its pair and failed on evidence anyway — the duplication was doing no work. The control was drawn
  once where the set asked for two, for the second set running.
- 0.8 (2026-09-10): **set 3 rendered, the dark-mass hypothesis is REFUTED by its own control, and
  the owner named what replaces it.** Six of six opened and graded under ADR-011: **2 pass, 1
  partial, 3 fail**. Owner: *"đối tượng sử dụng (chủ thể) trong ảnh cần phải thể hiện được sự tiện
  nghi, thoải mái, môi trường tươi sáng… ưu tiên nền sáng, tone sáng, tự nhiên, mang lại cảm giác
  thoải mái, chân thực (không phải chân thực kiểu đồ vật lộn xộn, cũ)"*. **The clause landed and
  the target was wrong**: cell 1 was written for deep dark and returned median value 0.18 with 45%
  of pixels below 0.15, against 0.6's editorial column of 0.18 / 44%; cell 5 was written bright and
  returned 0.87 / 6%. **The CONTROL is the best frame in the set** at 0.67 / 3% / 0.20 — inside the
  column 0.6 called *stock* — and set 3 had predicted those three numbers correctly while
  predicting the wrong verdict for them. 0.6's table is right as measurement and inverted as
  judgement. **`PARTS/light` replaced**: a bright naturally lit place with the SURFACES named, and
  where the product forbids one, the frame shows the problem already solved — the dark is the
  product's stage, never the reader's experience. **`PARTS/grade` replaced**: natural and true, and
  authentic is not shabby. **New `PARTS/comfort`** with its own skeleton slot, because cell 5
  proved the relief clause loses when it has no slot of its own. **The anti-method now outranks
  every method**, on a fourth instance and a precedence set by cell 5 — a correctly written muscles
  clause lost to a `[SUBJECT]` line describing sun and sweat. **New product class `symptom-shaped`,
  REFUSED**: a cooling vest works by being wet and the heat it relieves also makes a person wet, so
  no wording separates them. **`PARTS/environment` gains cared-for** and loses 0.7's dark-mass
  justification. **SLOT CONSTRAINTS: naming the scene object unlabelled**, after cell 3 shipped a
  binding no-text constraint and still returned a gibberish back-of-pack panel, because the prompt
  had asked for a jar of preserve and a jar of preserve has a label — a prohibition losing to a
  named thing, 0 of 12 again. Two instrument notes: 0.6's saturation column is a MEAN over all
  pixels, found by recomputing its four published rows and matching to 0.004 before any new figure
  was published; and a warm-hue share that ranked set 3 almost exactly by eye was **discarded for
  failing its control**, with no figure from it published. The control was drawn once where the set
  asked for two, so *bright is better* is not yet a rule — what is established is that 0.7's
  prediction is refuted, which needed only that one draw.
- 0.7 (2026-09-10): **0.6 decided the light and grade rewrite and did not apply it; 0.7 applies
  it, and the file's own corpus refutes a second inherited clause.** No render since 0.6 — this
  is a restructure and the set that tests it. **The leak, found by reading the file top to bottom
  before writing set 3**: `PARTS/light` still read *even natural daylight, bright, soft shadows*,
  `PARTS/grade` still read *a natural palette*, the SKELETON's call-map still read *plain
  daylight, no glamour* and *muted, desaturated*, and NEGATIVE still banned *golden hour*, *warm
  flattering light*, *glamour lighting* and *saturated colors* — every one of them the thing 0.6's
  own CHANGELOG entry said had been released. A set written from this file would have shipped the
  fault it was testing. CLAUDE.md rule 6c's failure mode, inside one file, and a sweep for the
  eight phrases puts every other hit in a record of what was rendered (`sets/`, `round-*/`,
  `eval/`, `query/sessions/`), in another type's own law (`06-relief-scene`, `01-pain-scene`,
  `lede-pain`, `lede-authority` — different corpora, and rules do not cross them), or in
  `toplist-instruction.md`'s role-vs-value table, where the phrase is quoted AS the fault and is
  correct where it stands. **`PARTS/register` was leaking the same way since 0.4** — BOUNDARY has
  quoted *"a candid documentary photograph a passer-by could have taken"* as the UGC register G14
  refuses, for three versions, while the clause itself sat unchanged forty lines below; *"not
  lit"* in the same sentence is the seed of the whole light fault. Both struck. **New clause
  shape for `light`**: one key named by source, position and hardness; what it lands on; and what
  stays dark **as a share of the frame** — 0.6 wrote *how much of the frame sits below mid-grey*,
  which asks for a measurement, and this namespace lands measurements 0 of 12 against 15 of 15 for
  a share. **`grade` names a colour position and one carrying colour**, the fourth repair of the
  role-vs-value default. **`PARTS/environment` rewritten as a FAULT**: the copy said *never set
  at home*, and this type's only corpus MATCH is a man brushing his teeth in a dark bathroom while
  set 2's best frame is a car interior — the demand on the body is the thing, publicness was the
  proxy, and an interior is also the only place a dark mass can be put. n = 1 corpus + 3 renders.
  Set 3 tests the light axis at three depths against a control holding all four released bans, and
  splits dark mass from colour with one bright, strongly coloured cell.
- 0.6 (2026-09-10): **set 2 rendered — the seven methods land 5 of 5 and the control returns
  neutral exactly as predicted.** Effect as matter (paint blistering with stripped wood behind
  and unstripped ahead), the forbidden act (a knee folded to the heel, both hands in the soil),
  work only the benefit allows (fingers visibly loose on a running breaker), comparison as an
  object (one windscreen, half iced and half clear), and muscles named (brow smooth, jaw loose,
  shoulders dropped) all delivered; the control, carrying set 1's absences word for word,
  returned a person wearing a brace with nothing showing it works. **The prohibition diagnosis of
  0.5 is confirmed against a declared control.** Owner then named the remaining fault: *"ánh
  sáng, màu ảnh vẫn chưa đạt được editorial feel"*. `PARTS/light` and `PARTS/grade` rewritten as
  a second intended divergence from the copy — **the flat-light hypothesis is refuted** at
  spread_v median 0.68 against the namespace's own 0.67, and what separates editorial from stock
  is the MASS of the frame: median value 0.18–0.22 with 32–44% genuinely dark pixels against
  0.61–0.77 with 3–8%. Three inherited clauses cause it, and the anti-glamour NEGATIVE is split
  — flattery bans kept, light-quality bans released, values named instead. And a new SLOT
  CONSTRAINT: **the prompt's `TYPE:` header can be printed onto a product**, which cell 3's
  gloves did on the one blank branded surface in the set.
- 0.5 (2026-09-10): **set 1 rendered, the crop hypothesis is refuted, and the real fault is
  named.** Owner: *"sự dễ chịu chưa được thể hiện rõ"*. Six of six came back photographic with
  the **G14 firewall clean 6 of 6** on its first outing and the designed mat working **2 of 2** —
  but **benefit visible in 1 of 6**, and the only one that worked is the headlamp, where the
  product's effect is a beam of light on rock. **0.4's crop hypothesis is refuted**: the wide
  frames are composed as well as the tight ones and fail identically, so crop is not the
  variable. New **`PARTS/evidence`**: relief had been specified almost entirely as ABSENCES —
  *not guarding*, *no wince*, *calm* — and this namespace measured prohibitions at 0 of 12
  against 37 of 37 for things to draw. Seven methods listed, each a thing to draw, plus the
  anti-method: **never describe the problem**, which the founding round and set 1 cell 5 both did
  before leaving the relief to the product's presence.
- 0.4 (2026-09-10): **the firewall this file never had, a contradiction it shipped with, and the
  crop its own corpus shows.** Type pass opened after `lede-collage` was approved and committed
  at `4c3b95b`. **G14 was missing entirely** — `lede-authority` treats it as the load-bearing
  NEGATIVE for the same situation, and the register copied from the parent, *"a candid
  documentary photograph a passer-by could have taken"*, names the UGC register that
  `registry/toplist-instruction.md` records G14 refusing at this slot. Resolved as
  `lede-authority` resolved it: the frame is made by a PHOTOGRAPHER, not by the subject; candid
  stays, amateur goes, and NEGATIVE gains the visible tells. **MARKS is removed as an intended
  divergence (ADR-070)** — PURPOSE said *"no inset and no graphics"* while MARKS specified two
  that exist only inside one, a contradiction that shipped at 0.2; every count in it was
  borrowed from the parent's register and never re-tested here. New **`PARTS/crop`**: both
  corpus frames crop tight to the product ON a body, one of them showing no person above the
  shin, against a copied `subject` that describes a whole person mid-errand in public — n=2 and
  under SPEC §6.2's threshold, so it is recorded with its n and tested rather than legislated.
  New **`PARTS/presentation`**: 1 of 2 wraps the real photograph in a DESIGNED object, measured
  at value 0.94 and texture 3.1, which is also the second half of the G14 answer.
- 0.3 (2026-09-09): **FOUNDING RENDER ROUND** — one render, round 2 prompt 2 at 0.2,
  `partial`. Every slot landed, including the hard one: the cooler reads as the reason
  rather than as the subject. What failed is the ARGUMENT — the sleeper reads as still
  overheated, so the frame states the pain this type is the relief half of, and the prompt
  built it by asking for a plainly hot room and leaving the release to the product. Noted
  as a candidate argument fault and NOT written into `argument-faults.md` at 1 of 1.
- 0.2 (2026-09-09): **copied verbatim from `06-relief-scene` at 3.7** — owner decision,
  reversing 0.1's citation (ADR-070). PURPOSE, SKELETON, PARTS, THE RELIEF, MARKS, SLOT
  CONSTRAINTS, NEGATIVE and KNOWN-FLAKY are that file's text, spliced by script. The
  attribute gate this type used to inherit no longer reaches it — a gate keyed on
  `06-relief-scene` does not name a copy — so `result_visibility: invisible` is restated
  by toplist id in `mapping/toplist-rules.md`.
- 0.1 (2026-09-09): drafted for the top-N lede slot, inheriting `06-relief-scene`. One
  real difference from the parent, recorded rather than smoothed: the parent's `use_when`
  says *"closing image of an advertorial or final frame of an ads creative"* and this
  slot is an OPENING image. After ADR-059 and ADR-060 position is not an admission test,
  so the parent needs no edit; this file carries the lede reading. Inherits the parent's
  attribute gate — `result_visibility: invisible` drops it. ADR-069.
