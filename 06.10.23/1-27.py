# def f(x, y, z, w):
#     return (x or (not y)) and (not x == z) and w
#
#
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if f(x, y, z, w):
#                     print(x, y, z, w)


# def f(n, c):
#     s=''
#     while n!=0:
#         s += str(n%c)
#         n = n//c
#     return s[::-1]
#
# for N in range(1, 1000):
#     n6 = f(N, 6)
#     if N%3==0:
#         n6 = n6+n6[:2]
#     else:
#         n6 = n6 + f(((N%3)*10), 6)
#     if int(n6, 6)>680:
#         print(int(n6, 6))


# alf = 'ЕКМОПРТЬЮ'
# k=0
# for x in alf:
#     for x1 in alf:
#         for x2 in alf:
#             for x3 in alf:
#                 for x4 in alf:
#                     X = x+x1+x2+x3+x4
#                     k+=1
#                     if k%2!=0 and x!='Ь' and 'К'*2 in X:
#                         print(k, X)

# s1=[]
# for n in range(3, 1001):
#     s = '1' + '2'*n
#     while '12' in s or '322' in s or '222' in s:
#         s = s.replace('12', '2', 1)
#         s = s.replace('322', '21', 1)
#         s = s.replace('222', '3', 1)
#     s1.append(len(s))
# print(max(s1))
