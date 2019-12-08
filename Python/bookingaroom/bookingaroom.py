r,n = [int(x) for x in input().split()]
if r==n:
    print('too late')
    exit()
possible_rooms = set(range(1,r+1))
for i in range(n):
    nmb = int(input())
    possible_rooms.remove(nmb)
print(list(possible_rooms)[0])
