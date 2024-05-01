#2)
from itertools import *
# def f3(x, y, z, w):
#     return (x and not y) or (x == z) or not w
#
#
# for a in product([0, 1], repeat=4):
#     table = [(0, 1, 1, 0),
#              (0, a[0], a[1], a[2]),
#              (a[3], 1, 0, 1)]
#     if len(table) == len(set(table)):
#         for x in permutations('xyzw'):
#             if [f3(**dict(zip(x, r))) for r in table] == [0, 0, 0]:
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
# def f3(x, a):
#     return (70%a==0) and ((x%28==0) <= ((x%2!=0) <= (x%21!=0)))
#
#
# for a in range(1, 1000):
#     if all(f3(x, a)==1 for x in range(1, 1000)):
#         print(a)


#16)
# def f3(x):
#     if x>=2025: return x
#     if x<2025: return x + 3 + f3(x+3)
# print(f3(23) - f3(21))


#17)
# f3 = [int(x) for x in open('17.txt')]
# sp = []
# for i in range(len(f3)-1):
#     for j in range(i+1, len(f3)):
#         if (f3[i]+f3[j])%8==0:
#             sp.append((f3[i]+f3[j]))
# print(len(sp), max(sp))


#23)
# def f3(s, m):
#     if s>=43: return m%2==0
#     if m==0: return 0
#     h = [f3(s+1, m-1), f3(s+2, m-1), f3(s*2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
# print([s for s in range(1, 43) if f3(s, 2)])
# print([s for s in range(1, 43) if f3(s, 3) and not f3(s, 1)])
# print([s for s in range(1, 43) if f3(s, 4) and not f3(s, 2)])


#23)
# def f3(s, e):
#     if s>e or s==6: return 0
#     if s==e: return 1
#     if s<e: return f3(s+1, e) + f3(s+2, e) + f3(s*2, e)
# print(f3(4, 15) + f3(15, 19))


#24)
# f3 = open('24.txt').readline()
# k=0
# sp=[]
# mx = -100
# for i in range(len(f3)-1):
#     if f3[i]=='Y':
#         k+=1
#     for j in range(i+1, len(f3)):
#         if f3[j]=='Y':
#             k+=1
#         if k>100:
#             k=0
#             sp.append(j-i)
#             break
# print(max(sp))


#26)
# f3 = [int(x) for x in open('26.txt')]
# sp = []
# for i in range(len(f3)-1):
#     for j in range(i+1, len(f3)):
#         if ((f3[i]%2==0 and f3[j]%2!=0) or (f3[i]%2!=0 and f3[j]%2==0)) and (f3[i]+f3[j]) in f3:
#             sp.append((f3[i]+f3[j]))
# print(len(f3), max(sp))


#27A)
# f3 = [list(map(int, x.split())) for x in open('27a.txt')]
# n = f3[0]
# f3 = f3[1:]
# sp=[]
# for i in range(20):
#     for j in range(20):
#         if (f3[i][0]+f3[j][0])%3==0:
#             sp.append(f3[i][0]+f3[j][0])
#
#         if (f3[i][0]+f3[j][1])%3==0:
#             sp.append(f3[i][0] + f3[j][1])
#
#         if (f3[i][1]+f3[j][0])%3==0:
#             sp.append(f3[i][1] + f3[j][0])
#
#         if (f3[i][1]+f3[j][1])%3==0:
#             sp.append(f3[i][1] + f3[j][1])
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