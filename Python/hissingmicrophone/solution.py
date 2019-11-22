import sys

data = sys.stdin.readlines()
if "ss" not in data[0]:
    print("no hiss")
else:
    print("hiss")
