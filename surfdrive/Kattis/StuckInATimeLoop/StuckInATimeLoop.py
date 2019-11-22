import fileinput

for var in fileinput.input():
	for i in range(1,(int)(var)+1):
		print i, "Abracadabra";
