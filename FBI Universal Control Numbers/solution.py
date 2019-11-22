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
    print(inp)
    string.ascii_lowercase
#
    #'B','8'print(line)
