#Crie uma calculadora que utilize funções para fazer as 4 operações básicas, os números usados devem vir de um input do\
# teclado.

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Por favor, digite números válidos.")
    exit()

soma = adicao(numero1, numero2)
subtracao_resultado = subtracao(numero1, numero2)
multiplicacao_resultado = multiplicacao(numero1, numero2)
divisao_resultado = divisao(numero1, numero2)

print(f"\nResultados:\nSoma: {soma}\nSubtração: {subtracao_resultado}\nMultiplicação: {multiplicacao_resultado}")
print(f"Divisão: {divisao_resultado}")
