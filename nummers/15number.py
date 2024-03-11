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


def treug(a, b, c):
    return max(a, b, c) <= (a+b+c-max(a, b, c))

def f(x, a):
    return treug(a, 5, x) <= ((max(x, 11) <= 19) == (not treug(23, 13, x)))


for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)
