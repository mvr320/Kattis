import sys
data = sys.stdin.readlines()[1:]
#storage = {}
#for p in [(2,'abc'), (3,'def'), (4,'ghi'),(5,'jkl'),(6,'mno'),(7,'pqrs'),(8,'tuv'),(9,'wxyz')]:
#    c,s = p
#    for t in list(s):
#        storage[t] = c
#print(storage)
storage = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}

counter = 0
code = int(data[-1].strip('\n'))
for line in data[:-1]:
    #tmp_code = int(''.join(str([storage[x] for x in list(line.strip('\n'))])))
    tmp_code = int(''.join([str(storage[x]) for x in list(line.strip('\n'))]))
    #print(tmp_code, code)
    if code==tmp_code:
        counter += 1
print(counter)