import sys
from collections import Counter

cnt = Counter()
i=1
data = sys.stdin.readlines()
for l in range(2, len(data), 2):
    for g in data[l].strip("\n").split(" "):
        cnt[g] +=1
    print("Case #%d: %s"%(i,cnt.most_common()[::-1][0][0]))
    cnt = Counter()
    i+=1
