# a. .get() vs [] (Tránh lỗi Crash App)
print("\na) Sử dụng get và []")

student = {'id': 'SV01', 'name': 'An'}

# Nếu không có key 'score', trả về 0 (giá trị mặc định)
score = student.get('score',0)
print(score)


# b. Dictionary Comprehension
print("\nb) Sử dụng Dictionary Comprehision")

names = ['An', 'Binh', 'Chi']
ids = [101, 102, 103]

id_map = {uid: name for uid,name in zip(ids, names)}
print(id_map)


# c. Duyệt Dict hiệu quả (.items())
print("\nc) Duyệt Dict bằng item()")
for uid, name in id_map.items():
    print(f"Id: {uid} - Name: {name}")