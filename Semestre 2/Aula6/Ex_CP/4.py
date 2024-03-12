# Crie uma classe FiguraGeometrica com um método calcular_area. Em seguida, crie subclasses para representar diferentes\
# formas geométricas, como Retangulo, Triangulo e Circulo, cada uma com métodos para calcular a área específica da\
# figura. Utilize o polimorfismo para chamar o método calcular_area de cada forma geométrica sem saber previamente qual\
# é a forma.

import math

class FiguraGeometrica:
    def calcular_area(self):
        pass  # Este método será sobrescrito nas subclasses


class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)


# Criando uma lista de figuras geométricas
figuras = [Retangulo(5, 4), Triangulo(3, 6), Circulo(2)]

# Calculando a área de cada figura geométrica
for figura in figuras:
    print("Área:", figura.calcular_area())