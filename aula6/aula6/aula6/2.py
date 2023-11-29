#Crie uma função que terá 2 parâmetros, caso não seja passado nenhum valor nesses parâmetros,\
#usar valores “default”, os parâmetros a serem usados são: Nome e Idade.

def func(nome="Daniel", idade=29):
    print(f"{nome} tem {idade} anos de idade")

func("Erik", 22)
func()


