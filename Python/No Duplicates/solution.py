import sys
from collections import Counter

cnt = Counter()
data = sys.stdin.readlines()[0].strip("\n").split(" ")
for word in data:
    cnt[word] += 1
if cnt.most_common()[0][1]>1:
    print("no")
else:
    print("yes")
