import functools

current_user = "Nhat Tin"

def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user:
            print("Bạn chưa đăng nhập")
            return None
        return func(*args, **kwargs)
    return wrapper

@login_required
def view_profile():
    print("Thông tin cá nhân: ...")

view_profile()