#Usando as duas funções dos (Ex 5 e Ex 12), criar um jogo de adivinhação, onde o jogador terá\
#5 chances de acertar o número sorteado pelo computador, a cada tentativa o jogo deve mostrar\
#se o chute foi maior ou menor que o número certo.

def verifica_maior_num(val1, val2):
    if val1 < val2:
        print(f"Escolha um valor mais baixo")

    elif val2 < val1:
        print(f"Escolha um valor mais alto")

    else:
        print(f"Os dois são iguais")

import random as rd

def gerar_rd_num():
    return rd.randint(0, 20)

num_cpu = gerar_rd_num()

for i in range(0, 6):
    num_player = int(input("Qual o numero da vez: "))
    verifica_maior_num(num_cpu, num_player)
    if num_cpu == num_player:
        result = f"Parabéns!!! vc ganhou em {i} jogadas"
        break
    else:
        result = "Que pena n foi dessa vez"


print(result)
