import products
class Store:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.quantity
        return total

    def get_all_products(self):
        for product in self.products:
            if product.quantity > 0:
                print(product)
            else:
                continue

    def order(self, shopping_list):




bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)
store = Store()
store.add_product(bose)
store.add_product(mac)
print(store.products)