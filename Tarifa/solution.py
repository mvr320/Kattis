import sys
data = sys.stdin.readlines()
mbpm = int(data[0])
n=int(data[1])+1
t=mbpm*n
for i in range(2, len(data)):
    t-=int(data[i])
print(t)
