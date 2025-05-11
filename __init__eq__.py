class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otra_persona):
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

p1 = Persona("Ana", 30)
p2 = Persona("Ana", 30)

print(p1 == p2)  # True: both have the same name and age   
