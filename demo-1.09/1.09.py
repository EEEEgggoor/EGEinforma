# 1) 35
#
#
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
#
#
# 3) 3570
#
#
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
#
# Ответ - 163
#
#
# 6) Ответ: 275
#
#
# 7) Ответ: 288
#
#
# 8)Ответ: 180
#
#
# 12)
#
# for n in range(4, 10000):
#     s = '5' + n * '2'
#     while '52' in s or '2222' in s or '1122' in s:
#         if '52' in s:
#             s = s.replace('52', '11', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
#         if '1122' in s:
#             s = s.replace('1122', '25', 1)
#     s1 = (list(map(int, s)))    #преобразование строки в список(каждый эдемент списка - число строки)
#     s1 = sum(s1)
#     if s1==64:
#         print(n)
#
#
# 14)
# for x in '0123456789abcdefghi':
#     a = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
#     if a%18==0:
#         print(a//18)
#
# a = (3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024)
# s=''
# while a!=0:
#     s+=str(a%25)
#     a//=25
# s = s[::-1]
# print(s.count('0'))
# #Ответ - 469034148, 9
#
#
# 15)
# def f(x, y, a):
#     return (x+2*y<a) or (y>x) or (x>60)
#
#
# for a in range(0, 1001):
#     if all(f(x, y, a)==1 for x in range(1000) for y in range(1000)):
#         print(a)
#         break
#
#
# Ответ-181
#
#
# 16)
# def f(n):
#     if n>2024: return n
#     if n<=2024: return n*f(n+1)
#
# print(f(2022)/f(2024))
#
# Ответ - 4090506
#
#
# 17)
# ans = []
# l = [int(i) for i in open('17.txt')]
# mx = 0
# for y in range(len(l)):
#     if l[y] % 100 == 13:
#         mx = max(l[y], mx)
#
# for x in range(len(l) - 2):
#     if (((99 < l[x] < 1000 ) + (99 < l[x+1] < 1000) + (99 < l[x+2] < 1000))==2) and (l[x] + l[x + 1] + l[x + 2])<=mx:
#         ans.append(l[x] + l[x + 1] + l[x + 2])
# print(len(ans), max(ans))
#
#
#
#  18)2167,
#
#
#  19-21)
# def f(s, m):
#     if s>=129: return m%2==0
#     if m==0: return 0
#     h = [f(s+1, m-1), f(s*2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
#
# print('19)', [s for s in range(1, 129) if f(s, 2)])
# print('20)', [s for s in range(1, 129) if f(s, 3) and not f(s, 1)])
# print('21)', [s for s in range(1, 129) if f(s, 4)])
#
#
# 22) 4
#
# 23)
# def F(s, f):
#     if s > f or s==11: return 0
#     if f==s: return 1
#     if s<f: return F(s+1, f) + F(s*2, f) + F(s**2, f)
#
#
# print(F(2, 20))
# Ответ - 37
#
#
# 24)
# f = open('24.txt').readline()
#
# mx=-1
# sp=[]
# for i in range(len(f)):
#     if f[i]=='T':
#         sp.append(i)
#
# for i in range(101, len(sp)):
#     len_ = sp[i] - sp[i-101] - 1
#     mx = max(mx, len_)
#
# print(mx)
#
#
# 25)
# from fnmatch import *
# for i in range(0, 10**10+1, 2024):
#     if fnmatch(str(i),'1?2157*4'):
#         print(i, i//2024)


# 26)
k = 0
s = 0
f = [list(map(int, x.split())) for x in open('26.txt')]
for i in range(1, len(f)):
    for j in range(i, len(f) - 1):
        s1 = []
        if f[i][0] < f[j][1]:
            pass
        if f[i][1] == f[j][0]:
            pass
