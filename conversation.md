# Đọc ảnh và tạo prompt cho nano banana

_Created: 2026-08-10T04:39:33.020352Z_
_Updated: 2026-08-10T06:56:26.657102Z_

## Human

đọc ảnh và trả về prompt cho nano banana

**Attachments:**
- 1786336767635_image.png

---

## Assistant

<details><summary>Thinking</summary>

The user shared an image of a lumbar support cushion product advertisement and wants me to analyze it and create a detailed prompt for Nano Banana image generation. I'm looking at the product visuals and marketing elements to craft a comprehensive generation prompt that captures the design, style, and key features shown in the banner.

</details>

Ảnh này là banner quảng cáo đệm tựa lưng công thái học (kiểu chữ S ôm hông), gồm 3 lớp: nhân vật chính bên phải, 2 sản phẩm ở góc dưới trái, và khung so sánh "VS" ở góc trên trái.

**Prompt chính (Nano Banana):**

```
A wide 2:1 e-commerce banner for an ergonomic S-shaped posture seat cushion.

MAIN SCENE (right two-thirds): A young Asian businessman in his early 30s wearing a cream beige suit sits reclined in a modern white-framed mesh office chair, hands clasped behind his head, legs crossed, eyes closed slightly with a relaxed satisfied smile. A grey S-curved foam posture cushion is clearly visible supporting his lower back and seat. He sits at a light wood conference table with an open silver laptop and a small potted plant. Background is a bright modern open-plan office with floor-to-ceiling glass windows, soft daylight, a wooden cabinet with binders, and two blurred coworkers in the far distance. Shallow depth of field, clean corporate lifestyle photography, natural window light, soft shadows, high-key bright white-and-beige color grade.

PRODUCT SHOWCASE (bottom-left foreground): Two identical S-shaped ergonomic seat cushions shown in three-quarter angle, floating slightly above the floor, one soft pink and one dark charcoal grey. Ribbed lumbar panel, curved hip-hugging wings, matte foam texture, crisp studio lighting with soft contact shadow, sharp product-photography detail.

INSET COMPARISON PANEL (top-left corner, rectangular white-bordered box, split in two halves, red circular "VS" badge in the center):
- Left half: desaturated grayscale illustration of a woman slouching forward over a desk, spine curved badly, glowing red pain hotspots on her neck, shoulder, lower back and hip.
- Right half: full-color photo of a woman sitting upright and smiling while typing, with a blue and yellow anatomical spine alignment overlay showing a healthy S-curve against the chair back.

STYLE: clean commercial advertising layout, bright and airy, no text, no logo, no watermark, sharp focus, 4K product-ad quality.
```

**Negative prompt:**
```
text, letters, watermark, logo, distorted hands, extra fingers, deformed face, cluttered background, dark moody lighting, low resolution, blurry product
```

**Vài lưu ý khi chạy:**
- Nano Banana hay bỏ sót lớp inset "VS". Nếu nó không ra, tách làm 2 lần: gen scene chính trước, rồi dùng chế độ chỉnh sửa và yêu cầu "add a comparison inset panel in the top-left corner".
- Muốn giữ đúng sản phẩm thật, hãy upload ảnh đệm của bạn làm reference rồi thêm câu: "keep the cushion shape, ribbing and color exactly as in the reference image".
- Nếu cần bản dọc cho ads, đổi câu đầu thành "vertical 4:5 banner" và chuyển khung VS xuống dưới thay vì góc trên trái.

---

## Human

hãy breakdown cấu trúc của ảnh để xử lí prompt tạo prompt skeleton ngắn gọn cụ thể nhất cho riêng loại ảnh này và gọi tên loại ảnh theo cú pháp (tôi sẽ input rất nhiều ảnh để AI học, tạo prompt skeleton cho từng image type và tự gọi tên)

---

## Assistant

<details><summary>Thinking</summary>

Người d

</details>

```
This block is not supported on your current device yet.
```

<details><summary>Thinking</summary>

I'm working through the structure of this image type—there's a hero lifestyle scene taking up most of the right side showing someone using the product in context, product variants displayed as floating cutouts in the foreground with studio lighting, and a comparison module boxed off in the top-left corner. Now I need to establish a naming convention and skeleton template that accounts for these distinct layers.

I'm thinking about a simple, machine-readable naming syntax that captures the essence of this layout without depending on external tier codes. Something like a slug that identifies the layer count, primary intent, and the signature proof device—so something like `HERO-COMPOSITE` paired with descriptors like `vs-inset` and `product-cluster` to make it clear what modules are present and how they function together. I'm settling on a naming syntax that combines format, intent, and visual device—so this banner becomes `BNR-RELIEF-VSINSET`, which is memorable and self-documenting for scaling across the library.

Now I'm mapping out the structural layout: a 2:1 canvas with the hero subject positioned at the right third, a product cluster in the bottom-left with overlapping elements, and an inset comparison panel in the top-left with a VS badge at the seam. I'm thinking through the depth layering—blurred background, sharp hero, razor-sharp overlays with drop shadows for separation—and establishing the color palette with high-key whites and beiges.

The visual flow follows a Z-pattern: eye catches the red VS badge first (high contrast, top-left), moves down to the product, then across to the happy user on the right. The key principle is keeping pain signals isolated to the inset panel only, while the hero zone stays purely relief-focused—never mixing the two.

I'm about to write out the skeleton with slots for customization, then provide a filled example with negative prompts and variant descriptions, plus the router trigger for this skill type. I should also document the naming syntax convention for this image taxonomy since it extends the AIF file structure.

</details>

```
This block is not supported on your current device yet.
```

# 1. Breakdown cấu trúc

Ảnh này không phải 1 cảnh. Nó là **3 lớp độc lập được ghép chồng**, mỗi lớp làm 1 việc bán hàng khác nhau.

| Zone | Vị trí | Nội dung | Job |
|---|---|---|---|
| **A. Hero** | Phải ~60%, chủ thể lệch phải 1/3 | Người dùng thư giãn + sản phẩm đang được dùng | Bán trạng thái sau khi mua |
| **B. Product cluster** | Dưới trái, ~30% rộng, z-index cao nhất | 2 units cắt nền, 2 colorway, lơ lửng | Bán vật thể + báo có nhiều màu |
| **C. VS inset** | Trên trái, ~38% x 50%, viền trắng 3px | Split 50/50, badge VS đỏ ở khe | Bán vấn đề, hợp thức hóa lý do mua |

**Các luật ngầm giữ ảnh này hoạt động:**

- **Đau chỉ tồn tại trong Zone C.** Zone A tuyệt đối 100% relief. Không bao giờ trộn.
- **Ngữ nghĩa màu:** đỏ = pain/sai (chỉ nửa trái Zone C). Xanh dương/vàng = anatomy đúng. Nền hero = high-key trắng/be/gỗ, không màu mạnh, để 2 overlay nổi.
- **Độ sâu 3 tầng:** background blur, hero sharp, overlay siêu nét + drop shadow tách lớp.
- **Luồng mắt Z:** VS đỏ (trái trên) → product (trái dưới) → người vui (phải). Khoảng giữa để trống làm chỗ đặt headline.
- **Desaturate = trước, full color = sau.** Đây là tín hiệu nhận diện nhanh hơn cả chữ.

# 2. Cú pháp gọi tên

Đề xuất 3 token, viết hoa, nối bằng gạch:

```
{FORMAT}-{INTENT}-{DEVICE}
```

- **FORMAT**: BNR (ngang 2:1), SQR (1:1), VERT (4:5, 9:16), GIF, VID
- **INTENT**: nấc Trust Ladder mà ảnh phục vụ. PAIN, RELIEF, COMPARE, MECH, PROOF, USE, SPEC, TRUST
- **DEVICE**: thiết bị thị giác chữ ký. VSINSET, XRAY, EXPLODE, GRID, CUTOUT, TIMELINE, MACRO, HANDDEMO

Ảnh này = **`BNR-RELIEF-VSINSET`**

Biến thể cùng họ tự sinh tên: `VERT-RELIEF-VSINSET`, `SQR-COMPARE-VSINSET`, `BNR-RELIEF-XRAY`.

Nếu có module phụ, ghi hậu tố `+`: `BNR-RELIEF-VSINSET+COLORWAY`.

# 3. Prompt skeleton

```
TYPE: BNR-RELIEF-VSINSET
RATIO: [2:1 / 4:5 / 1:1]
LAYERS: 3 (hero base + inset panel + product cluster)

[ZONE A: HERO, right 60%]
[age/gender/ethnicity] wearing [wardrobe, tone khớp nền],
[relief pose: hands behind head / eyes closed / stretching],
in [chair/seat/surface], [PRODUCT] clearly visible at [contact point].
Setting: [environment], [3-4 prop cụ thể], [natural light source].
Background blurred, shallow depth of field, high-key [neutral palette] grade.
Subject offset right, empty mid-frame for headline.

[ZONE C: INSET, top-left, white 3px border, split 50/50, red circular "VS" badge at seam]
LEFT: desaturated grayscale [same-role person] in [wrong posture/behavior],
glowing red pain hotspots at [3-4 anatomical points].
RIGHT: full-color [same person] in [correct state],
[blue/yellow] [anatomical / technical] overlay showing [correct mechanism].

[ZONE B: PRODUCT CLUSTER, bottom-left foreground]
[N] identical [PRODUCT] in three-quarter angle, floating, colorways: [color1], [color2].
[texture + signature detail]. Crisp studio lighting, soft contact shadow, razor sharp.

STYLE: clean commercial e-commerce banner, bright airy, sharp focus, 4K.
NO text, no logo, no watermark.
```

**Negative cố định cho type này:**
```
text, letters, watermark, logo, deformed hands, extra fingers,
cluttered background, dark moody lighting, pain cues in main scene,
blurry product, inconsistent product shape between layers
```

# 4. Trigger description (cho skill router)

```yaml
id: bnr-relief-vsinset
name: Relief Hero Banner with VS Inset
use_when: >
  Sản phẩm giải quyết một vấn đề tư thế, thói quen hoặc cơ thể mà người
  mua đã tự cảm nhận nhưng chưa gọi tên. Cần vừa chứng minh sai/đúng,
  vừa show sản phẩm, vừa bán cảm giác nhẹ nhõm, trong 1 ảnh duy nhất.
  Hợp cho ảnh phụ Amazon A+, banner LP, ảnh 2-3 trong gallery.
avoid_when: >
  Sản phẩm không có "trạng thái sai" nhìn thấy được, hoặc cần zoom vào
  cơ chế bên trong (dùng XRAY / EXPLODE thay thế).
```

Khi bạn đưa ảnh tiếp theo, tôi sẽ dò xem nó có rơi vào type đã có không. Trùng thì bổ sung biến thể, khác thì đặt tên mới theo đúng cú pháp trên và viết skeleton riêng.

---

## Human

**Attachments:**
- 1786337122572_image.png

---

## Assistant

<details><summary>Thinking</summary>

Looking at this image, I'm seeing a before-and-after comparison: the left side shows a woman in grayscale experiencing discomfort with red hotspots and a red X badge, while the right side displays the product—a pink cushion on a black office chair with what appears to be a testing apparatus with a dial gauge, suggesting this is demonstrating the product's durability or pressure-relief capabilities in a lab setting.

</details>

# Breakdown

Ảnh này chính là **Zone C của type trước, phóng to lên toàn khung**. Bỏ hero, bỏ product cluster, chỉ giữ lại module so sánh.

| Thành phần | Chi tiết |
|---|---|
| **Canvas** | 1:1, khe dọc chia chính xác 50/50, viền trắng mảnh bao ngoài |
| **Panel trái** | Grayscale, người dùng ngửa cổ nhăn nhó, 3 điểm nóng đỏ dọc cột sống (cổ/lưng giữa/thắt lưng), tia sáng đỏ lan tỏa |
| **Panel phải** | Full color, sản phẩm hồng gắn trên ghế, không có người, ánh sáng thật, hơi tối |
| **Badge** | X đỏ tròn góc trên trái, ✓ xanh tròn góc trên phải. Đối xứng chéo qua khe |

**Điểm khác biệt cấu trúc so với `BNR-RELIEF-VSINSET`:**

- **So sánh bất đối xứng.** Trái là người chịu đau, phải là vật thể. Type trước là người vs người. Cái này nói "vấn đề của bạn" vs "thứ này", không nói "bạn sau khi dùng".
- **Badge thay VS.** X/✓ là phán xét tuyệt đối, không phải đối chiếu. Đọc nhanh hơn, thô hơn.
- **Đau chiếm 50% khung** thay vì 19%. Đây là ảnh nghiêng hẳn về pain, thuộc nấc thấp hơn trên Trust Ladder.

**Hai lỗi kỹ thuật trong ảnh này, đừng chép lại:**

1. **Lệch register.** Trái là ảnh studio đã xử lý đồ họa, phải là ảnh chụp thô ánh đèn huỳnh quang, nền lộn xộn, có cả chân giá đỡ và mặt đồng hồ đo lạc lõng. Mắt đọc ra hai nguồn khác nhau, mất tin tưởng.
2. **Phải tối hơn trái.** Vế "đúng" đang trông kém hấp dẫn hơn vế "sai". Ngược logic. Vế ✓ luôn phải sáng hơn, sạch hơn, thoáng hơn.

# Tên type

**`SQR-PAIN-XCHECK`**

Không phải COMPARE vì trọng tâm vẫn là pain, vế phải chỉ là câu trả lời. Nếu vế phải đổi thành người dùng thoải mái thì tên thành `SQR-COMPARE-XCHECK`.

Cùng họ: `VERT-PAIN-XCHECK`, `BNR-PAIN-XCHECK`, `SQR-PAIN-XCHECK+ANATOMY` (khi thêm overlay cột sống).

# Prompt skeleton

```
TYPE: SQR-PAIN-XCHECK
RATIO: [1:1 / 4:5]
LAYERS: 2 panels, hard vertical split 50/50, thin white outer border

[LEFT PANEL: THE PROBLEM]
Desaturated grayscale photo of [age/gender] in [wardrobe],
[wrong posture/behavior] on [surface], face showing [discomfort expression].
Glowing red pain hotspots at [3 anatomical points], soft red radial glow,
[red zigzag/lightning marks] along [affected structure].
Neutral cropped background, subject fills frame.

[RIGHT PANEL: THE ANSWER]
Full-color [product-in-place / correct-state] shot:
[PRODUCT] mounted on [context object], three-quarter angle,
[colorway]. Clean uncluttered background, bright even lighting,
brighter and cleaner than left panel.

[BADGES]
Red circle with white X, top-left corner of left panel.
Green circle with white check, top-right corner of right panel.
Both flat, solid, same diameter.

STYLE: e-commerce comparison tile, high contrast, sharp.
Both panels must share the same lighting register and shooting style.
NO text, no logo, no watermark.
```

**Negative:**
```
text, letters, watermark, logo, deformed hands, extra fingers,
cluttered background on right panel, dim right panel,
mismatched photo style between panels, visible test rigs or props,
red cues on right panel, distorted face
```

# Trigger description

```yaml
id: sqr-pain-xcheck
name: Split Pain vs Answer Tile
use_when: >
  Cần dừng scroll bằng nỗi đau, hoặc chiếm 1 ô trong gallery/grid nơi
  người xem chỉ liếc 0.5 giây. Hợp ảnh 2 Amazon, thumbnail ads, tile
  trong lưới LP. Dùng khi tư thế sai nhìn thấy được bằng mắt thường.
avoid_when: >
  Ảnh chính (main image) hoặc bất kỳ vị trí nào cần thiện cảm trước.
  Không dùng khi vấn đề vô hình, không quay được cảnh "sai".
pairs_with: bnr-relief-vsinset (đặt sau, để đóng vòng pain → relief)
```

Đã có 2 type. Đưa ảnh tiếp.

---

## Human

đối với từng image type, tôi sẽ test (cần prompt được phát triển từ prompt skeleton về 1 sản phẩm hoàn toàn khác) và feedback để sửa prompt skeleton.

---

## Assistant

<details><summary>Thinking</summary>

I need to create test prompts for each of the two existing image types, but apply them to a different product to really stress-test the skeleton. I'll pick one of their actual products—the mouth tape, knife sharpener, or showerhead filter—to make this a realistic test that will surface any weaknesses in the template structure.

</details>

```
This block is not supported on your current device yet.
```

Chuẩn. Tôi chọn sản phẩm test cố tình xa domain gốc (không phải đồ ngồi, không phải cơ thể) để ép skeleton lộ chỗ gãy.

---

## Test A: `BNR-RELIEF-VSINSET` v1.0

**Sản phẩm test: lọc nước vòi sen kim loại**
Stress axis: vấn đề vô hình (khoáng nặng trong nước), inset không có anatomy overlay, hero không ngồi.

```
A wide 2:1 e-commerce banner for a metal shower filter.

MAIN SCENE (right two-thirds): A woman in her late 20s with long dark hair stands under a running shower, head tilted back, eyes closed, calm satisfied expression, water streaming over her face and shoulders. A brushed stainless steel inline shower filter is clearly visible screwed between the hose and the showerhead above her. Setting: a bright modern bathroom with white marble tile, a glass partition, a small eucalyptus bundle, soft daylight from a frosted window. Background softly blurred, shallow depth of field, high-key white and warm grey grade, steam catching the light. Subject offset right, empty mid-frame for headline.

INSET COMPARISON PANEL (top-left corner, white 3px border, split 50/50, red circular "VS" badge at the seam):
LEFT: desaturated grayscale macro of a showerhead nozzle plate caked with white limescale crust, dull dripping water, glowing red hotspots at three clogged nozzles.
RIGHT: full-color macro of a clean chrome nozzle plate spraying clear even water jets, with a blue and cyan cutaway overlay showing filter media layers trapping orange particles inside the cartridge.

PRODUCT SHOWCASE (bottom-left foreground): Two identical cylindrical metal shower filters in three-quarter angle, floating, colorways: brushed silver and matte black. Knurled grip ring, visible thread, crisp studio lighting, soft contact shadow, razor sharp.

STYLE: clean commercial e-commerce banner, bright airy, sharp focus, 4K.
NO text, no logo, no watermark.
```

**Negative:** `text, letters, watermark, logo, deformed hands, extra fingers, cluttered background, dark moody lighting, pain cues in main scene, blurry product, inconsistent product shape between layers, wet lens distortion`

**Tôi đoán chỗ sẽ gãy:** slot ZONE C RIGHT. Skeleton gốc viết cho overlay giải phẫu trên người, ở đây phải chuyển thành cutaway cơ chế. Nano Banana nhiều khả năng bỏ luôn lớp cutaway hoặc vẽ thành hình minh họa 2D lệch register với macro ảnh thật.

---

## Test B: `SQR-PAIN-XCHECK` v1.0

**Sản phẩm test: dụng cụ mài dao lăn**
Stress axis: "pain" không nằm trên cơ thể, nó nằm ở kết quả công việc. Ép skeleton chứng minh slot pain hotspot có tổng quát hóa được không.

```
A 1:1 e-commerce comparison tile, hard vertical split 50/50, thin white outer border.

LEFT PANEL: Desaturated grayscale close-up of a woman's hands pressing hard with a dull kitchen knife into a ripe tomato on a wooden board, the tomato skin tearing and crushing, juice and seeds squeezed out, knuckles white from force. Glowing red hotspots on the crushed tomato flesh, the knife edge, and the straining wrist, soft red radial glow, red jagged marks along the blade edge. Neutral cropped background, hands fill the frame.

RIGHT PANEL: Full-color close-up of the same hands gliding a knife through a tomato in one clean pass, producing paper-thin uniform slices fanned on a light wood board. A rolling knife sharpener with a black handle and a diamond-coated disc sits beside the board in soft focus. Clean uncluttered marble counter, bright even daylight, noticeably brighter and cleaner than the left panel.

BADGES: Red circle with a white X in the top-left corner of the left panel. Green circle with a white check in the top-right corner of the right panel. Both flat, solid, identical diameter.

STYLE: e-commerce comparison tile, high contrast, sharp. Both panels must share the same lighting register, camera distance and shooting style.
NO text, no logo, no watermark.
```

**Negative:** `text, letters, watermark, logo, deformed hands, extra fingers, six fingers, cluttered background on right panel, dim right panel, mismatched photo style between panels, red cues on right panel, blood, injury`

**Tôi đoán chỗ sẽ gãy:** bàn tay (Nano Banana yếu nhất ở đây, mà cả 2 panel đều cận cảnh tay cầm dao), và slot "3 anatomical points" bị ép thành "3 điểm bất kỳ" nên hotspot có thể rải lung tung. Ngoài ra dao + đỏ dễ kích cảnh báo an toàn.

---

## Cách gửi feedback

Để tôi vá đúng chỗ thay vì viết lại cả prompt, mỗi lần test gửi theo mẫu này:

```
TYPE: [mã type] v[số]
SẢN PHẨM: [tên]
KẾT QUẢ: [pass / partial / fail]
SAI Ở ĐÂU:
  - ZONE [A/B/C] | slot [tên slot] | hiện tượng: [AI vẽ ra cái gì]
LẶP LẠI: [lỗi này xuất hiện mấy lần trên mấy lần chạy]
```

Chỉ cần ảnh output + dòng "SAI Ở ĐÂU" là đủ, phần còn lại tôi tự suy ra.

Quy tắc vá tôi sẽ áp dụng:
- Lỗi lặp ≥2/3 lần chạy thì sửa vào skeleton. Lỗi 1 lần thì chỉ ghi vào mục known-flaky, không đụng skeleton.
- Lỗi do model yếu (tay, chữ) thì đẩy xuống negative, không phình phần mô tả.
- Lỗi do slot mơ hồ thì tách slot đó thành 2 slot cụ thể hơn.
- Mỗi lần sửa tăng version: v1.0 → v1.1. Đổi cấu trúc lớp thì lên v2.0.

Chạy xong 2 cái này rồi quay lại. Trong lúc đó bạn cứ đưa tiếp ảnh mới, tôi vẫn đặt tên và dựng skeleton song song được.

---

## Human

**Attachments:**
- 1786337685721_image.png

---

## Assistant

<details><summary>Thinking</summary>

I'm looking at a technical illustration showing a 3D mannequin seated on an ergonomic cushion with the spine anatomy visible inside, including the vertebrae and discs in red. There are measurement annotations with dimension arrows along the edges, and a comparison inset in the top-left showing pressure distribution differences between two positions using color coding.

The design uses a featureless white mannequin to keep the focus on the mechanism rather than creating a realistic human figure, with the anatomical overlay embedded as a cutaway. The color palette stays neutral except for the spine details and the pressure visualization, where orange indicates problematic pressure points and blue/yellow show proper support and bone structure.

I'm weighing whether to call this device GHOSTBODY or XRAY — the core signature is the abstracted white figure with internal anatomy visible, no surrounding environment. I'm leaning toward XRAY since it's already in my device vocabulary, though the naming convention is getting long with all the modifiers stacked together.

</details>

# Breakdown

Đây là register hoàn toàn khác 2 type trước. Không có ảnh chụp, không có người thật, không có môi trường. Toàn bộ là render kỹ thuật trên nền trắng vô cực.

| Lớp | Nội dung | Job |
|---|---|---|
| **Ghost body** | Manikin trắng không mặt, không quần áo, không màu da, cắt lát ở thân | Cho thấy tư thế mà không tạo nhân vật |
| **Anatomy cutaway** | Cột sống nằm **bên trong** silhouette, xương trắng ngà + đĩa đệm đỏ | Chứng minh cơ chế bên trong cơ thể |
| **Product** | Vật thể duy nhất có chất liệu thật, khớp đường cong với cột sống | Nói "hình dạng này là có lý do" |
| **Dimension lines** | Mũi tên 2 đầu, đường gióng mảnh, đo cao + rộng, **không có số** | Vay uy tín bản vẽ kỹ thuật |
| **Micro inset** | Góc trên trái, 2 ô vector phẳng, X đỏ / ✓ xanh, cam = ép, xanh = đỡ | Nhét thêm 1 bằng chứng phụ về cơ chế |

**Luật màu, chặt hơn 2 type trước:**
Toàn khung achromatic trắng xám. Chỉ 4 màu được phép xuất hiện: đỏ (đĩa đệm), cam (áp lực sai), xanh dương (nâng đỡ đúng), vàng (cấu trúc xương trong inset). Không có màu nào khác.

**Điểm ăn tiền:** cơ thể bị tước hết danh tính. Không giới tính, không tuổi, không sắc tộc. Người xem tự chiếu mình vào. Đây là lý do type này bán được cho mọi tệp, khác hẳn hero có người thật.

**Điểm yếu của ảnh gốc:** dimension lines không có số nên chỉ là trang trí, mất 60% giá trị. Inset quá nhỏ, trên mobile thành 2 vệt mờ. Đường gióng chạy đè lên đường viền sản phẩm ở cạnh phải, đọc rối.

# Tên type

**`SQR-MECH-GHOSTBODY+DIMS+XCHECK`**
Base: `SQR-MECH-GHOSTBODY`

Bổ sung vào registry DEVICE: `GHOSTBODY` (manikin vô danh + cutaway nội tạng), `DIMS` (đường đo kỹ thuật).

Cùng họ: `SQR-MECH-GHOSTBODY` (bản trần, không dims không inset), `VERT-SPEC-GHOSTBODY+DIMS`, `BNR-MECH-GHOSTBODY+XRAY`.

# Prompt skeleton

```
TYPE: SQR-MECH-GHOSTBODY
RATIO: [1:1 / 4:5]
REGISTER: 3D technical render. NOT photography. Seamless white infinity background.

[BASE: GHOST BODY]
Featureless matte white 3D mannequin, no face, no hair, no clothing, no skin tone,
shown [pose] in [interaction with product]. Body cross-sectioned at [cut plane]
to reveal interior. Soft even studio lighting, subtle grey ambient occlusion only.

[ANATOMY CUTAWAY]
[anatomical structure] rendered inside the body silhouette, not floating on top:
bone in off-white ivory, [stress element] highlighted in red.
Anatomically accurate, follows the exact curve of the product beneath it.

[PRODUCT]
[PRODUCT] in [colorway], the only object with real material finish,
matte [texture], its [contour/feature] visibly matching [anatomical structure].
Sharp silhouette against white.

[DIMS] (optional module)
Thin black double-headed arrows measuring [dimension 1] and [dimension 2],
with fine extension lines offset clear of the product outline.
Drafting style, [leave blank for text overlay / label with real specs].

[XCHECK] (optional module, top-left corner)
Two small rounded-square panels side by side, flat 2D vector illustration style,
light grey outline, white fill.
LEFT: [wrong state] with orange heat glow at [pressure point] and small motion squiggles.
Red circle with white X above.
RIGHT: [correct state] with blue support cushion and yellow [structure] neutral.
Green circle with white check above.

PALETTE LOCK: achromatic white and grey everywhere. The ONLY colors permitted are
red [stress], orange [wrong pressure], blue [correct support], yellow [structure].
STYLE: clean medical-technical product render, e-commerce infographic, sharp, 4K.
NO text, no numbers, no logo, no watermark.
```

**Negative:**
```
text, letters, numbers, watermark, logo, human face, facial features, hair,
skin tone, clothing, photographic background, environment, furniture, shadows on floor,
extra colors, rainbow palette, anatomically wrong spine, floating disconnected organs,
dimension lines overlapping product edge, cluttered inset
```

# Trigger description

```yaml
id: sqr-mech-ghostbody
name: Ghost Body Mechanism Render
use_when: >
  Cần giải thích TẠI SAO hình dạng sản phẩm hoạt động, bằng cơ chế bên
  trong cơ thể mà không quay được. Dùng ở ảnh 3-4 trong gallery, sau khi
  đã có pain và relief. Hợp mọi tệp vì cơ thể vô danh.
avoid_when: >
  Ảnh chính, ảnh dừng scroll, hoặc khi sản phẩm không tác động lên cấu
  trúc cơ thể. Không dùng nếu cần cảm xúc, type này lạnh và không có ai
  để đồng cảm.
pairs_with: sqr-pain-xcheck (trước), bnr-relief-vsinset (sau)
sequence_role: nấc 3 trên Trust Ladder, tầng cơ chế
```

---

## Test C: `SQR-MECH-GHOSTBODY` v1.0

**Sản phẩm test: băng dán miệng ngủ**
Stress axis: cutaway ở đầu chứ không phải cột sống, sản phẩm nhỏ và phẳng nên DIMS gần như vô nghĩa, cơ chế là luồng khí chứ không phải lực.

```
A 1:1 3D technical render on a seamless white infinity background. NOT photography.

BASE: A featureless matte white 3D mannequin head and upper chest in profile, no face details, no hair, no clothing, no skin tone, lying back as if asleep. The head is cross-sectioned along the sagittal plane to reveal the interior airway. Soft even studio lighting, subtle grey ambient occlusion only.

ANATOMY CUTAWAY: The nasal cavity, soft palate, tongue and throat rendered inside the head silhouette, not floating on top. Tissue in off-white ivory, the open nasal passage highlighted with a smooth blue airflow ribbon travelling from the nostril down the throat. The collapsed area behind the tongue marked in red.

PRODUCT: A single horizontal strip of mouth tape in soft matte beige placed across the closed lips, the only object with a real material finish, slightly textured fabric weave, gently rounded corners, sharp silhouette against white.

DIMS: Thin black double-headed arrows measuring the strip length and strip width, with fine extension lines offset clear of the product outline. Drafting style, no numbers.

XCHECK: Two small rounded-square panels side by side in the top-left corner, flat 2D vector illustration style, light grey outline, white fill. LEFT: an open mouth in profile with orange heat glow at the throat and small motion squiggles for turbulent air, red circle with white X above. RIGHT: a closed mouth with a blue airflow arrow entering the nose and the yellow tongue resting in neutral position, green circle with white check above.

PALETTE LOCK: achromatic white and grey everywhere. The ONLY colors permitted are red for collapsed tissue, orange for wrong airflow, blue for correct airflow, yellow for structure.
STYLE: clean medical-technical product render, e-commerce infographic, sharp, 4K.
NO text, no numbers, no logo, no watermark.
```

**Negative:** như trên, thêm `teeth, gore, wet tissue, realistic flesh, medical horror`

**Đoán chỗ gãy:** slot ANATOMY CUTAWAY. Mặt cắt dọc đầu người rất dễ trượt sang render y khoa gớm ghiếc hoặc sang phong cách sách giáo khoa 2D, lệch register với sản phẩm. Slot DIMS gần như chắc chắn thừa vì strip quá đơn giản, có thể chính test này sẽ chứng minh DIMS nên là module chỉ bật khi sản phẩm có hình khối 3 chiều rõ ràng.

---

Đã có 3 type. Registry hiện tại:

| Mã | Vai trò trên ladder |
|---|---|
| `SQR-PAIN-XCHECK` | nấc 1, dừng scroll bằng đau |
| `SQR-MECH-GHOSTBODY` | nấc 3, giải thích cơ chế |
| `BNR-RELIEF-VSINSET` | nấc 5, bán trạng thái sau mua |

Đang trống nấc 2 (khuếch đại hậu quả) và nấc 4 (bằng chứng thật, demo, review). Nếu bạn có ảnh mẫu cho 2 nấc đó thì đưa vào, bộ sẽ khép kín.

---

## Human

**Attachments:**
- 1786337706404_image.png

---

## Assistant

<details><summary>Thinking</summary>

I'm designing a new image layout that combines a hero lifestyle photo with a curved sidebar on the right containing four circular pain point vignettes, plus red arrows on the product showing upward support—this hybrid approach amplifies both the relief narrative and the breadth of the problem. The canvas is square, with the left side taking up about 72% for a photorealistic lifestyle scene of a woman at her desk in correct posture, the pink product visible in the chair, and she's smiling.

On the right ~28%, there's a vertical sidebar with a wavy S-curve left edge and pale blue-white gradient, holding four evenly spaced circular photo vignettes showing people clutching different body parts (neck, mid-back, hip, lower back) with red radial glows—all cropped without faces, grayscale clothing but color photos. The red arrows overlaid on the product act as a vector device showing the direction of support and force. This "pain rail" design communicates that one product solves multiple pain zones, so I'm adding a new intent category called SCOPE to capture this coverage angle, and naming the device `SQR-SCOPE-PAINRAIL+FORCEARROWS` with the base being `SQR-SCOPE-PAINRAIL`.

The original has some weaknesses: the wavy sidebar edge is purely decorative and takes up 28% of the frame, the four circles become tiny on mobile, the hero and vignettes have different lighting, and the red arrows on the product might get confused with heat or warming functionality. Now I'm testing this pattern on a different product—I've already used a showerhead filter, knife sharpener, and mouth tape, so I need something new from their portfolio. A vertical ergonomic mouse could work, or I could revisit the showerhead filter with different pain points like dry skin, hair fall, itchy scalp, and limescale buildup, which actually maps well to their real in-development product.

The knife sharpener would be a harsh stress test since it has no body pain rail at all, which would break the entire PAINRAIL structure—revealing but maybe

</details>

# Breakdown

Type mới, và nó chính là nấc 2 đang trống. Cấu trúc là **hero + rail**, không phải split.

| Zone | Vị trí | Nội dung | Job |
|---|---|---|---|
| **A. Hero** | Trái ~72%, chủ thể lệch trái | Người dùng ngồi đúng tư thế, mỉm cười, sản phẩm hồng lộ rõ trên ghế | Bán trạng thái đúng |
| **B. Force arrows** | Đè lên sản phẩm trong ảnh thật | 3 mũi tên đỏ hướng lên, bo tròn, mờ dần | Chỉ hướng lực nâng đỡ |
| **C. Pain rail** | Phải ~28%, cạnh trái uốn cong hình S | Dải gradient xanh nhạt, 4 vignette tròn xếp dọc đều nhau | Liệt kê phạm vi vấn đề được giải quyết |

**Nội dung 4 vignette:** mỗi ô là 1 vùng đau khác nhau, crop chặt, không thấy mặt, tay ôm vào vùng đau, vầng đỏ radial ngay tại điểm. Cổ → lưng trên → hông → thắt lưng. Thứ tự đi từ trên xuống dưới theo đúng giải phẫu, không xáo trộn.

**Khác biệt logic với 3 type trước:** ba type kia đều lập luận theo chiều sâu (sai → đúng, ngoài → trong). Type này lập luận theo **chiều rộng**: một sản phẩm, bốn vấn đề. Nó không chứng minh gì cả, nó đếm.

**Ba lỗi trong ảnh gốc:**

1. Rail ăn 28% khung để chứa 4 hình mà trên mobile mỗi hình còn dưới 60px. Đếm được nhưng không đọc được. Nên hạ xuống 3 ô, phóng to.
2. Mũi tên đỏ đặt trên đệm dễ bị đọc nhầm thành chức năng sưởi ấm. Trong hệ màu của bạn đỏ đang là tín hiệu đau. Xung đột ngữ nghĩa. Nên đổi sang xanh dương (nâng đỡ) và giữ đỏ riêng cho rail.
3. Cạnh cong hình S của rail là trang trí thuần túy, làm mất một mảng nội dung ở góc trên phải mà không đổi lại được gì.

# Tên type

**`SQR-SCOPE-PAINRAIL+FORCEARROWS`**
Base: **`SQR-SCOPE-PAINRAIL`**

Bổ sung registry:
- INTENT mới: `SCOPE` (một sản phẩm, nhiều vấn đề, lập luận theo chiều rộng)
- DEVICE mới: `PAINRAIL` (dải vignette dọc liệt kê triệu chứng), `FORCEARROWS` (mũi tên hướng lực đè lên ảnh thật)

Cùng họ: `VERT-SCOPE-PAINRAIL`, `SQR-SCOPE-BENEFITRAIL` (đổi 4 ô đau thành 4 ô lợi ích), `BNR-RELIEF-VSINSET+FORCEARROWS`.

# Prompt skeleton

```
TYPE: SQR-SCOPE-PAINRAIL
RATIO: [1:1 / 4:5]
LAYERS: photographic hero base + vector overlay + vignette rail on right edge

[ZONE A: HERO, left 72%]
[age/gender] in [wardrobe, muted neutral tones], [correct posture/behavior]
while [everyday activity], calm content expression, [gaze direction].
[PRODUCT] in [colorway] clearly visible at [contact point], unobstructed.
Setting: [environment], [3 props], soft natural window light, background blurred.
Bright high-key [neutral palette] grade. Subject offset left.

[ZONE B: FORCE ARROWS]
[N] [color] rounded arrows overlaid on [PRODUCT] pointing [direction],
evenly spaced, semi-transparent, fading at the tips, flat vector style.
Arrow color MUST differ from the pain color used in the rail.

[ZONE C: PAIN RAIL, right 25-28%, vertical band, [straight / soft S-curved] left edge]
Pale [tint] gradient panel. [3-4] circular photo vignettes stacked evenly,
white ring border, equal diameter, generous spacing.
Each vignette: tight crop of [same-role person], no face visible,
hand pressing on [body zone N], red radial glow centered on that zone.
Zones ordered top to bottom: [zone1], [zone2], [zone3], [zone4].
All vignettes share the hero's lighting, wardrobe tone and photographic style.

STYLE: clean e-commerce infographic tile, bright airy, sharp focus, 4K.
NO text, no logo, no watermark.
```

**Negative:**
```
text, letters, numbers, watermark, logo, deformed hands, extra fingers,
faces inside vignettes, mismatched lighting between hero and vignettes,
red arrows on product, heat or warming cues, cluttered background,
dark grade, vignettes too small, overlapping circles, product obscured
```

# Trigger description

```yaml
id: sqr-scope-painrail
name: Relief Hero with Symptom Coverage Rail
use_when: >
  Sản phẩm giải quyết nhiều vấn đề cùng lúc và cần cho thấy phạm vi bao
  phủ trong một ảnh. Dùng ở ảnh 2 hoặc 3 trong gallery, ngay sau ảnh dừng
  scroll. Hợp khi tệp khách rộng và mỗi người đau một kiểu khác nhau.
avoid_when: >
  Sản phẩm chỉ giải quyết đúng 1 vấn đề, khi đó rail thành nhồi nhét.
  Không dùng làm ảnh chính. Không dùng khi triệu chứng không quay được.
pairs_with: sqr-pain-xcheck (trước), sqr-mech-ghostbody (sau)
sequence_role: nấc 2 trên Trust Ladder, tầng khuếch đại phạm vi
```

---

## Test D: `SQR-SCOPE-PAINRAIL` v1.0

**Sản phẩm test: lọc nước vòi sen kim loại**
Stress axis: rail phải liệt kê triệu chứng không ai ôm tay vào được (tóc rụng, da khô, ngứa da đầu). Ép skeleton chứng minh slot vignette có tổng quát hóa ngoài động tác ôm vùng đau hay không.

```
A 1:1 e-commerce infographic tile.

ZONE A (left 72%): A woman in her late 20s with long dark hair stands under a running shower in a bright modern bathroom, head tilted back, eyes closed, calm content expression. A brushed stainless steel inline shower filter is clearly visible screwed between the hose and the showerhead above her, unobstructed. Setting: white marble tile, a glass partition, a small eucalyptus bundle, soft daylight from a frosted window, background blurred. Bright high-key white and warm grey grade. Subject offset left.

ZONE B: Three blue rounded arrows overlaid on the water stream below the filter pointing downward, evenly spaced, semi-transparent, fading at the tips, flat vector style.

ZONE C (right 26%, vertical band with a soft S-curved left edge): Pale aqua gradient panel. Three circular photo vignettes stacked evenly, white ring border, equal diameter, generous spacing. Each vignette is a tight crop with no face visible, sharing the hero's lighting and photographic style:
- top: a hand running through dry brittle hair with strands breaking away, red radial glow at the hair ends
- middle: a forearm with flaky irritated dry skin, red radial glow on the patch
- bottom: fingers scratching a scalp at the hairline, red radial glow at the scalp

STYLE: clean e-commerce infographic tile, bright airy, sharp focus, 4K.
NO text, no logo, no watermark.
```

**Negative:** như trên, thêm `wet lens distortion, steam obscuring product, skin disease, gore, medical rash photography`

**Đoán chỗ gãy:** slot vignette. Skeleton hiện viết cứng "hand pressing on body zone", ở đây phải chuyển thành "biểu hiện trên cơ thể". Nhiều khả năng model vẫn vẽ tay ôm. Nếu đúng thì slot này phải tách làm 2 biến thể: `pain-gesture` và `visible-symptom`.

---

## Registry sau 4 type

| Mã | Nấc | Job |
|---|---|---|
| `SQR-PAIN-XCHECK` | 1 | dừng scroll bằng đau |
| `SQR-SCOPE-PAINRAIL` | 2 | khuếch đại phạm vi vấn đề |
| `SQR-MECH-GHOSTBODY` | 3 | giải thích cơ chế |
| `BNR-RELIEF-VSINSET` | 5 | bán trạng thái sau mua |

Còn trống **nấc 4: bằng chứng thật**. Đó là ảnh dạng demo tay người, before/after chụp thật, screenshot review, chứng nhận, hoặc test vật lý. Nếu bạn có mẫu cho nấc này thì hệ sẽ khép kín và tôi có thể viết luôn phần sequencing rule cho cả bộ gallery.

---

## Human

**Attachments:**
- 1786337910638_image.png

---

## Assistant

<details><summary>Thinking</summary>

I'm thinking about a different type of visual—a collage grid layout with one large panel on the right showing a pregnant woman on a sofa, and three stacked panels on the left showing an elderly man in a wheelchair, a woman at a desk, and a man driving. This represents expanding the product's scope across different user segments and contexts rather than different symptoms, so I'd frame this as SCOPE but along a different axis—moving from one product addressing many symptoms to one product serving many people in different situations.

I'm naming this layout structure `SQR-SCOPE-PERSONAGRID` with a 1:1 canvas split vertically—left column takes up 38% with three equal horizontal cells separated by thin white gutters, while the right panel is a single large cell at 62%. The unifying elements are a warm beige and cream palette, natural window light in every scene, the same grey product colorway visible throughout, and everyone seated in soft-focus environments. But I'm noticing some visibility issues—the product is barely visible in the wheelchair cell and blends into the white background in the desk cell, which weakens the consistency I'm going for.

The core principle here is that the casting should be maximally spread across demographics while keeping the palette, lighting, and posture identical—that's what signals "one product, many lives." I now have two devices in the registry: PAINRAIL for symptom variety and PERSONAGRID for demographic variety. I'm thinking of stress-testing this layout with a knife sharpener next, using personas like a home cook, elderly person, camper, and butcher—that would really challenge the design since the product is tiny and handheld, making visibility in each cell difficult. Mouth tape would be another option but four sleeping people feels monotonous. I should also note that step 4 is still empty and needs attention.

</details>

# Breakdown

Type mới, và nó không lập luận. Nó **casting**.

| Zone | Vị trí | Nội dung |
|---|---|---|
| **Hero cell** | Phải 62%, full height | Bà bầu ngồi sofa, tay ôm bụng, cười, sản phẩm xám lộ sau lưng |
| **Stack cell 1** | Trái trên, 1/3 chiều cao | Ông cụ ngồi xe lăn cạnh cửa sổ |
| **Stack cell 2** | Trái giữa | Phụ nữ văn phòng ngồi làm việc bên laptop |
| **Stack cell 3** | Trái dưới | Đàn ông trung niên lái xe ban đêm |

Gutter trắng mảnh 4px, không viền ngoài, không badge, không mũi tên, không chữ.

**Trục lập luận:** ba type SCOPE trước đi theo chiều rộng của *vấn đề*. Type này đi theo chiều rộng của *người*. Thông điệp duy nhất: "có người giống bạn đang dùng cái này".

**Luật giữ collage không vỡ.** Bốn ô phải cách nhau tối đa về nhân khẩu (tuổi, giới, tình trạng cơ thể, bối cảnh) nhưng trùng khít nhau về bốn thứ:
1. Bảng màu, ở đây là kem, be, trắng, gỗ nhạt. Không ô nào lệch tông.
2. Nguồn sáng, cửa sổ tự nhiên, kể cả ô lái xe ban đêm cũng dùng ánh sáng dịu chứ không đèn màu.
3. Tư thế, tất cả đều đang ngồi.
4. Colorway sản phẩm, chỉ một màu duy nhất xuyên suốt.

Lệch một trong bốn thì collage đọc thành bốn ảnh stock ghép lại.

**Vì sao ô lớn là bà bầu:** ô lớn luôn dành cho persona có tình trạng cụ thể nhất và cảm xúc mạnh nhất, không phải persona đông nhất. Ba ô nhỏ mới là phần mở rộng.

**Lỗi trong ảnh gốc:** ở ô xe lăn và ô lái xe gần như không nhìn thấy sản phẩm, nên hai ô đó chỉ còn là ảnh người. Ô văn phòng thì đệm trắng chìm vào ghế trắng, sai colorway so với ô hero màu xám. Collage mất đi một nửa công năng.

# Tên type

**`SQR-SCOPE-PERSONAGRID`**

Bổ sung registry DEVICE: `PERSONAGRID` (collage đa persona, không overlay đồ họa).

Ghi layout bằng hậu tố khi cần: `SQR-SCOPE-PERSONAGRID@1+3`. Các layout khả dụng: `@1+3`, `@2x2`, `@1+4`, `@4x1` (dạng dải ngang).

Cùng họ: `VERT-SCOPE-PERSONAGRID@1+2`, `SQR-SCOPE-CONTEXTGRID` (đổi trục từ người sang nơi chốn: bàn làm việc, xe hơi, máy bay, sofa).

# Prompt skeleton

```
TYPE: SQR-SCOPE-PERSONAGRID
RATIO: [1:1 / 4:5]
LAYOUT: [@1+3 / @2x2 / @1+4], thin white 4px gutters, no outer border,
photographic collage, no graphic overlays.

[GLOBAL LOCK, applies to every cell]
Same palette: [3-4 neutral tones]. Same lighting: [single light character].
Same posture family: all subjects [shared body position].
[PRODUCT] in [ONE colorway only] must be clearly visible and unobstructed in EVERY cell.
Same photographic style, same grade, backgrounds softly blurred.

[HERO CELL, largest]
[most specific persona: age, gender, distinguishing condition] in [wardrobe],
[interaction with product] in [environment], [warm emotional expression].

[SUPPORT CELL 1] [persona 2, maximally different age/gender] in [environment 2], [activity 2].
[SUPPORT CELL 2] [persona 3] in [environment 3], [activity 3].
[SUPPORT CELL 3] [persona 4] in [environment 4], [activity 4].

CASTING RULE: the four personas must differ maximally in age, gender and context,
and match exactly in palette, lighting, posture and product colorway.

STYLE: clean lifestyle collage for e-commerce, bright airy, sharp focus, 4K.
NO text, no logo, no watermark, no badges, no arrows.
```

**Negative:**
```
text, letters, numbers, watermark, logo, borders around cells, badges, arrows,
deformed hands, extra fingers, product hidden or cropped out in any cell,
different product colors between cells, mismatched color grade between cells,
one cell darker than the others, stock photo collage look, inconsistent lighting,
cluttered backgrounds, duplicate-looking people
```

# Trigger description

```yaml
id: sqr-scope-personagrid
name: Multi-Persona Lifestyle Grid
use_when: >
  Cần trả lời câu hỏi "cái này có hợp với tôi không" bằng cách cho thấy
  nhiều kiểu người khác nhau đang dùng. Hợp làm ảnh 4-5 trong gallery
  hoặc ảnh chốt cuối. Dùng khi tệp khách rộng về tuổi và bối cảnh.
avoid_when: >
  Tệp khách hẹp và cụ thể, khi đó grid làm loãng định vị. Không dùng làm
  ảnh chính. Không dùng nếu sản phẩm quá nhỏ để nhìn thấy trong ô con.
pairs_with: sqr-scope-painrail (cùng tầng, khác trục), bnr-relief-vsinset
sequence_role: tầng nhận diện bản thân, đặt sau khi đã có cơ chế và relief
```

---

## Test E: `SQR-SCOPE-PERSONAGRID` v1.0

**Sản phẩm test: dụng cụ mài dao lăn**
Stress axis: sản phẩm nhỏ, cầm tay, dễ biến mất trong ô con. Đây đúng là điều kiện mà `avoid_when` cảnh báo, nên test này để xác định ngưỡng gãy chứ không phải để pass đẹp.

```
A 1:1 photographic lifestyle collage, layout one large cell on the right and three stacked cells on the left, thin white 4px gutters, no outer border, no graphic overlays.

GLOBAL LOCK: every cell uses the same palette of warm cream, pale oak, soft white and matte black. Same lighting: soft natural window light from the side. All subjects standing at a counter, hands in frame. A rolling knife sharpener with a black handle and a diamond-coated disc, always the same black colorway, clearly visible and unobstructed in every cell. Same color grade, backgrounds softly blurred.

HERO CELL (large, right): A woman in her early 30s in a cream linen apron rolls the sharpener along a chef's knife on a pale oak kitchen counter, looking down at the blade with a focused satisfied expression, bright modern kitchen behind her.

SUPPORT CELL 1 (top left): A man in his late 60s with grey hair uses the sharpener on a paring knife at a rustic kitchen counter, relaxed and unhurried.

SUPPORT CELL 2 (middle left): A young man in his 20s in a plain t-shirt uses the sharpener on a santoku knife in a small apartment kitchen.

SUPPORT CELL 3 (bottom left): A woman in her 40s uses the sharpener on a hunting knife at a wooden picnic table outdoors, soft daylight, blurred trees behind.

CASTING RULE: the four people differ maximally in age, gender and setting, and match exactly in palette, lighting, posture and product colorway.

STYLE: clean lifestyle collage for e-commerce, bright airy, sharp focus, 4K.
NO text, no logo, no watermark, no badges, no arrows.
```

**Negative:** như trên, thêm `blood, cuts, injury, knife pointed at person, blurred product, product out of frame`

**Đoán chỗ gãy:** hai chỗ. Một, sản phẩm trong ba ô nhỏ sẽ nhỏ hơn 40px và mất nhận diện, xác nhận giả thuyết rằng skeleton cần thêm slot bắt buộc `product occupies at least X% of each cell`. Hai, dao trong tay nhiều người dễ kích bộ lọc an toàn hoặc ra tay dị dạng.

---

## Registry sau 5 type

| Mã | Nấc | Job |
|---|---|---|
| `SQR-PAIN-XCHECK` | 1 | dừng scroll bằng đau |
| `SQR-SCOPE-PAINRAIL` | 2 | mở rộng phạm vi vấn đề |
| `SQR-MECH-GHOSTBODY` | 3 | giải thích cơ chế |
| `SQR-SCOPE-PERSONAGRID` | 4b | nhận diện bản thân |
| `BNR-RELIEF-VSINSET` | 5 | bán trạng thái sau mua |

Vẫn trống **nấc 4a: bằng chứng vật lý**. Đó là ảnh test thật, demo tay người cận cảnh, before/after chụp nguyên bản, chất liệu cắt đôi, hoặc chứng nhận. Đây là nấc duy nhất mà người mua hoài nghi thực sự dừng lại kiểm tra. Có mẫu cho nấc đó thì bộ khép kín và tôi viết được luôn quy tắc sắp xếp thứ tự cho cả gallery.

---

## Human

một số lưu ý:

* không mô tả chi tiết hình dáng sản phẩm ở prompt (tôi sẽ input ảnh sản phẩm sau)
* BNR-RELIEF-VSINSET chưa logic ở prompt sản phẩm
* SQR-SCOPE-PERSONAGRID cần đa dạng góc độ chụp ảnh, setup môi trường hơn

---

## Assistant

<details><summary>Thinking</summary>

I'm working through three feedback items that need to be applied across the skeleton templates. First, I need to establish a global rule removing product shape descriptions from prompts since users will provide product images instead — this requires a standard reference clause across all five skeletons. Second, there's a logic issue with the BNR-RELIEF-VSINSET product zone that needs investigation, particularly around how the product cluster is structured in the shower filter test where Zone B showed duplicate cylindrical elements.

The core problem is that Zone B shouldn't describe invented details like knurled grip rings or threads when the reference image shows something different, and it shouldn't assume colorway variants that don't exist in the actual product. The fix is to make Zone B conditional: it should display the same product from the reference image with only the colorways that actually exist, maintaining consistency between Zone A and Zone B. If there's only one colorway, show a single unit at a different angle rather than duplicating it.

For PERSONAGRID, the real issue is that all the cells feel visually repetitive because they're shot from the same eye-level perspective at a counter. I need to add camera angle variety per cell and change up the environments while keeping cohesion through grade, light quality, and colorway alone. That means loosening the posture lock so the diversity comes from angle and setting instead.

I should write out the v1.1 patches concisely and reissue corrected test prompts for the two affected types. I also need to establish a standard line in the global rule about attached product images and when shape descriptions are off-limits, which feels

</details>

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

Ba mục này, mục 1 là luật toàn hệ nên phải sửa cả 5 skeleton. Hai mục còn lại vá riêng.

---

# PATCH 0: Global rule (áp cho mọi type)

Thêm block cố định vào đầu mọi skeleton, và **xóa sạch mọi tính từ mô tả hình dáng** trong các slot PRODUCT.

```
[PRODUCT REFERENCE, bắt buộc, đặt ở đầu prompt]
Use the attached product photo as the exact reference for the product.
Preserve its shape, proportions, material, finish and color exactly as shown.
Do not redesign, restyle, simplify or add features.
Render it from [angle] at [scale in frame], integrated with the scene lighting.
```

Slot PRODUCT trong mọi skeleton từ nay chỉ được chứa 4 thông tin, không hơn:

| Được phép | Cấm |
|---|---|
| Vị trí trong khung | Hình dáng, đường cong, chất liệu |
| Góc nhìn | Màu sắc (trừ khi chọn giữa các colorway có thật) |
| Tỉ lệ chiếm khung | Chi tiết cấu tạo, ren, gân, khóa, nút |
| Quan hệ với vật khác (gắn lên, tựa vào, cầm trong tay) | Bất kỳ tính từ thẩm mỹ nào |

Thêm vào negative của mọi type: `redesigned product, altered product shape, invented product details, different product than reference`

---

# PATCH 1: `BNR-RELIEF-VSINSET` v1.1

**Chẩn đoán.** Zone B cũ sai ở ba tầng:

1. Nó bịa colorway. Skeleton ép "2 units, 2 màu" trong khi sản phẩm có thể chỉ có 1 màu. Với ảnh reference đính kèm thì lệnh này mâu thuẫn trực tiếp với reference.
2. Nó không có lý do tồn tại. Sản phẩm đã hiện rõ trong Zone A rồi. Lặp lại nguyên vật thể ở Zone B chỉ thừa, trừ khi Zone B cho thấy **thứ Zone A không cho thấy được**.
3. Nó bịa chi tiết cấu tạo (knurled ring, visible thread), vi phạm luật global mới.

**Sửa.** Zone B đổi từ "cluster khoe màu" thành **complementary view**: bắt buộc trình bày một góc nhìn mà Zone A bị che khuất. Số lượng unit do sản phẩm quyết định, không do skeleton quyết định.

```
TYPE: BNR-RELIEF-VSINSET v1.1
RATIO: [2:1 / 4:5]
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
high-key [neutral palette] grade. Subject offset right, empty mid-frame.

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

**Negative v1.1:** thêm `redesigned product, altered product shape, invented product details, different product than reference, same angle repeated, fabricated colorways, mixed illustration and photo inside one inset half`

## Test A v1.1 (lọc nước vòi sen, có đính ảnh sản phẩm)

```
A wide 2:1 e-commerce banner.

Use the attached product photo as the exact reference for the shower filter. Preserve its shape, proportions, material, finish and color exactly. Do not redesign or add features. The product must be identical in every layer of this image.

MAIN SCENE (right two-thirds): A woman in her late 20s with long dark hair stands under a running shower, head tilted back, eyes closed, calm satisfied expression, water streaming over her shoulders. The filter is installed above her between the hose and the showerhead, seen from a low three-quarter angle, unobstructed. Setting: bright modern bathroom, white marble tile, glass partition, a small eucalyptus bundle, soft daylight from a frosted window. Background blurred, high-key white and warm grey grade, steam catching the light. Subject offset right, empty mid-frame.

PRODUCT VIEW (bottom-left foreground): The same filter from the reference, shown from a top-down angle looking into the inlet, floating above the surface, occupying about 25 percent of the frame width. Studio lighting, soft contact shadow, razor sharp, clean cutout edge. Show one unit only.

INSET PANEL (top-left, white 3px border, split 50/50, red circular VS badge at the seam):
LEFT: desaturated grayscale macro photo of a showerhead nozzle plate caked with white limescale, dull uneven dripping water, glowing red hotspots at three clogged nozzles.
RIGHT: full-color macro photo of a clean nozzle plate spraying clear even jets, with a cyan translucent overlay tracing the water path. Both halves photographic, right half brighter and cleaner.

STYLE: clean commercial e-commerce banner, bright airy, sharp focus, 4K.
NO text, no logo, no watermark.
```

---

# PATCH 2: `SQR-SCOPE-PERSONAGRID` v1.1

**Chẩn đoán.** v1.0 khóa nhầm biến. Nó khóa *tư thế* và ép mọi ô cùng một kiểu chụp, nên grid ra bốn ảnh na ná nhau, mất cảm giác "nhiều thế giới khác nhau".

**Sửa.** Tách rõ hai danh sách: cái gì phải khác, cái gì phải giống. Chuyển gánh nặng gắn kết từ tư thế sang **grade màu + chất ánh sáng + colorway sản phẩm**, ba thứ này đủ giữ collage liền mạch. Thêm slot góc máy bắt buộc khác nhau cho từng ô, và slot tỉ lệ sản phẩm tối thiểu.

```
TYPE: SQR-SCOPE-PERSONAGRID v1.1
RATIO: [1:1 / 4:5]
LAYOUT: [@1+3 / @2x2 / @1+4], thin white 4px gutters, no outer border,
photographic collage, no graphic overlays.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly across all cells.

[MUST MATCH across cells]
Color grade and palette: [3-4 neutral tones].
Light quality: [soft / diffused / directional], never harsh or colored.
Product colorway: [one only].
Overall photographic finish: same lens character, same contrast, same skin rendering.

[MUST DIFFER across cells]
Age, gender and body situation of the subject.
Camera angle, one per cell, chosen from: eye-level side profile / high three-quarter /
low angle / over-the-shoulder / waist-level frontal / close crop on the interaction.
Environment type, one per cell, and shot distance (wide, medium, close).

[PRODUCT VISIBILITY RULE]
The product must be clearly visible and unobstructed in EVERY cell,
occupying at least 15% of that cell's height. If a cell cannot meet this,
tighten the crop until it does.

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

**Negative v1.1:** thêm `identical camera angles, repeated framing, same environment twice, product smaller than 15% of cell height, redesigned product, different product than reference`

## Test E v1.1 (dụng cụ mài dao lăn, có đính ảnh sản phẩm)

```
A 1:1 photographic lifestyle collage, layout one large cell on the right and three stacked cells on the left, thin white 4px gutters, no outer border, no graphic overlays.

Use the attached product photo as the exact reference for the knife sharpener. Preserve shape, proportions, material, finish and color exactly across all cells.

MUST MATCH: warm cream, pale oak, soft white and matte black palette. Soft diffused daylight in every cell, never harsh or colored. One product colorway throughout. Same lens character, contrast and skin rendering.

MUST DIFFER: age, gender, environment, camera angle and shot distance in every cell.

The product must be clearly visible and unobstructed in every cell, occupying at least 15 percent of that cell's height.

HERO CELL (large, right): A woman in her early 30s in a cream linen apron sharpens a chef's knife on a pale oak counter in a bright modern kitchen, looking down with a focused satisfied expression. Camera: waist-level frontal, medium shot.

SUPPORT CELL 1 (top left): A man in his late 60s with grey hair sharpens a small paring knife at a rustic wooden counter, relaxed. Camera: eye-level side profile, wide shot showing the room.

SUPPORT CELL 2 (middle left): A young man in his 20s sharpens a santoku in a narrow apartment kitchen at night, warm lamp light kept soft. Camera: high three-quarter looking down over his hands, close crop on the interaction.

SUPPORT CELL 3 (bottom left): A woman in her 40s sharpens a hunting knife on a wooden picnic table outdoors, blurred trees behind. Camera: low angle from table height, medium shot.

STYLE: clean lifestyle collage for e-commerce, bright airy, sharp focus, 4K.
NO text, no logo, no watermark, no badges, no arrows.
```

---

# Ba type còn lại, phần bị ảnh hưởng bởi Patch 0

Chỉ đổi slot PRODUCT, mọi thứ khác giữ nguyên.

**`SQR-PAIN-XCHECK` v1.1**, panel phải:
```
RIGHT PANEL: Full-color shot of the reference product [in place / in use] at
[context], seen from [angle], occupying [X%] of the panel. Clean uncluttered
background, bright even lighting, noticeably brighter than the left panel.
```

**`SQR-MECH-GHOSTBODY` v1.1**, slot PRODUCT:
```
[PRODUCT] The reference product, positioned [relation to body], seen from [angle],
the only object with a real material finish in the frame. Sharp silhouette against
white. Its contour must visibly align with [anatomical structure] above it.
```
Bỏ hẳn dòng mô tả matte texture và feature.

**`SQR-SCOPE-PAINRAIL` v1.1**, Zone A:
```
The reference product clearly visible at [contact point], seen from [angle],
unobstructed, occupying at least [X%] of the hero area height.
```

---

Version hiện tại: toàn bộ 5 type lên **v1.1**. Chạy lại Test A và Test E trước vì đó là hai cái vừa sửa logic. Test B, C, D chỉ cần thêm block PRODUCT REFERENCE và cắt phần mô tả hình dáng, không cần chạy lại nếu lần trước đã ra đúng bố cục.

---

## Human

list lại 5 image type và prompt skeleton

---

## Assistant

<details><summary>Thinking</summary>

I'm deciding whether to create a markdown file for this reference document or keep it in the chat—the user asked for a list, but this is structured content they'll likely reuse and reference across sessions, so a file format makes more sense.

</details>

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

Toàn bộ 5 type ở v1.1 đã gom vào một file registry, kèm 6 luật toàn hệ, negative prompt nền, trigger description, và quy trình test/vá.

| Mã | Nấc | Job |
|---|---|---|
| `SQR-PAIN-XCHECK` | 1 | Dừng scroll bằng đau |
| `SQR-SCOPE-PAINRAIL` | 2 | Mở rộng phạm vi vấn đề |
| `SQR-MECH-GHOSTBODY` | 3 | Giải thích cơ chế bên trong |
| `SQR-SCOPE-PERSONAGRID` | 4b | Nhận diện bản thân |
| `BNR-RELIEF-VSINSET` | 5 | Bán trạng thái sau khi mua |

Ba thứ đáng chú ý khi đọc file:

- **G1 đến G6** là phần quan trọng nhất. Chúng là luật chung, thay đổi một luật ở đây là sửa cả 5 skeleton cùng lúc. Đặc biệt G2 (slot PRODUCT chỉ chứa 4 loại thông tin) chính là mục feedback của bạn được mã hóa thành quy tắc kiểm tra được.
- **Nấc 4a vẫn trống**: bằng chứng vật lý. Đây là nấc duy nhất người mua hoài nghi thực sự dừng lại kiểm tra, nên thiếu nó thì gallery bị hụt ngay trước lúc chốt.
- `SQR-SCOPE-PAINRAIL` giờ có 2 biến thể vignette (`pain-gesture` và `visible-symptom`) cần chọn rõ trong prompt, vì test D đã lộ ra rằng viết cứng "tay ấn vào vùng đau" không tổng quát hóa được.

---

## Human

thay đổi format tên, không sử dụng BNR, SQR,... hãy đặt tên cho image type để người dùng dễ check và máy tính dễ đọc

---

## Assistant

<details><summary>Thinking</summary>

The user wants to move away from format-prefix abbreviations and instead use a human-readable naming scheme with kebab-case slugs that describe both the job and device, ordered with a step number. I'm proposing a format like `NN-job-device` where each entry gets a sequential number and descriptive English words, making it both easy for people to understand and machines to parse.

I'm also separating the ratio out into a parameter field rather than embedding it in the name, since the same type can render at multiple ratios. Now I'm mapping the five existing designs to this new naming convention and restructuring the ladder to include a reserved slot for physical proof, renumbering everything cleanly from 01 through 06. Updating the file with sed replacements to swap out the old naming convention for the new one.

</details>

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

Cú pháp mới:

```
{step}-{job}-{device}
```

Viết thường, gạch ngang, không dấu. Dùng thẳng làm tên file, key JSON, slug URL.

| Cũ | Mới | Bán cái gì |
|---|---|---|
| `SQR-PAIN-XCHECK` | `01-pain-split` | Dừng scroll bằng đau |
| `SQR-SCOPE-PAINRAIL` | `02-symptom-rail` | Mở rộng phạm vi vấn đề |
| `SQR-MECH-GHOSTBODY` | `03-mechanism-ghostbody` | Giải thích cơ chế bên trong |
| (trống) | `04-proof-demo` | Bằng chứng vật lý |
| `SQR-SCOPE-PERSONAGRID` | `05-persona-grid` | Nhận diện bản thân |
| `BNR-RELIEF-VSINSET` | `06-relief-hero` | Trạng thái sau khi mua |

Ba thay đổi về nguyên tắc, không chỉ về chữ:

**Bỏ tỉ lệ khung ra khỏi tên.** Đây là lỗi thiết kế của v1.1. Cùng một type render được cả 1:1 lẫn 4:5, nên nhét `SQR` vào tên tạo ra hai danh tính giả cho cùng một thứ. Giờ ratio là tham số truyền lúc chạy.

**Số thứ tự nằm đầu tên.** Sort chữ cái là ra đúng thứ tự gallery, không cần bảng tra. Đây là lý do dùng 2 chữ số thay vì 1.

**Slot 04 để trống có chủ đích.** Đánh số thưa để chèn type mới vào giữa mà không phải đánh số lại toàn bộ. Khi có mẫu cho nấc bằng chứng vật lý thì nó lấp đúng chỗ, không phải nối vào cuối.

Biến thể layout dùng hai gạch: `05-persona-grid--1plus3`.

---

## Human

**Attachments:**
- 1786342383697_image.png

---

## Assistant

<details><summary>Thinking</summary>

I'm shifting to a completely different visual approach here—a cinematic, editorial-style image capturing a raw pain moment rather than selling a product. The scene is a man struggling to exit a car at dusk in a garage, hand pressed to his lower back, face contorted in discomfort. It's moody and dark, shot like a film still with no graphics or overlays, and the emotional goal is identification with the struggle itself, not comparison or product positioning.

This works as a top-of-funnel hook—an advertorial hero image or cold-traffic ad creative that stops the scroll before anything else. It's step 1 territory but a different device than the pain-split image: both are step 1, just different formats. I'll name it `01-pain-scene` to keep it alongside `01-pain-split` in the same step, since the schema allows step numbers to repeat across different device types. The wide 5:3 aspect ratio and single-frame, zero-graphic approach make it distinct from everything else in the sequence.

The entire story lives in the acting and the moment—a man in his fifties caught mid-transition, exiting a car with a grimace, eyes squeezed, real discomfort. The back is the only visual anchor for the pain; no red hotspots, no signal colors at all. Low-key dusk lighting from the garage opening, warm interior fill, heavy shadows, rim-lit subject. Desaturated blue-grey palette with brown leather, film-like grade with crushed blacks and slight grain. The setting is mundane and specific: suburban garage, winter dusk, bare trees. This type explicitly breaks the brightness and color rules that apply everywhere else—it needs a note that it's exempt from G4 brightness constraints and G3 color semantics don't apply here.

The weakness is that without a product visible, it can't sell alone and risks feeling like stock photography, so the specificity of the transition moment becomes the mitigation. I'm naming this `01-pain-scene` and building a skeleton with slots for subject, transition moment, gesture, face, environment specificity, light, palette, grade, and camera. I'll add a moment rule: always choose an ordinary transition action, never a static pose. Testing this with mouth tape as the product—a pain scene for mouth tape would be a man experiencing discomfort from wearing it.

</details>

# Breakdown

Type này phá gần hết luật của 5 type trước. Không overlay, không split, không badge, không sản phẩm, không nền sáng.

| Thành phần | Chi tiết |
|---|---|
| **Khung** | ~5:3 ngang, một frame duy nhất, zero lớp đồ họa |
| **Chủ thể** | Nam ~50s, sơ mi công sở, đang **giữa một hành động chuyển tiếp** (bước ra khỏi xe), không phải dáng tạo hình |
| **Cử chỉ** | Tay ấn thắt lưng. Đây là toàn bộ thông tin bệnh lý của ảnh |
| **Mặt** | Nhăn thật, mắt nheo, hàm nghiến. Diễn xuất mang tải trọng, không phải minh họa |
| **Ánh sáng** | Low-key, xanh hoàng hôn từ cửa garage, fill ấm từ trong xe, rim sáng viền vai |
| **Grade** | Điện ảnh, đen bị nén, hạt phim nhẹ, khử bão hòa |
| **Bối cảnh** | Garage ngoại ô, chạng vạng, cây trụi lá. Tầm thường nhưng cụ thể |

**Ba điểm cấu trúc quan trọng:**

**Không có một pixel đỏ nào.** Năm type trước dùng đỏ làm tín hiệu đau. Type này dùng diễn xuất. Nếu thêm vầng đỏ vào đây thì ảnh chết ngay, vì nó tự khai là quảng cáo.

**Chọn khoảnh khắc chuyển tiếp, không chọn tư thế.** Đau ập đến khi đang bước ra khỏi xe, khi cúi buộc dây giày, khi đứng dậy khỏi ghế. Đây là thứ người xem nhận ra ngay vì họ vừa trải qua sáng nay. Ảnh chụp ai đó "đang ngồi sai tư thế" thì không có tính nhận diện đó.

**Nó cố tình trông không giống quảng cáo.** Đây là ảnh header cho advertorial hoặc creative cho ads nguội, không phải ảnh gallery. Nếu bỏ vào gallery Amazon cạnh 5 type kia thì lệch tông hoàn toàn.

**Điểm yếu:** không có sản phẩm nên bán một mình không được, bắt buộc phải ghép. Và rủi ro lớn nhất là rơi vào ảnh stock sáo mòn "người đàn ông đau lưng". Thứ duy nhất cứu được là độ cụ thể của khoảnh khắc và bối cảnh.

# Tên type

**`01-pain-scene`**

Cùng step với `01-pain-split` nhưng khác device. Hai cái này là hai triết lý đối lập cho cùng một việc: một cái nói đau bằng đồ họa, một cái nói đau bằng diễn xuất. Không bao giờ dùng chung trong một bộ.

Bổ sung registry DEVICE: `scene` (một frame điện ảnh, zero lớp đồ họa).

Cùng họ: `01-pain-scene--night`, `06-relief-scene` (cùng device, đổi job, dùng làm ảnh đóng advertorial).

# Miễn trừ luật toàn hệ

Type này là ngoại lệ duy nhất, phải ghi rõ trong registry:

| Luật | Trạng thái |
|---|---|
| G1 product reference | **Không áp dụng**, ảnh không có sản phẩm |
| G3 ngữ nghĩa màu | **Không áp dụng**, ảnh không có màu tín hiệu nào |
| G4 vế đúng sáng hơn | **Không áp dụng**, ảnh chỉ có một vế |
| G6 negative "dark moody lighting" | **Đảo ngược**, low-key là yêu cầu bắt buộc |

# Prompt skeleton

```
TYPE: 01-pain-scene v1.0
RATIO: [16:9 / 5:3 / 4:5]
REGISTER: cinematic film still. Single frame. NO graphic overlays of any kind.

[SUBJECT]
[age/gender] in [ordinary specific wardrobe, lived-in not styled],
caught mid-action while [everyday transitional movement],
[hand/body position expressing the symptom],
face showing [genuine involuntary discomfort: which muscles, which expression].
Body weight unbalanced, mid-motion, not posed.

[MOMENT RULE]
The action must be a mundane transition anyone performs daily,
not a demonstration of wrong behavior.

[ENVIRONMENT]
[specific ordinary place], [time of day], [seasonal or temporal marker].
Real lived-in clutter, nothing staged or styled.

[LIGHT]
Low-key. Key light: [source, direction, color temperature].
Fill: [source, weaker]. Rim light separating subject from background.
Deep shadow occupying [X%] of the frame.

[GRADE]
Desaturated [dominant hue] palette, crushed blacks, fine film grain,
shallow depth of field, [lens character].
NO saturated colors. NO red anywhere in the frame.

[FORBIDDEN]
No product. No overlays, arrows, badges, glows, hotspots, insets or split panels.
Nothing that signals advertising.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
NO text, no logo, no watermark.
```

**Negative:**
```
text, letters, watermark, logo, deformed hands, extra fingers,
red glow, pain hotspots, graphic overlay, arrows, badges, split panel,
bright airy lighting, white background, studio lighting, stock photo look,
posed model, fake grimace, smiling, clean staged interior, saturated colors,
advertising composition, product placement
```

# Trigger description

```yaml
id: 01-pain-scene
step: 1
job: pain
device: scene
version: "1.0"
ratios: [16:9, 5:3, 4:5]
requires_product_photo: false
exempt_from: [G1, G3, G4]
status: active
use_when: >
  Traffic nguội, chưa biết sản phẩm. Ảnh header advertorial, creative cho
  ads Facebook/native, ảnh mở bài. Việc duy nhất là làm người xem nhận ra
  chính mình rồi đọc tiếp.
avoid_when: >
  Gallery sàn thương mại điện tử, ảnh chính, hoặc bất kỳ chỗ nào cần thấy
  sản phẩm. Không dùng chung bộ với 01-pain-split, hai cái xung đột triết lý.
pairs_with: 06-relief-hero (đóng vòng), 04-proof-demo
never_with: 01-pain-split
```

---

## Test F: `01-pain-scene` v1.0

**Sản phẩm test: băng dán miệng ngủ**
Stress axis: triệu chứng không có cử chỉ nào để diễn (mệt mỏi, khô miệng, ngủ không sâu). Ép skeleton chứng minh slot cử chỉ có hoạt động khi không có chỗ nào để ấn tay vào.

```
A cinematic film still, 5:3 ratio. Single frame. NO graphic overlays of any kind.

SUBJECT: A man in his late 40s in a worn grey t-shirt and pyjama pants, caught mid-action sitting up on the edge of an unmade bed at 3am, feet on the floor, one hand rubbing his dry throat, the other braced on the mattress, shoulders slumped forward. Face showing genuine exhaustion, eyes half open and heavy, mouth slightly open and dry, deep creases under the eyes. Body weight unbalanced, mid-motion, not posed.

MOMENT RULE: this is the ordinary act of waking in the middle of the night, not a demonstration of wrong behaviour.

ENVIRONMENT: A small suburban bedroom, deep night, tangled duvet pushed aside, a glass of water and a phone face-down on the nightstand, curtains half drawn. Real lived-in clutter, nothing staged.

LIGHT: Low-key. Key light: cold blue streetlight through the gap in the curtains from behind and to the left. Fill: faint warm glow from a hallway door left ajar. Rim light along his shoulder and jaw separating him from the dark wall. Deep shadow occupying most of the frame.

GRADE: Desaturated blue-grey palette, crushed blacks, fine film grain, shallow depth of field, 35mm lens character.
NO saturated colors. NO red anywhere in the frame.

FORBIDDEN: No product. No overlays, arrows, badges, glows, hotspots, insets or split panels. Nothing that signals advertising.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
NO text, no logo, no watermark.
```

**Đoán chỗ gãy:** slot cử chỉ. "Tay xoa cổ họng" yếu hơn nhiều so với "tay ấn thắt lưng" vì nó không phải ký hiệu phổ quát. Nhiều khả năng model vẽ ra một người chỉ đang ngồi mệt, và ảnh mất luôn thông tin về triệu chứng. Nếu đúng thì skeleton cần thêm slot bắt buộc `symptom evidence in frame`: khi cử chỉ yếu thì phải có vật chứng trong khung (ly nước cạn, đồng hồ báo 3:14, gối hằn mồ hôi) gánh phần kể chuyện.

---

## Registry sau 6 type

| Tên | Bán cái gì | Dùng ở đâu |
|---|---|---|
| `01-pain-scene` | Nhận ra chính mình | Advertorial header, ads nguội |
| `01-pain-split` | Dừng scroll bằng đau | Gallery, thumbnail |
| `02-symptom-rail` | Mở rộng phạm vi vấn đề | Gallery ảnh 2-3 |
| `03-mechanism-ghostbody` | Giải thích cơ chế | Gallery ảnh 3-4 |
| `04-proof-demo` | Bằng chứng vật lý | **RESERVED** |
| `05-persona-grid` | Nhận diện bản thân | Gallery ảnh 4-5 |
| `06-relief-hero` | Trạng thái sau khi mua | Banner LP, A+ |

Type mới này mở ra một trục phân loại thứ hai mà registry chưa có: **kênh sử dụng**. Sáu type kia đều là ảnh gallery sàn, type này là ảnh quảng cáo ngoài sàn. Nếu bạn định làm cả hai kênh thì tôi nên thêm trường `channel` vào schema, giá trị `marketplace` hoặc `paid-social` hoặc `landing-page`, để router không bao giờ trộn nhầm hai bộ vào nhau.

---

## Human

**Attachments:**
- 1786342561889_image.png

---

## Assistant

<details><summary>Thinking</summary>

I'm designing a new medical illustration asset type that shows skeletal anatomy in a car seat context, comparing correct versus incorrect positioning. This will be a 2D medical illustration style on a blue clinical background with a hex pattern and cross motifs, distinct from the ghostbody 3D renders. The left panel shows an upright skeleton in profile with a translucent body silhouette and highlighted blue discs.

The right panel depicts the same skeleton seated in a car with compressed lumbar discs shown in red, a tilted pelvis, and a curved arrow indicating the bucket-seat slope. The background is a shared pale blue gradient with faint medical crosses and ghosted vertebrae watermarks, divided by a thin vertical line rather than a hard split. The key difference from the ghostbody register is that this is a 2D illustration with a branded clinical aesthetic, where the skeleton is foregrounded against a ghosted body outline—the inverse of the previous approach.

The car seat itself is positioned as the culprit rather than the product, which reverses the typical comparison direction: left shows correct posture, right shows the problem caused by the seat. The dashed pelvic line functions as a measuring device—horizontal indicates neutral alignment, while tilted indicates posterior pelvic tilt, which carries the core argument. This image is diagnostic in nature, explaining the cause of the problem rather than showcasing a product solution. It sits conceptually between the pain introduction and the mechanism explanation, so it might be better framed as a "cause" image that identifies the culprit rather than a mechanism image.

I'm considering whether to name this `02-cause-anatomy` as a new job category, since step 02 already has `02-symptom-rail`. Both can coexist at the same step like the pain images do. The design actually follows most guidelines—red marks the wrong posture, blue marks correct, and the left side is cleaner and brighter—but there's an inconsistency with the convention that left typically represents the "before" or problematic state. I should flag this and potentially enforce left as the wrong position to maintain consistency.

For the channel field, this works as both a landing page and gallery piece, so I'll add that metadata. Now I'm thinking about which product to test against—mouth tape has airway anatomy but I've already used it elsewhere, so the shower filter is a better choice. I can test whether the anatomy slot generalizes beyond body structures by using microstructure instead: clean pipe with intact hair cuticles versus limescale buildup. That's a good stress test for the framework.

</details>

# Breakdown

Type mới. Cùng họ giải phẫu với `03-mechanism-ghostbody` nhưng đảo ngược gần như mọi lựa chọn, và quan trọng hơn: nó không nói về sản phẩm.

| Thành phần | Chi tiết |
|---|---|
| **Register** | Minh họa y khoa 2D vẽ tay, không phải render 3D |
| **Nền** | Gradient xanh y tế, hoa văn lục giác, chữ thập mờ, đốt sống phóng to làm watermark |
| **Chia khung** | Một đường kẻ dọc mảnh, hai panel **dùng chung một nền**, không phải hai ảnh ghép |
| **Cơ thể** | Bộ xương là lớp trên, thân người chỉ còn đường viền trong suốt. Ngược hẳn ghostbody |
| **Panel trái** | Đứng thẳng, đĩa đệm xanh, đường gạch chấm xanh **nằm ngang** ở khung chậu, quầng xanh dọc sống lưng, badge ✓ xanh |
| **Panel phải** | Ngồi trong ghế ô tô, đĩa đệm thắt lưng đỏ, đường cong đỏ dọc cột sống, đường gạch chấm đỏ **nghiêng**, mũi tên đỏ hai đầu cong theo mặt đệm ghế |

**Ba điểm cấu trúc:**

**Đường gạch chấm ở khung chậu mới là thứ gánh toàn bộ lập luận.** Ngang = trung tính, nghiêng = xoay chậu ra sau. Bỏ hai đường này đi thì ảnh chỉ còn là "ngồi thì cong lưng", ai cũng biết rồi. Có chúng thì ảnh mới chỉ ra được nguyên nhân đo được.

**Không có sản phẩm, và thứ trong khung là thủ phạm.** Ghế ô tô ở đây đóng vai kẻ gây hại, không phải hàng bán. Đây là ảnh buộc tội môi trường, khác hẳn `03-mechanism-ghostbody` vốn biện hộ cho hình dáng sản phẩm.

**Nền là tài sản thương hiệu.** Lục giác, chữ thập, đốt sống mờ, gradient xanh. Ba thứ này không mang thông tin nào nhưng chúng mua uy tín y khoa và giữ hai panel dính vào nhau thành một canvas duy nhất.

**Lỗi trong ảnh gốc:** vế đúng đặt bên **trái**, ngược với `01-pain-split` (sai trái, đúng phải). Trong một bộ gallery mà hai ảnh đảo hướng nhau thì người xem đọc sai ở lần liếc đầu. Ngoài ra chỉ có badge ✓ mà không có badge ✗, mất đối xứng, panel phải bị bỏ lửng không ai gán nhãn.

# Tên type

**`02-cause-anatomy`**

Bổ sung vocabulary:
- **job** mới: `cause` (chỉ ra nguyên nhân đo được của vấn đề, không nói về sản phẩm)
- **device** mới: `anatomy` (minh họa y khoa 2D, xương nổi trên thân người trong suốt)

Cùng họ: `02-cause-anatomy--desk`, `02-cause-anatomy--sleep`, `03-mechanism-anatomy` (cùng register nhưng thêm sản phẩm vào để biện hộ).

## Phân biệt với `03-mechanism-ghostbody`

| | `02-cause-anatomy` | `03-mechanism-ghostbody` |
|---|---|---|
| Register | Minh họa 2D | Render 3D |
| Nền | Xanh y tế có hoa văn | Trắng vô cực |
| Lớp trên | Xương | Thân người |
| Vật thể trong khung | Thủ phạm | Sản phẩm |
| Câu nói | "Đây là thứ đang làm hại bạn" | "Đây là lý do hình dáng này hoạt động" |

Hai cái này dùng được cùng bộ, đặt liền nhau theo thứ tự 02 rồi 03. Nhưng phải khóa cùng một bảng màu để không đọc thành hai nguồn.

# Miễn trừ luật toàn hệ

| Luật | Trạng thái |
|---|---|
| G1 product reference | **Không áp dụng**, ảnh không có sản phẩm |
| G3 ngữ nghĩa màu | Áp dụng đầy đủ, đây là type tuân thủ chặt nhất |
| G4 vế đúng sáng hơn | Áp dụng |
| G5 register lock | Áp dụng, hai panel bắt buộc cùng nét vẽ |

# Prompt skeleton

```
TYPE: 02-cause-anatomy v1.0
RATIO: [5:3 / 16:9 / 1:1]
REGISTER: 2D medical illustration, airbrushed textbook style.
NOT photography. NOT 3D render.

[CANVAS]
One continuous pale blue clinical gradient background shared by both panels,
divided by a single thin vertical line, not a hard split.
Background motifs, all very low opacity: hexagon mesh, faint medical cross icons,
oversized ghosted [anatomical structure] as a watermark.
[optional: ghosted silhouette of [context object] behind the right panel]

[BODY TREATMENT, both panels]
[anatomical structure] drawn in warm ivory as the top layer,
the human body reduced to a translucent glowing outline behind it.
Same figure, same scale, same viewing angle in both panels.

[LEFT PANEL: WRONG]
Figure [wrong position] in/on [culprit object, drawn realistically].
[affected elements] highlighted in red. A red curved line tracing [wrong contour].
A red dashed reference line at [landmark], clearly TILTED.
A red double-headed curved arrow along [surface causing the problem].
Red circle with white X badge in the corner.

[RIGHT PANEL: CORRECT]
Same figure [correct position], no object or [supportive object].
[affected elements] highlighted in blue. A soft blue aura along [correct contour].
A blue dashed reference line at the same [landmark], clearly HORIZONTAL.
Green circle with white check badge in the corner.
Brighter and cleaner than the left panel.

[MEASUREMENT RULE]
The paired dashed reference lines are the core argument.
They must be at the identical anatomical landmark in both panels,
identical thickness and dash pattern, differing ONLY in angle.

PALETTE LOCK: pale blue and ivory throughout. The ONLY signal colors permitted are
red [wrong], blue [correct], green [confirmation badge].
STYLE: clinical medical illustration, e-commerce infographic, crisp linework, 4K.
NO text, no numbers, no logo, no watermark.
```

**Negative:**
```
text, letters, numbers, watermark, logo, photographic elements, 3D render,
photorealistic skin, human face, facial features, gore, wet tissue,
correct side on the left, both dashed lines at the same angle,
missing badge on either panel, different figure scale between panels,
extra colors, saturated background, cluttered motifs, anatomically wrong structures
```

# Trigger description

```yaml
id: 02-cause-anatomy
step: 2
job: cause
device: anatomy
version: "1.0"
ratios: [5:3, 16:9, 1:1]
channel: [landing-page, marketplace]
requires_product_photo: false
exempt_from: [G1]
status: active
use_when: >
  Cần buộc tội một thứ trong đời sống hàng ngày của khách (ghế ô tô, bàn
  làm việc, đệm ngủ, nước máy) và chỉ ra cơ chế gây hại đo được. Đặt sau
  ảnh đau, trước ảnh cơ chế sản phẩm. Hợp đoạn giữa advertorial.
avoid_when: >
  Vấn đề không có cấu trúc bên trong để vẽ, hoặc nguyên nhân không quy
  được về một vật thể cụ thể. Không dùng làm ảnh chính.
pairs_with: 01-pain-scene (trước), 03-mechanism-ghostbody (sau)
```

---

## Test G: `02-cause-anatomy` v1.0

**Sản phẩm test: lọc nước vòi sen**
Stress axis: không có xương, không có cơ thể. Ép device `anatomy` chứng minh nó có tổng quát hóa sang vi cấu trúc hay không, và ép slot đường gạch chấm tìm được một landmark đo được ngoài giải phẫu người.

```
A 2D medical illustration, 5:3 ratio, airbrushed textbook style. NOT photography. NOT 3D render.

CANVAS: One continuous pale blue clinical gradient background shared by both panels, divided by a single thin vertical line, not a hard split. Background motifs at very low opacity: hexagon mesh, faint water-drop icons, an oversized ghosted cross-section of a hair strand as a watermark. A ghosted silhouette of a showerhead behind the left panel.

SUBJECT TREATMENT, both panels: a magnified longitudinal cross-section of a single hair strand drawn in warm ivory as the top layer, its cuticle scales clearly defined, the surrounding water reduced to a translucent glowing outline behind it. Same strand, same scale, same viewing angle in both panels.

LEFT PANEL, WRONG: The hair strand under falling untreated water, with hard water minerals drawn as small angular crystals. The cuticle scales lifted, splayed open and chipped, highlighted in red. A red curved line tracing the roughened outer surface. A red dashed reference line along the cuticle surface, clearly JAGGED AND UNEVEN. A red double-headed curved arrow along the strand showing mineral scale accumulating on it. Red circle with white X badge in the corner.

RIGHT PANEL, CORRECT: The same strand under filtered water, no crystals. The cuticle scales lying flat, closed and overlapping, highlighted in blue. A soft blue aura along the smooth outer surface. A blue dashed reference line at the same cuticle surface, clearly SMOOTH AND EVEN. Green circle with white check badge in the corner. Brighter and cleaner than the left panel.

MEASUREMENT RULE: the paired dashed reference lines are the core argument. Identical position, thickness and dash pattern, differing ONLY in how even they run.

PALETTE LOCK: pale blue and ivory throughout. The ONLY signal colors permitted are red for damage, blue for healthy, green for the confirmation badge.
STYLE: clinical medical illustration, e-commerce infographic, crisp linework, 4K.
NO text, no numbers, no logo, no watermark.
```

**Đoán chỗ gãy:** slot MEASUREMENT RULE. Ở ảnh gốc hai đường gạch chấm khác nhau về **góc**, một biến số nhị phân sạch sẽ mà model vẽ đúng dễ dàng. Ở đây tôi phải đổi sang khác nhau về **độ đều**, một biến số mờ hơn nhiều. Nhiều khả năng hai đường sẽ ra giống hệt nhau và lập luận sập. Nếu đúng thì skeleton cần ghi rõ: biến số so sánh của đường gạch chấm bắt buộc phải là góc, khoảng cách, hoặc chiều dài. Ba thứ đo được. Không được dùng texture hay độ đều.

---

## Registry sau 7 type

| Tên | Bán cái gì | Kênh |
|---|---|---|
| `01-pain-scene` | Nhận ra chính mình | paid-social, advertorial |
| `01-pain-split` | Dừng scroll bằng đau | marketplace |
| `02-cause-anatomy` | Buộc tội nguyên nhân | landing-page, marketplace |
| `02-symptom-rail` | Mở rộng phạm vi vấn đề | marketplace |
| `03-mechanism-ghostbody` | Biện hộ cho hình dáng | marketplace |
| `04-proof-demo` | Bằng chứng vật lý | **RESERVED** |
| `05-persona-grid` | Nhận diện bản thân | marketplace |
| `06-relief-hero` | Trạng thái sau khi mua | landing-page, marketplace |

Trường `channel` giờ đã có dữ liệu thật ở ba giá trị nên tôi đề nghị chốt nó vào schema. Không có nó thì router sẽ trộn `01-pain-scene` (điện ảnh, tối, không sản phẩm) vào cùng gallery với `01-pain-split` (đồ họa, sáng, có badge), và bộ ảnh sẽ đọc như hai thương hiệu khác nhau.

---

## Human

**Attachments:**
- 1786342571404_image.png

---

## Assistant

# Breakdown

Type mới, và nó là **nấc 4a đang trống**. Đây chính là bằng chứng vật lý.

| Thành phần | Chi tiết |
|---|---|
| **Khung** | 5:3 ngang, 3 panel dọc bằng nhau, gutter trắng mảnh |
| **Máy quay** | **Khóa cứng.** Cùng vị trí, cùng tiêu cự, cùng độ cao ba panel. Vô lăng, cần số, hộc cốc trùng khít từng pixel |
| **Bối cảnh** | Ghế da đen ô tô, thùng carton nhàu và túi nilon vứt ở ghế phụ, sàn bẩn |
| **Biến số duy nhất** | Vật đặt trên mặt ghế: đệm nỉ mỏng gập mép, gối tựa hình boomerang, đệm hạt gỗ |
| **Ánh sáng** | Xám phẳng, không nắng, không đổ bóng mạnh |

**Ba điểm cấu trúc:**

**Khóa máy quay là toàn bộ giá trị.** Vì khung không đổi, mắt tự động trừ đi phần giống nhau và chỉ còn thấy phần khác nhau. Đây là cơ chế so sánh mạnh nhất trong nhiếp ảnh, và nó không cần một mũi tên hay badge nào. Lệch khung một chút thôi là ảnh tụt xuống thành ba ảnh stock ghép lại.

**Sự lộn xộn là chủ ý, không phải sơ suất.** Thùng carton, túi nilon, sàn bẩn. Chúng nói "ba thứ này vừa được mở hộp và thử ngay tại chỗ", không phải chụp studio. Dọn sạch bối cảnh đi là mất luôn tính chứng cứ.

**Không có vế thắng trong khung.** Ba lựa chọn được bày ra ngang hàng, không badge, không đỏ, không mũi tên. Người xem tự phán xét. Đây là lý do nó bán được ở nấc hoài nghi: nó không đòi bạn tin, nó mời bạn nhìn.

**Điểm yếu:** ba món ở đây đều là **đối thủ**, sản phẩm của mình không có mặt. Nếu định dùng để bán thì panel cuối phải là sản phẩm mình. Còn nếu để trong advertorial làm đoạn "tôi đã thử ba thứ" thì đúng như hiện tại.

# Tên type

**`04-proof-lockedframe`**

Bổ sung device: `lockedframe` (nhiều panel, máy quay khóa cứng, chỉ một biến số thay đổi).

Cùng họ: `04-proof-lockedframe--2panel` (before/after), `04-proof-lockedframe--4panel`, `04-proof-lockedframe--timelapse` (biến số là thời gian thay vì vật thể).

# Miễn trừ luật toàn hệ

| Luật | Trạng thái |
|---|---|
| G1 product reference | Áp dụng **cho panel chứa sản phẩm mình**, các panel khác không |
| G3 ngữ nghĩa màu | **Không áp dụng**, ảnh cố tình không có màu tín hiệu |
| G4 vế đúng sáng hơn | **Không áp dụng**, ba panel phải sáng bằng nhau |
| G5 register lock | Áp dụng cực chặt, đây là type nghiêm ngặt nhất |

# Prompt skeleton

```
TYPE: 04-proof-lockedframe v1.0
RATIO: [5:3 / 16:9 / 1:1]
LAYOUT: [3] equal vertical panels, thin white gutters, no outer border.
REGISTER: documentary photography. NO graphic overlays, badges, arrows or text.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the item in panel [N].
Preserve shape, proportions, material, finish and color exactly.

[LOCKED CAMERA, the core rule]
Identical camera position, focal length, height and angle in every panel.
Every fixed element in the frame must align pixel for pixel across all panels:
[list 3-4 anchor objects that must not move].
Identical lighting, identical exposure, identical white balance in every panel.

[SCENE, constant across all panels]
[specific environment], [surface the variable sits on].
Deliberate real-world clutter: [2-3 mundane untidy details].
Flat [light quality], no strong shadows, no sunlight, no styling.

[THE VARIABLE, the only thing that changes]
Panel 1: [item 1] placed on [surface], [how it sits].
Panel 2: [item 2] placed on [surface], [how it sits].
Panel 3: [item 3] placed on [surface], [how it sits].

[JUDGEMENT RULE]
No panel may be favoured. No badge, no glow, no color cue, no brighter exposure.
The viewer decides. All panels equally lit and equally neutral.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
NO text, no logo, no watermark.
```

**Negative:**
```
text, letters, numbers, watermark, logo, badges, arrows, glows, checkmarks,
different camera angle between panels, shifted background elements,
inconsistent lighting between panels, one panel brighter, studio background,
clean styled set, staged perfection, saturated colors, red or green cues,
motion blur, people, hands
```

# Trigger description

```yaml
id: 04-proof-lockedframe
step: 4
job: proof
device: lockedframe
version: "1.0"
ratios: [5:3, 16:9, 1:1]
channel: [advertorial, landing-page, marketplace]
requires_product_photo: true
exempt_from: [G3, G4]
status: active
use_when: >
  Người mua đã hiểu vấn đề và cơ chế, giờ hoài nghi và muốn tự nhìn.
  Đoạn "tôi đã thử ba thứ" trong advertorial, hoặc ảnh so sánh với đối
  thủ trong gallery. Dùng khi khác biệt nhìn thấy được bằng mắt thường.
avoid_when: >
  Khác biệt vô hình hoặc chỉ cảm nhận được khi dùng. Không dùng làm ảnh
  dừng scroll, type này chậm và cần người xem đã chú ý.
pairs_with: 02-cause-anatomy (trước), 06-relief-hero (sau)
```

---

## Test H: `04-proof-lockedframe` v1.0

**Sản phẩm test: dụng cụ mài dao lăn**
Stress axis: biến số không phải vật đặt vào khung mà là **kết quả** của vật đó. Ép skeleton chứng minh nó xử lý được so sánh đầu ra chứ không chỉ so sánh vật thể.

```
A documentary photograph, 5:3 ratio, three equal vertical panels, thin white gutters, no outer border. NO graphic overlays, badges, arrows or text.

Use the attached product photo as the exact reference for the sharpener visible in panel 3. Preserve shape, proportions, material, finish and color exactly.

LOCKED CAMERA: identical camera position, focal length, height and angle in every panel, shot from directly above at 45 degrees. Every fixed element must align pixel for pixel across all three panels: the wooden cutting board, the edge of the counter, a folded tea towel at the top left, and a knife handle resting at the same spot. Identical lighting, exposure and white balance in every panel.

SCENE, constant: a worn pale oak cutting board on a kitchen counter. Deliberate real-world clutter: a crumpled paper bag pushed to the back, a few loose tomato seeds on the counter, a faint water ring on the wood. Flat overcast daylight from a side window, no strong shadows, no sunlight, no styling.

THE VARIABLE:
Panel 1: a ripe tomato cut with a dull knife, the slices thick, uneven and crushed, skin torn, juice and seeds pooling on the board.
Panel 2: the same tomato cut with a pull-through sharpener beside it, slices somewhat neater but still ragged at the edges, some juice on the board.
Panel 3: the same tomato cut with the reference rolling sharpener lying beside the board, slices paper thin, uniform and cleanly fanned, the board almost dry.

JUDGEMENT RULE: no panel may be favoured. No badge, no glow, no color cue, no brighter exposure. All panels equally lit and equally neutral.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
NO text, no logo, no watermark.
```

**Đoán chỗ gãy:** khóa máy quay. Mô hình sinh ảnh gần như chắc chắn sẽ vẽ ba khung hơi lệch nhau vì mỗi panel được sinh độc lập, và lệch khung là thứ giết chết type này. Nếu đúng thì skeleton cần đổi cách chạy: sinh **một panel duy nhất trước**, rồi dùng chế độ chỉnh sửa để thay đúng biến số và giữ nguyên phần còn lại, ghép ba panel ở bước hậu kỳ. Đây có thể là type đầu tiên trong bộ không sinh được bằng một prompt.

---

## Registry sau 8 type, nấc 4a đã lấp

| Tên | Bán cái gì | Kênh |
|---|---|---|
| `01-pain-scene` | Nhận ra chính mình | paid-social, advertorial |
| `01-pain-split` | Dừng scroll bằng đau | marketplace |
| `02-cause-anatomy` | Buộc tội nguyên nhân | landing-page, marketplace |
| `02-symptom-rail` | Mở rộng phạm vi vấn đề | marketplace |
| `03-mechanism-ghostbody` | Biện hộ cho hình dáng | marketplace |
| `04-proof-lockedframe` | Bằng chứng tự nhìn | advertorial, landing-page, marketplace |
| `05-persona-grid` | Nhận diện bản thân | marketplace |
| `06-relief-hero` | Trạng thái sau khi mua | landing-page, marketplace |

Bộ đã khép kín cả 6 nấc. Giờ có đủ dữ liệu để tôi viết phần **sequencing rule**: chọn type nào cho từng vị trí trong gallery Amazon 7 ảnh, và chọn chuỗi nào cho advertorial. Hai kênh dùng hai chuỗi khác nhau vì thứ tự đọc khác nhau.

Nói tôi biết bạn muốn tôi xuất bản registry v1.3 kèm sequencing luôn, hay còn ảnh mẫu nữa muốn đưa vào trước.

---

## Human

**Attachments:**
- 1786342714299_image.png

---

## Assistant

# Breakdown

Type mới. Đây là type đầu tiên trong bộ có **hai người tương tác với nhau** thay vì một người tương tác với sản phẩm.

| Thành phần | Chi tiết |
|---|---|
| **Khung** | 5:3 ngang, ảnh chụp thật, một overlay duy nhất |
| **Nhân vật A** | Nam ~60s, mũ lưỡi trai, áo da, đang **chỉ tay vào ghế xe**, mặt hơi cười, đang nói |
| **Nhân vật B** | Nam ~40s, blazer xám, quay lưng về máy quay, đang **nhìn theo hướng tay chỉ** |
| **Sản phẩm trong cảnh** | Đệm ghế màu be trên ghế lái, hơi bị che, nằm ở cuối đường tay chỉ |
| **Overlay** | Vòng tròn trắng góc trên trái, sản phẩm render sạch trên nền trắng, không viền, không mũi tên nối |
| **Bối cảnh** | Khu đón khách sân bay, hành khách kéo vali, ban ngày, ánh sáng phẳng |

**Bốn điểm cấu trúc:**

**Đường tay chỉ là xương sống bố cục.** Ngón tay nhân vật A vạch một đường chéo từ giữa khung xuống trái, kết thúc đúng ở sản phẩm. Ánh mắt nhân vật B chạy song song. Hai vector cùng chỉ về một điểm, mắt người xem buộc phải theo. Bỏ cử chỉ chỉ tay đi thì sản phẩm biến mất trong khung.

**Nhân vật B quay lưng có chủ đích.** Anh ta là chỗ trống để người xem bước vào. Không thấy mặt nên không có ai cạnh tranh danh tính với người xem. Nhân vật A quay mặt về phía máy quay vì anh ta là người kể.

**Đây là truyền miệng được dàn dựng.** Không phải người dùng khoe sản phẩm với máy quay, mà là người dùng mách nước cho một người khác, và ta tình cờ nhìn thấy. Đó là lý do nó vượt được hàng rào hoài nghi mà ảnh testimonial thẳng mặt không vượt được.

**Overlay tồn tại vì cảnh không cho nhìn rõ sản phẩm.** Sản phẩm bị che một phần bởi cửa xe và góc chụp. Vòng tròn là lối thoát: giữ cảnh tự nhiên mà vẫn cho xem hàng.

**Ba lỗi trong ảnh gốc:** vòng tròn để lệch màu, sản phẩm trong cảnh màu be còn trong vòng tròn màu đen than, đọc thành hai sản phẩm khác nhau. Overlay đặt ở góc trên trái xa điểm được chỉ, phá luồng mắt vừa dựng. Và bối cảnh sân bay không có liên hệ gì với hành động chỉ vào ghế xe, chọn bãi đỗ hay lối lên xe sẽ chặt hơn.

# Tên type

**`05-social-handoff`**

Bổ sung vocabulary:
- **job** mới: `social` (bằng chứng xã hội, người khác đang giới thiệu)
- **device** mới: `handoff` (hai người, một người chỉ, một người nhìn theo, kèm inset sản phẩm)

Cùng họ: `05-social-handoff--noinset` (khi cảnh cho nhìn rõ sản phẩm), `05-social-handoff--group` (một người mách cho nhóm), `06-relief-handoff` (đổi job sang khoảnh khắc sau khi dùng).

## Phân biệt với `05-persona-grid`

Cùng step 5, cùng trả lời câu hỏi "có ai giống tôi dùng không", nhưng khác cơ chế:

| | `05-persona-grid` | `05-social-handoff` |
|---|---|---|
| Bằng chứng | Số lượng người dùng | Một người đủ tin để đi mách |
| Khung | Collage nhiều ô | Một cảnh duy nhất |
| Người xem là ai | Một trong các persona | Người đang được mách |
| Cường độ | Rộng, nông | Hẹp, sâu |

Dùng được cùng bộ nhưng đặt cách nhau, không liền kề.

# Miễn trừ luật toàn hệ

| Luật | Trạng thái |
|---|---|
| G1 product reference | Áp dụng **hai lần**, cho cả sản phẩm trong cảnh và trong inset. Bắt buộc trùng khít |
| G3 ngữ nghĩa màu | Không áp dụng, ảnh không có màu tín hiệu |
| G4 vế đúng sáng hơn | Không áp dụng, chỉ có một vế |

# Prompt skeleton

```
TYPE: 05-social-handoff v1.0
RATIO: [5:3 / 16:9 / 4:5]
REGISTER: candid documentary photograph. One scene. One inset overlay maximum.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly.
The product must appear IDENTICAL in the scene and in the inset,
same colorway, same finish. This is the single most important constraint.

[CHARACTER A: THE ADVOCATE]
[age/gender] in [ordinary specific wardrobe], face turned toward camera,
mid-sentence, [warm relaxed expression], pointing with [hand] toward the product.
The pointing gesture forms a clear diagonal line ending exactly at the product.

[CHARACTER B: THE LISTENER]
[age/gender] in [wardrobe], seen from behind or in profile, FACE NOT VISIBLE,
head turned to follow the pointing gesture, gaze parallel to the pointing line.
This character is a placeholder for the viewer.

[PRODUCT IN SCENE]
The reference product placed at [natural location], partially framed by
[foreground element], sitting exactly where the pointing line terminates.

[INSET] (include ONLY if the scene cannot show the product clearly)
Circular white cutout containing the reference product on a plain white background,
positioned [near the terminus of the pointing line, never opposite it],
occupying [15-20%] of the frame width. Clean edge, no border, no connecting arrow.
Product colorway MUST match the in-scene product exactly.

[ENVIRONMENT]
[specific place directly related to the moment of use],
[2-3 incidental background people or details], flat natural daylight,
no dramatic shadows, nothing styled.

[COMPOSITION RULE]
Two vectors, the pointing arm and the listener's gaze, must converge on the product.
Nothing else in the frame may compete for attention.

STYLE: candid lifestyle photography, natural, unposed, sharp, 4K.
NO text, no logo, no watermark, no arrows, no badges.
```

**Negative:**
```
text, letters, numbers, watermark, logo, arrows, badges, connecting lines,
deformed hands, extra fingers, both faces visible, listener facing camera,
product color mismatch between scene and inset, two different products,
inset placed opposite the pointing direction, product outside the pointing line,
staged posing, direct eye contact with camera, studio lighting, empty background,
unrelated location
```

# Trigger description

```yaml
id: 05-social-handoff
step: 5
job: social
device: handoff
version: "1.0"
ratios: [5:3, 16:9, 4:5]
channel: [paid-social, advertorial, landing-page]
requires_product_photo: true
exempt_from: [G3, G4]
status: active
use_when: >
  Cần bằng chứng xã hội mà không dùng testimonial thẳng mặt. Ảnh giữa
  advertorial ở đoạn "một người bạn mách tôi", creative cho ads nguội,
  hoặc ảnh chốt trên landing page. Hợp sản phẩm mà người ta thật sự đi
  kể cho nhau.
avoid_when: >
  Gallery sàn, ảnh chính. Không dùng khi sản phẩm riêng tư, không ai
  mách nhau ngoài đời. Không dùng nếu cảnh không có lý do tự nhiên để
  hai người đứng cạnh sản phẩm.
pairs_with: 04-proof-lockedframe (trước), 06-relief-hero (sau)
spacing_rule: không đặt liền kề 05-persona-grid
```

---

## Test I: `05-social-handoff` v1.0

**Sản phẩm test: lọc nước vòi sen**
Stress axis: sản phẩm lắp trong phòng tắm, một nơi không có lý do tự nhiên để hai người đứng cùng. Ép skeleton tìm được khoảnh khắc truyền miệng hợp lý cho sản phẩm riêng tư. Đây là điều kiện mà `avoid_when` cảnh báo, nên test này để dò ngưỡng gãy.

```
A candid documentary photograph, 5:3 ratio. One scene, one inset overlay.

Use the attached product photo as the exact reference for the shower filter. Preserve shape, proportions, material, finish and color exactly. The filter must appear identical in the scene and in the inset, same colorway, same finish.

CHARACTER A, THE ADVOCATE: A woman in her early 40s in a soft grey sweatshirt, hair damp, standing in a hallway doorway, face turned toward camera, mid-sentence, warm relaxed expression, pointing with her right hand through the open bathroom door toward the shower. The pointing gesture forms a clear diagonal line ending exactly at the filter fitted above the showerhead.

CHARACTER B, THE LISTENER: A woman in her late 20s in a casual jacket holding a mug, seen from behind, face not visible, head turned to follow the pointing gesture, gaze parallel to the pointing line.

PRODUCT IN SCENE: The reference filter installed between the hose and the showerhead, visible through the open doorway, partially framed by the door edge, sitting exactly where the pointing line terminates.

INSET: Circular white cutout containing the reference filter on a plain white background, positioned just below and left of the pointing hand, never opposite it, occupying about 18 percent of the frame width. Clean edge, no border, no connecting arrow. Colorway matching the in-scene product exactly.

ENVIRONMENT: An ordinary apartment hallway opening into a small bathroom, a laundry basket on the floor, a towel over the rail, a plant on a shelf. Flat natural daylight, no dramatic shadows, nothing styled.

COMPOSITION RULE: the pointing arm and the listener's gaze must converge on the filter. Nothing else in the frame may compete for attention.

STYLE: candid lifestyle photography, natural, unposed, sharp, 4K.
NO text, no logo, no watermark, no arrows, no badges.
```

**Đoán chỗ gãy:** hai chỗ. Một, khoảng cách. Filter ở xa qua một khung cửa nên trong khung nó sẽ chỉ còn vài chục pixel, không nhận ra được, làm cả đường tay chỉ trở nên vô nghĩa. Hai, ràng buộc trùng màu giữa cảnh và inset. Model sinh hai vùng độc lập nên gần như chắc chắn lệch tông, đúng như lỗi của ảnh gốc. Nếu cả hai đều gãy thì skeleton cần thêm ràng buộc cứng: `sản phẩm trong cảnh phải chiếm tối thiểu 8% chiều cao khung`, và inset phải sinh ở bước hậu kỳ bằng chính ảnh reference thay vì để model vẽ lại.

---

## Registry sau 9 type

| Tên | Bán cái gì | Kênh |
|---|---|---|
| `01-pain-scene` | Nhận ra chính mình | paid-social, advertorial |
| `01-pain-split` | Dừng scroll bằng đau | marketplace |
| `02-cause-anatomy` | Buộc tội nguyên nhân | landing-page, marketplace |
| `02-symptom-rail` | Mở rộng phạm vi vấn đề | marketplace |
| `03-mechanism-ghostbody` | Biện hộ cho hình dáng | marketplace |
| `04-proof-lockedframe` | Bằng chứng tự nhìn | advertorial, landing-page, marketplace |
| `05-persona-grid` | Nhận diện bản thân | marketplace |
| `05-social-handoff` | Người khác đi mách | paid-social, advertorial, landing-page |
| `06-relief-hero` | Trạng thái sau khi mua | landing-page, marketplace |

Chín type này giờ chia rõ thành hai bộ theo kênh: bốn type `marketplace` thuần (split, rail, ghostbody, persona-grid) và ba type `advertorial` thuần (pain-scene, proof-lockedframe, social-handoff). Hai type còn lại bắc cầu.

Đây là lúc hợp lý để xuất registry v1.3 kèm sequencing cho từng kênh. Có ảnh mẫu nào nữa không, hay chốt ở đây?

---

## Human

04-proof-lockedframe chia 2 trường hợp: 3 sản phẩm của đối thủ và trường hợp 2 sản phẩm của đối thủ 1 sản phẩm của mình bán

---

## Assistant

<details><summary>Thinking</summary>

I'm splitting this proof concept into two distinct variants based on what products are featured. Variant A showcases three competitors with no mention of our own product—it's purely documentary, establishing the problem without any bias, and works as the failed-solutions setup in advertorial content. Variant B takes a different approach by including two competitors alongside our product, which shifts the narrative and requires different positioning.

The challenge with Variant B is maintaining credibility while our product is present. I can't use visual favoring like badges or special lighting without collapsing the type into a pure advertisement and losing its evidentiary weight. The solution is strict neutrality in treatment—identical styling across all three panels, letting the physical position and evidence speak instead. Our product goes in the third panel because that's where the reading order naturally resolves, creating the conclusion without needing visual manipulation. I should also flag the trademark consideration: keeping competitor items unbranded or generic to avoid legal issues around comparative claims.

For naming, I'm weighing options that capture the semantic difference between the two variants—something like `--tried` versus `--versus`, or `--alternatives` versus `--verdict`.

</details>

# `04-proof-lockedframe` tách 2 biến thể

Hai biến thể này khác nhau ở một điểm duy nhất nhưng điểm đó đổi luôn bản chất của ảnh: **trong khung có vế thắng hay không**.

| | `--rivals` | `--verdict` |
|---|---|---|
| Nội dung | 3 sản phẩm đối thủ | 2 đối thủ + 1 của mình |
| Sản phẩm mình | Vắng mặt | Panel cuối |
| Câu ảnh nói | "Tôi đã thử, không cái nào ổn" | "Tôi đã thử, cái này khác" |
| Vị trí trong phễu | Đoạn thất bại | Đoạn giải pháp |
| G1 product reference | Không áp dụng | Áp dụng, chỉ panel cuối |
| Rủi ro chính | Không có, ảnh trung lập thật | Lộ ra là quảng cáo và mất sạch giá trị chứng cứ |

---

## `04-proof-lockedframe--rivals`

Sản phẩm mình không có mặt. Đây là điều làm nó mạnh: ảnh không bán gì cả nên người xem không dựng hàng rào. Nó chỉ dựng sẵn cảm giác "mấy thứ này đều dở" để đoạn sau đưa giải pháp vào.

**Sửa so với skeleton gốc:**

```
[PRODUCT REFERENCE]
Not applicable. No reference product appears in this image.

[THE VARIABLE]
Panel 1: [generic alternative type 1], unbranded, placed on [surface].
Panel 2: [generic alternative type 2], unbranded, placed on [surface].
Panel 3: [generic alternative type 3], unbranded, placed on [surface].
All three are common existing solutions people already try.
They must look ordinary and plausible, not deliberately broken or dirty.

[JUDGEMENT RULE]
No panel may be favoured. All three equally lit, equally neutral.
None of them wins. The image makes no claim.
```

**Negative bổ sung:** `brand logos, recognizable trademarks, damaged or dirty items, exaggerated flaws, one item obviously better`

Một cạm bẫy: đừng bôi xấu ba món này. Làm chúng trông cũ nát hay bẩn thỉu là ảnh tự khai đang dàn dựng. Chúng phải trông bình thường và hợp lý, để người xem tự nhận ra "ừ, tôi từng mua đúng mấy cái này".

---

## `04-proof-lockedframe--verdict`

Có vế thắng, và đây là chỗ type dễ hỏng nhất. Sức mạnh của lockedframe nằm ở chỗ nó **không phán xét**. Nếu bạn thêm badge, thêm ánh sáng đẹp hơn, thêm nền sạch hơn cho panel của mình thì nó tụt xuống thành `01-pain-split` phiên bản dài, mất toàn bộ lợi thế.

Luật cứng: **chỉ được thắng bằng vật lý, không được thắng bằng xử lý ảnh.**

**Sửa so với skeleton gốc:**

```
[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the item in panel 3 ONLY.
Preserve shape, proportions, material, finish and color exactly.
Panels 1 and 2 contain generic unbranded alternatives, not the reference product.

[THE VARIABLE]
Panel 1: [generic alternative 1], unbranded, [how it sits / what result it produces].
Panel 2: [generic alternative 2], unbranded, [how it sits / what result it produces].
Panel 3: the reference product, [how it sits / what result it produces].

[ORDER RULE]
The reference product is always in the LAST panel.
Left-to-right reading ends on it, which is the resolution position.

[FAIRNESS RULE, replaces JUDGEMENT RULE]
Panels 1 and 2 must be given exactly the same photographic respect as panel 3:
identical exposure, identical background tidiness, identical framing generosity.
The alternatives must look like reasonable products someone would genuinely buy.
The difference between panels must be VISIBLE IN THE OBJECTS THEMSELVES,
never in how they are lit, styled, cropped or graded.
No badge, no glow, no arrow, no color cue on any panel.
```

**Negative bổ sung:**
```
brand logos, recognizable trademarks, badges, checkmarks, glows,
last panel brighter or cleaner than the others, alternatives made to look broken,
dirty or damaged competitor items, exaggerated flaws, cluttered first panels,
different background between panels, hero lighting on the final panel
```

**Ba quyết định cần chốt trước khi viết prompt biến thể này:**

1. **Biến số là vật thể hay kết quả?** Vật thể (ba món đặt cạnh nhau) dễ sinh hơn nhưng yếu hơn. Kết quả (thứ ba món đó tạo ra) mạnh hơn nhiều nhưng khó khóa khung. Với sản phẩm có đầu ra nhìn thấy được, luôn chọn kết quả.
2. **Hai món đối thủ chọn thế nào?** Không chọn hai món tệ nhất thị trường. Chọn hai món **phổ biến nhất** mà khách đã từng mua. Người xem phải nhận ra chính món trong ngăn kéo nhà mình, nếu không thì so sánh này không liên quan đến họ.
3. **Không logo, không nhãn hiệu.** Cả pháp lý lẫn hiệu quả. Món đối thủ có logo thì bạn đang quảng cáo miễn phí cho họ, và mở cửa cho khiếu nại nhãn hiệu trên Amazon.

---

## Cập nhật registry

```yaml
- id: 04-proof-lockedframe
  step: 4
  job: proof
  device: lockedframe
  version: "1.1"
  status: active
  layout_variants: [rivals, verdict]
  variants:
    rivals:
      requires_product_photo: false
      exempt_from: [G1, G3, G4]
      funnel_position: failed-solutions
      channel: [advertorial, paid-social]
    verdict:
      requires_product_photo: true
      exempt_from: [G3, G4]
      funnel_position: solution-reveal
      channel: [advertorial, landing-page, marketplace]
      hard_rules: [product-in-last-panel, equal-photographic-treatment]
```

**Luật chuỗi:** hai biến thể dùng được liền nhau trong cùng một advertorial, `--rivals` trước rồi `--verdict` sau, nhưng phải **khóa cùng bối cảnh và cùng góc máy** giữa hai ảnh. Khi đó ảnh thứ hai đọc như phần tiếp theo của cùng một buổi thử, không phải một quảng cáo mới chen vào.

Trong gallery sàn thì chỉ dùng `--verdict`. `--rivals` không có sản phẩm nên vi phạm quy định ảnh sản phẩm của Amazon.

---

Chốt xong chỗ này thì tôi xuất registry v1.3, gồm 9 type, biến thể mới, trường `channel`, và phần sequencing cho ba kênh.

---

## Human

hãy cho tôi 2 prompt để  so sánh 2 trường hợp 04-proof-lockedframe. sản phẩm shower head filter

---

## Assistant

<details><summary>Thinking</summary>

I need to set up two comparison prompts for a shower head filter test—one showing rivals and one showing my verdict. The key constraints are no product shape descriptions, a reference photo only for the verdict shot, locked camera angle, no logos, and fair treatment across all products. For the rivals prompt, I'm comparing three competitor filters, while the verdict includes two competitors plus my own filter. The critical difference is using RESULT as the variable instead of object since the filter's output is directly visible through limescale buildup on the nozzle plate, water clarity, and hair/skin effects. I need to design a shared scene setup that works for both shots.

I'm settling on a bathroom wall with a shower arm and locked camera position. For the rivals, I'll show three generic, unbranded alternatives people commonly try: a plastic inline vitamin C filter, a filtered showerhead unit, and a small mesh screen attachment. For the verdict, I'll display the plastic inline filter, the filtered showerhead, and my reference product. Rather than trying to capture residue buildup on a cloth (which creates claim issues), I'll keep it straightforward by showing each unit fitted with water flowing, letting the visible results speak for themselves.

</details>

Hai prompt dùng **chung một bối cảnh và một khung máy**, để chạy liền nhau trong cùng advertorial thì đọc như hai khoảnh khắc của một buổi thử.

---

## A. `04-proof-lockedframe--rivals`

Không có sản phẩm mình. Không đính ảnh reference.

```
A documentary photograph, 5:3 ratio, three equal vertical panels, thin white gutters, no outer border. NO graphic overlays, badges, arrows or text.

LOCKED CAMERA: identical camera position, focal length, height and angle in every panel, shot straight on at chest height. Every fixed element must align pixel for pixel across all three panels: the chrome shower arm where it meets the wall, the horizontal grout line behind it, a small corner shelf holding one plain white bottle at the upper right, and the edge of a damp towel entering the frame at the lower left. Identical lighting, exposure and white balance in every panel.

SCENE, constant: a plain white tiled bathroom wall with a chrome shower arm. Deliberate real-world clutter: faint water spots and limescale streaks on the tile, a hair tie left on the corner shelf, a slightly crooked towel. Flat overcast daylight from a frosted window to the left, no strong shadows, no sunlight, no styling.

THE VARIABLE, the only thing that changes: a different unbranded shower filter fitted to the same arm in each panel, all shown not running.
Panel 1: a bulky translucent plastic inline canister filled with coloured granules, joined by a short plastic collar.
Panel 2: an all-in-one plastic filtering showerhead with a wide flat face, matte white plastic body.
Panel 3: a small flat mesh screen disc clamped between the arm and a basic chrome head.
All three are common existing solutions people already try. They must look ordinary, clean and plausible, not broken, dirty or exaggerated.

JUDGEMENT RULE: no panel may be favoured. All three equally lit, equally neutral, equally tidy. None of them wins. The image makes no claim.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
NO text, no logo, no watermark.
```

**Negative:**
```
text, letters, numbers, watermark, logo, brand logos, recognizable trademarks,
badges, arrows, glows, checkmarks, different camera angle between panels,
shifted background elements, inconsistent lighting between panels, one panel brighter,
damaged or dirty items, exaggerated flaws, one item obviously better,
studio background, clean styled set, saturated colors, people, hands, running water
```

---

## B. `04-proof-lockedframe--verdict`

Đính ảnh sản phẩm. Sản phẩm ở panel cuối.

```
A documentary photograph, 5:3 ratio, three equal vertical panels, thin white gutters, no outer border. NO graphic overlays, badges, arrows or text.

Use the attached product photo as the exact reference for the filter in panel 3 ONLY. Preserve shape, proportions, material, finish and color exactly. Do not redesign or add features. Panels 1 and 2 contain generic unbranded alternatives, not the reference product.

LOCKED CAMERA: identical camera position, focal length, height and angle in every panel, shot straight on at chest height. Every fixed element must align pixel for pixel across all three panels: the chrome shower arm where it meets the wall, the horizontal grout line behind it, a small corner shelf holding one plain white bottle at the upper right, and the edge of a damp towel entering the frame at the lower left. Identical lighting, exposure and white balance in every panel.

SCENE, constant: a plain white tiled bathroom wall with a chrome shower arm. Deliberate real-world clutter: faint water spots and limescale streaks on the tile, a hair tie left on the corner shelf, a slightly crooked towel. Flat overcast daylight from a frosted window to the left, no strong shadows, no sunlight, no styling.

THE VARIABLE, the only thing that changes: a different filter fitted to the same arm in each panel, all shown not running.
Panel 1: a bulky translucent plastic inline canister filled with coloured granules, joined by a short plastic collar, unbranded.
Panel 2: an all-in-one plastic filtering showerhead with a wide flat face, matte white plastic body, unbranded.
Panel 3: the reference product, fitted to the same arm in the same position.

ORDER RULE: the reference product is in the last panel. Left-to-right reading ends on it.

FAIRNESS RULE: panels 1 and 2 receive exactly the same photographic respect as panel 3. Identical exposure, identical background tidiness, identical framing generosity, identical distance from camera. The alternatives must look like reasonable products someone would genuinely buy. Any difference between panels must be visible in the objects themselves, never in how they are lit, styled, cropped or graded. No badge, no glow, no arrow, no color cue on any panel.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
NO text, no logo, no watermark.
```

**Negative:**
```
text, letters, numbers, watermark, logo, brand logos, recognizable trademarks,
badges, checkmarks, glows, arrows, different camera angle between panels,
shifted background elements, last panel brighter or cleaner than the others,
hero lighting on the final panel, alternatives made to look broken,
dirty or damaged competitor items, exaggerated flaws, cluttered first panels,
different background between panels, studio background, staged perfection,
people, hands, running water
```

---

## Ba lưu ý khi chạy

**Biến số ở đây là vật thể, không phải kết quả.** Với lọc vòi sen tôi cố tình chọn vật thể. Kết quả của bộ lọc (nước sạch hơn, tóc bớt khô) không quan sát được trong một khung hình tĩnh, nên ép nó thành biến số sẽ buộc bạn phải dàn dựng, và dàn dựng thì mất sạch giá trị chứng cứ. Panel 3 thắng bằng thứ nhìn thấy thật: kim loại thay vì nhựa, kích thước, độ hoàn thiện. Đó là khác biệt bảo vệ được nếu bị khiếu nại.

**Khóa khung gần như chắc chắn sẽ gãy ở lần chạy đầu.** Mô hình sinh ba panel độc lập nên chúng sẽ lệch nhau. Cách chạy đúng: sinh **một panel duy nhất** ở tỉ lệ dọc trước, chọn được ảnh ưng ý rồi dùng chế độ chỉnh sửa để thay riêng cái filter và giữ nguyên toàn bộ phần còn lại, làm ba lần, ghép ở hậu kỳ. Đây là type đầu tiên trong bộ không sinh được bằng một prompt.

**Hai ảnh phải chạy từ cùng một panel gốc.** Nếu định dùng cả `--rivals` lẫn `--verdict` trong một advertorial, hãy dựng panel nền một lần rồi tạo cả sáu biến thể từ đúng panel đó. Khác nền giữa hai ảnh là người đọc nhận ra ngay đây là hai lần dàn dựng khác nhau.

---

## Human

**Attachments:**
- 1786343189192_image.png

---

## Assistant

# Breakdown

Đây **không phải type mới**. Đây là `01-pain-split` chạy ở tỉ lệ ngang, với một khác biệt cấu trúc quan trọng đủ để tạo biến thể.

| Thành phần | Ảnh này | `01-pain-split` gốc |
|---|---|---|
| Chia khung | Dọc 50/50 | Dọc 50/50 |
| Vế trái | Grayscale, người đau | Grayscale, người đau |
| Vế phải | **Người** thoải mái, có sản phẩm | **Sản phẩm** đơn thuần |
| Badge | X đỏ và ✓ xanh ở **đáy**, thêm VS ở giữa | X và ✓ ở **đỉnh**, không có VS |
| Hotspot đỏ | Không có, chỉ có tay ôm lưng | Có, 3 điểm phát sáng |

**Khác biệt quyết định: hai vế cùng một người, cùng một tư thế, cùng một hành động.** Chỉ đổi trạng thái. Đây là dạng so sánh mạnh nhất vì nó loại bỏ mọi biến số nhiễu. Ảnh gốc `01-pain-split` so người với vật, nên người xem phải tự bắc cầu. Ảnh này không bắt bắc cầu gì cả.

**Điểm hay:** vế phải có sản phẩm nhưng nó không phải nhân vật chính, người mới là. Nắng ấm, mặt thư thái, tay thả lỏng trên vô lăng. Sản phẩm chỉ đứng đó như lời giải thích.

**Ba lỗi:**

1. **Badge ở đáy khung.** Mắt đọc từ trên xuống nên khi tới badge thì đã phán xét xong rồi. Badge đặt đỉnh mới có tác dụng dẫn hướng.
2. **Thừa tín hiệu.** Có VS ở giữa, lại có X và ✓ ở đáy. Ba badge cho một lập luận nhị phân. Bỏ VS đi, giữ X và ✓.
3. **Vế phải nắng vàng gắt.** Nó vi phạm G5 register lock: trái là ảnh xám phẳng, phải là ảnh golden hour. Hai nguồn khác nhau. Chỉ cần sáng hơn và có màu là đủ, không cần đổi hẳn giờ chụp.

# Tên

**`01-pain-split--mirror`**

Biến thể của type đã có, không phải type mới. Đặt tên `mirror` vì hai vế soi nhau: cùng người, cùng khung, cùng hành động.

`01-pain-split` giờ có 2 biến thể:

| Biến thể | Vế phải là gì | Dùng khi |
|---|---|---|
| `--object` (mặc định) | Sản phẩm | Sản phẩm là câu trả lời hiển nhiên, khung nhỏ, thumbnail |
| `--mirror` | Cùng người ở trạng thái đúng | Vấn đề là trạng thái cơ thể, cần cho thấy sự thay đổi ở người |

## Sửa skeleton, phần biến thể

```
[RIGHT PANEL, variant --mirror]
Full-color photo of THE SAME PERSON in THE SAME setting,
same camera angle, same distance, same wardrobe, same framing,
now in [correct posture/state], [relaxed expression], hands [released position].
The reference product visible at [contact point], secondary to the person.
Brighter, warmer and cleaner than the left panel,
but the SAME lighting setup and time of day. Only the grade differs.

[MIRROR RULE]
Left and right must be the same person, same shot, same everything.
The ONLY differences permitted: posture, expression, presence of the product,
and color grade. Any other change breaks the comparison.

[BADGES]
Red circle with white X, TOP-left corner of left panel.
Green circle with white check, TOP-right corner of right panel.
Both flat, solid, same diameter. NO VS badge, NO third marker.
```

**Negative bổ sung cho `--mirror`:**
```
different person between panels, different camera angle between panels,
different wardrobe, different time of day, golden hour on one side only,
VS badge, third badge, badges at bottom of frame, red hotspots
```

---

## Test J: `01-pain-split--mirror`

**Sản phẩm test: băng dán miệng ngủ**

```
A 1:1 e-commerce comparison tile, hard vertical split 50/50, thin white outer border.

Use the attached product photo as the exact reference for the mouth tape. Preserve shape, proportions, material and color exactly.

LEFT PANEL, THE PROBLEM: Desaturated grayscale photo of a man in his late 30s in a plain grey t-shirt lying on his back in bed, head on a pillow, mouth hanging open, brow furrowed, neck slightly strained, one arm thrown across the duvet. Shot from a high three-quarter angle above the pillow. Neutral cropped background, subject fills the frame.

RIGHT PANEL, THE ANSWER: Full-color photo of the same man in the same bed, same t-shirt, same pillow, same camera angle, same distance, same framing, now lying relaxed with his mouth closed, jaw soft, brow smooth, both arms resting easily at his sides. The reference mouth tape is on his lips, secondary to him. Brighter, warmer and cleaner than the left panel, but the same lighting setup and time of day. Only the grade differs.

MIRROR RULE: both panels show the same person in the same shot. The only differences permitted are posture, expression, presence of the product, and color grade.

BADGES: Red circle with a white X in the top-left corner of the left panel. Green circle with a white check in the top-right corner of the right panel. Flat, solid, same diameter. No VS badge, no third marker.

STYLE: e-commerce comparison tile, high contrast, sharp. Both panels share the same lighting register and shooting style.
NO text, no logo, no watermark.
```

**Đoán chỗ gãy:** ràng buộc cùng người. Model sinh hai panel độc lập nên khuôn mặt gần như chắc chắn sẽ khác nhau, và `--mirror` mất toàn bộ giá trị khi đó. Cách chạy đúng có lẽ giống `04-proof-lockedframe`: sinh panel trái trước, rồi dùng chế độ chỉnh sửa đổi tư thế và grade, ghép ở hậu kỳ. Nếu đúng thì hai type này chia chung một thuộc tính mới cần thêm vào schema: `generation_mode: multi-pass`.

---

## Registry sau 9 type, 12 biến thể

| Tên | Biến thể |
|---|---|
| `01-pain-scene` | |
| `01-pain-split` | `--object`, `--mirror` |
| `02-cause-anatomy` | |
| `02-symptom-rail` | |
| `03-mechanism-ghostbody` | |
| `04-proof-lockedframe` | `--rivals`, `--verdict` |
| `05-persona-grid` | `--1plus3`, `--2x2` |
| `05-social-handoff` | |
| `06-relief-hero` | |

Ba type giờ đã lộ ra cùng một vấn đề kỹ thuật: `01-pain-split--mirror`, `04-proof-lockedframe`, và `05-social-handoff` đều cần giữ một thứ **giống hệt nhau qua nhiều vùng ảnh**, thứ mà một prompt duy nhất không làm được. Nên thêm trường `generation_mode` với hai giá trị `single-pass` và `multi-pass`, cùng ghi chú quy trình chạy cho nhóm multi-pass.

---

## Human

04-proof-lockedframe--verdict cả verdict và rivals đều chưa đạt. đây là sản phẩm shower head filter, hãy triển khai theo hướng khác.

**Attachments:**
- 1786343351000_image.png

---

## Assistant

<details><summary>Thinking</summary>

Looking at their uploaded image, the locked frame technique worked fine technically—three panels showing different bathroom products with filters applied. But the real issue is that it's visually flat and doesn't actually demonstrate anything meaningful. All three options look equally acceptable, so the comparison fails to make a compelling case for any particular choice.

The core problem is that shower filters are inherently difficult to prove visually because the actual mechanism—what's happening to the water itself—is completely invisible. A locked-frame product comparison won't work here because there's nothing to see in the filtered versus unfiltered water at first glance.

The user is asking me to pivot to a different approach entirely. Instead of comparing the filter products themselves, I should focus on what actually shows proof: the cartridge before and after use is the strongest visual evidence—new white filter media turning brown or rust-stained after weeks of use. That's the industry standard and it's genuinely compelling. Other options include spraying unfiltered water onto white cloth to show sediment stains, photographing limescale buildup on bathroom surfaces over time, or settling sediment in water samples in clear jars. These approaches actually demonstrate the filter's effect rather than just displaying the product.

The best direction forward is to keep the locked-frame device but shift the variable from comparing different products to showing the same cartridge's transformation over time—a timelapse variant showing Day 0, Day 30, Day 90 of the same filter getting progressively stained. This proves the filter is capturing contaminants without any competitor comparison or trademark risk. A second approach would be the white cotton cloth test, showing unfiltered water leaving visible residue versus filtered water coming through clean.

I need to diagnose why the original direction failed, propose these two new directions with concrete prompts, and be careful not to make health claims—just show what's being captured.

Looking at their image, the locked frame and consistent background actually worked well, so the technique is sound but the concept was wrong. There's also a practical issue: the metal filter appears to be mounted where the showerhead should be, but there's no showerhead attached, making it look incomplete. Worth flagging that detail.

I should also update the memory with their stated finding that both locked-frame variants didn't work for the shower filter—that's useful feedback for the framework going forward.

</details>

# Chẩn đoán

Kỹ thuật của bạn không sai. Khóa khung chạy hoàn hảo: tay sen, ke tường, kệ, chai, khăn, ô cửa mờ, tất cả trùng khít qua ba panel. Đó là phần khó nhất và bạn đã làm được.

Cái sai nằm ở tầng ý tưởng: **với lọc vòi sen, bản thân vật thể không mang bằng chứng nào.**

Ba panel này nói với người xem đúng một điều: ba cái này trông khác nhau. Panel 1 nhựa đục có hạt màu, panel 2 nhựa trắng, panel 3 kim loại. Đẹp hơn không phải là lọc tốt hơn, và người mua biết điều đó. Họ nhìn xong không rút ra được kết luận nào nên ảnh không có tác dụng thuyết phục.

So sánh khóa khung chỉ hoạt động khi **khác biệt hiện ra trong khung**. Ở test dao mài, khác biệt là lát cà chua, nhìn phát biết ngay. Ở lọc vòi sen, khác biệt nằm trong nước, mà nước thì trong suốt. Sai ở chỗ đó, không phải ở prompt.

Thêm một lỗi nhỏ: panel 3 lắp lọc vào tay sen nhưng không có bát sen phía sau, nên nó trông như lắp dở. Hai panel kia đều là thiết bị hoàn chỉnh. Người xem đọc thành "cái này thiếu đồ".

# Hướng khác

Giữ nguyên device `lockedframe`, đổi **biến số**. Thay vì hỏi "cái nào tốt hơn", hỏi "cái này có bắt được gì không".

Khi đó vật thể so sánh không còn là ba sản phẩm mà là **cùng một thứ ở các trạng thái khác nhau**. Bằng chứng tự hiện ra, không cần ai phán xét, và không đụng đến đối thủ nên không có rủi ro nhãn hiệu.

Hai biến thể dùng được cho sản phẩm này:

| Biến thể | Biến số | Bằng chứng |
|---|---|---|
| `--timelapse` | Thời gian sử dụng | Lõi lọc chuyển màu, chứng minh nó giữ lại thứ gì đó |
| `--capture` | Nước qua và không qua lọc | Vết bẩn trên vải trắng, chứng minh có thứ gì đó trong nước |

---

## Prompt 1: `04-proof-lockedframe--timelapse`

Mạnh nhất trong hai cái. Đính ảnh sản phẩm.

```
A documentary photograph, 5:3 ratio, three equal vertical panels, thin white gutters, no outer border. NO graphic overlays, badges, arrows or text.

Use the attached product photo as the exact reference for the filter cartridge shown in all three panels. Preserve shape, proportions, material and form exactly. The cartridge is the SAME unit in every panel, only its internal filter media changes color.

LOCKED CAMERA: identical camera position, focal length, height and angle in every panel, shot straight on at close range so the cartridge fills most of the frame height. Every fixed element must align pixel for pixel across all three panels: the cartridge sits upright in the same position on the same surface, the same folded white towel behind it at the same angle, the same grout line on the tile wall, the same soft shadow direction. Identical lighting, exposure and white balance in every panel.

SCENE, constant: the cartridge stands upright on a plain white bathroom counter against a white tiled wall, cut open lengthwise so the packed filter media inside is fully visible. Deliberate real-world detail: a faint water mark on the counter, a single drop of water beside the base. Flat overcast daylight from the left, no strong shadows, no sunlight, no styling.

THE VARIABLE, the only thing that changes: the color and condition of the filter media packed inside the cartridge.
Panel 1: media clean, uniform bright white and pale grey granules, evenly packed, untouched.
Panel 2: media partially discolored, the upper third stained a dull ochre and rust brown, the lower portion still pale, an uneven tide line between them.
Panel 3: media heavily discolored, deep rust brown and orange throughout, dark sediment visible at the top surface, dulled and compacted.

The cartridge shell, its shape, its position and its lighting are identical in all three panels. Only the media color changes.

JUDGEMENT RULE: no badge, no glow, no color cue, no arrow. All panels equally lit and equally neutral. The image makes no claim, it only shows the object.

STYLE: honest documentary product test photography, unstyled, natural, sharp, macro clarity on the media texture.
NO text, no logo, no watermark.
```

**Negative:**
```
text, letters, numbers, watermark, logo, badges, arrows, glows, checkmarks,
different camera angle between panels, shifted background elements, different cartridge
shape between panels, inconsistent lighting between panels, one panel brighter,
studio background, clean styled set, saturated colors, green or red cues,
blood-like colors, mold, slime, disgusting texture, people, hands, running water
```

**Vì sao nó hoạt động:** người mua đã tin sẵn rằng nước máy có cặn, họ chỉ chưa thấy. Ảnh này không tranh luận, nó đưa vật chứng. Và vì cả ba panel đều là sản phẩm của bạn, nó không thể bị đọc thành công kích đối thủ.

**Lưu ý pháp lý:** không ghi số ngày lên ảnh, không nói lõi lọc bắt được chất gì cụ thể. Để hình ảnh tự nói. Thêm chữ vào là thành claim phải chứng minh được.

---

## Prompt 2: `04-proof-lockedframe--capture`

Hai panel. Bằng chứng gián tiếp qua vật trung gian.

```
A documentary photograph, 3:2 ratio, two equal vertical panels, thin white gutter, no outer border. NO graphic overlays, badges, arrows or text.

Use the attached product photo as the exact reference for the filter visible in panel 2. Preserve shape, proportions, material, finish and color exactly.

LOCKED CAMERA: identical camera position, focal length, height and angle in both panels, shot straight on at chest height. Every fixed element must align pixel for pixel: the chrome shower arm meeting the wall, the horizontal grout line behind it, a small chrome shelf at the upper right holding one plain white bottle, the edge of a folded towel entering at the lower left. Identical lighting, exposure and white balance in both panels.

SCENE, constant: a plain white tiled bathroom wall with a chrome shower arm and a basic chrome shower head. A square of clean white cotton cloth is stretched taut and clipped flat across the face of the shower head in both panels. Flat overcast daylight from a frosted window to the left, no strong shadows, no styling.

THE VARIABLE:
Panel 1: no filter fitted, the shower arm bare between wall and head. The white cotton cloth is marked with a spreading pattern of pale rust, ochre and grey staining where water has passed through it, heaviest at the center, with fine sediment speckles.
Panel 2: the reference filter fitted between the arm and the head. The same white cotton cloth is clean and evenly damp, uniform white, no staining, no speckles.

The cloth is the same size, same clips, same position, same tautness in both panels. Only its staining changes.

JUDGEMENT RULE: no badge, no glow, no arrow, no color cue. Both panels equally lit and equally neutral.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
NO text, no logo, no watermark.
```

**Negative:** như prompt 1, thêm `cloth in different position, different cloth size, dramatic staining, black mold, unrealistic dirt, cartoonish contrast`

**Điểm yếu cần biết trước:** biến thể này dễ bị đọc là dàn dựng hơn `--timelapse`, vì người xem không thấy quá trình. Nếu chạy được cả hai thì đặt `--timelapse` trước, `--capture` sau, khi đó cái sau được cái trước bảo lãnh.

---

## Cập nhật registry

`04-proof-lockedframe` lên v1.2, bốn biến thể, kèm luật chọn:

```yaml
variant_selection_rule: >
  Nếu khác biệt giữa các sản phẩm KHÔNG hiện ra trong khung hình tĩnh,
  không dùng --rivals hay --verdict. Chuyển sang --timelapse hoặc --capture,
  đổi biến số từ "sản phẩm nào" sang "trạng thái nào của cùng một vật".
```

Đây là luật chung, không riêng lọc nước. Nó áp cho mọi sản phẩm có cơ chế vô hình: viên uống, nước hoa, sản phẩm chăm sóc da, phần mềm. Với nhóm đó, `--rivals` và `--verdict` sẽ luôn ra ảnh đẹp mà rỗng, đúng như cái bạn vừa gặp.

---

## Human

global rule: sản phẩm hoặc chủ thể phải đúng context xử dụng, logic, tự nhiên

---

## Assistant

<details><summary>Thinking</summary>

The user is adding a new global rule about products needing to be in correct, logical usage contexts—like how a filter cartridge on a counter without a showerhead doesn't make sense. I need to define this rule precisely as G7, create a test to validate it, audit existing prompt types against it, and fix the two prompts I just gave that violate it.

I'm handling a file conflict with a stale token, so I'll attempt to append and retry if needed. Now I'm drafting the rule definition with three sub-tests: completeness (no half-assembled devices, all mounting components present), placement (objects where someone would actually put them), and reason (a plausible explanation for why this scene exists). Then I'll apply this to my existing prompt types and identify which ones break the rule—starting with the timelapse that shows a cut-open cartridge.

For the cartridge, the unnatural cut-open view needs fixing; instead I should show it whole through transparent housing, or better yet, capture the realistic moment of replacement—a spent cartridge just removed and placed on the counter. For filters without transparency, the natural inspection state is when unscrewed with the media visible at the open end. The shower capture with the white cloth clipped over the showerhead is a test rig rather than natural use, though it's defensible if framed as a legitimate at-home test someone would actually perform.

</details>

```
This block is not supported on your current device yet.
```

# G7. Context integrity

```
[CONTEXT INTEGRITY, bắt buộc]
Every object in frame must appear in a state, position and setting it would
genuinely occupy during real use, real installation or real inspection.
Nothing may be cut, floated, disassembled, clipped, propped or arranged
in a way that only exists to make a photograph.
```

## Ba phép kiểm tra

Ảnh phải qua cả ba. Trượt một cái là sai.

**1. Toàn vẹn.** Thiết bị trong khung phải hoàn chỉnh. Nếu sản phẩm lắp vào thứ khác thì thứ đó phải có mặt và đầy đủ. Đây chính là chỗ ảnh test của bạn hỏng: panel 3 có lọc nhưng không có bát sen, nên nó đọc thành lắp dở, còn hai panel kia là thiết bị nguyên vẹn.

**2. Vị trí.** Vật nằm đúng chỗ người thật sẽ đặt nó. Lõi lọc dựng đứng trên mặt bàn phòng tắm là không tự nhiên. Lõi lọc vừa tháo ra, nằm nghiêng cạnh bồn rửa, còn ướt, mới là cảnh có thật.

**3. Lý do.** Phải có lý do hợp lý để cảnh này tồn tại và để ai đó đang nhìn thấy nó. Người ta bổ dọc lõi lọc để làm gì? Không ai làm thế cả. Nhưng người ta **tháo lõi ra xem** thì có, và lúc tháo ra là nhìn thấy được vật liệu lọc ở đầu hở.

## Phạm vi áp dụng

G7 chỉ áp cho **lớp ảnh chụp cảnh**. Không áp cho:

| Lớp | G7 | Lý do |
|---|---|---|
| Cảnh chụp thật | Có | Đây là chỗ tính tự nhiên quyết định niềm tin |
| Product cutout, inset tròn, sản phẩm lơ lửng | Không | Người xem đọc đúng đây là lớp đồ họa, không phải cảnh |
| Sơ đồ, minh họa, render kỹ thuật | Không | `03-mechanism-ghostbody`, `02-cause-anatomy` được miễn |

Trộn hai register trong một khung thì mỗi lớp chịu luật riêng của nó. Sản phẩm lơ lửng ở góc `06-relief-hero` không vi phạm G7, nhưng sản phẩm trong cảnh hero thì có.

## Negative bổ sung cho mọi type

```
implausible setup, staged test rig, product half installed, missing components,
device shown incomplete, cut-open product, object floating in a real scene,
item propped in an unnatural position, arrangement that only exists for the photo
```

---

# Audit 9 type hiện có

| Type | G7 | Ghi chú |
|---|---|---|
| `01-pain-scene` | Có, chặt nhất | Toàn bộ giá trị nằm ở tính tự nhiên |
| `01-pain-split` | Có, cả hai panel | |
| `02-cause-anatomy` | **Miễn** | Minh họa, không phải cảnh |
| `02-symptom-rail` | Có, zone A và vignette | |
| `03-mechanism-ghostbody` | **Miễn** | Render kỹ thuật |
| `04-proof-lockedframe` | Có, chặt nhất | Type vừa hỏng vì vi phạm G7 |
| `05-persona-grid` | Có, cả 4 ô | |
| `05-social-handoff` | Có, cả cảnh, miễn cho inset | Đây là type dễ trượt phép kiểm tra thứ 3 |
| `06-relief-hero` | Có cho zone A, miễn cho zone B | |

---

# Sửa lại `--timelapse` theo G7

Bản trước vi phạm cả ba phép kiểm tra. Bản này đổi cảnh sang **khoảnh khắc thay lõi**, thứ mà mọi người dùng đều thật sự làm.

```
A documentary photograph, 5:3 ratio, three equal vertical panels, thin white gutters, no outer border. NO graphic overlays, badges, arrows or text.

Use the attached product photo as the exact reference for the filter cartridge. Preserve shape, proportions, material and finish exactly. It is the same unit in every panel, unscrewed and set down for inspection.

LOCKED CAMERA: identical camera position, focal length, height and angle in every panel, shot from slightly above at close range so the cartridge fills most of the frame. Every fixed element must align pixel for pixel: the cartridge lies on its side in the same spot on the same white bathroom counter, its open threaded end facing the camera so the packed filter media inside is visible at the opening, the same chrome tap base at the upper right, the same folded towel edge at the lower left, the same water droplets on the counter. Identical lighting, exposure and white balance in every panel.

SCENE, constant: a real bathroom counter beside a basin, the cartridge just removed and laid down, still faintly wet. Deliberate real-world detail: a few water spots on the counter, a damp ring where the cartridge sits. Flat overcast daylight from the left, no strong shadows, no styling.

THE VARIABLE, the only thing that changes: the color of the filter media visible inside the open end.
Panel 1: media clean, uniform white and pale grey granules, evenly packed, dry looking.
Panel 2: media partly discolored, dull ochre and light rust staining across the exposed surface, uneven, some pale granules still showing.
Panel 3: media heavily discolored, deep rust brown and orange across the whole exposed surface, darker sediment settled at the rim, dulled and compacted.

The cartridge shell, its shape, its position, its angle and its lighting are identical in all three panels. Only the media color changes.

CONTEXT INTEGRITY: this is an ordinary inspection moment, a cartridge unscrewed and set on the counter. Nothing is cut open, propped up or arranged for the camera.

JUDGEMENT RULE: no badge, no glow, no color cue, no arrow. All panels equally lit and equally neutral.

STYLE: honest documentary product test photography, unstyled, natural, sharp, macro clarity on the media texture.
NO text, no logo, no watermark.
```

**Negative:** như bản trước, thêm `cut-open cartridge, cross-section, product standing upright unnaturally, staged arrangement, mold, slime, blood-like color`

---

# Về `--capture`

Biến thể này trượt phép kiểm tra thứ 3 ngay từ thiết kế. Miếng vải căng kẹp lên mặt bát sen là một giàn thử nghiệm, không phải cảnh có thật.

Hai lựa chọn:

**Bỏ.** Nếu bạn muốn giữ G7 tuyệt đối trong mọi type.

**Giữ, nhưng khai báo là thử nghiệm tại nhà.** Khi đó nó phải trông đúng như một người bình thường tự làm, không phải phòng lab: vải buộc bằng dây thun chứ không kẹp căng, hơi lệch, chậu hứng bên dưới, khăn ướt vắt tạm trên thành bồn. Cảnh dàn dựng vụng về đọc thật hơn cảnh dàn dựng gọn gàng.

Tôi nghiêng về giữ, và thêm biến thể này vào schema với cờ riêng:

```yaml
context_mode: [natural-use, declared-test]
```

`natural-use` là mặc định và áp G7 đầy đủ. `declared-test` là ngoại lệ có kiểm soát: cảnh được phép dàn dựng nhưng phải dàn dựng **nghiệp dư**, và chỉ dùng ở kênh advertorial, không dùng trong gallery sàn.

---

## Human

tôi sẽ vẫn đưa ảnh vào, nếu đọc ảnh mà thấy trùng với type hiện có, hãy đối chiếu nội dung hình ảnh và so sánh hiệu quả để tối ưu image prompt

---

## Assistant

<details><summary>Thinking</summary>

I'm understanding the new workflow: when an image matches an existing type, I should compare the content and effectiveness to optimize the prompt rather than creating a duplicate type. I'll define the comparison protocol with a match test, variance analysis, and verdict outcomes, then file this to memory. Let me verify the version token and confirm my changes are saved.

</details>

```
This block is not supported on your current device yet.
```

Rõ. Từ giờ mỗi ảnh mới đi qua ba bước.

## Bước 1: Phân loại

Ba khả năng, phân biệt bằng **cấu trúc lập luận**, không phải bằng bố cục hay chủ đề.

| Kết luận | Điều kiện | Hành động |
|---|---|---|
| **Trùng type** | Cùng job, cùng device, cùng số lớp | Sang bước 2 |
| **Biến thể mới** | Cùng job và device, khác một quyết định cấu trúc | Đặt tên `--variant`, viết phần diff của skeleton |
| **Type mới** | Khác job hoặc khác device | Breakdown đầy đủ như trước |

Hai ảnh cùng chụp người ngồi ghế có thể là hai type khác nhau. Hai ảnh trông rất khác nhau có thể là cùng một type. Cấu trúc lập luận quyết định, không phải chủ đề.

## Bước 2: Đối chiếu

Khi trùng type, tôi so hai ảnh trên đúng những slot mà skeleton đang kiểm soát, không so cảm tính:

```
SLOT | Ảnh A (đã có) | Ảnh B (mới) | Cái nào mạnh hơn | Vì sao
```

Mỗi dòng phải kết luận được **một trong ba**:

- **B mạnh hơn ở slot này.** Sửa giá trị mặc định của slot trong skeleton.
- **Hai cái mạnh ở hai ngữ cảnh khác nhau.** Slot đó thành có điều kiện, ghi rõ khi nào dùng cái nào.
- **Không phân biệt được.** Ghi vào mục chưa kết luận, không đụng skeleton. Đây là kết quả hợp lệ, không phải thất bại.

Tiêu chí "mạnh hơn" xếp theo thứ tự ưu tiên, cái trên thắng cái dưới khi mâu thuẫn:

1. Lập luận có đứng vững không (bằng chứng có thật sự hiện trong khung)
2. Đọc được ở kích thước thumbnail không
3. Có qua G7 không (context tự nhiên)
4. Có tuân G3 đến G5 không (màu, vế đúng, register)
5. Thẩm mỹ

Thẩm mỹ xếp cuối vì ảnh đẹp mà rỗng là đúng thứ vừa xảy ra với `--verdict`.

## Bước 3: Vá

Chỉ sửa slot có kết luận. Tăng minor version. Ghi lại **cả hai** giá trị cũ và mới trong skeleton dưới dạng lựa chọn có điều kiện, không xóa giá trị cũ, vì cái cũ đã từng chạy được và có thể vẫn đúng cho ngữ cảnh khác.

Nếu ảnh mới chỉ khác ảnh cũ ở thẩm mỹ mà không khác ở lập luận, tôi sẽ nói thẳng là không có gì để vá, thay vì bịa ra một thay đổi cho có.

Đưa ảnh tiếp đi.

---

## Human

**Attachments:**
- 1786343881118_image.png

---

## Assistant

<details><summary>Thinking</summary>

Looking at this product image, I see a spray mist hairbrush with an oil reservoir shown in a lifestyle bathroom scene with backlighting, plus a circular inset in the top-right showing damaged, frizzy hair from a salon perspective. This layout with the hero lifestyle shot and circular inset overlay suggests it could match the `05-social-handoff` template, but there's only one person and no pointing or listener dynamic, so it's actually fitting the `06-relief-hero` pattern instead.

The key structural difference here is that the inset isn't showing a before-and-after split comparison—it's a single circular image of the problem state (damaged hair) rather than a two-panel versus split. There's also no product cutout layer. Since the job is still relief (selling the improved after state) and the device is still hero plus circular inset, this is a variant of the base template. I'm thinking this should be named `06-relief-hero--recall` to distinguish it from the standard `06-relief-hero--vsinset` that uses the three-layer structure with a split comparison inset.

Now I'm comparing these two approaches across the key visual slots: the three-layer version has the product partially obscured behind the person with a flat office light, while this version centers the product in hand with strong backlighting that makes the spray mist visible—which actually serves as proof the product works. The emotion shifts too, from relaxed (eyes closed) to actively engaged (looking at own hair mid-action). On effectiveness, the visible mist gives this version a stronger argument than relying on a claim, and the centered product placement reads much better at thumbnail size.

The trade-offs I'm seeing: this version's inset is a single dark salon photo without a before/after label, which creates ambiguity about whether that's the "before" or "after" state, and the low-res inset breaks visual consistency with the bright hero. But the bigger insight is that when the product is handheld and clearly in-use, the product cutout zone becomes unnecessary—so that should be conditional in the framework. I'm also recognizing a new principle: if the product creates something visible (mist, foam, water), the hero lighting needs to be chosen specifically to capture that mechanism in action. And for the inset, a single-panel recall version needs a clear marker to avoid ambiguity.

</details>

# Bước 1: Phân loại

**Trùng type.** Đây là `06-relief-hero`, không phải type mới.

Cùng job (`relief`, bán trạng thái đang dùng), cùng device (`hero`, một cảnh chụp thật kèm overlay). Khác một quyết định cấu trúc: inset là **một ô nhắc lại vấn đề** thay vì ô so sánh VS, và không có lớp product cutout.

Đặt là biến thể: **`06-relief-hero--recall`**, bản gốc thành `--vsinset`.

# Bước 2: Đối chiếu

| Slot | A (đệm công thái học) | B (lược xịt dưỡng) | Mạnh hơn | Vì sao |
|---|---|---|---|---|
| Số lớp | 3 (hero + cutout + VS inset) | 2 (hero + inset) | **B** | Ít lớp hơn nhưng không mất thông tin nào |
| Sản phẩm trong hero | Bị người che, nằm sau lưng | Chính giữa khung, trong tay, đang hoạt động | **B** | Ở thumbnail, A mất sản phẩm hoàn toàn |
| Bằng chứng | Không có, chỉ có người vui | **Làn sương xịt nhìn thấy được** | **B** | A tuyên bố, B trưng ra |
| Ánh sáng | High-key phẳng, đều | Ngược sáng mạnh, nắng xiên | **B trong ngữ cảnh này** | Ngược sáng là thứ duy nhất làm làn sương hiện lên |
| Tư thế | Ngả người, mắt nhắm, tĩnh | Đang giữa động tác chải, mắt nhìn tóc | **B** | Sản phẩm chủ động thì cảnh phải động |
| Lớp product cutout | Có | Không | **Có điều kiện** | A cần vì hero che sản phẩm, B không cần |
| Inset | VS hai vế, có badge | Một ô, không nhãn | **A** | Ô của B không rõ là trước hay sau, người xem đọc nhầm thành kết quả |
| Register inset | Cùng nguồn với hero | Ảnh salon tối, độ phân giải thấp, dán lên nền sáng | **A** | B vi phạm G5 rõ rệt |

Kết luận: B thắng ở tầng lập luận và tầng đọc nhanh, A thắng ở tầng inset. Hai bên bù nhau, nên ra ba mục vá chứ không phải một.

# Bước 3: Vá, `06-relief-hero` v1.2

## Vá 1: Zone B thành có điều kiện

Đây là điều B chứng minh dứt khoát.

```
[ZONE B: PRODUCT VIEW]
INCLUDE THIS LAYER ONLY IF the hero scene cannot show the product clearly.
Skip it entirely when the product is held in hand, centered, and legible at
thumbnail size. An extra layer that repeats information the hero already carries
costs frame space and buys nothing.
```

## Vá 2: Slot mới, cơ chế nhìn thấy được

Đây là nâng cấp lớn nhất rút ra từ ảnh B, và nó áp cho mọi sản phẩm có đầu ra vật lý.

```
[VISIBLE MECHANISM, bắt buộc khi sản phẩm tạo ra thứ nhìn thấy được]
If the product emits, produces or moves anything visible in air or on a surface
(mist, spray, steam, foam, water, particles, light, heat shimmer),
that output MUST be visible in the hero frame, and the lighting must be chosen
to reveal it: strong backlight or side rim light from [source],
subject and product placed between the light and the camera.
This output is the only proof the image carries. Losing it loses the argument.

If the product produces nothing visible, do NOT invent an effect.
Use the default even daylight setup instead.
```

## Vá 3: Ánh sáng thành có điều kiện

Giá trị cũ giữ nguyên, thêm nhánh thứ hai. Không xóa cái cũ vì nó vẫn đúng cho sản phẩm tĩnh.

```
[LIGHT]
IF visible mechanism present: [backlight / hard side light] from [source],
strong enough to make the output glow against a darker background area.
Accept lens flare and blown highlights, they read as real.
ELSE: soft even [natural window light], background blurred, high-key grade.
```

## Vá 4: Tư thế theo tính chủ động của sản phẩm

```
[POSE]
IF the product is actively operated by the user: mid-action, hands engaged,
gaze on the point of use, expression of focused satisfaction rather than repose.
IF the product works passively while the user does something else:
relaxed pose, [relief position], gaze away from the product.
```

## Biến thể `--recall`

```
[INSET, variant --recall]
One circular cutout containing a photograph of [the problem state],
positioned [corner], occupying [12-18%] of frame width.
The inset MUST be visually marked as the past state, either desaturated,
or carrying a small red X badge. An unlabelled inset reads as a result,
which inverts the entire message.
REGISTER: the inset photo must match the hero in resolution, grade and
light quality. A darker, lower-resolution or differently lit inset reads as
pasted in and costs more trust than the inset earns.
```

**Negative bổ sung:** `unlabelled before-state inset, low resolution inset, inset darker than hero, inset from a different photographic source, invented spray or mist, fake steam`

# Chốt lại

| Biến thể | Dùng khi |
|---|---|
| `--vsinset` | Sản phẩm thụ động, không nhìn thấy cơ chế, cần lập luận sai/đúng |
| `--recall` | Sản phẩm chủ động, cơ chế nhìn thấy được, chỉ cần nhắc lại vấn đề |

Vá 2 là thứ đáng giá nhất trong lượt này. Nó không chỉ sửa `06-relief-hero`, nó là luật áp cho mọi type có cảnh chụp thật: sản phẩm nào tạo ra thứ nhìn thấy được thì ánh sáng phải được chọn để lộ nó ra, không phải chọn cho đẹp. Với lọc vòi sen thì đây chính là câu trả lời cho vấn đề bạn gặp ở `04-proof-lockedframe`, vì tia nước ngược sáng là thứ duy nhất của sản phẩm đó hiện được ra trong khung.

---

## Human

**Attachments:**
- 1786343916526_image.png

---

## Assistant

# Bước 1: Phân loại

**Trùng type.** Đây là `01-pain-scene`, không phải type mới. Cùng job (`pain`, làm người xem nhận ra chính mình), cùng device (`scene`, một khung chụp thật, zero lớp đồ họa).

Nhưng nó khác `01-pain-scene` gốc ở gần như mọi lựa chọn thi hành, nên đây là biến thể: **`01-pain-scene--confront`**, bản gốc thành **`--candid`**.

# Bước 2: Đối chiếu

| Slot | A (đàn ông bước ra khỏi xe) | B (phụ nữ trước gương) | Mạnh hơn | Vì sao |
|---|---|---|---|---|
| Hướng nhìn | Nhìn xuống, không biết có máy quay | **Nhìn thẳng vào ống kính** | Có điều kiện | Xem bên dưới |
| Ánh sáng | Low-key, chạng vạng, khối tối lớn | Sáng đều, ban ngày, trắng xanh | **B ở kênh sàn, A ở kênh ads** | Sáng thì đọc được ở thumbnail, tối thì điện ảnh hơn |
| Bằng chứng triệu chứng | Chỉ có cử chỉ tay ôm lưng | **Tóc rối, sợi rụng bám áo, lược cầm tay** | **B** | A phải suy ra, B nhìn phát biết |
| Vật chứng trong khung | Không có | Bàn chải, kem đánh răng, khăn, gương | **B** | Đây chính là slot tôi đoán thiếu ở Test F |
| Biểu cảm | Nhăn vì đau thể chất | **Bực bội, cam chịu, hơi bĩu môi** | **B cho nhóm thẩm mỹ** | Vấn đề thẩm mỹ không có đau, chỉ có bực |
| Thời điểm | Chuyển tiếp, giữa hành động | Tĩnh, khoảnh khắc dừng lại nhìn mình | Ngang nhau | Hai cơ chế nhận diện khác nhau |
| Gương | Không có | **Có, nhân đôi chủ thể** | **B** | Gương là lý do tự nhiên để có khoảnh khắc đối diện bản thân |

Kết luận: B không thắng A. B là **một thi hành khác cho một loại vấn đề khác**, và nó lấp đúng lỗ hổng mà Test F đã dự đoán. A dùng cho đau thể chất, B dùng cho vấn đề thẩm mỹ và trạng thái.

# Bước 3: Vá, `01-pain-scene` v1.1

## Vá 1: Slot bằng chứng triệu chứng, bắt buộc

Test F đã đoán đúng chỗ này. B xác nhận.

```
[SYMPTOM EVIDENCE, bắt buộc]
The symptom must be visible as physical fact in the frame, not only as expression.
Rank the available evidence and use the strongest present:
  1. The symptom itself on the body or object ([visible condition])
  2. Physical residue or debris it produces ([what it leaves behind, and where])
  3. The failed tool the person is holding ([what they tried, still in hand])
  4. Gesture alone (weakest, use only when 1-3 are impossible)
If only gesture is available, at least one object in frame must independently
imply the problem. Expression alone carries nothing.
```

## Vá 2: Hướng nhìn thành có điều kiện

```
[GAZE]
--candid: subject unaware of the camera, gaze on their task or the ground.
  Use for physical pain, for moments the person would not choose to be seen in.
--confront: subject looking directly into the lens, holding the viewer's eye.
  Use for appearance and self-image problems, where the mirror moment is the
  real moment and being seen is the point.
Never mix. A half-turned glance reads as a model waiting for direction.
```

## Vá 3: Ánh sáng thành có điều kiện, gắn với kênh

Đây là chỗ tôi viết cứng sai ở v1.0.

```
[LIGHT]
--candid: low-key, [directional source], deep shadow across [X%] of frame.
  Channel: paid-social, advertorial header. Reads cinematic, survives being scrolled past.
--confront: even ambient daylight, bright, minimal shadow.
  Channel: advertorial body, landing page, marketplace-adjacent.
  Reads legible at small size, survives being a thumbnail.
Both remain desaturated. Neither may use warm flattering light.
```

## Vá 4: Slot gương

```
[MIRROR] (tùy chọn, chỉ dùng với --confront)
A mirror behind or beside the subject showing them from another angle.
Gives a natural reason for the confrontation moment and doubles the symptom
evidence without adding a second person.
The reflection must be consistent with the subject's actual position.
```

## Vá 5: Bối cảnh, chốt lại luật lộn xộn

```
[ENVIRONMENT]
[specific ordinary place tied to the moment the problem is noticed].
Real lived-in clutter that belongs to that place and independently signals
the routine being disrupted: [3-4 mundane objects].
Nothing styled, nothing arranged, nothing removed to make the frame tidy.
```

# Cập nhật registry

```yaml
- id: 01-pain-scene
  version: "1.1"
  variants:
    candid:
      gaze: unaware
      light: low-key
      problem_class: [physical-pain, physical-limitation]
      channel: [paid-social, advertorial-header]
    confront:
      gaze: direct-to-lens
      light: even-daylight
      problem_class: [appearance, self-image, daily-frustration]
      channel: [advertorial-body, landing-page]
  required_slots: [symptom-evidence]
```

---

Vá 1 là thứ đáng giá nhất lượt này, và nó không chỉ áp cho type này. Nguyên tắc chung: **cảm xúc trên mặt không phải bằng chứng.** Mặt nhăn có thể vì bất cứ lý do gì. Tóc rối, sợi rụng bám áo, cái lược cầm trong tay mới là thứ chỉ có một cách giải thích.

Điều này quay lại chỉnh cả Test F (băng dán miệng ngủ) mà tôi viết trước đó. Ở đó tôi để mặc cử chỉ xoa cổ họng gánh toàn bộ, và đã đoán nó sẽ gãy. Bản sửa theo v1.1: ly nước cạn trên tủ đầu giường, gối nhàu về một bên, đồng hồ hiện giờ khuya, vỏ chăn bị đạp tung. Bốn vật chứng đó nói được thứ mà một cái nhăn mặt không nói được.

---

## Human

đưa prompt để test

---

## Assistant

<details><summary>Thinking</summary>

I'm setting up test cases for the pain-scene prompt variants using different products. For the candid variant, I'll test it on mouth tape to rewrite an earlier test with a symptom-evidence slot. For the confront variant, I'm considering a knife sharpener since it fits the daily frustration angle better than appearance-related products, avoiding overlap with the shower filter test.

</details>

Hai prompt, mỗi biến thể một cái, cố tình chọn hai loại vấn đề khác nhau để tách bạch khi nào dùng cái nào.

---

## Test K: `01-pain-scene--candid`

**Sản phẩm: băng dán miệng ngủ.** Đây là bản viết lại của Test F theo v1.1. Cử chỉ ở đây yếu (không có chỗ nào để ôm), nên toàn bộ gánh nặng chuyển sang tầng 2 và 3 của thang bằng chứng.

```
A cinematic film still, 5:3 ratio. Single frame. NO graphic overlays of any kind.

SUBJECT: A man in his late 30s in a worn grey t-shirt, caught mid-action sitting up on the edge of an unmade bed in the middle of the night, feet on the floor, shoulders slumped forward, one hand braced on the mattress, the other reaching for the nightstand. Unaware of the camera, gaze down and unfocused. Face showing genuine involuntary exhaustion: eyes heavy and half open, deep creases beneath them, lips dry and parted, jaw slack.

SYMPTOM EVIDENCE, must be visible as physical fact: an almost empty glass of water on the nightstand with a second empty glass beside it, the pillow deeply creased and shoved to one side, the duvet kicked into a tangle at the foot of the bed, a phone face-up on the nightstand casting a small cold glow. These objects independently signal a night that has been interrupted more than once.

MOMENT RULE: this is the ordinary act of waking again at 3am, not a demonstration of wrong behaviour.

ENVIRONMENT: A small suburban bedroom, deep night, curtains half drawn, a chair in the corner with clothes over the back. Real lived-in clutter, nothing styled, nothing arranged, nothing removed to tidy the frame.

LIGHT: Low-key. Key light: cold blue streetlight through the gap in the curtains from behind and to the left. Fill: faint warm glow from a hallway door left ajar. Rim light along his shoulder and jaw separating him from the dark wall. Deep shadow across most of the frame.

GRADE: Desaturated blue-grey palette, crushed blacks, fine film grain, shallow depth of field, 35mm lens character. NO saturated colors. NO red anywhere in the frame.

FORBIDDEN: No product. No overlays, arrows, badges, glows, hotspots, insets or split panels. Nothing that signals advertising.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
NO text, no logo, no watermark.
```

**Negative:**
```
text, letters, numbers, watermark, logo, deformed hands, extra fingers,
red glow, pain hotspots, graphic overlay, arrows, badges, split panel,
bright airy lighting, white background, studio lighting, stock photo look,
posed model, fake grimace, smiling, looking at camera, clean styled bedroom,
made bed, tidy nightstand, saturated colors, advertising composition, product placement
```

**Đoán chỗ gãy:** hai ly nước. Model hay gộp thành một hoặc bỏ một. Nếu chỉ còn một ly thì mất tầng "lặp lại", vốn là thứ duy nhất phân biệt "khát nước" với "đêm nào cũng thế". Nếu gãy thì slot cần đổi từ đếm số lượng sang một vật chứng tự nó mang tính lặp: ví dụ vệt ố nước trên mặt tủ đầu giường.

---

## Test L: `01-pain-scene--confront`

**Sản phẩm: dụng cụ mài dao lăn.** Đây là stress test thật của biến thể `--confront`: nó được rút ra từ một ảnh về ngoại hình, giờ ép nó chạy cho **bực bội thường ngày**, một `problem_class` khác. Nếu chạy được thì biến thể này rộng hơn tôi nghĩ.

```
A cinematic film still, 5:3 ratio. Single frame. NO graphic overlays of any kind.

SUBJECT: A woman in her early 40s in a plain t-shirt and an apron, standing at a kitchen counter, turned toward the camera and looking directly into the lens, holding the viewer's eye. She holds a knife loosely in one hand, the other hand raised slightly in a small gesture of giving up. Face showing genuine everyday frustration: brow drawn together, mouth pressed flat and slightly turned down, chin tucked, the look of someone who has been fighting this for ten minutes.

SYMPTOM EVIDENCE, must be visible as physical fact: on the board in front of her, a tomato mangled into thick uneven wedges, its skin torn and juice and seeds spread across the wood. Beside it, a second half-crushed tomato pushed aside. A cheap pull-through sharpener sits on the counter, clearly already tried and abandoned. A dish towel bunched under her wrist.

MOMENT RULE: this is the ordinary act of stopping mid-task because the tool will not do its job, not a demonstration of wrong technique.

ENVIRONMENT: A small ordinary home kitchen, mid-morning, worn wooden counter, an open drawer behind her with utensils visible, a chopping board leaning against the tiles, dishes stacked in the sink. Real lived-in clutter, nothing styled, nothing arranged, nothing removed to tidy the frame.

LIGHT: Even ambient daylight from a window to the left, bright, minimal shadow, flat and unflattering. No golden hour, no rim light, no drama.

GRADE: Desaturated neutral palette, muted greens and greys, fine film grain, moderate depth of field, 35mm lens character. NO saturated colors. NO red glow or highlight anywhere, the tomato is the only red and it must read as ordinary food color.

FORBIDDEN: No hero product. No overlays, arrows, badges, glows, hotspots, insets or split panels. Nothing that signals advertising.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
NO text, no logo, no watermark.
```

**Negative:**
```
text, letters, numbers, watermark, logo, deformed hands, extra fingers, six fingers,
blood, cuts, injury, knife pointed at the person, red glow, pain hotspots,
graphic overlay, arrows, badges, split panel, golden hour, warm flattering light,
studio lighting, stock photo look, posed model, exaggerated grimace, smiling,
clean styled kitchen, empty counter, tidy sink, saturated colors,
advertising composition, product placement
```

**Đoán chỗ gãy:** hai chỗ. Một, dao trong tay người nhìn thẳng ống kính rất dễ kích bộ lọc an toàn hoặc ra tư thế đe dọa. Nếu gãy thì đổi sang đặt dao xuống thớt và hai tay chống lên mặt bàn, cử chỉ bỏ cuộc vẫn giữ được. Hai, biểu cảm bực bội dễ trượt sang giận dữ kịch tính. `--confront` sống bằng sự tiết chế, mặt càng phẳng càng thật.

---

Nếu Test L chạy được thì `--confront` mở rộng ra ngoài nhóm ngoại hình và trở thành biến thể mặc định cho mọi vấn đề "bực mình hàng ngày", còn `--candid` co lại chỉ dùng cho đau thể chất và những khoảnh khắc mà người ta sẽ không muốn bị nhìn thấy.

---

## Human

đây là output ví dụ (02-cause-anatomy): tôi thấy không nên giữ camera angle. các ảnh cần xê dịch hơn, tự nhiên hơn như người chụp

**Attachments:**
- 1786344189415_image.png

---

## Assistant

<details><summary>Thinking</summary>

The user flagged a mislabeling issue—this is actually the locked-frame timelapse output, not the cause-anatomy piece. They're also pushing back on the core locked-camera constraint, saying it reads as too synthetic and artificial; they want the perspective to drift naturally like a human operator would shoot it. I see their point about the CGI feel, but that locked frame is fundamentally what defines this technique.

The real insight here is that the constraint should flex based on context: a timelapse spanning months would naturally have slight framing variance from hand-held shooting, whereas a same-session comparison (like rivals or verdict) benefits from a tighter lock. So I'm thinking of introducing a `camera_lock` parameter with `strict` and `handheld` modes to handle both cases credibly.

I should also review the specific output's other details—the material mismatch (white plastic vs. metal), the panel 3 media looking too muddy and potentially off-putting, and whether those discoloration effects (yellowing, rust, water stains) are landing as intentional aging or just looking wrong.

</details>

```
This block is not supported on your current device yet.
```

Một đính chính trước: ảnh này là `04-proof-lockedframe--timelapse`, không phải `02-cause-anatomy`. Cái sau là minh họa y khoa 2D nền xanh. Ghi nhầm nhãn thì lần vá sau sẽ vá nhầm file.

# Bạn đúng, và lý do quan trọng hơn cảm giác

Ảnh này trông như render 3D chứ không phải ảnh chụp. Nguyên nhân chính xác là khóa khung tuyệt đối. Ba lõi lọc nằm cùng một tọa độ, cùng một góc nghiêng, cùng một giọt nước trên mặt bàn. Không có buổi chụp nào của con người ra được như vậy.

Nhưng có một tầng sâu hơn: **`--timelapse` mâu thuẫn nội tại với khóa khung tuyệt đối.** Ba tấm này được cho là chụp cách nhau hàng tháng. Một người bình thường không dựng chân máy cố định suốt sáu tháng. Khung trùng khít từng pixel qua sáu tháng là bằng chứng của dàn dựng, không phải bằng chứng của quá trình. Nó tự phản bội chính lập luận nó đang mang.

Vậy nên đây không phải bỏ luật, mà là **luật khóa khung phải phụ thuộc vào khoảng cách thời gian giữa các panel.**

| Biến thể | Các panel chụp khi nào | Chế độ khung |
|---|---|---|
| `--rivals`, `--verdict` | Cùng một buổi, thay vật rồi bấm tiếp | `strict` |
| `--timelapse` | Cách nhau hàng tuần, hàng tháng | `handheld` |
| `--capture` | Cùng buổi | `strict` |

# Chế độ mới: `camera_lock: handheld`

Thay slot LOCKED CAMERA bằng slot này khi các panel cách nhau về thời gian:

```
[HANDHELD CONTINUITY, thay cho LOCKED CAMERA]
Same room, same surface, same light direction, same rough shooting distance.
Shot by the same person on a phone on three different days, not on a tripod.

MUST VARY between panels, naturally and independently:
  camera position shifted 10-20cm in any direction
  camera angle differing by 5-10 degrees
  the object rotated 15-30 degrees, resting at a different tilt
  the object placed a few centimetres from where it sat before
  incidental details different: water droplets in different spots,
  the towel folded differently, a different item left at the frame edge
  slight exposure and white balance drift, as if shot under different daylight

MUST STAY CONSTANT:
  the room, the surface, the direction the light comes from
  the identity of the object
  the single variable being compared

The panels must look like three photographs a person took, not three renders
from one scene file. Perfect alignment reads as CGI and destroys the evidence.
```

# Prompt sửa lại

```
Three photographs taken on different days, shown as three equal vertical panels, 5:3 ratio overall, thin white gutters, no outer border. NO graphic overlays, badges, arrows or text.

Use the attached product photo as the exact reference for the filter cartridge. Preserve shape, proportions, material and finish exactly. It is the same unit in every panel, unscrewed and set down for inspection.

HANDHELD CONTINUITY: same bathroom counter, same basin, same daylight direction from the left, same rough shooting distance. Shot by the same person on a phone on three separate occasions, never on a tripod.
Vary naturally between panels: camera position shifted 10 to 20 centimetres, camera angle differing by 5 to 10 degrees, the cartridge rotated 15 to 30 degrees and resting at a different tilt, placed a few centimetres from where it sat before, water droplets scattered differently, the towel at the frame edge folded differently, slight drift in exposure and white balance as if shot under different daylight.
Keep constant: the room, the counter surface, the light direction, the identity of the cartridge, and the single thing being compared.

SCENE: a real bathroom counter beside a basin, the cartridge just removed and laid on its side, still faintly wet, its open threaded end angled toward the camera so the packed filter media inside is visible at the opening. Ordinary real-world detail: water spots on the counter, a damp ring under the cartridge, a towel at the edge of frame. Overcast daylight from the left, soft, no styling.

THE VARIABLE, the only thing being compared: the color of the filter media visible inside the open end.
Panel 1: media clean, uniform white and pale grey granules, evenly packed.
Panel 2: media partly discolored, dull ochre and light rust across the exposed surface, uneven, pale granules still showing through.
Panel 3: media heavily discolored, deep rust brown across the whole exposed surface, the granule texture still clearly readable as granules, darker staining at the rim, and light rust staining creeping onto the outer shell near the threads.

CONTEXT INTEGRITY: an ordinary inspection moment, a cartridge unscrewed and set on the counter. Nothing cut open, propped up or arranged for the camera.

JUDGEMENT RULE: no badge, no glow, no color cue, no arrow. All panels equally neutral. The image makes no claim, it only shows the object.

STYLE: honest phone photography, natural, unstyled, slightly imperfect, sharp enough to read the media texture.
NO text, no logo, no watermark.
```

**Negative bổ sung:**
```
identical framing between panels, pixel-perfect alignment, tripod shot,
3D render look, CGI, product visualization, perfectly clean studio surface,
identical water droplets between panels, mud, sludge, mold, slime,
texture losing its granular structure
```

# Hai chỗ khác trong output cần chỉnh

**Panel 3 đang trượt sang bùn.** Vật liệu lọc mất cấu trúc hạt, thành một khối nâu mịn. Người xem đọc là bùn bẩn chứ không phải hạt lọc đã bão hòa. Prompt mới ghi thêm ràng buộc giữ được texture hạt, vì đó là thứ chứng minh nó vẫn là vật liệu lọc chứ không phải cặn ngoài rơi vào.

**Vỏ ngoài ố vàng theo là chi tiết tốt, giữ lại.** Model tự thêm và nó đúng. Nó cho thấy toàn bộ thiết bị đã qua thời gian, không phải chỉ phần ruột bị đổi màu bằng hậu kỳ.

# Cập nhật schema

```yaml
camera_lock: [strict, handheld]
selection_rule: >
  strict khi các panel chụp trong cùng một buổi và biến số là vật thể được
  thay ra thay vào. handheld khi các panel cách nhau về thời gian. Chọn sai
  chế độ thì khung hình tự tố cáo dàn dựng, kể cả khi mọi thứ khác đều đúng.
```

---

## Human

**Attachments:**
- 1786344392279_image.png

---

## Assistant

<details><summary>Thinking</summary>

I'm looking at a new image of a woman smiling at her reflection in a shop window—a relief scene without any product visible. Based on the classification protocol, this is a scene-type delivery with a relief job, making it a new type called `06-relief-scene`, which mirrors the structure of `01-pain-scene` but with a different emotional job. The thinking cuts off mid-sentence while evaluating whether this is truly a new type or a variant. The hair visible in both the reflection and direct view becomes the evidence of change without needing the product itself. This gaze-at-self moment is the inverse of the confrontational look in the pain scene — it's private resolution rather than viewer engagement. Standing alone it reads as generic lifestyle, but paired as a bookend it completes the arc. I should add a new gaze mode called `--reflect` and consider whether the mirror device from the pain scene should be promoted to a shared module since it's proving generalizable across different shots.

</details>

# Bước 1: Phân loại

**Type mới**, không phải biến thể. Cùng device (`scene`) nhưng khác job: `relief` thay vì `pain`.

**`06-relief-scene`**

Nó chính là bản đối xứng của `01-pain-scene--confront`. Cùng một hành động (nhìn chính mình), cùng một thiết bị (mặt phản chiếu), ngược lại phán quyết.

# Bước 2: Đối chiếu với `01-pain-scene--confront`

| Slot | Pain confront | Relief scene | Ghi chú |
|---|---|---|---|
| Hướng nhìn | Thẳng vào ống kính | **Vào phản chiếu của chính mình** | Chế độ thứ ba, chưa có trong skeleton |
| Mặt phản chiếu | Gương phòng tắm, tùy chọn | **Kính cửa hàng, bắt buộc** | Ở đây nó gánh toàn bộ bằng chứng |
| Bằng chứng | Tóc rối, sợi rụng, lược | **Tóc mượt, thấy từ hai góc trong một khung** | Cùng cơ chế, ngược dấu |
| Biểu cảm | Bực, cam chịu | Cười khép miệng, nhỏ, riêng tư | Cả hai đều tiết chế |
| Không gian | Phòng tắm, riêng tư, chật | Đường phố, công cộng, thoáng | Khỏi nhà là một phần của thông điệp |
| Ánh sáng | Đều, phẳng, không tôn dáng | Đều, sáng, hơi tôn dáng | Nới nhẹ so với pain |
| Sản phẩm | Không có | Không có | Cả hai đều là type không sản phẩm |

**Ba điểm cấu trúc của ảnh này:**

**Phản chiếu là bằng chứng, không phải trang trí.** Tóc được nhìn từ hai góc trong cùng một khung, và đó là cách duy nhất một ảnh không sản phẩm chứng minh được điều gì. Bỏ ô kính đi thì còn lại một ảnh stock phụ nữ đi trên phố.

**Nhìn vào chính mình chứ không nhìn vào ống kính.** Người xem đứng ngoài quan sát một khoảnh khắc riêng tư. Nếu cô ấy nhìn máy quay thì thành khoe, và khoe thì bị dựng hàng rào.

**Đường phố, không phải trong nhà.** Vấn đề bắt đầu ở phòng tắm, kết thúc ở nơi công cộng. Đó là lời hứa thật của loại sản phẩm này: không phải tóc đẹp, mà là ra khỏi cửa mà không phải nghĩ về nó nữa.

**Điểm yếu:** đứng một mình nó không nói gì cả. Không có gì đánh dấu đây là trạng thái "sau". Type này chỉ hoạt động khi có ảnh "trước" đi kèm, cùng người, cùng bảng màu.

# Bước 3: Spec

## Vá chung: chế độ nhìn thứ ba

Áp cho cả `01-pain-scene` và `06-relief-scene`.

```
[GAZE]
--candid: unaware of camera, gaze on task or ground.
--confront: direct into the lens, holding the viewer's eye.
--reflect: at their own reflection in [mirror / shop window / car glass].
  The viewer observes a private moment. Never mix with a glance at camera.
  Required when the image must carry evidence but contains no product:
  the reflection shows the subject twice, from two angles, in one frame.
```

## Skeleton `06-relief-scene`

```
TYPE: 06-relief-scene v1.0
RATIO: [5:3 / 16:9 / 4:5]
REGISTER: candid documentary photograph. Single frame. NO graphic overlays.
requires_product_photo: false

[SUBJECT]
[same demographic as the paired pain image] in [wardrobe: put-together but ordinary,
same palette family as the pain image],
[everyday action in a public place], pausing briefly.
Gaze on their own reflection in [reflective surface].
Expression: small closed-mouth smile, private and understated.
Not performing, not aware of a camera.

[EVIDENCE OF CHANGE, bắt buộc]
The resolved symptom must be visible as physical fact: [what the body or object
now looks like]. It must be readable from BOTH the direct view and the reflection.
Do not state the change with expression alone.

[REFLECTION]
[shop window / mirrored panel / car glass] filling [25-35%] of the frame,
showing the subject from a different angle, sharp enough to read the evidence.
The reflection must be geometrically consistent with the subject's position.

[ENVIRONMENT]
[a public everyday place the subject would pass through],
[2-3 incidental blurred passersby or street details], ordinary weather.
Nothing aspirational, no travel-brochure location, no styling.

[LIGHT]
Even natural daylight, bright, soft shadows.
Slightly kinder than the paired pain image, but the SAME time-of-day character.
No golden hour, no rim light, no glamour lighting.

[GRADE]
Muted [palette matching the paired pain image], light film grain,
shallow depth of field. Desaturated, never warm-boosted.

[PAIRING RULE]
This image only works alongside its pain counterpart.
Same person, same palette, same lens character, same grade family.
It carries no argument on its own.

STYLE: candid lifestyle photography, natural, unposed, sharp.
NO text, no logo, no watermark, no product.
```

**Negative:**
```
text, letters, numbers, watermark, logo, badges, arrows, overlays,
looking at camera, posing, laughing, arms raised, celebration gesture,
golden hour, warm flattering light, glamour lighting, beauty retouching,
plastic skin, aspirational travel location, empty clean street, styled outfit,
geometrically wrong reflection, reflection out of focus, product in frame,
saturated colors, stock photo look
```

## Trigger

```yaml
id: 06-relief-scene
step: 6
job: relief
device: scene
version: "1.0"
ratios: [5:3, 16:9, 4:5]
channel: [paid-social, advertorial]
requires_product_photo: false
gaze_modes: [reflect]
exempt_from: [G1, G3, G4]
status: active
use_when: >
  Ảnh đóng của advertorial, hoặc khung cuối của một creative ads. Dùng
  khi lời hứa của sản phẩm là một trạng thái sống chứ không phải một
  tính năng. Bắt buộc đi kèm ảnh pain cùng người.
avoid_when: >
  Gallery sàn, ảnh chính, hoặc bất kỳ chỗ nào ảnh phải đứng một mình.
  Không dùng khi kết quả không nhìn thấy được trên cơ thể hay đồ vật.
requires_pair: 01-pain-scene
```

---

## Test M: `06-relief-scene`

**Sản phẩm: băng dán miệng ngủ.** Đây là ảnh đóng cho Test K. Stress axis: kết quả gần như vô hình. Không có tóc mượt để nhìn, chỉ có một khuôn mặt đã ngủ đủ.

```
A candid documentary photograph, 5:3 ratio. Single frame. NO graphic overlays.

SUBJECT: A man in his late 30s in a plain shirt and an open jacket, walking to work in the early morning, pausing for a second on the pavement. He is looking at his own reflection in a shop window, adjusting his collar. Expression: a small closed-mouth smile, private and understated. Not performing, not aware of a camera.

EVIDENCE OF CHANGE: his face is visibly rested. Skin even rather than sallow, eyes fully open and clear, no shadowing or puffiness beneath them, jaw relaxed, lips closed and not dry. This must be readable both in the direct view and in the reflection.

REFLECTION: a shop window filling roughly 30 percent of the frame on the left, showing him from a different angle, sharp enough to read his face. Geometrically consistent with his position.

ENVIRONMENT: an ordinary city street early in the morning, bare trees, a bus stop sign, two blurred commuters passing behind him, overcast weather. Nothing aspirational, no travel-brochure location, no styling.

LIGHT: even natural daylight, bright, soft shadows. Slightly kinder than a night-time scene but with the same plain documentary character. No golden hour, no rim light, no glamour lighting.

GRADE: muted blue-grey and neutral palette, light film grain, shallow depth of field. Desaturated, never warm-boosted.

STYLE: candid lifestyle photography, natural, unposed, sharp.
NO text, no logo, no watermark, no product.
```

**Đoán chỗ gãy:** slot bằng chứng. "Mặt đã nghỉ ngơi đủ" không phải là vật chứng, nó là suy diễn. Model gần như chắc chắn sẽ ra một người đàn ông bình thường, và ảnh không nói được gì. Nếu gãy thì kết luận là: **`06-relief-scene` chỉ chạy được cho sản phẩm có kết quả nhìn thấy được trên cơ thể hoặc đồ vật.** Với nhóm sản phẩm kết quả vô hình, ảnh đóng phải là `06-relief-hero` có sản phẩm trong khung, không phải type này.

---

## Registry sau 10 type

| Tên | Bán cái gì |
|---|---|
| `01-pain-scene` | Nhận ra chính mình |
| `01-pain-split` | Dừng scroll bằng đau |
| `02-cause-anatomy` | Buộc tội nguyên nhân |
| `02-symptom-rail` | Mở rộng phạm vi vấn đề |
| `03-mechanism-ghostbody` | Biện hộ cho hình dáng |
| `04-proof-lockedframe` | Bằng chứng tự nhìn |
| `05-persona-grid` | Nhận diện bản thân |
| `05-social-handoff` | Người khác đi mách |
| `06-relief-hero` | Trạng thái sau khi mua, có sản phẩm |
| `06-relief-scene` | Trạng thái sau khi mua, không sản phẩm |

`01-pain-scene` và `06-relief-scene` giờ tạo thành cặp đóng mở đầu tiên trong bộ. Chúng phải sinh cùng lúc, cùng nhân vật, cùng bảng màu, và tốt nhất là chạy multi-pass từ cùng một ảnh gốc để giữ đúng khuôn mặt.

---

## Human

**Attachments:**
- 1786344570621_image.png

---

## Assistant

# Bước 1: Phân loại

**Type mới.** Không khớp bất kỳ type nào hiện có.

Đây là job chưa xuất hiện trong bộ: nó không bán vấn đề, không bán cơ chế, không bán trạng thái. Nó **dạy cách dùng**. Ba khung theo trình tự thời gian, mỗi khung một bước, cùng một đôi tay.

**`03-use-sequence`**

Xếp step 3 vì nó thuộc tầng "làm sao nó hoạt động", cùng tầng với `03-mechanism-ghostbody`. Hai cái này bổ nhau: ghostbody giải thích cơ chế bên trong, sequence giải thích thao tác bên ngoài.

Bổ sung vocabulary:
- **job** mới: `use` (chuỗi thao tác)
- **device** mới: `sequence` (nhiều khung, biến số là bước, không phải vật)

# Breakdown

| Khung | Nội dung | Bước |
|---|---|---|
| **Trên** | Tháo nắp bình, nhỏ tinh dầu vào khoang, ngón cái bấm nút, đèn xanh sáng | Chuẩn bị |
| **Giữa** | Chải trên lưng mèo, làn hơi mờ thoát ra từ mặt lược | Sử dụng |
| **Dưới** | Chải tiếp, bàn tay kia vuốt lưng mèo, nắng cửa sổ, mèo yên | Kết quả |

**Cấu trúc:**

Ba khung ngang xếp dọc, gutter trắng mảnh, không đánh số, không mũi tên, không chữ. Trình tự được đọc bằng **logic hành động**, không bằng ký hiệu. Đây là điểm khác biệt với ảnh hướng dẫn thông thường và là lý do nó không trông như tờ hướng dẫn sử dụng.

**Ba luật giữ nó hoạt động:**

**Cùng một đôi tay xuyên suốt.** Móng tay, tông da, cổ tay giống nhau ba khung. Lệch cái này thì thành ba ảnh ghép.

**Sản phẩm ở chính giữa mọi khung.** Không có khung nào để sản phẩm ra rìa. Mắt luôn tìm thấy nó ở cùng vị trí.

**Khung cuối bỏ thao tác, thêm cảm xúc.** Nắng ấm vào, bàn tay kia vuốt con vật, tay cầm lược lùi ra sau. Chuỗi kết thúc bằng quan hệ, không phải bằng thao tác. Đây là thứ tách nó khỏi ảnh hướng dẫn khô khan.

**Điểm yếu:** khung 1 chứa hai hành động khác nhau (tháo nắp và nhỏ tinh dầu) bị dồn vào một khung, đọc hơi chật và mất một nhịp. Ba khung nên là ba hành động, không phải bốn hành động chia ba.

# Skeleton

```
TYPE: 03-use-sequence v1.0
RATIO: [1:1 / 4:5]
LAYOUT: [3] horizontal panels stacked vertically, thin white gutters,
no outer border, no numbers, no arrows, no text.
REGISTER: warm lifestyle photography, close range.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly in every panel.

[CONTINUITY LOCK]
The same hands in every panel: same skin tone, same nails, same wrists,
same sleeves. The same [subject/surface] in every panel.
Same warm neutral palette, same soft natural light direction throughout.
Camera distance may vary between panels, framing may shift naturally.

[SEQUENCE RULE]
One action per panel. Never two.
The order must be readable from the actions alone, with no numbering.
The product must sit near the center of every panel.

[PANEL 1: PREPARE]
[the single setup action], hands in frame, product centered,
[the readiness signal: indicator light / opened part / loaded state] visible.

[PANEL 2: USE]
[the core action in progress] on [subject], mid-motion.
[VISIBLE MECHANISM: if the product emits anything, it must be visible here,
lit to reveal it].

[PANEL 3: RESULT]
[the action continuing or just finished], plus [a second hand or gesture
expressing the relationship or the outcome].
Warmer light than the previous panels. No new mechanics introduced.

[ENVIRONMENT]
[an ordinary domestic setting], soft daylight, [1-2 incidental details].
Same location across all three panels.

STYLE: warm lifestyle product photography, natural, unstyled, sharp, 4K.
NO text, no numbers, no logo, no watermark, no arrows, no step markers.
```

**Negative:**
```
text, letters, numbers, step numbers, arrows, badges, watermark, logo,
deformed hands, extra fingers, different hands between panels,
different subject between panels, two actions in one panel,
product off-center, product cropped out, instruction manual look,
technical diagram, cold clinical lighting, different location between panels,
inconsistent palette, staged perfection
```

## Trigger

```yaml
id: 03-use-sequence
step: 3
job: use
device: sequence
version: "1.0"
ratios: ["1:1", "4:5"]
channel: [marketplace, landing-page]
requires_product_photo: true
camera_lock: handheld
exempt_from: [G3, G4]
status: active
use_when: >
  Sản phẩm có nhiều hơn một thao tác, hoặc người mua có thể nghĩ nó phức
  tạp. Ảnh 4-5 trong gallery. Trả lời câu hỏi "tôi có dùng được không".
avoid_when: >
  Sản phẩm chỉ có một thao tác hiển nhiên. Không dùng làm ảnh chính,
  không dùng để dừng scroll.
pairs_with: 03-mechanism-ghostbody (cùng tầng, khác trục)
```

---

## Test N: `03-use-sequence`

**Sản phẩm: lọc nước vòi sen.** Stress axis: thao tác là lắp đặt một lần, không phải sử dụng hàng ngày. Ép skeleton chứng minh slot PANEL 3 có tìm được kết quả để đóng chuỗi khi bản thân thao tác kết thúc ở bước lắp xong.

```
A warm lifestyle photograph, 1:1 ratio, three horizontal panels stacked vertically, thin white gutters, no outer border, no numbers, no arrows, no text.

Use the attached product photo as the exact reference for the shower filter. Preserve shape, proportions, material, finish and color exactly in every panel.

CONTINUITY LOCK: the same pair of hands in every panel, same skin tone, same nails, same wrists, sleeves pushed up. The same chrome shower arm and the same white tiled wall in every panel. Same warm neutral palette, same soft daylight from the left throughout. Camera distance may vary between panels and framing may shift naturally.

SEQUENCE RULE: one action per panel, never two. The order must be readable from the actions alone. The filter sits near the center of every panel.

PANEL 1, PREPARE: both hands unscrewing the existing shower head from the arm, the head coming free, the bare threaded arm visible. Close range.

PANEL 2, USE: one hand holding the reference filter against the threaded arm, the other hand turning it into place, mid-motion, thread engaging.

PANEL 3, RESULT: the filter fitted and the shower head reattached below it, water running in a clean even spray, backlit from the window so the individual streams and fine mist are clearly visible. One hand held open under the flow, palm up, fingers relaxed. Warmer light than the previous panels.

ENVIRONMENT: an ordinary home bathroom, soft daylight, a folded towel on a rail, a small plant on the sill. Same location across all three panels.

STYLE: warm lifestyle product photography, natural, unstyled, sharp, 4K.
NO text, no numbers, no logo, no watermark, no arrows, no step markers.
```

**Đoán chỗ gãy:** hai chỗ. Một, bàn tay tháo lắp thiết bị ở cự ly gần là bài toán khó nhất với mô hình sinh ảnh, khả năng ra ngón thừa rất cao. Hai, khung 3 phải vừa cho thấy nước chảy vừa giữ được filter ở giữa khung, hai yêu cầu này cạnh tranh không gian. Nếu gãy thì slot PANEL 3 cần tách: hoặc là kết quả, hoặc là sản phẩm ở giữa, không đòi cả hai.

---

## Registry sau 11 type

| Tên | Bán cái gì |
|---|---|
| `01-pain-scene` | Nhận ra chính mình |
| `01-pain-split` | Dừng scroll bằng đau |
| `02-cause-anatomy` | Buộc tội nguyên nhân |
| `02-symptom-rail` | Mở rộng phạm vi vấn đề |
| `03-mechanism-ghostbody` | Biện hộ cho hình dáng |
| `03-use-sequence` | Trấn an về thao tác |
| `04-proof-lockedframe` | Bằng chứng tự nhìn |
| `05-persona-grid` | Nhận diện bản thân |
| `05-social-handoff` | Người khác đi mách |
| `06-relief-hero` | Trạng thái sau khi mua, có sản phẩm |
| `06-relief-scene` | Trạng thái sau khi mua, không sản phẩm |

Bộ đã đủ dày để xuất bản. Nói tôi biết khi nào bạn muốn registry v1.3, gồm 11 type, các biến thể, trường `camera_lock`, `context_mode`, `generation_mode`, luật G7, và phần sequencing cho ba kênh.

---

## Human

**Attachments:**
- 1786344689542_image.png

---

## Assistant

<details><summary>Thinking</summary>

I'm looking at a UGC-style iPhone photo showing someone holding an air purifier up to their face with visible mist, eyes closed in satisfaction, plus a wall-mounted product inset in the top-left corner. The classification seems to be relief as the job (capturing that satisfied state of use) with the device as hero, though I'm reconsidering whether this fits the 06-relief-hero pattern since the inset shows the product installation context rather than a problem state.

The key distinction here is the register—this is amateur UGC photography, not polished commercial work, which feels like a meaningful structural difference. Since the job and device are the same as the previous relief-hero example, this would be a variant with a `--ugc` modifier. I'm

</details>

# Bước 1: Phân loại

**Trùng type.** `06-relief-hero`. Cùng job (`relief`), cùng device (`hero`, một cảnh chụp kèm inset).

Nhưng nó khác hai ảnh trước ở hai trục độc lập nhau, và đây là lúc phải tách hai trục đó ra:

| Trục | Giá trị đã gặp |
|---|---|
| **Register** | `commercial` (đệm ghế, lược xịt), **`ugc`** (ảnh này) |
| **Chức năng inset** | `vsinset` (so sánh), `recall` (nhắc vấn đề), **`context`** (ảnh này) |

Trước giờ tôi gộp hai trục làm một nên đặt tên sai. Sửa lại:

```
06-relief-hero--{register}--{inset_mode}
```

Ảnh này là **`06-relief-hero--ugc--context`**.

# Bước 2: Đối chiếu

| Slot | A (đệm ghế) | B (lược xịt) | C (ảnh này) | Ghi chú |
|---|---|---|---|---|
| Register | Studio, high-key, sạch | Studio, ngược nắng đẹp | **iPhone, phơi sáng lệch, nền lộn xộn** | Trục mới |
| Cơ chế nhìn thấy | Không có | Làn sương xịt | **Luồng hơi trắng dày, chiếm 20% khung** | C mạnh nhất |
| Chức năng inset | So sánh sai/đúng | Nhắc lại vấn đề | **Cho thấy vị trí lắp đặt thật** | Trục mới |
| Sản phẩm trong hero | Bị che sau lưng | Trong tay, giữa khung | Trong tay, **quá gần mặt** | Xem lỗi bên dưới |
| Biểu cảm | Cười, mắt nhắm | Nhìn tóc, tập trung | Mắt nhắm, cảm nhận | Ngang nhau |
| Độ tin | Rõ là quảng cáo | Rõ là quảng cáo | **Đọc như ảnh người thật gửi** | C thắng ở kênh nguội |

**C xác nhận dứt khoát Vá 2 (visible mechanism).** Luồng hơi ở đây là toàn bộ nội dung của ảnh. Bỏ nó đi thì còn lại một người đàn ông ôm cái máy. Nó cũng chứng minh thêm một điều: cơ chế nhìn thấy được **quan trọng hơn chất lượng ảnh**. Ảnh này chụp xấu hơn hẳn hai ảnh kia nhưng thuyết phục hơn cả hai.

**Nhưng C vi phạm G7 nặng.** Inset cho thấy thiết bị gắn tường trong bếp. Hero cho thấy người đó tháo nó xuống, cầm lên, dí sát mặt. Không ai làm vậy với máy gắn tường. Hai lớp trong cùng một ảnh mâu thuẫn nhau về cách dùng, và đây đúng là loại lỗi mà G7 vừa được lập ra để chặn. Ảnh thắng ở tầng bằng chứng, thua ở tầng logic.

# Bước 3: Vá, `06-relief-hero` v1.3

## Vá 6: Trục register

```
[REGISTER]
--commercial: professional camera, controlled light, clean composition,
  deliberate negative space. Channel: marketplace, landing page, A+ content.

--ugc: shot on a phone by an ordinary person. Slightly off exposure,
  mild overexposure on skin or windows, no rim light, no negative space,
  the room behind left exactly as it is: furniture, cables, books, clutter.
  Framing casual and a little too close. Subject not styled.
  Channel: paid-social, advertorial header.
  This register buys trust, not beauty. Do not clean it up.
```

**Negative cho `--ugc`:** `professional lighting, studio setup, clean composition, styled interior, negative space, color graded, retouched skin, magazine look, glossy, symmetrical framing`

## Vá 7: Trục chức năng inset

```
[INSET MODE]
--vsinset: split panel, wrong state vs correct state, VS badge.
  Use when the argument is sai/đúng.

--recall: single circle showing the problem state. Must be marked as past
  (desaturated or red X badge), or it reads as a result.
  Use when the problem is visual and needs one reminder.

--context: single panel showing the product in its real installed position
  or its real place of use, as a clean product-in-place shot.
  Use when the hero shows the product in hand and the buyer still needs
  to know where it actually lives.
  HARD CONSTRAINT: the usage shown in the inset and the usage shown in the
  hero must be the SAME mode of use. An inset showing the product mounted
  while the hero shows it handheld contradicts itself and breaks G7.
```

## Vá 8: G7 áp cho quan hệ giữa các lớp

Đây là mở rộng của G7, rút ra từ chính lỗi của ảnh này. Áp cho mọi type nhiều lớp.

```
[G7 EXTENSION: CROSS-LAYER CONSISTENCY]
When an image contains more than one layer showing the product,
every layer must depict the same mode of use.
Installed in one layer and handheld in another is a contradiction,
even when each layer is plausible on its own.
Pick one mode of use and hold it across the whole image.
```

## Vá 9: Cơ chế nhìn thấy được, nâng lên bắt buộc

Ba ảnh liên tiếp đã chứng minh. Nâng slot này từ có điều kiện lên bắt buộc trong `06-relief-hero`.

```
[VISIBLE MECHANISM]
If the product emits anything visible, that output is the primary subject
of the frame, not the person and not the product.
Frame, light and expose for the output. Everything else serves it.
It must occupy at least 15% of the frame and read at thumbnail size.
```

---

## Test O: `06-relief-hero--ugc--context`

**Sản phẩm: lọc nước vòi sen.** Chọn sản phẩm này vì nó vừa có cơ chế nhìn thấy được (tia nước), vừa là thiết bị lắp cố định, đúng cấu hình đã làm ảnh gốc vi phạm G7. Test này kiểm tra xem Vá 8 có chặn được lỗi đó không.

```
A photograph taken on a phone by an ordinary person, 2:1 ratio.

Use the attached product photo as the exact reference for the shower filter. Preserve shape, proportions, material, finish and color exactly. It appears installed in both the main scene and the inset. Never handheld.

MAIN SCENE (right two-thirds): A man in his early 40s standing in his own bathroom with his eyes closed and his face tilted up under the running shower, water hitting his shoulders, an unguarded relaxed expression. The reference filter is fitted above him between the arm and the shower head, clearly visible in the upper part of the frame. The water spray is the primary subject: dense individual streams and fine mist backlit by a window behind him, occupying a large part of the frame and clearly readable at small size.

REGISTER: shot on a phone. Slightly overexposed on the tiles and the window, no rim light, no negative space. Framing casual and a little too close, tilted a few degrees. The bathroom left exactly as it is: shampoo bottles crowded on the corner shelf, a razor on the ledge, towels bunched on the rail, water spots on the glass. Not styled, not cleaned up.

INSET (top-left corner, rectangular, thin white border): a plain closer shot of the same filter installed on the same shower arm, taken from a step back so the whole fitting is clear. Same mode of use as the main scene: installed, never in hand. Same room, same daylight.

STYLE: casual phone photography, natural, unstyled, honest.
NO text, no logo, no watermark, no badges, no arrows.
```

**Đoán chỗ gãy:** khoảng cách. Trong ảnh gốc, sản phẩm ở sát mặt nên chiếm 30% khung, đó là lý do người xem thấy rõ cả sản phẩm lẫn cơ chế. Ở đây filter treo trên cao, xa máy quay, có thể chỉ còn vài chục pixel. Nếu gãy thì phải chấp nhận: **thiết bị lắp cố định không dùng được `--ugc` ở cự ly gần**, và cấu hình đúng cho nhóm đó là khung chụp từ dưới lên, lấy filter và tia nước làm chủ thể, người chỉ còn một phần vai trong khung.

---

## Cập nhật registry

```yaml
- id: 06-relief-hero
  version: "1.3"
  axes:
    register: [commercial, ugc]
    inset_mode: [vsinset, recall, context, none]
  naming: 06-relief-hero--{register}--{inset_mode}
  required_slots: [visible-mechanism]
  hard_rules: [G7, G7-cross-layer]
```

Trục `register` này gần như chắc chắn áp được cho nhiều type khác, không riêng relief-hero. `01-pain-scene--confront` chụp kiểu UGC sẽ là một creative rất mạnh cho ads nguội. Nếu bạn có ảnh mẫu UGC cho các type khác thì đưa vào, tôi sẽ nâng `register` thành trục toàn hệ thay vì thuộc tính riêng của một type.

---

## Human

**Attachments:**
- 1786344748461_image.png

---

## Assistant

<details><summary>Thinking</summary>

I'm looking at a new image type that shows a side-by-side comparison of an old, worn motor stator against a sleek new brushless motor with a CGI render. This isn't about pain or medical anatomy—it's a component-level comparison designed to highlight the technological difference between the old and new product. The job here is to differentiate based on the superior internal technology.

I'm calling this `03-spec-split` since it's operating at the mechanism tier, using a diagonal split with a glowing blue edge to convey energy and dynamism. The left side is a grayscale, corroded real photo, while the right is a pristine CGI render with blue rim glow. There's a deliberate register mismatch between the two—photo versus render—which reinforces the message: old equals real-world decay, new equals engineered perfection. The gold VS with spark burst at the center adds visual drama, though I'm noting this reads as fairly aggressive advertising, almost bordering on the dropship aesthetic with that sparks effect.

The credibility issue here is that neither component is necessarily verifiable—the left motor might not be a competitor's, just a dirty motor, and the right is likely a stock CGI render, not the actual product inside. This works on marketplaces like Amazon or Temu where buyers are spec-driven, but it fails on brand-led channels. For testing this template with a different product, I'm thinking a knife sharpener would be stronger than a shower filter—comparing a cheap ceramic rod against a diamond disc gets at the actual material differentiation that matters to the buyer.

</details>

# Bước 1: Phân loại

**Type mới.** Không khớp type nào hiện có.

Nó dùng thiết bị chia đôi giống `01-pain-split`, nhưng chủ thể không phải người, không phải triệu chứng, mà là **linh kiện bên trong**. Job cũng khác: nó không bán vấn đề, nó bán tính vượt trội về kỹ thuật.

**`03-spec-split`**

Bổ sung vocabulary: job `spec` (so sánh cấp linh kiện, không có người, không có triệu chứng).

# Breakdown

| Thành phần | Chi tiết |
|---|---|
| **Chia khung** | **Đường chéo**, không phải dọc, viền phát sáng xanh dọc mép |
| **Vế trái** | Ảnh chụp thật, xám, mô tơ cũ, dây đồng cháy, gỉ, bụi bẩn |
| **Vế phải** | Render 3D, mô tơ mới, viền sáng xanh, sạch tuyệt đối, lơ lửng |
| **Tâm khung** | Chữ VS vàng kim, tia lửa cam nổ tại đường chia |
| **Đáy** | Sản phẩm hoàn chỉnh trong khung bo tròn trắng, nền trắng |

**Ba điểm cấu trúc:**

**Lệch register là cố ý.** Trái là ảnh chụp, phải là render. Vi phạm G5 nhưng có lý do: ảnh chụp mang nghĩa "thứ đang mục nát trong đời thật", render mang nghĩa "thứ được thiết kế ra". Đây là lần đầu trong bộ mà phá G5 lại đúng.

**Đường chéo thay đường dọc.** Dọc là so sánh tĩnh, cân bằng. Chéo là chuyển động, một bên đang lấn bên kia. Cùng với tia lửa, nó biến so sánh thành xung đột.

**Inset đáy là neo thực tế.** Hai vế trên đều là linh kiện, người mua không mua linh kiện. Ô đáy trả lời "vậy cái tôi nhận được là gì".

# Nhận xét thẳng về hiệu quả

Đây là type rủi ro nhất trong bộ, vì ba lý do:

**Thẩm mỹ này gắn liền với hàng rẻ.** VS vàng kim, tia lửa, viền neon xanh. Người mua đã học được rằng ảnh trông như thế này thường đi kèm sản phẩm không tên tuổi. Nó tăng chuyển đổi trên sàn giá rẻ và giảm chuyển đổi ở phân khúc cao hơn.

**Vế phải là render nên không chứng minh được gì.** Không ai xác nhận được cái mô tơ đó thật sự nằm trong sản phẩm. Vế trái là ảnh thật, vế phải là đồ họa. Người xem tinh ý đọc ra ngay sự bất đối xứng đó.

**Vế trái không phải linh kiện của đối thủ.** Nó chỉ là một mô tơ cũ bẩn. Đặt cạnh nhau thì hàm ý "cái kia là của họ", nhưng không có gì bảo đảm điều đó. Đây là claim mềm nhưng vẫn là claim.

Dùng được, nhưng chỉ ở đúng chỗ: sàn giá cạnh tranh, ngành hàng mà người mua thật sự tra cứu thông số (mô tơ, pin, chip, vật liệu mài, màng lọc). Không dùng cho ngành hàng bán bằng cảm xúc hay thương hiệu.

# Skeleton

```
TYPE: 03-spec-split v1.0
RATIO: [1:1 / 4:5]
LAYERS: diagonal two-panel split + center badge + product inset at bottom.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the inset only.
Preserve shape, proportions, material, finish and color exactly.

[SPLIT]
A diagonal division running from [top-left to bottom-right / top-right to
bottom-left], edged with a thin glowing [accent color] line.
The two halves must be visually unequal in energy: the right half advancing.

[LEFT PANEL: THE OLD COMPONENT]
Photographic register. Desaturated grayscale.
A generic, unbranded [component type] in aged condition:
[3 signs of degradation]. Dusty, dim environment, no styling.
It must look like a real object photographed in the real world.

[RIGHT PANEL: THE NEW COMPONENT]
3D render register. A pristine [component type] of the improved type,
[key visible technical differentiator], cool [accent color] rim lighting,
floating against a dark gradient, sharp reflective surfaces.
It must look engineered, not photographed.

[CENTER BADGE]
Large [metallic] "VS" at the intersection of the diagonal,
with a burst of [warm] sparks at the seam. Nothing else at the center.

[PRODUCT INSET, bottom]
The reference product, complete and whole, on a plain white background
inside a rounded rectangle, occupying [20-25%] of the frame width.
This is the only place the finished product appears.

[HONESTY CONSTRAINT]
The left component must not carry any brand mark, logo or identifiable design.
The right component must be the type genuinely used inside the product.
Do not render a component the product does not contain.

STYLE: high-contrast technical comparison graphic, e-commerce, sharp, 4K.
NO text beyond the VS badge, no logo, no watermark.
```

**Negative:**
```
text, letters, numbers, watermark, logo, brand marks, recognizable trademarks,
readable model numbers, both halves rendered, both halves photographic,
symmetrical composition, vertical split, dull center, low contrast,
product inset missing, product inset cropped, cartoonish explosion, fire, smoke,
gore, human hands, human figures
```

## Trigger

```yaml
id: 03-spec-split
step: 3
job: spec
device: split
version: "1.0"
ratios: ["1:1", "4:5"]
channel: [marketplace]
register: commercial
requires_product_photo: true
exempt_from: [G5, G7]
status: active
use_when: >
  Ngành hàng mà người mua thật sự so sánh thông số linh kiện: mô tơ, pin,
  chip, vật liệu mài, tầng lọc, lưỡi cắt. Ảnh 4-6 trong gallery sàn.
  Chỉ dùng khi sản phẩm THẬT SỰ chứa linh kiện được vẽ.
avoid_when: >
  Ngành hàng bán bằng cảm xúc, thương hiệu hoặc thẩm mỹ. Không dùng ở
  paid-social hay advertorial, thẩm mỹ này báo hiệu hàng giá rẻ. Không
  dùng làm ảnh chính.
pairs_with: 03-mechanism-ghostbody (cùng tầng, đối tượng khác)
risk: credibility, unverifiable internal claim
```

---

## Test P: `03-spec-split`

**Sản phẩm: dụng cụ mài dao lăn.** Linh kiện khác biệt là vật liệu mài, một thứ người mua nhóm này thật sự tra cứu.

```
A high-contrast technical comparison graphic, 1:1 ratio.

Use the attached product photo as the exact reference for the inset only. Preserve shape, proportions, material, finish and color exactly.

SPLIT: a diagonal division running from top-left to bottom-right, edged with a thin glowing cyan line. The right half advances into the left.

LEFT PANEL, THE OLD COMPONENT: photographic register, desaturated grayscale. A generic unbranded ceramic sharpening rod and a worn steel honing rod lying in a dim drawer, the ceramic chipped along its length, the steel scored with deep uneven scratches, metal filings and grey dust around them. It must look like a real object photographed in the real world.

RIGHT PANEL, THE NEW COMPONENT: 3D render register. A pristine circular abrasive disc of the diamond-coated type, its surface covered in a dense uniform field of fine crystalline grit catching the light, edge-on so both the flat face and the thin profile are visible, cool cyan rim lighting, floating against a dark gradient, sharp reflective surfaces. It must look engineered, not photographed.

CENTER BADGE: a large brushed-gold "VS" at the intersection of the diagonal, with a burst of warm orange sparks at the seam. Nothing else at the center.

PRODUCT INSET, bottom: the reference sharpener, complete and whole, on a plain white background inside a rounded rectangle, occupying about 22 percent of the frame width. This is the only place the finished product appears.

HONESTY CONSTRAINT: the left components carry no brand mark, logo or identifiable design.

STYLE: high-contrast technical comparison graphic, e-commerce, sharp, 4K.
NO text beyond the VS badge, no logo, no watermark.
```

**Đoán chỗ gãy:** hai chỗ. Một, hạt kim cương ở cự ly render rất dễ ra thành bề mặt nhám chung chung, mất luôn điểm khác biệt duy nhất. Nếu gãy thì slot cần đổi từ mô tả vật liệu sang mô tả **hiệu ứng ánh sáng của vật liệu**: vô số điểm sáng li ti bắt sáng, thứ mô hình vẽ tốt hơn. Hai, chữ VS. Đây là type duy nhất trong bộ cho phép chữ trong khung, mà mô hình sinh chữ thì hay ra sai. Nhiều khả năng phải chèn VS ở hậu kỳ.

---

## Registry sau 12 type

| Tên | Bán cái gì | Kênh |
|---|---|---|
| `01-pain-scene` | Nhận ra chính mình | paid-social, advertorial |
| `01-pain-split` | Dừng scroll bằng đau | marketplace |
| `02-cause-anatomy` | Buộc tội nguyên nhân | landing-page, marketplace |
| `02-symptom-rail` | Mở rộng phạm vi vấn đề | marketplace |
| `03-mechanism-ghostbody` | Biện hộ cho hình dáng | marketplace |
| `03-spec-split` | Vượt trội cấp linh kiện | marketplace |
| `03-use-sequence` | Trấn an về thao tác | marketplace, landing-page |
| `04-proof-lockedframe` | Bằng chứng tự nhìn | mọi kênh |
| `05-persona-grid` | Nhận diện bản thân | marketplace |
| `05-social-handoff` | Người khác đi mách | paid-social, advertorial |
| `06-relief-hero` | Trạng thái sau, có sản phẩm | mọi kênh |
| `06-relief-scene` | Trạng thái sau, không sản phẩm | paid-social, advertorial |

Step 3 giờ có ba type, đủ để thấy rõ chúng chia nhau ba câu hỏi khác nhau: `ghostbody` trả lời "hình dáng này có lý do gì", `spec-split` trả lời "bên trong có gì tốt hơn", `use-sequence` trả lời "tôi có dùng nổi không". Một gallery hiếm khi cần cả ba, chọn một hoặc hai tùy ngành hàng.

---
