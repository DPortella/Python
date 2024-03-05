class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def __del__(self):
            print("Deletado com sucesso")

    def __str__(self):
        return f"Meu nome é {self.nome} e a idade {self.idade}"

    def __len__(self):
        return len(self.__dict__)

    def get_peso(self):
        return self.peso


class professor(Pessoa):
    def __init__(self, nome, idade, peso, turma):
            super().__init__(nome, idade, peso)
            self.turma = turma

    def print_turma(self):
        print(f"A turma é {self.turma}")

prof1 = professor("Kaio", 38, 85, "1td")
print(prof1)
print(prof1.get_peso())
print(prof1.print_turma())

ser = Pessoa("", "", 90)
print(ser.get_peso())