import sys
import itertools
import math
import string

freefood = set()
data = sys.stdin.readlines()[1:]
for line in data:
    b,e = line.split()
    for elem in list(range(int(b),int(e)+1)):
        freefood.add(elem)
print(len(freefood))