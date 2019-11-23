import sys
import itertools
import math
import string

s,p = sys.stdin.readline().split()
if 'ex' in s[-2:]:
    print(''.join([s,p]))
elif s[-1] in ['e','a','i','o','u']:
    print(s[:-1]+'ex'+p)
else:
    print(s+'ex'+p)