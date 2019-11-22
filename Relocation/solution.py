import sys
data = sys.stdin.readlines()
n,q = [int(x) for x in data[0].split(" ")]
initloc = [int(x) for x in data[1].split(" ")]
loc = {}
for i in range(1,n+1):
    loc[i] = initloc[i-1]
for l in range(2,len(data)):
    a,b,c = [int(x) for x in data[l].split(" ")]
    if a==1:
        loc[b]=c
    else:
        print(abs(loc[b]-loc[c]))
