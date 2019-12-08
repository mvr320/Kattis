c = int(input())

def flip_row(row):
    if len(row)==1:
        return row
    else:
        return flip_row(row[1:])+flip_row(row[0])

for n in range(c):
    r,c = [int(x) for x in input().split()]
    lines = []
    print('Test {}'.format(n+1))
    for rid in range(r):
        lines.append(input())
    for rid in range(r):
        print(flip_row(lines[r-1-rid]))
        