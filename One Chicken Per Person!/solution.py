import sys

data = sys.stdin.readlines()
n = int(data[0].strip("\n").split(" ")[0])
m = int(data[0].strip("\n").split(" ")[1])
if n<m:
    s = 's' if (m-n>1) else ''
    print("Dr. Chaz will have %d piece%s of chicken left over!"%(m-n, s))
else:
    s = 's' if (n-m>1) else ''
    print("Dr. Chaz needs %d more piece%s of chicken!"%(n-m, s))

