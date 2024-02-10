#Crie uma função que terá 2 parâmetros, caso não seja passado nenhum valor nesses parâmetros, usar valores “default”,\
# os parâmetros a serem usados são: Nome e Idade

def informacoes_pessoa(nome="Sem Nome", idade=0):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

informacoes_pessoa()
informacoes_pessoa("João", 25)