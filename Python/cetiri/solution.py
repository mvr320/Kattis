import sys
l,m,r = sorted([int(i) for i in sys.stdin.readline().split(' ')])
if m-l==r-m:
    print(int(r+(r-m)))
elif m-l>r-m:
    print(int(l+(m-l)/2))
else:
    print(int(m+(r-m)/2))
