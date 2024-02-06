#Crie um programa que vai criar a tabuada do número escolhido

num = int(input("Indique qual número deseja ver multiplicado: "))
mul = int(input("Indique quantas vezes: "))

for i in range(1, mul+1):
    result = num * i
    print(f"{num} X {i} = {result}")