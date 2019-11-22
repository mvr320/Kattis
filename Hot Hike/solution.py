import sys
data = [int(i) for i in sys.stdin.readlines()[1].strip('\n').split(' ')]
mt = 41
md = 0
for i in range(len(data)-2):
    ct = sorted([data[i],data[i+2]])[1]
    if ct<mt:
        mt=ct
        md=i
print(md+1,mt)
