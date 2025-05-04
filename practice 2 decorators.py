# Decorador que comprueba si un empleado tiene un rol específico

def check_acces(required_role):
    def decorator(func):
        def wrapper(employee):
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f"ACCESO DENEGADO. Solo {required_role} puede realizar esta acción")
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f"El empleado {employee['name']} ha sido eliminado.")
        return func(employee)
    return wrapper

@check_acces('admin')
@log_action
def delete_employee(employee):
    print(f"El empleado {employee['name']} ha sido eliminado.")

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

delete_employee(employee)