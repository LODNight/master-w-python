# Tình huống Dự án LMS: Hệ thống cần quản lý 2 loại người dùng: Student và Teacher.

# Cả 2 đều là User (Có name).
# Riêng Student: Có student_id. Hành động đặc trưng: study().
# Riêng Teacher: Có subject (Môn dạy). Hành động đặc trưng: teach().

# Yêu cầu:
# Viết Class User.
# Viết Class Student và Teacher kế thừa từ User.
# Nhớ dùng super() để tái sử dụng logic khởi tạo tên.

# 1. Class Cha
class User:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hello, I am {self.name}")

# 2. Class Student
class Student(User):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    
    def study(self):
        print(f"{self.name} (ID: {self.student_id}) is studying...")

# 3. Class Teacher
class Teacher(User):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def teach(self):
        print(f"Teacher {self.name} is teaching {self.subject}")

# --- TEST CASE ---
s1 = Student("Tin", "SV01")
t1 = Teacher("Mr. Ba", "Math")

# Kiểm tra tính kế thừa
s1.introduce() # Dùng của Cha
s1.study()     # Dùng của Con

t1.introduce() # Dùng của Cha
t1.teach()     # Dùng của Con