class Vehicle:
    def __new__(cls, wheels: int):
        if wheels == 2:
            return Motorbike()
        elif wheels == 4:
            return Car()
        else:
            return super().__new__(cls)
        
    def __init__(self, wheels: int):
        self.wheels = wheels
        print(f'Initializing vehicle with {wheels} wheels')

class Motorbike:
    def __init__(self):
        print('Initializing motorbike')

class Car:
    def __init__(self):
        print('Initializing car')

#mb = Vehicle(2)

bus = Vehicle(10)

