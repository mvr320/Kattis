import sys

data = sys.stdin.readlines()[1:]

for line in data:
    letters = set(list(line.lower()))
    not_list = []
    for i in range(26):
        if chr(i+97) not in letters:
            not_list.append(chr(i+97))
    if len(not_list)==0:
        print("pangram")
    else:
        print("missing {}".format(''.join(sorted(not_list))))
