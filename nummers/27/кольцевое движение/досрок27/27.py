f = open('27A_15342.txt')
n, m = map(int, f.readline().split())
a = []
sp = []
for i in range(n):
    num, kount = (map(int, f.readline().split()))
    k = kount//11 if kount%11==0 else kount//11+1
    a.append((num, k))
for i in range(n):
    benz = a[i][0]
    sm = 0
    for j in range(n):
        sm+=(min(abs(benz - a[j][0]), m-abs(benz - a[j][0])))*a[j][1]
    sp.append(sm)
print(min(sp))
