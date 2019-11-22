import sys
import itertools
import math
import string

s,l,r = [int(x) for x in sys.stdin.readline().split()]
if s==l+r:
    print("{}={}+{}".format(s,l,r))
elif s==l-r:
    print("{}={}-{}".format(s,l,r))
elif s==l*r:
    print("{}={}*{}".format(s,l,r))
elif s==l/r:
    print("{}={}/{}".format(s,l,r))
elif s+l==r:
    print("{}+{}={}".format(s,l,r))
elif s-l==r:
    print("{}-{}={}".format(s,l,r))
elif s*l==r:
    print("{}*{}={}".format(s,l,r))
elif s/l==r:
    print("{}/{}={}".format(s,l,r))
