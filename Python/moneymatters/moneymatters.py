import sys
data = sys.stdin.readlines()
prices,lines = [int(x) for x in data[0].split()]

split_list = []

final_list = []

def merge(a,b):
    to_merge = []
    for ita in a:
        counter = 0
        for itb in range(len(b)):
            if len(ita.intersection(b[itb]))>0:
                b[itb] = ita.union(b[itb])
                counter +=1
        if counter>1:
            b = divide(b)
        if counter==0:
            to_merge.append(ita)
    for item in to_merge:
        b.append(item)
    return b

def divide(a,b):
    fa = set()
    fb = set()
    if len(a)==1:
        fa = a
    else:
        fa = divide(a)
    if len(b)==1:
        fb = b
    else:
        fb = divide(b)
    return merge(a,b)

for i in range(lines):
    #a,b = [int(x) for x in data[i+prices+1].split()]
    a,b = data[i+prices+1].split()
    if i!=0:
        split_list.append( set([a,b]))
    else:
        final_list.append( set([a,b]))

#Maybe divide...
for it1 in range(len(split_list)):
    mixed = False
    for it2 in range(len(final_list)):
        if len(final_list[it2].intersection(split_list[it1]))>0:
            final_list[it2] = final_list[it2].union(split_list[it1]
            mixed = True
    if not mixed:
        final_list.append(split_list[it1])

'''while change:
    change = False
    for it1 in range(len(split_list)):
        for it2 in range(it1+1,len(split_list)):
            if len(split_list[it1].intersection(split_list[it2]))>0:
                split_list[it1] = split_list[it1].union(split_list[it2])
                split_list[it2] = set()
    tmp_split_list = []
    for it1 in split_list:
        if len(it1)>0:
            tmp_split_list.append(it1)
        else:
            change = True
    split_list = tmp_split_list[:]'''

for tset in split_list:
    summer = 0
    for item in tset:
        summer += int(data[item+1])
    if summer != 0:
        print('IMPOSSIBLE')
        exit()
print('POSSIBLE')
        