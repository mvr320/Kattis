import sys
data = sys.stdin.readlines()
output = []
for lid in range(len(data)):
    if 'FBI' in data[lid]:
        output.append(str(lid+1))
if len(output)==0:
    print('HE GOT AWAY!')
else:
    print(' '.join(output))
