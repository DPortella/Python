#Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque\
#o valor das variáveis e exiba na tela.

num1 = int(input("Indique o primeiro número: "))
num2 = int(input("Indique o segundo número: "))

num3 = num2
num2 = num1
num1 = num3

print(num1, num2)
