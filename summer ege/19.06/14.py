s = hex(4 ** 34 + 5 * 4 ** 22 + 4 ** 13 + 2 * 4 ** 9 + 82)
k=set()
for x in s:
    k.add(x)
print(k)