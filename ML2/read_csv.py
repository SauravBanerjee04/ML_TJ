#
import csv
#
with open( 'Advertising.csv' , newline='' ) as csvfile :
    #
    myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
    #
    # header
    #
    for row in myreader :
        #
        # print( row )
        #
        break
        #
    #
    # data
    #
    for row in myreader :
        #
        tv = row[1]
        #
        sales = row[4]
        #
        print( tv , sales )
        #
    #
#
print( 'done' )
#

xlist = []
ylist = []