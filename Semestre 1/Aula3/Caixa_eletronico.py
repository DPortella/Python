#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do \
#saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis\
#serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.\
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.


valor = int(input('Indique um valor para sacar: '))

cem = int(valor / 100)
valor = valor - (cem * 100)

cinquenta = int(valor / 50)
valor = valor - (cinquenta * 50)

dez = int(valor / 10)
valor = valor - (dez * 10)

cinco = int(valor / 5)
valor = valor - (cinco * 5)

um = valor

print(f'Notas R$100,00 = {cem}')
print(f'Notas R$ 50,00 = {cinquenta}')
print(f'Notas R$ 10,00 = {dez}')
print(f'Notas R$  5,00 = {cinco}')
print(f'Notas R$  1,00 = {um}')
