import sys
data = sys.stdin.readlines()
iter = int(data[0])
line = data[1].strip("\n").split(" ")
for i in range(1,iter+1):
    if "mumble" not in line[i-1]:
        if int(line[i-1]) != i:
            print("something is fishy")
            exit()
print("makes sense")
