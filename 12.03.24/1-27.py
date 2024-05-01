# from itertools import *

# def f3(x, y, z, w):
#     return (((z <= w) or (y == w)) and ((x or z) == y))
#
# for a in product([0, 1], repeat=4):
#     t = [(0, 1, 1, 0),
#          (a[0], 1, 0, a[1]),
#          (0, a[2], a[3], 1)]
#     if len(t)==len(set(t)):
#         for x in permutations('xyzw'):
#             if [f3(**dict(zip(x, r))) for r in t]==[1, 1, 1]:
#                 print("".join(x))


# itog = []
# for x in range(630, 1000):
#     strok = str(x)
#     pervtor = int(strok[0]) * int(strok[1])
#     vtortret = int(strok[1]) * int(strok[2])
#     otvet = str(min(pervtor, vtortret))+str(max(pervtor, vtortret))
#     if otvet=='621':
#         itog.append(x)
# print(max(itog))


# k=0
# for i in product('КОР', repeat=5):
#     k+=1
#     x= ''.join(i)
#     print(k, x)


# otvet = []
# for x in '0123456':
#     for y in '0123456':
#         t = int(y+x+'320', 7) + int('1'+x+'3'+y+'3', 9)
#         if t%181==0:
#             otvet.append(t)
# print(min(otvet)//181)


# def f3(x, y, a):
#     return (y + 2*x < a) or (x > 15) or (y > 30)
# A = []
# for a in range(0, 1000):
#     if all(f3(x, y, a)==1 for x in range(-200, 200) for y in range(-200, 200)):
#         A.append(a)
# print(min(A))


# def f3(x):
#     if x==1 or x==2: return 1
#     if x>2: return f3(x-2)*(x-1)
# print(f3(7))


# f3 = [int(x) for x in open('17.txt')]
# mn = []
# for i in range(len(f3)):
#     if str(f3[i])[-1]=='5':
#         mn.append(f3[i])
# min5 = min(mn)
# otvet=[]
# for i in range(len(f3) - 1):
#     if ((len(str(f3[i])) == 3 and len(str(f3[i + 1])) != 3) or (len(str(f3[i])) != 3 and len(str(f3[i + 1])) == 3)) \
#             and (f3[i]+f3[i+1])%min5==0:
#         otvet.append(f3[i] + f3[i+1])
# print(len(otvet), min(otvet))


# def f3(s, m):
#     if s>=27: return m%2==0
#     if m==0: return 0
#     h = [f3(s+1, m-1), f3(s+2, m-1), f3(s*2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
# print('19', [s for s in range(1, 27) if f3(s, 2)])
# print('20', [s for s in range(1, 27) if f3(s, 3) and not f3(s, 1)])
# print('20', [s for s in range(1, 27) if f3(s, 4) and not f3(s, 2)])


# def f3(s, e):
#     if s>e: return 0
#     if s==e: return 1
#     if s<e: return f3(s+1, e) + f3(s+3, e) + f3(s + (s-1), e)
# print(f3(2, 10))


# f3 = open("24.txt").readline()
# k=0
# mx=-1000
# for i in range(len(f3)-1):
#     if f3[i]==f3[i+1]=='Y':
#         k+=1
#         mx = max(mx, k)
#     else:
#         k=1
#         mx = max(mx, k)
# print(mx)


# from fnmatch import*
#
# for i in range(0, 10**10, 2024):
#     if fnmatch(str(i), "3?6906*4"):
#         print(i)


# F = open('26.txt')
# n = F.readline()[:4]
# f3 = sorted([int(x) for x in F])
# sm = 0
# sp = []
# for x in range(len(f3)):
#     if sm<int(n):
#         sp.append(f3[x])
#         sm+=f3[x]
#     else:
#         break
#
# sp2 = sp[:-1]
# for x in range(len(f3)):
#     if (sum(sp2)+f3[x])>int(n):
#         print(len(sp), f3[x-1])
#         break


f = open('27A.txt')
n = f.readline()
f = ([int(i) for i in open('27A.txt')][1:])
minproz=100000
for i in range(len(f)):
    for j in range(len(f)-1):
        if j-i>=int(n):
            minproz = min(minproz, f[j]*f[i])
print((minproz))