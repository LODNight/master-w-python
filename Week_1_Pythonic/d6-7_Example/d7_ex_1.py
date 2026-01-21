headers = ["  id  ", " name", "score "]
rows = [
    ["SV01", "  Nguyen Van A  ", 8.5],
    ["SV02", "Tran Thi B", 9.0],
    ["SV03", "   Le Van C ", 5.0]
]

# Làm sạch headers (xóa khoảng trắng thừa) -> ['id', 'name', 'score'].

# Tạo ra một List of Dictionaries chuẩn chỉnh map header với value tương ứng, đồng thời làm sạch luôn value (nếu là string). Output mong muốn:
[
    {'id': 'SV01', 'name': 'Nguyen Van A', 'score': 8.5},
    {'id': 'SV02', 'name': 'Tran Thi B', 'score': 9.0}, 
    ...
]

clean_header = [i.strip() for i in headers]
clean_data = [
    dict(zip(clean_header,
        [val.strip() 
         if isinstance(val, str) else val 
         for val in row]
        ))
        for row in rows
]

import pprint
pprint.pprint(clean_data)