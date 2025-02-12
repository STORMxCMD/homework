class Product:
    def __init__(self, name, price, quantity, company):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.company=company

    def info(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Company:{self.company} "


class Company:
    def __init__(self, name, age):
        self.name=name
        self.age=age


class Basket:
    def __init__(self, products):
        self.products=products
        
    