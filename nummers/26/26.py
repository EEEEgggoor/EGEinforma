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
f = open("26_1.txt")
n = int(f.readline())
f = [list(map(int, x.split())) for x in f]
mn = [0] * 44641
for i in range(n):
    for j in range(f[i][0], f[i][1]):
        mn[j] = 1
print(sum(mn))


f = ''.join(map(str, mn))
# потом как в 24, находим макс кол-во 1