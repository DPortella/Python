#Crie um programa que vai receber as informações de uma lista, e irá salva-lás num arquivo “exercicio2.txt”.

def salvar_em_arquivo(info, file):
    with open(file, "w") as arquivo:
        for item in info:
            arquivo.write(str(item) + "\n")

def receber_lista():
    lst = []
    while True:
        item = input("Digite um item para adicionar à lista (ou 'sair' para encerrar): ")
        if item.lower() == "sair":
            break
        lst.append(item)
    return lst

info = receber_lista()
salvar_em_arquivo(info, "exercicio2.txt")