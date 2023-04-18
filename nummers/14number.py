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