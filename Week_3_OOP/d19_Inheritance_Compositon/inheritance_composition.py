class Student:
    def __init__(self,name):
        self.name = name

class Classroom:
    def __init__(self, room_name):
        self.room_name = room_name
        # HAS-A: Lớp học CÓ MỘT danh sách học sinh
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all(self):
        print(f"Lop {self.room_name} gom:")
        for s in self.students:
            print(f"- {s.name}")

# --- SỬ DỤNG ---
s1 = Student("Tin")
s2 = Student("An")

lop_10A = Classroom("10A")
lop_10A.add_student(s1) # Nhét s1 vào lớp
lop_10A.add_student(s2) # Nhét s2 vào lớp

lop_10A.show_all()