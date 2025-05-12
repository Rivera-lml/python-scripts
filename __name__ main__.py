# Function that sums two numbers
def add(a, b):
    return a + b

# Function that subtracts two numbers
def subtract(a, b):
    return a - b

# Function that multiplies two numbers
def multiply(a, b):
    return a * b

# Function that divides two numbers
def divide(a, b):
    if b == 0:
        raise ValueError("Not possible divide by zero")
    return a / b

if __name__ == "__main__":
    print('Operaciones')
    res_1 = add(3, 4)
    print(f'Suma: {res_1}')
    print(divide(10, 7))

    