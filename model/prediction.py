import numpy as np
import tensorflow as tf
from .preprocessing import clean_text

def predict(interpreter, tokenizer, input_text, class_names, max_len):
    """
    Faz a predição usando o interpretador TensorFlow Lite e o texto de entrada.

    Args:
        interpreter: O interpretador TensorFlow Lite.
        tokenizer: O tokenizador para o texto de entrada.
        input_text: O texto a ser classificado.
        class_names: Lista de nomes de classes.
        max_len: Comprimento máximo da sequência.

    Returns:
        List: Lista com os departamentos e probabilidades.
    """
    text_cleaned = [clean_text(input_text)]  # Assume clean_text is defined in preprocessing.py
    encoded_input = [tokenizer.encode(sentence) for sentence in text_cleaned]
    input_sequence = tf.keras.preprocessing.sequence.pad_sequences(encoded_input, maxlen=max_len, padding='post', truncating='post')
    
    # Obter os detalhes dos tensores de entrada e saída do interpretador
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Definir o tensor de entrada
    interpreter.set_tensor(input_details[0]['index'], np.array(input_sequence, dtype=np.float32))

    # Executar a inferência
    interpreter.invoke()

    # Obter o tensor de saída
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Ordenar e retornar os resultados
    top_indices = output_data[0].argsort()[-4:][::-1]
    predictions = [(class_names[i], output_data[0][i]) for i in top_indices]

    return predictions
