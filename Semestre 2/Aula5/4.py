#Crie métodos especiais para a classe Computador

class Computador:
    def __init__(self, marca, modelo, so, memoria_ram, processador):
        self.marca = marca
        self.modelo = modelo
        self.so = so
        self.memoria_ram = memoria_ram
        self.processador = processador

    def __del__(self):
        print("O pc deu tela azul")

    def __str__(self):
        return f"Sou um pc gamer com {self.processador} e {self.memoria_ram}"

    def __len__(self):
        return len(self.__dict__)

    def alterar_so(self, novo_so):
        self.so = novo_so

    def alterar_memoria_ram(self, nova_memoria_ram):
        self.memoria_ram = nova_memoria_ram

    def alterar_processador(self, novo_processador):
        self.processador = novo_processador

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, SO: {self.so}, Memória RAM: {self.memoria_ram}, Processador: {self.processador}")

computador1 = Computador("Dell", "Inspiron", "Windows 10", "8GB", "Intel Core i5")
print(computador1)
print(len(computador1))
del computador1