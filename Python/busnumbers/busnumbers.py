_ = input()
busnumbers = sorted([int(x) for x in input().split()])
out = []
last = None
final = []
for n in range(len(busnumbers)):
    if (busnumbers[n]-1)!=last:
        out.append([busnumbers[n]])
        last = busnumbers[n]
    else:
        out[-1].append(busnumbers[n])
        last = busnumbers[n]
for lst in out:
    if len(lst)<3:
        final.append(str(lst[0]))
        if len(lst)==2:
            final.append(str(lst[1]))
    else:
        final.append(str(lst[0])+'-'+str(lst[-1]))
print(' '.join(final))