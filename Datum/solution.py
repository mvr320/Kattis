import sys
import datetime
data = sys.stdin.readlines()
d = int(data[0].split(" ")[0])
m = int(data[0].split(" ")[1])
print(datetime.datetime(2009,m,d).strftime('%A'))
