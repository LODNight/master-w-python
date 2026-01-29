# Tình huống: Công ty có quy định về Hệ số tăng lương (raise_amount) chung cho toàn nhân viên là 1.04 (tăng 4%). 
# Tuy nhiên, sếp có thể thay đổi con số này bất cứ lúc nào cho toàn công ty.

# Yêu cầu:
# Class Employee:
# Class Attribute: raise_amount = 1.04.
# __init__: Nhận name, salary.
# Instance Method apply_raise(self):
    # Cập nhật self.salary bằng cách nhân với Employee.raise_amount.
    # Class Method set_raise_amount(cls, amount):
    # Thay đổi raise_amount chung của cả công ty.

class Employee:
    # TODO 1: Khai báo hệ số tăng lương chung = 1.04
    raise_amount = 1.04

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        # TODO 2: Tăng lương dựa trên hệ số chung
        self.salary *= Employee.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        # TODO 3: Cập nhật hệ số chung
        cls.raise_amount = amount

# --- TEST CASE ---
emp1 = Employee("Tin", 1000)
emp2 = Employee("An", 2000)

# 1. Tăng lương theo mức cũ (4%)
emp1.apply_raise()
print(f"Lương Tin sau khi tăng: {emp1.salary}") # Mong đợi: 1040

# 2. Công ty làm ăn tốt, sếp tăng hệ số lên 1.10 (10%)
Employee.set_raise_amount(1.10)

# 3. Tăng lương cho An theo mức mới
emp2.apply_raise()
print(f"Lương An sau khi tăng: {emp2.salary}") # Mong đợi: 2200 (2000 * 1.1)