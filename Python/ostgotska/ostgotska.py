line = input()
ost = 0
nst = 0
for word in line.split():
    if 'ae' in word:
        ost += 1
    else:
        nst += 1
print('dae ae ju traeligt va' if ost/(nst+ost)>=0.4 else 'haer talar vi rikssvenska')