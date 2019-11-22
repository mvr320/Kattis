import sys
data = sys.stdin.readlines()
for c in range(1,1+int(data[0])):
    b = int(len(data[c].strip("\n"))**0.5)
    for i in range(b-1,-1,-1):
        for j in range(b):
            print(data[c][j*b+i], end="")
    print("")
