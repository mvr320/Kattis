import itertools

l,h = [int(x) for x in input().split()]

total_tries = 0
for comb in itertools.combinations(range(1,10), 6):
    #print(comb)
    for perm in itertools.permutations(comb):
        number = int(''.join([str(i) for i in perm]))
        if l<=number and number<=h:
            usable = True
            for digit in comb:
                if number%digit!=0:
                    usable = False
            if usable:
                total_tries += 1
print(total_tries)