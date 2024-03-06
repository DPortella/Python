# Modifique a classe Automóvel, para mostrar quantas pessoas a classe filho consegue carregar de acordo com a quantidade\
# de rodas, crie 3 subclasses(filhos).

class carro:
    def __init__(self, nome, marca, peso, altura, rodas):
        self.nome = nome
        self.marca = marca
        self.peso = peso
        self.altura = altura
        self.rodas = rodas

    def dizer_nome(self):
        print(f"O nome do carro é {self.nome}")

    def dizer_marca(self):
        print(f"A marca é {self.marca}")

    def dizer_peso(self):
        print(f"O carro pesa {self.peso} quilos")

    def dizer_rodas(self):
        print(f"O carro possui {self.rodas} rodas")

        if self.rodas <= 4:
            print(f"O carro consegue carregar 2 pessoas")

        elif self.rodas <= 6:
            print(f"O carro consegue carregar até 8 pessoas")

        elif self.rodas > 10:
            print(f"Muitas rodas")

class caminhonete(carro):
    def __init__(self, nome, marca, peso, altura, rodas):
            super().__init__(nome, marca, peso, altura, rodas)



car = carro("Golf", "Volkswagen", 500, 1.50, 4)
car.dizer_nome()
car.dizer_marca()
car.dizer_peso()
car.dizer_rodas()
car1 = caminhonete("Ranger", "Ford", 500, 1.50, 6)
car1.dizer_peso()
car1.dizer_rodas()
