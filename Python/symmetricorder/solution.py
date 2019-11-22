import sys
data = sys.stdin.readlines()
processed=0
cnt = 1
while(processed != len(data)-1):
    print("SET {}".format(cnt))
    backward = []
    for lid in range(int(data[processed])):
        if lid%2==0:
            print(data[processed+1+lid].strip('\n'))
        else:
            backward.append(data[processed+1+lid].strip('\n'))
    backward.reverse()
    for string in backward:
        print(string)
    #for lid in range(int(data[processed])-2,0,-2):
    #    print(data[processed+1+lid].strip('\n'))
    processed +=(int(data[processed])+1)
    cnt += 1

