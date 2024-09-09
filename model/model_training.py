import tensorflow as tf

def train_model(model, train_inputs, train_labels, test_inputs, test_labels, checkpoint_path):
    """
    Trains the model and saves checkpoints.

    Args:
        model (tf.keras.Model): Keras model to train.
        train_inputs (np.ndarray): Training input data.
        train_labels (np.ndarray): Training labels.
        test_inputs (np.ndarray): Testing input data.
        test_labels (np.ndarray): Testing labels.
        checkpoint_path (str): Path to save model checkpoints.

    Returns:
        tf.keras.callbacks.History: Training history.
    """
    ckpt = tf.train.Checkpoint(model=model)
    ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)
    
    if ckpt_manager.latest_checkpoint:
        ckpt.restore(ckpt_manager.latest_checkpoint)
        print('Latest checkpoint restored')

    history = model.fit(
        train_inputs, train_labels,
        epochs=25,
        batch_size=64,
        validation_data=(test_inputs, test_labels)
    )
    
    return history
