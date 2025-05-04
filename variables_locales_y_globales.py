x = 100 

def local_function():
    x = 10 # variable local
    print(f'El valor de la variable local es {x}')

def show_global():
    print(f'El valor de la variable global es {x}')


print(local_function())
print(show_global())


