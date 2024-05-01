from itertools import *


# 2)
# def f3(x, y, z, w):
#     return (y <= z) and not ((y or w) <= (z and x))
#
# for a in product([0, 1], repeat=5):
#     table = [(1, 1, a[0], 1),
#              (a[1], 1, 1, a[2]),
#              (1, 1, a[3], a[4])]
#     if len(table)==len(set(table)):
#         for x in permutations('xyzw'):
#             if [f3(**dict(zip(x, r))) for r in table] == [1, 1, 1]:
#                 print(x)


# 3)
# for N in range(1, 1000):
#     n2 = bin(N)[2:]
#
#     sm = n2.count('1')
#     N2 = n2 + str(sm%2)
#
#     sm = N2.count('1')
#     NN2 = N2 + str(sm % 2)
#     R = int(NN2,2)
#     if R>170:
#         print(N)
#         break

# 7)
# k=[]
# for i in permutations('полина', r=6):
#     s = s = ''.join(i)
#     s = s.replace('п', '*')
#     s = s.replace('л', '*')
#     s = s.replace('н', '*')
#
#     s = s.replace('о', '/')
#     s = s.replace('и', '/')
#     s = s.replace('а', '/')
#     if ('**' not in s) and ('//' not in s):
#         k.append(s)
# print(len(k))


# 12)
# for i in range(100):
#     s = '0' + ('1' * i) + ('2' * i) + '0'
#     while '00' not in s:
#         s = s.replace('011', '20', 1)
#         s = s.replace('022', '10', 1)
#         s = s.replace('01', '220', 1)
#         s = s.replace('02', '110', 1)
#         if s.count('1')==47 and s.count('2')<70:
#             print(s.count('2'))


# 14)
# for x in '0123456789ABCDE':
#     p = int('97968' + x + '15', 15) + int('7' + x + '233', 15)
#     if p%14==0:
#         print(x)
#         break


# 15)
# def f3(m, n, a):
#     return (2 * m + 3 * n > 40) or ((m < a) and (n <= a))
#
#
# for a in range(100):
#     if all(f3(m, n, a) == 1 for m in range(1000) for n in range(1000)):
#         print(a)
#         break


# 16)
# def f3(x):
#     if x == 1 or x == 2: return 1
#     if x > 2: return f3(x - 2) * (x - 1)
# print(f3(8))


#17)
# f3 = [int(x) for x in open('17.txt')]
# mn=[]
# for i in range(len(f3)-1):
#     for j in range(i, len(f3)):
#         if (f3[i]+f3[j])%2!=0 and (f3[i]*f3[j])%5==0:
#             mn.append(f3[i]+f3[j])
# print(len(mn), max(mn))


#19-21)
# def f3(s, m):
#     if s>=39: return m%2==0
#     if m==0: return 0
#     h = [f3(s+1, m-1), f3(s+2, m-1), f3(s*2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
# print('19)', [s for s in range(1, 39) if f3(s, 2)])
# print('20)', [s for s in range(1, 39) if not f3(s, 1) and f3(s, 3)])
# print('21)', [s for s in range(1, 39) if f3(s, 4) and not f3(s, 2)])


#23)
# def f3(s, e):
#     if s>e or s==10 or s==11: return 0
#     if s==e: return 1
#     if s<e: return f3(s+1, e) + f3(s+2, e) + f3(s*3, e)
# print(f3(1, 8)*f3(8, 27))


#24)
from string import *
str26 = '0123456789' + ascii_lowercase
str26 = (str26[:26])
s26 = [str(i) for i in str26]

f = open('24_59849.txt').readline()
mx=0
cnt=0
for i in range(len(f)):
    if f[i] in s26:
        cnt += 1
        mx = max(cnt, mx)
    else:
        cnt = 0
mx = max(cnt, mx)
print(mx)




#25)
# from fnmatch import fnmatch
# for i in range(0, 10**8, 317):
#     if fnmatch(str(i), '12??1*56'):
#         print(i)