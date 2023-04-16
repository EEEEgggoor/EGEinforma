# # 19 задание с одной кучей
# def f(s, c, m):
#     if s >= 129:
#         return c % 2 == m % 2
#     if c == m:
#         return 0
#     h = [f(s + 1, c + 1, m + 1), f(s * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
# for s in range(1, 128 + 1):
#     for m in range(1, 4 + 1):
#         if f(s, 0, m) == 1:
#             print(s, m)






# 19 задание с двумя кучами

# номер 27759 решу егэ
'''def f(s1, s2, c, m):
    if (s1 + s2) >= 41: return c % 2 == m % 2
    if c == m: return 0
    h = [f(s1 + 1, s2, c + 1, m), f(s1 * 2, s2, c + 1, m), f(s1, s2 + 1, c + 1, m), f(s1, s2 * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else any(h)
for s2 in range(1, 33 + 1):
    for m in range(1, 4 + 1):
        if f(8, s2, 0, m) == 1:
            print(s2, m)
            break'''






# Задача № 4827 Поляков

'''def f(s, p, c, m):
    if s >= 55: return c%2==m%2
    if c == m: return 0
    h =[]
    if p != '+1': h += [f(s+1, '+1', c+1, m)]
    if p != '+3': h += [f(s+3, '+3', c+1, m)]
    if p != '*2': h += [f(s*2, '*2', c+1, m)]
    return any(h) if (c+1)%2 == m%2 else all(h)
for s in range(1, 55):
    for m in range(1, 5):
        if f(s, '', 0, m) == 1:
            print(s, m)
            break'''






# def f(s, p0, p1, c, m):
#     if s >= 121: return c%2 == m%2
#     if c == m: return 0
#
#     h = []
#     if p1 != '+2': h += [f(s + 2, '+2', p0, c + 1, m)]
#     if p1 != '+5': h += [f(s + 5, '+5', p0, c + 1, m)]
#     if p1 != '+12': h += [f(s + 12, '+12', p0, c + 1, m)]
#     if p1 != '*2': h += [f(s * 2, '*2', p0, c + 1, m)]
#
#     return any(h) if (c+1) % 2 == m % 2 else all(h)
#
# for s in range(1, 121):
#     for m in range(1,7):
#         if f(s, '', '', 0, m) == 1:
#             if m == 3:
#                 print(s, m)
#                 break