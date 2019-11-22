import sys
data = sys.stdin.readlines()
c=int(data[0])
for i in range(c):
    values = [int(t) for t in data[i+1].split(' ')]
    #print(values)
    import_val = 0
    for n in range(1,len(values)):
        diff = values[n]-(values[n-1]*2)
        if diff>0:
            import_val += diff
    print(import_val)
