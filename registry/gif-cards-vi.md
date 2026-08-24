# Vietnamese copy for the GIF library folder cards

The one place in this repo where artifact content is not English (SPEC §3.6, ADR-044). Its
reader is an editor filing files into `gifs-library/`, not a harness reading law, and an
editor who works in Vietnamese should not have to parse English to know which folder a loop
belongs in. Everything that BINDS still lives in English in `registry/gif-types/<id>.md`;
this file is copy for a view.

`scripts/gen-gif-cards.py` reads it and writes `README.vi.md` beside each folder's
`README.md`. `scripts/validate.py` fails a gif type with no entry here, or an entry missing
a field, so the two cards cannot drift into saying different things by omission.

One `## <gif-type>` section per type. Each field is one line, and short is the point — the
English card is already the long form.

## cause

message: Thủ phạm đang gây hại ngay lúc này, và sản phẩm không có trong khung.
yes: Mục nói điều gì gây ra vấn đề, và nguyên nhân là một sự việc đang diễn ra chứ không phải một trạng thái đứng yên.
no: Vấn đề là trạng thái tĩnh để người xem soi — giường đã lột, đống đồ đã thử, căn phòng đơn giản là nóng.
vs: So với `proof`, ở đây sản phẩm vắng mặt và chính sự vắng mặt đó là phép thử.
never: Không chữ, không số, không mũi tên. Không có sản phẩm trong khung, kể cả gợi ý.

## mechanism

message: Nó đáng tiền vì thứ xảy ra bên trong.
yes: Mục giải thích vì sao sản phẩm chạy được, và lời giải thích là một chuyển động — cánh quạt quay, luồng khí đi một đường, mút nở lại.
no: Tuyên bố vô hình với mọi register thư viện có: nhiệt, mùi, chất lượng không khí, hoá học pin.
vs: So với `use`, khác ở khung hình chứ không ở chủ thể — không ai là chủ thể ở đây. So với `proof`, đây là nguyên nhân chứ không phải kết quả.
never: Không chữ, không số, không mũi tên, không đường dẫn dòng. Không lấy người làm chủ thể.

## proof

message: Trước và sau, trong một khung liền không cắt.
yes: Lập luận của mục là bằng chứng vật lý, và bằng chứng là một thay đổi đo được do sản phẩm gây ra.
no: Bằng chứng là những trạng thái đặt cạnh nhau để soi — bảng nhiều ô khoá cứng, ba mốc thời gian trong một khung.
vs: So với `mechanism` là kết quả chứ không phải nguyên nhân; so với `cause` thì ở đây sản phẩm có mặt; so với `relief` là đo được chứ không phải sống được.
never: Không chữ, không số, không thanh tiến trình. Không cắt cảnh giữa hai trạng thái, và không lặp ngược.

## relief

message: Đời sống sau khi mua, quay đúng chỗ mà vấn đề từng chặn lại.
yes: Mục bán trạng thái sau, và trạng thái đó chứa một hành động TIẾP DIỄN mà vấn đề trước đây từng chặn.
no: Trạng thái sau là một khoảnh khắc đứng yên — ai đó đang nghỉ, căn phòng gọn gàng, cả nhà ngồi xem.
vs: So với `proof`, đây là sống được chứ không phải đo được.
never: Không chữ, không mũi tên, không overlay. Sản phẩm không được giơ ra khoe hay đặt vào giữa khung.

## use

message: Bạn dùng được nó mà không phải nghĩ.
yes: Việc của mục là thao tác — một beat hướng dẫn, một tính năng vốn LÀ hành động, hoặc dụng cụ mà cả tuyên bố nằm ở chỗ thao tác dễ.
no: Điều cần nói chỉ nói được bằng cách phóng to bộ phận làm việc, đó là `mechanism`; hoặc mục đang nói về thay đổi mà hành động tạo ra chứ không phải hành động, đó là `proof`.
vs: So với `mechanism`, khác ở khung hình — có bàn tay và cả sản phẩm. So với `proof`, đây là hành động chứ không phải kết quả.
never: Không chữ, không số bước, không mũi tên chỉ thứ tự đọc.

## unboxing

message: Bạn thực sự nhận được gì, từng món một.
yes: Brief cho kênh quảng cáo, sản phẩm bán theo bộ hoặc nhiều món, và câu hỏi bỏ ngỏ của người mua là "có đủ không".
no: Bất cứ chỗ nào trên landing page — type này chỉ chạy kênh quảng cáo.
vs: So với `use`, đây là bày ra chứ không phải thao tác.
never: Không chữ, không số. Không dựng cảnh gọn gàng quá mức thật.
