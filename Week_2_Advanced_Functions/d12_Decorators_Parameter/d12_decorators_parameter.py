# Cấu trúc Decorator "Matryoshka"

# Lớp 1: Nhận cấu hình (Config)
def repeat(times):
    print(f"1. Nhận cấu hình: lập {times} lần")

    # Lớp 2: Nhận hàm (The Decorator)
    def actual_decorator(func):
        print(f"2. Nhận hàm: {func.__name__}")

        # Lớp 3: Chay logic (The Wrapper)
        def wrapper(*args, **kwargs):
            print(f"3. Bắt đầu chạy wrapper...")

            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper          # Trả về lớp 3
    return actual_decorator     # Trả về lớp 2