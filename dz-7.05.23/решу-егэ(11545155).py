# номер-2
# def f(x, y, z, w):
#     return (not x or y or z)==(not y and z and w)
#
#
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if f(x, y, z, w)==1:
#                     print(x, y, z, w)


# номер-5
# for N in range(256):
#     s = bin(N)[2:]
#     if len(s) < 8:
#         s = '0' * (8 - len(s)) + s
#     s = s.replace('1', '*')
#     s = s.replace('0', '1')
#     s = s.replace('*', '0')
#     r = int(s, 2)
#     if r - N == 133:
#         print(N)


# номер-8
# alf='abcdefx'
# k=0
# for x1 in alf:
#     for x2 in alf:
#         for x3 in alf:
#             for x4 in alf:
#                 sl = x1+x2+x3+x4
#                 if sl.count('x')==1:
#                     k+=1
#                     print(sl, k)


# номер-12
# s = 68 * '8'
# while '222' in s or '888' in s:
#     s = s.replace('222', '8', 1)
#     s = s.replace('888', '2', 1)
# print(s)


# номер-14
# print(bin(4**16 + 2**36 - 16)[2:].count('1'))


# номер-15
# def f(x, a):
#     return (x & a != 0) <= ((x & 36 == 0) <= (x & 6 != 0))
#
#
# for a in range(0, 1001):
#     fl = True
#     for x in range(0, 1001):
#         if f(x, a)==0:
#             fl = False
#             break
#     if fl:
#         print(a)


# номер-16
# def f(n):
#     if n<=2: return n+1
#     if n>2: return f(n-1) * f(n-2)
#
# print(f(4))


# номер-17
# ans=[]
# m=0
# l = [int(i) for i in open('17.txt')]
# for i in range(len(l)-1):
#     for j in range(i+1, len(l)):
#         if (l[i]*l[j])%34!=0:
#             ans.append(l[i]+l[j])
#
# print(len(ans), max(ans))


# номер-19 20 21
# def f(s, m):
#     if s>=65: return m%2==0
#     if m==0: return 0
#     h = [f(s+1, m-1), f(s*2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
#
# print('19)', [s for s in range(1, 65) if f(s, 2)])
# print('20)', [s for s in range(1, 65) if f(s, 3)])
# print('21)', [s for s in range(1, 65) if f(s, 4)])


# номер-23
# def F(s, f):
#     if s>f or s==12: return 0
#     if s==f: return 1
#     if s<f: return F(s+1, f) + F(s+3, f)
#
# print(F(1, 10) + F(10, 15))


# номер-24
# k=1
# n=0
# l = open("24.txt").readline()
# for i in range(1, len(l)):
#     if (l[i]=='K' and l[i-1]=='L') or (l[i]=='L' and l[i-1]=='K'):
#         k=1
#     else:
#         k+=1
#         if k>n:
#             n=k
# print(n)


# номер 25
# def div(n):
#     s = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             s.add(i)
#             s.add(n // i)
#     return sorted(s)
#
#
# def m(n):
#     if len(n) >= 5:
#         return sorted(n)[0] * sorted(n)[1] * sorted(n)[2] * sorted(n)[3] * sorted(n)[4]
#     if len(n) < 5:
#         return 0
#
#
# k = 0
# for n in range(200_000_000, 1 * 10 ** 9):
#     if len(div(n)) >= 5:
#         if 0 < m(div(n)) < n:
#             k += 1
#             print(m(div(n)))
#             if k == 6:
#                 break


#номер-26
summ=0
k=0
sp=[]
with open('26.txt') as f:
    s = [x for x in f]
    st = int(s[0][:5])
    s = [int(x) for x in s[1:]]
    s = sorted(s, reverse=False)
    for i in range(1, len(s)):
        summ +=s[i]
        if summ<st:
            k+=1
            sp.append(s[i])

print(len(sp), sum(sp), max(sp))




