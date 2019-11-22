import sys

data = sys.stdin.readlines()
r,c = [int(x) for x in data[0].strip("\n").split(" ")]

fin = {}
fin[0] = 0
fin[1] = 0
fin[2] = 0
fin[3] = 0
fin[4] = 0

for y in range(r-1):
    for x in range(c-1):
        #print(y,x)
        l = data[1+y][x:x+2]+data[2+y][x:x+2]
        #print(l)
        if "#" not in l:
            fin[l.count('X')] +=1
print(fin[0])
print(fin[1])
print(fin[2])
print(fin[3])
print(fin[4])
            
#print(data[0])
#for c in data[0].split(" "):
#    cnt[c[0]] += 1
#
#print(cnt.most_common(1)[0][1])
