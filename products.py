class Product:
    """
  Creating a product object
  """

    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise TypeError("Invalid input!")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """
    Getting quantity of an object
    """
        return float(self.quantity)

    def set_quantity(self, quantity):
        """
    Setting the quantity of an object and reaise an exception if
    it goes below 0
    """
        if self.quantity - quantity == 0:
            self.quantity = self.quantity - quantity
            self.active = False
        elif self.quantity - quantity < 0:
            raise ValueError("Quantity cannot get below 0!")
        else:
            self.quantity = self.quantity - quantity

    def is_active(self):
        """
    Check if a product object is active
    """
        return self.active

    def activate(self):
        """
    Setting a product to active state
    """
        self.active = True

    def deactivate(self):
        """
    Setting a product to deactivate state
    """
        self.active = False

    def show(self):
        """
    returns the name, price, and quantity of a product
    """
        return f"{self.name}, Price:{self.price}, Quantity:{self.quantity}"

    def buy(self, quantity):
        """
    Setting the product price and quantity base on what the user buys
    """
        try:
            self.set_quantity(quantity)
            total_price = self.price * quantity
            return float(total_price)
        except ValueError:
            print(f"Not enough {self.name} in stock!")
            return 0
