import sys
data = sys.stdin.readlines()
c = int(data[0])
a = ""
b = ""
g = ""
at = 0
bt = 0
gt = 0

for i in range((c//4)+1):
    a +="ABCABC"
    b +="BABC"
    g +="CCAABB"

for l in range(len(data[1].strip("\n"))):
    #print(data[1], a, b, g)
    if data[1][l]==a[l]:
        at+=1
    if data[1][l]==b[l]:
        bt+=1
    if data[1][l]==g[l]:
        gt+=1

m = max(at,max(bt,gt))
print(m)
if at==m:
    print("Adrian")
if bt==m:
    print("Bruno")
if gt==m:
    print("Goran")
