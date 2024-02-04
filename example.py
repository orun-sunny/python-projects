class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print(f"Products in {self.name}:")

        for product in self.products:
            product.display_info()

# Example usage:
product1 = Product("Laptop", 999.99, 10)
product2 = Product("Smartphone", 299.99, 20)

shop = Shop("Electronics Store")
shop.add_product(product1)
shop.add_product(product2)

shop.display_products()
