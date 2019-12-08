h,v = input().split()
vid = 0
hid = 0
for i in range(len(h)):
    if h[i] in v:
        hid = i
        vid = v.index(h[i])
        break
for i in range(len(v)):
    line = []
    for j in range(len(h)):
        if hid==j:
            line.append(v[i])
        elif vid==i:
            line.append(h[j])
        else:
            line.append('.')
    print(''.join(line))