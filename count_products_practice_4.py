from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:

    count = defaultdict(int)

    for value in orders:

        count[value] += 1

    return count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']

results = count_products(orders)

print(results)