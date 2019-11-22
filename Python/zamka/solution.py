import sys
data = sys.stdin.readlines()
l=int(data[0])
h=int(data[1])
s=int(data[2])
for i in range(l,h+1):
    stri = str(i)
    #print("+",i,stri)
    sum = 0
    for c in range(len(stri)):
        sum += int(stri[c])
    if sum==s:
        break
print(i)
for i in range(h,l-1,-1):
    stri = str(i)
    #print("+",i,stri)
    sum = 0
    for c in range(len(stri)):
        sum += int(stri[c])
    if sum==s:
        break
print(i)

