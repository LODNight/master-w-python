# Tình huống Dự án LMS: Chúng ta cần xây dựng Class Classroom (Lớp học).
# Lớp học không kế thừa từ Học sinh.
# Một Lớp học có (chứa) nhiều Học sinh (Student).
# Một Lớp học có (chứa) một Giáo viên chủ nhiệm (Teacher).

# Yêu cầu:
# Tạo Class Student và Teacher đơn giản (có name).
# Tạo Class Classroom:
# Thuộc tính: name (Tên lớp), teacher (Object Teacher), students (List các Object Student).
# Method add_student(student): Thêm học sinh vào list.
# Method show_summary(): In ra tên lớp, tên giáo viên chủ nhiệm, và tổng số học sinh


class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name

class Classroom:
    def __init__(self, class_name, teacher):
        self.class_name = class_name
        self.teacher = teacher
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def show_summary(self):
        print(f"Lop {self.class_name} - Giao vien: {self.teacher.name} - Si so: {sum(self.students)}")

t = Teacher("Thầy Ba")
s1 = Student("Tin")
s2 = Student("An")

my_class = Classroom("12A", t)
my_class.add_student(s1)
my_class.add_student(s2)

my_class.show_summary()