# Crie uma classe Produto com os atributos nome, preco e quantidade. Em seguida, crie duas subclasses, ProdutoFisico e\
# ProdutoDigital. ProdutoFisico deve ter um atributo adicional peso, enquanto ProdutoDigital deve ter um atributo\
# adicional tamanho_em_mb. Crie um método calcular_frete na classe ProdutoFisico que calcula o frete com base no peso\
# e na distância, e um método calcular_tamanho_em_mb na classe ProdutoDigital que retorna o tamanho em MB do produto.

class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

class Fisico(Produto):
    def __init__(self, nome, preco, qtd, peso):
        super().__init__(nome, preco, qtd)
        self.peso = peso

    def frete(self):
        dis = float(input("Indique a distância em KM: "))
        print(f"O valor do frete será {self.peso * dis:.2f}")

class Digital(Produto):
    def __init__(self, nome, preco, qtd, tamanho_mb):
        super().__init__(nome, preco, qtd)
        self.tamanho_mb = tamanho_mb


    def calcular_tamanho(self):
        print(f"O tamanho é de {self.tamanho_mb * self.qtd} MB")

fis1 = Fisico("", "", "", 15)
fis1.frete()

dig1 = Digital("", "", 2, 500)
dig1.calcular_tamanho()
