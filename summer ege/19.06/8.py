alf = 'абвгд'
k = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    if x1 != 'а' and (x1 != x2 and x2 != x3 and x3 != x4 and x4 != x5):
                        k += 1
print(k)
