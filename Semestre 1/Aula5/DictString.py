#Faça um programa que vai receber pares de chave e valor, onde a chave deve ser um número e o\
#valor deve ser uma palavra, após o usuário não tiver mais informações para inserir,\
#o programa deve formar uma frase aleatória usando os valores salvos no dicionário.

import random as rd

dict_val = {}
count = 0
while count == 0:

    key = input("Informe a chave: ")
    value = input("Informe o valor: ")
    dict_val[key] = value
    count = int(input("0 - continuar \n 1 - parar"))

values = list(dict_val.values())
print(values)
print(rd.sample(values, len(values)))
