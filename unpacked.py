#def add(args1):
#    return sum(args1)

#values = (1, 2, 3, 4, 5, 7)
#print(add(values))


def add(a, b, c):
    return a + b + c

values = (1, 2, 3)
print(add(*values))


def show_info(name, age):
    print(f"Name: {name}, Age: {age}")

data = {"name": "Ana", "age": 28}
show_info(**data)


