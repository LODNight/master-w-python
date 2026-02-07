# Tình huống: Hệ thống LMS cho phép thanh toán qua nhiều cổng: Thẻ tín dụng, Ví Momo, hoặc Chuyển khoản.
#  Dù cổng nào thì cũng phải có hành động process_payment(amount).

# Class Cha Payment: Có hàm process_payment chỉ in ra "Đang xử lý...".
# Class Con CreditCard: Ghi đè hàm trên -> In ra "Thanh toán [amount] bằng thẻ VISA".
# Class Con Momo: Ghi đè hàm trên -> In ra "Thanh toán [amount] bằng ví Momo".

# Yêu cầu: Viết code để khi gọi hàm pay(payment_method, amount), nó tự động chạy đúng logic của từng loại ví.

# Class CHA
class Payment():
    def process_payment(self, amount):
        print(f"Đang xử lý...")

# Class Con  CreditCard
class CreditCard(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)
        print(f"Thanh toán [{amount}] bằng thẻ VISA")


class Momo(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)
        print(f"💸 Trừ tiền ví Momo: -[{amount}] VND")

# --- TEST CASE ---
def pay(method, amount):
    method.process_payment(amount)

visa = CreditCard()
momo = Momo()

pay(visa, 100000) # Mong đợi: 💳 Quẹt thẻ VISA...
pay(momo, 50000)  # Mong đợi: 💸 Trừ tiền ví Momo...