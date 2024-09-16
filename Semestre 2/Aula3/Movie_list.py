#Crie um programa que vai receber nomes de filmes do usuário e deverá salva-lós num arquivo, caso o arquivo “filmes.txt”\
# não exista o mesmo deverá ser criado, faça uma validação para ver ser os nomes são validos

lst = []

try:
    while True:
        movies = input("Indique o nome de um filme (digite 'sair' para terminar): " ).lower()
        if movies == "sair":
            break
        else:
            lst.append(movies)

except:
    with open ("Filmes", "r") as arquivo:
        print(arquivo.read())

finally:
    file = open("Filmes.txt", "w")
    file.write("\n".join(lst))
    file = open("Filmes.txt")
    print(file.read())
    file.close()
