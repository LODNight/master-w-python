# Tình huống Dự án LMS: 
# Chúng ta bắt đầu xây dựng Class cốt lõi: Student. 
# Học sinh cần có: Tên, ID, và danh sách điểm. 
# Hành động: Thêm điểm, tính điểm trung bình, và hiển thị thông tin.

class Student:
    
    # 1. Khai báo Constructor
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []

    # 2. Method thêm điểm
    def add_score(self, score):
        # Logic: Chỉ thêm nếu score từ 0 đến 10. Nếu sai in ra lỗi.
        if 0 >= score <= 10: 
            self.scores.append(score)
        else: 
            print(f"Lỗi Score phải lớn hơn 0 và bé hơn 10")
        
    # 3. Method tính trung bình
    def calculate_gpa(self):
        # TODO: Trả về tổng điểm / số lượng điểm
        # Chú ý: Nếu list rỗng thì trả về 0.0 để tránh lỗi chia cho 0
        if self.scores:
            return sum(self.scores) / len(self.scores)
        return 0.0

    # 4. Method hiển thị thông tin
    def show_info(self):
        # TODO: In ra "HV: [Tên] - ID: [ID] - GPA: [GPA]"
        print(f"HV: {self.name} - ID: {self.student_id} - GPA: {self.calculate_gpa()}")

# --- TEST CASE ---
sv = Student("Khuu Tin", "SV2026")
sv.add_score(8.5)
sv.add_score(9.0)
sv.add_score(11) # Test validation (Lỗi)

sv.show_info() 
# Mong đợi: HV: Khuu Tin - ID: SV2026 - GPA: 8.75