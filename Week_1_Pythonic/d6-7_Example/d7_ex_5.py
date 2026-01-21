# Tình huống: Bạn có một file log server khổng lồ (giả lập bằng 1 list chứa 1 triệu dòng string). 
# Dữ liệu: "ERROR: Disk full", "INFO: User login", "WARNING: Low memory", ... 

# Yêu cầu: Viết một quy trình xử lý (pipeline) dùng Generator (không dùng List trung gian) để:
# Duyệt qua từng dòng log.
# Chỉ lọc lấy dòng có chữ "ERROR".
# Biến đổi dòng đó thành chữ hoa (Upper case).

# Lấy ra 5 lỗi đầu tiên và in ra màn hình. 
# Mục tiêu: Chứng minh rằng dù input có 1 tỷ dòng thì RAM vẫn không tăng.

import sys
def process_log(logs):
    error_lines = (line for line in logs if "ERROR" in line)

    upper_lines = (line.upper() for line in set(error_lines))

    for line in upper_lines:
        print(line)
    print(f"\n Kiem Tra bo nho {sys.getsizeof(upper_lines)} bytes")

logs = ["ERROR: Disk full", "INFO: User login", "WARNING: Low memory", "ERROR: Out Memory"]
process_log(logs)
