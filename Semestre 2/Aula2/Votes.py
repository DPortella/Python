# Faça um programa que apure o resultado de uma votação para determinar o personagem do desenho “The Simpsons” favorito.\
# Suponha que existam 5 candidatos cujos códigos de identificação são: 1-Bart, 2-Homer, 3-Krusty, 4-Mr Burns,\
# 5-Ned Flanders. Considere um arquivo texto (denominado “votos.txt”) que contém, em cada linha, um determinado voto\
# (um voto é representado pelo código de identificação do candidato). O programa deverá apresentar, como resultado, o\
# nome do candidato e a quantidade de votos do candidato mais votado, o código de identificação e a quantidade de votos\
# do candidato menos votado e a quantidade de votos nulos (um voto nulo é um voto cujo código de identificação é um\
# inteiro diferente de 1,2,3,4,5)

candidatos = {
    1: "Bart",
    2: "Homer",
    3: "Krusty",
    4: "Mr Burns",
    5: "Ned Flanders"
}



contagem_votos = {candidato: 0 for candidato in candidatos.keys()}
votos_nulos = 0


with open("votos.txt", "r") as arquivo:
    for linha in arquivo:
        voto = int(linha.strip())
        print(voto)
        print(contagem_votos)
        if voto in contagem_votos.keys():
            contagem_votos[voto] += 1
        else:
            votos_nulos += 1


candidato_mais_votado = max(contagem_votos, key=contagem_votos.get)
votos_mais_votado = contagem_votos[candidato_mais_votado]


candidato_menos_votado = min(contagem_votos, key=contagem_votos.get)
votos_menos_votado = contagem_votos[candidato_menos_votado]


print("Resultado da votação:")
print(f"Candidato mais votado: {candidatos[candidato_mais_votado]} com {votos_mais_votado} votos.")
print(f"Código: {candidato_mais_votado}, Votos: {votos_mais_votado}")
print(f"Candidato menos votado: {candidatos[candidato_menos_votado]} com {votos_menos_votado} votos.")
print(f"Código: {candidato_menos_votado}, Votos: {votos_menos_votado}")
print(f"Votos nulos: {votos_nulos}")
