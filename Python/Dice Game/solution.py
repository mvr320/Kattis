import sys
data = sys.stdin.readlines()
ga1,gb1,ga2,gb2 = [int(x) for x in data[0].split(" ")]
ea1,eb1,ea2,eb2 = [int(x) for x in data[1].split(" ")]

if ((ga1+gb1)/2+(ga2+gb2)/2)>((ea1+eb1)/2+(ea2+eb2)/2):
    print("Gunnar")
else:
    if ((ga1+gb1)/2+(ga2+gb2)/2)<((ea1+eb1)/2+(ea2+eb2)/2):
        print("Emma")
    else:
        print("Tie")
