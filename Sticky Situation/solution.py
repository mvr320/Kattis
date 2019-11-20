import sys
data = sorted([int(i) for i in sys.stdin.readlines()[1].strip('\n').split(' ')])
doable = False
for i in range(len(data)-2):
    if not doable:
        if data[i]+data[i+1]>data[i+2]:
            print("possible")
            doable = True
if not doable:
    print("impossible")
