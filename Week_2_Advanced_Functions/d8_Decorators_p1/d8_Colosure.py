def make_multiplier(n):
    # 'n' là biến của hàm cha (biến tự do)
    def multiplier(x):
        return x * n # Hàm con dùng 'n' dù hàm cha đã chạy xong
    return multiplier

# Tạo ra hàm nhân 2
nhan_doi = make_multiplier(2) 
# Lúc này make_multiplier đã chạy xong, nhưng 'nhan_doi' vẫn nhớ n=2

print(nhan_doi(5)) # Output: 10
print(nhan_doi(10)) # Output: 20