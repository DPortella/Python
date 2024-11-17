#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses\
#três argumentos através de uma função. Seu script também deve fornecer a média dos três números,\
#através de uma segunda função que chama a primeira.

def soma_e_media(num1, num2, num3):
    soma = num1+num2+num3
    media = (num1+num2+num3) / 3

    return soma, media

print(soma_e_media(10, 20, 30))
