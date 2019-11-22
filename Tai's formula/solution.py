import sys
data = sys.stdin.readlines()
tc = int(data[0].strip('\n'))
score = 0.0
for i in range(tc-1):
    t0 = int(data[1+i].strip('\n').split(' ')[0])
    t1 = int(data[2+i].strip('\n').split(' ')[0])
    g0 = float(data[1+i].strip('\n').split(' ')[1])
    g1 = float(data[2+i].strip('\n').split(' ')[1])
    score += (g1+g0)/2.0*(t1-t0)/1000
print(score)
