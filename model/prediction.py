import numpy as np
import tensorflow as tf
from .preprocessing import clean_text


def predict(model, tokenizer, input_text, class_names, max_len):
    """
    Make predictions using the pre-trained model.

    Args:
        model: The loaded Keras model.
        tokenizer: The loaded tokenizer.
        input_text (str): The input text to predict.
        class_names (list): List of class names.
        max_len (int): The maximum length for padding/truncation.

    Returns:
        list: List of tuples with class names and their corresponding probabilities.
    """
    text_cleaned = [clean_text(input_text)]  # Assume clean_text is defined in preprocessing.py
    encoded_input = [tokenizer.encode(sentence) for sentence in text_cleaned]
    padded_input = tf.keras.preprocessing.sequence.pad_sequences(encoded_input, maxlen=max_len, padding='post', truncating='post')
    
    predictions = model.predict(padded_input)
    predicted_classes = np.argpartition(predictions[0], -4)[-4:]
    predicted_class_names = [(class_names[i], predictions[0][i]) for i in predicted_classes]
    return sorted(predicted_class_names, key=lambda x: x[1], reverse=True)
