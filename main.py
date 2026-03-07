import products
import store
from store import Store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)



def make_order(best_buy):
    active_products = best_buy.get_all_products()
    print("------")
    print("When you want to finish order, enter empty text.")

    shopping_list = []

    while True:
        product_input = input("Which product # do you want? ").strip()
        if product_input == "":
            break
        amount_input = input("What amount do you want? ").strip()
        if amount_input == "":
            break

        try:
            product_num = int(product_input)
            amount = int(amount_input)

            if product_num < 1 or product_num > len(active_products):
                print("Invalid product number, please try again.")
                continue
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            selected_product = active_products[product_num - 1]
            shopping_list.append((selected_product, amount))
            print("Product added to list!")

        except ValueError:
            print("Invalid input, please enter a number.")
            continue

    if shopping_list:
        print("********")
        total = best_buy.order(shopping_list)
        print(f"Order made! Total payment: ${total}")
    else:
        print("No items ordered.")


def start(best_buy):

    while True:
        print("---------")
        print("Store Menu")
        print("---------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        try:
            user_choice = int(input("Please choose a number: "))
            if user_choice == 1:
                print("---------")
                best_buy.get_all_products()
                print("---------")
                input("Press enter to continue")

            elif user_choice == 2:
                print(f"Total of {best_buy.get_total_quantity()} items in store")
                input("Press enter to continue")
            elif user_choice == 3:
                make_order(best_buy)
                input("Press enter to continue")

            elif user_choice == 4:
                    input("Press enter to continue")
            else:
                print("invalid input")
        except Exception as e:
            print(f"Error: {e}")

def main():
    start(best_buy)

if __name__ == "__main__":
    main()