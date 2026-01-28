class Student:
    school_names = "LMS Tech School"
    total_students = 0

    def __init__(self,name):
        # --- Instance Attribute (của riêng từng Object) ---
        self.name = name
        # --- Mỗi lần tạo HS mới là + 1 (của chung toàn bộ Object sử dụng Class này) ---
        Student.total_students += 1
    
    # --- Instance Method (Thao tác trên self) ---
    def show_name(self):
        print(f"Tui tên là: {self.name}")

    # --- Class Method (Thao tác trên cls - Class) ---
    @classmethod
    def set_school_name(cls, new_name):
        cls.school_names = new_name
        print(f"Trường đã đổi tên thành: {cls.school_names}")

s1 = Student("An")
s2 = Student("Binh")

print(s1.school_names)
print(Student.total_students)

Student.set_school_name("Future Academy")
print(s1.school_names)