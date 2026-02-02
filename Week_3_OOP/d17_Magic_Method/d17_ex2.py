# Tình huống Dự án LMS: Hoàn thiện Class Student để hệ thống có thể:
# In thông tin đẹp đẽ (__str__).
# Nhận diện 2 học sinh là trùng nhau nếu trùng student_id (__eq__).
# So sánh ai giỏi hơn dựa trên gpa (__gt__).

# Yêu cầu: Hãy viết lại code hôm trước, chú ý kỹ phần other.attribute và return True/False.

class Student:
    def __init__(self, name, student_id, gpa=0):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    # TODO 1: Viết __str__ trả về "Student: [ID] - [Name]"
    # VD: Student: SV01 - Tin
    def __str__(self):
        return f"Student: {self.student_id} - {self.name}"

    # TODO 2: Viết __eq__ so sánh ID của self và ID của other
    # Logic: return True nếu ID trùng nhau
    def __eq__(self, other):
        return self.student_id == other.student_id

    # TODO 3: Viết __gt__ so sánh GPA của self và GPA của other
    # Logic: return True nếu GPA của self lớn hơn
    def __gt__(self, other):
        return self.gpa > other.gpa

# --- TEST CASE ---
s1 = Student("Tin", "SV01", 8.0)
s2 = Student("Fake Tin", "SV01", 5.0) # Trùng ID, điểm thấp hơn
s3 = Student("An", "SV02", 7.5)

print(f"1. Hiển thị: {s1}") 
# Mong đợi: Student: SV01 - Tin

print(f"2. Check trùng (s1 == s2): {s1 == s2}") 
# Mong đợi: True (Vì cùng ID SV01)

print(f"3. Check giỏi hơn (s1 > s3): {s1 > s3}") 
# Mong đợi: True (Vì 8.0 > 7.5)

print(f"4. Check giỏi hơn (s3 > s1): {s3 > s1}") 
# Mong đợi: False