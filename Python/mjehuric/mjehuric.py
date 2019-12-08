numbers = [int(x) for x in input().split()]
sortd = False
while not sortd:
    sortd = True
    for i in range(1,len(numbers)):
        l = numbers[i-1]
        r = numbers[i]
        if l>r:
            numbers[i]   = l
            numbers[i-1] = r
            sortd = False
            print(' '.join([str(x) for x in numbers]))