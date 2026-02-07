# Yêu cầu:
# Class Course: __init__ nhận title, price.
# Class User: __init__ nhận name.
# Class Student (Kế thừa User):
# Có thuộc tính courses = [] (Danh sách khóa học).
# Method enroll(course): Nhận vào một Object Course, thêm vào danh sách.
# Validation: Nếu tài khoản dư (giả sử balance ở User) không đủ trả course.price thì báo lỗi (Nâng cao: thêm thuộc tính balance cho User).
# Method show_courses(): In ra danh sách khóa đã đăng ký.

class Course: 
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def __str__(self):
        return f"- Name: {self.title} - price: {self.price}"

class User: 
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

class Student(User):
    def __init__(self,name, balance=0):
        super().__init__(name,balance)
        self.courses = []

    def enroll(self,course):
        if self.balance < course.price:
            print("Fail")
            return            
        
        self.balance -= course.price
        self.courses.append(course)
        print("Success")
    
    def show_my_courses(self):
        print(f"\nKhoa hoc cua {self.name}")
        if not self.courses:
            print("Chua co khoa hoc nao")
        else:
            for c in self.courses:
                print(f"- {c}")

# --- TEST CASE ---
c1 = Course("Python Basic", 50)
c2 = Course("Python Advanced", 100)

s1 = Student("Tin", 120) # Có 120 đồng

s1.enroll(c1) # Mua khóa 50 -> Còn 70. OK
s1.enroll(c2) # Mua khóa 100 -> Thiếu tiền. Báo lỗi.

s1.show_my_courses()
# s1.info() # Kiểm tra lại số dư cuối cùng