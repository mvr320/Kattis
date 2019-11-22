import sys
data = sys.stdin.readlines()
for i in range(1,len(data)):
    print(len(data[i])-1)
