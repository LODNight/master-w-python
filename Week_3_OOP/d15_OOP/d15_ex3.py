# Thuộc tính: name, price, quantity (số lượng tồn kho).

# Hành động:
# get_total_value(): Tính tổng giá trị lô hàng này (price * quantity). -> Return kết quả.
# sell(amount): Bán hàng. Giảm quantity đi. Nếu không đủ hàng thì báo "Hết hàng".

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        return self.price * self.quantity

    def sell(self, amount):
        if 0 < amount < self.quantity:
            self.quantity -= amount
            print(f"Bán {amount} cái. Còn lại {self.quantity}")
        else: 
            print(f"Error: Không bán được. Số lượng hiện tại: {self.quantity}")


# --- TEST ---
p1 = Product("Laptop", 1000, 5) # Có 5 cái, giá 1000/cái
print(f"Giá trị kho: {p1.get_total_value()}") # Mong đợi: 5000

p1.sell(2) # Bán 2 cái -> Còn 3
p1.sell(10) # Bán 10 cái -> Báo lỗi
print(f"Tồn kho còn: {p1.quantity}") # Mong đợi: 3