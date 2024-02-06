#Escreva um programa que vai criar um loop de repetição, para adicionar pares de chave-valor, até o usuário\
# não quiser continuar.

dict = {}

while True:
    key = input("Indique uma nova chave para o dicionário: ")
    if key == "N":
        print(dict)
        break
    value = input("Indique um novo valor para o dicionário: ")
    dict[key] = value