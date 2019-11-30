import sys
import itertools
import math
import string

stor = {}
wa = 0
wb = 0
total_votes = 0
num_lines, num_region = [int(x) for x in input().split()]
for nre in range(num_region):
    stor[nre+1] = {'A':0, 'B':0}
for _ in range(num_lines):
    rid, va, vb = [int(x) for x in input().split()]
    stor[rid]['A'] += va
    stor[rid]['B'] += vb
    total_votes += (va+vb)
for nre in range(num_region):
    total = stor[nre+1]['A']+stor[nre+1]['B']
    winner = 'A' if stor[nre+1]['A']>stor[nre+1]['B'] else 'B'
    exA = stor[nre+1]['A'] if winner=='B' else (stor[nre+1]['A']-1)-(total//2)
    exB = stor[nre+1]['B'] if winner=='A' else (stor[nre+1]['B']-1)-(total//2)
    wa += exA
    wb += exB
    print("{} {} {}".format(winner, exA, exB))
print(abs(wa-wb)/total_votes)
