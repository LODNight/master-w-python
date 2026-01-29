# Thuộc tính: owner (Tên chủ thẻ), balance (Số dư - mặc định là 0 nếu không nạp lúc mở thẻ).

# Hành động:
# deposit(amount): Nạp tiền. (Phải kiểm tra amount > 0).
# withdraw(amount): Rút tiền. (Phải kiểm tra amount > 0 VÀ amount <= balance). Nếu rút lố thì báo lỗi.
# show_balance(): In ra "Chủ thẻ: [Tên] - Số dư: [Tiền] VND".
class BankAccount:
    def __init__(self, owner, balance=0):
        # TODO: Gán thuộc tính
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # TODO: Kiểm tra > 0 -> Cộng tiền -> In thông báo
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        # TODO: Kiểm tra đủ tiền không -> Trừ tiền -> In thông báo
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Rút {amount} thành công. Số dư mới: {self.balance}")
        else: 
            print(f"Error: Không thể rút tiền. Số dư hiện tại: {self.balance}")

    def show_balance(self):
        # TODO: In thông tin
        print(f"Chủ thẻ: {self.owner} - Số dư: {self.balance}")

# --- TEST ---
acc = BankAccount("Tin", 1000) # Mở thẻ nạp sẵn 1000
acc.deposit(500)   # Dư 1500
acc.withdraw(2000) # Lỗi: Không đủ tiền
acc.withdraw(200)  # Dư 1300
acc.show_balance()