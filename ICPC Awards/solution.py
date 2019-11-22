import sys

ul = []
cnt = 0
data = sys.stdin.readlines()
for l in range(1,len(data)):
    u,t = data[l].strip("\n").split(" ")
    if u not in  ul:
        ul.append(u)
        print(u,t)
        cnt+=1
        if cnt==12:
            exit()
