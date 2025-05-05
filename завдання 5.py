class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    def display_info(self):
        print(f"Товар: {self.name}")
        print(f"Ціна: {self.price} грн")
        print(f"Кількість: {self.quantity}")
        print(f"Загальна вартість: {self.calculate_total_price()} грн")
product = Product("Комп'ютер", 40000, 5)
product.display_info()