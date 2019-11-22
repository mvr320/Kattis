import sys
data = sys.stdin.readlines()
for l in range(1,len(data)):
    a,b,c = [int(x) for x in data[l].split(" ")]
    if a+b==c:
        print("Possible")
    elif a*b==c:
        print("Possible")
    elif a-b==c:
        print("Possible")
    elif b-a==c:
        print("Possible")
    elif a/b==c:
        print("Possible")
    elif b/a==c:
        print("Possible")
    else:
        print("Impossible")
