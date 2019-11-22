import sys

data = sys.stdin.readlines()
for l in range(len(data)-1):
    cl = data[l].strip("\n").split(" ")
    x1 = float(cl[0])
    y1 = float(cl[1])
    x2 = float(cl[2])
    y2 = float(cl[3])
    p  = float(cl[4])
    print( ( (abs(x1-x2)**p)+(abs(y1-y2)**p) )**(1/p) )
