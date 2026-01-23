# Bai 1: Hóa đơn siêu thị (Zip & List Comp)
items = ["Gạo", "Thịt", "Trứng", "Sữa"]
prices = [20000, 150000, 35000, 18000] # Giá đơn vị
quantities = [2, 1, 5, 3] # Số lượng mua

# Yêu cầu:
# Tạo một danh sách bill gồm các chuỗi: "Món [Tên]: [Tổng tiền] VND".
# Tổng tiền = Giá * Số lượng.
# Bắt buộc: Chỉ dùng 1 dòng code (List Comprehension + Zip). 
# Output mẫu: ['Món Gạo: 40000 VND', 'Món Thịt: 150000 VND', ...]

out_bill = [f"Món {name}: {price * qty} VND" 
            for name,price,qty in zip(items, prices, quantities)
            ]

print(out_bill)

# =========================================================
# Bài 2: Lọc số liệu (Filter & Lambda)
# Input: numbers = [1, -5, 10, -2, 8, 0, 15, -9] 
# Yêu cầu:
# Lọc lấy các số dương (> 0).
# Bình phương chúng lên.
# Sắp xếp giảm dần.
# Dùng filter, map và sorted. Output mẫu: [225, 100, 64, 1]

print("\n===========================")
numbers = [1, -5, 10, -2, 8, 0, 15, -9]

# Cách 1: Dùng biến tạm
filter_nums = filter(lambda x: x > 0, numbers) 
binh_phuong = map(lambda x: x**2, filter_nums)

print("\nCach 1: Dùng biến tạm (dễ nhìn - dễ debug)")
print(sorted(list(binh_phuong),key=lambda x: -x))

# Cách 2: Không cần dùng biến mà làm gọp
result = sorted(
    map(lambda x: x**2, filter(lambda x: x > 0, numbers)), 
    key = lambda x: x, reverse = True
)
print("\nCach 2: Gọp (nhìn chuyên nhiệp hơn)")
print(result)

# Cách 3: Sử dụng list Comprehensions
result = sorted([i**2 for i in numbers if i > 0], reverse= True)
print("\nCach 3: List Comprehensions (thông dụng, dễ đọc nhất)")
print(result)