from collections import Counter

def count_sales(products: list[str]) -> Counter:

    return Counter(products)

sales = ['laptop', 'smartphone', 'smartphone', 'laptop', 'tablet']

cuenta = count_sales(sales)

print(cuenta)

