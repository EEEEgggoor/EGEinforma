f = open('27-122b.txt')
n, m = map(int, f.readline().split())

a = []
sp = []

f = sorted([list(map(int, x.split())) for x in f])
for i in range(n):
    num = f[i][0]
    kount = f[i][1]
    k = kount//m if kount%m==0 else kount//m + 1
    a.append((num, k))

for i in range(n):
    punkt = a[i][0]
    sm = 0
    for j in range(n):
        sm += abs(punkt-a[j][0])*a[j][1]
    sp.append(sm)
print(min(sp))
