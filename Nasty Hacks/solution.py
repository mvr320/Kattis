import sys

data = sys.stdin.readlines()
for i in range(1,int(data[0])+1):
    #print(data[i].split(" "))
    r = int(data[i].split("\n")[0].split(" ")[0])
    e = int(data[i].split("\n")[0].split(" ")[1])
    c = int(data[i].split("\n")[0].split(" ")[2])
    if r+c<e:
        print("advertise")
    else:
        if r+c==e:
            print("does not matter")
        else:
            print("do not advertise")
