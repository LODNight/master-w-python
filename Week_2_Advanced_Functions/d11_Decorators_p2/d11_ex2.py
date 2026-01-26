# Dùng import time để đo thời gian.
# Dùng import functools và @functools.wraps để giữ nguyên tên hàm gốc (Metadata).
# Xử lý tham số *args, **kwargs để decorator không làm hỏng logic hàm gốc.
# In ra thời gian chạy với độ chính xác 4 số thập phân (VD: 0.0025s).

import time
import functools

def timer(func):
    """Decorator đo thời gian chạy của hàm"""   # docstring của hàm
    
    # TODO 1: Thêm dòng code để giữ nguyên tên và docstring của hàm gốc (Metadata)
    @functools.wraps(func)

    def wrapper(*args, **kwargs):
        # TODO 2: Lấy thời gian bắt đầu (biến start_time)
        start_time = time.time()
        
        # TODO 3: Gọi hàm gốc với đúng tham số và lưu kết quả vào biến result
        result = func(*args, **kwargs)

        # TODO 4: Lấy thời gian kết thúc (biến end_time)
        end_time = time.time()
        
        # TODO 5: Tính toán thời gian chạy và In ra màn hình
        # Mẫu in: "Hàm [Tên hàm] chạy mất [x.xxxx] giây"
        print(f"Hàm [{func.__name__}] chạy mất [{end_time - start_time:.4f}] giây")
        
        # TODO 6: Trả về kết quả gốc (result)
        return result

    return wrapper

# --- TEST CASE ---
@timer
def heavy_computation(n):
    """Hàm giả lập tính toán nặng"""    # docstring của hàm 
    print(f"🔄 Đang tính tổng bình phương của {n} số đầu tiên...")
    
    time.sleep(1)  # Giả vờ tính toán (ngủ 1 giây)
    return sum(i**2 for i in range(n))

# CHẠY THỬ
print("--- BẮT ĐẦU ---")
res = heavy_computation(500000)
print(f"✅ Kết quả trả về: {res}")

# KIỂM TRA METADATA
print("-" * 20)
print(f"Tên hàm thật là: {heavy_computation.__name__}") 