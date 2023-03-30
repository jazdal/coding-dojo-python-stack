class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.products = []
    
    def show_products(self):
        print()
        [print(f'{product.product_id} - {product.product_name} ({product.category}): PHP {product.price}') for product in self.products]
        return self
    
    def add_product(self, new_product):
        print()
        print(f'Adding {new_product.product_name} to store inventory...')
        self.products.append(new_product)
        print()
        print("Current inventory contents:")
        self.show_products()
        return self
    
    def sell_product(self, id):
        print()
        print(f'{self.products[id].product_name} has been sold. Updating product inventory...')
        del self.products[id]
        self.show_products()
        return self
    
    def inflation(self, percent_increase):
        [product.update_price(percent_increase, True) for product in self.products]
        self.show_products()
        return self
    
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        self.show_products()
        return self