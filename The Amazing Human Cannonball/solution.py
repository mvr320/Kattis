import sys
import math

data = sys.stdin.readlines()
for c in range(1,len(data)):
    v0,th,x1,h1,h2 = [float(x) for x in data[c].split(" ")]
    t = x1/(math.cos(math.radians(th))*v0)
    y = v0*t*math.sin(math.radians(th))-0.5*9.81*t**2
    #print(h1,y,h2, end="")
    if (h1+1.0)<y and (h2-1.0)>y:
        print("Safe")
    else:
        print("Not Safe")
    
