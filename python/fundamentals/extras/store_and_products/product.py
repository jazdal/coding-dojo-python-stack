import random

class Product:
    def __init__(self, product_name, price, category):
        self.product_id = random.randint(1, 100)
        self.product_name = product_name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        return self
    
    def print_info(self):
        print()
        print(f'{self.product_id} - {self.product_name} ({self.category}): PHP{self.price}')
        return self