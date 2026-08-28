"""Train a small TensorFlow network to learn XOR."""

import os

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")

import numpy as np
import tensorflow as tf


XOR_INPUTS = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
XOR_LABELS = np.array([[0.0], [1.0], [1.0], [0.0]])


def train_xor(epochs: int = 1_500) -> np.ndarray:
    """Train an XOR binary classifier and return predictions for its four inputs."""
    tf.keras.utils.set_random_seed(42)

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(2,)),
            tf.keras.layers.Dense(4, activation="tanh"),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.05), loss="binary_crossentropy")
    model.fit(XOR_INPUTS, XOR_LABELS, epochs=epochs, verbose=0)

    probabilities = model.predict(XOR_INPUTS, verbose=0).ravel()
    return (probabilities >= 0.5).astype(int)


if __name__ == "__main__":
    for inputs, prediction in zip(XOR_INPUTS.astype(int), train_xor()):
        print(f"{inputs.tolist()} -> {prediction}")
