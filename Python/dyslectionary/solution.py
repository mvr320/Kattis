import sys

data = sys.stdin.readlines()
maxa = 0
min = 0
store = []
for i in range(len(data)):
    if len(data[i])==1:
        store.sort()
        for j in range(len(store)):
            #print("[]", i,j, data[j].strip("\n"))
            print(" "*(maxa-1-len(store[j]))+store[j][::-1])
        min = i
        maxa = 0
        print("")
        store = []
    else:
        store.append(data[i].strip("\n")[::-1])
        maxa = max(maxa, len(data[i]))
    #print(len(data[i]), data[i].strip("\n"))
store.sort()
#print("")
for j in range(len(store)):
    print(" "*(maxa-1-len(store[j]))+store[j][::-1])
