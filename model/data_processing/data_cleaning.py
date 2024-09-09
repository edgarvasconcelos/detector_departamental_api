import numpy as np
import pandas as pd
import spacy
import string
from unidecode import unidecode

nlp = spacy.load('pt_core_news_lg')
stop_words = spacy.lang.pt.STOP_WORDS

def clean_resumo(resumo):
    """
    Cleans the provided text by lowercasing, removing accents,
    stop words, and punctuation.

    Args:
        resumo (str): Text to be cleaned.

    Returns:
        str: Cleaned text.
    """
    resumo = resumo.lower()
    resumo = unidecode(resumo)
    document = nlp(resumo)

    words = [token.text for token in document if token.text not in stop_words and token.text not in string.punctuation]
    return ' '.join(words)