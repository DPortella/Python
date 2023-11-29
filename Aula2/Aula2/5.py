#Crie um código que receba 4 números, calcule o quadrado deles e some o\
#resultados dos quadrados, mostre cada um dos resultados

i = 0
lst = []
while i < 4:
    n = int(input("Indique um número: "))**2
    lst.append(n)
    i += 1
print(sum(lst))
