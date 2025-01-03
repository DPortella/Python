class Pessoa:
    def __init__(self):
        self.nome = "Erik"
        self.idade = 19
        self. peso = 60.0

    def dizer_nome(self):
        print(f"Olá meu nome é {self.nome}")

    def dizer_idade(self):
        print(f"Tenho {self.idade} anos")

    def dizer_peso(self):
        print(f"Tenho {self.peso} quilos")

ser = Pessoa()
ser.dizer_nome()
ser.dizer_idade()
ser.dizer_peso()
