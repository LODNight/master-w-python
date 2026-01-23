# LEVEL 2: LOGIC & DATA HANDLING (Xử lý dữ liệu thực tế)
# Mục tiêu: Sử dụng Set, Dict và Unpacking linh hoạt.

# ====================================================
# Bài 3: Hệ thống phân quyền (*args & Set)
# Tình huống: Bạn viết hàm check_permission cho API.
# User có 1 tập quyền (VD: {'read', 'write'}).
# API yêu cầu một số quyền nhất định để chạy. Input:

user_perms = {'read', 'view_ads'}
# Hàm check:
def check_permission(user_perms, *required_perms):
    # Code của bạn ở đây...
    pass

# Yêu cầu:
# Hàm nhận vào user_perms và danh sách các quyền bắt buộc (*required_perms).
# Trả về True nếu user có TẤT CẢ các quyền yêu cầu. Ngược lại False.
# Gợi ý: Dùng set.issubset() hoặc phép trừ set. Test:
# check_permission(user_perms, 'read') -> True
# check_permission(user_perms, 'read', 'write') -> False (Thiếu write)



# ====================================================

# Bài 4: Cấu hình API đa tầng (**kwargs & Dict Merge)
# Tình huống: Gộp config theo thứ tự ưu tiên: Default < File Config < User Config. Input:

default = {'host': 'localhost', 'port': 8000, 'debug': False}
file_conf = {'port': 9090} # Config từ file ghi đè port

# Yêu cầu: Viết hàm start_server(**options):
# Hàm này nhận các tham số tùy chọn từ người dùng (User Config).
# Tạo ra biến final_config là sự kết hợp của default, file_conf và options (User truyền vào).
# Cái sau ghi đè cái trước.
# In ra: "Starting server at {host}:{port} (Debug: {debug})"