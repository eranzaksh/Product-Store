import sys
import products
import store
import promotions


def quit_program():
    """
    Quits the program
    """
    sys.exit()


def make_order(store_obj):
    """
    Takes user input to order items and when done calculate,
    if items are in stock then show total order.
    if items are not in stock output a message and cancel the order.
    """
    list_products(store_obj)
    print("\n*****Press '0' anytime to finish the order*****\n")
    all_products = store_obj.get_all_products()
    user_order = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    overall_payment = 0
    product_payment = 0
    while True:
        try:
            user_product = int(input("What product do you want?\n"
                                     "choose according to the corresponding numbers: "))
            if user_product == 0:
                break
            if user_product > len(all_products):
                print("Invalid product number, please try again.")
                continue
            user_quantity = int(input("Enter the amount you want: "))
            if user_quantity == 0:
                break
            user_order[user_product] += user_quantity
            print("Product added to the shopping list!")
        except ValueError:
            print("****Please enter only numbers.****")
            continue
    if sum(user_order.values()) != 0:
        # Check if there are any items at all.
        for orders, quantity in user_order.items():
            if quantity > (store_obj.check_inventory(all_products[orders - 1])) \
                    or user_order[5] > store_obj.check_limitation(all_products[4]):
                print("Not enough quantity in store, order canceled!")
                return 0
        print("\n***** Total Order *****")
        for orders, quantity in user_order.items():
            product_payment = store_obj.order([(all_products[orders - 1], quantity)])
            print(f"{all_products[orders - 1].name}, Amount Ordered: {quantity}, Price: {product_payment}$")
            overall_payment += product_payment
        print(f"Order made! overall payment is: ${overall_payment}")
    else:
        print("No order was made!")
        return 0


def total_quantity(store_obj):
    """
    Prints the total items quantity
    """
    print(f"\nStore total item quantity is: {store_obj.get_total_quantity()}")


def list_products(store_obj):
    """
    Prints all the items in inventory
    """
    print("---------------------------------------")
    for product in store_obj.get_all_products():
        print(product.show())
    print("---------------------------------------")


def start(store_obj):
    """
    Start menu
    """
    while True:
        user_choice = input("""
       * Store menu * 
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number: """)
        if user_choice == '1':
            list_products(store_obj)
        if user_choice == '2':
            total_quantity(store_obj)
        if user_choice == '3':
            make_order(store_obj)
        if user_choice == '4':
            quit_program()


def main():
    """
    Initializing the store with products
    """
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    best_buy = store.Store(product_list)
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    product_list[0].set_promotion(thirty_percent)
    start(best_buy)


if __name__ == "__main__":
    main()
