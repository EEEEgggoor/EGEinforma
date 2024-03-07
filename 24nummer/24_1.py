# a = [x for x in open('241_1.txt')]
# max_s = 0
# for i in range(len(a)):
#     if a[i].count('G') < 25:
#         for j in range(len(a[i])-1):
#             for q in range(j+1, len(a[i])):
#                 if a[i][j] == a[i][q]:
#                     if abs(j - q) > max_s:
#                         max_s = abs(j - q)
# print(max_s)


f = open('241_2.txt').readline()
m = 0
k=0
for i in range(len(f)):
    if (f[i] == 'A' and k % 2 == 0) or (f[i] == 'B' and k % 2 == 1):
        k += 1
        m = max(m, k)
    elif f[i] == 'A':
        k = 1
    else:
        k = 0
print(m)
