class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs

    def show_employee(self):
        print('Employee:', self.name)
        print('Skills', self.skills)
        print('Details', self.details)

employee = Employee('Adrian', 'Python', 'Java', 'C++', age=30, city = 'Santiago', pueblo = 'Colina')
employee.show_employee()