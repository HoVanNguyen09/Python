# Chương 1 - Phương thức của chương trình
Mục tiêu của cuốn sách này là dạy bạn tư duy như một Nhà khoa học máy tính. Phương pháp tư duy này kết hợp những điểm tốt nhất giữa toán học, kỹ thuật và khoa học tự nhiên. Giống như những nhà toán học, các nhà khoa học máy tính sử dụng ngôn ngữ chính thức để chứng tỏ các ý tưởng của họ (cụ thể là các phép tính). Như các kỹ sư, họ thiết kế nhiều thứ, tập hợp các linh kiện thành các hệ thống và đánh giá sự được mất giữa các lựa chọn khác nhau. Như các nhà khoa học, họ quan sát hành vi của các hệ thống phức tạp, tạo ra các giả thuyết và kiểm chứng các tiên đoán. Kỹ năng quan trọng nhất đối với một Nhà khoa học máy tính là giải quyết vấn đề. Kỹ năng giải quyết vấn đề là khả năng công thức hóa các vấn đề, nghĩ một cách sáng tạo về các giải pháp, và trình bày giải pháp một cách rõ ràng và chính xác. Thật ra, quá trình học lập trình là một cơ hội tuyệt vời để luyện tập kỹ năng giải quyết vấn đề. Đó là lý do tại sao chương sách này có tên là: “Phương thức của một chương trình”. Ở một cấp độ, bạn sẽ được học lập trình, một kỹ năng mà bản thân nó đã hữu ích. Ở một cấp độ khác, bạn sẽ sử dụng lập trình như một phương thức để đạt được mục đích. Trong quá trình ta học cùng nhau, mục đích đó sẽ trở nên rõ ràng hơn.

## 1. Một chương trình là gì?
Một chương trình là một chuỗi những câu lệnh (hay hướng dẫn) chỉ rõ cách thực hiện một phép tính. Phép tính đó có thể là một điều gì đó mang tính toán học, như là giải quyết một hệ phương trình hoặc là tìm nghiệm của một đa thức, nhưng cũng có thể là một phép tính biểu tượng, như là tìm kiếm và thay thế đoạn ký tự trong một văn bản hay thứ gì đó mang tính đồ họa, như xử lý một hình ảnh hay chạy một đoạn video. Các chi tiết trông khác nhau tùy vào ngôn ngữ khác nhau, nhưng các câu lệnh hướng dẫn cơ bản xuất hiện trong hầu như tất cả mọi ngôn ngữ:

- Đầu vào: Lấy dữ liệu từ bàn phím, từ một file, từ một mạng, hay từ một số thiết bị khác.
Đầu ra: Hiển thị dữ liệu trên màn hình, lưu vào trong một file, gửi qua mạng…
- Toán học: Thực hiện các phép toán cơ bản như cộng và nhân.
Xử lý có điều kiện: Kiểm tra một số điều kiện nhất định và chạy đoạn mã phù hợp.
- Lặp lại: Thực hiện một số hành động lặp đi lặp lại, thường là với sự biến đổi.
Tin hay không, tất cả chỉ có vậy. Mọi chương trình chúng ta từng sử dụng, cho dù phức tạp đến thế nào, đều được tạo nên từ các câu lệnh trông như vậy. Vậy nên bạn có thể nghĩ về lập trình như một quy trình chia nhỏ một tác vụ lớn, phức tạp thành các tác vụ phụ nhỏ hơn và nhỏ hơn nữa cho đến khi các tác vụ phụ đã đủ đơn giản để được thực hiện với những câu lệnh hướng dẫn cơ bản này.

## 2. Vận hành Python
Một trong những thách thức của việc bắt đầu với Python là bạn có thể phải cài đặt Python và các phần mềm liên quan trên máy tính của bạn. Nếu như bạn quen thuộc với hệ điều hành của bạn, và đặc biệt nếu như bạn thoải mái với giao diện theo dòng lệnh, bạn sẽ không gặp vấn đề gì trong việc cài đặt Python. Nhưng cho người mới bắt đầu, sẽ rất khó khăn để học về quản trị hệ thống và lập trình cùng một lúc.

Để tránh vấn đề đó, tôi đề xuất bạn bắt đầu chạy Python trong một trình duyệt Internet. Sau đó, khi bạn đã quen với Python, tôi sẽ tạo ra những đề xuất để cài đặt Python trên máy tính của bạn.

Có một số trang web bạn có thể dùng để chạy Python. Nếu như bạn đã có trang ưa thích, cứ thoải mái sử dụng nó. Nếu không tôi xin giới thiệu PythonAnywhere. Tôi cung cấp hướng dẫn chi tiết để bắt đầu tại đường dẫn http://tinyurl.com/thinkpython2e.

Có 2 phiên bản Python, có tên là Python 2 và Python 3. Chúng rất giống nhau, nên nếu bạn đã học một phiên bản trước đó, sẽ rất dễ để chuyển sang phiên bản khác. Thật ra, chỉ có một vài điểm khác biệt mà bạn sẽ tiếp xúc với tư cách là một người bắt đầu. Cuốn sách này được viết cho Python 3, nhưng tôi sẽ thêm một số ghi chú về Python 2.

Chương trình thông dịch Python là một chương trình đọc và thực thi các mã lệnh Python. Tùy vào môi trường của bạn, bạn có thể khởi động chương trình thông dịch bằng cách nhấp chuột vào biểu tượng, hoặc gõ python3 - dòng lệnh Terminal hay python - dòng lệnh CMD. Khi nó khởi động, bạn sẽ thấy kết quả hiển thị như sau:
`Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>`
Ba dòng đầu tiên chứa thông tin về chương trình thông dịch và hệ điều hành mà đang chạy chương trình này, vì vậy nó có thể khác đối với bạn. Nhưng bạn nên kiểm tra xem số phiên bản, ví dụ như 3.11.0, bắt đầu với số 3, nghĩa là bạn đang chạy Python 3. Nếu nó bắt đầu với số 2, nghĩa là bạn đang chạy Python 2.

Dòng cuối cùng là dòng nhập lệnh nghĩa là chương trình thông dịch này sẵn sang cho bạn nhập mã (code). Nếu bạn gõ một dòng lệnh và nhấn enter, trình thông dịch hiển thị kết quả:

>>> 1 + 1
2
Bây giờ bạn đã sẵn sàng để bắt đầu. Từ giờ trở đi, tôi mặc định rằng bạn biết cách khởi động chương trình thông dịch Python và chạy code.

## 3. Chương trình đầu tiên
Theo truyền thống, chương trình đầu tiên các bạn viết bằng một ngôn ngữ mới gọi là Hello, World! vì tất cả những gì nó làm là hiển thị các từ Hello, World! ra ngoài màn hình. Trong Python, nó sẽ trông như thế này:

>>> print ('Hello, World!')
Đây là một ví dụ của một câu lệnh print – in ra, mặc dù nó không thật sự in thứ gì lên trên giấy cả. Nó hiển thị kết quả lên màn hình. Trong trường hợp này, kết quả là chuỗi từ Hello, World!

Dấu ngoặc đơn () trong chương trình đánh dấu sự bắt đầu và kết thúc của chuỗi cần được hiển thị, chúng sẽ không xuất hiện trong kết quả.

Dấu ngoặc đơn xác định rằng print là một hàm. Chúng ta sẽ học về hàm trong chương 3.

Trong Python 2, câu lệnh print có khác hơn một chút; nó không phải là một hàm, cho nên nó không dùng dấu ngoặc đơn.

>>>print 'Hello, World'
Sự khác biệt này sẽ sớm được giải thích hợp lý, nhưng khởi đầu như vậy là đủ.

## 4. Các phép toán tử
Sau Hello, World, bước tiếp theo là các phép toán tử. Python cung cấp các phương thức tính toán, gồm những ký tự đặc biệt đại diện cho các phép tính như cộng và nhân.

Các dấu +,- và * biểu diễn phép cộng, trừ, và nhân, như trong các ví dụ sau đây:

>>> 40 + 2
42
>>> 43 - 1
42
>>> 6 * 7
42
Dấu / thực hiện phép chia:

>>> 84 / 2
42.0
Bạn sẽ tự hỏi tại sao kết quả lại là 42.0 thay vì 42. Tôi sẽ giải thích ở phần sau. Sau cùng, dấu ** thực hiện phép lũy thừa; đó là nâng một số theo một cấp mũ của nó:
>>> 6 ** 2 + 6
42
Trong một số ngôn ngữ khác, ký hiệu ^ được sử dụng cho phép tính lũy thừa, nhưng trong Python nó lại là phép tính dạng bit gọi là XOR. Nếu như bạn không quen với các phép toán dạng bit, kết quả sẽ làm bạn ngạc nhiên:

>>> 6 ^ 2
4
Tôi sẽ không đề cập dến các phép tính dạng bit trong cuốn sách này, nhưng bạn có thể đọc về chúng tại: http://wiki.python.org/moin/BitwiseOperators

## 5. Các giá trị và kiểu dữ liệu
Một giá trị là một trong những điều cơ bản mà chương trình làm việc với, như là chữ hay là số. Một số giá trị chúng ta đã thấy cho đến giờ là 2, 42.0, và Hello, World!.

Những giá trị này thuộc về nhiều kiểu dữ liệu khác nhau: 2 là số nguyên, 42.0 là số thập phân, và Hello, World! là kiểu chuỗi, gọi như vậy là vì các chữ mà nó chứa được xâu chuỗi với nhau.

Nếu như bạn không rõ giá trị thuộc kiểu nào, chương trình thông dịch có thể nói với bạn:

>>> type(2)
<class 'int'>
>>> type(42.0)
<class 'float'>
>>> type("Hello, World!")
<class 'str'>
Trong những kết quả này, từ lớp hay class được dùng như một cách phân loại, một kiểu là một loại giá trị. Không ngạc nhiên, số nguyên thuộc loại int, chuỗi thuộc loại str và số thập phân thuộc loại float. Vậy còn các giá trị như 2 và 42.0 thì sao? Chúng trông như số nhưng là lại nằm trong dấu ngoặc đơn như kiểu chuỗi.

>>> type('2')
<class 'str'>
>>> type('42.0')
<class 'str'>
=> Chúng là kiểu chuổi.

Khi bạn gõ một số nguyên lớn, bạn sẽ khó cưỡng lại việc dùng dấu phẩy (,) để phân cách các nhóm số với nhau, ví dụ như 1,000,000. Đây không phải là một số nguyên hợp lệ trong Python, nhưng lại hợp lệ theo kiểu khác:

>>> 1,000,000
(1, 0, 0)
Đây không phải là điều mà chúng ta mong muốn! Python hiểu và thông dịch 1,000,000 là một chuỗi số nguyên phân cách bởi các dấu phẩy. Chúng ta sẽ học về kiểu chuỗi như vậy sau này.

## 6. Ngôn ngữ chính thức và ngôn ngữ tự nhiên
Những ngôn ngữ tự nhiên là những ngôn ngữ mà con người dùng để nói như tiếng Anh, Tây Ban Nha và Pháp. Chúng không được thiết kế bởi con người (mặc dù một số người cố áp đặt trật tự lên chúng); chúng tiến hóa một cách tự nhiên.

Những ngôn ngữ chính thức là những ngôn ngữ được thiết kế bởi con người cho những ứng dụng nhất định. Ví dụ, các ghi chú mà các nhà toán học sử dụng là một ngôn ngữ chính thức rất tốt trong việc ghi lại mối quan hệ giữa các con số và các dấu. Các nhà hóa học sử dụng ngôn ngữ chính thức để ghi đại diện cho các cấu trúc hóa học của các phân tử. Và quan trọng nhất là:

Ngôn ngữ lập trình là ngôn ngữ chính thức được thiết kế để diễn giải các phép tính toán.
Ngôn ngữ chính thức thường có những quy tắc cú pháp để quy định cấu trúc của các câu. Ví dụ, trong toán học, câu 3 + 3 = 6 có cú pháp chính xác nhưng 3+ = 3$6 thì không. Trong hóa học, [H_2O] là một công thức đúng cú pháp nhưng [_2Zz] thì không.

Các quy tắc cú pháp thường đến theo hai dạng, ký tự và cấu trúc. Ký tự là những yếu tố cơ bản của ngôn ngữ, như là từ ngữ, số, và các nguyên tố hóa học. Một trong những vấn đề của 3+ = 3$6 là dấu $ không phải là một ký tự hợp pháp trong toán học (theo như tôi được biết). Tương tự, [_2ZZ] không hợp pháp vì không có nguyên tố hóa học nào được viết tắt bằng 2 chữ Zz. Loại luật cú pháp thứ hai dựa trên cách mà các yếu tố được kết hợp. Phương trình 3 + /3 không hợp lệ vì dù + và / là ký tự hợp lệ, bạn không thể có dấu này ngay sau dấu kia. Tương tự, trong công thức hóa học, số của nguyên tố đi sau tên của nguyên tố, không phải trước.

Đây là một câu tiếng @nh có cấu trúc hợp lệ với ký t# không hợp lệ trong nó. Câu này có các ký tự hợp lệ, nhưng cấu trúc lại không hợp lệ.

Khi bạn đọc một câu trong tiếng Anh hoặc một câu trong một ngôn ngữ chính thức, bạn phải đoán ra được cấu trúc (mặc dù trong ngôn ngữ tự nhiên bạn vô thức làm điều đó). Quá trình này gọi là phân tích cú pháp.

Mặc dù ngôn ngữ chính thức và ngôn ngữ tự nhiên có nhiều đặc điểm chung, như ký tự, cấu trúc và cú pháp, nhưng cũng có một số điểm khác nhau:

Sự mơ hồ: Các ngôn ngữ tự nhiên chứa nhiều sự mơ hồ mà con người thường đối phó bằng cách sử dụng các manh mối nội dung của bối cảnh và các thông tin khác. Ngôn ngữ chính thức được thiết kế để trở nên gần như hoặc hoàn toàn rõ ràng, không mơ hồ, nghĩa là bất kỳ câu nào chỉ có một ý nghĩa, bất kể bối cảnh nào.

Sự dư thừa: Để làm rõ cho sự mơ hồ và giảm hiểu lầm, ngôn ngữ tự nhiên sử dụng rất nhiều sự dư thừa. Kết quả, chúng thường dài dòng. Ngôn ngữ chính thức thường ít dư thừa và ngắn gọn hơn.

Sự đúng nghĩa: Ngôn ngữ tự nhiên thường có rất nhiều thành ngữ, tục ngữ và ẩn dụ. Nếu như tôi nói “Đồng tiền rơi xuống - The penny dropped”, thì chưa chắc là đã có đồng tiền và không có gì rơi xuống (câu thành ngữ này để chỉ việc một người đã hiểu điều gì đó sau một thời gian nhầm lẫn). Các ngôn ngữ chính thức có nghĩa chính xác những gì mà chúng đề cập.

Vì chúng ta lớn lên với ngôn ngữ tự nhiên, đôi khi sẽ rất khó để làm quen với ngôn ngữ chính thức. Sự khác biệt giữa ngôn ngữ chính thức và ngôn ngữ tự nhiên giống như sự khác biệt giữa thơ ca và văn xuôi, nhưng hơn thế:

Thơ ca: Các từ ngữ được dùng vì âm điệu cũng như ý nghĩa của chúng, và cả bài thơ kết hợp lại tạo ra một hiệu ứng hoặc phản ứng cảm xúc. Sự mơ hồ không chỉ phổ biến mà còn thường được cố ý thêm vào.

Văn xuôi: Nghĩa đen của từ ngữ quan trọng hơn, và cấu trúc đóng góp nhiều cho ý nghĩa. Văn xuôi thường dễ dàng để phân tích hơn thơ ca nhưng vẫn thường mơ hồ.

Chương trình: Ý nghĩa của một chương trình máy tính là không mơ hồ và sát nghĩa, và có thể được hiểu hoàn toàn bằng việc phân tích các ký tự và cấu trúc.

Ngôn ngữ chính thức thường dày đặc hơn ngôn ngữ tự nhiên, vì thế cũng mất nhiều thời gian hơn để đọc chúng. Hơn nữa, cấu trúc thì quan trọng, cho nên việc đọc từ trên xuống dưới, trái sang phải không phải lúc nào cũng tốt nhất. Thay vào đó, hãy học cách phân tích cú pháp chương trình trong đầu bạn, xác định các chương trình và thông dịch cấu trúc. Cuối cùng, các chi tiết rất quan trọng. Các lỗi nhỏ trong đánh vần và chấm phẩy, mà bạn có thể bỏ qua trong ngôn ngữ tự nhiên, có thể tạo sự khác biệt lớn trong ngôn ngữ chính thức.

## 7. Gỡ lỗi
Các lập trình viên mắc lỗi vì những lý do bất thường, những lỗi lập trình gọi là con bọ hay là bug và quy trình tìm các lỗi gọi là gỡ lỗi hay là debug.

Lập trình, đặc biệt là debug, đôi khi mang đến những cảm xúc mạnh mẽ. Nếu như bạn đang vật lộn với một bug khó, bạn có thể cảm thấy tức giận, chán nản, hoặc xấu hổ.

Có bằng chứng rằng con người trả lời tự nhiên với máy tính giống như chúng là con người. Khi chúng làm việc hiệu quả, ta nghĩ về chúng như đồng đội, và khi chúng cứng đầu hoặc thô lỗ, ta đáp lại chúng như cái cách mà ta đáp lại người cứng đầu, thô lỗ.

Chuẩn bị cho những phản ứng này có thể giúp ta đối phó với chúng. Một cách tiếp cận là nghĩ về máy tính như một nhân viên với một số thế mạnh nhất định, như tốc độ và sự chính xác, và điểm yếu nhất định, như sự vô cảm và không có khả năng nắm được bức tranh tổng quát.

Công việc của bạn là trở thành một nhà quản lý tốt: Tìm ra các cách để tận dụng điểm mạnh và hạn chế điểm yếu. Và tìm các cách sử dụng cảm xúc để kết nối với vấn đề, mà không để phản ứng của bạn can thiệp vào khả năng làm việc hiệu quả.

Học debug có thể làm nản lòng, nhưng đó là một kỹ năng quý giá mà hữu dụng cho nhiều hoạt động trên cả lập trình. Ở cuối mỗi chương có một đoạn, như đoạn này, với đề xuất của tôi cho debug. Tôi hy vọng chúng sẽ giúp được bạn!

## 8. Thuật ngữ
- problem solving – giải quyết vấn đề: Quy trình công thức hóa một vấn đề, tìm ra giải pháp và diễn giải nó.

- high-level language – ngôn ngữ cấp cao: Một ngôn ngữ lập trình như Python được thiết kế để trở nên dễ đọc và viết cho con người.

- low-level language – ngôn ngữ cấp thấp: Một ngôn ngữ lập trình được thiết kế để trở nên dễ dàng cho máy tính vận hành; còn được gọi là “ngôn ngữ máy” hay “ngôn ngữ tập hợp” (“assembly language”).

- portability – tính di động: Một tính chất của một chương trình mà có thể chạy trên hơn một loại máy tính.

- interpreter – trình thông dịch: Một chương trình mà đọc một chương trình khác và xử lý nó.

- prompt – lời nhắc: Các ký tự hiển thị bởi trình thông dịch để gợi ý rằng nó đã sẵn sàng để lấy thông tin đầu vào từ người dùng. Đối với chương trình Python là >>>

- program – chương trình: Một tập hợp các lệnh đặc tả một phép tính.

- print statement – lệnh in: Một mệnh lệnh khiến cho trình thông dịch Python hiển thị một giá trị lên màn hình của bạn.

- operator – toán tử: Một ký tự đặc biệt đại diện cho một phép tính đơn giản như cộng, nhân hay nối chuỗi...

- value – giá trị: Một trong những đơn vị cơ bản của dữ liệu, như một số hay một chuỗi mà chương trình điều khiển.

- type – kiểu dữ liệu: Là một loại dữ liệu. Các kiểu dữ liệu mà chúng ta thấy tới nay là số nguyên (int), số thập phân (float), và kiểu chuỗi (str).

- integer – số nguyên: Một kiểu dữ liệu mà đại diện cho số nguyên.

- floating-point - số thập phân: Một kiểu dữ liệu đại diện cho các số với các phần số thập phân.

- string – chuỗi: Một kiểu dữ liệu đại diện một chuỗi các ký tự.

- natural language – ngôn ngữ tự nhiên: Bất kỳ ngôn ngữ nào mà con người nói, tiến hóa một cách tự nhiên.

- formal language – ngôn ngữ chính thức: Bất kỳ ngôn ngữ nào mà con người thiết kế vì một mục đích cụ thể, ví dụ như biểu diễn các ý tưởng toán học hoặc các chương trình máy tính; tất cả các ngôn ngữ lập trình đều là ngôn ngữ chính thức.

- token – đơn vị mã hóa: Một trong những yếu tố cơ bản của cấu trúc cú pháp của một chương trình, tương đương với từ trong ngôn ngữ tự nhiên.

- syntax – cú pháp: Những quy tắc quản lý cấu trúc của một chương trình.

- parse – phân tích cú pháp: Kiểm tra một chương trình và phân tích cấu trúc cú pháp của nó.

- bug – lỗi: Một lỗi của một chương trình máy tính.

- debugging – gỡ lỗi: Quá trình tìm và sửa lỗi.

## 9. Bài tập
### Bài tập 1:
Sẽ là một ý kiến rất hay khi bạn đọc cuốn sách này trước một máy tính để bạn có thể thử hết các ví dụ:

1. Khi nào mà bạn thử nghiệm với các tính năng mới, bạn nên thử mắc lỗi. Ví dụ, trong chương trình “Hello, world!, chuyện gì xảy ra nếu bạn bỏ một dấu nháy đôi đi? Chuyện gì xảy ra nếu bạn bỏ cả hai dấu nháy đôi? Chuyện gì xảy ra nếu bạn gõ lệnh `print` sai?
2. Những thử nghiệm như thế này giúp bạn nhớ những gì bạn đã đọc, nó cũng giúp khi bạn lập trình, vì bạn sẽ biết được ý nghĩa của tin nhắn lỗi như thế nào. Sẽ tốt hơn cho bạn nếu bạn mắc lỗi bây giờ và có mục đích hơn là sau này và vô ý.
3. Trong câu lệnh `print`, chuyện gì xảy ra nếu bạn bỏ một dấu ngoặc đơn hoặc là cả hai?
4. Nếu như bạn đang cố in ra một chuỗi, chuyện gì xảy ra nếu như bạn bỏ một dấu nháy, hoặc cả hai?
5.Bạn có thể dùng dấu trừ `(-)` để tạo một số âm như `-2`. Chuyện gì xảy ra nếu bạn bỏ dấu cộng `(+)` trước một số? Phép tính `2++2` thì sao?
6. Trong ghi chú toán học, số 0 đứng đầu thì ổn, vì dụ như `09`. Chuyện gì xảy ra nếu bạn thử gõ như vậy trong Python? `011` thì sao?
7. Chuyện gì xảy ra nếu bạn có hai giá trị mà không có phép tính ở giữa chúng?
### Bài tập 2:
Khởi động trình thông dịch Python và dùng nó như một máy tính để thực hiện các yêu cầu sau đây:

1. Có bao nhiêu giây trong 42 phút 42 giây?
2. Có bao nhiêu dặm (miles) trong 10 km? Gợi ý: Một dặm tương đương 1.61 km.
3. Nếu như bạn chạy trong một cuộc đua 10 km trong thời gian là 42 phút 42 giây, thì vận tốc trung bình của bạn (tức là thời gian cho một dặm tính bằng phút và giây) là bao nhiêu? Tốc độ trung bình của bạn tính bằng dặm/giờ là bao nhiêu?
Chú ý: Khi bạn đã tự hoàn thành các bài tập bên trên, bạn có thể truy cập vào thư mục Đáp án để xem [đáp án](https://bitbucket.org/tanhuynhng/thinking-python/src/master/%C4%90%C3%A1p%20%C3%A1n/).
