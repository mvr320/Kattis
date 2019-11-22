l = input().split()
a = int(l[0])
b = int(l[1])
r = []
for i in range(a+b):
	r.append(0)
res = set()
big = 0
for i in range(a):
	for j in range(b):
		r[i+j] += 1
		if big == r[i+j]:
			res.add(i+j+2)
		if big < r[i+j]:
			res = set()
			res.add(i+j+2)
			big = r[i+j]
li = list(res)
li.sort()
li.reverse()
for i in range(len(li)):
	print(li.pop())
