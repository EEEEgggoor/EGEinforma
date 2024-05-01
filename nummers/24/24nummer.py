# Текстовый файл состоит не более чем из 106 символов A, B и C. Определите максимальное количество идущих подряд символов C
# f3 = open('zadanie24_1.txt').readline()
# k = 1
# m = 0
# for i in range(1, len(f3)):
#     if f3[i] == 'C' and f3[i-1]=='C':
#         k += 1
#     else:
#         m = max(m, k)
#         k = 1
# m = max(m, k)
# print(m)


# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите максимальное количество идущих подряд символов, среди которых не более одной буквы A.
# f3 = open("24.txt")
# x = f3.read()
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


# f3 = open('24.txt').readline()
# count = count_old = m = 0
# for i in (1, len(f3)-3):
#     if (f3[i] == 'X' and f3[i+2]=='X') or (f3[i] == 'Y' and f3[i+2]=='Y'):
#         m = max(m, count + count_old + 1)
#         count_old = count
#         count = 0
#     else:
#         count += 1
# m = max(m, count + count_old + 1)
# print(m)

# Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
# f3 = open('24_demo.txt').readline()
# k = 1
# mx = -1
# for x in range(len(f3) - 1):
#     if f3[x] != f3[x + 1]:
#         k+=1
#         mx = max(k, mx)
#     else:
#         k=1
# print(mx)

# Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите длину самой длинной последовательности, состоящей из символов X. Хотя бы один символ X находится в последовательности.
# f3 = open('24_demo.txt').readline()
# k=1
# mx=-1
#
# for i in range(len(f3)-1):
#     if f3[i]==f3[i+1]=='X':
#         k+=1
#         mx = max(mx, k)
#     else:
#         k=1
#
# print(mx)


# Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите длину самой длинной последовательности, состоящей из символов Y. Хотя бы один символ Y находится в последовательности.
# f3 = open('24_demo.txt').readline()
# k=1
# mx=-1
#
# for i in range(len(f3)-1):
#     if f3[i]==f3[i+1]=='Y':
#         k+=1
#         mx=max(mx, k)
#     else:
#         k=1
# print(mx)


# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z). Определите количество строк, в которых буква E встречается чаще, чем буква A.
# f3 = open('24_24_1.txt').readlines()
# k=0
#
# for i in f3:
#     if i.count('E')>i.count("A"):
#         k+=1
# print(k)


# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле сразу после буквы E.
# from collections import Counter
# f3 = open("24 (2).txt").readline()
# a = []
# for x in range(len(f3)-1):
#     if f3[x]=='E':
#         a.append(f3[x+1])
# print(Counter(a))


# from collections import Counter
#
# f3 = open('24 (3).txt').readlines()
# a=[]
# k=0
# for i in range(len(f3)):
#     k+=1
#     for x in range(len(f3[i])):
#         a1 = []
#         a.append(f3[i][x])
#     a.append(Counter(a).most_common(-1))


# f3 = open("24-4.txt").readline()
# s=''
# a=[]
# for i in range(len(f3)-1):
#     if ord(f3[i])<ord(f3[i+1]):
#         s+=f3[i]
#         a.append(s+f3[i+1])
#     else:
#         s=''
# print(max(a, key=len), len(max(a, key=len)))


import string
a = open("C:/Users/Student/Desktop/24-274.txt").readline()
a = a.replace("PCCSGO", "6")
a = a.replace("CSGO", "4")
a = a.replace("PC", "2")
alf = string.ascii_uppercase
for l in alf:
    a = a.replace(l, " ")
print(max([sum([int(x) for x in s]) for s in a.split()]))
