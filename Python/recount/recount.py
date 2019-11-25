import sys
import itertools
import math
import string
from collections import Counter

votes = [item.strip('\n') for item in sys.stdin.readlines()[:-1]]
cntr = Counter(votes)

highest = 0
names = set(votes)
winner = None

for item in names:
    if cntr[item]==highest:
        winner = None
    if cntr[item]>highest:
        highest = cntr[item]
        winner = item

if winner==None:
    print('Runoff!')
else:
    print(winner)