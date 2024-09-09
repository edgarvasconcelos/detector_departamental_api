import random
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def resumir(texto):
    """
    Summarizes the provided text by extracting important sentences.

    Args:
        texto (str): Text to be summarized.

    Returns:
        str: Summarized text.
    """
    numero_de_sentencas = ajustar_numero_de_sentencas(texto)
    parser = PlaintextParser.from_string(texto, Tokenizer('portuguese'))
    sumarizador = TextRankSummarizer()
    resumo = sumarizador(parser.document, numero_de_sentencas)

    return " ".join(str(sentenca) for sentenca in resumo)

def ajustar_numero_de_sentencas(texto):
    """
    Determines the number of sentences for summarization.

    Args:
        texto (str): Text to analyze.

    Returns:
        int: Number of sentences.
    """
    parser = PlaintextParser.from_string(texto, Tokenizer('portuguese'))
    total_sentencas = len(list(parser.document.sentences))
    return random.randint(1, total_sentencas)
