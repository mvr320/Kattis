n = int(input())
for _ in range(n):
    i = int(input())
    start = .0
    for j in range(i):
        start += .5
        start *= 2
    print(int(start))
