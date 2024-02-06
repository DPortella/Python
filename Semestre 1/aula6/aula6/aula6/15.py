#Crie uma função para mostrar todos os valores que foram criados numa lista, sendo que eles\
#não tem um tamanho específico.

lst = []

def itens(*args):
    lst.append(args)
    print(lst)

itens(15, "Daniel", "35", "Erik")
