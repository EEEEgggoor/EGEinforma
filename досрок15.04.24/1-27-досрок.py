#5)
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
import string
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
# alf = ('0123456789' + string.ascii_lowercase)[:27]
# for x in alf:
#     t = int(f'123{x}24', 27) + int(f'135{x}78', 27)
#     if t%26==0:
#         print(x, t/26)


#16)
# from sys import setrecursionlimit
# setrecursionlimit(10000)
# def f(n):
#     if n<=7: return 1
#     else: return n+2+f(n-1)
# print(f(2024)-f(2020))


#24)
f = "".join([x for x in open('24_15339.txt')])
f = f.replace('6', '*').replace('7', '*').replace('8', '*').replace('9', '*').replace('A', '!').replace('B', '!').replace('C', '!')
k=mx=0
for x in range(len(f)-1):
    if f[x]!=f[x+1]:
        k+=1
        mx = max(mx, k)
    else:
        k=1
print(mx)