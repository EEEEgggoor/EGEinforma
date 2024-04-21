from itertools import*
#1) 110


#2)
# def f(x, y, z, w):
#     return (x and (not z)) or (y==z) or (not(w))
#
# for a in product([0, 1], repeat = 4):
#     table = [(a[0], a[1], 0, 0),
#              (1, 0, a[3], 0),
#              (1, 0, 1, a[3])]
#     if len(table)==len(set(table)):
#         for x in permutations('xyzw'):
#             if [f(**dict(zip(x, r))) for r in table] == [0, 0, 0]:
#                 print(x)

#3) - 3825
#4) - 001

#5)
# for N in range(1000):
#     n2 = bin(N)[2:]
#     if N%2==0:
#         n2 += '01'
#     else: n2 = '1'+n2+'1'
#     R = int(n2, 2)
#     if R>156:
#         print(N)
#         break


#6)
# from turtle import*
# left(90)
# k = 15
# speed(30)
# for i in range(2):
#     forward(k*13)
#     right(90)
#     forward(18*k)
#     right(90)
# up()
# forward(5*k)
# right(90)
# forward(9*k)
# left(90)
# down()
# for i in range(2):
#     forward(11*k)
#     right(90)
#     forward(7*k)
#     right(90)
# up()
# for x in range(-1*k, 20*k, k):
#     for y in range(-5*k, 20*k, k):
#         goto(x, y)
#         dot(3, 'red')
# done()

#7) - 520

#8)
# k=0
# for i in product('апрсу', repeat=5):
#     k+=1
#     s = ''.join(i)
#     if 'аа' not in s and s.count('у') <= 1:
#         print(k, s)
#         break

#9) - 133
#10) - 734
#11) - 198

#12)
# s = '8'*45
# while '1111' in s or '8888' in s:
#     if '1111' in s: s = s.replace('1111', '88', 1)
#     else: s = s.replace('8888', '11', 1)
# print(s)

#13)
# from ipaddress import *
# k=0
# net = ip_network('105.224.200.224/255.255.255.224', 0)
# for ip in net:
#     i = list(map(int, str(ip).split('.')))
#     i2 = [bin(x)[2:] for x in i]
#     ip2 = ''.join(i2)
#     if ip2.count('1')%4==0:
#         k+=1
# print(k)


#14)
# s = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029
# k=0
# while s!=0:
#     if s%27>9:
#         k+=1
#     s //= 27
# print(k)

# from string import *
# alf = ('0123456789' + ascii_lowercase)[:27]
# for x in alf:
#     t = int(f'123{x}24', 27) + int(f'135{x}78', 27)
#     if t%26==0:
#         print(x, t/26)


#15)
# def f(x, a):
#     return (x%a!=0) <= ((x%28==0) <= (x%49!=0))
#
# for a in range(1, 1000):
#     if all(f(x, a)==1 for x in range(1, 1000)):
#         print(a)

#16)
# from sys import setrecursionlimit
# setrecursionlimit(10000)
# def f(n):
#     if n<=7: return 1
#     else: return n+2+f(n-1)
# print(f(2024)-f(2020))


#17)
# f = [int(x) for x in open('17.txt')]
# mx = []
# for i in range(len(f)):
#     if i%19==0:
#         mx.append(i)
# mx = max(mx)
#
# otv = []
# for i in range(len(f)-1):
#     if (f[i]>mx or f[i+1]>mx):
#         otv.append(f[i] + f[i+1])
# print(len(otv), max(otv))


#19-21)
# def f(s1, s2, m):
#     if s1+s2>=123: return m%2==0
#     if m==0: return 0
#     h = [f(s1+1, s2, m-1), f(s1*2, s2, m-1),
#          f(s1, s2+1, m-1), f(s1, s2*2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
# print('19)', [x for x in range(1, 110) if f(13, x, 2)])
# print('20)', [x for x in range(1, 110) if f(13, x, 3) and not f(13, x, 1)])
# print('21)', [x for x in range(1, 110) if not f(13, x, 2) and f(13, x, 4)])

#22) - 8

#23)
# def f(n, e):
#     if n>e: return 0
#     if n==e: return 1
#     if n<e: return f(n+1, e) + f(n*2, e)
# print(f(4, 8)*f(8, 10)*f(10, 15))

#24)
# f = "".join([x for x in open('24_15339.txt')])
# f = f.replace('6', '*').replace('7', '*').replace('8', '*').replace('9', '*').replace('A', '!').replace('B', '!').replace('C', '!')
# k=mx=0
# for x in range(len(f)-1):
#     if f[x]!=f[x+1]:
#         k+=1
#         mx = max(mx, k)
#     else:
#         k=1
# print(mx)

#25)
# from fnmatch import *
# for i in range(0, 10**10, 2024):
#     if fnmatch(str(i), '1*2322?2'):
#         print(i, i//2024)

#26)
n = int(open('26_15341.txt').readline())
f = [int(x) for x in open('26_15341.txt')][1:]
f = sorted(f, reverse=True)
a = f[0]
sp=[]
for i in range(n-1):
    if a-f[i]>=8:
        a=f[i]
        sp.append(a)
print(len(sp), a)