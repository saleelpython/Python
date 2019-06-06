import random



x = [1, 6, 3, 7, 9, 4, 1, 4, 6, 8]
d = {}
for i in x:
    k = d.keys()
    if i in k:
        d[i] += 1
    else:
        d[i] = 1
print(d)

