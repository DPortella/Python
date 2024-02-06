#Crie uma função que vai verificar se o número A e menor que o número B e retornar a resposta.\
#Exemplo: “Número A é menor Número B”.

def valores(num1, num2):
    if num1 < num2:
        print("O número A é menor que o número B")
    elif num1 > num2:
        print("O número A é maior que o número B")
    else:
        print("Os números são iguais")


x = float(input("Indique o primeiro elemento: "))
y = float(input("Indique o segundo elemento: "))

valores(x, y)


