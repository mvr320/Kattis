import sys
data = sys.stdin.readlines()
l,c1,c2 = tuple([int(i) for i in data[0].split(" ")])
lw = l-c1 if l-c1>c1 else c1
lh = l-c2 if l-c2>c2 else c2
print(lw*lh*4)
#data[1].split(" ").index(str(lv)))
