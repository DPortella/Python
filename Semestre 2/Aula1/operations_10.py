# Crie um módulo chamado math_operations que contém as funções addition, subtraction, multiplication e division.\
# Cada função deve receber dois argumentos e retornar o resultado da operação correspondente.

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."