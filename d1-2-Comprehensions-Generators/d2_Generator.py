
# List Comprehesions: Chạy hết 1 lần rồi mới đưa ra kết quả => Chậm + Tốn RAM
# my_gen = [i for i in range(100000000)]


# Generator: Dùng tới đâu trả kết quả tới đó => Nhanh + đỡ tốn RAM
my_gen = (i for i in range(10000000))

print(my_gen)

# Bài tập maaxu: Chuyển đổi cú pháp (Dễ)
# Đề bài: Bạn có đoạn code List Comprehension dưới đây để tính bình phương. Hãy viết lại nó dưới dạng Generator Expression và dùng vòng lặp for để in ra từng số.

# Input: numbers = [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]

num = (i**3 for i in numbers)

for i in num:
    print(i)