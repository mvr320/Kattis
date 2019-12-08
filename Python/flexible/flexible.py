import itertools
w,a = [int(x) for x in input().split()]
dividers = [int(x) for x in input().split()]

room_layouts = set()
for i in range(0,a+1):
    for comb in itertools.combinations(dividers,i):
        small = 0
        for d in sorted(comb):
            room_layouts.add(d-small)
            small = d
        room_layouts.add(w-small)
print(' '.join([str(i) for i in sorted(room_layouts)]))