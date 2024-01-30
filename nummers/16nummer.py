def f(n):
    if n == 0: return 0
    if n % 2 == 0 and n > 0: return f(n / 2)
    if n % 2 == 1 and n > 0: return 1 + f(n - 1)


k = 0
for x in range(1, 501):
    if f(x) == 8:
        k += 1
print(k)
