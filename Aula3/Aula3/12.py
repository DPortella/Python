#Ler três valores para os lados de um triângulo, considerando lados como: A, B e C.\
#Verificar se os lados fornecidos formam realmente um triângulo, e se for esta condição\
#verdadeira, deverá ser indicado qual tipo de triângulo foi formado: isósceles, escaleno\
#ou equilátero.

lst = []
i = 0

while i < 3:
    x = float(input("Indique um lado do triângulo: "))
    lst.append(x)
    i+=1

if (lst[0] + lst[1] < lst[2]) or (lst[0] + lst[2] < lst[1]) or (lst[1] + lst[2] < lst[0]):
    print("Isso não é um triângulo!")
    quit()
if lst[0] == lst[1] and lst[0] == lst[2]:
    print("Isso é um triângulo equilátero!")

elif (lst[0] != lst[1]) and (lst[0] != lst[2]) and (lst[1] != lst[2]):
    print("Isso é um triângulo escaleno!")

else:
    print("Isso é um triângulo Isósceles!")
