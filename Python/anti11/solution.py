import sys
import itertools
import math
import string

data = [int(x) for x in sys.stdin.readlines()[1:]]
for excase in data:
    count = 0
    for exstring in ["{0:b}".format(x) for x in range(2**excase)]:
        if '11' not in exstring:
            count +=1
    print('{}'.format(count%(10**9+7)))