# 3. Lambda: Hàm dùng 1 lần rồi bỏ
# Thường đi kèm với filter, sorted, map,..


# Cách truyền thống (Dài dòng)
def binh_phuong(x):
    return x ** 2


# Cách Lambda (Gọn)
sq = lambda x: x**2
print(sq)

# Ứng dụng thực tế trong LMS: Sort danh sách dictionary
students = [{'name': 'A', 'score' : 10}, {'name': 'B', 'score': 9}]
# Sort theo score
students.sort(key=lambda s: s['score'])

print(students)