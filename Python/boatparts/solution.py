import sys
import itertools
import math
import string

s,t = [int(x) for x in sys.stdin.readline().split()]
dset = set()
data = sys.stdin.readlines()
for lid in range(len(data)):
    dset.add(data[lid].strip('\n'))
    if len(dset)==s:
        print(lid+1)
        exit()
print("paradox avoided")