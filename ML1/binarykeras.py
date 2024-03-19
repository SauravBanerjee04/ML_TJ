import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from tensorflow.keras.models import load_model
import copy


# model = Sequential([
#     Dense(5, activation = 'sigmoid', input_dim = 32),
#     Dense(32, activation = 'sigmoid'),
# ])

# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['binary_accuracy'])

model = load_model( 'saved_model' )

listof32zeroes = 32*[0]

inputset = []
#create array of numbers
for x in range (32):
    f = copy.deepcopy(listof32zeroes)
    f[x] = 1
    inputset.append(copy.deepcopy(f))
    


data = np.array(inputset)
labels = np.array(inputset)

model.fit(
    data, 
    labels, 
    epochs = 20000,
    verbose = 0)

scores = model.evaluate(data,labels)
print(model.metrics_names[1], scores[1] * 100)

model.save('saved_model')
