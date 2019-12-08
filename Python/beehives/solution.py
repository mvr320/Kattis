import sys
import itertools
import math

data = sys.stdin.readlines()
processed=0
cnt = 1
while(processed != len(data)-1):
    d,n = data[processed].split(' ')
    d = float(d)
    n = int(n)
    sour = 0
    swee = 0
    coords = []
    for lid in range(n):
        x,y = [float(i) for i in data[processed+lid+1].split(' ')]
        coords.append( (x,y) )
    for pairid in range(len(coords)):
        sour_ish = False
        for pairid2 in range(len(coords)):
            if pairid!=pairid2:
                (x1,y1) = coords[pairid]
                (x2,y2) = coords[pairid2]
                summer = (x1-x2)**2+(y1-y2)**2
                if (math.sqrt(summer)-d)<0:
                    if not sour_ish:
                        sour_ish = True
                        sour +=1
        if not sour_ish:
            swee +=1
    print("{} sour, {} sweet".format(sour,swee))
    processed += n+1
