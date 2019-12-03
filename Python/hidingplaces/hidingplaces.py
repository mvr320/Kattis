import sys
data = sys.stdin.readlines()
total_k = 0
row_done = 0
col_done = 0
storage = []
for i in range(5):
    storage.append([])
    for j in range(5):
        storage[i].append(0)
for line in data:
    for pl in list(line.strip('\n')):
        if pl=='k':
            total_k += 1
            mutation = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
            #print(storage)
            for mut in mutation:
                rd,cd = mut
                rs = row_done-rd
                cs = col_done-cd 
                if rs>=0 and cs>=0 and rs<5 and cs<5:
                    #print(storage[rs][cs])
                    if storage[rs][cs]==1:
                        print('invalid')
                        exit() 
            #print(row_done, col_done)
            storage[row_done][col_done]=1
        col_done += 1
    row_done += 1
    col_done = 0
#print(storage)
print('valid' if total_k==9 else 'invalid')