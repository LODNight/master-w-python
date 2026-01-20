
# Bài tập mẫu: Chuyển đổi cú pháp (Dễ)
# Đề bài: Bạn có đoạn code List Comprehension dưới đây để tính bình phương. Hãy viết lại nó dưới dạng Generator Expression và dùng vòng lặp for để in ra từng số.

# Input: numbers = [1, 2, 3, 4, 5]

# numbers = [1, 2, 3, 4, 5]

# num = (i**2 for i in numbers)

# for i in num:
#     print(i)


# Bài tập 2: Cơ chế tạm dừng (Trung bình)
# Đề bài: Viết một hàm my_countdown(n) nhận vào số nguyên n. Dùng yield để đếm ngược từ n về 0.

# Thử chạy debug bằng tay với hàm next().

# def count_down(n):
#     print("Start countdown...")
#     while n > 0:
#         yield n
#         n -= 1
#     print("END")

# counter = count_down(4)

# print(next(counter))
# print(next(counter))
# print(next(counter))



# Bài tập 3: Cấp mã ID tự động (LMS System)
# Tình huống: Trong hệ thống trường học, bạn cần cấp mã thẻ sinh viên liên tục mà không bao giờ bị trùng, không bao giờ hết (Infinite Sequence). Nếu dùng List, bạn không thể tạo một list vô tận được (tràn RAM ngay). Yêu cầu: Viết hàm student_id_generator(prefix) sử dụng yield.
# Input: prefix="STU"
# Output lần 1: "STU-1"
# Output lần 2: "STU-2"
# ... mãi mãi.

# def student_id_generator(prefix):
#     num = 1
#     while True:
#         yield f"{prefix}-{num}"
#         num += 1

# id_gen = student_id_generator("STU")
# print(next(id_gen))
# print(next(id_gen))
# print(next(id_gen))
# print(next(id_gen))



# Bài tập 4: Xử lý file Log khổng lồ (Data Analysis)
# Tình huống: Bạn có một file server log nặng 10GB. Bạn không thể dùng open().readlines() vì nó sẽ load cả 10GB vào RAM (máy sẽ treo). 
# Giả lập: Chúng ta có một list log giả lập (coi như là các dòng trong file). 
# Yêu cầu: Viết một generator function nhận vào danh sách log, chỉ yield ra những dòng có chứa chữ "ERROR".

logs = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "INFO: View page home",
    "ERROR: Timeout 500ms",
    "WARNING: Low disk space"
]
# Kết quả: Duyệt qua generator để in các dòng lỗi.

def error_log(log_lines):
    for i in log_lines:
        if "ERROR" in i:
            yield i

error = error_log(logs)
for err in error:
    print(err)