def my_decorate(func_goc):
    def wrapper(*args, **kwargs):
        print("---- LOG: Trc khi chay ham ----")

        ket_qua = func_goc(*args, **kwargs)
        print("---- LOG: Sau khi chay ham ----")
        return ket_qua

    return wrapper


def say_hello():
    print("HEllo world")

@my_decorate
def say_bye():
    print("Good Bye")


say_hello_co_log = my_decorate(say_hello)
say_hello_co_log()
say_bye()