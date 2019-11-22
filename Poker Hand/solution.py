import sys
from collections import Counter

cnt = Counter()

data = sys.stdin.readlines()
#print(data[0])
for c in data[0].split(" "):
    cnt[c[0]] += 1

print(cnt.most_common(1)[0][1])
