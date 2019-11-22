import math
line = input()
t = int(line.split()[0])
d = int(line.split()[1])
h = int(line.split()[2])
s = math.sqrt(float(d)**2+float(h)**2)
for i in range(t):
	j = input()
	if s<float(j):
		print("NE")
	else:
		print("DA")
