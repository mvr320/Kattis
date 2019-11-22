import sys
fl = float(sys.stdin.readlines()[0].strip("\n"))
cr = 5280.0/4854.0*1000.0
print(int(0.5+(fl*cr)))
