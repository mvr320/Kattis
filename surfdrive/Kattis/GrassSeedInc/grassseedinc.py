c = float(input())
n = int(input())
sum = 0.0
for i in range(n):
	s = input().split()
	sum += (float(s[0])*float(s[1]))*c
print(round(sum,8))
