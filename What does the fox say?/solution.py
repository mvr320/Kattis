import sys

data = sys.stdin.readlines()
cl = 1
for c in range(int(data[0])):
    fox_list = data[cl].strip("\n").split(" ")
    cl +=1
    while "what does the fox say?" not in data[cl]:
        fox_list = [ sound for sound in fox_list if sound != data[cl].strip("\n").split(" ")[-1]]
        cl += 1
    for soundi in range(len(fox_list)-1):
        print("%s "%fox_list[soundi], end="")
    print(fox_list[len(fox_list)-1])
    cl +=1
