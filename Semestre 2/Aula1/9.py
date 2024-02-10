#Crie uma função que vai gerar um número aleatório entre 0 e 20, e deve retornar o valor para uma variável

import random

def gerar_numero_aleatorio():
    numero_aleatorio = random.randint(0, 20)
    return numero_aleatorio

numero_gerado = gerar_numero_aleatorio()
print(f"Número aleatório gerado: {numero_gerado}")