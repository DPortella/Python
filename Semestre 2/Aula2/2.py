#Crie um programa que vai receber as informações de uma lista, e irá salva-lás num arquivo “exercicio2.txt”.

lst = ["Daniel", "Erik", "Gabriel", "Higor", "Nicolas"]

file = open("lista.txt", "w")
file.write("\n".join(lst))
file = open("lista.txt")
print(file.read())
file.close()
