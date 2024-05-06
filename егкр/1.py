f = open("27_A.txt")
n = int(f.readline())
f = [int(x) for x in f]
sm = []
for i in range(n):
    s = 0
    k = 0
    for j in range(i, n):
        k += 1
        s += f[j]
        if s % 137 == 0:
            sm.append((s, k))

print(max(sm))