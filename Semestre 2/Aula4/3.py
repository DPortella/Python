# Crie uma classe para Clientes de uma lan house, cada cliente deve ter um nome, tempo de uso, créditos e outras coisas\
# que o programador achar importante para o negocio, para cada um dos atributos deve ser criado um método para aumentar,\
# diminuir ou alterar as informações

class ClienteLanHouse:
    def __init__(self, nome, tempo_de_uso, creditos):
        self.nome = nome
        self.tempo_de_uso = tempo_de_uso
        self.creditos = creditos

    def aumentar_tempo_de_uso(self, tempo):
        # Verifica se há créditos suficientes para aumentar o tempo de uso
        if tempo * 0.5 <= self.creditos:
            self.tempo_de_uso += tempo
            self.creditos -= tempo * 0.5
            print(f"Tempo de uso aumentado para {self.tempo_de_uso} minutos.")
        else:
            print("Créditos insuficientes para aumentar o tempo de uso.")

    def diminuir_tempo_de_uso(self, tempo):
        if self.tempo_de_uso >= tempo:
            self.tempo_de_uso -= tempo
            print(f"Tempo de uso diminuído para {self.tempo_de_uso} minutos.")
        else:
            print("Tempo de uso não pode ser menor que zero.")

    def aumentar_creditos(self, creditos):
        self.creditos += creditos

    def diminuir_creditos(self, creditos):
        if self.creditos < 0:
            print("A quantidade de créditos não pode ser menor que zero")
        else:
            self.creditos -= creditos
            print(f"A quantidade de créditos foi diminuído para R$: {self.creditos}")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Tempo de Uso: {self.tempo_de_uso} minutos, Créditos: R${self.creditos:.2f}")

# Exemplo de uso da classe ClienteLanHouse
cliente1 = ClienteLanHouse("João", 60, 10)
cliente1.exibir_informacoes()

cliente1.aumentar_tempo_de_uso(30)
cliente1.diminuir_tempo_de_uso(20)
cliente1.aumentar_creditos(15)
cliente1.exibir_informacoes()
cliente1.aumentar_tempo_de_uso(30)
cliente1.diminuir_creditos(10)