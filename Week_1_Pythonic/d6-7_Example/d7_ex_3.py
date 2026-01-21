# Tình huống: Xếp hạng thi đua trong LMS. Tiêu chí xếp hạng (Ưu tiên từ trên xuống dưới):

# Điểm số (Score): Cao xếp trên.
# Số lần vi phạm (Warning): Thấp xếp trên.
# Tên (Name): A-Z. Input:

students = [
    {'name': 'An', 'score': 9, 'warning': 2},
    {'name': 'Binh', 'score': 9, 'warning': 0}, # Binh xếp trên An (vì ít warning hơn)
    {'name': 'Cuong', 'score': 8, 'warning': 0},
    {'name': 'Dat', 'score': 9, 'warning': 0}, # Dat xếp dưới Binh (vì tên D > B)
]

# Yêu cầu: Dùng sorted() với lambda để sắp xếp 1 phát ăn ngay. 
# Gợi ý: Tuple so sánh (Tiêu chí 1, Tiêu chí 2, Tiêu chí 3). 
# Lưu ý dấu - nếu muốn đảo ngược chiều sort số.

sort_student = [
    sorted(
        students, key=lambda x: (
            -x['score'],
            x['warning'],
            x['name']
            )
    )
]

import pprint
pprint.pprint(sort_student)