#Crie uma calculadora que utilize funções para fazer as 4 operações básicas, os números\
#usados devem vir de um input do teclado.

def add(num1, num2):
    '''Adicionando números'''
    print(num1+num2)

def sub(num1, num2):
    '''Subtraindo números'''
    print(num1-num2)

def mul(num1, num2):
    '''Multiplicando números'''
    print(num1*num2)

def div(num1, num2):
    '''Dividindo números'''
    print(num1/num2)

x = float(input("Indique o primeiro elemento: "))
y = float(input("Indique o segundo elemento: "))

calc = int(input("Indique a operação que deseja fazer: \n"
           "1 soma\n"
           "2 subtração\n"
           "3 multiplicação\n"
           "4 divisão\n"))

if calc == 1:
    print(add.__doc__)
    add(x, y)
elif calc == 2:
    print(sub.__doc__)
    sub(x, y)
elif calc == 3:
    print(mul.__doc__)
    mul(x, y)
else:
    print(div.__doc__)
    div(x, y)
