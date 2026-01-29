class Student:
    def __init__(self, name, student_id, gpa=0):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    # TODO 1: Viết __str__ trả về "Student: [ID] - [Name]"
    def __str__(self):
        return f"Student: {self.student_id} - {self.name}"

    # TODO 2: Viết __eq__ so sánh dựa trên student_id
    def __eq__(self, other):
        return self.student_id == other.student_id

    # TODO 3: Viết __gt__ so sánh dựa trên gpa (Lớn hơn)
    def __gt__(self, other):
        return self.gpa > other.gpa

# --- TEST CASE ---
s1 = Student("Tin", "SV01", 8.0)
s2 = Student("Khuu Tin", "SV01", 9.0) # Cùng ID với s1 (Giả sử nhập trùng)
s3 = Student("An", "SV02", 7.5)

print("--- Test hiển thị ---")
print(s1) 
# Mong đợi: Student: SV01 - Tin

print("\n--- Test so sánh bằng (ID) ---")
if s1 == s2:
    print("✅ Hai học sinh này là một (Trùng ID)!")
else:
    print("❌ Khác nhau")

print("\n--- Test so sánh điểm ---")
if s1 > s3:
    print(f"✅ {s1.name} điểm cao hơn {s3.name}")