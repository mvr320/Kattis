import sys
data = sys.stdin.readlines()[1:]

for place in data:
    storage = []
    que = []
    done = set()
    highest = 1
    for i in range(8):
        new_row = []
        for j in range(8):
            new_row.append(0)
        storage.append(new_row)
    col = ord(list(place)[0])-97
    row = int(list(place)[1])-1
    que.append( (col,row,0) )
    highest_val = 0
    highest_lst = []
    while len(que)!=0:
        col,row,it = que[0]
        if col>=0 and row>=0 and col<8 and row<8 and (col,row) not in done:
            #print(col, row, it)
            if highest_val<it:
                highest_val=it
                highest_lst = []
            if highest_val==it:
                highest_lst.append( chr(col+97)+str(row+1) )
            que.append( (col-2, row-1, it+1) )
            que.append( (col-2, row+1, it+1) )
            que.append( (col+2, row-1, it+1) )
            que.append( (col+2, row+1, it+1) )
            que.append( (col-1, row-2, it+1) )
            que.append( (col-1, row+2, it+1) )
            que.append( (col+1, row-2, it+1) )
            que.append( (col+1, row+2, it+1) )
            done.add( (col,row) )
        que = que[1:]
    print("{} {}".format(highest_val, ' '.join( sorted(sorted(highest_lst, key=lambda x: x[0], reverse=False), key=lambda x: x[1], reverse=True) )))