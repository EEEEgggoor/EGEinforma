# 1) 35


# 2):
from itertools import *


def f(x, y, z, w):
    return (x and not y) or (y == z) or (not w)


for t in product([0, 1], repeat=4):
    table = [(t[0], t[1], 0, 0),
             (1, 0, t[2], 0),
             (1, 0, 1, t[3])]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**(dict(zip(p, r)))) for r in table] == [0, 0, 0]:
                print(p)
# # Ответ - wzyx


# 3) 3570
