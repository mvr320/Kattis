import sys
#from collections import Counter
#cnt = Counter()

log = []
sum = 0
data = sys.stdin.readlines()

for li in range(len(data)-2, -1, -1):
    t,q,s = data[li].strip("\n").split(" ")
    if "right" in s:
        log.append(q)
        sum += int(t)
    elif q in log:
        sum += 20
print(len(log), sum)
#print(data[0])
#for c in data[0].split(" "):
#    cnt[c[0]] += 1
#
#print(cnt.most_common(1)[0][1])
