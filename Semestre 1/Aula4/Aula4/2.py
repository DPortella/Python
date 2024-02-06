#Faça um programa que vai ter 8 números, podendo ser int, float ou até ambos, o programa\
#deve perguntar para o usuário se ele quer ver o menor valor da lista, o maior ou a soma de\
#todos os valores.

lst = []
i = 0

while i < 8:
    num = float(input("Indique um número para ser adicionado a lista: "))
    lst.append(num)
    i += 1

x = input("Digite max para ver o maior número da lista, min para o menor número da lista ou soma para somar os valores: ")

if x == "max":
    print(max(lst))
elif x == "min":
    print(min(lst))
else:
    print(sum(lst))
