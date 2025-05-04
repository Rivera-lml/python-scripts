numbers = [1, 2, 3, 4, 5]

print(f'Original:  {numbers}')

squares = [x**2 for x in numbers]
print(f'squares: {squares}')

sum_2 = [x + 2 for x in numbers]
print(f'sum: {sum_2}')

mult_2 = [x * 2 for x in numbers]
print(f'mult: {mult_2}')

rest_2 = [x - 2 for x in numbers]
print(f'rest: {rest_2}')

