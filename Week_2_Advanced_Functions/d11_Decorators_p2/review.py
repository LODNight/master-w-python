

import functools

def my_decorator(func):
    # @functools.wraps là BẮT BUỘC để giữ nguyên tên và docstring của hàm gốc
    # Nếu không, hàm của bạn sẽ bị đổi tên thành "wrapper" -> Khó debug
    @functools.wraps(func)
    
    # *args, **kwargs: Chấp nhận MỌI loại tham số đầu vào
    def wrapper(*args, **kwargs):
        # 1. Code chạy TRƯỚC khi hàm gốc chạy (Logging, Check quyền...)
        print("--- Before ---")
        
        # 2. Gọi hàm gốc và lấy kết quả
        # Dùng * và ** để "bung" tham số ra (Kiến thức Ngày 9)
        result = func(*args, **kwargs)
        
        # 3. Code chạy SAU khi hàm gốc chạy (Đo thời gian, xử lý kết quả...)
        print("--- After ---")
        
        # 4. Trả về kết quả gốc (Đừng quên cái này!)
        return result
        
    return wrapper

# ❌ TRƯỜNG HỢP KHÔNG DÙNG @functools.wraps
def timer_bad(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Đây là docstring của Wrapper"""
        print("Đang chạy...")
        return func(*args, **kwargs)
    return wrapper

@timer_bad
def tinh_tong(a, b):
    """Hàm này dùng để tính tổng 2 số"""
    return a + b

# --- HẬU QUẢ ---
print("Tên hàm là:", tinh_tong.__name__) 
# 😱 Output: Tên hàm là: wrapper (Sai bét! Tên tui là tinh_tong mà?)

print("Hướng dẫn:", tinh_tong.__doc__)
# 😱 Output: Hướng dẫn: Đây là docstring của Wrapper (Mất luôn hướng dẫn gốc!)