def check_access(func):
    def wrapper(employee1):
        # Comprobar si el empleado tiene rol 'admin'
        if employee1.get('role') == 'employee':
            return func(employee1)
        else:
            print('ACCESO DENEGADO. Solo los administradores pueden acceder.')
    return wrapper
        
@check_access
def delete_employee(info_employee):
    print(f"Elempleado {info_employee['name']} ha sido eliminado.")

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}


#delete_employee(admin)
delete_employee(employee)
