import functools

def debug_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Tạo chuỗi log tham số args (VD: "1, 2")
        args_repr = [repr(a) for a in args]
        
        # Tạo chuỗi log tham số kwargs (VD: "x=3")
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        
        # Gộp lại
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"🐞 DEBUG: Đang gọi {func.__name__}({signature})")
        
        # Chạy hàm thật
        result = func(*args, **kwargs)
        
        print(f"✅ DEBUG: {func.__name__} trả về {result!r}")
        return result
    return wrapper

# --- TEST ---
@debug_log
def add(a, b):
    return a + b

add(5, 10)