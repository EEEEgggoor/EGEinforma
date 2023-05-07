# Текстовый файл состоит не более чем из 106 символов A, B и C. Определите максимальное количество идущих подряд символов C
# f = open('zadanie24_1.txt').readline()
# k = 1
# m = 0
# for i in range(1, len(f)):
#     if f[i] == 'C' and f[i-1]=='C':
#         k += 1
#     else:
#         m = max(m, k)
#         k = 1
# m = max(m, k)
# print(m)


# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите максимальное количество идущих подряд символов, среди которых не более одной буквы A.
# f = open("24.txt")
# x = f.read()
# count = count_old = m = 0
# for i in x:
# 	if i == "A":
# 		m = max(m, count + count_old + 1)
# 		count_old = count
# 		count = 0
# 	else:
#                 count += 1
# m = max(m, count + count_old + 1)
# print(m)


# f = open('24.txt').readline()
# count = count_old = m = 0
# for i in (1, len(f)-3):
#     if (f[i] == 'X' and f[i+2]=='X') or (f[i] == 'Y' and f[i+2]=='Y'):
#         m = max(m, count + count_old + 1)
#         count_old = count
#         count = 0
#     else:
#         count += 1
# m = max(m, count + count_old + 1)
# print(m)
