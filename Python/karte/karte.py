line = input()
seen = set()
count = {'P':13, 'K':13, 'H':13, 'T':13}
for i in range(len(line)//3):
    card = line[i*3:(i+1)*3]
    suit = card[0]
    if card in seen:
        print('GRESKA')
        exit()
    seen.add(card)
    count[suit] -= 1
print(' '.join(str(count[i]) for i in ['P', 'K', 'H', 'T']))