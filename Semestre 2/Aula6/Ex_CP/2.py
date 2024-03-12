# Crie uma classe ContaBancaria com os atributos titular e saldo, e métodos para depositar, sacar e verificar o saldo.\
# Em seguida, crie duas subclasses, ContaCorrente e ContaPoupanca. ContaCorrente deve ter um atributo adicional\
# limite_cheque_especial, e o método de saque deve verificar se é possível sacar considerando o saldo mais o limite\
# do cheque especial. ContaPoupanca deve ter um método adicional calcular_rendimento que retorna o rendimento mensal\
# da conta.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def verificar_saldo(self):
        return self.saldo

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, limite_cheque_especial=0):
        super().__init__(titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if valor <= (self.saldo + self.limite_cheque_especial):
            self.saldo -= valor
            return True
        else:
            print("Limite do cheque especial ultrapassado.")
            return False
class ContaPoupanca(ContaBancaria):
    def calcular_rendimento(self, taxa_rendimento):
        rendimento_mensal = self.saldo * (taxa_rendimento / 100)
        return rendimento_mensal

# Exemplo de uso das classes
conta_corrente = ContaCorrente("João", 1000, 500)
conta_corrente.depositar(200)
print("Saldo da Conta Corrente:", conta_corrente.verificar_saldo())
conta_corrente.sacar(1500)
print("Saldo da Conta Corrente após saque:", conta_corrente.verificar_saldo())

conta_poupanca = ContaPoupanca("Maria", 5000)
rendimento = conta_poupanca.calcular_rendimento(0.5)  # 0.5% de rendimento mensal
print("Rendimento mensal da Conta Poupança:", rendimento)
