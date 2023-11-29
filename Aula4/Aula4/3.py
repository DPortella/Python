#Crie um programa que vai receber os nomes das músicas favoritas do usuário, e deve salva-las\
#numa lista, usando um loop de repetição, e no final mostre elas por sub listas, ou em\
#ordem alfabética.

lst = []
n = 0

while n == 0:
    lst.append(input("Indique a música para a lista: "))
    n = int(input("Digite 0 para continuar ou 1 para parar: "))

for musica in lst:
    print(musica)
