#Crie uma função para adicionar valores a uma lista que está no escopo global.

lst = []

def app():
    i = 0
    x = int(input("Indique o número de elementos: "))
    while i < x:
        y = input("Indique o que será adicionado à lista: ")
        lst.append(y)
        i += 1
    print(lst)

app()
