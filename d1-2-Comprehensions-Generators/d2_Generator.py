import sys

# List Comprehesions: Chạy hết 1 lần rồi mới đưa ra kết quả => Chậm + Tốn RAM
list_data = [i for i in range(10000)]


# Generator: Dùng tới đâu trả kết quả tới đó => Nhanh + đỡ tốn RAM
gen_data = (i for i in range(10000))

print(f"Dung luon cua List comprehensions: {sys.getsizeof(list_data)} bytes")
print(f"Dung luon cua Generator: {sys.getsizeof(gen_data)} bytes")


# Bài 2: Hiểu cơ chế "Pause/Resume" (Debug thủ công)

# Tạo hàm my_generator()
def my_generator():
    print("--- Start ---")
    yield 1
    print("--- Get 1 ---")
    yield 2
    print("--- Get 2 ---")
    yield 3
    print("--- END ---")
    
# Khởi tạo hàm => Chưa chạy dòng code nào trong my_generator()
gen = my_generator()

print("Call 1: ")
val1 = next(gen)    # Chạy đến yield 1 rồi dừng lại
print(f"GET val1: {val1}")

print("Call 2: ")
val2 = next(gen)    # Chạy tiếp dòng print() sau yield 1 => đến yield 2 rồi dừng lại
print(f"GET val2: {val2}")



# Bài 3: Batch Processing (Xử lý dữ liệu theo lô - Rất thực tế cho Data)
# Tình huống: Bạn có một danh sách 10.000 user cần xử lý. Bạn không muốn xử lý 1 lần (quá tải), mà muốn lấy ra từng nhóm 3 người một (Batch size = 3) để xử lý dần.

users = ["User 1", "User 2", "User 3", "User 4", "User 5", "User 6", "User 7"]

def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        # return về một nhóm bên trong list
        yield data[i : i+batch_size]

batches = batch_generator(users,3)

for i in batches:
    print(f"Process: {i}")
    