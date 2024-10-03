#Crie um código que vai receber o nome do aluno, seu RM, e a nota de 3 Acs,\
#calcule a nota e mostre o nome do aluno, RM e a nota final.

nome = input("Indique o nome: ")
rm = input("Indique o RM:")
i = 0
lst = []
while i < 3:
    nota = float(input("Insira a nota: "))
    lst.append(nota)
    i += 1
print(f"O(a) aluno(a) {nome} do RM {rm} teve a média final de: {sum(lst) / 3}")
