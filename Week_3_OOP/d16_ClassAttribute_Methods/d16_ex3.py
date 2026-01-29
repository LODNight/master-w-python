# Bài 2: Xử lý Ngày tháng (Date Handler) - Factory Method
# Mục tiêu: Rèn luyện kỹ năng viết "Cổng nhập liệu" bằng Class Method.

# Tình huống: Bạn cần tạo Object MyDate gồm day, month, year. 
# Dữ liệu đầu vào có thể đến từ 2 nguồn:
    # Truyền số trực tiếp: MyDate(29, 1, 2026) -> Dùng __init__.
    # Truyền chuỗi String (từ API): "29-01-2026" -> Cần viết Factory Method.

# Yêu cầu: Viết Class Method from_string(cls, date_str) để xử lý chuỗi và trả về Object.

class MyDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def from_string(cls, date_str):
        # Input: "29-01-2026"
        # TODO: Tách chuỗi, ép kiểu int, trả về Object
        day,month,year = date_str.split("-")
        return cls(int(day),int(month),int(year))
        
        
    def show(self):
        print(f"Ngày: {self.day}/{self.month}/{self.year}")

# --- TEST CASE ---
# Cách 1: Truyền thống
d1 = MyDate(1, 1, 2025)

# Cách 2: Từ chuỗi (Factory)
d2 = MyDate.from_string("29-01-2026")

d1.show()
d2.show() # Mong đợi: Ngày: 29/1/2026