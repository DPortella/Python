#Faça um programa que leia um nome de usuário e a sua senha e não aceite a não ser que a senha\
#e o nome do usuário, sejam o esperado, mostrando uma mensagem de erro e voltando a pedir\
#as informações.

while True:
    usuario = input("Indique o usuário: ")
    senha = input("indique a senha: ")


    if usuario != "DPortella" and senha != "senha123":
        print("Não encontrado!")

    else:
        print("Você logou!")
        break
