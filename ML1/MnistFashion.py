import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from tensorflow.keras.models import load_model
import copy

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28,28]))
model.add(Dense(300, activation = "relu"))
model.add(Dense(100, activation = "relu"))
model.add(Dense(10, activation = "softmax"))

model.compile(optimzer = "adam",loss = "sparse_categorical_crossentropy",metrics = ["sparse_categorical_accuracy"])
