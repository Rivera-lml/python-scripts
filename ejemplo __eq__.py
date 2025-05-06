class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

    def __eq__(self, otro_libro):
        print(f"self = {self.titulo}, otro_libro = {otro_libro.titulo}")
        return self.titulo == otro_libro.titulo

l1 = Libro("1984")
l2 = Libro("1984")
l3 = Libro("Fahrenheit 451")

print(l1 == l2)  
print(l1 == l3)  


