class Product:
    """
    Represents a product available for purchase in the store.

        Attributes:
            name (str): The name of the product.
            price (float): The price per unit.
            quantity (int): The current stock quantity.
            active (bool): Whether the product is available for purchase.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a Product instance.

                Args:
                    name (str): The product name. Must not be empty.
                    price (float): The unit price. Must not be negative.
                    quantity (int): The initial stock quantity. Must not be negative.

                Raises:
                    ValueError: If name is empty, price is negative, or quantity is negative.
        """
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True # Products are active by default upon creation

    def show(self):
        """Print the product's name, price, and current quantity."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def get_quantity(self):
        """Return the current stock quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set the stock quantity and deactivate the product if it reaches zero.

                Args:
                    quantity (int): The new stock quantity.
        """
        self.quantity = quantity

        # Automatically deactivate the product when it goes out of stock
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """
        Check whether the product is currently active.

                Returns:
                    bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """Mark the product as active, making it available for purchase."""
        self.active = True

    def deactivate(self):
        """Mark the product as inactive, removing it from available inventory."""
        self.active = False

    def buy(self, quantity):
        """
        Purchase a given quantity of the product and update stock.
        Deactivates the product automatically if stock reaches zero after purchase.
                Args:
                    quantity (int): The number of units to purchase.

                Returns:
                    float: The total cost for the purchased quantity.
        """
        self.quantity -= quantity

        # Deactivate the product if it's now out of stock
        if self.quantity == 0:
            self.deactivate()
        return quantity * self.price



