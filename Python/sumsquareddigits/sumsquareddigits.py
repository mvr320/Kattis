import sys
import itertools
import math
import string

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

for line in sys.stdin.readlines()[1:]:
    k,b,n = [int(x) for x in line.split()]
    print(k, sum([x**2 for x in numberToBase(n,b)]))