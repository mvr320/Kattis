import sys

sum=0
data = sys.stdin.readlines()
for i in range(1,len(data)):
    sum += 1 if "CD" not in data[i] else 0
print(sum)
