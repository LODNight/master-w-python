# Tình huống: Hệ thống gửi Email đôi khi bị lỗi mạng. 
# Sếp yêu cầu: "Nếu gửi lỗi, hãy tự động thử lại 3 lần trước khi báo thất bại."

# Yêu cầu: Viết Decorator @retry(times=...) để bọc hàm send_email.

import functools
def retry(times):
    print(f"Bắt đầu gửi mail...")

    def decorate_retry(func):
        @functools.wraps(func)

        def wrapper(*args, **kwargs):
            print(f"\n--- Bắt đầu cơ chế Retry ({times} lần) ---")
            for i in range(times):
                try:
                    print(f"Lần thử thứ [{i+1}]...")
                    result = func(*args, **kwargs)
                    if result:
                        return result
                except Exception as e: 
                    print(f"⚠️ Lỗi: {e}. Đang thử lại")
                
            
            print(f"❌ Đã thử hết {times} lần mà vẫn lỗi")
            return None
        
        return wrapper
    return decorate_retry 


# -- TEST -- 
@retry(times=3)
def connect_database():
    import random 
    if random.choice([True, False, False]): # 66% Tỉ lệ lỗi
        print("❌ Kết nối thất bại")
        raise ConnectionError("Mất mạng")
    print("✅ Kết nối thành công")
    return "OK"


# Test
connect_database()