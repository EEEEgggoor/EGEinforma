# def f(x, y, z):
#     return ((x == z) or (( x<= (y and z))))  #<<<логическое выражение из задания
#
# print('x y z')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             if f(x, y, z) == 0:
#                 print(x, y, z)


# def f(x, y, z, w):
#     return ((z and y) or ((x <= z) == (y <= w)))  #<<<логическое выражение из задания
#
# print('x y z w')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if f(x, y, z, w) == 0:
#                     print(x, y, z, w)


# def f(x, y, z, w):
#     return w or (x <= y) and (not z <= x)
#
#
# print('x y z w')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if f(x, y, z, w) == 0:
#                     print(x, y, z, w)


# 6691
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


