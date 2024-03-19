import math
import random
import copy
LEARNING_RATE = .2
NUM_EPOCHS = 1000


def listmaker(x):
    b = []
    for m in range(x):
        b.append(0)
    return b

def creatematrix(y,x):
    m = []
    for b in range(y):
        m.append(listmaker(x))
    return m 

def mult(X,Y):
    if not (len(X[0]) == len(Y)):
        return None
    result = creatematrix(len(X),len(Y[0]))
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

def vectorize(mat,act):
    matrix = copy.deepcopy(mat)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[x][y] = act(matrix[x][y])
    return matrix
    
def feed_forward(A,x,w_list,b_list):
    aL = [x]
    for l in range(1,len(w_list)):
        aL = add([vectorize(mult(aL,w_list[l]),A),b_list[l]])
    return aL


#these are adapted from old code that i've lost sorta
#@ is the same thing as mulitplying
def sigmoid(x):
    return 1/(1+math.exp(-x)) 
def sigmoidprime(x):
    return sigmoid(x) * (1.0 - sigmoid(x))
def sigmoidize(x):
    return vectorize(x,sigmoid)
def sigmoidizeprime(x):
    return vectorize(x,sigmoid)

def randomize(x):
    for a in range (len(x)):
        for b in range (len(x[0])):
            x[a][b] = random.random()
    return x
    
def transpose(m):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return rez

def smult(x,y): #scalarmultiplicaton
    m = y
    for a in range(len(y)):
        for b in range(len(y[0])):
            m[a][b] = x * m[a][b]
    return m

def imult(x,y):
    rez = creatematrix(len(x),len(x[0]))
    for c in range(len(rez)):
        for d in range(len(rez)):
            rez[c][d] = x[c][d] * y[c][d]
    return rez

def sub(x,y):
    rez = [[x[i][j] - y[i][j] for i in range(len(x))] for j in range(len(x[0]))]
    return rez

def add(l):
    result = l.pop(0)
    a = len(result)
    b = len(result[0])
    while len(l) > 0:
        c = l.pop(0)
        for a in range(len(result)):
            for b in range(len(result[0])):
                result[a][b] = result[a][b] + c[a][b]
    return result

def train(trainingset,layerlist):
    #add random weights and biases
    w_list = [0]
    for x in range(len(layerlist)-1):
        w_list.append(randomize(creatematrix(layerlist[x],layerlist[x+1])))
    b_list = [0]
    for y in range(1,len(layerlist)):
        b_list.append(randomize(creatematrix(1,layerlist[y])))
    # randomize(b_list)
    
    # print(w_list)
    # print(b_list)
    
    
    a_list = [[listmaker(m)] for m in layerlist]
    dot_list = [[listmaker(m)] for m in layerlist]
    dot_list[0] = None
    delta_list = [[listmaker(m)] for m in layerlist]
    
    
    
    for t in range(NUM_EPOCHS):
        for (x,y) in trainingset:
            a_list[0] = x
            for l in range(1,len(layerlist)):
                dot_list[l] = add([mult(a_list[l-1],w_list[l]),b_list[l]])
                a_list[l] = sigmoidize(dot_list[l])
            N = len(layerlist) - 1
            delta_list[N] = imult(sigmoidizeprime(dot_list[N]),(sub(y,a_list[N])))
            for l in range(int(N)-1,0,-1):
                delta_list[l] = imult(sigmoidizeprime(dot_list[l]),(mult(delta_list[l+1],transpose(w_list[l+1]))))
            for l in range(1,len(layerlist)):
                b_list[l] = add([b_list[l],smult(LEARNING_RATE,delta_list[l])])
                w_list[l] = add([w_list[l],smult(LEARNING_RATE,(mult(transpose(a_list[l-1]),delta_list[l])))])
            # print(b_list)
            # print(w_list)
            # print(totalerror(trainingset,w_list,b_list))
            # print(a_list[N])
        # print()
    return (w_list,b_list)

trainingset = [([[1,1]],[[1]]),([[1,0]],[[0]]),([[0,1]],[[0]]),([[0,0]],[[0]])]
layerlist = [2,2,1]
(a,b) = train(trainingset,layerlist)
print(feed_forward(sigmoid,[1,1],a,b))





