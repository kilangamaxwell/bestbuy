class Product:
    """A class representing a product."""

    def __init__(self, name, price, quantity):
        """
        Initialize a Product object.

        Parameters:
        - name (str): The name of the product.
        - price (float): The price of the product.
        - quantity (int): The quantity of the product.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Get the quantity of the product.

        Returns:
        - int: The quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set the quantity of the product.

        Parameters:
        - quantity (int): The new quantity of the product.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """
        Check if the product is active.

        Returns:
        - bool: True if the product is active, False otherwise.
        """
        return self.active

    def deactivate(self) -> bool:
        """
        Deactivate the product.

        Returns:
        - bool: The updated activation status of the product.
        """
        if self.active:
            self.active = False
        return self.active

    def activate(self) -> bool:
        """
        Activate the product.

        Returns:
        - bool: The updated activation status of the product.
        """
        self.active = True
        return self.active

    def show(self) -> str:
        """
        Get a string representation of the product.

        Returns:
        - str: A string containing the name, price, and quantity of the product.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Process a purchase of the product.

        Parameters:
        - quantity (int): The quantity of the product to purchase.

        Returns:
        - float: The total price of the purchase.
        """
        if self.is_active() and self.quantity >= quantity:
            try:
                self.quantity -= quantity
            except Exception as error:
                print("Invalid Entry: Enter a numeric quantity.")
            price = self.price * quantity
            return price
        else:
            print(f"{self.name} not in stock.")
