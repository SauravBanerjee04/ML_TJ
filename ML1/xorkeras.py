import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np



model = Sequential([
    Dense(2, activation = 'sigmoid', input_dim = 2),
    Dense(1, activation = 'sigmoid'),
])

# print(model.summary())
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['binary_accuracy'])

data = np.array([[1,1],[1,0],[0,1],[0,0]])
labels = np.array([[0],[1],[1],[0]])
model.fit(
    data, 
    labels, 
    epochs = 20000,
    verbose = 0)

scores = model.evaluate(data,labels)
print(model.metrics_names[1], scores[1] * 100)

for layer in model . layers :
    print(layer.get_weights())