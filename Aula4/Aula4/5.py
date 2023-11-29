#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...\
#Faça um programa capaz de gerar a série até o n−ésimo termo.

seq = int(input("Quantas sequências de Fibonacci qur ver? "))
i = 0
a = 0
b = 1

while i < seq:
    c = a + b
    a = b
    b = c
    i += 1
    print(a)
