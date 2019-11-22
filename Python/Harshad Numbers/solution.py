import sys

n = int(sys.stdin.readlines()[0].strip("\n"))
while 1:
    suma = [int(c) for c in str(n)]
    #print(sum(suma))
    if (n%sum(suma))==0:
        print(n)
        exit()
    n+=1
    
