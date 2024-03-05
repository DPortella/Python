class ClienteLanHouse:
    def __init__(self, nome, tempo_de_uso, creditos):
        self.nome = nome
        self.tempo_de_uso = tempo_de_uso
        self.creditos = creditos

    def __del__(self):
        print("O clinte saiu do pc")

    def __str__(self):
        return f"Meu nome é {self.nome} e tenho R${self.creditos}"

    def __len__(self):
        return len(self.__dict__)

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

p1 = ClienteLanHouse("Jonathan", 60, 50)
print(p1)
print(len(p1))