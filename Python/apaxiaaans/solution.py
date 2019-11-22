import sys

data = sys.stdin.readlines()
c=' '
for l in data[0]:
    if l != c:
        print(l, end="")
        c=l
