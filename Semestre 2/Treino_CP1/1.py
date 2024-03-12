#Leia o arquivo de texto “vendas.txt” com os dados de vendas (produto, quantidade vendida, preço). Crie uma classe\
# para representar um item de venda e processe esses dados para calcular o total de vendas, para isso utilize o\
# arquivo.

class ItemVenda:
    def __init__(self, produto, quantidade, preco_unitario):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def calcular_total(self):
        return self.quantidade * self.preco_unitario

def ler_arquivo_vendas(nome_arquivo):
    itens_venda = []
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        #linhas = arquivo.readlines()[1:]  # Ignorar o cabeçalho
        for linha in arquivo:
            dados = linha.strip().split(',')
            print(dados)
            produto = dados[0]
            quantidade = int(dados[1])
            preco_unitario = float(dados[2])
            item = ItemVenda(produto, quantidade, preco_unitario)
            itens_venda.append(item)
    return itens_venda


def calcular_total_vendas(itens_venda):
    total_vendas = 0
    for item in itens_venda:
        total_vendas += item.calcular_total()
    return total_vendas

nome_arquivo = 'vendas.txt'
itens_venda = ler_arquivo_vendas(nome_arquivo)
total_vendas = calcular_total_vendas(itens_venda)
print("Total de Vendas:", total_vendas)
