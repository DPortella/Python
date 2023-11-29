#Crie uma função que vai receber um nome por parâmetro, e irá mostrar uma mensagem falando\
#que essa pessoa vai passar de ano.

def name(nome):
    print(f"O aluno {nome} vai passar de ano")

nome = input("Indique um nome: ")
name(nome)
