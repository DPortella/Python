#Crie um programa que vai ler o arquivo ”Exercicio4.txt” caso não encontre deve cria-ló, com as informações das matérias\
# que você tem no curso

lst = ["Python, Architecture, Governança, Redes, Linux, Hardware"]

try:
    with open ("Exercicio4.txt", "r") as arquivo:
        print(arquivo.read())

except FileNotFoundError:
    file = open("Exercicio4.txt", "w")
    file.write("\n".join(lst))
    file = open("Exercicio4.txt")
    print(file.read())
    file.close()