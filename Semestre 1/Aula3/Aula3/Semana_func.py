#Faça um Programa que leia um número e exiba o dia correspondente da semana.\
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dict = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sábado"}
number = int(input("Indique um número entre 1 e 7: "))
print(dict[number])
