# f = open("24.txt").read()
# count = count_old = m = 0
# for i in f:
#     if i == "A":
#         m = max(m, count + count_old + 1)
#         count_old = count
#         count = 0
#     else:
#         count += 1
# m = max(m, count + count_old + 1)
# print(m)


# def f(n):
#     d = set()
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             d.add(i)
#             d.add(n // i)
#
#     return sorted(d)
#
#
# s=[]
# for i in range(84052, 84130):
#     s1 = []
#     s1.append(len(f(i)))
#     s1.append(i)
#     s.append(s1)
# print(sorted(s)[-1])

# s = []
# f = [int(x) for x in open('26.txt')][1:]
# for i in range(0, len(f)):
#     for j in range(i, len(f)-1):
#         if (f[i] + f[j] in f) and f[i] % 2 != f[j] % 2:
#             s.append(f[i] + f[j])
# print(len(s), max(s))


f = open('27-A.txt').readlines()
k = 0
for i in range(0, len(f)):
    for j in range(i, len(f)):
        if j - i + 1 >= 14:
            if (int(f[i]) + int(f[j])) % 8 == 0 and (int(f[i]) * int(f[j])) % 19683 == 0:
                k += 1

print(k)
