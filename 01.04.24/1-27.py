#2)
from itertools import *
# def f(x, y, z, w):
#     return (x and not y) or (x == z) or not w
#
#
# for a in product([0, 1], repeat=4):
#     table = [(0, 1, 1, 0),
#              (0, a[0], a[1], a[2]),
#              (a[3], 1, 0, 1)]
#     if len(table) == len(set(table)):
#         for x in permutations('xyzw'):
#             if [f(**dict(zip(x, r))) for r in table] == [0, 0, 0]:
#                 print(x)


# for x in range(100, 1000):
#     xstr = str(x)
#     pervtor = int(xstr[0]) + int(xstr[1])
#     vtortret = int(xstr[1]) + int(xstr[2])
#     R = str(max(pervtor, vtortret)) + str(min(pervtor, vtortret))
#     if R=='1412':
#         print(x)
#         break

#8)
# sp = [0]
# for i in product('KOP',repeat=5):
#     s = "".join(i)
#     sp.append(s)
# print(sp[238])


#12)
# s = '1' + '8'*80
# while '18' in s or '288' in s or '3888' in s:
#     if '18' in s:
#         s = s.replace('18', '2', 1)
#     elif '288' in s:
#         s = s.replace('288', '3', 1)
#     else:
#         s = s.replace('3888', '1', 1)
# print(s)


#14)
# s = 4**2016 + 2**2015 - 7
# print(bin(s)[2:].count('1'))


#15)
# def f(x, a):
#     return (70%a==0) and ((x%28==0) <= ((x%2!=0) <= (x%21!=0)))
#
#
# for a in range(1, 1000):
#     if all(f(x, a)==1 for x in range(1, 1000)):
#         print(a)


#16)
# def f(x):
#     if x>=2025: return x
#     if x<2025: return x + 3 + f(x+3)
# print(f(23) - f(21))


#17)
# f = [int(x) for x in open('17.txt')]
# sp = []
# for i in range(len(f)-1):
#     for j in range(i+1, len(f)):
#         if (f[i]+f[j])%8==0:
#             sp.append((f[i]+f[j]))
# print(len(sp), max(sp))


#23)
# def f(s, m):
#     if s>=43: return m%2==0
#     if m==0: return 0
#     h = [f(s+1, m-1), f(s+2, m-1), f(s*2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
# print([s for s in range(1, 43) if f(s, 2)])
# print([s for s in range(1, 43) if f(s, 3) and not f(s, 1)])
# print([s for s in range(1, 43) if f(s, 4) and not f(s, 2)])


#23)
# def f(s, e):
#     if s>e or s==6: return 0
#     if s==e: return 1
#     if s<e: return f(s+1, e) + f(s+2, e) + f(s*2, e)
# print(f(4, 15) + f(15, 19))


#24)
# f = open('24.txt').readline()
# k=0
# sp=[]
# mx = -100
# for i in range(len(f)-1):
#     if f[i]=='Y':
#         k+=1
#     for j in range(i+1, len(f)):
#         if f[j]=='Y':
#             k+=1
#         if k>100:
#             k=0
#             sp.append(j-i)
#             break
# print(max(sp))


#26)
# f = [int(x) for x in open('26.txt')]
# sp = []
# for i in range(len(f)-1):
#     for j in range(i+1, len(f)):
#         if ((f[i]%2==0 and f[j]%2!=0) or (f[i]%2!=0 and f[j]%2==0)) and (f[i]+f[j]) in f:
#             sp.append((f[i]+f[j]))
# print(len(f), max(sp))


#27A)
# f = [list(map(int, x.split())) for x in open('27a.txt')]
# n = f[0]
# f = f[1:]
# sp=[]
# for i in range(20):
#     for j in range(20):
#         if (f[i][0]+f[j][0])%3==0:
#             sp.append(f[i][0]+f[j][0])
#
#         if (f[i][0]+f[j][1])%3==0:
#             sp.append(f[i][0] + f[j][1])
#
#         if (f[i][1]+f[j][0])%3==0:
#             sp.append(f[i][1] + f[j][0])
#
#         if (f[i][1]+f[j][1])%3==0:
#             sp.append(f[i][1] + f[j][1])
# print(max(sp))


#25)
# def div(n):
#     d = set()
#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             d.add(i)
#             d.add(n//i)
#     return sorted(d)
#
# sp = [0]
# for i in range(2422000, 2422081):
#     if len(div(i))==2:
#         sp.append(i)
# print(sp)