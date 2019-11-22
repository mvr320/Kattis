import sys
data = sys.stdin.readlines()
for li in range(1,len(data)):
    if "P=NP" in data[li]:
        print("skipped")
    else:
        print(sum([int(x) for x in data[li].split("+")]))
