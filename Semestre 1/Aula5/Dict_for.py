#Crie um programa que vai criar um dicionário que deverá ter todas as letras do alfabeto, use\
#loop de repetição para isso, exemplo: alfabeto={1:”a”,...}

alfabeto = {}
i = 1

for char in range(97, 123):
    alfabeto[i] = chr(char)
    i += 1
print(alfabeto)

