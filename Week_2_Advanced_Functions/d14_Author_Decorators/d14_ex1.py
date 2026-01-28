# Tình huống Dự án LMS: Bạn cần bảo vệ các hàm nhạy cảm.
# update_score: Chỉ dành cho 'teacher'.
# delete_student: Chỉ dành cho 'admin'.
# User hiện tại đang là 'teacher'.

# Yêu cầu: Hoàn thiện Decorator @check_permission bên dưới.

import functools

# Giả lập User hiện tại (Đang là giáo viên)
current_user = {"username": "thay_ba", "role": "teacher"}

def check_permission(required_role):
    # Lớp 1: Nhận role yêu cầu (VD: 'admin')
    def decorator(func):
        # Lớp 2: Nhận hàm gốc
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Lớp 3: Logic kiểm tra
            
            # Lấy role của current_user
            user_role = current_user["role"]
            
            # Nếu user_role bằng required_role:
            if user_role == required_role:
                return func(*args, **kwargs)

            # Nếu không bằng:
            else:
                print(f"⛔ Cần quyền '{required_role}' nhưng bạn là '{user_role}'")
                return None
            
        return wrapper
    return decorator

# --- TEST CASE (Chạy để kiểm tra) ---

print("--- Test 1: Giáo viên sửa điểm (Mong đợi: ✅) ---")
@check_permission("teacher")
def update_score(student_id, score):
    print(f"✅ Đã sửa điểm HS {student_id} thành {score}")

update_score("SV01", 10)


print("\n--- Test 2: Giáo viên xóa HS (Mong đợi: ⛔) ---")
@check_permission("admin")
def delete_student(student_id):
    print(f"❌ Đã xóa HS {student_id}")

delete_student("SV01")