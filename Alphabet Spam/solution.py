import sys
line = sys.stdin.readlines()[0].strip("\n")
wh = 0
lc = 0
uc = 0
sy = 0
for l in line:
    a = ord(l)
    if l=='_':
        #print(l, "wh")
        wh +=1
    else:
        if a<123:
            if a>96:
                #print(l, "lc")
                lc +=1
            else:
                if a>64 and a<91:
                    #print(l, a, "uc")
                    uc +=1
                else:
                    #print(l, "sy")
                    sy +=1
        else:
            #print(l, "sy")
            sy +=1
print("%.17f"%(float(wh)/float(wh+lc+uc+sy)))
print("%.17f"%(float(lc)/float(wh+lc+uc+sy)))
print("%.17f"%(float(uc)/float(wh+lc+uc+sy)))
print("%.17f"%(float(sy)/float(wh+lc+uc+sy)))
