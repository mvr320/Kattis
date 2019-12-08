import sys

data = sys.stdin.readlines()
rint_list = [int(i) for i in data]
int_list = sorted(rint_list)
o=sum(int_list)-100
for i in range(len(int_list)):
    for j in range(i+1, len(int_list)):
        #print(i, j, int_list[i], int_list[j], o)
        #if (int_list[i]+int_list[j])>o:
        #    continue
        #else:
        if (int_list[i]+int_list[j])==o:
            #print("Yes!")
            for t in rint_list:
                if t != int_list[i] and t != int_list[j]:
                    print(t)
