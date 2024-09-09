from googletrans import Translator

def translate_text(text, src_lang='pt', dest_lang='en'):
    """
    Translates text from source language to destination language.

    Args:
        text (str): Text to be translated.
        src_lang (str): Source language.
        dest_lang (str): Destination language.

    Returns:
        str: Translated text.
    """
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def translate_round_trip(text):
    """
    Translates text from Portuguese to English and back to Portuguese.

    Args:
        text (str): Text to be translated.

    Returns:
        str: Text translated back to Portuguese.
    """
    translated_to_english = translate_text(text, src_lang='pt', dest_lang='en')
    return translate_text(translated_to_english, src_lang='en', dest_lang='pt')
