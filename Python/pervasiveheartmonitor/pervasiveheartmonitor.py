import sys
for line in sys.stdin.readlines():
    words = line.split()
    name = []
    avg = []
    for word in words:
        try:
            avg.append(float(word))
        except ValueError:
            name.append(word)
    print('{} {}'.format(sum(avg)/len(avg), ' '.join(name)))