import sys
todo = "welcome to code jam"

def process_letter(ci, str, mtrx):
    if ci==-1:
        return (mtrx[0][0]%10000)
    for i in range(len(str)-1,-1,-1):
        mtrx[ci][i] = mtrx[ci][i+1]
        if todo[ci]==str[i]:
            if ci==len(todo)-1:
                mtrx[ci][i] += 1
            else:
                mtrx[ci][i] += mtrx[ci+1][i]
    return process_letter((ci-1), str, mtrx)

data = sys.stdin.readlines()
for i in range(int(data[0])):
    str = data[i+1].split("\n")[0]
    rc = list( set(list(str))-set(list(todo)))
    for lt in rc:
        str = str.replace(lt, "")
    mtrx = [ [0 for x in range(len(str)+1)] for t in range(len(todo)+1) ]
    s = process_letter(len(todo)-1, str, mtrx)
    print("Case #%d: %04d"%(i+1,s))
