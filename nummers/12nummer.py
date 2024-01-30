# s = '8' * 99 + '1'
# while ('133' in s) or ('881' in s):
#     if '133' in s:
#         s = s.replace('133', '81', 1)
#     else:
#         s = s.replace('881', '13', 1)
# print(s)

# def IsPrime(n): #функция проверки числа на простоту
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n #возвращает True если число - простое
#
# for p in range(50):
#     s = '>' + 39 * '0' + p * '1' + 39 * '2'
#     while ('>1' in s) or (">2" in s) or (">0" in s):
#         s = s.replace(">1", "22>", 1)
#         s = s.replace(">2", "2>", 1)
#         s = s.replace(">0", "1>", 1)
#     if IsPrime(s.count('1') + s.count('2')*2):
#         print(p)
#         break
