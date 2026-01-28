# Tình huống: Hệ thống LMS cần quản lý Danh sách khóa học (Course).
# Mỗi khóa học có: title (Tên khóa), price (Giá).
# Hệ thống cần biết Tổng số khóa học đang có trên toàn hệ thống.
# Hệ thống cần một phương thức để tạo khóa học từ một chuỗi "Tên-Giá" 
# (Do dữ liệu từ file Excel import vào thường là dạng chuỗi).

# Yêu cầu: Viết Class Course.
# Có Class Attribute total_courses = 0.
# __init__: Tăng total_courses lên 1 mỗi khi tạo khóa học.
# @classmethod from_string(cls, text): Nhận vào "Python-500", trả về Object Course.

class Course:
    total_courses = 0
    def __init__(self,title, price):
        self.title = title
        self.price = price
        # Biến chung
        Course.total_courses += 1

    @classmethod
    def from_string(cls, text):
        title,price = text.split("-")
        return cls(title,int(price))
    
    def show_info(self):
        print(f"Course: {self.title} - Price: {self.price}")

    
# --- TEST CASE ---
# 1. Tạo thủ công
c1 = Course("Lập trình C", 100)

# 2. Tạo bằng Factory Method (từ chuỗi nhập liệu)
c2 = Course.from_string("Python Advanced-300")

# 3. Kiểm tra
c1.show_info()
c2.show_info()

print(f"Tổng số khóa học: {Course.total_courses}") 
# Mong đợi: 2