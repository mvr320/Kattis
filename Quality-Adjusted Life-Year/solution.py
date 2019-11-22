import sys
data = sys.stdin.readlines()
p = int(data[0])
t=0.0
for i in range(1, len(data)):
    s=data[i].split()
    t+=float(s[0])*float(s[1])
print(t)
