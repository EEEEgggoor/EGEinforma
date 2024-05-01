# f3 = sorted([int(x) for x in open("26_0.txt")][1:], reverse=True)
# a = f3[0]
# s = []
# s.append(a)
#
# for i in range(len(f3)):
#     if a - f3[i] >=8:
#         a = f3[i]
#         s.append(a)
# print(len(s), a)


# 10726
# f3 = open("26_1.txt")
# n = int(f3.readline())
# f3 = [list(map(int, x.split())) for x in f3]
# mn = [0] * 44641
# for i in range(n):
#    for j in range(f3[i][0], f3[i][1]):
#        mn[j] = 1
# print(sum(mn))
# f3 = ''.join(map(str, mn))
# потом как в 24, находим макс кол-во 1


# komp-ege - #12933
# f3 = open("26_2.txt")
# n, k = [int(x) for x in f3.readline().split()]
# a = []
# lenta = [0] * (n+1)
# start, end = 1, n
# for i in range(1, n + 1):
#    ts, to = [int(x) for x in f3.readline().split()]
#    a.append((ts, i, 's'))
#    a.append((to, i, 'h'))
# a.sort()
# kts = 0
# spisokocrashenihdetaley = set()
# for t, id, oper in a:
#    if id not in spisokocrashenihdetaley:
#        spisokocrashenihdetaley.add(id)
#        if oper == 's':
#            lenta[start] = id
#            start+=1
#            kts += 1
#        else:
#            lenta[end] = id
#            end -= 1
# print(kts, lenta[k])


# kompege 13101
# f3 = open('26_3.txt')
# n = f3.readline()
# k2 = 0
# okno1 = []
# okno2 = []
# kn = 0
# f3 = [tuple(map(int, x.split())) for x in f3]
#
# f3.sort()
# for st, t, o in f3:
#     okno1 = [x for x in okno1 if x > st]
#     okno2 = [x for x in okno2 if x > st]
#
#     if o == 1 or (o == 0 and len(okno1) <= len(okno2)):
#         if len(okno1) >= 14:
#             kn += 1
#             continue
#         if len(okno1) == 0:
#             okno1 += [st + t]
#         else:
#             okno1 += [max(okno1) + t]
#
#     else:
#         if len(okno2) >= 14:
#             kn += 1
#             continue
#         k2 += 1
#         if len(okno2) == 0:
#             okno2 += [st + t]
#         else:
#             okno2 += [max(okno2) + t]
#
# print(k2, kn)



# kompege12478
# f3 = open("26_4.txt")
# n = f3.readline()
# f3 = [tuple(map(int, x.split())) for x in f3]
# f3.sort()
# n = (tuple(map(int, n.split())))[1:]
# sp = []
# for i in range(len(f3)):
#     if f3[i][0]!=f3[i+1][0]:
#         sp.append(f3[i])
#         break
#
# sm=0
# mx = -100
# for i in range(len(f3)-1):
#     if f3[i][0]==sp[-1][1]:
#         for j in range(i, len(f3)):
#             if f3[j][0]!=f3[j+1][0]:
#                 sp.append(f3[j])
#                 break
#
# for i in range(len(sp)):
#     sm = f3[i][1] - f3[i][0]
#     mx = max(sm, mx)
#
#
# print(len(sp), mx)


# kompege11605
# f3 = open("26_5.txt")
# n = f3.readline()
# f3 = [tuple(map(int, x.split())) for x in f3]
# f3.sort()
# n = (tuple(map(int, n.split())))
#
#
#
# sp=[]
# sp.append(f3[0][1])
# per = f3[0][1]
#
#
# for i in range(len(f3)):
#     if f3[i][0]>per:
#         for j in range(i-1, len(f3)):
#             if f3[j][0] != f3[j + 1][0]:
#                 sp.append(f3[j])
#                 per = f3[j][1]
#                 break
#
#     if f3[i][0]==per:
#         for j in range(i, len(f3)):
#             if f3[j][0] != f3[j + 1][0]:
#                 sp.append(f3[j])
#                 per = f3[j][1]
#                 break
#
#
# print(n[1] - len(sp), len(sp))
# print(f3[:1000])
# print(sp[:100])

# temp = 25
#
# for ele in f3:
#     if ele[0] < temp:
#         temptemp = ele[0]
#     temp =temptemp


