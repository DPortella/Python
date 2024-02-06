#Crie um código que receba o código da peça, valor da peça e quantidade de peças,\
#depois calcule o valor total da peça (Quantidade * Valor da peça). Mostre o resultado junto\
#com o código da peça.

pn = input("Insira o código da peça: ")
vlr = float(input("Insira o valor da peça: "))
qtd = int(input("Insira a quantidade de peças: "))
print(f"{qtd} da peça de código {pn}, tem um valor total de {vlr*qtd}")
