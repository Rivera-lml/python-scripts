from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:

    product_count = defaultdict(int)

    for product in orders:
        product_count[product] += 1
    return product_count



orders = ['laptop', 'smartphone', '']

count = count_products(orders)

print(count)

