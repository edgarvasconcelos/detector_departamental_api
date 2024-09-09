import tensorflow as tf

def create_model(vocab_size, emb_dim, max_len, nb_classes):
    """
    Creates a Convolutional Neural Network model.

    Args:
        vocab_size (int): Size of the vocabulary.
        emb_dim (int): Dimension of the embedding layer.
        max_len (int): Maximum length of input sequences.
        nb_classes (int): Number of output classes.

    Returns:
        tf.keras.Model: Compiled Keras model.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=emb_dim, input_length=max_len),
        tf.keras.layers.Conv1D(filters=100, kernel_size=3, activation='relu'),
        tf.keras.layers.GlobalMaxPooling1D(),
        tf.keras.layers.Dense(units=256, activation='relu'),
        tf.keras.layers.Dropout(rate=0.1),
        tf.keras.layers.Dense(units=nb_classes, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model
