import sys
while True:
    result = []
    total = int(input())
    storage = {}
    if total == -1:
        exit()
    #Lets assume we can be our own neighbor
    for i in range(total):
        storage[i] = {}
        #Lets assume we can never be our own neighbor
        vertices = [int(x) for x in input().split()]
        for j in range(total):
            if i!=j:
                if bool(vertices[j]):
                    storage[i][j] = True
    for key in storage.keys():
        neighbors = set(storage[key].keys())
        found = False
        for nk in storage[key].keys():
            if not found:
                n_neighbors = set(storage[nk].keys())
                if len(neighbors.intersection(n_neighbors))>0:
                    found = True
        if not found:
            result.append(str(key))
    print(' '.join(sorted(result)))