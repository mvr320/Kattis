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
    # (2*D1 + 4*D2 + 5*D3 + 7*D4 + 8*D5 + 10*D6 + 11*D7 + 13*D8) mod 27

    for char in list(inp):
        if not char.isdigit():
            print(char)
            print(1+string.ascii_uppercase.index(char))
    #print(string.ascii_uppercase)
    #string.ascii_lowercase
