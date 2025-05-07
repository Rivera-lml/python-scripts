class ModeloRegresion:
    def __init__(self, coeficiente):
        self.coef = coeficiente

    def __call__(self, x):
        return self.coef * x

# Crear el modelo
modelo = ModeloRegresion(2)

# Usar el modelo como si fuera una función
prediccion = modelo(5)
print(f"Predicción: {prediccion}")
