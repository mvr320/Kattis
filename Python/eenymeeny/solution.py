import sys

s = len(sys.stdin.readline().split())
names = [i.strip('\n') for i in sys.stdin.readlines()[1:]]
team = [[],[]]
swt = 0
curid=0
while(len(names)!=0):
    team[swt].append(names[ (curid+s)%len(names)-1])
    swt = (swt+1)%2
    names.remove(names[ (curid+s)%len(names)-1])
for lst in team:
    print(len(lst))
    for member in lst:
        print(member)