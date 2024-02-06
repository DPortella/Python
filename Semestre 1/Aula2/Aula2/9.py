#Crie um código para calcular a comissão de vendas de um vendedor de aparelhos eletrônicos,\
#levando-se em consideração que sua comissão é de 15% da venda. O resultado que deve ser\
#mostrado no final é o código do vendedor, quantos aparelhos ele vendeu, o valor total em\
#vendas e sua comissão.

cod = input("Indique o código do vendedor: ")
qtd = int(input("Indique quantas peças foram vendidas: "))
vlr = float(input("Indique o valor unitário da peça: "))
print(f"O vendedor de código {cod} vendeu {qtd} peças, totalizando {qtd * vlr:.2f} em vendas e em {(qtd*vlr) * 0.15:.2f} \
de comissão")
