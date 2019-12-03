_ = input()
data = [int(x) for x in input().split()]
for it in sorted(list(set(data)), reverse=True):
    if data.count(it)==1:
        print(data.index(it)+1)
        exit()
print('none')