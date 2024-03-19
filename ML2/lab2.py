tvs = []
sales = []
import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

with open( 'Datasaurus_data.csv' , newline='' ) as csvfile :
    #
    myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
    #
    # header
    #
    # for row in myreader :
    #     #
    #     # print( row )
    #     #
    #     break
    #     #
    #
    # data
    #
    x = 0
    for row in myreader :
        #
        if(x == 0):
            n = 1
            x += 1
        else:
            tvs.append(float(row[0]))
            #
            sales.append(float(row[1]))
            #
            # print( tv , sales )
            #
            x+= 1
    #
#
tvmean = sum(tvs)/len(tvs) #x 
salesmean = sum(sales)/len(sales) #y
def mean(z):
    return sum(z)/len(z)

b1 = sum([(tvs[z]-tvmean)*(sales[z]-salesmean) for z in range(len(tvs))])/sum([(tvs[z1] - tvmean)**2 for z1 in range(len(tvs))])
b0 = salesmean - b1 * tvmean
print(b1)
print(b0)

def rss(b1,b0,x_list,y_list):
    return sum([(y_list[x] - b0 - b1*x_list[x])**2 for x in range(len(x_list))])
print(rss(b1,b0, tvs, sales))

def b1error(x_list, y_list):
    return(float(scipy.stats.linregress(x_list, y_list).stderr))


def b0error(x_list, y_list):
    return(float(scipy.stats.linregress(x_list, y_list).intercept_stderr))

#print(b1error(tvs,sales))
#print(b0error(tvs,sales))
#print((scipy.stats.linregress(tvs, sales)[5]))
#print((scipy.stats.linregress(tvs, sales)[4]))
# print((scipy.stats.linregress(tvs, sales)))
# l =(scipy.stats.linregress(tvs, sales))
# for b in l:
#     print(b)

# b1_error = (scipy.stats.linregress(tvs, sales).stderr)
# b0_error = (scipy.stats.linregress(tvs, sales).intercept_stderr)



print("approximation")
print("b0")
print(b0)
print("b1")
print(b1)
print("")

print('errors')
print("b0 error ")
print(b0error(tvs, sales))
print("b1 error")
print(b1error(tvs, sales))
print("")


# print(b0 - 2* b0error(tvs,sales))
# print(b0 + 2* b0error(tvs,sales))


# print(b1 - 2* b1error(tvs,sales))
# print(b1 + 2* b1error(tvs,sales))


print("b0")
print(b0)
print("b0 95 percent confidence interval: ")
print("("+ str(b0 - b0error(tvs,sales)) + ", " + str(b0 + b0error(tvs,sales)) +  ")")


print("b1")
print(b1)
print("b1 95 percent confidence interval: ")
print("("+ str(b1 - b1error(tvs,sales)) + ", " + str(b1 + b1error(tvs,sales)) +  ")")

