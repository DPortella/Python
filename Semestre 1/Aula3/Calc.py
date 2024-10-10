#Crie um programa para receber 2 números quaisquer que deverá ser escolhido pelo usuário,\
#o tipo de operação que será realizada e mostre o resultado da operação.

num1 = float(input("Dê o primeiro número da operação: "))
num2 = float(input("Dê o segundo número: "))

tipo = int(input("Indique o tipo de operação: \n 1 para somar \n 2 para subtrair \n 3 para mulltiplicar \n"
             "4 para dividir:"))

if tipo == 1: print(num1 + num2)
elif tipo == 2: print(num1 - num2)
elif tipo == 3: print(num1 * num2)
else: print(num1 / num2)
