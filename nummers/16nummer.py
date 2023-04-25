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

def f(n):
    if n < 2025: return n + f(n + 2)
    if n >= 2025: return n


print(f(2022) - f(2023))
