import sys
data = sys.stdin.readlines()
t=0
if int(data[0])>0:
    t=(1 if int(data[1])>0 else 4)
else:
    t=(2 if int(data[1])>0 else 3)
print(t)
