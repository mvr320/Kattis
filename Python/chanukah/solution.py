import sys
import itertools
import math
import string

for line in sys.stdin.readlines()[1:]:
    i,s = [int(x) for x in line.split()]
    print("{} {}".format(i, int(s+(s+1)*(s)/2)))