#Faça um Programa que leia três números e mostre-os em ordem decrescente.

lst = []
i = 0

while i < 3:
    n = int(input("Indique um número: "))
    lst.append(n)
    i += 1
lst.sort(reverse=True)
print(lst)
