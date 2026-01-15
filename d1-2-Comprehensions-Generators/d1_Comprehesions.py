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


# CAU 4: Cho một danh sách các số từ 1 đến 20. Tạo một danh sách mới chỉ chứa các số chia hết cho 2.
# Input: range(1, 21)
# Output mong muốn: [2, 4, 6, ..., 20]

evens = [i for i in range(1,24) if i%2==0]
print(evens)


# CAU 5: Cho một câu văn. Hãy tách lấy các từ có độ dài lớn hơn 3 ký tự.
# Input: sentence = "Học Python rất thú vị và bổ ích"
sentence = "Học Python rất thú vị và bổ ích"
out = [i for i in sentence.split() if len(i) > 3]
print(out)



# CAU 6: Cho một danh sách số. Tạo danh sách mới: nếu số chẵn thì ghi "Chẵn", nếu số lẻ thì ghi "Lẻ".
# Input: nums = [1, 2, 3, 4]
# Output mong muốn: ['Lẻ', 'Chẵn', 'Lẻ', 'Chẵn']
nums = [1, 2, 3, 4]
out = ["Chan" if i%2 == 0 else "Le" for i in nums]
print(out)


# Bài 7: Làm phẳng danh sách (Flatten Matrix)
# Đề bài: Cho một ma trận (list chứa các list con). Hãy chuyển nó thành một list đơn duy nhất (1 chiều).
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output mong muốn: [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
out = [num for col in matrix for num in col]
print(out)