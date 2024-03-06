# Crie uma classe ContaBancaria com os atributos titular e saldo, e métodos para depositar, sacar e verificar o saldo.\
# Em seguida, crie duas subclasses, ContaCorrente e ContaPoupanca. ContaCorrente deve ter um atributo adicional\
# limite_cheque_especial, e o método de saque deve verificar se é possível sacar considerando o saldo mais o limite\
# do cheque especial. ContaPoupanca deve ter um método adicional calcular_rendimento que retorna o rendimento mensal\
# da conta.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):

    def sacar(self):

    def verificar(self):


class Corrente(ContaBancaria):
    def __init__(self, titular, saldo, limite_cheque):
        super().__init__(titular, saldo)
        self.limite_cheque = limite_cheque

class Poupanca(ContaBancaria):
    def __init__(self, titular, saldo, calcular_rendimento):
        super().__init__(titular, saldo)
        self.calcular_rendimento = calcular_rendimento
