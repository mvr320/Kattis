import sys
import itertools
import math
import string


for inp in range(10):
    count = 0
    subs = '11'
    count2 = 0
    subs2 = '01'
    for i in range(2**inp):
        if subs not in "{0:b}".format(i):
            count +=1
    for i in range(2**inp):
        if subs2 not in "{0:b}".format(i):
            count2 +=1
    print(inp, count, count2, count-count2)