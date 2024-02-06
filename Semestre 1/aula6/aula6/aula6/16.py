#Construa uma função que vai criar um dicionário que deverá ter todas as letras do alfabeto,\
#use loop de repetição para isso, exemplo: alfabeto={1:”a”,...}

alfabeto = {}

def alfa():
    chave = 1
    for valor in range(97, 123):
        alfabeto[chave] = chr(valor)
        chave += 1
    print(alfabeto)

alfa()
