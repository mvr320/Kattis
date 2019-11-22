import sys

import string
digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

data = sys.stdin.readlines()
for i in range(len(data)-1):
    l = data[i].split("\n")[0].split(" ")
    b = int(l[0])
    p = int(l[1],b)
    m = int(l[2],b)
    print(int2base(p%m, b))
