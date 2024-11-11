#Faça um programa que tenha 2 funções uma delas irá receber uma frase e depois modificar ela\
#para deixar uma letra maiúscula seguida de uma letra minúscula, exemplo: AbAcAxI é UmA fRuTa.\
#A outra função irá fazer o mesmo mas começando com uma letra minúscula seguida de uma letra maiúscula.

def maiuscula(string):
    x = " "
    for i in range(len(string)):
        if not i % 2:
            x = x + string[i].upper()
        else:
            x = x + string[i].lower()
    print(str(x))

def minuscula(string):
    x = " "
    for i in range(len(string)):
        if not i % 2:
            x = x + string[i].lower()
        else:
            x = x + string[i].upper()
    print(str(x))

maiuscula("daniel")
minuscula("daniel")
