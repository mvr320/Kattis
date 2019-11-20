import sys
sum = 0
cnt = 0
data = sys.stdin.readlines()
m,c = [int(x) for x in data[0].strip("\n").split(" ")]
for ci in range(1,c+1):
    s,n = data[ci].split(" ")
    if "enter" in s:
        if int(n)+sum>m:
            cnt +=1
        else:
            sum += int(n)
    else:
        sum -= int(n)
print(cnt)
