from functools import lru_cache


# поляков №224
# def f(x):
#     if x==1: return 1
#     if x>1 and x%2==0: return x*x + f(x-1)
#     if x>1 and x%2!=0: return f(x-1) + 2 * f(x-2)
# print(f(23))


# поляков 5537
# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) + 2 * g(n - 1)
#
#
# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) - 2 * g(n - 1)
#
# print(g(21))


# поляков 5537

#
#
# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n > 1: return n * f(n - 1)
#
#
# for n in range(2, 1526):
#     f(n)
#
# print(f(2023) / f(2020))


# компегэ №7618
#
# def f(n):
#     if n < 2025: return n + f(n + 2)
#     if n >= 2025: return n
#
#
# print(f(2022) - f(2023))


# #поляков №3691
# @lru_cache(None)
# def f(n):
#     if n<=1: return 1
#     if n>1 and n%2!=0: return n + f(n+2)
#     if n>1 and n%2==0: return 3 + f(n/2 - 1)
#
#

#поляков №15
# k=[]
# def F(n):
#     if n > 0: return G(n - 1)
# def G(n):
#     k.append("*")
#     if n > 1: return F(n - 3)
# F(11)
# print(len(k))


#поляков №2265
# def f(n):
#     if n<=3: return n
#     if 3<n<=32: return n//4 +f(n-3)
#     if n>32: return 2*f(n-5)
# print(f(100))


#поляков №2278
# k=0
# def f(n):
#     if n>25: return 2*n*n*n + 1
#     if n<=25: return f(n+2) + 2*f(n+3)
# for n in range(1, 1001):
#     if f(n)%11==0:
#         k+=1
# print(k)


#поляков №3691
# def f(n):
#     if n<=1: return 1
#     if n>1 and n%2==0: return 3+f(n/2 - 1)
#     if n>1 and n%2!=0: return n+f(n+2)
# n=2
# while n<1000:
#     try:
#        r = f(n)
#        print(n)
#        if r==19:
#            print(n)
#            break
#     except:
#         pass
#     n+=1

#поляков №6299
def f(a, b):
    if b==0: return a
    if a>=b.0:: return f(a-b, b)
