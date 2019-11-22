import sys

data = sys.stdin.readlines()
g,s,c = [int(x) for x in data[0].split(" ")]
bpow = g*3+s*2+c
if bpow>=8:
    print("Province or ", end="")
elif bpow>=5:
    print("Duchy or ", end="")
elif bpow>=2:
    print("Estate or ", end="")

if bpow>=6:
    print("Gold")
elif bpow>=3:
    print("Silver")
elif bpow>=0:
    print("Copper")

