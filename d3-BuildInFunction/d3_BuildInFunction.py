# 1. enumerate 
#   + Thay thế cho range(len(arr))
#   + enumerate tự động trả về cặp (index, value)
#   + tham số start=1 để bắt đầu đếm từ 1 thay vì 0

students = ['An', 'Bình', 'Châu']
print("--- Use enumerate ---")
for idx, student in enumerate(students, start = 1):  # 
    print(f"STT: {idx}, Name: {student}")


# ===========================
# 2. zip
#   + Kéo khóa các danh sách lại với nhau
#   + Giúp liên kết các list lại với nhau mà không bị lỗi "out of range" nếu 2 độ dài khác nhau

# zip gom lại từng cặp: ('An', 8), ('Binh', 9)...
scores = [10, 8, 6, 9]

print("\n--- Use zip ---")
for name, score in zip(students,scores):    # Sử dụng strict=True để báo lỗi nếu lệch độ dài
    print(f"Name: {name} - Score: {score}")


# ===========================
# 3. sorted
#   + Sắp xếp tùy biến (Custom Sort)

print("\n--- Use sorted ---")
students = [
    {'name': 'Tung', 'score': 8},
    {'name': 'An', 'score': 8},
    {'name': 'Binh', 'score': 9},
]

#   + sorted(iterable, key=..., reverse=...)
#   + key nhận vào một hàm (thường dùng lambda) để quyết định tiêu chí so sánh

sorted_students = sorted(
    students,
    key = lambda x: (-x['score'], x['name'])     # Dùng dấu - để đảo ngược số (Giảm dần)
)

print(sorted_students)


# ===========================
# 4. map & filter
#   + Phong cách lập trình hàm (Functional)
#   + Kết quả trả về là Iterator (Lazy evaluation - tiết kiệm nhớ) giống Generator

#   + map(func, list): Áp dụng hàm func lên từng phần tử.
#   + filter(func, list): Chỉ giữ lại phần tử mà func trả về True.

# Ví dụ làm sạch khoảng trắng trong mảng
print("\n--- Use Map ---")

raw_names = ['  An ', 'Binh  ', '  Chi']

# Dùng map() để strip từng tên
clean_names_iterator = map(str.strip, raw_names)

# clean_names_iterators chưa chạy ngay
# Muốn chạy đc kết quả thì phải dùng loop hoặc dùng list() 

# C1: Dùng list()
print(list(clean_names_iterator))

# C2: Dùng loop
# for i in clean_names_iterator:
#     print(i)