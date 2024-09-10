import tensorflow as tf
import tensorflow_datasets as tfds

def load_model(model_path='model/modelo_dcnn_91_30.h5', tokenizer_path='model/tokenizer'):
    """
    Load the Keras model and tokenizer.

    Args:
        model_path (str): Path to the Keras model file.
        tokenizer_path (str): Path to the tokenizer file.

    Returns:
        interpreter: O interpretador do modelo TensorFlow Lite.
        tokenizer: Loaded tokenizer.
    """
    # Carregar o modelo .tflite
    interpreter = tf.lite.Interpreter(model_path="model/model.tflite")
    interpreter.allocate_tensors()
    tokenizer = tfds.deprecated.text.SubwordTextEncoder.load_from_file(tokenizer_path)
    return interpreter, tokenizer
