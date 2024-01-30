'''alf = 'ABCX'
alf1 = 'ABC'
k=0
for x1 in alf1:
    for x2 in alf1:
        for x3 in alf1:
            for x4 in alf1:
                for x5 in alf:
                    k += 1
                    print(x1+x2+x3+x4+x5)
print(k)'''

# alf = 'abx'
# k=0
# for x1 in alf:
#     for x2 in alf:
#         for x3 in alf:
#             for x4 in alf:
#                 for x5 in alf:
#                     for x6 in alf:
#                         X = x1+x2+x3+x4+x5+x6
#                         if X.count('x')==1:
#                             k+=1
# print(k)


alf = 'авелрфь'
k = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        k += 1
                        sl = x1 + x2 + x3 + x4 + x5 + x6
                        if ('а' not in sl) and ('е' not in sl):  # <<< в слове нету ни одной гласной
                            print(k, sl)
