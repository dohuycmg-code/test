import math # Import thư viện math để dùng số Pi (math.pi)

# 1. Định nghĩa một hàm để tính diện tích
def tinh_dien_tich_hinh_tron(ban_kinh):
    """
    Hàm tính diện tích hình tròn A = π * r^2
    """
    # math.pi là giá trị của Pi (~3.14159...)
    # ** 2 là phép toán lũy thừa (bán kính mũ 2)
    dien_tich = math.pi * (ban_kinh ** 2)
    return dien_tich

# 2. Khối lệnh chính để chạy chương trình
if __name__ == "__main__":
    print("--- Chương trình tính Diện tích Hình tròn ---")
    
    # Yêu cầu người dùng nhập bán kính
    try:
        ban_kinh_str = input("Vui lòng nhập bán kính hình tròn (số): ")
        
        # Chuyển đổi đầu vào (chuỗi) sang số thực (float)
        ban_kinh = float(ban_kinh_str)

        # Kiểm tra bán kính không âm
        if ban_kinh < 0:
            print("Lỗi: Bán kính không thể là số âm.")
        else:
            # Gọi hàm để tính toán
            ket_qua = tinh_dien_tich_hinh_tron(ban_kinh)
            
            # In kết quả, làm tròn đến 2 chữ số thập phân
            print(f"\nVới bán kính r = {ban_kinh},")
            print(f"Diện tích hình tròn là: {ket_qua:.2f}")
            
    except ValueError:
        print("Lỗi: Đầu vào không phải là một số hợp lệ.")
    except Exception as e:
        print(f"Đã xảy ra lỗi không xác định: {e}")