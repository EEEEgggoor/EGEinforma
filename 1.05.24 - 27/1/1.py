f = open('27A_1.txt')
n = int(f.readline())
k = int(f.readline())
f = [int(x) for x in f]
sp = []
for i in range(n):
    for j in range(i, n):
        s = f[i] + f[j]
        if j - i >= k and s % 2023 == 0 and (f[i] % 47 == 0 or f[j] % 47 == 0):
            sp.append(f[i] + f[j])
print(max(sp))
