stri = input()
counts = sorted([stri.count(i) for i in set(stri) if stri.count(i)%2==1])[:-1]
print(len(counts))