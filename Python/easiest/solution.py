import sys
data = sys.stdin.readlines()
for li in range(len(data)-1):
    bool = True
    lii = data[li].strip("\n")
    sumn = sum( [int(x) for x in lii])
    p = 11
    while bool:
        sumpn = sum( [int(x) for x in str(int(lii)*p)])
        if sumpn==sumn:
            print(p)
            bool = 0
        else:
            p+=1
