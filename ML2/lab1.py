tvs = []
sales = []
import csv
import numpy as np
import matplotlib.pyplot as plt

with open( 'Advertising.csv' , newline='' ) as csvfile :
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
            tvs.append(float(row[1]))
            #
            sales.append(float(row[4]))
            #
            # print( tv , sales )
            #
            x+= 1
    #
#
tvmean = sum(tvs)/len(tvs) #x 
salesmean = sum(sales)/len(sales) #y

b1 = sum([(tvs[z]-tvmean)*(sales[z]-salesmean) for z in range(len(tvs))])/sum([(tvs[z1] - tvmean)**2 for z1 in range(len(tvs))])
b0 = salesmean - b1 * tvmean
print(b1)
print(b0)

def rss(b1,b0,x_list,y_list):
    return sum([(y_list[x] - b0 - b1*x_list[x])**2 for x in range(len(x_list))])
print(rss(b1,b0, tvs, sales))


#
import numpy as np
#
xp = np . arange( 5.0 , 9.0 , 4.0 / 100 )
yp = np . arange( .03 , .07 , .04 / 100 )
#
print(xp)
print(yp)
zp = np . zeros( ( yp . size , xp . size ) )
#
xp , yp = np . meshgrid( xp , yp )

print(xp)
print(yp)

#
# *** calculate zp here ***
#x value goes into b1 which is first value, y goes into second 
for y in range (len(zp)):
    for x in range (len(zp[0])):
        zp[y][x] = rss(yp[y][x], xp[y][x], tvs, sales)



#
import matplotlib.pyplot as plt
#
fig = plt . figure()
ax  = plt . axes( projection = '3d' )
ax  . plot_surface( xp , yp , zp )
ax  . scatter( 7.0325935491277 , 0.04753664, 2102.53 , color = '#ff0000' )
plt . show()
#
# can also use 'fig' and 'ax'
# to add contour labels in the
# previous example
#

import matplotlib.pyplot as plt
#
plt.contour(xp, yp, zp)
plt.scatter(7.032593548,0.04753664, color = '#ff0000', marker = '.')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#xp is 1-d yp is 10d zp is 2-d



