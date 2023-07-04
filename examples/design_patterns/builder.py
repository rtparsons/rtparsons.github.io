from datetime import date
from dataclasses import dataclass


@dataclass
class Product():
    created_by: str
    product_name: str
    cost: int

    def __str__(self) -> str:
        return f'Product: {self.created_by=}, {self.product_name=}, {self.cost=}'



class PerishableProduct(Product):
    use_by_date: date

    def __init__(self, created_by: str, product_name: str, cost: int, use_by_date: date) -> None:
        super().__init__(created_by, product_name, cost)
        self.use_by_date = use_by_date

    def __str__(self) -> str:
        return f'PerishableProduct: {super().__str__()}, {self.use_by_date=}'


class ProductBuilder():
    created_by: str = ''
    product_name: str = ''
    cost: int = 0
    use_by_date: date = None
    
    def build(self, product_name: str, cost: int):
        if self.use_by_date:
            return PerishableProduct(self.created_by, product_name, cost, self.use_by_date)
        return Product(self.created_by, product_name, cost)

builder = ProductBuilder()
builder.created_by = 'rob'
builder.use_by_date = None
product = builder.build('product 1', 1)
product2 = builder.build('product 2', 2)
builder.use_by_date = date(2023, 7, 1)
product3 = builder.build('product3', 3)

print(product)
print(product2)
print(product3)
