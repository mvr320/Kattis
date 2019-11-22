import sys
import itertools
import math
import string

def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

processed = 0
lines = sys.stdin.readlines()
while(processed != len(lines)-1):
    lpoint = int(lines[processed])
    coords = []
    for plin in range(lpoint):
        x,y = [int(i) for i in lines[plin+processed+1].split(' ')]
        coords.append( (x,y) )
    print(coords, PolygonArea(coords))
    processed += lpoint+1
