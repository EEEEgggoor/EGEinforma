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
