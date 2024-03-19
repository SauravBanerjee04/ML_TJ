import json
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from tensorflow.keras.models import load_model
import copy
from keras import backend as K
import math

model = load_model( 'saved_model' )


weights = model.layers[0].get_weights()
for x in range(32):
    l = []
    for y in range(5):
        sum = 1/ (1 + math.exp(-(weights[0][x][y] + weights[1][y])))
        l.append(round(sum))
    print(l)
