# Tệp app.py tạo giao diện nhập dữ liệu, chạy thuật toán Gradient và hiển thị kết quả.
import tkinter as tk  # Nhập thư viện Tkinter để tạo giao diện cửa sổ.
from tkinter import ttk, messagebox  # Nhập các thành phần giao diện và hộp thoại thông báo.
import math  # Nhập thư viện toán học để kiểm tra dữ liệu số.
from gradient import gradient_descent, tao_ham_chi_phi  # Nhập thuật toán Gradient và hàm mục tiêu.

class UngDungGradient:  # Khai báo lớp quản lý ứng dụng Gradient.
    def __init__(self, cua_so):  # Khởi tạo giao diện chính của ứng dụng.
        self.cua_so = cua_so  # Lưu cửa sổ chính để sử dụng trong các phương thức.
        self.cua_so.title("Ứng dụng tối ưu hóa bậc nhất - Gradient")  # Đặt tên cửa sổ ứng dụng.
        self.cua_so.geometry("720x560")  # Đặt kích thước cửa sổ.
        self.cua_so.resizable(False, False)  # Không cho thay đổi kích thước để bố cục ổn định.
        self.tao_giao_dien()  # Gọi hàm tạo các thành phần giao diện.

    def tao_giao_dien(self):  # Tạo các ô nhập liệu, nút chạy và khu vực kết quả.
        khung = ttk.Frame(self.cua_so, padding=20)  # Tạo khung chứa toàn bộ nội dung.
        khung.pack(fill="both", expand=True)  # Đặt khung chiếm vùng hiển thị của cửa sổ.
        ttk.Label(khung, text="TỐI ƯU HÓA BẬC NHẤT - GRADIENT", font=("Arial", 16, "bold")).pack(pady=10)  # Hiển thị tên đề tài.
        ttk.Label(khung, text="Hàm mục tiêu: C(x) = a*x² + b*x + c", font=("Arial", 12)).pack(pady=5)  # Hiển thị hàm mục tiêu đang giải.
        nhom_nhap = ttk.LabelFrame(khung, text="INPUT - Dữ liệu đầu vào", padding=15)  # Tạo nhóm chứa các tham số đầu vào.
        nhom_nhap.pack(fill="x", pady=12)  # Đặt nhóm nhập liệu vào giao diện.
        self.cac_o_nhap = {}  # Tạo từ điển lưu các ô nhập theo tên tham số.
        cac_tham_so = [("a", "1"), ("b", "-20"), ("c", "150"), ("x₀", "0"), ("alpha", "0.1"), ("Số lần lặp", "100")]  # Khai báo tên và giá trị mặc định của các tham số.
        for chi_so, (ten, mac_dinh) in enumerate(cac_tham_so):  # Duyệt qua từng tham số để tạo nhãn và ô nhập.
            ttk.Label(nhom_nhap, text=ten + ":").grid(row=chi_so // 2, column=(chi_so % 2) * 2, sticky="w", padx=8, pady=9)  # Tạo nhãn cho tham số hiện tại.
            o_nhap = ttk.Entry(nhom_nhap, width=18)  # Tạo ô nhập giá trị cho tham số hiện tại.
            o_nhap.insert(0, mac_dinh)  # Điền giá trị mặc định vào ô nhập.
            o_nhap.grid(row=chi_so // 2, column=(chi_so % 2) * 2 + 1, sticky="w", padx=8, pady=9)  # Đặt ô nhập cạnh nhãn tương ứng.
            self.cac_o_nhap[ten] = o_nhap  # Lưu ô nhập vào từ điển để đọc dữ liệu khi chạy.
        ttk.Button(khung, text="CHẠY THUẬT TOÁN", command=self.chay_thuat_toan).pack(pady=12)  # Tạo nút để bắt đầu tính toán.
        ttk.Label(khung, text="Công thức cập nhật: x(k+1) = x(k) - alpha*C'(x(k))", font=("Arial", 11, "bold")).pack(pady=5)  # Hiển thị công thức cập nhật của Gradient.
        nhom_ket_qua = ttk.LabelFrame(khung, text="OUTPUT - Kết quả đầu ra", padding=15)  # Tạo nhóm hiển thị kết quả tính toán.
        nhom_ket_qua.pack(fill="both", expand=True, pady=10)  # Đặt nhóm kết quả và cho phép mở rộng.
        self.ket_qua = tk.StringVar(value="Nhập tham số và nhấn CHẠY THUẬT TOÁN để xem kết quả.")  # Tạo biến lưu nội dung kết quả.
        ttk.Label(nhom_ket_qua, textvariable=self.ket_qua, justify="left", wraplength=630, font=("Arial", 11)).pack(anchor="w", fill="x")  # Hiển thị kết quả trong giao diện.
        ttk.Label(khung, text="Mô hình hàm mục tiêu giả định dùng để minh họa thuật toán.", foreground="#555555").pack(pady=5)  # Ghi chú phạm vi của mô hình.

    def chay_thuat_toan(self):  # Đọc Input, kiểm tra dữ liệu và thực hiện thuật toán.
        try:  # Bắt đầu khối xử lý lỗi để ứng dụng không bị dừng đột ngột.
            a = float(self.cac_o_nhap["a"].get())  # Đọc hệ số bậc hai a.
            b = float(self.cac_o_nhap["b"].get())  # Đọc hệ số bậc nhất b.
            c = float(self.cac_o_nhap["c"].get())  # Đọc hằng số tự do c.
            x0 = float(self.cac_o_nhap["x₀"].get())  # Đọc nghiệm ban đầu x0.
            alpha = float(self.cac_o_nhap["alpha"].get())  # Đọc tốc độ học alpha.
            so_lan_lap = int(self.cac_o_nhap["Số lần lặp"].get())  # Đọc số lần lặp tối đa.
            if not all(math.isfinite(v) for v in (a, b, c, x0, alpha)):  # Kiểm tra các tham số số thực có hữu hạn hay không.
                raise ValueError("Các tham số phải là số hữu hạn.")  # Báo lỗi nếu có dữ liệu không hợp lệ.
            if a <= 0:  # Kiểm tra hệ số a để hàm bậc hai có cực tiểu.
                raise ValueError("Hệ số a phải lớn hơn 0.")  # Yêu cầu người dùng nhập a dương.
            if not 0 < alpha < 1 / a:  # Kiểm tra điều kiện đủ hội tụ của hàm bậc hai đang xét.
                raise ValueError(f"Alpha phải thỏa mãn 0 < alpha < {1 / a:.8f}.")  # Thông báo khoảng alpha phù hợp.
            ham, dao_ham = tao_ham_chi_phi(a, b, c)  # Tạo hàm mục tiêu và đạo hàm từ các hệ số.
            nghiem, gia_tri_ham, lich_su = gradient_descent(ham, dao_ham, x0, alpha, so_lan_lap)  # Chạy thuật toán Gradient Descent.
            so_buoc = len(lich_su) - 1  # Tính số bước cập nhật đã thực hiện.
            self.ket_qua.set(f"Kết quả tối ưu gần đúng:\nNghiệm x = {nghiem:.10f}\nGiá trị hàm C(x) = {gia_tri_ham:.10f}\nSố bước lặp đã thực hiện = {so_buoc}")  # Hiển thị các kết quả đầu ra chính.
        except (ValueError, OverflowError, ZeroDivisionError) as loi:  # Bắt lỗi nhập liệu hoặc lỗi tính toán.
            messagebox.showerror("Dữ liệu không hợp lệ", str(loi))  # Hiển thị nội dung lỗi để người dùng điều chỉnh.

if __name__ == "__main__":  # Kiểm tra tệp có được chạy trực tiếp hay không.
    cua_so = tk.Tk()  # Tạo cửa sổ ứng dụng Tkinter.
    ung_dung = UngDungGradient(cua_so)  # Khởi tạo ứng dụng trên cửa sổ vừa tạo.
    cua_so.mainloop()  # Bắt đầu vòng lặp giao diện để nhận thao tác người dùng.
