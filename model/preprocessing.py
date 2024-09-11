import spacy
import string

# Carregar o modelo spacy uma vez, desativando componentes desnecessários
nlp = spacy.load('pt_core_news_md', disable=['ner', 'parser', 'lemmatizer'])
stop_words = spacy.lang.pt.STOP_WORDS

def clean_text(text):
    """
    Clean the input text by removing stop words and punctuation, and converting to lowercase.

    Args:
        text (str): The text to clean.

    Returns:
        str: The cleaned text.
    """
    # Converter o texto para minúsculas
    text = text.lower()

    # Processar o texto com o spaCy
    document = nlp(text)

    # Filtrar palavras que não são stop words ou pontuações
    words = [token.text for token in document if token.text not in stop_words and token.text not in string.punctuation]

    # Retornar o texto limpo
    return ' '.join(words)
