import products
import store
import sys
import promotions


def create_product_list():
    """Generates the total inventory of products in the 
    store and assigns promotions if they exist."""
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds",
                                     price=250, quantity=500),
                    products.Product("Google Pixel 7",
                                     price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct(
                        "Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    return store.Store(product_list)


def list_all_products(store_obj):
    """Displays a list of all products in inventory."""
    prod_list = store_obj.get_all_products()
    product_index = 1
    print("------")
    for product in prod_list:
        print(f"{product_index}. {product.show()}")
        product_index += 1
    print("------")
    start(store_obj)


def show_total_amount(store_obj):
    """Displays total amount of products in the inventory."""
    total_quantities = store_obj.get_total_quantity()
    print(f"Total of {total_quantities} items in store")
    start(store_obj)


def make_an_order(store_obj):
    """Allows customer to place a purchase order."""
    prod_list = store_obj.get_all_products()
    curr_index = 1
    print("------")
    for product in prod_list:
        print(f"{curr_index}. {product.show()}")
        curr_index += 1
    print("------")
    shopping_list = []
    input1 = "#"
    input2 = "#"
    print("When you want to finish order, empty text")
    while len(input1) > 0 and len(input2) > 0:
        input1 = input("Which product # do you want? ")
        input2 = input("What amount do you want? ")
        if input1.isdigit() and input2.isdigit():
            product = int(input1)
            amount = int(input2)
        else:
            break
        shopping_list.append(
            (prod_list[product - 1].name, amount)
        )
        print("Product added to list!")
        print()
    total_payment = store_obj.order(shopping_list)
    print("********")
    print(f"Order made! Total payment: ${int(total_payment)}")
    start(store_obj)


def exit_app():
    """Terminates the application."""
    sys.exit()


def menu_dispatcher(selection):
    """Creates a dispatcher for running menu requests"""
    menu = {
        1: list_all_products,
        2: show_total_amount,
        3: make_an_order,
        4: exit_app
    }
    return menu[selection]


def start(store_obj):
    """Displays a menu of commands available to customers."""
    choices = """
       Store Menu
       ----------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
    """
    print(choices)
    selection = int(input("Please choose a number: "))
    while selection not in [1, 2, 3, 4]:
        print(choices)
        selection = int(input("Please choose a number: "))
    menu = menu_dispatcher(selection)
    if selection == 4:
        menu()
    menu(store_obj)


def main():
    """Generates a product list object and initiates the 
    application."""
    best_buy = create_product_list()
    start(best_buy)


if __name__ == "__main__":
    main()
