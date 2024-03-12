# Crie um programa que vai ler o arquivo “lista de personagens Stan lee.txt” e crie uma classe Personagem que vai\
# receber essas informações.

class Personagem:
    def __init__(self, nome, nome_real):
        self.nome = nome
        self.nome_real = nome_real

    def __str__(self):
        return f"Nome: {self.nome} (Nome real: {self.nome_real})"

def ler_arquivo_personagens(nome_arquivo):
    personagens = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            personagem = Personagem(*dados)
            personagens.append(personagem)
    return personagens

nome_arquivo = 'lista de personagens Stan lee.txt'
personagens = ler_arquivo_personagens(nome_arquivo)

for personagem in personagens:
    print(personagem)
    print()

