# Leia o arquivo de texto “produtos.txt” com as informações sobre os produtos em um supermercado\
# (nome, preço, departamento). Crie classes para representar os produtos e os diferentes departamentos do supermercado.\
# Implemente funcionalidades como adicionar novos produtos, atualizar preços e gerar relatórios de vendas\
# por departamento.

class Produto:
    def __init__(self, nome, preco, departamento):
        self.nome = nome
        self.preco = preco
        self.departamento = departamento

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total_vendas(self):
        total_vendas = 0
        for produto in self.produtos:
            total_vendas += produto.preco
        return total_vendas


def ler_arquivo_produtos(nome_arquivo):
    departamentos = {}
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()[1:]  # Ignorar o cabeçalho
        for linha in linhas:
            dados = linha.strip().split(',')
            nome = dados[0]
            preco = float(dados[1])
            departamento_nome = dados[2]
            #verifica se o departamento já existe no dicionario
            if departamento_nome not in departamentos:
                departamentos[departamento_nome] = Departamento(departamento_nome)
            produto = Produto(nome, preco, departamento_nome)
            departamentos[departamento_nome].adicionar_produto(produto)
    return departamentos


def main():
    nome_arquivo = 'produtos.txt'
    departamentos = ler_arquivo_produtos(nome_arquivo)

    for nome_departamento, departamento in departamentos.items():
        total_vendas = departamento.calcular_total_vendas()
        print(f"Folha de Vendas do Departamento {nome_departamento}:")
        for produto in departamento.produtos:
            print(produto)
        print("Total de Vendas:", total_vendas)
        print()


if __name__ == "__main__":
    main()
