# # 19 задание с одной кучей
's - кол-во камней'
'm  -пороговое значение'
#если петя делает первый ход, то чётное m - ход вани, нечётное - пети

# функция проверяет, монжно ли выйграть за m ходов
def f(s, m):
    if s>=65: return m%2==0
    if m==0: return 0
    h = [f(s+1, m-1), f(s*2, m-1)]
    return any(h) if (m-1)%2==0 else all(h)


print('19)', [s for s in range(1, 65) if f(s, 2)])
print('20)', [s for s in range(1, 65) if f(s, 3)])
print('21)', [s for s in range(1, 65) if f(s, 4)])


# 19 задание с двумя кучами - 27786
def f(s1, s2, m):
    if s1 + s2 >= 86: return m % 2 == 0
    if m == 0: return 0
    h = [f(s1 + 1, s2, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1)]
    return any(h) if (m-1)%2==0 else all(h)

print('19)', [s for s in range(1, 71) if f(14, s, 2)])
print('20)', [s for s in range(1, 71) if f(14, s, 3)])
print('21)', [s for s in range(1, 71) if f(14, s, 4)])
