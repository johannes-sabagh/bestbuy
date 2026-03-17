
class Store:
    """Represents a store that manages a collection of products.

        Attributes:
            products (list): A list of Product instances in the store's inventory.
    """

    def __init__(self, products=None):
        """
        Initialize the Store with an optional list of products.

               Args:
                   products (list, optional): Initial list of Product instances.
                       Defaults to an empty list if not provided.
        """

        if products is not None:
            if not isinstance(products, list):
                raise TypeError("products must be a list.")
            for item in products:
                if not isinstance(getattr(item, "name", None), str) or not isinstance(getattr(item, "price", None), (int, float)):
                    raise TypeError("Each product must have a name (str) and price (int or float).")
            self.products = products
        else:
            self.products = []

    def add_product(self, product):
        """
        Add a product to the store's inventory.

                Args:
                    product (Product): The product to add.

                Raises:
                    TypeError: If the object is not a valid product.
        """

        if not isinstance(getattr(product, "name", None), str) or not isinstance(getattr(product, "price", None), (int, float)):
            raise TypeError("product must have a name (str) and price (int or float).")
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store's inventory.

               Args:
                   product (Product): The product to remove.

               Raises:
                   TypeError: If the object is not a valid product.
                   ValueError: If the product is not found in the inventory.
        """

        if not isinstance(getattr(product, "name", None), str) or not isinstance(getattr(product, "price", None), (int, float)):
            raise TypeError("product must have a name (str) and price (int or float).")
        self.products.remove(product)

    def get_total_quantity(self):
        """
        Calculate the total number of items across all products.

                Returns:
                    int: The sum of quantities for all products in the store.
        """

        total = 0
        for product in self.products:
            total += product.quantity
        return total

    def get_all_products(self):
        """
        Print and return all currently active products.

                Displays a numbered list of active products with their name,
                price, and available quantity.

                Returns:
                    list: A list of active Product instances.
        """

        # Filter to only products that are currently active
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
        """
        Process an order for multiple products and return the total cost.

                Validates stock availability for each item before processing.
                Deducts purchased quantities from each product's inventory.

                Args:
                    shopping_list (list of tuple): Each tuple contains a Product instance
                        and the desired purchase quantity, e.g. [(product, quantity), ...].

                Returns:
                    float: The total cost of the entire order.

                Raises:
                    Exception: If a product is inactive or has insufficient stock.
        """

        total_price = 0
        for product, quantity in shopping_list:
            # Ensure the product is still available before purchasing
            if not product.is_active():
                raise Exception(f"{product.name} is not available.")

            # Ensure there is enough stock to fulfill the requested quantity
            if quantity > product.get_quantity():
                raise Exception(f"Not enough stock for {product.name}.")
            total_price += product.buy(quantity)
        return total_price



