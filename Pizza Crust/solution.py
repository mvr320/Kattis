import sys
import math
r,c = [int(x) for x in sys.stdin.readlines()[0].split(" ")]

rv  =r**2*math.pi
icv =(r-c)**2*math.pi
print("%.100f"%(100.0*(icv/rv)))
