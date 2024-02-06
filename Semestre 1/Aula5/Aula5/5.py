#Faça um programa que receba uma frase do usuário, para depois mostrar cada uma das letras de\
#forma individual.

frase = input("Digite uma frase: ")
frase = frase.replace(" ", "")

for i in frase:
    print(i)