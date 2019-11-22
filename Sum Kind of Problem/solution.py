import sys

data = sys.stdin.readlines()

for it in range(1,len(data)):
    l = data[it].strip("\n").split(" ")
    k,n = [int(x) for x in l]
    print( it, int( (1+n)*n/2), int( (2*n)*n/2), int( (2+2*n)*n/2) )
