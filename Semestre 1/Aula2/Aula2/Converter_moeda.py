#Crie um código que faça uma simulação de conversão de Real(R$) para dólar Americano($)\
#e mostre o total que ele receberia.

vlr_r = float(input("Insira o valor em reais: "))
cot = float(input("Insira a cotação do dólar do dia: "))
print(f"R${vlr_r:.2f} reais com a cotação do dia fica no total de {vlr_r / cot:.2f}")
