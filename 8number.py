alf = 'ABCX'
alf1 = 'ABC'
k=0
for x1 in alf1:
    for x2 in alf1:
        for x3 in alf1:
            for x4 in alf1:
                for x5 in alf:
                    k += 1
                    print(x1+x2+x3+x4+x5)
print(k)