l = input()
c = 3
sum = 0
for i in range(int(len(l)/3)):
	if l[i*c]!='P':
		sum += 1
	if l[i*c+1]!='E':
		sum += 1
	if l[i*c+2]!='R':
		sum += 1
print(sum)
