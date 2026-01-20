import time

# Tạo danh sách blacklist giả lập (1 triệu phần tử)
# Đây là List (tra cứu chậm)
blacklist_list = [f"User_{i}" for i in range(1000000)]

    
# Hãy tạo một Set từ List trên (tra cứu nhanh)
blacklist_set = set(blacklist_list) 

# ID cần kiểm tra (Nằm ở cuối danh sách để test trường hợp xấu nhất)
user_to_check = "User_999999"

# Yêu cầu:
# Viết code đo thời gian kiểm tra user_to_check trong blacklist_list (dùng toán tử in).
def check_user_list():
    if user_to_check in blacklist_list:
        pass

# Viết code đo thời gian kiểm tra user_to_check trong blacklist_set (dùng toán tử in).
def check_user_set():
    if user_to_check in blacklist_set:
        pass

# So sánh kết quả xem Set nhanh hơn gấp bao nhiêu lần?


# Gợi ý dùng module time để đo:

start = time.time()
check_user_list()

end = time.time()
print(f"Thời gian: {end - start} giây")


start = time.time()
check_user_set()
end = time.time()
print(f"Thời gian: {end - start} giây")