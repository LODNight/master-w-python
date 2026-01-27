# L (Local): Tìm trong hàm hiện tại trước. Có không? -> Có thì lấy.
# E (Enclosing): Không có ở Local? Tìm ra hàm cha (hàm bao bọc nó). Đây chính là nơi Decorator lấy func.
# G (Global): Không có ở cha? Tìm ra ngoài cùng file.
# B (Built-in): Không có ở file? Tìm trong thư viện gốc Python (len, print, str...).
