---
layout: post
title:  "The adapter pattern in python"
date:   2023-04-15 20:00:00 +0000
categories: python design-patterns
---

The Adapter pattern is a design pattern that allows objects with incompatible interfaces to work together. It provides a way to convert the interface of an object into another interface that clients expect. This pattern is especially useful in situations where existing code needs to be integrated with new code that has different interfaces.

In Python, the Adapter pattern can be implemented using a combination of inheritance and composition. Let's take a look at how this can be done.

Suppose we have two classes that provide comparable data but in two different formats, and via two different interfaces. However, we wish to bring the two classes in line so that the format of the data and interfaces match and can be used interchangeably. In other words, we want the classes to have matching function signatures and return types.

To solve this problem, we can create an adapter class that inherits from the existing class and implements the new interface. This adapter class will then be used in the new project.

Here's an example. Suppose we have two existing classes `SupermarketOne` and `SupermarketTwo`. They both have their own functions for getting products with prices but return the data in different formats.

```
class SupermarketOne:
    def get_products(self):
        return {'apples': 0.2,
                'oranges': 0.3,
                'chicken': 4.12}


class SupermarketTwo:
    def get_fruit(self):
        return [('apples', 0.19), ('pears', 0.21)]

    def get_meat(self):
        return [('lamb', 6.17)]
```

Now suppose we want to combine the data from the two classes so that we can save it in a database. We could do this separately for each class and deal with their differences individually. This could cause lots of extra work if we had more classes, and even more if each class had multiple use cases. 

To solve this problem, we can create an adapter class for `SupermarketTwo` called `SupermarketTwoAdapter` that brings the feed in line with `SupermarketOne`. Here's how this can be done:

```
class SupermarketTwoAdapter:

    def __init__(self, supermarket_two):
        self.supermarket_two = supermarket_two

    def get_products(self):
        products = self.supermarket_two.get_fruit() + self.supermarket_two.get_meat()
        return dict(products)
```

In this implementation, `SupermarketTwoAdapter` takes an instance of `SupermarketTwo` and utilises that to combine the two calls to `get_fruit` and `get_meat` into a single `get_products` call. Finally, it converts the return type from a list of tuples to a dictionary to match `SupermarketOne`.

Now, thanks to duck typing we can use `SupermarketTwoAdapter` and `SupermarketOne` interchangeably so that the calling code doesn't need to know which type of supermarket we are providing. For example:

```
supermarkets = [SupermarketOne(),
                SupermarketTwoAdapter(SupermarketTwo())]
for supermarket in supermarkets:
    print(f'{type(supermarket).__name__} products = {supermarket.get_products()}')
```

If we wish to retain typing here, we can also ensure that both `SupermarketOne` and `SupermarketTwoAdapter` share a common interface which defines the `get_products` function.

In summary, the Adapter pattern allows us to use existing code with incompatible interfaces in a more consistent way, without altering the existing base classes.