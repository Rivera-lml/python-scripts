def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='Carlos', age='30', city='Bogotá')
print_info(name='Carlos', age='30', city='Bogotá', country='Colombia')
print_info(name='Rodri', apellido='Rivera', city='Metapán', Direccion='Barrio El Calvario', trabajo='Tech')

