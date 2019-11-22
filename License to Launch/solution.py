import sys
data = sys.stdin.readlines()
lv = sorted([int(x) for x in data[1].split(" ")])[0]
print(data[1].split(" ").index(str(lv)))
