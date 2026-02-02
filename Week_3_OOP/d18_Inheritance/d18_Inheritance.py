# 1. Class Cha (Cơ bản)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def login(self):
        print(f"👤 {self.name} đã đăng nhập!")

# 2. Class Con (Kế thừa từ User)
class Student(User): # <--- Mở ngoặc truyền tên Cha vào
    def __init__(self, name, email, student_id):
        # Gọi hàm khởi tạo của Cha (để Cha setup name, email giùm)
        super().__init__(name, email) 
        self.student_id = student_id # Cái riêng của con
        
    def study(self): # Hàm riêng của con
        print(f"🎓 {self.name} đang học bài...")

# --- SỬ DỤNG ---
s = Student("Tin", "tin@gmail.com", "SV01")

s.login() # Dùng đồ của Cha (Output: 👤 Tin đã đăng nhập!)
s.study() # Dùng đồ của Con (Output: 🎓 Tin đang học bài...)