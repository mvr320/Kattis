def rec(a):
    if a==1:
        return a
    return rec(a-1)*a

import sys
data = sys.stdin.readlines()
for c in range(int(data[0])):
    print(rec(int(data[c+1]))%10)
