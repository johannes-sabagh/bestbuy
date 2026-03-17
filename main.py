"""
Sets up the product inventory, initializes the store, and launches
the interactive menu for the user.
"""



import products
import store

# Set up the initial stock of inventory with product name, price, and quantity
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]

# Create the store instance with the initial product list
best_buy = store.Store(product_list)



def make_order(best_buy):
    """
    Interactively build and place an order from the store's active products.

        Prompts the user to select products by number and specify quantities.
        Continues accepting inputs until the user submits an empty entry.
        Displays the total order cost upon successful completion.

        Args:
            best_buy (Store): The store instance to place the order with.
    """
    active_products = best_buy.get_all_products()
    print("------")
    print("When you want to finish order, enter empty text.")

    shopping_list = []

    while True:
        product_input = input("Which product # do you want? ").strip()
        if product_input == "":
            break # User signals end of order with empty input
        amount_input = input("What amount do you want? ").strip()
        if amount_input == "":
            break # Also allow exiting at the amount prompt

        try:
            product_num = int(product_input)
            amount = int(amount_input)

            # Validate the product number is within the available range
            if product_num < 1 or product_num > len(active_products):
                print("Invalid product number, please try again.")
                continue

            # Ensure the user is ordering at least one item
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            # Add the selected product and quantity to the shopping list
            selected_product = active_products[product_num - 1]
            shopping_list.append((selected_product, amount))
            print("Product added to list!")

        except ValueError:
            # Catch non-integer inputs for product number or amount
            print("Invalid input, please enter a number.")
            continue

    # Place the order only if the user added at least one item
    if shopping_list:
        print("********")
        total = best_buy.order(shopping_list)
        print(f"Order made! Total payment: ${total}")
    else:
        print("No items ordered.")


def start(best_buy):
    """
    Launch the main menu loop for the store application.

        Displays a menu and routes user input to the appropriate action:
        listing products, showing total inventory, placing an order, or quitting.

        Args:
            best_buy (Store): The store instance to operate on.
    """

    def list_products():
        print("---------")
        best_buy.get_all_products()
        print("---------")

    def show_total():
        print(f"Total of {best_buy.get_total_quantity()} items in store")

    def place_order():
        make_order(best_buy)

    menu = {
        1: list_products,
        2: show_total,
        3: place_order,
    }

    while True:
        # Display the main menu options
        print("---------")
        print("Store Menu")
        print("---------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        try:
            user_choice = int(input("Please choose a number: "))
            if user_choice == 4:
                break
            elif user_choice in menu:
                menu[user_choice]()
                input("Press enter to continue")
            else:
                print("invalid input")
        except Exception as e:
            print(f"Error: {e}")

def main():
    """Main entry point — starts the store application."""
    start(best_buy)

if __name__ == "__main__":
    main()