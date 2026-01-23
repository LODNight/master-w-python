# LEVEL 3: SENIOR MINDSET (Hiệu năng & Decorator)
# Mục tiêu: Tối ưu bộ nhớ và viết Decorator có tính ứng dụng cao.

# ====================================================

# Bài 5: Xử lý chuỗi Gen (DNA) khổng lồ (Generator)
# Tình huống: Chuỗi DNA người rất dài (hàng tỷ ký tự). Bạn cần tìm các đoạn mã (codon) gồm 3 ký tự liên tiếp (VD: "ATG", "CGC"...). Input giả lập: dna_sequence = "ATGCGATCGTAGCTAG..." (Rất dài). Yêu cầu:
# Viết hàm chunk_generator(sequence, size=3) sử dụng yield.
# Hàm này sẽ cắt chuỗi và trả về từng khúc 3 ký tự một.
# Tuyệt đối không tạo ra một list chứa tất cả các khúc (vì sẽ tràn RAM).
# Duyệt qua generator và in 5 khúc đầu tiên.


# ====================================================

# Bài 6: Decorator "Bắt lỗi" (Error Handling Decorator)
# Tình huống: Các hàm gọi API thường hay bị lỗi mạng. Thay vì viết try...except trong từng hàm, hãy viết 1 Decorator. Yêu cầu:
# Viết decorator @safe_run.
# Nếu hàm được trang trí chạy thành công -> Trả về kết quả.
# Nếu hàm bị lỗi (Exception) -> Không crash app, mà in ra dòng log: "Lỗi rồi: [Nội dung lỗi]" và trả về None. Áp dụng:

@safe_run
def divide(a, b):
    return a / b

print(divide(10, 2)) # Output: 5.0
print(divide(5, 0))  # Output: "Lỗi rồi: division by zero" -> None (App vẫn sống)