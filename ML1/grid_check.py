import sys 
w= int(sys.argv[1])
h = int(sys.argv[2])
for x in range(h):
    s = ""
    for y in range(w):
        s = s + "0 "
    print(str(s))
    s = ""
