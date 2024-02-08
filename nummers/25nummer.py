# from fnmatch import *
#
# for i in range(0, 10 ** 10, 73):
#     if fnmatch(str(i), '12345*76'):
#         print(i, i // 73)

def delt(n):
    s = set()
    for i in range(1, int(n**0.5) + 1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return sorted(s)


# 59818
from fnmatch import*
for i in range(0, 10**9, 2031):
    if fnmatch(str(i), '*31*65?') and len(delt(i)) in [int(2**x) for x in range(0, 20)] and i%31==0:
        print(i, i//2031)


