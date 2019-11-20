import sys

data = sys.stdin.readlines()
a = int(data[0].strip("\n").split(" ")[0])
b = int(data[0].strip("\n").split(" ")[1])
c = int(data[0].strip("\n").split(" ")[2])
print(max(b-a, c-b)-1)
