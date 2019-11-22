import sys

data = sys.stdin.readlines()
d=0
s=0
for c in [int(b) for b in data[1].split(" ")]:
    if c!=-1:
        d+=1
        s+=c
print("%.17f"%(float(s)/float(d)))
