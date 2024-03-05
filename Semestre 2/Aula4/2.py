class carro:
    def __init__(self):
        self.nome = "Golg"
        self.marca = "Volkswagen"
        self.peso = 500
        self.altura: 1.50

    def dizer_nome(self):
        print(f"O nome do carro é {self.nome}")

    def dizer_marca(self):
        print(f"A marca é {self.marca}")

    def dizer_peso(self):
        print(f"O carro pesa {self.peso} quilos")


car = carro()
car.dizer_nome()
car.dizer_marca()
car.dizer_peso()