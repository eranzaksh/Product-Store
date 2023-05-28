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
        """
        Basically second in half price means as long as the order is an even number there is a 25% discount
        so i check for even number. if it does - there is a 25% discount on all the order. if not - means there is
        1 adder to add with full price
        """
        normal_price = product.price * quantity
        if quantity > 1:
            if quantity % 2 == 0:
                discounted_price = int(normal_price) - (int(normal_price) * 0.25)
                return discounted_price
            else:
                #Quantity - 1 will be an even number which has a 25% discount on it. then i add another 1 full price.
                normal_price_for_discount = product.price * (quantity - 1)
                discounted_price = int(normal_price_for_discount) - (int(normal_price_for_discount) * 0.25)
                discounted_price += product.price * 1
                return discounted_price
        else:
<<<<<<< HEAD
            return normal_price
=======
            return None
>>>>>>> 1e11399a7380cc6c99d44ae464ba902dfb4a2e1c


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
<<<<<<< HEAD
        normal_price = product.price * quantity
        if quantity > 2:
            if quantity % 3 == 0:
                discounted_price = int(normal_price) - (int(normal_price) / 3)
                return discounted_price
            no_discounted_quantity = quantity % 3
            normal_price_for_discount = product.price * (quantity - no_discounted_quantity)
            discounted_price = normal_price_for_discount - (normal_price_for_discount / 3)
            discounted_price += product.price * no_discounted_quantity
            return discounted_price
        else:
            return normal_price
=======
>>>>>>> 1e11399a7380cc6c99d44ae464ba902dfb4a2e1c

