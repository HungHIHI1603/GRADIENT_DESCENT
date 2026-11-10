# Tệp này cài đặt thuật toán Gradient Descent dùng để tìm giá trị nhỏ nhất của hàm một biến.
from typing import Callable, List, Tuple  # Nhập kiểu dữ liệu để mô tả hàm, danh sách và kiểu kết quả.
import math  # Nhập thư viện toán học để kiểm tra giá trị số và phát hiện trường hợp không hợp lệ.

def gradient_descent(  # Khai báo hàm tối ưu bằng phương pháp Gradient Descent.
    ham: Callable[[float], float],  # Nhận hàm mục tiêu C(x) cần tối thiểu hóa.
    dao_ham: Callable[[float], float],  # Nhận đạo hàm C'(x) của hàm mục tiêu.
    x0: float,  # Nhận nghiệm ban đầu x₀.
    alpha: float,  # Nhận tốc độ học α dùng để điều chỉnh độ dài bước cập nhật.
    so_lan_lap: int = 100,  # Đặt số lần lặp tối đa, mặc định là 100.
    epsilon: float = 1e-8,  # Đặt ngưỡng dừng khi độ lớn đạo hàm đủ nhỏ.
) -> Tuple[float, float, List[dict]]:  # Khai báo kết quả gồm nghiệm cuối, giá trị hàm và lịch sử từng bước.
    if not math.isfinite(x0):  # Kiểm tra nghiệm ban đầu có phải số hữu hạn hay không.
        raise ValueError("Nghiệm ban đầu phải là số hữu hạn.")  # Báo lỗi nếu nghiệm ban đầu không hợp lệ.
    if not math.isfinite(alpha) or alpha <= 0:  # Kiểm tra tốc độ học là số hữu hạn và dương.
        raise ValueError("Tốc độ học alpha phải là số hữu hạn lớn hơn 0.")  # Báo lỗi nếu tốc độ học không hợp lệ.
    if not isinstance(so_lan_lap, int) or so_lan_lap <= 0:  # Kiểm tra số lần lặp là số nguyên dương.
        raise ValueError("Số lần lặp phải là số nguyên dương.")  # Báo lỗi nếu số lần lặp không hợp lệ.
    x = float(x0)  # Chuyển nghiệm ban đầu thành số thực để tính toán.
    lich_su = []  # Tạo danh sách lưu thông tin của từng bước.
    for buoc in range(so_lan_lap + 1):  # Duyệt từ bước 0 đến bước tối đa.
        gia_tri = float(ham(x))  # Tính giá trị hàm mục tiêu tại nghiệm hiện tại.
        gradient = float(dao_ham(x))  # Tính đạo hàm tại nghiệm hiện tại.
        if not math.isfinite(gia_tri) or not math.isfinite(gradient):  # Kiểm tra kết quả hàm và đạo hàm có hữu hạn không.
            raise ValueError("Hàm mục tiêu hoặc đạo hàm tạo ra giá trị không hữu hạn; hãy đổi tham số.")  # Báo lỗi khi phép tính vượt giới hạn số.
        lich_su.append({"buoc": buoc, "x": x, "f_x": gia_tri, "dao_ham": gradient})  # Lưu bước lặp, nghiệm, giá trị hàm và đạo hàm.
        if abs(gradient) < epsilon:  # Kiểm tra đạo hàm có đủ gần 0 để dừng hay chưa.
            break  # Kết thúc vòng lặp khi đã đạt tiêu chí dừng.
        if buoc == so_lan_lap:  # Kiểm tra đã tới số lần lặp tối đa hay chưa.
            break  # Dừng cập nhật nếu đã dùng hết số lần lặp.
        x_moi = x - alpha * gradient  # Tính nghiệm mới theo công thức x(k+1) = x(k) - alpha*f'(x(k)).
        if not math.isfinite(x_moi):  # Kiểm tra nghiệm mới có vượt giới hạn biểu diễn số hay không.
            raise ValueError("Nghiệm bị tràn số; hãy giảm tốc độ học alpha.")  # Báo lỗi và hướng dẫn giảm tốc độ học.
        x = x_moi  # Cập nhật nghiệm hiện tại bằng nghiệm mới.
    return x, float(ham(x)), lich_su  # Trả về nghiệm cuối, giá trị hàm tại nghiệm cuối và lịch sử.

def tao_ham_chi_phi(he_so_bac_hai: float, he_so_bac_nhat: float, hang_so: float):  # Tạo hàm bậc hai theo các hệ số người dùng cung cấp.
    def chi_phi(x: float) -> float:  # Khai báo hàm chi phí C(x).
        return he_so_bac_hai * x ** 2 + he_so_bac_nhat * x + hang_so  # Tính C(x) = a*x^2 + b*x + c.
    def dao_ham_chi_phi(x: float) -> float:  # Khai báo đạo hàm của hàm chi phí.
        return 2 * he_so_bac_hai * x + he_so_bac_nhat  # Tính C'(x) = 2*a*x + b.
    return chi_phi, dao_ham_chi_phi  # Trả về hàm chi phí và đạo hàm để thuật toán sử dụng.
