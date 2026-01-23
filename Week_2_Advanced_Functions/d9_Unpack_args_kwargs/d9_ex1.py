# Tình huống: Bạn nhận được dữ liệu thô từ một file Excel nhập học. 
# Dữ liệu này lộn xộn, bao gồm ID, Tên, Email và một loạt điểm số phía sau. 
# Đồng thời, bạn có một cấu hình mặc định cho học sinh mới.

# Yêu cầu: Viết hàm process_import(raw_data, **custom_options) để:
# Tách ID, Tên, Email riêng ra.
# Gom toàn bộ điểm số còn lại vào một list scores.
# Gộp custom_options vào default_options để ra cấu hình cuối cùng.
# Trả về một Dictionary hoàn chỉnh để lưu DB.

def process_import(raw_data, **custom_options):
    default_options = {'role': 'student', 'active': True, 'class': 'K10'}
    
    # Dùng Unpacking (*) để tách ID, Name, Email và Scores từ raw_data
    id, name,email, *scores = raw_data
    
    # Merge 2 dictionaries (default và custom) thành final_options
    final_options = default_options | custom_options
    
    # 3. Đóng gói kết quả
    return {
        'id': id,
        'name': name,
        'email': email,
        'scores': scores,
        'info': final_options
    }

# --- CHẠY THỬ ---
# Dữ liệu giả lập 1 dòng từ Excel
row_excel = ['SV009', 'Nguyen Van A', 'a@gmail.com', 8, 9, 7.5]

# Gọi hàm: Vừa truyền list, vừa truyền đè option (active=False)
result = process_import(row_excel, active=False, note="Học sinh chuyển trường")

import pprint
pprint.pprint(result)