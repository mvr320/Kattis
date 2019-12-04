import sys
total = int(input())
line = [int(x) for x in input().split()]
final = ['1']
for number in range(total-1):
    final.append(str(line.index(number)+2))
print(' '.join(final))