def chao_mung(ten):
    return f"Hello {ten}"

# 1. Gán hàm cho biến
loi_chao = chao_mung 
print(loi_chao("An")) # Output: Hello An

# 2. Định nghĩa hàm bên trong hàm (Nested Function)
def outer():
    print("Đây là hàm ngoài")
    
    def inner():
        print("Đây là hàm trong")
    
    # 3. Trả về hàm bên trong (trả về cái máy, chưa chạy cái máy)
    return inner 

my_func = outer() # Chạy outer, trả về inner
my_func()         # Bây giờ mới chạy inner