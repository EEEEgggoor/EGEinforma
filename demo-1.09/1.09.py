# 1) 35


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


# 3) 3570


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

# Ответ - 163


# 6) Ответ: 275


# 7) Ответ: 288


# 8)Ответ: 180


# 12)

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


#14)
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


#15)
# def f(x, y, a):
#     return (x+2*y<a) or (y>x) or (x>60)
#
#
# for a in range(0, 1001):
#     if all(f(x, y, a)==1 for x in range(1000) for y in range(1000)):
#         print(a)
#         break


#Ответ-181


#16)
# def f(n):
#     if n>2024: return n
#     if n<=2024: return n*f(n+1)
#
# print(f(2022)/f(2024))
#
# Ответ - 4090506


#17)
ans = []
l = [int(i) for i in open('17.txt')]
mx = 0
for y in range(len(l)):
    if l[y]%100==13:
        mx = max(l[y], mx)
print(mx)



for x in range(len(l)-2):
    if :
        ans.append(sum(len(x), len(x+1), len(x+2)))
print(max(ans), len(ans))