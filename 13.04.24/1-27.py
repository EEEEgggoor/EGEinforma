import string
from itertools import*

#1)14
#2)
#
# def f(x, y, z, w, u):
#     return ((x <= y) and (z == (not w))) <= (u == (x or z))
#
# for a in product([0, 1], repeat = 8):
#     table = [(0, a[0], 0, 0, 0),
#              (0, a[1], a[2], 0, a[3]),
#              (a[4], 0, 0, 0, a[5]),
#              (a[5], 0, a[6], a[7], 0)]
#     if len(table)==len(set(table)):
#         for x in permutations('xyzwu'):
#             if [f(**dict(zip(x, r))) for r in table] == [0, 0, 0, 0]:
#                 print(x)

#3) ---

#4) ---

#5)
# otr = []
# otv = []
# k=0
# for N in range(1000):
#     k+=1
#     n2 = bin(N)[2:]
#     n2_ = n2 + bin(N%4)[2:]
#     R = int(n2_, 2)
#     otr.append(R)
#     if k==49:
#         otv.append(otr)
#         otr = []
#         k=0
# print(len(max(otv)))

#6) 69

#7) ---

#8)
# k=0
# for i in product('012345678', repeat=11):
#     s = "".join(i)
#     if ('0' not in s) and \
#             s.count('1')<=4 and\
#             s.count('2')<=4 and\
#             s.count('3')<=4 and\
#             s.count('4')<=4 and\
#             s.count('5')<=4 and\
#             s.count('6')<=4 and\
#             s.count('7')<=4 and\
#             s.count('8')<=4:
#         s = s.replace('1', '!')
#         s = s.replace('3', '!')
#         s = s.replace('5', '!')
#         s = s.replace('7', '!')
#         s = s.replace('2', '@')
#         s = s.replace('4', '@')
#         s = s.replace('6', '@')
#         s = s.replace('8', '@')
#         if "!!" not in s and "@@" not in s:
#             k+=1
# print(k)

#9) 941

#10) 2201

#11) ---

#12)
# sp = []
# for x in range(50):
#     for y in range(50):
#         for z in range(50):
#             s = '0' + x*'1' + y*'2' + z*'3' +'0'
#             while '00' not in s:
#                 s = s.replace('01','220',1)
#                 s = s.replace('02','1013', 1)
#                 s = s.replace('03','120', 1)
#             if s.count('1')==13 and s.count('2')==18:
#                 sp.append(x+y+z+2)
# print(min(sp))

#13)---
# for x in range(10):
#     for y in range(10):
#         t = int('57' + str(x) + '692' + str(y) + '19', 40)
#         T = int(str(x) + str(y), 40)
#         if t%39 and type(T**0.5)==int:
#             print(T)

#15)
# def f(x, a):
#     return ((x&57>0) or (x&99>0))<=(x&a>0)
#
# for a in range(1000):
#     if all(f(x, a)==1 for x in range(1000)):
#         print(a)
#         break

#16)
print(2*10**9//2)
