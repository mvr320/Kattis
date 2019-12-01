import sys
import itertools
import math
import string

data = sys.stdin.readlines()[:-1]
for line in data:
    bd,v = [int(x) for x in line.split()]
    print("{}".format(( (((-6)*v)/math.pi) + (bd**3))**(1./3.)))