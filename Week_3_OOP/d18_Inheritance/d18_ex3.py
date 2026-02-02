# Tình huống: Trong LMS có 2 loại khóa học:

# Course (Thường): Chỉ có title (Tiêu đề).
# PremiumCourse (Vip): Là con của Course. Có thêm price (Giá) và discount (Giảm giá %).

# Yêu cầu:
# Class PremiumCourse kế thừa Course.
# Trong __init__: Dùng super() để gán title, sau đó tự gán price và discount.
# Viết hàm get_price_after_discount() trong PremiumCourse để tính giá cuối.

class Course:   
    def __init__(self, title):
        self.title = title
    
    def info(self):
        return f"Khóa học: {self.title}"

class PremiumCourse(Course):
    def __init__(self, title, price, discount):
        super().__init__(title)
        self.price = price
        self.discount = discount

    def get_price_after_discount(self):
        return (self.price * (1 - self.discount/100))
    
    def info(self):
        return f"Khóa học: {self.title} - Giá: {self.get_price_after_discount()}"

# --- TEST CASE ---
c1 = Course("Python Basic")
p1 = PremiumCourse("Python Pro", 1000, 20) # Giá 1000, giảm 20%

print(c1.info()) 
# Output: Khóa học: Python Basic

print(p1.info()) 
# Mong đợi Output: Khóa học: Python Pro - Giá: 800.0

    