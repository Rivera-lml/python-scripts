class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = new_salary

    @salary.deleter
    def salary(self):
        print(f"The salary of {self.name} has been deleted")
        del self._salary

# create an instance of Employee
employee = Employee("Ana", 5000)
print(employee.salary)

# modify the salary in a controlled manner
employee.salary = 6000
print(employee.salary)

# trying to stablish a negative salary
#employee.salary = -1000

# Delete the salary
del employee.salary
