import multiprocessing

# function that calculates the square of a number
def calculate_square(n):
    return n*n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    # create a pool
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_square, numbers)

    print(f'Results: {results}')

