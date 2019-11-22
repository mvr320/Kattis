import sys

data = sys.stdin.readlines()
for c in range(1,int(data[0])+1):
    b = int(data[c].split(" ")[0])
    p = float(data[c].split(" ")[1])
    print("%.17f %.17f %.17f"%( (60*(b-1)/p), (60*b/p), (60*(b+1)/p)))
