class Product:

    def __init__(self, name, price, quantity):
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def buy(self, quantity):
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return quantity * self.price



