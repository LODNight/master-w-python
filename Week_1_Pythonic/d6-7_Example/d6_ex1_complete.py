

# --- DỮ LIỆU ĐẦU VÀO ---
student_names = ["nguyen van a", "tran thi b", "le van c", "hoang thi d", "pham van e"]
student_scores = [4, 9, 8, 2, 9]
blacklist_ids = ["le van c", "nguyen van x"] # Danh sách cấm thi (đang để dạng List)

# --- CODE CỦA FRESHER (Cần bạn sửa lại) ---
def process_results(names, scores, blacklist):

    # Tạo set để biến đổi blacklist thành dictionary => Truy vấn nhanh
    banned_set = set(blacklist)

    # Sử dụng List comprehensions + zip + title() để duyệt qua
    results = [name.title() 
               for name,score in zip(names,scores) 
               if score >=5 and name not in banned_set]

    # In kết quả bằng enumerate
    print("--- DANH SÁCH ĐẬU ---")
    for id,name in enumerate(results, start = 1):
        print(f"STT {id}: {name}")

# Chạy thử
process_results(student_names, student_scores, blacklist_ids)

