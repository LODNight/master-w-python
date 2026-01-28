class Student: # Tên Class viết hoa chữ cái đầu (PascalCase)
    
    # Hàm khởi tạo (Constructor): Chạy ngay khi tạo Object
    def __init__(self, name, student_id):
        self.name = name          # Gán thuộc tính name
        self.student_id = student_id # Gán thuộc tính id
        self.scores = []          # Tạo list điểm trống
        
    # Phương thức (Hành động)
    def add_score(self, score):
        self.scores.append(score)
        print(f"Đã thêm điểm {score} cho {self.name}")

# Tạo Object (Instance)
sv1 = Student("Nguyen Van A", "SV01") 
sv2 = Student("Tran Thi B", "SV02")

# Sử dụng
sv1.add_score(10)