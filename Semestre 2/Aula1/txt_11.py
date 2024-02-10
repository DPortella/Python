def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    text = text.lower()
    return len(text)

def sentence_count(text):
    sentences = text.split('.')  # Assumindo que as sentenças terminam com ponto final
    return len(sentences)

def sentence_count_sem_vazio(text):
    sentences = [sentence.strip() for sentence in text.split('.') if sentence.strip()]
    return len(sentences)