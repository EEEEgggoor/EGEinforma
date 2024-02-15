# f = sorted([int(x) for x in open("26_0.txt")][1:], reverse=True)
# a = f[0]
# s = []
# s.append(a)
#
# for i in range(len(f)):
#     if a - f[i] >=8:
#         a = f[i]
#         s.append(a)
# print(len(s), a)


# 10726
# f = open("26_1.txt")
# n = int(f.readline())
# f = [list(map(int, x.split())) for x in f]
# mn = [0] * 44641
# for i in range(n):
#    for j in range(f[i][0], f[i][1]):
#        mn[j] = 1
# print(sum(mn))
# f = ''.join(map(str, mn))
# потом как в 24, находим макс кол-во 1


# komp-ege - #12933
#f = open("26_2.txt")
#n, k = [int(x) for x in f.readline().split()]
#a = []
#lenta = [0] * (n+1)
#start, end = 1, n
#for i in range(1, n + 1):
#    ts, to = [int(x) for x in f.readline().split()]
#    a.append((ts, i, 's'))
#    a.append((to, i, 'h'))
#a.sort()
#kts = 0
#spisokocrashenihdetaley = set()
#for t, id, oper in a:
#    if id not in spisokocrashenihdetaley:
#        spisokocrashenihdetaley.add(id)
#        if oper == 's':
#            lenta[start] = id
#            start+=1
#            kts += 1
#        else:
#            lenta[end] = id
#            end -= 1
#print(kts, lenta[k])


#kompege 13101
f = open('26_3.txt')
n = f.readline()
k2 = 0
kn = 0
f = [tuple(map(int, x.split())) for x in f]

f.sort()
for st, t, o in f:
    okno1 = [x for x in okno1 if x>st]
    okno2 = [x for x in okno2 if x>st]

    if o==1 or (o==0 and len(okno1)<=len(okno2)):
        if len(okno1)>=14:
            kn+=1
            continue

