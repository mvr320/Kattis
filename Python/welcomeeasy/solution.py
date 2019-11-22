import sys
todo = "welcome to code jam"

def process_letter(ci, str):
    tmpstr = str[:]
    t=0
    if ci==len(todo):
        return 1
    l=tmpstr.find(todo[ci])
    while(l!=-1):
        t += process_letter(ci+1, tmpstr[l+1:])
        tmpstr = tmpstr[l+1:]
        l=tmpstr.find(todo[ci])
    return t

data = sys.stdin.readlines()
for i in range(int(data[0])):
    s = process_letter(0, data[i+1].split("\n")[0])
    print("Case #%d: %04d"%(i+1,s))
