nt = int(input())
targets = []
for _ in range(nt):
    targets.append(input().split())
ns = int(input())
shots = []
for _ in range(ns):
    shots.append([int(x) for x in input().split()])
for shot in shots:
    hit = 0
    for target in targets:
        if target[0]=='circle':
            hit += 1 if ((int(target[1])-shot[0])**2)+((int(target[2])-shot[1])**2) <= int(target[3])**2 else 0
        if target[0]=='rectangle':
            x1 = int(target[1])
            y1 = int(target[2])
            x2 = int(target[3])
            y2 = int(target[4])
            if shot[0]>=x1 and shot[0]<=x2 and shot[1]>=y1 and shot[1]<=y2:
                hit += 1
    print(hit)