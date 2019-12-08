n = int(input())
cal = sorted([int(x) for x in input().split()])
minv = 1.0
for i in range(n):
    if cal[i]/(i+1)>1.0:
        print('impossible')
        exit()
    v = cal[i]/(i+1)
    if v<minv:
        minv=v
print(minv)
