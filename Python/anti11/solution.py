import sys
import itertools
import math
import string

storage = {}
def fib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    global storage
    n1 = None
    n2 = None
    if n-1 not in storage.keys():
        storage[n-1] = fib(n-1)
    if n-2 not in storage.keys():
        storage[n-2] = fib(n-2)
    return storage[n-1]+storage[n-2]

data = [int(x) for x in sys.stdin.readlines()[1:]]
for excase in data:
    print(fib(excase+1)%( (10**9)+7))