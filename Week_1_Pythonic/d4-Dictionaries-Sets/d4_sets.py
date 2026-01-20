# Set là một cái túi chứa các phần tử không trùng lặp và không có thứ tự

# a. Khử trùng lặp (Remove Duplicates)

print("\na) Remove Duplicates")
emails = ['a@gmail.com', 'b@gmail.com', 'a@gmail.com']
unique_email = list(set(emails))

print(unique_email)

# b. Các phép toán tập hợp (Cực quan trọng cho LMS)
print("\nb) Toán tập hợp")

# A: Tất cả sinh viên trong lớp.
# B: Sinh viên đã nộp bài tập.
# Hỏi: Ai chưa nộp bài?

all_students = {'SV01', 'SV02', 'SV03', 'SV04'}
submitted = {'SV02', 'SV04'}

# 1. Tìm người chưa nộp (Hiệu của tập hợp: A - B)
missing_student = all_students - submitted
print(f"Chưa nộp: {missing_student}")

# 2. Tìm người vừa đăng ký lớp Toán VÀ lớp Lý (Giao của tập hợp: A & B)
math_class = {'SV01', 'SV02'}
physic_class = {'SV02', 'SV03'}
both = math_class & physic_class
print(f"Đăng ký Toán và Lý: {both}")

# 3. Gom hết sinh viên 2 lớp lại (Hợp của tập hợp: A | B)
total = math_class | physic_class
print(f"Sinh viên 2 lớp: {total}")
