
# 1. *args: Non-Keyword Arguments
# Python sẽ gom tất cả các tham số thừa bạn truyền vào thành một Tuple.

def calculator(*score):
    # scores lúc này là tuple: (8, 9, 7, ...)
    print(f"Kieu du lieu la: {type(score)}")
    return sum(score)


print(calculator(10,2,5))