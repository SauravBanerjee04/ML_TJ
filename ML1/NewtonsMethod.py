
x0 = -.7
f = lambda x: x**3 + x -1.0
fp = lambda x: 3*x*x + 1.0

x = x0
for b in range(10):
    print(str(b) + "  " + str(x) + ", " + str(f(x)))
    x -= ( f(x)/fp(x))
  