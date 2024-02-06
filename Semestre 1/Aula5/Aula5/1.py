#Crie um programa que vai receber os pares de chave-valor, com o RM sendo a chave e o valor\
#sendo o nome do aluno, faça isso usando um loop de repetição e preencha um dicionário com as\
#informações do pessoal do seu grupo do challenge.

dict = {}
for i in range(1, 6):
    rm = int(input("Informe o RM: "))
    nome = input("Informe o nome do aluno: ")
    dict[rm] = nome

print(dict)
