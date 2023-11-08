---
layout: post
title:  "Factory pattern in Python"
date:   2023-07-10 20:00:00 +0000
categories: python design-patterns
permalink: /the-factory-pattern-in-python/
---

The factory pattern (or factory method pattern) is a creational design pattern which abstracts away the creation of objects via a factory class. This allows us to defer object creation and alter the type of objects created at runtime.

### Example

```python
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
    def __init__(self, username: str):
        self.created_by = username
    
    def create_product(self, product_name: str, cost: int, use_by_date: date=None) -> Product:
        if use_by_date:
            return PerishableProduct(self.created_by, product_name, cost, use_by_date)
        return Product(self.created_by, product_name, cost)

factory = ProductFactory('rob')
product = factory.create_product('item1', 100, None)
product2 = factory.create_product('item1', 100, date(1999, 12, 31))
print(product)
print(product2)
```

The core component in this example is `ProductFactory` and the `create_product` method. This takes details about the product we want to create via the method arguments and then determines what type of product we want to create based on them. As both products share a common interface, whatever calls this can code against the generic `BaseProduct` interface and not worry about the implementation details.

### Why use it?

Let's consider an example where you wish to take some legacy code and add a unit test to it. This code creates a new `Product` object and then calls purchase on it which goes on and contacts a third-party API to purchase the product. We wouldn't want that code to be executed under test...

We could just wrap the offending code with something like `if not is_test:`, but this would only fix this instance and is not very helpful if you have multiple calls you wish to stud out. In this case, we could use the factory pattern to abstract that if condition away and then return a mocked object at test time.

This also aids with future extensibility as if we wish to implement a new version of the `Product` class with a differing implementation, it is now much simpler. All we would need to do is add the new product to the builder, and the calling code would not need to be altered as they are only concerned with the interface.
