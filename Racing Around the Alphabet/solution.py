import sys

data = sys.stdin.readlines()
store = {}
for i in range(91-65):
    store[chr(i+65)] = [i,i+28]
    #print(chr(i+65))
store[' ']=[26,26+28]
store['\'']=[27,27+28]
const = 60.0/28.0
for r in range(1,len(data)):
    sum = 1.0
    line = data[r].strip("\n")
    for l in range(1,len(line)):
        lea = 1000.0#abs(store[data[r][l-1]][0]-store[data[r][l]][0])
        ria = abs(store[data[r][l-1]][0]-store[data[r][l]][1])
        leb = 1000.0#abs(store[data[r][l-1]][1]-store[data[r][l]][0])
        rib = abs(store[data[r][l-1]][1]-store[data[r][l]][1])
        mini = min(min(lea,ria), min(leb,rib))
        sum += 1.0
        print(data[r][l], end="")
    print(sum, len(line))
