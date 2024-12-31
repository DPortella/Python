#Crie um arquivo com o nome “grupo.txt”, nesse arquivo salve os nomes dos integrantes do seu grupo.

names = ["Daniel", "Erik", "Higor", "Gabriel", "Nicolas"]

with open("grupo.txt", "w") as file:
    for nome in names:
        file.write(nome + "\n")

print("Arquivo criado!")
