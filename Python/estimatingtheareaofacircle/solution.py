import sys
import math
data = sys.stdin.readlines()
for li in range(len(data)-1):
    r,m,c = [float(x) for x in data[li].split(" ")]
    print("%.20f %.20f"%(r**2*math.pi, c/m*(2*r)**2))
