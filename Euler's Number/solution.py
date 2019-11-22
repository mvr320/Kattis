import sys
import math
sum = 0.0
n = int(sys.stdin.readlines()[0].strip("\n"))
for it in range(n+1):
    if(it<171):
        sum +=(1.0/math.factorial(it))
print("%.200f"%sum)
