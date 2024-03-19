# 22 - polyakov
# def f(x, a):
#     return (x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0))
#
#
# asp = []
# for a in range(0, 1000):
#     if all(f(x, a)==1 for x in range(0, 1000)):
#         print(a)


# №370
# def f(x, a):
#     return (x%a!=0) <= ((x%6==0) <= (x%4!=0))
#
#
# asp = []
# for a in range(1, 1000):
#     if all(f(x, a)==1 for x in range(1, 1000)):
#         print(a)


# №7267
# def f(x, y, a):
#     return (4*x + y > 115) or (x > 3*y) or (x + 4*y < a)
#
#
#
# for a in range(0, 1000):
#     if any(f(x, y, a)==0 for x in range(0, 1000) for y in range(0, 1000)):
#         print(a)


# №6222
# def f(x, y, a):
#     return not((x+y-73)>0) or not(37-(x-y)>0) or (y-a>0)
#
# for a in range(1000):
#     if all(f(x, y, a)==1 for x in range(1000) for y in range(1000)):
#         print(a)


# №5921
# def f(x, a):
#     return (x + a >= 160) or ((x%7==0) <= (not(x + (-17)>0)))
#
#
# for a in range(1000):
#     if all(f(x, a) for x in range(1000)):
#         print(a)

# №5920

# def f(x, y, z, a):
#     return ((z%115==0) or (y%78==0) or (x%51==0)) <= (x*y*z%a==0)
#
# for a in range(1, 500):
#     if all(f(x, y, z, a) for x in range(1, 500) for y in range(1, 500) for z in range(1, 500)):
#         print(a)

# kompege - 7005
# def f(a, x):
#     return ((37+a+(x+45)==180) == (a+x+90==180)) and not(a+23<120)
#
# for a in range(1, 180):
#     if all(f(a, x)==1 for x in range(1, 181)):
#         print(a)


# kompege - 5905
# def f(x, y, z, a):
#     return (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x*y*z > (a//8))
#
#
# for a in range(1, 100):
#     if all(f(x, y, z, a)==1 for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):
#         print(a)


# def treug(a, b, c):
#     return max(a, b, c) <= (a+b+c-max(a, b, c))
#
# def f(x, a):
#     return treug(a, 5, x) <= ((max(x, 11) <= 19) == (not treug(23, 13, x)))
#
#
# for a in range(1, 1000):
#     if all(f(x, a) for x in range(1, 1000)):
#         print(a)


# 4881
# a = set()
# p = {1, 12}
# q = {12, 13, 14, 15, 16}
# def f(x):
#     return (not (x in a)) <= (not (x in p) and not (x in q))
#
# for x in range(-1000, 1000):
#     if f(x) == 0:
#         a.add(x)
# print(a)


# 3434
# A = {x for x in range(1, 1000)}
# P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# Q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
#
#
# def f(x):
#     return ((x in A) <= (x in P)) or (not (x in Q) <= (not (x in A)))
#
#
# for x in range(1, 1000):
#     if f(x) == 0:
#         A.remove(x)
# print(A, len(A))


# kompege2081
# from itertools import*
#
# b = ["".join(i) for i in product('01', repeat=8)]
# a = set()
# p = {i for i in b if i[:2]=='11'}
# q = {i for i in b if i[-1]=='0'}
#
# def f(x):
#     return (not (x in a)) <= ((x in p) or not(x in q))
# for i in b:
#     if f(i)==0:
#         a.add(i)
# print(len(a))


# kompege4284
# P = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Q = {2, 4, 8, 10}
# A = set()
# from itertools import *
# k=0
#
# def f(x):
#     return ((x in Q) <= (x in A)) and ((x in A) <= (x in P))
#
# for i in range(1, 11):
#     for A in combinations(P, i):
#         if all(f(x) for x in P):
#             k+=1
# print(k)


# kompege1072
# P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
# Q = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31}
# A= {i for i in range(1, 1000)}
#
# def f(x):
#     return ((x in A) <= (x in P)) and ((x in Q) <= (x not in A))
#
# for x in range(1, 1000):
#     if f(x)==0:
#         A.remove(x)
# print(len(A))


# kompege12924
# P = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
# A= {i for i in range(1, 1000)}
#
# def f(x):
#     return ((x in A) <= (x in P)) and (not(x in Q) <= (not(x in A)))
#
# for x in range(1, 1000):
#     if f(x)==0:
#         A.remove(x)
# print(len(A))


# kompege4283
# P = {1,3,4,9,11,13,15,17,19,21}
# Q = {3,6,9,12,15,18,21,24,27,30}
# A = set()
#
# def f(x):
#     return ((x in P) <= (x in A)) or ((x not in A) <= ((x not in Q)))
#
# for x in range(-1000, 1000):
#     if f(x)==0:
#         A.add(x)
#
# print(A, 9*3*21*15)


# from itertools import *
# def f(x):
#     P = 25 <= x <= 50
#     Q = 54 <= x <= 75
#     A = a1 <= x <= a2
#     return Q <= ((P==Q) or ((not P) <= A))
#
# Ox = [i/10 for i in range(24*10, 76*10)]
# ans = []
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) == 1 for x in Ox):
#         ans.append(a2-a1)
# print(min(ans), Ox)


# from itertools import *
# def f(x):
#     P = 1 <= x <= 98
#     Q = 25 <= x <= 42
#     A = a1 <= x <= a2
#     return Q <= (((not P) and Q) <= A)
#
# Ox = [i/10 for i in range(0*10, 99*10)]
# ans = []
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) == 1 for x in Ox):
#         ans.append(a2-a1)
# print(min(ans))



# def f(x, a):
#     P = 5 <= x <= 54
#     Q = 50 <= x <= 93
#     return ((not P) and Q) <= (x>a)
#
# ans = []
# for a in range(500):
#     k=0
#     for x in range(500):
#         if (f(x, a) == 0):
#             k+=1
#     if k==20:
#         ans.append(a)
# print(min(ans))


def f(x, a):
    Q = 29 <= x <= 47

    return ((x%3!=0) and (x not in {48, 52, 56})) <= ((abs(x-50) <= 7) <= (Q)) or (x & a == 0)

ans = []
for a in range(1, 500):
    if all(f(x, a)==1 for x in range(500)):
        ans.append(a)
print(min(ans))
