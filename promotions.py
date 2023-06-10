from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for promotions.
    """

    def __init__(self, name):
        """
        Initialize a promotion.

        Parameters:
        - name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(product, quantity) -> float:
        """
        Apply the promotion to a product and quantity.

        Parameters:
        - product: The product to apply the promotion to.
        - quantity: The quantity of the product.

        Returns:
        - float: The discounted price after applying the promotion.
        """
        pass


class PercentDiscount(Promotion):
    """
    A promotion that applies a percentage discount to the total price.
    """

    def __init__(self, name, percent):
        """
        Initialize a percent discount promotion.

        Parameters:
        - name (str): The name of the promotion.
        - percent (float): The percentage discount to apply.
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """
        Apply the percentage discount to the product price.

        Parameters:
        - product: The product to apply the discount to.
        - quantity: The quantity of the product.

        Returns:
        - float: The discounted price after applying the promotion.
        """
        discounted_price = ((100 - self.percent) / 100) * \
            product.price * quantity
        return discounted_price


class SecondHalfPrice(Promotion):
    """
    A promotion that applies a discount for every second item at half price.
    """

    def apply_promotion(self, product, quantity) -> float:
        """
        Apply the second half price promotion.

        Parameters:
        - product: The product to apply the promotion to.
        - quantity: The quantity of the product.

        Returns:
        - float: The discounted price after applying the promotion.
        """
        half_price = (quantity // 2) * (product.price / 2)
        full_price = (quantity - (quantity // 2)) * product.price
        return half_price + full_price


class ThirdOneFree(Promotion):
    """
    A promotion that provides one item for free for every three items.
    """

    def apply_promotion(self, product, quantity) -> float:
        """
        Apply the third one free promotion.

        Parameters:
        - product: The product to apply the promotion to.
        - quantity: The quantity of the product.

        Returns:
        - float: The discounted price after applying the promotion.
        """
        full_price_items = quantity - (quantity // 3)
        return full_price_items * product.price
