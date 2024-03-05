# Crie uma classe para Computador e nele deve ter atributos referente a sua configuração, SO, Memória Ram, Processador e\
# assim vai, além dos métodos para modifica-los.

class Computador:
    def __init__(self, marca, modelo, so, memoria_ram, processador):
        self.marca = marca
        self.modelo = modelo
        self.so = so
        self.memoria_ram = memoria_ram
        self.processador = processador

    def alterar_so(self, novo_so):
        self.so = novo_so

    def alterar_memoria_ram(self, nova_memoria_ram):
        self.memoria_ram = nova_memoria_ram

    def alterar_processador(self, novo_processador):
        self.processador = novo_processador

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, SO: {self.so}, Memória RAM: {self.memoria_ram}, Processador: {self.processador}")

# Exemplo de uso da classe Computador
computador1 = Computador("Dell", "Inspiron", "Windows 10", "8GB", "Intel Core i5")
computador1.alterar_so("Linux")
computador1.alterar_memoria_ram("16GB")
computador1.alterar_processador("Intel Core i7")
computador1.exibir_informacoes()
print(computador1.__dict__)
