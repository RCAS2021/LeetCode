# Dataclass will automatically make the __init__, __repr__, __eq__ methods and more.
'''
class Product:
    """ Product class """
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self) -> float:
        """ Calculates and return total cost """
        return self.price * self.quantity

    def __repr__(self):
        return f"Product name = {self.name}, price = {self.price}, quantity = {self.quantity}"

    def __eq__(self, other):
        if not isinstance(other, Product):
            # Don't attempt to compare between different types
            return NotImplemented

        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity)
'''

# Using dataclass
from dataclasses import dataclass

@dataclass
class Product:
    """ Product class """
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        """ Calculates and return total cost """
        return self.price * self.quantity

# Testing
p1 = Product(name="Product 1", price=10, quantity=5)
p2 = Product(name="Product 2", price=15, quantity=3)
p3 = Product(name="Product 1", price=10, quantity=5)

print(p1)
print(p1.total_cost())
print(p1 == p2)
print(p1 == p3)
