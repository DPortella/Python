# Crie uma classe Personagem com o método atacar. Em seguida, crie duas subclasses, Guerreiro e Mago, que sobrescrevem\
# o método atacar para imprimir uma mensagem específica para cada tipo de personagem. Crie uma lista de personagens e\
# faça-os atacar, demonstrando o polimorfismo.

class Personagem:
    def atacar(self):
        pass  # Implementação será sobrescrita nas subclasses


class Guerreiro(Personagem):
    def atacar(self):
        print("Guerreiro ataca com sua espada!")


class Mago(Personagem):
    def atacar(self):
        print("Mago lança uma bola de fogo!")


# Criando uma lista de personagens
personagens = [Guerreiro(), Mago(), Guerreiro(), Mago()]

# Fazendo com que cada personagem ataque
for personagem in personagens:
    personagem.atacar()