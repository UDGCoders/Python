class Product:
    def __init__(self,name,price):
        self.name=name
        self.__price=price

    def get_price(self):
        return self.__price

class Warehouse():
    def __init__(self):
        self.inventory=[]
        
    def add_product(self,product):
        self.inventory.append(product)

    def get_total_value(self):
        
        total_value = 0
        for product in self.inventory:
            total_value += product.get_price()

        return total_value
        
