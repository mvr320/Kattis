import sys
l,r,m = [int(i) for i in sys.stdin.readline().split(' ')]
nl = set(range(l,m+1,l))
nr = set(range(r,m+1,r))
print("yes" if len(nl.intersection(nr))>0 else "no")
