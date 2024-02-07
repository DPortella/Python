#Crie uma calculadora que utilize funções para fazer as 4 operações básicas, os números usados devem vir de um input do\
# teclado.

num1 = float(input("Dê o primeiro número da operação: "))
num2 = float(input("Dê o segundo número: "))

tipo = int(input("Indique o tipo de operação: \n 1 para somar \n 2 para subtrair \n 3 para mulltiplicar \n"
             "4 para dividir:"))

if tipo == 1: print(num1 + num2)
elif tipo == 2: print(num1 - num2)
elif tipo == 3: print(num1 * num2)
else: print(num1 / num2)
