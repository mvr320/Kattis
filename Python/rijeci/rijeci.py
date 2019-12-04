import sys
count = int(input())
start = "A"

storage = {}
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    global storage
    n1 = None
    n2 = None
    if n-1 not in storage.keys():
        storage[n-1] = fib(n-1)
    if n-2 not in storage.keys():
        storage[n-2] = fib(n-2)
    return storage[n-1]+storage[n-2]

count_A = fib(count-1)
count_B = fib(count)
print(count_A, count_B)
'''for i in range(count):
    new = ''
    for char in list(start):
        if char=='A':
            new += 'B'
        if char=='B':
            new += 'BA'
    #print(new)
    start = new[:]
    #print(start)
print(start.count('A'), start.count('B'))'''