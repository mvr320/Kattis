import sys
data = sys.stdin.readlines()[1:]

storage = ['1/1']

loopstop = 0

summer = 0
for i in range(6):
    summer += 2**i
    print(i+1, 2**i, summer)

for line in data:
    lid,frc = line.split()
    l,r = [int(x) for x in frc.split('/')]
    #
    # biggest one is the level...
    #
    #print(lid, frc)
    while frc not in storage[loopstop:]:
        l,r = [int(x) for x in storage[loopstop].split('/')]
        storage.append('{}/{}'.format(l, r+l))
        storage.append('{}/{}'.format(r+l, r))
        print('new: {}/{}'.format(l, r+l), '{}/{}'.format(l+r, r))
        loopstop +=1
    #print(lid, 1+loopstop+storage[loopstop:].index(frc))