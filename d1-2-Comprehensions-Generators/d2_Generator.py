import sys

# List Comprehesions: Chạy hết 1 lần rồi mới đưa ra kết quả => Chậm + Tốn RAM
list_data = [i for i in range(10000)]


# Generator: Dùng tới đâu trả kết quả tới đó => Nhanh + đỡ tốn RAM
gen_data = (i for i in range(10000))

print(f"Dung luon cua List comprehensions: {sys.getsizeof(list_data)} bytes")
print(f"Dung luon cua Generator: {sys.getsizeof(gen_data)} bytes")



