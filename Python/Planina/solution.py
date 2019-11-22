def rec(a):
    if a==0:
        return 2
    return (rec(a-1)+rec(a-1)-1)

import sys
data = sys.stdin.readlines()
print(rec(int(data[0]))**2)
