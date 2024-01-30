# x = 5 ** 36 + 5 ** 24 - 25
# s = ''
# while x != 0:
#     s += str(x % 5)
#     x //= 5
# s = s[::-1]
# print(s.count("4"))

# result_search = []
# for x in '0123456789A':
#     for y in '0123456789A':
#         t = int(x + '341' + y, 11) + int('56' + x + '1' + y, 19)
#         if t % 305 == 0:
#             result_search.append(t)
# if result_search:
#     print(min(result_search) // 305)

x = 6 * 343 ** 1156 - 5 * 49 ** 1147 + 4 * 7 ** 1153 - 875
s = ''
while x != 0:
    s += str(x % 7)
    x //= 7
s = s[::-1]
print(s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6)
