---
layout: post
title:  "The strategy pattern in python"
date:   2023-05-01 20:00:00 +0000
categories: python design-patterns
permalink: /the-strategy-pattern-in-python/
---

The Strategy Pattern is a behavioral pattern that defines a set of algorithms, encapsulates each one, and makes them interchangeable within a context. This pattern allows the algorithms to vary independently of the clients that use them. The Strategy Pattern is useful when we have multiple algorithms that can be used to solve a problem, and we want to choose the best one for the situation at runtime.

Lets consider the following example which selects and applies a discount to a cost.

```python
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
```

Whilst the example is quite simple follow, it's easy to imagine how the code here could quickly get out of hand with more discount types, or more complex discount calculations. Let's improve this by implementing the strategy pattern.  

```python
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
```

The Strategy Pattern consists of three components:

1. Context: It is the class that contains a reference to the current strategy object.

2. Strategy: It is the interface that defines the contract for the different algorithms.

3. ConcreteStrategy: It is the class that implements the Strategy interface and contains the algorithm's implementation.


In the above example, we first define the `DiscountStrategy` interface, which defines the contract for the different discount calculation algorithms. Then we define three concrete strategies, `PercentageDiscount`, `FixedAmountDiscount` and `HalfPriceDiscount`, which implement the `DiscountStrategy` interface and contain the algorithm's implementation.

Finally, we define the `DiscountContext` class, which contains a reference to the current strategy object and provides a way to change the strategy at runtime. The `apply_discount` method of the `DiscountContext` class delegates the discount calculation to the current strategy object.

The most Pythonic way to implement the Strategy Pattern in Python is by using the `abc` module to define abstract base classes and methods. This allows us to define interfaces and enforce their implementation by concrete classes.

The Strategy Pattern has several strengths, including:
1. Encapsulates algorithms: The Strategy Pattern encapsulates each algorithm in a separate class, making it easier to maintain and modify.
2. Provides flexibility: The Strategy Pattern allows us to change the algorithm at runtime, providing flexibility to the application.
3. Enhances code reuse: The Strategy Pattern promotes code reuse by allowing us to reuse the same algorithm in different contexts.

However, the Strategy Pattern also has some weaknesses, including:
1. Increased complexity: The Strategy Pattern adds additional complexity to the code, which can make it harder to understand and maintain.
2. Increased number of classes: The Strategy Pattern requires the creation of multiple classes, which can lead to code bloat and increased memory usage.

The Strategy Pattern is a powerful design pattern that can help in creating more maintainable and reusable code. By encapsulating different discount calculation algorithms in separate classes, we can make our code more modular and flexible, and by using the Strategy Pattern, we can change the discount calculation algorithm at runtime to meet the changing needs of our application.