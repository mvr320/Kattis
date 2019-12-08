import sys
data = sys.stdin.readlines()
numbers = [int(x) for x in data[1:]]
maxv = sorted(numbers)[-1]
needed = list(range(1,maxv+1))
if len(needed)==len(numbers):
    print('good job')
    exit()
for i in sorted(set(needed)-set(numbers)):
    print(i)