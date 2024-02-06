# Ler o valor de salário de um funcionário e aplicar o reajuste de acordo com as seguintes condições: Salário menor\
# que 500, reajuste de 15%; Salário maior ou igual a 500, porém menor ou igual a 1000, reajuste de 10%; Salário maior\
# que 1000, reajuste de 5%

salario = float(input("Indique o slário do funcionário: "))

if salario < 500:
    salario = salario * 1.15

elif salario < 1000:
    salario = salario * 1.10

else:
    salario = salario * 1.05

print(f"O total do salário reajustado é de: R${salario: .2f}")