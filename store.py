import products


class Store:
    """A class representing a store."""

    def __init__(self, products_list):
        """
        Initialize a Store object.

        Parameters:
        - products_list (list): A list of Product objects representing the initial products in the store.
        """
        self.products_list = products_list

    def add_product(self, product):
        """
        Add a product to the store's product list.

        Parameters:
        - product (Product): A Product object to be added.
        """
        quantity = product.get_quantity()
        for existing_product in self.product_list:
            if existing_product.name == product.name:
                raise ValueError("Product already exists in the store.")
        self.products_list.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store's product list.

        Parameters:
        - product (Product): A Product object to be removed.
        """
        try:
            self.products_list.remove(product)
        except ValueError:
            print("Product not found.")

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of all active products in the store.

        Returns:
        - int: The total quantity of active products.
        """
        total_quantity = 0
        for product in self.products_list:
            if product.is_active():
                total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> list:
        """
        Get a list of all active products in the store.

        Returns:
        - list: A list of active Product objects in the store.
        """
        active_products = []
        for product in self.products_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """
        Process an order and calculate the total price.

        Parameters:
        - shopping_list (list): A list of tuples representing the products and quantities to order.

        Returns:
        - float: The total price of the order.
        """
        total_price = 0.0
        for name, quantity in shopping_list:
            for product in self.products_list:
                if product.name == name:
                    if quantity <= 0:
                        print("Invalid quantity for", name)
                        break
                    if quantity > product.quantity and type(product) != products.NonStockedProduct:
                        print(
                            f"Not enough stock for {name}. Available quantity: {product.quantity}")
                        break
                    if type(product) == products.LimitedProduct and quantity > product.maximum:
                        print(f"Purchase quantity for {product.name} cannot exceed" +
                              f" the max limit of {product.maximum} item per order.")
                        break
                    total_price += product.buy(quantity)
                    break
        return total_price
