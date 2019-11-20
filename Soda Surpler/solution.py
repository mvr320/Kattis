import sys

e,f,c = [int(x) for x in sys.stdin.readlines()[0].strip("\n").split(" ")]
st = e+f
ct = st
fb = 0
while ct>=c:
    ct = ct-c+1
    fb +=1
print(fb)
