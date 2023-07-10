from dataclasses import dataclass
from abc import ABC


@dataclass
class Item:
    name: str
    cost: int


class Discount(ABC):
    def calculate_discount(self, items: list[Item]) -> int:
        pass


class CalculateDiscountImplementation(ABC):
    def calculate_discount(self, items: list[Item], discount_value: int) -> int:
        pass


class FixedDiscount(Discount):
    def __init__(self, amount: int, calculate_discount_impl: CalculateDiscountImplementation) -> None:
        super().__init__()
        self.amount = amount
        self.calculate_discount_impl = calculate_discount_impl

    def calculate_discount(self, items: list[Item]) -> int:
        return self.calculate_discount_impl.calculate_discount(items, self.amount)


class FixedDiscountImplementation(CalculateDiscountImplementation):
    def calculate_discount(self, items: list[Item], discount_value: int) -> int:
        return sum([x.cost for x in items]) - discount_value


class FixedDiscountImplementationMinSpend(CalculateDiscountImplementation):
    def __init__(self, min_spend: int) -> None:
        super().__init__()
        self.min_spend = min_spend

    def calculate_discount(self, items: list[Item], discount_value: int) -> int:
        items_total: int = sum([x.cost for x in items])
        if items_total > self.min_spend:
            return items_total - discount_value
        return items_total

items1 = []
items2 = [Item('Apple', 5)]
items3 = [Item('Apple', 5), Item('Orange', 6)]

fixed_discount = FixedDiscount(2, FixedDiscountImplementation())
fixed_discount_min_spend = FixedDiscount(2, FixedDiscountImplementationMinSpend(10))

print(fixed_discount.calculate_discount(items1))
print(fixed_discount.calculate_discount(items2))
print(fixed_discount.calculate_discount(items3))

print(fixed_discount_min_spend.calculate_discount(items1))
print(fixed_discount_min_spend.calculate_discount(items2))
print(fixed_discount_min_spend.calculate_discount(items3))
