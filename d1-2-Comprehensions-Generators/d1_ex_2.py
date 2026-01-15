#=============================================================
# Mức độ: Dễ (Easy)
# Bài 1: Tổng doanh thu (loại bỏ dữ liệu lỗi)

# Tình huống: Bạn nhận được một list doanh thu theo ngày từ API, nhưng có một số ngày hệ thống bị lỗi trả về None hoặc số âm. Bạn cần tính tổng doanh thu hợp lệ.
# Input: revenue = [100, 200, None, 50, -10, 300]
# Yêu cầu: Tính tổng các số lớn hơn 0 (bỏ qua None và số âm). Sử dụng hàm sum().
# Kết quả mong muốn: 650 (100 + 200 + 50 + 300)
revenue = [100, 200, None, 50, -10, 300]
result = sum([s for s in revenue if s is not None and s > 0])

print("\nCau 1:")
print(result)



#=============================================================
# Mức độ: Trung Bình (Medium)
# Bài 2: Tìm học sinh có điểm trung bình cao nhất (LMS Context)

# Tình huống: Trong hệ thống LMS, bạn có danh sách học sinh kèm điểm các môn. Bạn cần tìm ra số điểm trung bình cao nhất trong lớp để hiển thị lên bảng vinh danh.
# Input:
students = [
    {'name': 'A', 'scores': [8, 9, 7]},
    {'name': 'B', 'scores': [10, 9, 10]},
    {'name': 'C', 'scores': [6, 5, 7]}
]
# Yêu cầu: Tạo một list chứa điểm trung bình của từng bạn, sau đó tìm giá trị lớn nhất bằng max().
# Kết quả mong muốn: 9.66 (hoặc 9.666... do bạn B có điểm cao nhất).
avg_score = max([sum(i["scores"]) / len(i["scores"]) for i in students])

print("\nCau 2:")
print(avg_score)



#=============================================================
# Mức độ: Khó (Hard)
# Bài 3: Kiểm tra tính hợp lệ của mật khẩu (Validation)

# Tình huống: Bạn xây dựng chức năng đăng ký. Một danh sách mật khẩu người dùng nhập vào cần được kiểm tra. Mật khẩu hợp lệ phải chứa ít nhất một chữ số.
# Input: passwords = ["abcdef", "password123", "admin", "secure4you"]
# Yêu cầu: Trả về danh sách các mật khẩu hợp lệ.
# Gợi ý: Trong Python, chuỗi cũng là một iterable. Bạn có thể dùng list comprehension lồng nhau hoặc kết hợp hàm any(char.isdigit() for char in pwd).
# Kết quả mong muốn: ['password123', 'secure4you']
passwords = ["abcdef", "password123", "admin", "secure4you"]

a = [pwd for pwd in passwords if (any(char.isdigit() for char in pwd))]

print("\nCau 3:")
print(a)


#=============================================================
# Mức độ: Nâng cao (Advanced)
# Bài 4: Tính tổng giá trị đơn hàng phức tạp (E-commerce Order)

# Tình huống: Đây là bài toán thực tế khi xử lý JSON đơn hàng. Bạn có một danh sách các đơn hàng (Orders). Mỗi đơn hàng chứa danh sách các sản phẩm (Items). Bạn cần tính Tổng doanh thu của tất cả các đơn hàng.
# Input:
orders = [
    {
        'id': 1,
        'items': [{'price': 10, 'qty': 2}, {'price': 5, 'qty': 1}] # Tổng đơn 1 = 25
    },
    {
        'id': 2,
        'items': [{'price': 20, 'qty': 1}] # Tổng đơn 2 = 20
    }
]
# Yêu cầu: Dùng một dòng lệnh duy nhất (kết hợp sum và List Comprehension 2 tầng for) để tính tổng tiền.Công thức: Tổng = price x qty của tất cả item trong tất cả order.
# Kết quả mong muốn: 45

result = sum([i["price"]*i["qty"] for item in orders for i in item["items"]])

print("\nCau 4:")
print(result)



#=============================================================
# Mức độ: "Trùm cuối" (Expert - SQL Logic in Python)
# Bài 5: Group By và Join chuỗi (SQL style)

# Tình huống: Bạn có danh sách nhân viên thuộc các phòng ban khác nhau. Bạn muốn tạo một báo cáo dạng chuỗi liệt kê nhân viên theo từng phòng ban cụ thể (ví dụ phòng IT).
# Input:
employees = [
    {'name': 'Tín', 'dept': 'IT'},
    {'name': 'Hùng', 'dept': 'HR'},
    {'name': 'Lan', 'dept': 'IT'},
    {'name': 'Điệp', 'dept': 'Marketing'}
]
target_dept = 'IT'
# Yêu cầu: Tạo một chuỗi thông báo: "Nhân viên phòng IT gồm: Tín, Lan".
# Sử dụng List Comprehension để lọc tên.
# Sử dụng hàm ", ".join(...) để nối chuỗi.
# Sử dụng f-string để format kết quả cuối.

result = [i["name"] for i in employees if i["dept"] == target_dept]

print("\nCau 5:")
print(f"Nhan vien phong {target_dept} gom: {' ,'.join(result)}")

