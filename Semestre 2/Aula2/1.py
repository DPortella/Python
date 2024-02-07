#Crie um arquivo com o nome “grupo.txt”, nesse arquivo salve os nomes dos integrantes do seu grupo.

file = open("grupo.txt", "w")
file.write("Daniel, Erik, Higor, Gabriel, Nicolas")
file = open("grupo.txt")
print(file.read())
file.close()
