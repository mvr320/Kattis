ciphertext = input()
key = input()
d = ord('A')

final = ''
for i in range(len(ciphertext)):
    shifted_numb = ord(ciphertext[i])- (ord(key[i])-d)
    shifted = chr(shifted_numb if shifted_numb>=d else (26+shifted_numb) )
    key += shifted
    final += shifted
print(final)
