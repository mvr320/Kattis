import sys
data = sys.stdin.readlines()[0].strip('\n')
who = list(data)[0::2]
val = [int(i) for i in list(data)[1::2]]
result = {'A':0,'B':0}
for i in range(len(who)):
    result[who[i]] += val[i]
print('A' if result['A']>result['B'] else 'B')
