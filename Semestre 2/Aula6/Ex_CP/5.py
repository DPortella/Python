# Suponha que você tenha um arquivo de texto chamado dados.txt que contém informações sobre produtos em uma loja, cada\
# linha do arquivo segue o formato:
# nome_do_produto, preço, quantidade
# Camiseta, 29.99, 50
# Calça Jeans, 59.99, 30
# Tênis, 79.99, 20
# Seu desafio é criar um programa em Python que leia o arquivo dados.txt, analise suas informações e crie objetos\
# correspondentes à classe Produto para cada linha do arquivo. Em seguida, armazene esses objetos em uma lista.
# Além disso, implemente métodos para calcular:
# O valor total em estoque de todos os produtos.
# O produto com o maior preço.
# O produto com a maior quantidade em estoque.
# Por fim, imprima os resultados obtidos.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = int(quantidade)

    def valor_total(self):
        print(f"Produto: {self.nome} - {self.preco * self.quantidade}")
def ler_arquivo_dados(nome_arquivo):
    produtos = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(',')
            produto = Produto(nome, preco, quantidade)
            produtos.append(produto)
    return produtos

def calcular_valor_total(produtos):
    return sum(produto.preco * produto.quantidade for produto in produtos)

def produto_maior_preco(produtos):
    return max(produtos, key=lambda produto: produto.preco)

def produto_maior_quantidade(produtos):
    return max(produtos, key=lambda produto: produto.quantidade)


nome_arquivo = 'dados.txt'
produtos = ler_arquivo_dados(nome_arquivo)

produtos[0].valor_total()
valor_total_estoque = calcular_valor_total(produtos)
print("Valor total em estoque de todos os produtos:", valor_total_estoque)

produto_maior_preco = produto_maior_preco(produtos)
print("Produto com o maior preço:", produto_maior_preco.nome)

produto_maior_quantidade = produto_maior_quantidade(produtos)
print("Produto com a maior quantidade em estoque:", produto_maior_quantidade.nome)
