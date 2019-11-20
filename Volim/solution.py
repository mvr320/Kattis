import sys

tp = 60*3+30
data = sys.stdin.readlines()
person = int(data[0])
for i in range(int(data[1])):
    t = int(data[2+i].split(" ")[0])
    v = data[2+i].split(" ")[1]
    tp -= t
    #print(tp,person)
    if tp>0:
        if "T" in v:
            person += 1
            if person>8:
                person = 1
    else:
        print(person)
        exit()
