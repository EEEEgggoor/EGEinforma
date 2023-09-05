# 1) 35


# 2):
# from itertools import *
#
#
# def f(x, y, z, w):
#     return (x and not y) or (y == z) or (not w)
#
#
# for t in product([0, 1], repeat=4):
#     table = [(t[0], t[1], 0, 0),
#              (1, 0, t[2], 0),
#              (1, 0, 1, t[3])]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**(dict(zip(p, r)))) for r in table] == [0, 0, 0]:
#                 print(p)
# # Ответ - wzyx


# 3) 3570


# 5)
# s=[]
# for N in range(1, 1000):
#     b = bin(N)[2:]
#     if N % 3 == 0:
#         b = b + b[-3:]
#     else:
#         b = b + (bin(3 * (N % 3))[2:])
#     R = int(b, 2)
#     if R>151:
#         s.append(R)
# print(min(s))

# Ответ - 163


# 6) Ответ: 275


# 7) Ответ: 288


# 8)Ответ: 180
