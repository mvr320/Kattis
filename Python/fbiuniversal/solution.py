import sys
import itertools
import math
import string

data = sys.stdin.readlines()
for line in data[1:]:
    ident,inp = line.split(' ')
    repl = [('B','8'), ('G','C'), ('I','1'), ('O','0'), ('Q','0'), ('S','5'), ('U','V'), ('Y','V'), ('Z','2')]
    for (ci,cj) in repl:
        inp = inp.replace(ci,cj)
    inp = inp.strip('\n')
    multi = [2,4,5,7,8,10,11,13]
    summer = 0
    for i in range(8):
        char = list(inp)[i]
        val = 0
        if not char.isdigit():
            val = 10+string.ascii_uppercase.index(char)
        else:
            val = int(char)
        summer += multi[i]*val
    check = 0
    char = list(inp)[8]
    val = 0
    if not char.isdigit():
        val = 10+string.ascii_uppercase.index(char)
    else:
        val = int(char)
    total = summer%27
    print(ident, total, val)
