import products
class Store:
    def __init__(self, products=None):
        if products is not None:
            self.products = products
        else:
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
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        i = 1
        for product in active_products:
            print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            i += 1
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise Exception(f"{product.name} is not available.")
            if quantity > product.get_quantity():
                raise Exception(f"Not enough stock for {product.name}.")
            total_price += product.buy(quantity)
        return total_price



