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


class SupermarketTwoAdapter:

    def __init__(self, supermarket_two):
        self.supermarket_two = supermarket_two

    def get_products(self):
        products = self.supermarket_two.get_fruit() + self.supermarket_two.get_meat()
        return dict(products)


supermarket_one = SupermarketOne()
print(f'Supermarket one products = {supermarket_one.get_products()}')

supermarket_two = SupermarketTwo()
print(f'Supermarket two fruit = {supermarket_two.get_fruit()}')
print(f'Supermarket two meat = {supermarket_two.get_meat()}')

supermarkets = [SupermarketOne(),
                SupermarketTwoAdapter(SupermarketTwo())]
for supermarket in supermarkets:
    print(f'{type(supermarket).__name__} products = {supermarket.get_products()}')
