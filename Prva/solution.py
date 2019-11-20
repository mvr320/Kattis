import sys
data = sys.stdin.readlines()
r,c = [int(x) for x in data[0].split(" ")]

wlist = []
for ri in range(r):
    string = ""
    for ci in range(c):
        ltr = data[1+ri][ci]
        if ltr !="#":
            string += ltr
        else:
            if len(string)>1:
                wlist.append(string)
            string = ""
    if len(string)>1:
        wlist.append(string)
    string = ""
for ci in range(c):
    string = ""
    for ri in range(r):
        ltr = data[1+ri][ci]
        if ltr !="#":
            string += ltr
        else:
            if len(string)>1:
                wlist.append(string)
            string = ""
    if len(string)>1:
        wlist.append(string)
    string = ""
print(sorted(wlist)[0])
