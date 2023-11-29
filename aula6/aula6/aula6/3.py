#Crie uma função que vai receber 3 parâmetros em qualquer ordem, sendo eles: Nome, E-mail e Telefone.​

def func1(nome, email, telefone):
    print(f"O e-mail de {nome} é {email}, e seu telefone é {telefone}")

name = input("Indique seu nome: ")
e_mail = input("Indique seu e-mail:")
phone = input("Indique seu telefone: ")

func1(email=e_mail, telefone=phone, nome=name)
