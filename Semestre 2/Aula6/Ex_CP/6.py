# Crie um programa que vai ler o arquivo “planetas.txt” e crie uma classe Planetas que vai receber essas informações.

class Planeta:
    def __init__(self, nome, massa, raio, distancia_media_ao_sol):
        self.nome = nome
        self.massa = massa
        self.raio = float(raio)
        self.distancia_media_ao_sol = distancia_media_ao_sol

    def __str__(self):
        return f"Nome: {self.nome}, Massa: {self.massa}, Raio: {self.raio}, Distância média ao Sol: {self.distancia_media_ao_sol}"

def ler_arquivo_planetas(nome_arquivo):
    planetas = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            planeta = Planeta(*dados)
            planetas.append(planeta)
    return planetas

nome_arquivo = 'planetas.txt'
planetas = ler_arquivo_planetas(nome_arquivo)

for planeta in planetas:
    print(planeta)
