# L (Local): Tìm trong hàm hiện tại trước. Có không? -> Có thì lấy.
# E (Enclosing): Không có ở Local? Tìm ra hàm cha (hàm bao bọc nó). Đây chính là nơi Decorator lấy func.
# G (Global): Không có ở cha? Tìm ra ngoài cùng file.
# B (Built-in): Không có ở file? Tìm trong thư viện gốc Python (len, print, str...).

def counter(func):
    count = 0 # Biến Enclosing
    def wrapper(*args, **kwargs):
        count = count + 1 # LỖI! Python tưởng bạn đang tạo biến Local 'count' mới
        print(f"Đã chạy {count} lần")
        return func(*args, **kwargs)
    return wrapper
# 👉 UnboundLocalError: local variable 'count' referenced before assignment

def counter(func):
    count = 0 
    def wrapper(*args, **kwargs):
        nonlocal count # Báo hiệu: "Tui muốn sửa biến count của hàm cha!"
        count += 1 
        print(f"Đã chạy {count} lần")
        return func(*args, **kwargs)
    return wrapper