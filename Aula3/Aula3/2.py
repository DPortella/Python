#Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar.\
#Dica: utilize o operador módulo (resto da divisão)

number = int(input("Digite um número: "))

if number % 2 == 0: print(f"O número {number} é par!")
else: print(f"O número {number} é impar!")
