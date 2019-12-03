import sys
import math

data = [x.strip('\n') for x in sys.stdin.readlines()[1:]]
store = {}
for i in range(91-65):
    store[chr(i+65)] = [i,i+28]
    #print(chr(i+65))
store[' ']=[26,26+28]
store['\'']=[27,27+28]
const = (60.0*math.pi)/28.0

dist = 0
end_sum = 0.0
for line in data:
    start = store[list(line)[0]][0]
    for char in list(line)[1:]:
        # Pickup of letter
        dist += min( abs(store[char][0]-start), abs(store[char][1]-start))
        start = store[char][0]
    end_sum += float(len(line))
    end_sum += float(dist)*60.0/(28.0*15.0)*math.pi
    print(end_sum)