import sys
line = sys.stdin.readlines()[0].strip("\n")
s = {}
s['T'] = 0
s['C'] = 0
s['G'] = 0
for l in line:
    s[l]+=1
#print(s)
print(s['T']**2 + s['C']**2 + s['G']**2 + 7*min(s['T'],min(s['C'],s['G'])))
