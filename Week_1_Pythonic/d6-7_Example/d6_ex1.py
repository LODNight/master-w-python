# Đề bài: Đoạn code "Spaghetti" (Cần Refactor)
# Đoạn code dưới đây thực hiện 3 việc:
# + Ghép tên học sinh và điểm số.
# + Lọc ra học sinh đậu (điểm >= 5) VÀ không nằm trong danh sách cấm thi (blacklist).
# + In ra danh sách khen thưởng (viết hoa tên).

# --- DỮ LIỆU ĐẦU VÀO ---
student_names = ["nguyen van a", "tran thi b", "le van c", "hoang thi d", "pham van e"]
student_scores = [4, 9, 8, 2, 9]
blacklist_ids = ["le van c", "nguyen van x"] # Danh sách cấm thi (đang để dạng List)

# --- CODE CỦA FRESHER (Cần bạn sửa lại) ---
def process_results(names, scores, blacklist):
    results = []
    
    # 1. Vòng lặp kiểu C (dùng index i) - Rất rủi ro nếu độ dài 2 list lệch nhau
    for i in range(len(names)):
        name = names[i]
        score = scores[i]
        
        # 2. Check điều kiện đậu
        if score >= 5:
            
            # 3. Check blacklist thủ công (O(n) - Rất chậm)
            is_banned = False
            for banned_person in blacklist:
                if name == banned_person:
                    is_banned = True
                    break
            
            # Nếu không bị ban thì thêm vào list
            if is_banned == False:
                # 4. Xử lý string thủ công
                clean_name = name.title() # Viết hoa chữ cái đầu
                results.append(clean_name)

    # 5. In kết quả cũng dùng index nốt
    print("--- DANH SÁCH ĐẬU ---")
    for k in range(len(results)):
        print("STT " + str(k+1) + ": " + results[k])

# Chạy thử
process_results(student_names, student_scores, blacklist_ids)


# =====================================================
# Bạn hãy viết lại hàm process_results sao cho thỏa mãn các tiêu chí sau:
#   + Xóa bỏ vòng lặp range(len(...)): Hãy dùng zip để duyệt names và scores cùng lúc.
#   + Tối ưu tìm kiếm: Chuyển blacklist từ List sang Set để việc check if name in blacklist nhanh tức thì (O(1)).
#   + Code ngắn gọn: Dùng List Comprehension để lọc danh sách đậu trong 1 dòng (hoặc tối đa 2 dòng).
#   + In ấn đẹp: Dùng enumerate để in số thứ tự và dùng f-string.
