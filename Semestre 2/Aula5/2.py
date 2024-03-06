# Crie métodos especiais para a classe Automóvel

class carro:
    def __init__(self):
        self.nome = "Golf"
        self.marca = "Volkswagen"
        self.peso = 500
        self.altura = 1.50

    def __del__(self):
        print("Objeto deletado!")

    def __str__(self):
        return(f"Essa é a classe com o nome: {self.nome}")

    def __len__(self):
        return len(self.__dict__)

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
print(f"A quantidade de atributos é de {len(car)}")
print(car)
del car
