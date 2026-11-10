ĐỒ ÁN NHẬP MÔN TỐI ƯU HÓA – HK261
ĐỀ TÀI SỐ 1: TÌM HIỂU VÀ CÀI ĐẶT ỨNG DỤNG BÀI TOÁN TỐI ƯU HÓA BẬC NHẤT – GRADIENT

1. MỤC TIÊU
Cài đặt ứng dụng minh họa thuật toán Gradient để tìm giá trị nhỏ nhất của hàm mục tiêu một biến. Chương trình có Input, Output và các bước tính toán chính.

2. CẤU TRÚC
- app.py: giao diện nhập dữ liệu, chạy thuật toán và hiển thị kết quả.
- gradient.py: hàm mục tiêu, đạo hàm và thuật toán Gradient Descent.
- BAO_CAO_DO_AN_GRADIENT_DESCENT.docx: báo cáo đồ án.
- DE_CUONG_BAO_VE.txt: nội dung chuẩn bị báo cáo và bảo vệ.
- requirements.txt: thông tin thư viện.

3. CÁCH CHẠY
- Giải nén ZIP.
- Mở thư mục dự án, nhập cmd vào thanh địa chỉ File Explorer.
- Kiểm tra Python: python --version
- Chạy: python app.py (hoặc py app.py)
- Ứng dụng dùng Tkinter có sẵn trong Python, không cần API và không cần cài gói pip ngoài.

4. INPUT
Hàm mục tiêu: C(x)=a*x^2+b*x+c, với a>0.
- a: hệ số bậc hai.
- b: hệ số bậc nhất.
- c: hằng số tự do.
- x0: nghiệm ban đầu.
- alpha: tốc độ học, với mô hình bậc hai này chọn 0<alpha<1/a.
- Số lần lặp: số bước cập nhật tối đa.

5. BỘ THAM SỐ ĐỂ CHẠY THỬ
a=1; b=-20; c=150; x0=0; alpha=0.1; số lần lặp=100.
Hàm: C(x)=x^2-20*x+150.
Đạo hàm: C'(x)=2*x-20.
Nghiệm cực tiểu lý thuyết: x*=10; C(x*)=50.

6. OUTPUT
Chương trình hiển thị nghiệm gần tối ưu, giá trị hàm tại nghiệm và số bước lặp đã thực hiện.

7. LƯU Ý
Đây là mô hình hàm mục tiêu giả định dùng để minh họa phương pháp, không phải dữ liệu doanh nghiệp thực tế.
Tất cả dòng lệnh trong app.py và gradient.py có chú thích tiếng Việt giải thích tác dụng.
