import sys
data = sys.stdin.readlines()[1:]
for line in data:
    numbers = [int(x) for x in line.split()][1:]
    done = False
    for i in range(1,len(numbers)):
        if not done:
            #print(numbers[i], numbers[i-1])
            if (numbers[i]-numbers[i-1])!=1:
                print(i+1)
                done = True