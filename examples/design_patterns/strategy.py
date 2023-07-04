from decimal import Decimal

cost = Decimal(100)
discount_type = 'fixed'
discount_value = Decimal(5)

if discount_type == 'fixed':
    cost -= discount_value
elif discount_type == 'percentage':
    cost = cost * (Decimal(1) - (discount_value / Decimal(100)))
elif discount_type == 'half price':
    cost = cost * Decimal(0.5)

print(cost)


from abc import ABC, abstractmethod
from decimal import Decimal


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, cost, discount_value):
        pass


class FixedAmountDiscount(DiscountStrategy):
    def apply_discount(self, cost, discount_value):
        return cost - discount_value


class PercentageDiscount(DiscountStrategy):
    def apply_discount(self, cost, discount_value):
        return cost * (Decimal(1) - (discount_value / Decimal(100)))


class HalfPriceDiscount(DiscountStrategy):
    def apply_discount(self, cost, discount_value):
        return cost * Decimal(0.5)


class DiscountContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def apply_discount(self, cost, discount_value):
        return self._strategy.apply_discount(cost, discount_value)

cost = Decimal(100)
discount_value = Decimal(5)
strategy = FixedAmountDiscount()
result = DiscountContext(strategy).apply_discount(cost, discount_value)
print(result)


