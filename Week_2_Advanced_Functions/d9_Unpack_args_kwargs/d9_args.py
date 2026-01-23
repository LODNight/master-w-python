# ===========================================

# 1. Extended Iterable Unpacking (Bung lụa danh sách)
# Cú pháp: biến, biến, *biến_chứa_phần_còn_lại
row = ['SV01', 'An', 8, 9, 7, 10]

s_id, s_name, *s_score = row
print(s_id)
print(s_score)


# Nếu muốn chỉ lấy phần tử đầu và cuối
data = ['SV02', 'Binh', 8, 9, 7, 10]

s_first, *s_middle, s_last = data
print(f"{s_first} - {s_last}")

print("\n")

# ===========================================

# 2. Unpacking trong gọi hàm (Phá vỡ cấu trúc)
def create_student(sid, name,age):
    print(f"Tao {name} (Id: {sid}) - {age} tuoi ")

# *args
infor = ['SV01', 'Cuong', 20]
# Dùng * để "phá vỡ" cái list thành 3 biến rời
create_student(*infor)

# **kwagrs
data = {'sid': 'SV02', 'name': 'Chi', 'age': 22}
# Dùng ** để phá vỡ dict thành keyword arguments (sid=..., name=...)
create_student(**data)

# ===========================================

# 3. Merging Dictionaries (Gộp từ điển) - Skill quan trọng cho API
# Trong dự án LMS, bạn thường có:
# Default Config: Cấu hình mặc định.
# User Config: Cấu hình user gửi lên. Bạn cần gộp chúng lại, nếu trùng thì lấy của User.

default = {'theme': 'light', 'lang': 'vi', 'limit': 10}
user_setting = {'theme': 'dark', 'limit': 50}

# Dùng ** để bung cả 2 ra vào trong 1 dict mới
# Cái nào đứng sau (user_setting) sẽ ghi đè cái trước
final_config_1 = {**default, **user_setting}
print(final_config_1)

# Lưu ý: Từ Python 3.9+, bạn có thể viết ngắn hơn: final_config = default | user_setting.
final_config_2 = default | user_setting

print(final_config_2)

