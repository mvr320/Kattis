import sys
x,y = [int(x) for x in sys.stdin.readlines()[0].strip("\n").split(" ")]
if y%2==1:
    print("impossible")
else:
    print("possible")
