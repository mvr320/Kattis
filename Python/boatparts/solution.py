import sys
import itertools
import math
import string

s = int(sys.stdin.readline())
if s%2==1:
    print("Either")
elif s%4==0:
    print("Even")
else:
    print("Odd")