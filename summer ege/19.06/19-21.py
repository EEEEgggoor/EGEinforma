def f(s1, s2, m):
    if s1 + s2 >= 86: return m % 2 == 0
    if m == 0: return 0
    h = [f(s1 + 1, s2, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1)]
    return any(h) if (m-1)%2==0 else all(h)

print('19)', [s for s in range(1, 71) if f(14, s, 2)])
print('20)', [s for s in range(1, 71) if f(14, s, 3)])
print('21)', [s for s in range(1, 71) if f(14, s, 4)])