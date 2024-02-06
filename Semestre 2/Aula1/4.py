#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34, 55,... Faça um programa capaz de gerar\
# a série até o enésimo termo.

num = int(input("Indique quantos termos deseja fazer: "))
a = 1
b = 0
i = 0

while i < num:
    c = a + b
    b = a
    a = c
    i += 1
    print(c)