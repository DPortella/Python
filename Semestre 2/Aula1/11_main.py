# Crie um módulo chamado text_analysis que contém as funções word_count, character_count e sentence_count.\
# Cada função deve receber uma string como argumento e retornar o número correspondente de palavras, caracteres ou\
# sentenças na string.


from txt_11 import word_count, character_count, sentence_count

# Exemplo de uso:
texto = "Esta é uma frase de exemplo. Conta palavras, caracteres e sentenças."

palavras = word_count(texto)
caracteres = character_count(texto)
sentencas = sentence_count(texto)

print(f"Número de palavras: {palavras}")
print(f"Número de caracteres: {caracteres}")
print(f"Número de sentenças: {sentencas}")