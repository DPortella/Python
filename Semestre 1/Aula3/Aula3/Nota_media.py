#Crie um código que vai receber o nome do aluno, seu RM, e a nota de 3 CPs, calcule a\
#nota usando a média aritmética simples e mostre o nome do aluno, RM, a nota final e\
#apresentar se o aluno está reprovado ou aprovado considerando que a média 7 para aprovação.

cont = 0
nome = input("Indique o nome do aluno: ")
rm = input("Indique o rm: ")
lst = []

while cont < 3:
  nota = float(input("Indique uma nota: "))
  lst.append(nota)
  cont += 1

media = sum(lst) / 3

if media < 7:
 print(f"A média do aluno {nome} de RM {rm}, foi de {media:.2f}, portanto ele está reprovado")
else:
  print(f"A média do aluno {nome} de RM {rm}, foi de {media:.2f}, portanto ele está aprovado")
