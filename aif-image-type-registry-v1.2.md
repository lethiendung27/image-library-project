# AIF Image Type Registry v1.2

Bộ image type cho ảnh gallery / LP thương mại điện tử. Mỗi type gồm: mã, vai trò trên Trust Ladder, prompt skeleton, negative prompt, và trigger description cho skill router.

---

## Cú pháp đặt tên

```
{step}-{job}-{device}
```

Tất cả viết thường, nối bằng gạch ngang, không dấu, không khoảng trắng. Tên dùng được trực tiếp làm tên file, key trong JSON, và slug trong URL.

**step**: 2 chữ số, vị trí trên Trust Ladder. Sắp xếp theo thứ tự chữ cái là ra đúng thứ tự gallery.

**job**: ảnh này bán cái gì. `pain`, `symptom`, `mechanism`, `proof`, `persona`, `relief`, `use`, `spec`, `trust`

**device**: thiết bị thị giác chữ ký. `split`, `rail`, `ghostbody`, `grid`, `hero`, `demo`, `xray`, `explode`, `timeline`, `macro`

**Tỉ lệ khung KHÔNG nằm trong tên.** Cùng một type render được nhiều tỉ lệ, nên tỉ lệ là tham số truyền vào lúc chạy, không phải danh tính của type.

**Biến thể layout** dùng hai gạch: `05-persona-grid--1plus3`, `05-persona-grid--2x2`.

### Bảng đối chiếu tên cũ

| Cũ | Mới |
|---|---|
| `SQR-PAIN-XCHECK` | `01-pain-split` |
| `SQR-SCOPE-PAINRAIL` | `02-symptom-rail` |
| `SQR-MECH-GHOSTBODY` | `03-mechanism-ghostbody` |
| (chưa có) | `04-proof-demo` |
| `SQR-SCOPE-PERSONAGRID` | `05-persona-grid` |
| `BNR-RELIEF-VSINSET` | `06-relief-hero` |

---

## Registry

| Tên | Bán cái gì | Ratio khả dụng | Ver |
|---|---|---|---|
| `01-pain-split` | Dừng scroll bằng đau | 1:1, 4:5 | v1.1 |
| `02-symptom-rail` | Mở rộng phạm vi vấn đề | 1:1, 4:5 | v1.1 |
| `03-mechanism-ghostbody` | Giải thích cơ chế bên trong | 1:1, 4:5 | v1.1 |
| `04-proof-demo` | Bằng chứng vật lý | RESERVED, chưa có mẫu | |
| `05-persona-grid` | Nhận diện bản thân | 1:1, 4:5 | v1.1 |
| `06-relief-hero` | Bán trạng thái sau khi mua | 2:1, 4:5 | v1.1 |

### Schema cho máy đọc

```yaml
- id: 01-pain-split
  step: 1
  job: pain
  device: split
  version: "1.1"
  ratios: [1:1, 4:5]
  layout_variants: []
  requires_product_photo: true
  status: active
```

`step` là số nguyên để sort. `status` nhận `active`, `reserved`, `deprecated`. Type bị thay thế thì đặt `deprecated` và thêm `replaced_by`, không xóa khỏi registry.

---

## LUẬT TOÀN HỆ

### G1. Product reference (bắt buộc, đặt ở đầu mọi prompt)

```
Use the attached product photo as the exact reference for the product.
Preserve its shape, proportions, material, finish and color exactly as shown.
Do not redesign, restyle, simplify or add features.
Render it from [angle] at [scale in frame], integrated with the scene lighting.
```

### G2. Slot PRODUCT chỉ được chứa 4 thông tin

| Được phép | Cấm tuyệt đối |
|---|---|
| Vị trí trong khung | Hình dáng, đường cong, chất liệu |
| Góc nhìn | Màu sắc (trừ colorway có thật) |
| Tỉ lệ chiếm khung | Chi tiết cấu tạo (ren, gân, khóa, nút) |
| Quan hệ với vật khác | Mọi tính từ thẩm mỹ |

### G3. Ngữ nghĩa màu (khóa toàn hệ)

- **Đỏ** = đau, sai, hỏng. Chỉ xuất hiện ở vùng "vấn đề".
- **Cam** = áp lực sai, nhiệt sai.
- **Xanh dương / cyan** = nâng đỡ đúng, dòng chảy đúng, cơ chế hoạt động.
- **Xanh lá** = badge xác nhận.
- **Vàng** = cấu trúc trung tính (xương, khung).
- Không màu nào khác được phép làm tín hiệu.

### G4. Luật vế đúng

Vế "đúng" luôn sáng hơn, sạch hơn, thoáng hơn vế "sai". Không bao giờ ngược lại.

### G5. Register lock

Trong cùng một khung so sánh, hai vế phải cùng loại hình ảnh: cùng là ảnh chụp, hoặc cùng là minh họa. Không trộn.

### G6. Negative prompt nền (thêm vào mọi type)

```
text, letters, numbers, watermark, logo, deformed hands, extra fingers,
redesigned product, altered product shape, invented product details,
different product than reference
```

---

# 1. 01-pain-split v1.1

Dừng scroll bằng đau. Ảnh 2 Amazon, thumbnail ads, tile trong lưới LP.

## Skeleton

```
TYPE: 01-pain-split v1.1
RATIO: [1:1 / 4:5]  # tham số, không nằm trong tên type
LAYERS: 2 panels, hard vertical split 50/50, thin white outer border

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. Do not redesign or add features.

[LEFT PANEL: THE PROBLEM]
Desaturated grayscale photo of [age/gender] in [wardrobe],
[wrong posture/behavior] on [surface], face showing [discomfort expression].
Glowing red hotspots at [3 points], soft red radial glow,
[red jagged marks] along [affected structure].
Neutral cropped background, subject fills frame.

[RIGHT PANEL: THE ANSWER]
Full-color shot of the reference product [in place / in use] at [context],
seen from [angle], occupying [X%] of the panel.
Clean uncluttered background, bright even lighting,
noticeably brighter and cleaner than the left panel.

[BADGES]
Red circle with white X, top-left corner of left panel.
Green circle with white check, top-right corner of right panel.
Both flat, solid, same diameter.

STYLE: e-commerce comparison tile, high contrast, sharp.
Both panels must share the same lighting register and shooting style.
NO text, no logo, no watermark.
```

## Negative

```
[G6] + cluttered background on right panel, dim right panel,
mismatched photo style between panels, visible test rigs or props,
red cues on right panel, distorted face, blood, injury
```

## Trigger

```yaml
id: 01-pain-split
use_when: >
  Cần dừng scroll bằng nỗi đau, hoặc chiếm 1 ô trong gallery/grid nơi
  người xem chỉ liếc 0.5 giây. Dùng khi trạng thái sai nhìn thấy được
  bằng mắt thường.
avoid_when: >
  Ảnh chính, hoặc bất kỳ vị trí nào cần thiện cảm trước. Không dùng khi
  vấn đề vô hình.
pairs_with: 06-relief-hero (đặt sau, đóng vòng pain → relief)
```

---

# 2. 02-symptom-rail v1.1

Một sản phẩm, nhiều vấn đề. Lập luận theo chiều rộng của vấn đề.

## Skeleton

```
TYPE: 02-symptom-rail v1.1
RATIO: [1:1 / 4:5]  # tham số, không nằm trong tên type
LAYERS: photographic hero base + vector overlay + vignette rail on right edge

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. Do not redesign or add features.

[ZONE A: HERO, left 72%]
[age/gender] in [wardrobe, muted neutral tones], [correct posture/behavior]
while [everyday activity], calm content expression, [gaze direction].
The reference product clearly visible at [contact point], seen from [angle],
unobstructed, occupying at least [X%] of the hero area height.
Setting: [environment], [3 props], soft natural window light, background blurred.
Bright high-key [neutral palette] grade. Subject offset left.

[ZONE B: FORCE ARROWS]
[N] [color] rounded arrows overlaid on the product pointing [direction],
evenly spaced, semi-transparent, fading at the tips, flat vector style.
Arrow color MUST differ from the pain color used in the rail.

[ZONE C: PAIN RAIL, right 25-28%, vertical band, [straight / soft S-curved] left edge]
Pale [tint] gradient panel. [3] circular vignettes stacked evenly,
white ring border, equal diameter, generous spacing.
Each vignette: tight crop of [same-role person], no face visible,
showing [pain gesture at body zone / visible symptom],
red radial glow centered on that point.
Ordered top to bottom: [item1], [item2], [item3].
All vignettes share the hero's lighting, wardrobe tone and photographic style.

STYLE: clean e-commerce infographic tile, bright airy, sharp focus, 4K.
NO text, no logo, no watermark.
```

**Ghi chú slot vignette:** chọn 1 trong 2 biến thể và ghi rõ trong prompt.
`pain-gesture` (tay ấn vào vùng đau) dùng khi triệu chứng là cảm giác.
`visible-symptom` (biểu hiện thấy được trên cơ thể/vật) dùng khi triệu chứng là hậu quả nhìn thấy được.

## Negative

```
[G6] + faces inside vignettes, mismatched lighting between hero and vignettes,
red arrows on product, heat or warming cues, cluttered background, dark grade,
vignettes too small, overlapping circles, product obscured
```

## Trigger

```yaml
id: 02-symptom-rail
use_when: >
  Sản phẩm giải quyết nhiều vấn đề cùng lúc và cần cho thấy phạm vi bao
  phủ trong một ảnh. Ảnh 2 hoặc 3 trong gallery, ngay sau ảnh dừng scroll.
avoid_when: >
  Sản phẩm chỉ giải quyết đúng 1 vấn đề. Không dùng làm ảnh chính.
  Không dùng khi triệu chứng không quay được.
pairs_with: 01-pain-split (trước), 03-mechanism-ghostbody (sau)
```

---

# 3. 03-mechanism-ghostbody v1.1

Giải thích tại sao sản phẩm hoạt động, bằng cơ chế bên trong cơ thể. Cơ thể vô danh nên bán được cho mọi tệp.

## Skeleton

```
TYPE: 03-mechanism-ghostbody v1.1
RATIO: [1:1 / 4:5]  # tham số, không nằm trong tên type
REGISTER: 3D technical render. NOT photography. Seamless white infinity background.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. Do not redesign or add features.

[BASE: GHOST BODY]
Featureless matte white 3D mannequin, no face, no hair, no clothing, no skin tone,
shown [pose] in [interaction with product]. Body cross-sectioned at [cut plane]
to reveal interior. Soft even studio lighting, subtle grey ambient occlusion only.

[ANATOMY CUTAWAY]
[anatomical structure] rendered inside the body silhouette, not floating on top:
bone in off-white ivory, [stress element] highlighted in red.
Anatomically accurate, follows the exact contour of the product.

[PRODUCT]
The reference product, positioned [relation to body], seen from [angle],
the only object with a real material finish in the frame.
Sharp silhouette against white.
Its contour must visibly align with [anatomical structure].

[DIMS] (optional, bật khi sản phẩm có khối 3 chiều rõ ràng)
Thin black double-headed arrows measuring [dimension 1] and [dimension 2],
fine extension lines offset clear of the product outline. Drafting style.

[XCHECK] (optional, top-left corner)
Two small rounded-square panels side by side, flat 2D vector illustration,
light grey outline, white fill.
LEFT: [wrong state] with orange heat glow at [pressure point], motion squiggles.
Red circle with white X above.
RIGHT: [correct state] with blue support and yellow [structure] neutral.
Green circle with white check above.

PALETTE LOCK: achromatic white and grey everywhere. The ONLY colors permitted are
red [stress], orange [wrong pressure], blue [correct support], yellow [structure].
STYLE: clean medical-technical product render, e-commerce infographic, sharp, 4K.
NO text, no numbers, no logo, no watermark.
```

## Negative

```
[G6] + human face, facial features, hair, skin tone, clothing,
photographic background, environment, furniture, shadows on floor,
extra colors, rainbow palette, anatomically wrong structures,
floating disconnected organs, dimension lines overlapping product edge,
cluttered inset, gore, realistic flesh, medical horror
```

## Trigger

```yaml
id: 03-mechanism-ghostbody
use_when: >
  Cần giải thích TẠI SAO hình dạng sản phẩm hoạt động, bằng cơ chế bên
  trong cơ thể mà không quay được. Ảnh 3-4 trong gallery.
avoid_when: >
  Ảnh chính, ảnh dừng scroll, hoặc khi sản phẩm không tác động lên cấu
  trúc cơ thể. Type này lạnh, không có ai để đồng cảm.
pairs_with: 01-pain-split (trước), 06-relief-hero (sau)
```

---

# 4. 05-persona-grid v1.1

Trả lời câu hỏi "cái này có hợp với tôi không". Lập luận theo chiều rộng của người dùng.

## Skeleton

```
TYPE: 05-persona-grid v1.1
RATIO: [1:1 / 4:5]  # tham số, không nằm trong tên type
LAYOUT: [1plus3 / 2x2 / 1plus4], thin white 4px gutters, no outer border,
photographic collage, no graphic overlays.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly across all cells.

[MUST MATCH across cells]
Color grade and palette: [3-4 neutral tones].
Light quality: [soft / diffused / directional], never harsh or colored.
Product colorway: [one only].
Overall photographic finish: same lens character, contrast and skin rendering.

[MUST DIFFER across cells]
Age, gender and body situation of the subject.
Camera angle, one per cell, chosen from: eye-level side profile / high three-quarter /
low angle / over-the-shoulder / waist-level frontal / close crop on the interaction.
Environment type, one per cell, and shot distance (wide, medium, close).

[PRODUCT VISIBILITY RULE]
The product must be clearly visible and unobstructed in EVERY cell,
occupying at least 15% of that cell's height.
If a cell cannot meet this, tighten the crop until it does.

[HERO CELL, largest]
[most specific persona: age, gender, distinguishing condition] in [wardrobe],
[interaction with product] in [environment 1], [warm emotional expression].
Camera: [angle 1], [shot distance].

[SUPPORT CELL 1] [persona 2] in [environment 2], [activity]. Camera: [angle 2], [distance].
[SUPPORT CELL 2] [persona 3] in [environment 3], [activity]. Camera: [angle 3], [distance].
[SUPPORT CELL 3] [persona 4] in [environment 4], [activity]. Camera: [angle 4], [distance].

STYLE: clean lifestyle collage for e-commerce, bright airy, sharp focus, 4K.
NO text, no logo, no watermark, no badges, no arrows.
```

**Luật casting:** ô lớn nhất luôn dành cho persona có tình trạng cụ thể nhất và cảm xúc mạnh nhất, không phải persona đông nhất.

## Negative

```
[G6] + borders around cells, badges, arrows,
product hidden or cropped out in any cell, product smaller than 15% of cell height,
different product colors between cells, mismatched color grade between cells,
one cell darker than the others, identical camera angles, repeated framing,
same environment twice, stock photo collage look, duplicate-looking people
```

## Trigger

```yaml
id: 05-persona-grid
use_when: >
  Cần cho thấy nhiều kiểu người khác nhau đang dùng. Ảnh 4-5 trong
  gallery hoặc ảnh chốt cuối. Dùng khi tệp khách rộng về tuổi và bối cảnh.
avoid_when: >
  Tệp khách hẹp và cụ thể. Không dùng làm ảnh chính. Không dùng nếu sản
  phẩm quá nhỏ để nhìn thấy trong ô con.
pairs_with: 02-symptom-rail (cùng tầng, khác trục)
```

---

# 5. 06-relief-hero v1.1

Bán trạng thái sau khi mua. Ba lớp ghép chồng, mỗi lớp một việc.

## Skeleton

```
TYPE: 06-relief-hero v1.1
RATIO: [2:1 / 4:5]  # tham số, không nằm trong tên type
LAYERS: 3 (hero base + inset panel + product view)

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. Do not redesign or add features.
The product must be identical in every layer of this image.

[ZONE A: HERO, right 60%]
[age/gender] in [wardrobe, tone matching background],
[relief pose] while [activity], [warm expression].
The product visible at [contact point], seen from [angle A], unobstructed.
Setting: [environment], [3 props], [light source]. Background blurred,
high-key [neutral palette] grade. Subject offset right, empty mid-frame for headline.

[ZONE B: PRODUCT VIEW, bottom-left foreground, front z-layer]
The same product from the reference, shown from [angle B, MUST differ from angle A
and reveal the side hidden in Zone A], floating above the surface,
occupying [20-30%] of the frame width.
Studio lighting, soft contact shadow, razor sharp, clean cutout edge.
[IF product has multiple real colorways: show 2 units, colorways: [c1], [c2].
 IF single colorway: show 1 unit only.]

[ZONE C: INSET, top-left, white 3px border, split 50/50, red circular VS badge at seam]
LEFT: desaturated grayscale [wrong state], glowing red hotspots at [3 points].
RIGHT: full-color [correct state] with [blue/cyan] overlay showing [mechanism].
Both halves must share the same register (both photographic, or both illustrated).
Right half brighter and cleaner than left half.

STYLE: clean commercial e-commerce banner, bright airy, sharp focus, 4K.
NO text, no logo, no watermark.
```

**Luật Zone B:** chỉ tồn tại nếu nó cho thấy góc nhìn mà Zone A bị che khuất. Nếu không có góc nào mới để show, bỏ Zone B.

**Luật đau:** đau chỉ tồn tại trong Zone C. Zone A phải 100% relief. Không bao giờ trộn.

## Negative

```
[G6] + cluttered background, dark moody lighting, pain cues in main scene,
blurry product, inconsistent product between layers, same angle repeated,
fabricated colorways, mixed illustration and photo inside one inset half
```

## Trigger

```yaml
id: 06-relief-hero
use_when: >
  Sản phẩm giải quyết một vấn đề mà người mua đã tự cảm nhận nhưng chưa
  gọi tên. Cần vừa chứng minh sai/đúng, vừa show sản phẩm, vừa bán cảm
  giác nhẹ nhõm, trong 1 ảnh. Ảnh phụ Amazon A+, banner LP, ảnh 2-3.
avoid_when: >
  Sản phẩm không có "trạng thái sai" nhìn thấy được, hoặc cần zoom vào
  cơ chế bên trong (dùng 03-mechanism-ghostbody thay thế).
```

---

# Quy trình test và vá

## Mẫu feedback

```
TYPE: [mã type] v[số]
SẢN PHẨM: [tên]
KẾT QUẢ: [pass / partial / fail]
SAI Ở ĐÂU:
  - ZONE [A/B/C] | slot [tên slot] | hiện tượng: [AI vẽ ra cái gì]
LẶP LẠI: [số lần lỗi / số lần chạy]
```

## Quy tắc vá

1. Lỗi lặp từ 2/3 lần chạy trở lên thì sửa vào skeleton. Lỗi 1 lần thì ghi vào known-flaky, không đụng skeleton.
2. Lỗi do model yếu (tay, chữ, khuôn mặt) thì đẩy xuống negative, không phình phần mô tả.
3. Lỗi do slot mơ hồ thì tách slot đó thành 2 slot cụ thể hơn.
4. Mỗi lần sửa tăng minor version. Đổi cấu trúc lớp thì tăng major version.
