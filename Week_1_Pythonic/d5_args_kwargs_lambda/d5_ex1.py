# Tình huống: Bạn cần viết hàm update_student_info để cập nhật thông tin học sinh trong Database (giả lập bằng 1 list dict). Yêu cầu hàm này phải nhận vào student_id và bất kỳ thông tin nào cần sửa (có thể sửa tên, sửa điểm, hoặc sửa cả hai).
# Database giả lập
database = [
    {'id': 'SV01', 'name': 'An', 'score': 8.5, 'city': 'Hanoi'},
    {'id': 'SV02', 'name': 'Binh', 'score': 9.0, 'city': 'HCM'}
]

def update_student(student_id, **kwargs):
    """
    Hàm cập nhật thông tin học sinh.
    student_id: ID học sinh cần sửa.
    **kwargs: Các trường dữ liệu cần sửa (VD: score=10, city='Danang')
    """
    found = False
    for student in database:
        if student['id'] == student_id:
            found = True
            # TODO: Duyệt qua kwargs và cập nhật vào dictionary student
            # Gợi ý: dùng vòng lặp for key, val in kwargs.items(): ...
            for key,val in kwargs.items():
                student[key] = val
            
            print(f"Đã cập nhật SV01: {student}")
            break
            
    if not found:
        print("Không tìm thấy sinh viên!")

# --- TEST CASE ---
print("Trước khi sửa:", database[0])

# Trường hợp 1: Chỉ sửa điểm
update_student('SV01', score=10)

# Trường hợp 2: Sửa cả tên và thành phố
update_student('SV01', name='Nguyen Van An', city='Da Nang')

# Trường hợp 3: Sửa trường chưa từng có (vẫn chấp nhận -> tính năng mở rộng)
update_student('SV01', phone='0909999999')
