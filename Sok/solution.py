import sys

data = sys.stdin.readlines()
a,b,c = [int(x) for x in data[0].strip("\n").split(" ")]
i,j,k = [int(x) for x in data[1].strip("\n").split(" ")]
sr = 0
if a/i<b/j:
    if a/i<c/k:
        sr=a/i
    else:
        sr=c/k
else:
    if b/j<c/k:
        sr=b/j
    else:
        sr=c/k 
print("%.17f %.17f %.17f"%(a-(sr*i), b-(sr*j), c-(sr*k)))
