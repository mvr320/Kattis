import sys
data = sys.stdin.readlines()
c = 0
st=0
while "0" not in data[c]:
    if st!=0:
        print("")
    loop = int(data[c])
    lista = []
    listb = []
    listp = [0 for i in range(loop)]
    for i in range(loop):
        lista.append(int(data[c+1+i]))
        listb.append(int(data[c+1+i+loop]))
    slista = sorted(lista)
    slistb = sorted(listb)
    for i in range(loop):
        id = lista.index(slista[i])
        listp[id] = slistb[i]
    for i in listp:
        print(i)
    c += 2*loop+1
    st=1
