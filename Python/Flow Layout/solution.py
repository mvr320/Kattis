import sys
import itertools
import math
import string

processed = 0
lines = sys.stdin.readlines()
while(processed != len(lines)-1):
    mwidth = int(lines[processed])
    lcount = 1
    width = 0
    t_mwidth = 0
    height = 0
    t_height = 0
    while('-1 -1' not in lines[lcount+processed]):
        w,h = [int(i) for i in lines[lcount+processed].split(' ')]
        if t_mwidth+w<=mwidth:
            t_mwidth +=w
            if t_height<h:
                t_height = h
        else:
            if t_mwidth>width:
                width = t_mwidth
            t_mwidth = w
            height += t_height
            t_height = h
        #print(w,h)
        lcount +=1
    height += t_height
    if t_mwidth>width:
        width = t_mwidth
    print("{} x {}".format(width,height))
    processed += lcount+1
