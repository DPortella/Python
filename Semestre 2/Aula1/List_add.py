#Escreva um programa que vai criar um loop de repetição, para adicionar pares de chave-valor, até o usuário\
# não quiser continuar.

dict = {}

while True:
    key = input("Indique uma nova chave para o dicionário: ")
    value = input("Indique um novo valor para o dicionário: ")
    dict[key] = value
    continua = input("Deseja continuar? (S/N): ").upper()
    if continua != 'S':
        break

print(dict)
