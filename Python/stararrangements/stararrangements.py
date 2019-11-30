import sys
import itertools
import math
import string

num_stars = int(input())
print("{}:".format(num_stars))
for i in range(2,(1+(num_stars+1)//2) ):
    for j in range(i-1,i+1):
        if num_stars%(i+j)==0:
            print("{},{}".format(i,j))
        if num_stars%(i+j)==i:
            print("{},{}".format(i,j))