import numpy as np
import math
import random
import copy
import matplotlib.pyplot as plt
NUM_EPOCHS = 1000
LEARNING_RATE = .1
sigmoid = lambda x: 1/(1+math.exp(-x))
sig = np.vectorize(sigmoid)
sigp = np.vectorize(lambda x: sigmoid(x) * (1-sigmoid(x)))


def feed_forward(x,w_list,b_list):
    aL = copy.deepcopy(x)
    for l in range(len(w_list)-1):
        aL = sig(aL@w_list[l+1] + b_list[l+1])
    return aL

def rand(x,y):
    arr = np.zeros((x,y))
    for a in range(x):
        for b in range(y):
            arr[a,b] = random.random() * 2 -1
    return arr

def error(ts,w_list,b_list):
    error = 0
    for (a,b) in ts:
        error += .5 * ((b[0][0] - feed_forward(a,w_list,b_list)[0][0])**2)
    return error

enum = [] #epoch number
errorvals = [] #error

def train(ts,ll): #trainingset, layerlist
    w_list = [0]
    b_list = [0]

    for a in range(1,len(ll)):
        w_list.append(rand(ll[a-1],ll[a]))
        b_list.append(rand(1,ll[a]))
    for t in range(NUM_EPOCHS):
        for (x,y) in ts:
            al = [0] * len(ll)
            dl = al #dotlist
            delta_list = copy.copy(b_list)

            al[0] = x
            for l in range (1,len(ll)):
                dl[l] = (al[l-1]@w_list[l]) + b_list[l]
                al[l] = sig(dl[l])

            N = len(layerlist) - 1
            delta_list[N] = sigp(dl[N]) * (y-al[N])
            for l in range(N-1,0,-1):
                delta_list[l] = sigp(dl[l]) * (delta_list[l+1] @ w_list[l+1].transpose())
            for l in range(1,len(ll)):
                b_list[l] = b_list[l] + LEARNING_RATE * delta_list[l]
                w_list[l] = w_list[l] + LEARNING_RATE * (al[l-1].transpose() @ delta_list[l])
        enum.append(t+1)
        errorvals.append(error(ts,w_list,b_list))
    return(w_list,b_list)


trainingset = [([[1,1]],[[1]]),([[1,0]],[[1]]),([[1,1]],[[1]]),([[0,0]],[[0]])]
tset = [(np.array(a),np.array(b)) for (a,b) in trainingset]
layerlist = [2,1]
(a,b) = train(tset,layerlist)
print(a)
print(b)
print(feed_forward([0,0],a,b))
plt.plot(enum, errorvals, "o")
plt.show()
