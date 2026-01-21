# Giả lập 10.000 sinh viên (dùng List Comprehension để tạo nhanh)
all_students = [f"SV{i}" for i in range(10000)] 
# Giả lập những người đã nộp (thiếu mất vài người)
submitted_students = [f"SV{i}" for i in range(5, 10000)]

# Yêu cầu:
# Tìm danh sách ID chưa nộp bài (missing_students).
# Đo thời gian chạy. Nếu bạn dùng List để tìm -> TRƯỢT. 
# Phải dùng Set. 
# Output mong muốn: {'SV0', 'SV1', 'SV2', 'SV3', 'SV4'} (Thứ tự không quan trọng).


import time
start = time.time()
missing_students = set(all_students) - set(submitted_students)
end = time.time()

print(missing_students)
print(f"Time: {end - start}")