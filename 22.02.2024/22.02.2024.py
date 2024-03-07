# def f(x, y, z, w):
#     return ((x <= y ) == (z <= w)) or (x and w)
#
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if f(x, y, z, w)==0:
#                     print(x, y, z, w)


# from itertools import*
# a = [0]
# for i in product('ВИНТ', repeat=5):
#     a.append("".join(i))
# print(a[1019])


# f = sorted([int(x) for x in open('26.txt')][1:], reverse=True)
# a = [f[0]]
# for i in f[1:]:
#     if a[-1] - i >= 3:
#         a.append(i)
# print(len(a), a[-1])


f = [int(x) for x in open("27-A.txt")]
k=0
for i in range(len(f)-2):
    for j in range(len(f)-1):
        for n in range(len(f)):
            s = (f[i]+f[j]+f[n])
            if s%3==0:
                k+=1
print(k)