import tensorflow as tf
import tensorflow_datasets as tfds

class ModelManager:
    def __init__(self, model_path='model/modelo_dcnn_91_30.h5', tokenizer_path='model/tokenizer'):
        self.model_path = model_path
        self.tokenizer_path = tokenizer_path
        self.model = None
        self.tokenizer = None

    def load_model(self):
        if self.model is None:
            print("Loading model and tokenizer...")
            self.model = tf.keras.models.load_model(self.model_path)
            self.model.trainable = False
            self.tokenizer = tfds.deprecated.text.SubwordTextEncoder.load_from_file(self.tokenizer_path)

    def unload_model(self):
        self.model = None
        self.tokenizer = None
        print("Model and tokenizer unloaded.")

    def predict(self, inputs):
        self.load_model()
        encoded_inputs = [self.tokenizer.encode(input) for input in inputs]
        predictions = self.model.predict(encoded_inputs)
        return predictions
