import copy
from datetime import date


class Product():
    created_by: str
    product_name: str
    cost: int
    hash: str

    def __init__(self, created_by: str, product_name: str, cost: int) -> None:
        self.created_by = created_by
        self.product_name = product_name
        self.cost = cost
        self.hash = hash(f'{created_by}::{product_name}::{cost}')


    def __str__(self) -> str:
        return f'Product: {self.created_by=}, {self.product_name=}, {self.cost=}, {self.hash=}'


    def clone(self):
        return copy.deepcopy(self)


product = Product('rob', 'product 1', 1)
product2 = product.clone()

print(product)
print(product2)

product.cost = 3

print(product)
print(product2)
