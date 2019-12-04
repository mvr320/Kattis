import sys
data = sys.stdin.readlines()[1:]

'''storage = ['1/1']

loopstop = 0

summer = 0
for i in range(6):
    summer += 2**i
    print(i+1, 2**i, summer)

'''
def higher_level(l,r):
    if l!=1 or r!=1:
        if l>r:
            new_l = l-r
            print("{} / {} -> {} / {}".format(l,r, new_l,r))
            return 1+higher_level(new_l,r)
        if l<r:
            new_r = r-l
            print("{} / {} -> {} / {}".format(l,r, l,new_r))
            return 1+higher_level(l,new_r)
    else:
        return 1

for line in data:
    lid,frc = line.split()
    l,r = [int(x) for x in frc.split('/')]
    print(higher_level(l,r))
'''    if l>r:
        new_l = l-r

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
    #print(lid, 1+loopstop+storage[loopstop:].index(frc))'''