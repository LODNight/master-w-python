# Dữ liệu giả lập từ file Excel nhập điểm
student_ids = ['SV001', 'SV002', 'SV003', 'SV004']
names = ['nguyen van a', 'tran thi b', 'le van c', 'pham thi d']
scores = [8.5, 9.0, 4.5, 9.0] # Điểm số tương ứng

# --- YÊU CẦU ---

# 1. Dùng zip() và dict() để tạo một Dictionary tra cứu điểm theo ID
# Kết quả mong muốn: {'SV001': 8.5, 'SV002': 9.0, ...}

score_board = dict(zip(student_ids,scores)) 
print("Score Board:", score_board)


# 2. Dùng zip() và list comprehension để tạo danh sách báo cáo
# Kết quả: ['SV001 - Nguyen Van A - 8.5', ...]
# Gợi ý: Dùng .title() để viết hoa chữ cái đầu tên
report = [
    f"{sid} - {name} - {score}" 
    for sid, name, score in zip(student_ids, names, scores)
]
print("Report:", report)


# 3. Dùng sorted() để tìm ra Top 3 sinh viên có điểm cao nhất
# Gợi ý: zip lại 3 danh sách thành list các tuple (score, name, id) rồi sort
combined_data = list(zip(student_ids, names, scores))
top_students = sorted(combined_data, key = lambda x: x[2], reverse=True)
top_3_student = top_students[:3] 
print("Top Students:", top_3_student)