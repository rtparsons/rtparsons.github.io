from abc import ABC
from datetime import date
from dataclasses import dataclass


@dataclass
class BaseProduct(ABC):
    created_by: str
    product_name: str
    cost: int

    def __str__(self) -> str:
        return f'{self.created_by=}, {self.product_name=}, {self.cost=}'


class Product(BaseProduct):
    def __init__(self, created_by: str, product_name: str, cost: int) -> None:
        super().__init__(created_by, product_name, cost)

    def __str__(self) -> str:
        return f'Product: {super().__str__()}'


class PerishableProduct(BaseProduct):
    use_by_date: date

    def __init__(self, created_by: str, product_name: str, cost: int, use_by_date: date) -> None:
        super().__init__(created_by, product_name, cost)
        self.use_by_date = use_by_date

    def __str__(self) -> str:
        return f'PerishableProduct: {super().__str__()}, {self.use_by_date=}'


class ProductFactory():
    def __init__(self, username):
        self.created_by = username
    
    def create_product(self, product_name: str, cost: int, use_by_date: date=None):
        if use_by_date:
            return PerishableProduct(self.created_by, product_name, cost, use_by_date)
        return Product(self.created_by, product_name, cost)

factory = ProductFactory('rob')
product = factory.create_product('item1', 100, None)
product2 = factory.create_product('item1', 100, date(1999, 12, 31))
print(product)
print(product2)