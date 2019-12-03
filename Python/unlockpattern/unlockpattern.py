import math

data = [0,0,0,0,0,0,0,0,0]
order = [0,0,0,0,0,0,0,0,0]
for i in range(3):
    row = [int(x) for x in input().split()]
    for j in range(3):
        data[i*3+j] = row[j]
        order[row[j]-1] = (i,j)#i*3+j
        #print(row[j], order)
#print(data)
#print(order)
#print(j,i, i*3+j)
#print(data)
#for j in range(3):
#    try:
#        print(data[j].find(1))
#    except ValueError as e:
#        print('t:',j)
cur = None
dist = .0
for p in order:
    if cur == None:
        cur = p
    else:
        l,r = cur
        lp,rp = p
        dist += math.sqrt( (l-lp)**2 + (r-rp)**2 )
        cur = p
print(dist)