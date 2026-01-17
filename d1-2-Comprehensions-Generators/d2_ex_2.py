# Đề bài: Viết một hàm generator fibonacci_gen(limit) để tạo ra dãy số Fibonacci (số sau bằng tổng 2 số trước: 0, 1, 1, 2, 3, 5, 8...) nhưng không vượt quá số limit.

# Gợi ý:
# Khởi tạo a = 0, b = 1.
# Trong vòng lặp: yield a.
# Cập nhật: a, b = b, a + b.

def finonacci_gen(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

gen = finonacci_gen(8)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))