name = "5"   # Đây là String
score = 5    # Đây là Integer

# 1. Cách in thường (Mặc định !s)
print(f"Name: {name}, Score: {score}")
# 👉 Output: Name: 5, Score: 5 
# (Nhìn y hệt nhau! Không biết cái nào là chuỗi, cái nào là số -> Nguy hiểm khi debug)

# 2. Cách in dùng !r (rept())
print(f"Name: {name!r}, Score: {score!r}")
# 👉 Output: Name: '5', Score: 5
# (Thấy khác biệt chưa? '5' có dấu nháy bao quanh -> Biết ngay là String)