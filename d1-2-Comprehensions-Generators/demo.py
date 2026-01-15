# DAY 1
# Tìm hiểu thêm về List Comprehensions


# CAU 1: Hãy thêm các điểm số trên 7 vào danh sách passes_scores
scores = [5,6,7,3,8,10,9]
passes_scores_new = [i for i in scores if i > 7] 
print("Cách mới:",passes_scores_new)


# CAU 2:
nums = [1, 2, 3, 4, 5, 6, 7]
increase_nums = [i*2 for i in nums]
print(increase_nums)


# CAU 3: 
names = ["an", "bình", "chi"]

names_up = [i.upper() for i in names]
print(names_up)

# Day 2: 