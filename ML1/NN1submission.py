import sys; args = sys.argv[1:]
# args = ['weights2nn1.txt','T1', '.1', '.3']
myLines = open(args[0], "r").read().splitlines()
fname = args.pop(0)
import math
tfs = args.pop(0)
inputs = []
while len(args) > 0 :
    inputs.append(float(args.pop(0)))
linear = lambda x:x
def ramp(x):
    if(x >=0):
        return x
    else:
        return 0
logistic = lambda x: 1/(1+math.exp(-x)) 
t4 = lambda x: 2*logistic(x) - 1


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

activation = None
if tfs == "T1":
    activation = linear
elif tfs== "T2":
    activation = ramp
elif tfs == "T3":
    activation = logistic
else:
    activation = t4

def vectorize(matrix,act):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[x][y] = act(matrix[x][y])
    return matrix
    
def feed_forward(A,x,w_list):
    aL = [x]
    for l in range(1,len(w_list)-1):
        aL = vectorize(mult(aL,w_list[l]),A)#+ b_list[l])
    for m in range(len(aL[0])):
        aL[0][m] = aL[0][m] * w_list[len(w_list)-1][m]
    return aL


#converts inputs into array
inputlist = [inputs]


#reads weightfile
listlen = len(inputlist[0])
weightlist = [1]

for line in myLines:
    thisrow = line.strip().split()
    thisrow = [float(i) for i in thisrow]
    nextweight = creatematrix(listlen,int(len(thisrow)/listlen))
    for x in range (int(len(thisrow)/listlen)):
        for y in range(listlen):
            nextweight[y][x] = thisrow.pop(0)
    weightlist.append(nextweight)
    listlen = len(nextweight[0])
weightlist.pop()
weightlist.append([float(i) for i in myLines[len(myLines)-1].strip().split()])
# print(weightlist)
    
    
m = feed_forward(activation,inputs,weightlist)
s = ""
for x in m[0]: #goes through and prints final result
    s = s + str(x) + " "
print(s)
#Saurav Banerjee, 4, 2022




