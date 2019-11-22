import sys

data = sys.stdin.readlines()
l,r = [int(x) for x in data[0].strip("\n").split(" ")]
m = 2*max(l,r)
if m==0:
    print("Not a moose")
else:
    s = "Even" if l==r else "Odd"
    print(s,m)
