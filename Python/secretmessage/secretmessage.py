import sys
import math
data = sys.stdin.readlines()[1:]

for line in data:
    message = ''
    line = line.strip('\n')
    near_qu = math.ceil(math.sqrt(len(line)))
    #print(len(line), near_qu)
    mtrx = []
    ntrx = []
    for i in range(near_qu):
        mtrx.append([])
        ntrx.append([])
        for j in range(near_qu):
            if i*near_qu+j>=len(line):
                mtrx[i].append('*')
            else:
                mtrx[i].append(line[i*near_qu+j])
            ntrx[i].append('*')
    for i in range(near_qu):
        line = ''
        for j in range(near_qu):
            line += mtrx[i][j]
        #print(line)
    for i in range(near_qu):
        for j in range(near_qu):
            ntrx[j][near_qu-i-1] = mtrx[i][j]
    for i in range(near_qu):
        for j in range(near_qu):
            if ntrx[i][j] != '*':
                message += ntrx[i][j]
    print(message)