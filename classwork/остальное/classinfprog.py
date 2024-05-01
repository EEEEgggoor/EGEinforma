# Решу егэ №17 - 37348:
# ans = []
# l = [int(i) for i in open('17.txt')]
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if (l[i]*l[j]) % 34 !=0:
#             ans.append(l[i]+l[j])
# print(len(ans), max(ans))


# Решу егэ №17 - 37340
# ans = []
# l = [int(i) for i in open('17_1.txt')]
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if (l[i] - l[j]) % 2 == 0 and (l[i] % 31 == 0 or l[j] % 31 == 0):
#             ans.append(l[i] + l[j])
# print(len(ans), max(ans))


# Решу егэ №17 - 37337
# ans = []
# l = [int(i) for i in open('17_2.txt')]
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if (l[i] % 160 != l[j] % 160) and (l[i] % 7 == 0 or l[j] % 7 == 0):
#             ans.append(l[i] + l[j])
# print(len(ans), max(ans))


# # Решу егэ №17 - 48465
# l = [int(i) for i in open('17_3.txt')]
# ans = []
# # поиск минимального числа, оканчивающегося на 6
# min6 = 10001
# for i in range(len(l)):
#     if str(l[i])[-1] == '6':
#         min6 = min(min6, l[i])
# # пары
# for i in range(len(l)-1):
#     if ((str(l[i])[-1]=='6' and str(l[i+1])[-1] != '6') or (str(l[i])[-1]!='6' and str(l[i+1])[-1] == '6')) and ((l[i]**2 + l[i+1]**2)< min6**2):
#         ans.append((l[i]**2 + l[i+1]**2))
# print(len(ans), max(ans))


# Реуш егэ №17 - 472213
# l = [int(i) for i in open('17_4.txt')]
# ans = []
# max3 = -10001
# for i in range(len(l)):
#     if str(l[i])[-1] == '3':
#         max3 = max(max3, l[i])
# for i in range(len(l)-1):
#     if ((str(l[i])[-1]=='3' and str(l[i+1])[-1] != '3') or (str(l[i])[-1]!='3' and str(l[i+1])[-1] == '3')) and ((l[i]**2 + l[i+1]**2) >= max3**2):
#         ans.append((l[i]**2 + l[i+1]**2))
# print(len(ans), max(ans))


# Поляков №17 - 4496
# l = [int(i) for i in open('17-205.txt')]
# ans = []
# for i in range(len(l)-1):
#     if (l[i]-l[i+1])%2==0 and (l[i]-l[i+1])%37==0:
#         ans.append(l[i] + l[i+1])
# print(len(ans), max(ans))


#Самостоятельная работа 21.04.23
#1)
# f3 = open('24_1.txt').readline()
# k = 1
# m = 0
# for i in range(1, len(f3)):
#     if f3[i] == 'B' and f3[i-1]=='B':
#         k += 1
#     else:
#         m = max(m, k)
#         k = 1
# m = max(m, k)
# print(m)
#2)
# f3 = open("24_3.txt")
# x = f3.read()
# count = count_old = m = 0
# for i in x:
# 	if i == "D":
# 		m = max(m, count + count_old + 1)
# 		count_old = count
# 		count = 0
# 	else:
#                 count += 1
# m = max(m, count + count_old + 1)
# print(m)




#3)
# f3 = open("24_1.txt")
# x = f3.read()
# count = count_old = m = 0
# for i in x:
# 	if i == "D":
# 		m = max(m, count + count_old + 1)
# 		count_old = count
# 		count = 0
# 	else:
#                 count += 1
# m = max(m, count + count_old + 1)
# print(m)



#Поляков №25 - 5378
# from fnmatch import *
# for i in range(0, 10**8, 161):
#     if fnmatch(str(i), '12*4?65'):
#         print(i, i//161)


