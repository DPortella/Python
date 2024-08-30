#Faça um programa que receba uma frase e depois modifique ela para deixar uma letra maiúscula seguida de uma letra\
# minúscula, exemplo: AbAcAxI é UmA fRuTa.

frase = input("Digite a frase: ")

x = " "
for i in range(len(frase)):
    if not i % 2:
        x += frase[i].upper()
    else:
        x += frase[i].lower()

print(str(x))
