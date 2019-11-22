import sys

data = sys.stdin.readlines()
m = data[0].split(" ")[0]
d = data[0].split(" ")[1]
if m=="OCT" and d=="31\n":
    print("yup")
else:
    if m=="DEC" and d=="25\n":
        print("yup")
    else:
        print("nope")
