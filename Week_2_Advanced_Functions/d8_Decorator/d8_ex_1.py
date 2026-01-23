import time

# 1. Viết Decorator
def timer(func):
    """Decorator đo thời gian chạy của hàm"""
    def wrapper(*args, **kwargs):
        # Bắt đầu lấy thời gian
        start = time.time()

        result = func(*args, **kwargs)
        
        # Kết thúc thời gian
        end = time.time()
        
        execution_time = end- start
        
        # Format :.4f để lấy 4 số lẻ
        print(f"--- LOG: Ham {func.__name__} chay mat {execution_time:.3f} giay ---")
        
        return result
    return wrapper

# 2. Áp dụng vào hàm LMS
@timer
def calculate_gpa(student_ids):
    print(f"Đang tính điểm cho {len(student_ids)} học sinh...")
    # Giả vờ tính toán lâu (ngủ 1 giây)
    time.sleep(1.5) 
    return "Xong!"

# 3. Chạy thử
calculate_gpa(["SV01", "SV02", "SV03"])