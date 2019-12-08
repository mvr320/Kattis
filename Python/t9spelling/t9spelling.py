'''trans = {' ': '0'}

tmp = [3,3,3,3,3,4,3,4]
cur_dig = 1
for i in range(26):
    t9 = ''
    if i>=sum(tmp[:cur_dig]):
        cur_dig +=1
    for _ in range(i+1-sum(tmp[:cur_dig-1])):
        t9 += str(cur_dig+1)
    #print(chr(ord('a')+i), t9)
    trans[chr(ord('a')+i)] = t9
print(trans)'''
trans = {' ': '0', 'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777', 's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999'}
for i in range(int(input())):
    final = ''
    inp = list(input())
    for ch in inp:
        if len(final)>0:
            if final[-1] == trans[ch][0]:
                final += ' '
        final += trans[ch]
    print('Case #{}: {}'.format(i+1,final))