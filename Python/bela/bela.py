l = input().split()
n = int(l[0])
t = l[1]
D = {"A":11,"K":4,"Q":3,"J":20,"T":10,"9":14,"8":0,"7":0}
N = {"A":11,"K":4,"Q":3,"J":2,"T":10,"9":0,"8":0,"7":0}
sum = 0
for i in range(n*4):
	v = input()
	if v[1]	== t:
		sum+=D[v[0]]
	else:
		sum+=N[v[0]]
print(sum)
