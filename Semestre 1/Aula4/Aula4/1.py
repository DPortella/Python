#Escreva um programa que deve ter uma lista de 10 itens, que façam sentido entre si, ou seja,\
#uma lista de filmes, series, musicas, artistas, ou outro tema, o programa deve perguntar para\
#o usuário se ele quer adicionar mais um item, remover um item, ver a lista em ordem alfabética\
#ou reversa, como também se ele quer ver algum item especifico da lista, ou uma sub lista.

lst = ["Debian", "Windows", "MacOS", "Kali", "Ubuntu", "PfSense", "Android", "GrapheneOS", "Fedora", "Arch"]
n = 0
while n == 0:
    os = input("Digite r para remover um item da lista, a para adicionar ou l apenas para listar a lista: ")

    if os == "r":
        rem = input("Informe qual sistema será removido: ")
        lst.remove(rem)
        forma = input("Digite c para ver a lista em ordem crescente ou d para decrescente: ")
        if forma == "d":
            lst1 = lst
            lst1.reverse()
            print(lst1)
        else:
            lst1 = lst
            lst1.sort()
            print(lst1)

    elif os == "a":
        add = input("Informe qual sistema será adicionado: ")
        lst.append(add)
        forma = input("Digite c para ver a lista em ordem crescente ou d para decrescente: ")
        if forma == "d":
            lst1 = lst
            lst1.reverse()
            print(lst1)
        else:
            lst1 = lst
            lst1.sort()
            print(lst1)
    else:
        print(lst)
