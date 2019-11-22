import sys
data = sys.stdin.readlines()
n = int(data[0])
for ci in range(n):
    print(data[2*ci+1], end="")
    print(data[2*ci+2], end="")
    for li in range(len(data[2*ci+1])-1):
        if data[2*ci+1][li]==data[2*ci+2][li]:
            print(".", end="")
        else: 
            print("*", end="")
    print("\n")
