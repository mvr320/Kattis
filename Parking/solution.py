import sys
data = sys.stdin.readlines()
for i in range(2,len(data),2):
    int_list = sorted([int(x) for x in data[i].split(" ")])
    dst = 0
    for x in range(1,len(int_list)):
        dst += abs(int_list[x]-int_list[x-1])
    print(dst+abs(int_list[0]-int_list[-1]))
    #avg1 = int(sum(int_list)/len(int_list)+0.5)
    #sol_list = [abs(x-avg1) for x in int_list]
    #print(sum(sol_list))
