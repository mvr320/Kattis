import sys
iter = int(sys.stdin.readlines()[0])
start = "A"
ac = 1
bc = 0
for i in range(iter):
    new = ""
    for j in start:
        if j == "A":
            new+="B"
            #ac-=1
            #bc+=1
        else:
            new+="AB"
            #ac+=1
    start = new[:]
print(start.count("A"),start.count("B"))
