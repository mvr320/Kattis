import sys
alld = sys.stdin.readlines()
cases = int(alld[0])
data = alld[1:]
trans = data[:]
c=0
def wrong():
    print('0')
    exit()

for line in data:
    if 'BBB' in line:
        wrong()
    if 'WWW' in line:
        wrong()
    if line.count('B')!=line.count('W'):
        wrong()

for i in range(cases):
    line = ''
    for j in range(cases):
        line += data[j][i]
    if 'BBB' in line:
        wrong()
    if 'WWW' in line:
        wrong()
    if line.count('B')!=line.count('W'):
        wrong()


print('1')

#print(trans)
