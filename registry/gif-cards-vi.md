# Vietnamese copy for the GIF library folder cards

The one place in this repo where artifact content is not English (SPEC §3.6, ADR-044). Its
reader is an editor filing files into `gifs-library/`, not a harness reading law. Everything
that BINDS still lives in English in `registry/gif-types/<id>.md`; this file is copy for a
view.

**Three rules for writing it** (ADR-045, ADR-046):

1. **Definition first, then the example.** Say what the type is, finish the thought, and only
   then illustrate it. An example that arrives mid-definition reads as part of the definition.
2. **Every example is a real loop this library has commissioned**, named with its product and
   its page. The English type files illustrate with fragments — "a lane of fabric goes from
   grey to clean" — which carry their meaning only for someone who already knows the library.
   An editor holding a file does not. "The seat cushion page has a `cause` loop where…" does.
3. **Keep every English keyword as it stands**: type ids, `channels` values, `group`, `kind`,
   field names, file paths. Translating `landing-page` severs the card from every other
   surface the editor touches; translating `proof` makes the folder name and the card
   disagree.

`scripts/gen-gif-cards.py` reads this file and writes `README.vi.md` beside each folder's
`README.md`. `scripts/validate.py` fails a gif type with no entry here, or an entry missing a
field.

Format: one `## <gif-type>` section per type. A field is `<key>:` alone on a line, and
everything after it belongs to that field until the next key or the next type. Blank lines
inside a field are kept. Four fields: `message`, `yes`, `no`, `vs`.

## cause

message:
`cause` quay đúng lúc thủ phạm đang gây hại — cái thứ làm người mua khổ, đang diễn ra ngay
trước ống kính. Sản phẩm không có trong khung và cũng không được ám chỉ: loop này đi buộc tội,
chưa giới thiệu giải pháp.

Ví dụ, trang bán đệm ngồi ergonomic có một loop `cause` như sau. Người lái đang ngồi trên tấm
đệm phẳng cũ trên ghế xe. Xe phanh, tấm đệm trượt tới trước dưới người anh ta, và khe hở sau
lưng dưới hở toác ra. Chiếc đệm đang bán không xuất hiện ở đâu trong khung cả.

yes:
Nộp vào đây khi mục trên trang đang nói **cái gì gây ra vấn đề**, và cái đó là một sự việc đang
diễn ra chứ không phải một tình trạng nằm im. Nói cách khác: phải có thứ gì đó thật sự động
đậy để mà quay — trượt, rơi, bay lên, siết lại.

no:
Đừng nộp vào đây khi vấn đề chỉ là một trạng thái để người xem nhìn rồi tự hiểu.

Ví dụ, trang bán máy hút bụi đệm có một mục nói về bụi bẩn tích trong nệm. Nếu quay cái nệm đã
lột hết ga nằm đó thì không có gì chuyển động — đó là ảnh tĩnh, không phải `cause`. Chỉ khi
quay được bụi đang bốc lên khỏi thớ vải lúc có người ngồi xuống thì mới thành loop.

vs:
Ranh giới với `proof` rất gọn: **chỉ cần sản phẩm bước vào khung là hết `cause`**. Sự vắng mặt
của sản phẩm chính là phép thử — có nó trong hình thì loop chuyển sang nói về kết quả, và phải
nộp vào `proof`.

Còn quay một người đang chịu đựng hay quay riêng đồ vật thì vẫn là `cause` cả hai. Bàn tay
trượt và tấm thảm rụng vụn đang nói cùng một điều — chuyện tệ này vẫn đang xảy ra — nên đó chỉ
là hai cách dựng, không phải hai type.

## mechanism

message:
`mechanism` mở sản phẩm ra cho xem **bên trong nó làm gì mà đáng tiền**. Bộ phận làm việc được
phóng to hoặc cắt bổ ra, và đang làm đúng một việc mà sản phẩm được bán vì nó.

Ví dụ, trang bán lược xịt điện có một loop `mechanism` như sau. Quay cận giường răng lược, sau
ba tuần dùng đã bám đầy tóc rụng và bụi. Một ngón tay bấm nút trên cán, cả hàng răng thụt hẳn
vào lớp đệm, và búi tóc bong ra nguyên mảng.

yes:
Nộp vào đây khi mục đang giải thích **vì sao sản phẩm chạy được**, và lời giải thích đó là một
chuyển động nhìn thấy được: rotor quay, luồng khí đi hết một đường, lớp mút nở lại sau khi bị
ép, con trượt chạy trên rãnh của nó.

no:
Đừng nộp vào đây khi điều cần chứng minh vô hình với mọi cách quay mà thư viện này có.

Ví dụ, cùng chiếc lược đó còn có sáu đèn LED đỏ quảng cáo là kích thích da đầu. Cái đèn thì
quay được, nhưng **tác dụng** của nó lên da đầu thì không — không có gì chuyển động để cho
xem. Nhiệt độ, mùi, chất lượng không khí, phản ứng hoá học trong pin đều rơi vào nhóm này.

vs:
Khác `use` ở **khung hình, không phải ở chủ thể**. Vẫn cái kéo điện đó: quay cả bàn tay lẫn cả
sản phẩm là `use`; quay cận lưỡi kéo, không lấy người làm chủ thể, là `mechanism`.

Khác `proof` ở chỗ đây là nguyên nhân còn kia là kết quả. Rotor đang quay là `mechanism`; bụi
rời khỏi tấm nệm là `proof`. Loop nào cho xem cả hai thì tính là `proof`, vì người xem sẽ chấm
theo kết quả chứ không theo lý do.

## proof

message:
`proof` cho người xem **tự nhìn thấy sự thay đổi rồi tự kết luận**. Một khung quay liền, không
cắt, trong đó đúng một thứ đổi trạng thái.

Ví dụ, trang bán lược xịt điện có một loop `proof` như sau. Một lọn tóc dựng đứng thành quầng
vì tĩnh điện sau khi chải bằng lược nhựa thường. Chiếc lược đang bán đi qua một lượt, và quầng
tóc xẹp dần xuống từng sợi cho tới khi nằm phẳng hết. Không cắt cảnh ở giữa — vì cắt là bạn
đang khẳng định hộ người xem thay vì để họ tự thấy.

yes:
Nộp vào đây khi mục đang đưa **bằng chứng vật lý**, và bằng chứng đó là một thay đổi đo được do
sản phẩm gây ra. Thường rơi vào những chỗ mà người đang hoài nghi muốn tận mắt xem nó xảy ra,
chứ không muốn nghe kể lại.

no:
Đừng nộp vào đây khi bằng chứng là **nhiều trạng thái đặt cạnh nhau để so**, chứ không phải một
thay đổi diễn ra trước mắt.

Ví dụ, cũng trang lược đó có một thẻ so sánh dựng thành ảnh chia ba ô: cùng một lọn tóc, chụp
sau khi chải bằng lược nhựa, bằng lược tròn, và bằng chiếc lược đang bán, ba ô đặt cạnh nhau.
Ở dạng đó chính mắt người xem đi so ba ô; cho nó chuyển động sẽ xoá mất phép so ấy chứ không
làm rõ thêm.

vs:
Khác `mechanism` ở chỗ đây là kết quả, kia là nguyên nhân.

Khác `cause` ở chỗ **sản phẩm có mặt**, và chính sự có mặt đó mới khiến thay đổi quy được về
nó.

Khác `relief` ở chỗ `proof` là thứ đếm được hoặc so được, còn `relief` là một cuộc sống đang
trôi trơn tru.

Một lưu ý thực dụng: đây là đường bậc-2 chính của cả thư viện. Slot `proof` thường được định
tuyến sang một ảnh tĩnh chia ô, và ảnh đó đúng là không được cấp chuyển động. Bản loop là cách
dựng khác cho cùng lập luận — một khung liền, một biến đổi thay.

## relief

message:
`relief` quay **cuộc sống sau khi mua**, tại đúng chỗ mà vấn đề từng chặn lại. Sản phẩm có mặt
và đang chạy, nhưng nó không phải nhân vật chính.

Ví dụ, trang bán đệm ngồi ergonomic có một loop `relief` như sau. Người đàn ông đứng dậy khỏi
ghế khán đài sân bóng lúc trận đấu vừa tan. Anh ta đứng thẳng lên trong một nhịp, không vịn lan
can cũng không chống tay xuống ghế, rồi đi xuống bậc mà không một lần đưa tay ra sau lưng. Đúng
chuyện ngồi hết một trận bóng là thứ mà trước đây cơn đau đã lấy mất của anh ta.

yes:
Nộp vào đây khi mục đang bán **trạng thái sau**, và trạng thái đó chứa một hành động **đang tiếp
diễn** mà trước kia vấn đề vẫn hay làm gián đoạn.

no:
Đừng nộp vào đây khi trạng thái sau chỉ là một khoảnh khắc đứng yên.

Ví dụ, vẫn trang đệm ngồi đó, nếu quay người đàn ông đang ngồi thoải mái trên ghế khán đài và
mỉm cười thì đó là ảnh tĩnh đẹp chứ không phải `relief` — không có gì đang diễn ra. Chỉ khi anh
ta **đứng lên được** thì mới có chuyển động, và chính chuyển động đó mới là thứ vấn đề từng
chặn.

vs:
Khác `proof` ở chỗ đây là sống được, kia là đo được. Nếu người xem có thể đếm nó hoặc đem nó ra
so, thì đó là `proof`.

Và đây là chỗ có **luật chặt nhất trong cả sáu type**: `relief` chỉ được cấp loop khi **chính
chuyển động đó là thứ mà vấn đề từng chặn**. Rèm bay, hơi nước cuộn, cây lay — dễ chịu thật,
nhưng chúng chỉ tình cờ có mặt trong một cảnh hậu-mua và không chứng minh gì; loại đó mặc định
bị tắt. Luật này viết ra để `relief` không thành cái thùng chứa mọi loop không đủ tiêu chuẩn.

## use

message:
`use` nói **dùng nó chẳng phải nghĩ**. Một bàn tay tác động lên sản phẩm và sản phẩm đáp lại.
Loop bán sự dễ dàng của chính thao tác, chứ không bán cái mà thao tác để lại phía sau.

Ví dụ, trang bán lược xịt điện có một loop `use` như sau. Hai bàn tay ở bồn rửa, ô nhìn của
bình nước trên lược đang rỗng. Nước rót vào cửa nạp cho tới khi ô nhìn báo đầy một nửa, ngón
cái bấm công tắc, rồi chiếc lược chải xuôi hết chiều dài tóc với làn sương rời khỏi giường
răng.

yes:
Nộp vào đây khi việc của mục là **thao tác**: một đoạn hướng dẫn dùng, một tính năng mà bản
thân nó đã là một hành động, hoặc một dụng cụ mà toàn bộ điểm bán nằm ở chỗ làm nó dễ.

no:
Đừng nộp vào đây khi điều cần nói chỉ nói được bằng cách phóng to bộ phận làm việc, hoặc khi
mục đang nói về **thay đổi mà thao tác tạo ra** chứ không phải bản thân thao tác.

Ví dụ, vẫn chiếc lược đó: quay hai bàn tay chải xuôi một lượt là `use`; quay cận hàng răng thụt
vào nhả búi tóc là `mechanism`; quay quầng tóc tĩnh điện xẹp xuống sau một lượt chải là `proof`.
Cùng một sản phẩm, ba loop, ba folder khác nhau.

vs:
Khác `mechanism` ở khung hình: cả sản phẩm cộng một bàn tay là `use`; cận bộ phận làm việc,
không có người, là `mechanism`.

Khác `proof` ở chỗ `use` cho xem hành động, còn `proof` cho xem thay đổi mà hành động gây ra.
Loop nào mang cả hai thì tính là `proof`, và thao tác chỉ là nhịp mở đầu của nó.

Số nhịp là **tham số, không phải một type khác**: một thao tác liền mạch và một chuỗi ba bước
đang nói cùng một điều ở hai độ dài, tách ra sẽ thành hai thư mục cho một thông điệp.

## unboxing

message:
`unboxing` cho thấy **bạn thực sự nhận được những gì**, từng món một. Hộp mở ra, các món lần
lượt được lấy ra cho tới khi cả bộ nằm hết trong khung.

Ví dụ, một bộ dụng cụ nâng đồ nội thất bán qua kênh quảng cáo. Hộp mở trên sàn gỗ, lấy ra bốn
con lăn, rồi thanh đòn bẩy, rồi tờ hướng dẫn, xếp thành hàng cho tới khi nhìn thấy đủ bộ. Câu
người mua đang treo trong đầu là "có đủ không", và loop trả lời đúng câu đó.

yes:
Nộp vào đây khi đây là brief cho **kênh quảng cáo**, sản phẩm bán theo bộ hoặc nhiều món, và
câu hỏi còn treo trong đầu người mua là "có đủ không".

no:
Đừng dùng ở bất cứ chỗ nào trên `landing-page`, và `channels` của type này là thứ chặn điều đó.

Lý do: nó **bày ra chứ không làm gì thay đổi**, nên nó trượt phép thử mà một slot trên trang áp
dụng — lấy đồ ra khỏi hộp là để lộ cái vốn đã có, mà để lộ thì không được cấp chuyển động. Nó
vẫn tồn tại vì bên quảng cáo thật sự dùng màn mở hộp làm cú mở đầu, và đó là một việc khác.

vs:
Khác `use` ở một mốc rất rõ: ngay khi một bàn tay bắt đầu **thao tác** với món đồ thay vì trình
bày nó, loop đó thành `use`.

Type này mang `group: none` và `kind: null` — nó không tính vào sàn motion của trang nào, và
không bao giờ xuất hiện như một `gif.kind` trong bộ prompt đã định tuyến.
