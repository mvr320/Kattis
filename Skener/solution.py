import sys
data = sys.stdin.readlines()
line = data[0].strip("\n").split(" ")
r, c, zr, zc = [int(i) for i in line]
for ri in range(r):
    for zri in range(zr):
        for ci in range(c):
            for zci in range(zc):
                print(data[ri+1][ci], end="")
        print("")
