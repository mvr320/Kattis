import sys
data = sys.stdin.readlines()
n,t = [int(x) for x in data[0].split(" ")]
tl = [int(x) for x in data[1].split(" ")]
f=0
for ta in tl:
    if t-ta>0:
        f+=1
        t-=ta
    else:
        print(f)
        exit()
