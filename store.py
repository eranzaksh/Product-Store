class Store:
    """
  Creatinga store object
  """

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        """
    Adding a product to the store
    """
        self.list_of_products.append(product)

    def remove_product(self, product):
        """
    Removing a product from the store
    """
        self.list_of_products.remove(product)

    def list_all_products(self):
        """
    Return a string of all the products in the store
    """
        store_products = ""
        all_products = self.get_all_products()
        for product in all_products:
            store_products += product.show()
            store_products += '\n'
        return store_products

    def get_total_quantity(self):
        """
    Return a total of the products quantity
    """
        total = 0
        for product in self.list_of_products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """
    Creating a list of all the ACTIVE products in the store
    """
        active_products = [product for product in self.list_of_products
                           if product.is_active()]
        return active_products

    @staticmethod
    def order(shopping_list):
        """
    Order products based on the shopping list
    """
        total_price = 0
        for product in shopping_list:
            total_price += (product[0].buy(product[1]))
        return float(total_price)

    @staticmethod
    def check_inventory(product):
        """
    Check the inventory of a specific object
    """
        return product.get_quantity()
