# Bài 1: Làm sạch dữ liệu từ Form (Data Cleaning)
# Tình huống: Người dùng nhập danh sách sở thích vào một ô input, nhưng họ lỡ tay nhập nhiều khoảng trắng thừa hoặc để trống.
# Input: raw_hobbies = [" game ", "đọc sách", "", " ", "code python "]
# Yêu cầu: Loại bỏ khoảng trắng ở đầu/cuối mỗi từ và bỏ các chuỗi rỗng.
# Output mong muốn: ['game', 'đọc sách', 'code python']

# strip() dùng để kiểm tra chuỗi có bị trống ko
raw_hobbies = [" game ", "đọc sách", "", " ", "code python "]
out = [i.strip() for i in raw_hobbies if i.strip()]
print("\nCau 1:")
print(out)


# Bài 2: Lọc file ảnh trong thư mục (File Management)
# Tình huống: Bạn viết script để dọn dẹp thư mục download, bạn chỉ muốn lấy ra danh sách các file là ảnh (đuôi .png hoặc .jpg).
# Input: files = ["avatar.png", "report.docx", "notes.txt", "background.jpg", "script.py"]
# Yêu cầu: Lấy list các file có đuôi .png hoặc .jpg.
# Output mong muốn: ['avatar.png', 'background.jpg']

files = ["avatar.png", "report.docx", "notes.txt", "background.jpg", "script.py"]
# C1: 
png_jpg_1 = [f for f in files if f.split(".")[1] == "png" or f.split(".")[1] == "jpg"]

# C2: dung endswith()
png_jpg_2 = [f for f in files if f.endswith(("png","jpg"))] 

print("\nCau 2:")
print(png_jpg_1)
print(png_jpg_2)


# Bài 3: Tính giá sau thuế VAT (E-commerce)
# Tình huống: Bạn có danh sách giá gốc của sản phẩm. Bạn cần tính giá cuối cùng phải trả sau khi cộng thêm 10% thuế VAT.
# Input: prices = [100, 200, 50, 300]
# Yêu cầu: Tạo list giá mới, công thức: Giá x 1.1$. (Làm tròn 2 chữ số thập phân nếu cần).
# Output mong muốn: [110.0, 220.0, 55.0, 330.0]
prices = [100, 200, 50, 300]

new_price = [price + price*0.1 for price in prices]

print("\nCau 3:")
print(new_price)


# Bài 4: Lấy Email của sinh viên thi đỗ (LMS/Education)
# Tình huống: Trong hệ thống điểm thi, bạn có danh sách các sinh viên (dạng dictionary). Bạn cần trích xuất email của những bạn có điểm số >= 50 để gửi mail chúc mừng.
students = [
    {"name": "An", "email": "an@gmail.com", "score": 85},
    {"name": "Bình", "email": "binh@yahoo.com", "score": 40},
    {"name": "Chi", "email": "chi@outlook.com", "score": 60}
]
send_stu = [stu["email"] for stu in students if stu['score'] >= 50]

print("\nCau 4:")
print(send_stu)


# Bài 5: Tạo URL Slugs cho bài viết (Web Development)
# Tình huống: Khi làm blog, từ "Tiêu đề bài viết", bạn cần tạo ra "slug" để làm đường dẫn URL (viết thường, thay dấu cách bằng dấu gạch ngang).
# Input: titles = ["Học Python Cơ Bản", "List Comprehension Là Gì", "Lập Trình Web"]
# Yêu cầu: Biến đổi thành dạng hoc-python-co-ban (ở bài này mình chỉ giả sử xử lý dấu cách và chữ hoa thôi nhé, bỏ qua việc xử lý dấu tiếng Việt phức tạp).
# Output mong muốn: ['hoc-python-co-ban', 'list-comprehension-la-gi', 'lap-trinh-web']

titles = ["Học Python Cơ Bản", "List Comprehension Là Gì", "Lập Trình Web"]

slug = [t.lower().replace(" ", "-") for t in titles]

print("\nCau 4:")
print(slug)



