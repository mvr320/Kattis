import sys
import itertools
import math
import string

data = sys.stdin.readlines()[:-1]
for line in data:
    bd,v = [int(x) for x in line.split()]
    c=bd/(2.0)*math.pi*(bd/2.0)**2
    vq = c-v
    d = bd*(vq/c)
    #d = (vq*4.0*math.pi)**(1.0/3.0)
    print(d)