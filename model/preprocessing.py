import spacy
import string

def clean_text(text):
    """
    Clean the input text by removing stop words and punctuation, and converting to lowercase.

    Args:
        text (str): The text to clean.

    Returns:
        str: The cleaned text.
    """
    text = text.lower()
    nlp = spacy.load('pt_core_news_lg')
    stop_words = spacy.lang.pt.STOP_WORDS
    document = nlp(text)

    words = [token.text for token in document if token.text not in stop_words and token.text not in string.punctuation]
    return ' '.join(words)
