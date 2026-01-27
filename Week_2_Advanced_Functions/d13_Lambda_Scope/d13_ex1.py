# Tình huống: Trong hệ thống LMS, bạn có danh sách học sinh. 
# Bạn cần sắp xếp danh sách này theo tên (chữ cái cuối cùng của tên) chứ không phải họ.
# Ví dụ: "Nguyen Van An" xếp trước "Le Thi Binh".

# Yêu cầu:
# Dùng lambda kết hợp với sorted (hoặc sort).
# Viết hàm split trong lambda để lấy tên.

students = ["Nguyen Van C", "Le Thi A", "Tran Van B"]

sort_student = sorted(students, key= lambda x: x.split(" ")[-1])
print(sort_student)