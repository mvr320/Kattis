import sys
import collections
data = sys.stdin.readlines()
j1,j2 = tuple([int(i) for i in data[0].split(' ')[0:2]])
list1 = list()
list2 = list()
for i in range(j1):
    list1.append(data[1+i])
for i in range(j2):
    list2.append(data[1+i+j1])
a_multiset = collections.Counter(list1)
b_multiset = collections.Counter(list2)

overlap = list((a_multiset & b_multiset).elements())
a_remainder = list((a_multiset - b_multiset).elements())
b_remainder = list((b_multiset - a_multiset).elements())

print(len(overlap))
#, a_remainder, b_remainder)
