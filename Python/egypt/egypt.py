import sys
import math
data = sys.stdin.readlines()[:-1]

for place in data:
    b,o,s = sorted([int(x) for x in place.split()])
    print("right" if b**2+o**2==s**2 else "wrong")