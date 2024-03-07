def f(x):
    s = set()
    for i in range(int(1), int(x**0.5)+1):
        if x%i==0:
            s.add(i)
            s.add(x//i)
    return sorted(s)

# k=0
# for x in range(245_690, 245_756):
#     k+=1
#     if len(f(x))==2:
#         print(x, k)

# from fnmatch import *
#
# for i in range(0, 10**9, 23):
#     if fnmatch(str(i), '12345?7?8'):
#         print(i, i//23)
#

for m in range(0, 31, 2):
    for n in range(1, 19, 2):
        if(200000000 <= 2 ** m * 3 ** n <= 400000000):
            print(2 ** m * 3 ** n)