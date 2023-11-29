#Escreva um programa que vai criar um loop de repetição, para adicionar pares de chave-valor,\
#até o usuário não quiser continuar.

dict = {}
alunos = int(input("Quantos alunos serão? "))

for aluno in range(0,alunos):
    rm = int(input("Informe o RM: "))
    nome = input("Informe o nome do aluno: ")
    dict[rm] = nome

print(dict)
