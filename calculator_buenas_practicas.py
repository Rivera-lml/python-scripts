class Calculator:
    def add_numbers(self, first_number, second_number):
        result = first_number + second_number
        return result
    
calc = Calculator()

print(calc.add_numbers(1,2))


class Calculator:
    def add_numbers(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number