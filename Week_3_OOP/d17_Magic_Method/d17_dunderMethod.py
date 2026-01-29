#  Magic Methods (Dunder Methods)
# Magic Methods (hay Dunder Methods - Double Underscore) là các hàm đặc biệt có 2 dấu gạch dưới ở đầu và cuối (VD: __init__, __str__). 
# Không gọi trực tiếp các hàm này. 
# Python sẽ tự gọi chúng khi bạn thực hiện các phép toán hoặc lệnh in.

# __str__: Chạy khi bạn gọi print(obj) hoặc str(obj).
# __repr__: Chạy khi bạn gõ tên biến trong terminal (Representation).
# __eq__: Chạy khi bạn so sánh obj1 == obj2.
# __lt__, __gt__: Chạy khi so sánh nhỏ hơn < hoặc lớn hơn >.

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        
    # 1. Để in ra đẹp (Thay vì <__main__.Student object at 0x...>)
    def __str__(self):
        return f"Học sinh {self.name} - GPA: {self.gpa}"
    
    # 2. Để so sánh bằng (==)
    def __eq__(self, other):
        # Hai học sinh bằng nhau nếu tên giống nhau (Ví dụ vậy)
        return self.name == other.name
        
    # 3. Để so sánh lớn hơn (>)
    def __gt__(self, other):
        # So sánh dựa trên điểm GPA
        return self.gpa > other.gpa

    # 4. Sử dụng __repr__ cho DEV (giống với __str__)
    def __repr__(self):
        return f"Student: {self.name} - {self.gpa}"

# --- SỬ DỤNG ---
s1 = Student("An", 8.0)
s2 = Student("Binh", 9.0)
s3 = Student("An", 5.0)

print(s1)          # Tự gọi __str__ -> Output: Học sinh An - GPA: 8.0
print(s1 == s3)    # Tự gọi __eq__  -> Output: True (Vì cùng tên An)
print(s2 > s1)     # Tự gọi __gt__  -> Output: True (Vì 9.0 > 8.0)