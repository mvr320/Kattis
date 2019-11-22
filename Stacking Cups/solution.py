import sys
data = sys.stdin.readlines()
wlist = {}
for li in range(1,len(data)):
    arg1,arg2 = [x for x in data[li].split(" ")]
    try:
        cnt = int(arg2)
        col = arg1.strip("\n")
        wlist[cnt] = col
    except ValueError:
        cnt = int(int(arg1)/2.0)
        col = arg2.strip("\n")
        wlist[cnt] = col
for it in sorted(wlist):
    print(wlist[it])
