from collections import Counter

def count_sales(products: list[str]):

    return Counter(products)


sales = ['laptop', 'smartphone', 'smartphone', 'laptop', 'tablet']

contar = count_sales(sales)

print(contar)

