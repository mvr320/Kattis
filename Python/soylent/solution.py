import sys
import itertools
import math
import string

for val in [float(x) for x in sys.stdin.readlines()[1:]]:
    print(math.ceil(val/400))