import sys
import itertools
import math
import string

x,y,x1,y1,x2,y2 = [int(x) for x in sys.stdin.readline().split()]
dist = 0.0
if x<=x1 and y<=y1:
    #print("1-", x, x1, y, y1)
    dist = math.sqrt( (x-x1)**2 + (y-y1)**2 )
elif x<=x1 and y>y2:
    #print("2-", x, x1, y2, y)
    dist = math.sqrt( (x-x1)**2 + (y-y2)**2 )
elif x>x2 and y<=y1:
    #print("3-", x2, x, y, y1)
    dist = math.sqrt( (x-x2)**2 + (y-y1)**2 )
elif x>x2 and y>y2:
    #print("4-", x2, x, y2, y)
    dist = math.sqrt( (x-x2)**2 + (y-y2)**2 )
if y>y1 and y2>y and x<x1:
    # So the difference is the ratio on where we are between the ycoords, same ratio for where the crossing of the x is
    #yr = (y-y1)/(y2-y1)
    #xt = (x2-x1)*yr
    #print("5-")
    dist = math.sqrt( (x-x1)**2 )
elif y>y1 and y2>y and x>x2:
    #print("6-")
    #yr = (y-y1)/(y2-y1)
    #xt = (1-(x2-x1))*yr
    dist = math.sqrt( (x-x2)**2 )
elif x>x1 and x2>x and y<y1:
    #print("7-", x2, x, y2, y)
    #xr = (x-x1)/(x2-x1)
    #yt = (y2-y1)*xr
    dist = math.sqrt( (y-y1)**2 )
    #dist = math.sqrt( (y-yt)**2 )
elif x>x1 and x2>x and y>y2:
    #print("8-", x2, x, y2, y)
    #xr = (x-x1)/(x2-x1)
    #yt = (1-(y2-y1))*xr
    #dist = math.sqrt( (y-yt)**2 )
    dist = math.sqrt( (y-y2)**2 )
'''
else:
    area = (x*(y1-y2) + x1*(y-y2) + x2*(y-y1))/2
    height = (2*area)/( math.sqrt( (x2-x1)**2+(y2-y1)**2 ) )
    dist = height'''
print(dist)