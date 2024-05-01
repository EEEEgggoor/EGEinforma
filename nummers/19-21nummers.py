# # 19 задание с одной кучей
's - кол-во камней'
'm  -пороговое значение'


# если петя делает первый ход, то чётное m - ход вани, нечётное - пети

# функция проверяет, монжно ли выйграть за m ходов
# def f3(s, m):
#     if s >= 65: return m % 2 == 0
#     if m == 0: return 0
#     h = [f3(s + 1, m - 1), f3(s * 2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h) #<-- тут any если в 19 сказано "после НЕУДАЧНОГО",
#                                                        #а на 20 и 21 возвращаем all
# Если формулировка 19 номера такая ->"Известно, что Ваня выиграл своим первым ходом после первого хода Пети.
# Назовите минимальное значение S, при котором это возможно.", то для него all меняем на any, для 20 и 21 возвращаем all
#
#
# print('19)', [s for s in range(1, 65) if f3(s, 2)])
# print('20)', [s for s in range(1, 65) if f3(s, 3)])
# print('21)', [s for s in range(1, 65) if f3(s, 4)])
#
#
# # 19 задание с двумя кучами - 27786
# def f3(s1, s2, m):
#     if s1 + s2 >= 86: return m % 2 == 0
#     if m == 0: return 0
#     h = [f3(s1 + 1, s2, m - 1), f3(s1 * 2, s2, m - 1), f3(s1, s2 + 1, m - 1), f3(s1, s2 * 2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h) #<-- тут any если в 19 сказано "после НЕУДАЧНОГО",
# #                                                        #а на 20 и 21 возвращаем all
#
#
# print('19)', [s for s in range(1, 71) if f3(14, s, 2)])
# print('20)', [s for s in range(1, 71) if f3(14, s, 3)])
# print('21)', [s for s in range(1, 71) if f3(14, s, 4)])


# 6833
# def f3(s, m):
#     if s >= 37: return m % 2 == 0
#     if m == 0: return 0
#     h = [f3(s + 1, m - 1), f3(s + 2, m - 1), f3(s * 3, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 37) if f3(s, 2) and f3(s, 1)==0])
# print('20)', [s for s in range(1, 37) if f3(s, 3) and f3(s, 1)==0])
# print('21)', [s for s in range(1, 37) if f3(s, 4) and f3(s, 2)==0])


# 4107
# def f3(s, m):
#     if 25 <= s <= 45: return m % 2 == 0
#     if s > 45: return m % 2 != 0
#     if m == 0: return 0
#     h = [f3(s + 1, m - 1), f3(s * 2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(1, 25) if f3(s, 2) and f3(s, 1) == 0])
# print('20)', [s for s in range(1, 25) if f3(s, 3) and f3(s, 1) == 0])
# print('21)', [s for s in range(1, 25) if f3(s, 4) and f3(s, 2) == 0])


# 4032
# def f3(s1, s2, m):
#     if s1 + s2 >= 70: return m % 2 == 0
#     if m == 0: return 0
#     h = [f3(s1 + 1, s2, m - 1), f3(s1 * 3, s2, m - 1),
#          f3(s1, s2 + 1, m - 1), f3(s1, s2 * 3, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19', [s for s in range(1, 63) if f3(6, s, 2)])
# print('20', [s for s in range(1, 63) if f3(6, s, 3) and not f3(6, s, 1)])
# print('21', [s for s in range(1, 63) if f3(6, s, 4)])


# 6603
# не говнокод
# def f3(s, m):
#     if s==0: return m%2==0
#     if m==0: return 0
#     if s>=5: h = [f3(s-5, m-1), f3(s//3, m-1)]
#     else: h = [f3(s//3, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
# print("19)", [s for s in range(1, 150) if f3(s, 2)])
# print("20)", [s for s in range(1, 150) if f3(s, 3) and not f3(s, 1)])
# print("21)", [s for s in range(1, 150) if f3(s, 4) and not f3(s, 2)])


# 4830 - не повторять ход противика
# def f3(s, m, p):
#     if s >= 62: return m % 2 == 0
#     if m == 0: return 0
#     h = []
#     if p != '+1': h += [f3(s + 1, m - 1, '+1')]
#     if p != '+2': h += [f3(s + 2, m - 1, '+2')]
#     if p != '*3': h += [f3(s * 3, m - 1, '*3')]
#     return any(h) if (m-1)%2==0 else all(h)
#
# print("19)", [s for s in range(1, 62) if f3(s, 2, '')])
# print("20)", [s for s in range(1, 62) if f3(s, 3, '') and not f3(s, 1, '')])
# print("21)", [s for s in range(1, 62) if f3(s, 4, '') and not f3(s, 2, '')])


# 4181
# def f3(p1, p2, m):
#     if p1+p2>=45: return m%2==0
#     if m==0: return 0
#     h = [f3(p1+(p2), p2, m-1), f3(p1, p2+(p1), m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
#
# print("20)", [p for p in range(1, 45) if f3(6, p, 3) and not f3(6, p, 1)])
# print("21)", [p for p in range(1, 6) if f3(p, p, 4)])


# 3344
def f(s1, s2, m):
    if s1 + s2 >= 30: return m%2==0
    if m==0: return 0
    h = [f(s1+1, s2, m-1), f(s1*2, s2, m-1),
         f(s1, s2+1, m-1), f(s1, s2*2, m-1)]
    return any(h) if (m-1)%2==0 else all(h)


n19 = []
for s1 in range(1, 29):
    for s2 in range(1, 29):
        if f(s1, s2, 2) and s1+s2<30:
            n19.append([s1, s2])
print("19)",len(n19))

print('20)', [s for s in range(1, 29) if f(6, s, 3) and not f(6, s, 1)])


n21 = []
for s1 in range(1, 29):
    for s2 in range(1, 29):
        if f(s1, s2, 4) and not f(s1, s2, 2) and s1+s2<30:
            n21.append([s1, s2])
print("21)", len(n21))



