#Crie um programa que irá receber o ID do vendedor, o valor da peça, a quantidade de peças\
#vendidas e calcule o valor total, caso o vendedor não tenha atingido um valor maior ou igual\
#a cota de vendas mínima, devera aparecer a mensagem com o id, valor total e quanto falta\
#para atingir a cota.

id = int(input("Indique o ID do vendedor: "))
vlr = float(input("Indique o valor unitário da peça: "))
qtd = int(input("Indique quantas peças foram vendidas: "))
total = qtd * vlr
if total < 50.0: print(f"Faltam {50 - total:.2f} para que o vendedor {id} atinja a meta")
else: print(f"O vendedor {id} bateu a meta!")
