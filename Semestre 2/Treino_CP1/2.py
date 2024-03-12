# Leia o arquivo de texto “funcionarios.txt” com as informações de funcionários (nome, cargo, salário). Crie uma classe\
# para representar um funcionário e outra classe para representar um departamento. Use essas informações para criar\
# objetos correspondentes e realizar operações como calcular a folha de pagamento do departamento.

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nome} - {self.cargo} - Salário: R${self.salario:.2f}"


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def calcular_folha_pagamento(self):
        total_salarios = sum(funcionario.salario for funcionario in self.funcionarios)
        return total_salarios


def ler_arquivo_funcionarios(nome_arquivo):
    funcionarios = []
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        #linhas = arquivo.readlines()[1:]  # Ignorar o cabeçalho
        for linha in arquivo:
            dados = linha.strip().split(',')
            nome = dados[0]
            cargo = dados[1]
            salario = float(dados[2])
            funcionario = Funcionario(nome, cargo, salario)
            funcionarios.append(funcionario)
    return funcionarios



nome_arquivo = 'funcionarios.txt'
funcionarios = ler_arquivo_funcionarios(nome_arquivo)

departamento = Departamento("TI")  # Exemplo de nome de departamento

for funcionario in funcionarios:
    departamento.adicionar_funcionario(funcionario)

total_folha_pagamento = departamento.calcular_folha_pagamento()

print("Folha de Pagamento do Departamento", departamento.nome)
for funcionario in departamento.funcionarios:
    print(funcionario)
print("Total da Folha de Pagamento:", total_folha_pagamento)
