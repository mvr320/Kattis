import sys
data = sys.stdin.readlines()
for c in range(len(data)-1):
    i = int(data[c].split(" ")[0])
    s = data[c].strip("\n").split(" ")[1][::-1]
    for l in s:
        if '_'==l:
            n = 91
        elif '.'==l:
            n = 92
        else:
            n = ord(l)
        p = chr((n+i-ord('A'))%28+ord('A'))
        if '\\'==p:
            p='.'
        elif '['==p:
            p='_'
        print(p,end="")
    print("")
