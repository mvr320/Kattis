import sys
c,string = [x for x in sys.stdin.readlines()[0].split(" ")]
if c=="D":
    for i in range(int( (len(string)-1)/2)):
        print(string[2*i]*int(string[2*i+1]), end="")
else:
    tmp=string[0]
    cnt=0
    for i in range(len(string)):
        if string[i] not in tmp:
            print(tmp, end="")
            print(cnt, end="")
            cnt = 1
            tmp = string[i]
        else:
            cnt +=1
print("")
