import sys

data = sys.stdin.readlines()[0].strip("\n")
for v in "aeiou":
    data = data.replace(v+"p"+v, v)
print(data)
