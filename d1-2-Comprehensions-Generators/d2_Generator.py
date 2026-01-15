
# List Comprehesions: Chạy hết 1 lần rồi mới đưa ra kết quả => Chậm + Tốn RAM
# my_gen = [i for i in range(100000000)]


# Generator: Dùng tới đâu trả kết quả tới đó => Nhanh + đỡ tốn RAM
my_gen = (i for i in range(10000000))

print(my_gen)