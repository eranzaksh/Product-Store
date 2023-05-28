from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.discount = percent

    def apply_promotion(self, product, quantity):
        discount_percentage = float(self.discount) / 100
        normal_price = product.price * quantity
        discounted_price = normal_price - (normal_price * discount_percentage)
        return discounted_price


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        normal_price = product.price * quantity
        discounted_price = int(normal_price) - (int(normal_price) * 0.25)
        if quantity % 2 == 0:
            return discounted_price
        else:
            discounted_price += (product.price * 1)
            return discounted_price


class ThirdOneFree(Promotion):
    pass
