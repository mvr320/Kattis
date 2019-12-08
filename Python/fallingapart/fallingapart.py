_ = input()
numbers = sorted( [int(x) for x in input().split()], reverse=True)
print("{} {}".format(sum(numbers[0::2]),sum(numbers[1::2])))