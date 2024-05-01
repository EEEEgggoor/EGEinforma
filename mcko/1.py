#      №1
# print(hex(int(int('1011', 2) + 0.25 + int('24', 8) + 6 * 0.125)))


#      №2
# def f3(a, b, c):
#     return a or not b and c
#
#
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             print(a, b, c, int(f3(a, b, c)))


#       №5
# for N in range(1,1001):
#     n2 = bin(N)[2:]
#     if N%2==0:
#         n2 = n2 + '10'
#     else:
#         n2 = n2 + '11'
#     if n2.count('1')%2==0:
#         n2 = n2 + n2[-1]
#     else:
#         n2 = n2 + n2[-2]
#     if int(n2, 2) > 44:
#         print(N, int(n2, 2))
#         break


#       №8
# p=5
# q=7
# e=11
# for d in range(40):
#     f3 = (p-1)*(q-1)
#     if (d*e)%f3==1:
#         print(d)


#       №10
# print((~18|(132>>2))&(86<<1))


#       №11
# def f3(c, e):
#     if c > e or c == 32: return 0
#     if c == e: return 1
#     if c < e: return f3(c + 3, e) + f3(c + 4, e) + f3(c * 3, e)
#
#
# print(f3(4, 16) * f3(16, 46))


#       №13
# ans=[]
# l = [int(i) for i in open('13.txt')]
# for i in range(len(l)-1):
#     if l[i]%8==0 and l[i+1]%8==0:
#         ans.append(l[i]+l[i+1])
# print(len(ans), min(ans))


#       №5