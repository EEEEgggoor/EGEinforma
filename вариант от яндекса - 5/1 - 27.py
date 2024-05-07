from itertools import *
# 1) - 39

# 2)
# def f(x, y, w):
#     return (x and ( w<=y))==1
#
# for a in product([0, 1], repeat = 16):
#     table = [(a[0], 0, a[1]),
#              (a[2], a[3], 0),
#              (a[4], 0, a[5]),
#              (a[6], 0, a[7]),
#              (a[8], 0, a[9]),
#              (a[10], 1, a[11]),
#              (a[12], a[13], 1),
#              (a[14], 1, a[15])]
#     if len(table)==len(set(table)):
#         for x in permutations('xyw'):
#             if [f(**dict(zip(x, t))) for t in table] == [0, 0, 0, 0, 0, 1, 1, 1]:
#                 print(x)

# 3) - 887

# 4) - 24

for N in range(1000, 10000):
    if str(N).count('0')==0:
        n = (list(map(int, [str(x) for x in str(N)])))
        T = sum(n)
        r = [(T%x) for x in n]
        R = list(map(str, sorted(r, reverse=True)))
        R = int("".join(R))
        if R>2000:
            print(N)
            break
