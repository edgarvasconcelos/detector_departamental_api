import tensorflow_datasets as tfds

def create_tokenizer(data_clean, save_path):
    """
    Creates and saves a tokenizer from the cleaned data.

    Args:
        data_clean (list of str): List of cleaned text data.
        save_path (str): Path to save the tokenizer.

    Returns:
        tfds.deprecated.text.SubwordTextEncoder: Tokenizer.
    """
    tokenizer = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(data_clean, target_vocab_size=2**16)
    tokenizer.save_to_file(save_path + 'tokenizer')
    return tokenizer
