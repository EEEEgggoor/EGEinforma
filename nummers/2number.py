from itertools import *


# def f(x, y, z, w):
#     return ((z == (not y)) and (not (x) or y) and w)
#
#
# for a in product([0, 1], repeat=6):
#     table = [(1, a[0], a[1], 0),
#              (0, 0, a[2], 1),
#              (a[3], a[4], a[5], 1)]
#     if len(table)==len(set(table)):
#         for x in permutations('xyzw'):
#             if [f(**dict(zip(x, r))) for r in table]==[1, 1, 1]:
#                 print(x)

# 6365
# def f1(x, y, z, w):
#     return (w <= z) == (y <= x)
#
#
# def f2(x, y, z, w):
#     return (w <= z) and (not (x) == y)
#
#
# for a in product([0, 1], repeat=3):
#     table = [(a[0], 0, 0, 0),
#              (a[1], 0, 1, 1),
#              (0, 0, a[2], 0)]
#     if len(table) == len(set(table)):
#         for x in permutations('xyzw'):
#             if ([f1(**dict(zip(x, r))) for r in table][0] == 0 and [f2(**dict(zip(x, r))) for r in table][1] == 0 and
#                     [f1(**dict(zip(x, r))) for r in table][2] == 0 and [f2(**dict(zip(x, r))) for r in table][2] == 1):
#                 print(x)

